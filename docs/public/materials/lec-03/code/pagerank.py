#!/usr/bin/env python3
"""
Bài 03 — PageRank: mô hình và tính toán
Học phần Giải thuật nền tảng của Khoa học dữ liệu (UET.DSE2053)

Cài đặt mô hình đầy đủ bao gồm:
- Random Surfer với hệ số bước nhảy beta (damping factor)
- Xử lý Nút cụt (Dead Ends): gom tổng điểm delta và tái phân phối đều
- Xử lý Bẫy liên kết (Spider Traps)
- Kiểm tra tính dừng dựa trên chuẩn khoảng cách L1 giữa hai vòng liên tiếp (tol)
"""

import argparse
import json
import math
import sys

GRAPHS = {
    # Đồ thị gốc Hình 5.1 (MMDS): A, B, C, D
    "base": {
        "A": ["B", "C", "D"],
        "B": ["A", "D"],
        "C": ["A"],
        "D": ["B", "C"],
    },
    # Biến thể nút cụt: C không có liên kết ra
    "dead": {
        "A": ["B", "C", "D"],
        "B": ["A", "D"],
        "C": [],
        "D": ["B", "C"],
    },
    # Biến thể bẫy liên kết: C chỉ trỏ vào chính nó
    "trap": {
        "A": ["B", "C", "D"],
        "B": ["A", "D"],
        "C": ["C"],
        "D": ["B", "C"],
    },
}

def step(adj, r, beta):
    """
    Thực hiện đúng 1 vòng cập nhật PageRank đồng bộ:
    r^{t+1}_i = beta * sum_{j: j->i} (r^t_j / d_j) + ((1 - beta) + beta * delta^t) / n
    """
    n = len(adj)
    # delta: tổng điểm của các nút cụt từ vector cũ r
    delta = sum(r[j] for j in adj if not adj[j])
    # Phần bù chung chia đều cho toàn bộ n trang (bảo toàn khối lượng xác suất)
    common = (1.0 - beta + beta * delta) / n
    new = {i: common for i in adj}

    for j, targets in adj.items():
        if not targets:
            continue
        # Nút j chia đều phần đóng góp beta * r_j cho các đích
        share = beta * r[j] / len(targets)
        for i in targets:
            new[i] += share

    return new

def pagerank(adj, beta=0.8, tol=1e-8, max_iter=100):
    """
    Lặp lũy thừa tính PageRank cho tới khi đạt ngưỡng sai số L1 (tol) hoặc hết max_iter.
    """
    n = len(adj)
    if n == 0:
        return {"rank": {}, "converged": True, "iterations": 0, "delta": 0.0, "rank_sum": 0.0}

    # Khởi tạo vector phân phối đều ban đầu r^0
    r = {i: 1.0 / n for i in adj}
    converged = False
    iteration = 0
    delta_norm = 0.0

    for iteration in range(1, max_iter + 1):
        r_next = step(adj, r, beta)
        # delta_norm là chuẩn L1 của độ thay đổi giữa 2 vòng: sum |r^{t+1}_i - r^t_i|
        delta_norm = sum(abs(r_next[i] - r[i]) for i in adj)
        r = r_next
        if delta_norm <= tol:
            converged = True
            break

    rank_sum = sum(r.values())
    return {
        "rank": {k: round(v, 8) for k, v in r.items()},
        "converged": converged,
        "iterations": iteration,
        "delta": round(delta_norm, 10),
        "rank_sum": round(rank_sum, 8)
    }

def main():
    parser = argparse.ArgumentParser(description="Mô phỏng thuật toán PageRank trên đồ thị nhỏ.")
    parser.add_argument("--variant", choices=["base", "dead", "trap"], default="base",
                        help="Chọn đồ thị: base (chuẩn), dead (nút cụt), trap (bẫy liên kết)")
    parser.add_argument("--beta", type=float, default=0.8, help="Hệ số lướt theo liên kết (mặc định 0.8)")
    parser.add_argument("--tol", type=float, default=1e-8, help="Ngưỡng dung sai dừng L1 (mặc định 1e-8)")
    parser.add_argument("--max-iter", type=int, default=100, help="Số vòng lặp tối đa (mặc định 100)")

    args = parser.parse_args()
    adj = GRAPHS[args.variant]
    result = pagerank(adj, beta=args.beta, tol=args.tol, max_iter=args.max_iter)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
