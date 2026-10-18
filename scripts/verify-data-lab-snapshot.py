"""Verify published snapshot facts against the two downloaded source CSV files."""
from pathlib import Path
import argparse
import hashlib
import json
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("data_root", type=Path)
args = parser.parse_args()
ds = pd.read_csv(args.data_root / "listings.csv")
rv = pd.read_csv(args.data_root / "reviews.csv", parse_dates=["date"])
assert len(ds) == 18534 and len(ds.columns) == 19
assert len(rv) == 690112
assert rv.columns.tolist() == ["listing_id", "date"]
assert int((rv.date > pd.Timestamp("2026-06-29")).sum()) == 204
assert int((~rv.listing_id.isin(ds.id)).sum()) == 0
assert str(rv.date.min().date()) == "2010-11-13"
assert str(rv.date.max().date()) == "2026-07-01"
nu = ds.loc[ds.neighbourhood.eq("Ñuñoa")]
assert int(ds.room_type.eq("Private room").sum()) == 3413
assert int(ds.room_type.eq("Entire home/apt").sum()) == 15004
assert int(ds.price.isna().sum()) == 846
assert len(nu) == 1813 and nu.price.median() == 60981 and nu.price.min() == 2228
assert int(nu.price.isna().sum()) == 90
assert nu.room_type.value_counts().to_dict() == {"Entire home/apt": 1457, "Private room": 354, "Shared room": 2}
bands = pd.cut(ds.price, [-float("inf"), 30000, 100000, float("inf")], labels=["re", "trung", "cao"], right=False)
assert bands.value_counts().to_dict() == {"trung": 12325, "cao": 3703, "re": 1660}
assert round(ds.loc[bands.eq("trung"), "number_of_reviews_ltm"].mean(), 1) == 15.4
assert ds.loc[bands.eq("cao"), "price"].median() == 145318
pro = ds.calculated_host_listings_count.ge(5)
assert round(pro.mean() * 100, 1) == 35.8
assert ds.loc[pro, "price"].median() == 65078
assert round(ds.loc[~pro, "number_of_reviews_ltm"].mean(), 1) == 12.7
district_counts = ds.groupby("neighbourhood").size()
assert int(district_counts.ge(300).sum()) == 8
assert int(district_counts[district_counts.ge(300)].sum()) == 16850
assert round(ds.loc[bands.eq("trung"), "price"].median() * 1.13) == 61897
records = []
for name, frame in [("listings", ds), ("reviews", rv)]:
    data = (args.data_root / f"{name}.csv").read_bytes()
    records.append({
        "url": f"https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/{name}.csv",
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data), "rows": len(frame), "columns": frame.columns.tolist(),
    })
out = Path("raw_materials/xu-ly-du-lieu/lab-data-manifest.json")
out.write_text(json.dumps({"snapshot": "2026-06-29", "tables": records, "afterSnapshotReviewRows": 204, "orphanReviewRows": 0}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Snapshot facts verified: 18534 listings, 690112 reviews, 204 after snapshot, 0 orphan rows.")
