export const probStatsLabs = {
  "xac-suat-thong-ke/01-xac-suat-va-bayes": {
    "id": "01-xac-suat-va-bayes",
    "title": "Thực hành Cập nhật Niềm tin Định lý Bayes & Mô phỏng Monte Carlo",
    "dataset": {
      "name": "Mô phỏng dữ liệu sàng lọc y tế 100.000 bệnh nhân",
      "type": "Tập ngẫu nhiên mô phỏng (Synthetic Cohort)",
      "url": "https://raw.githubusercontent.com/uet-iai-notebook-labs-2026/notebook-labs-template/main/README.md",
      "description": "Quần thể 100.000 người với tỷ lệ nhiễm bệnh hiếm 0.1%, độ nhạy xét nghiệm 99% và tỷ lệ dương tính giả 5% để giải mã nghịch lý tỷ lệ nền (Base Rate Fallacy)."
    },
    "tasks": [
      {
        "id": "task-1",
        "title": "Bài 1: Giải mã Nghịch lý Tỷ lệ nền bằng Bảng số đếm tự nhiên",
        "prompt": "Viết hàm tính xác suất hậu nghiệm $P(Bệnh \\mid Dương\\ tính)$ theo định lý Bayes và so sánh với mô phỏng bảng 100.000 người đếm tự nhiên.",
        "prediction": "Dù xét nghiệm có độ nhạy 99%, xác suất người dương tính thực sự có bệnh chỉ rơi vào khoảng 1.94% do số ca dương tính giả từ nhóm 99.900 người khỏe mạnh áp đảo số ca dương tính thật.",
        "solutionBasic": "def bayes_cb(p_d, p_pos_d, p_pos_not_d):\n    p_pos = p_pos_d * p_d + p_pos_not_d * (1 - p_d)\n    return (p_pos_d * p_d) / p_pos\n\nres = bayes_cb(0.001, 0.99, 0.05)\nprint(f'Xác suất có bệnh khi dương tính: {res:.2%}')",
        "solutionAdvanced": "def bang_dem_tu_nhien(dan_so: int = 100000, p_benh: float = 0.001, do_nhay: float = 0.99, duong_tinh_gia: float = 0.05) -> dict:\n    so_benh = int(dan_so * p_benh)\n    so_khoe = dan_so - so_benh\n    tp = int(so_benh * do_nhay)\n    fp = int(so_khoe * duong_tinh_gia)\n    return {'dan_so': dan_so, 'duong_tinh_that': tp, 'duong_tinh_gia': fp, 'xac_suat_that': tp / (tp + fp)}\n\nprint(bang_dem_tu_nhien())",
        "explanation": "Quy đổi về bảng số đếm tự nhiên là phương pháp sư phạm trực quan nhất giúp giải thích nghịch lý tỷ lệ nền cho sinh viên và công chúng.",
        "verification": "assert abs(bayes_cb(0.001, 0.99, 0.05) - 0.0194) < 0.001"
      }
    ]
  }
};
