"""Compose independently runnable lab methods without changing surrounding Markdown.

python scripts/complete-data-lab-code.py --check --output-dir qa/data-labs/completed-code

The registry is deliberately explicit. AST is used to select named definitions or
fixture statements, never to replay preceding exercises or guess file producers.
--write is opt-in and is performed only after every composed program passes.
"""
from __future__ import annotations

import argparse
import ast
import builtins
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import symtable
import tempfile


ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "raw_materials/xu-ly-du-lieu/labs"
START = "# Bắt đầu lời giải"
END = "# Kết thúc lời giải"
GENERATED = "# Dữ liệu mẫu và các hàm hỗ trợ"
FENCES = re.compile(
    r"^(?P<fence>`{3,}|~{3,})python[^\r\n]*\r?\n"
    r"(?P<code>.*?)^(?P=fence)[ \t]*(?=\r?$)", re.M | re.S,
)
SPAN = re.compile(r'<span\s+id=[\"\'](data-lab-[^\"\']+)[\"\']')
WAY = re.compile(r"^#{3,5}\s+Cách ([12])\b", re.M)


class CompositionError(ValueError):
    pass


def original_code(code: str) -> str:
    """Recover the authored body, so composition remains idempotent."""
    if not code.startswith(GENERATED):
        return code
    if code.count(START) != 1 or code.count(END) != 1:
        raise CompositionError("Malformed completion markers; review the method manually")
    return code.split(START, 1)[1].split(END, 1)[0].lstrip("\r\n")


@dataclass(frozen=True)
class Method:
    exercise: str
    way: int
    start: int
    end: int
    code: str
    line: int

    @property
    def key(self):
        return self.exercise, self.way


def extract_methods(text: str) -> list[Method]:
    """Recognize spans/headings only outside fences and inside solutions."""
    fences = list(FENCES.finditer(text))
    fence_at = {match.start(): match for match in fences}
    # Skip all fenced languages while reading structural Markdown events.
    opening = re.compile(r"^(`{3,}|~{3,})[^\r\n]*\r?$", re.M)
    exercise = None
    way = None
    containers: list[str] = []
    methods = []
    position = 0
    lines = text.splitlines(keepends=True)
    index = 0
    while index < len(lines):
        line = lines[index]
        opened = opening.fullmatch(line.rstrip("\n"))
        if opened:
            fence = opened.group(1)
            found = fence_at.get(position)
            if found and exercise and way and "solution" in containers:
                methods.append(Method(exercise, way, found.start("code"),
                                      found.end("code"), original_code(found.group("code")), index + 2))
            position += len(line)
            index += 1
            while index < len(lines):
                closing = lines[index].strip()
                done = (len(closing) >= len(fence) and
                        closing and set(closing) == {fence[0]})
                position += len(lines[index])
                index += 1
                if done:
                    break
            continue
        span = SPAN.search(line)
        if span:
            exercise = span.group(1)
            way = None
        stripped = line.strip()
        if stripped == ":::" and containers:
            closed = containers.pop()
            if closed == "solution":
                way = None
        elif stripped.startswith("::: "):
            containers.append(stripped[4:].split()[0])
        heading = WAY.match(line)
        if heading and "solution" in containers:
            way = int(heading.group(1))
        position += len(line)
        index += 1
    keys = [method.key for method in methods]
    if len(set(keys)) != len(keys):
        raise CompositionError("Multiple Python fences for one method; configure their layout explicitly")
    return methods


def external_names(code: str) -> set[str]:
    """Audit global names, including names referenced inside nested functions."""
    table = symtable.symtable(code, "<method>", "exec")
    def referenced(scope):
        names = {symbol.get_name() for symbol in scope.get_symbols()
                 if symbol.is_global() and symbol.is_referenced()}
        for child in scope.get_children():
            names.update(referenced(child))
        return names
    defined = {symbol.get_name() for symbol in table.get_symbols()
               if symbol.is_assigned() or symbol.is_imported() or symbol.is_namespace()}
    return referenced(table) - defined - set(dir(builtins)) - {"__name__", "__file__"}


def statement_names(node: ast.AST) -> set[str]:
    return {child.id for child in ast.walk(node)
            if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Store)}


@dataclass(frozen=True)
class Select:
    """Select only named top-level statements from one explicit source block."""
    names: tuple[str, ...]
    exercise: str | None = None
    way: int = 1
    functions: bool = False
    mutations: tuple[str, ...] = ()


@dataclass(frozen=True)
class Asset:
    dependencies: tuple[str, ...] = ()
    selections: tuple[Select, ...] = ()
    code: str = ""


@dataclass(frozen=True)
class Plan:
    assets: tuple[str, ...] = ()
    output: str = ""


class Source:
    def __init__(self, text: str):
        self.text = text
        self.methods = extract_methods(text)
        self.by_key = {method.key: method for method in self.methods}
        first_span = SPAN.search(text)
        before = text[:first_span.start()] if first_span else text
        self.setup = "\n\n".join(match.group("code") for match in FENCES.finditer(before))
        self.imports: dict[str, str] = {"display": "from IPython.display import display"}
        for match in FENCES.finditer(text):
            code = original_code(match.group("code"))
            for node in ast.parse(code).body:
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    statement = ast.get_source_segment(code, node)
                    for alias in node.names:
                        name = alias.asname or (alias.name.split(".")[0] if isinstance(node, ast.Import) else alias.name)
                        self.imports.setdefault(name, statement)

    def select(self, selection: Select) -> str:
        if selection.exercise is None:
            code = self.setup
        else:
            method = self.by_key.get((selection.exercise, selection.way))
            if method is None:
                raise CompositionError(f"Missing helper source {selection.exercise}/method-{selection.way}")
            code = method.code
        tree = ast.parse(code)
        selected, found = [], set()
        for node in tree.body:
            if selection.functions:
                take = isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name in selection.names
                if take:
                    found.add(node.name)
            else:
                # A compound fixture loop is allowed only when the registry names
                # the mutated root. No arbitrary expression or demo call is copied.
                assigned = statement_names(node) if not isinstance(node, (ast.FunctionDef, ast.ClassDef)) else set()
                take = bool(assigned.intersection(selection.names))
                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                    root = node.value.func
                    while isinstance(root, (ast.Attribute, ast.Subscript)):
                        root = root.value
                    take = isinstance(root, ast.Name) and root.id in selection.mutations
                if isinstance(node, (ast.For, ast.While)) and selection.mutations:
                    for call in (child for child in ast.walk(node) if isinstance(child, ast.Call)):
                        root = call.func
                        while isinstance(root, (ast.Attribute, ast.Subscript)):
                            root = root.value
                        if isinstance(root, ast.Name) and root.id in selection.mutations:
                            take = True
                if take:
                    found.update(assigned.intersection(selection.names))
            if take:
                selected.append(ast.get_source_segment(code, node))
        missing = set(selection.names) - found
        if missing:
            raise CompositionError(f"Missing registered definitions {sorted(missing)} in {selection.exercise or 'setup'}")
        return "\n\n".join(selected)


# Assets below are local to one lab prefix. Helper references identify the exact
# exercise and method version, rather than the last function of the same name.
ASSETS: dict[str, Asset] = {}
REGISTRY: dict[tuple[str, int], Plan] = {}


def asset(name, dependencies=(), selections=(), code=""):
    ASSETS[name] = Asset(tuple(dependencies), tuple(selections), code)


def setup(*names, mutations=()):
    return Select(tuple(names), mutations=tuple(mutations))


def helper(exercise, *names, way=1):
    return Select(tuple(names), exercise, way, functions=True)


def assignment(exercise, *names, way=1):
    return Select(tuple(names), exercise, way)


def plan(lab, exercises, *assets, way=None, output=""):
    for number in exercises:
        for method in ((way,) if way else (1, 2)):
            REGISTRY[(f"data-lab-{lab}-{number:02d}", method)] = Plan(tuple(assets), output)


def build_registry():
    # Every present core exercise has a deliberate entry, even when already independent.
    for lab, count in {"01": 7, "02": 15, "03": 8, "04": 12,
                       "05": 10, "06": 12, "07": 15, "08": 14}.items():
        plan(lab, range(1, count + 1))
    asset("01.csv", selections=[setup("DEMO_CSV")])
    asset("01.table", ["01.csv"], code="from io import StringIO\nimport pandas as pd\nds = pd.read_csv(StringIO(DEMO_CSV))")
    asset("01.counts", ["01.table"], code='dem_loai = ds["room_type"].value_counts()')
    plan("01", [3, 6, 7], "01.table")
    plan("01", [4, 5], "01.counts")
    plan("01", [5], "01.counts", way=1, output="plt.show()")
    plan("01", [5], "01.counts", way=2, output="plt.show()")

    asset("02.csv", selections=[setup("DEMO_CSV")])
    asset("02.file", ["02.csv"], code='from pathlib import Path\nPath("listings.csv").write_text(DEMO_CSV, encoding="utf-8")')
    asset("02.rows", ["02.csv"], code="import csv\nfrom io import StringIO\nrows = list(csv.DictReader(StringIO(DEMO_CSV)))")
    asset("02.float", selections=[helper("data-lab-02-05", "to_float", way=2)])
    asset("02.prices", ["02.rows", "02.float"], code='gia = [to_float(row["price"]) for row in rows]')
    asset("02.records", ["02.rows", "02.float"], selections=[assignment("data-lab-02-08", "phong_co_gia_so")])
    asset("02.median", selections=[helper("data-lab-02-07", "trung_vi")])
    asset("02.report", ["02.prices", "02.records", "02.median"], selections=[
        helper("data-lab-02-07", "summarize_prices"),
        helper("data-lab-02-08", "most_expensive"),
        helper("data-lab-02-10", "median_by_area"),
        helper("data-lab-02-11", "review_qa"),
    ], code='''tom_tat_gia_c1 = summarize_prices(gia)
id_dat_nhat_c1 = most_expensive(phong_co_gia_so)
trung_vi_khu_c1 = median_by_area(phong_co_gia_so)
ket_qua_qa_c1 = review_qa(rows)''')
    asset("02.report-input", ["02.report"], selections=[assignment("data-lab-02-12", "bao_cao_tong_hop")])
    asset("02.review-sample", selections=[assignment("data-lab-02-14", "mau_danh_gia")])
    plan("02", [4], "02.file")
    plan("02", [6], "02.prices")
    plan("02", [7], "02.prices")
    plan("02", [8, 10, 13], "02.records", "02.median")
    plan("02", [9, 11], "02.rows")
    plan("02", [12], "02.report")
    plan("02", [12], "02.report-input", way=2)
    plan("02", [14], "02.review-sample", way=2)

    asset("03.A", selections=[setup("A")])
    asset("03.vectors", selections=[assignment("data-lab-03-05", "b", "d")])
    asset("03.row-prices", selections=[assignment("data-lab-03-06", "gia")])
    asset("03.nightly-prices", selections=[assignment("data-lab-03-08", "gia_dem")])
    plan("03", range(1, 6), "03.A")
    plan("03", [5], "03.A", "03.vectors", way=2)
    plan("03", [6], "03.row-prices", way=2)
    plan("03", [8], "03.nightly-prices", way=2)
    for number, output in {
        1: 'print({"shape": shape_a, "itemsize": byte_moi_so, "nbytes": byte_du_lieu, "strides": buoc, "offset": offset, "int32_nbytes": byte_du_lieu_32, "int32_strides": buoc_32})',
        2: 'print("View:", V)\nprint("Offset:", offset_v11)\nprint("Shared memory:", dung_chung)',
        3: 'print("Original:", A)\nprint("View parent:", B)\nprint("Fancy-index copy:", C)\nprint("Explicit copy:", D)',
        4: 'print("Paired selection:", hai_o)\nprint("Cartesian selection:", bon_o)',
        6: 'print("Row means:", trung_binh_hang)\nprint("Centered values:", chenh_lech)',
        8: 'print({"mean": trung_binh, "median": trung_vi, "std": do_lech_chuan, "share": ty_le, "indices": chi_muc, "sample": mau, "sample_mean": tb_mau})',
    }.items():
        previous = REGISTRY[(f"data-lab-03-{number:02d}", 1)]
        plan("03", [number], *previous.assets, way=1, output=output)

    asset("04.table", selections=[setup("DEMO")])
    asset("04.district", ["04.table"], selections=[setup("ds_quan")])
    plan("04", range(1, 13), "04.table")
    plan("04", range(4, 10), "04.district")

    asset("05.series", selections=[setup("s_demo")])
    asset("05.surveys", selections=[setup("gia_cu", "gia_moi")])
    asset("05.table", selections=[setup("DEMO")])
    asset("05.segmented", ["05.table"], selections=[Select(("phan_khuc_gia",), functions=True)],
          code='DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)')
    asset("05.pivot-input", ["05.segmented"], code='demo_pv = DEMO.copy()\ndemo_pv["chuyen"] = demo_pv["calculated_host_listings_count"] >= 5')
    asset("05.big-districts", ["05.segmented"], code='df_quan_lon = DEMO.loc[DEMO["neighbourhood"].isin(["Santiago", "Providencia"])].copy()')
    asset("05.fees", ["05.segmented"], selections=[setup("phi")])
    plan("05", [1], "05.series")
    plan("05", [2], "05.surveys")
    plan("05", [3], "05.table")
    plan("05", [4, 5, 6, 7, 8], "05.segmented")
    plan("05", [7], "05.pivot-input", way=2)
    plan("05", [8], "05.big-districts", way=2)
    plan("05", [9], "05.big-districts")
    plan("05", [10], "05.fees")

    asset("06.listings", selections=[setup("DEMO_LISTINGS_FULL")])
    asset("06.reviews", selections=[setup("_danh_sach_ngay", "DEMO_REVIEWS", mutations=["_danh_sach_ngay"])])
    asset("06.weather", selections=[setup("DEMO_WEATHER")])
    asset("06.full-file", ["06.listings"], code='DEMO_LISTINGS_FULL.to_csv("listings_full.csv", index=False)')
    asset("06.review-file", ["06.reviews"], code='DEMO_REVIEWS.to_csv("reviews.csv", index=False)')
    asset("06.listing-file", ["06.listings"], code='DEMO_LISTINGS_FULL[["id", "name", "room_type"]].to_csv("listings.csv", index=False)')
    asset("06.columns", selections=[assignment("data-lab-06-01", "cot_can_doc", "cot_ngay")])
    asset("06.selected", ["06.full-file", "06.columns"], selections=[helper("data-lab-06-01", "read_selected")],
          code='bang_chon_loc = read_selected("listings_full.csv", cot_can_doc, cot_ngay)')
    asset("06.price-reference", ["06.listings"], selections=[helper("data-lab-06-02", "clean_price")], code='gia_sach = clean_price(DEMO_LISTINGS_FULL["price"])')
    asset("06.daily", ["06.reviews"], selections=[helper("data-lab-06-05", "reviews_per_day")],
          code='thong_ke_ngay = reviews_per_day(DEMO_REVIEWS, "2025-01-01", "2025-01-10")')
    asset("06.weather-table", ["06.weather"], code='df_thoi_tiet = pd.DataFrame(DEMO_WEATHER["daily"])')
    asset("06.join", ["06.daily", "06.weather-table"], selections=[helper("data-lab-06-06", "join_weather")], code='ket_qua_ghep = join_weather(df_thoi_tiet, thong_ke_ngay)')
    asset("06.year-reference", ["06.review-file"], selections=[helper("data-lab-06-07", "sql_reviews_by_year")], code='bang_dem_nam = sql_reviews_by_year("reviews.csv")')
    asset("06.parquet", ["06.selected"], code='bang_chon_loc.to_parquet("listings.parquet", index=False)')
    asset("06.count-reference", ["06.parquet"], selections=[helper("data-lab-06-08", "sql_count_listings_and_reviews")], code='thong_ke_loai_cho = sql_count_listings_and_reviews("listings.parquet")')
    asset("06.room-reference", ["06.review-file", "06.listing-file"], selections=[helper("data-lab-06-09", "sql_reviews_by_room_type")], code='danh_gia_theo_phong = sql_reviews_by_room_type("reviews.csv", "listings.csv", 2025)')
    asset("06.active-reference", ["06.review-file"], selections=[helper("data-lab-06-10", "sql_active_listings_having")], code='cho_o_tich_cuc = sql_active_listings_having("reviews.csv", 2025, 5)')
    asset("06.july-fixtures", selections=[assignment("data-lab-06-11", "DEMO_WEATHER_JULY", "DEMO_REVIEWS_JULY")])
    asset("06.top-reference", ["06.review-file", "06.listing-file"], selections=[helper("data-lab-06-12", "sql_top_reviewed_listings")], code='top_5_cho_o = sql_top_reviewed_listings("reviews.csv", "listings.csv", 2025, 5)')
    plan("06", [1], "06.full-file")
    plan("06", [1], "06.full-file", "06.columns", way=2)
    plan("06", [2], "06.listings")
    plan("06", [2], "06.price-reference", way=2)
    plan("06", [3], "06.selected")
    plan("06", [4], "06.weather")
    plan("06", [5], "06.reviews")
    plan("06", [5], "06.daily", way=2)
    plan("06", [6], "06.daily", "06.weather-table")
    plan("06", [7], "06.review-file")
    plan("06", [7], "06.year-reference", way=2)
    plan("06", [8], "06.selected")
    plan("06", [8], "06.count-reference", way=2)
    plan("06", [9], "06.review-file", "06.listing-file")
    plan("06", [9], "06.room-reference", way=2)
    plan("06", [10], "06.review-file")
    plan("06", [10], "06.active-reference", way=2)
    plan("06", [11], "06.daily")
    plan("06", [11], "06.weather", "06.reviews", "06.july-fixtures", way=2)
    plan("06", [12], "06.review-file", "06.listing-file")
    plan("06", [12], "06.top-reference", way=2)

    for name in ("DEMO_COMMENTS", "DEMO_PRICES", "DEMO_PRICES_TEST", "DEMO_LISTINGS", "DEMO_DS_NHO", "PAT_ES", "PAT_GAN", "PAT_GIA"):
        asset("07." + name, selections=[setup(name)])
    asset("07.clean-text", ["07.DEMO_COMMENTS"], code='c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)\nc_sach_full = c_sach_demo.copy()')
    asset("07.language", ["07.clean-text", "07.PAT_ES"], selections=[helper("data-lab-07-07", "language_flag", way=2)],
          code='ket_qua_es = language_flag(c_sach_demo)\nflag_es = ket_qua_es["la_es"]\nflag_es_demo = flag_es.copy()')
    asset("07.places", selections=[assignment("data-lab-07-10", "gan_demo")])
    asset("07.amenities", ["07.DEMO_LISTINGS"], selections=[helper("data-lab-07-11", "parse_amenities_explode", way=2)], code='ds_demo, muc_demo = parse_amenities_explode(DEMO_LISTINGS)')
    asset("07.area-sample", selections=[assignment("data-lab-07-15", "mau_phong")])
    plan("07", [3], "07.DEMO_PRICES", way=2)
    plan("07", [4], "07.DEMO_PRICES_TEST", "07.PAT_GIA", way=2)
    plan("07", [5, 6], "07.DEMO_COMMENTS")
    plan("07", [7], "07.clean-text", "07.PAT_ES")
    plan("07", [8, 14], "07.language")
    plan("07", [9], "07.clean-text", "07.PAT_GAN")
    plan("07", [10], "07.places", way=2)
    plan("07", [11], "07.DEMO_LISTINGS")
    plan("07", [12], "07.amenities")
    plan("07", [13], "07.DEMO_DS_NHO")
    plan("07", [15], "07.area-sample", way=2)

    asset("08.dates", selections=[setup("DAT_DEMO")])
    asset("08.reviews", selections=[Select(("sinh_so_danh_gia",), functions=True), setup("_ngay", "_so", "DEMO_REVIEWS", mutations=["DEMO_REVIEWS"])])
    asset("08.snapshot", selections=[setup("SNAPSHOT")])
    asset("08.index", ["08.reviews", "08.snapshot"], selections=[helper("data-lab-08-03", "prepare_time_index")], code='ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)\nket_qua_idx_c2 = ket_qua_idx_c1')
    asset("08.quarters", ["08.index"], selections=[helper("data-lab-08-05", "quarterly")], code='ket_qua_quy_c1 = quarterly(ket_qua_idx_c1["r"], SNAPSHOT)\nket_qua_quy_c2 = ket_qua_quy_c1\nquy_day_du_demo = ket_qua_quy_c1["quy_day_du"]')
    asset("08.daily", ["08.index"], selections=[helper("data-lab-08-08", "daily_counts")], code='ngay_2025_c1 = daily_counts(ket_qua_idx_c1["r"], 2025)')
    asset("08.months", ["08.index"], code='thang_series = ket_qua_idx_c1["r"].resample("ME").size()\nthang_4nam_demo = thang_series.loc["2022":"2025"]')
    asset("08.listings", ["08.snapshot"], selections=[setup("LISTINGS_DEMO")])
    plan("08", [1, 2], "08.dates")
    plan("08", [3], "08.reviews", "08.snapshot")
    plan("08", [4, 5, 8, 11, 12, 13], "08.index")
    plan("08", [7, 10], "08.quarters")
    plan("08", [9], "08.daily")
    plan("08", [11, 12], "08.months", way=2)
    plan("08", [14], "08.listings")

    # Labs 10--12 use the same explicit source-selection policy. Reference
    # calculations are necessary for authored method-2 equality assertions.
    # Their helper definitions and named results are selected, never print calls.
    for lab, count in (("10", 13), ("11", 8), ("12", 11)):
        plan(lab, range(1, count + 1))
    asset("10.main", selections=[setup("MOC", "LTM_BAT_DAU", "DEMO_RV", "DEMO_DS")])
    references = {
        1: (("ds_demo_rpm",), ("dien_rpm_co_can_cu_buoc",), ("rpm_ket_qua_c1",)),
        2: (("ds_demo_gia",), ("dien_gia_nhom_vong_lap",), ("gia_uoc_c1", "co_dien_c1")),
        3: (("gia_thu",), ("kiem_gia_tuan_tu",), ("co_gia_c1",)),
        4: (("ds_demo_phan_vi",), ("phan_vi_chan_gia_buoc",), ("iqr_c1", "n_iqr_c1", "p99_c1", "bang_c1")),
        5: (("mau_rv_demo", "rv_rut_gon_demo"), ("xu_ly_trung_lap_co_ban",), ("rv_sach_c1", "lap_sau_c1", "nhom_lap_c1")),
        6: ((), ("time_domain_buoc", "kiem_reviews_buoc"), ("mien_c1", "co_rv_c1")),
        7: (("ds_thieu",), ("orphan_reviews_isin",), ("so_mo_coi_chuan", "so_mo_coi_thieu")),
        8: ((), ("duplicate_pairs_duplicated",), ("lap_c1_cap", "lap_c1_id")),
        9: ((), ("review_count_check_reindex", "doi_chieu_so_danh_gia_buoc"), ("kq_q4_c1", "bang_dc_c1")),
        10: ((), ("ltm_mismatch_buoc", "doi_chieu_12_thang_co_dinh_buoc"), ("kq_ltm_c1", "dem12_c1", "lech12_c1")),
        12: (("gia_nhap_demo",), ("tach_gia_mau_thuan_vong_lap",), ("gop_c1", "xem_c1")),
        13: (("loai_demo", "lich_demo", "nhiet_do_demo"), ("dien_khuyet_chuyen_sau_buoc",), ("loai_c1", "lich_c1", "ns_c1")),
    }
    for number, (inputs, functions, results) in references.items():
        exercise = f"data-lab-10-{number:02d}"
        selections = ([assignment(exercise, *inputs)] if inputs else [])
        selections += [helper(exercise, *functions), assignment(exercise, *results)]
        dependencies = ["10.main"] if 6 <= number <= 10 else []
        asset(f"10.reference-{number}", dependencies, selections)
        if dependencies:
            plan("10", [number], *dependencies)
        plan("10", [number], f"10.reference-{number}", way=2)
    asset("10.flags", ["10.main"], selections=[helper("data-lab-10-06", "kiem_reviews_buoc"),
                                                helper("data-lab-10-06", "kiem_reviews", way=2)],
          code='co_rv_c1 = kiem_reviews_buoc(DEMO_RV, DEMO_DS["id"], MOC)\nco_rv_c2 = kiem_reviews(DEMO_RV, DEMO_DS["id"], MOC)')
    asset("10.report-input", ["10.flags"], selections=[assignment("data-lab-10-11", "so_lieu_demo", "ghi_chu_demo")])
    asset("10.report-reference", ["10.report-input"], selections=[helper("data-lab-10-11", "qa_report_records", "tom_tat_co_buoc")],
          code='''import tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as report_folder:
    bao_cao_c1 = qa_report_records(so_lieu_demo, ghi_chu_demo, Path(report_folder) / "reference.csv")
bang_tt_c1 = tom_tat_co_buoc(co_rv_c1, "reviews")''')
    plan("10", [11], "10.flags")
    plan("10", [11], "10.report-reference", way=2)

    asset("11.sample-data", selections=[setup("_MAU_CAU", "DEMO_RV")])
    asset("11.sample", ["11.sample-data"], selections=[helper("data-lab-11-01", "choose_sample")], code='mau_co_ban = choose_sample(DEMO_RV, do_dai_min=50, n=100, seed=42)')
    asset("11.aspect", selections=[assignment("data-lab-11-03", "Aspect")])
    asset("11.schema", ["11.aspect"], selections=[helper("data-lab-11-03", "ReviewInfo")])
    asset("11.responses", selections=[setup("LLM_OUT")])
    asset("11.gold", selections=[setup("GOLD")])
    asset("11.validated", ["11.schema", "11.responses"], selections=[helper("data-lab-11-04", "validate_outputs")], code='ket_qua_kiem_dinh = validate_outputs(LLM_OUT)')
    asset("11.predictions", ["11.validated", "11.gold"], code='tap_du_doan = {rid: obj.sentiment for rid, obj in ket_qua_kiem_dinh["hop_le"].items()}')
    asset("11.accuracy", ["11.predictions"], selections=[helper("data-lab-11-05", "sentiment_accuracy")], code='kq_do_luong = sentiment_accuracy(tap_du_doan, GOLD)')
    asset("11.errors", ["11.accuracy"], selections=[setup("REVIEWS")])
    asset("11.dump", ["11.validated"], code='tap_dau_ra_dump = {rid: obj.model_dump() for rid, obj in ket_qua_kiem_dinh["hop_le"].items()}')
    asset("11.contradictions", ["11.dump"], selections=[helper("data-lab-11-07", "contradictions")], code='ds_mau_thuan = contradictions(tap_dau_ra_dump)')
    asset("11.evaluate", ["11.schema", "11.responses", "11.gold"], selections=[helper("data-lab-11-04", "validate_outputs"), helper("data-lab-11-05", "sentiment_accuracy"), helper("data-lab-11-07", "contradictions")])
    asset("11.pipeline", ["11.evaluate"], selections=[assignment("data-lab-11-08", "LLM_RUN_2"), helper("data-lab-11-08", "evaluate_llm_run")])
    plan("11", [1], "11.sample-data")
    plan("11", [1], "11.sample", way=2)
    plan("11", [3], "11.aspect", way=2)
    plan("11", [4], "11.schema", "11.responses")
    plan("11", [5], "11.predictions")
    plan("11", [6], "11.errors")
    plan("11", [7], "11.dump")
    plan("11", [7], "11.contradictions", way=2)
    plan("11", [8], "11.evaluate")
    plan("11", [8], "11.pipeline", way=2)

    asset("12.listings", selections=[setup("_QUAN", "_CHU_KY_PHONG_RIENG", "DEMO_DS")])
    asset("12.reviews", ["12.listings"], selections=[setup("_dong", "DEMO_RV", mutations=["_dong"])])
    asset("12.figures", code='from pathlib import Path\nPath("figures").mkdir(parents=True, exist_ok=True)')
    asset("12.monthly", ["12.reviews"], selections=[helper("data-lab-12-01", "monthly_reviews")], code='thang_pro_c1 = monthly_reviews(DEMO_RV, DEMO_DS, "Providencia")')
    asset("12.share", ["12.listings"], selections=[helper("data-lab-12-04", "share_entire")], code='tk_nguyen_can_c1 = share_entire(DEMO_DS, min_n=5)')
    asset("12.comparison", selections=[assignment("data-lab-12-08", "dulieu_sosanh")])
    asset("12.barh-reference", ["12.share", "12.figures"], selections=[helper("data-lab-12-05", "plot_share_barh")], code='ax_barh_c1 = plot_share_barh(tk_nguyen_can_c1, "figures/share-reference.png")')
    asset("12.honest-reference", ["12.comparison", "12.figures"], selections=[helper("data-lab-12-09", "plot_honest_bars")], code='ax_honest_c1 = plot_honest_bars(dulieu_sosanh, "figures/honest-reference.png")')
    plan("12", [1, 2], "12.reviews")
    plan("12", [3], "12.monthly", "12.figures")
    plan("12", [4, 7], "12.listings")
    plan("12", [5], "12.share", "12.figures")
    plan("12", [6, 11], "12.listings", "12.figures")
    plan("12", [8], "12.comparison", way=2)
    plan("12", [9], "12.comparison", "12.figures")
    plan("12", [10], "12.barh-reference", way=1)
    plan("12", [10], "12.honest-reference", way=2)


build_registry()


def compose_method(source: Source, method: Method) -> str:
    selected_plan = REGISTRY.get(method.key)
    if selected_plan is None:
        missing = external_names(method.code)
        if missing:
            raise CompositionError(f"Unconfigured {method.exercise}/method-{method.way}: {sorted(missing)}")
        return method.code  # New independently authored labs pass through unchanged.
    chunks = []
    done, active = set(), set()
    def visit(name):
        if name in done:
            return
        if name in active or name not in ASSETS:
            raise CompositionError(f"Invalid asset dependency: {name}")
        active.add(name)
        fixture = ASSETS[name]
        for dependency in fixture.dependencies:
            visit(dependency)
        chunks.extend(source.select(selection) for selection in fixture.selections)
        if fixture.code:
            chunks.append(fixture.code)
        active.remove(name)
        done.add(name)
    for name in selected_plan.assets:
        visit(name)
    body = method.code.rstrip()
    combined = "\n\n".join([*chunks, body, selected_plan.output])
    imports = []
    # Imports inside the authored body execute after fixture preparation. They
    # cannot satisfy names used by the prelude before that body is reached.
    needed_imports = external_names("\n\n".join(chunks)) | external_names(combined)
    for name in sorted(needed_imports):
        statement = source.imports.get(name)
        if statement is None:
            raise CompositionError(f"Unconfigured {method.exercise}/method-{method.way}: missing {name}")
        if statement not in imports:
            imports.append(statement)
    parts = [GENERATED, *imports, *chunks, START, body, END]
    if selected_plan.output:
        parts.append(selected_plan.output)
    result = "\n\n".join(part for part in parts if part) + "\n"
    missing = external_names(result)
    if missing:
        raise CompositionError(f"Unresolved names after composition: {sorted(missing)}")
    return result


def compose_document(text: str) -> tuple[str, list[tuple[Method, str]]]:
    source = Source(text)
    programs = [(method, compose_method(source, method)) for method in source.methods]
    if not programs:
        raise CompositionError("No method programs found")
    result = text
    for method, program in reversed(programs):
        newline = "\r\n" if "\r\n" in text[method.start:method.end] else "\n"
        result = result[:method.start] + program.replace("\r\n", "\n").replace("\n", newline) + result[method.end:]
    return result, programs


# This wrapper observes figures after runpy returns; it injects no application
# globals, imports, display stub, fixtures or previous method state into the run.
RUNNER = '''import json, pathlib, runpy, sys
runpy.run_path("program.py", run_name="__main__")
figures = []
if "matplotlib.pyplot" in sys.modules:
    plt = sys.modules["matplotlib.pyplot"]
    for number in plt.get_fignums():
        name = "figure-" + str(number) + ".png"
        plt.figure(number).savefig(name)
        figures.append(name)
pathlib.Path("execution.json").write_text(json.dumps({"figures": figures}), encoding="utf-8")
'''


def execute_program(program: str, timeout: float = 60) -> dict:
    """Each call starts a fresh interpreter and a fresh working directory."""
    with tempfile.TemporaryDirectory(prefix="studyhub-method-") as temporary:
        working = Path(temporary)
        (working / "program.py").write_text(program, encoding="utf-8")
        (working / "runner.py").write_text(RUNNER, encoding="utf-8")
        env = os.environ.copy()
        env.update(PYTHONIOENCODING="utf-8", MPLBACKEND="Agg")
        try:
            run = subprocess.run([sys.executable, str(working / "runner.py")], cwd=working,
                                 env=env, capture_output=True, encoding="utf-8", errors="replace", timeout=timeout)
        except subprocess.TimeoutExpired as exc:
            return {"passed": False, "returncode": None, "stdout": exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or ""),
                    "stderr": f"Execution timed out after {timeout}s", "artifacts": []}
        metadata = json.loads((working / "execution.json").read_text(encoding="utf-8")) if (working / "execution.json").exists() else {}
        artifacts = [str(path.relative_to(working)) for path in working.rglob("*")
                     if path.is_file() and path.name not in {"program.py", "runner.py", "execution.json"}]
        visible = bool(run.stdout.strip() or metadata.get("figures"))
        return {"passed": run.returncode == 0 and visible, "returncode": run.returncode,
                "stdout": run.stdout, "stderr": run.stderr,
                "visibleOutput": visible, "figures": metadata.get("figures", []), "artifacts": artifacts}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="Defaults to all lab Markdown fragments")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Execute every method in a fresh process; never edit source")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "qa/data-labs/completed-code")
    mode.add_argument("--write", action="store_true", help="After successful validation, replace only method fence bodies")
    parser.add_argument("--published-only", action="store_true", help="With --check, execute the exact visible programs without composing them")
    parser.add_argument("--timeout", type=float, default=60)
    parser.add_argument("--jobs", type=int, default=1, choices=range(1, 5), help="Independent process checks in parallel (1--4)")
    args = parser.parse_args(argv)
    if args.published_only and not args.check:
        parser.error("--published-only requires --check")
    output = args.output_dir.resolve()
    files = args.files or sorted(LABS.glob("lab-*.md"))
    # Prevent accidentally using a source folder as disposable inspection output.
    for path in files:
        if output == path.resolve().parent or output in path.resolve().parents:
            parser.error("--output-dir must be separate from source directories")
    output.mkdir(parents=True, exist_ok=True)
    records, pending = [], []
    for path in files:
        path = path.resolve()
        original = path.read_bytes()
        try:
            source_text = original.decode("utf-8")
            if args.published_only:
                composed = source_text
                programs = [(method, source_text[method.start:method.end])
                            for method in extract_methods(source_text)]
                if not programs:
                    raise CompositionError("No method programs found")
            else:
                composed, programs = compose_document(source_text)
        except (CompositionError, SyntaxError) as exc:
            records.append({"file": path.name, "passed": False, "error": str(exc)})
            print(f"FAIL {path.name}: {exc}", flush=True)
            continue
        (output / path.name).write_bytes(composed.encode("utf-8"))
        methods = []
        executor = ThreadPoolExecutor(max_workers=args.jobs)
        executions = [executor.submit(execute_program, program, args.timeout)
                      for _, program in programs] if (args.check or args.write) else []
        for index, (method, program) in enumerate(programs):
            name = f"{method.exercise}-method-{method.way}"
            (output / f"{name}.py").write_text(program, encoding="utf-8")
            record = {"exercise": method.exercise, "method": method.way, "line": method.line,
                      "configured": method.key in REGISTRY, "passed": True}
            if args.check or args.write:
                record.update(executions[index].result())
                (output / f"{name}.stdout.txt").write_text(record["stdout"], encoding="utf-8")
                (output / f"{name}.stderr.txt").write_text(record["stderr"], encoding="utf-8")
            methods.append(record)
            label = ('PASS' if record['passed'] else 'FAIL') if (args.check or args.write) else 'COMPOSED'
            print(f"{label} {name}", flush=True)
        executor.shutdown(wait=True)
        passed = all(record["passed"] for record in methods)
        records.append({"file": path.name, "passed": passed, "methods": methods})
        pending.append((path, original, composed.encode("utf-8")))
    passed = bool(records) and all(record["passed"] for record in records)
    # Also invalidate a check-only snapshot if authors changed its source during
    # execution. No source is written until all concurrency checks have passed.
    changed = [str(path) for path, original, _ in pending if path.read_bytes() != original]
    if changed:
        passed = False
        records.append({"passed": False, "error": "Sources changed during validation; rerun", "files": changed})
    if args.write and passed:
        for path, _, composed in pending:
            path.write_bytes(composed)
    report = {"passed": passed, "executed": args.check or args.write, "wroteSource": bool(args.write and passed),
              "files": records}
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Report: {output / 'report.json'}", flush=True)
    return 0 if passed else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
