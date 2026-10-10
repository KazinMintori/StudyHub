export const discreteMathLabs = {
  "discrete-math/logic": {
    "id": "logic",
    "title": "Thực hành Bảng Chân trị & Thuật toán Kiểm tra Tương đương Logic",
    "dataset": {
      "name": "Bộ biểu thức mệnh đề Boolean",
      "type": "Cây cú pháp trừu tượng (AST) của biểu thức logic",
      "url": "https://raw.githubusercontent.com/uet-iai-notebook-labs-2026/notebook-labs-template/main/README.md",
      "description": "Tập hợp các biểu thức mệnh đề logic để tự động hóa việc lập bảng chân trị và kiểm tra tính hằng đúng (Tautology)."
    },
    "tasks": [
      {
        "id": "task-1",
        "title": "Bài 1: Tự động hóa lập bảng chân trị cho biểu thức n biến",
        "prompt": "Viết hàm `lap_bang_chan_tri(bieu_thuc_fn, so_bien)` tự động sinh $2^n$ tổ hợp giá trị chân lý của các biến mệnh đề và in ra bảng kết quả chân trị tương ứng.",
        "prediction": "Sử dụng `itertools.product([False, True], repeat=n)` sẽ sinh ra toàn bộ các tổ hợp nhị phân một cách tối ưu.",
        "solutionBasic": "import itertools\n\ndef lap_bang_cb(fn, n):\n    for combo in itertools.product([False, True], repeat=n):\n        val = fn(*combo)\n        print(combo, '->', val)",
        "solutionAdvanced": "def kiem_tra_hang_dung(fn, n_vars: int) -> bool:\n    \"\"\"Kiểm tra biểu thức có phải là hằng đúng (Tautology) hay không.\"\"\"\n    for combo in itertools.product([False, True], repeat=n_vars):\n        if not fn(*combo):\n            return False\n    return True",
        "explanation": "Lập bảng chân trị bằng mã nguồn giúp sinh viên nắm vững nguyên lý hoạt động của các bộ giải SAT Solver hiện đại.",
        "verification": "assert kiem_tra_hang_dung(lambda p: p or not p, 1) == True"
      }
    ]
  }
};
