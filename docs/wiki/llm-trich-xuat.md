---
title: "Trích xuất bằng LLM"
wikiTerm: llm-trich-xuat
prev: false
next: false
---

# Trích xuất bằng LLM

Trích xuất bằng LLM dùng mô hình ngôn ngữ để chuyển văn bản thành trường hoặc nhãn theo nhiệm vụ. Kết quả cần kiểm cấu trúc, căn cứ trong nguồn và chất lượng trên mẫu đánh giá.

<WikiUsage />

## Giải thích kỹ thuật

Định nghĩa nhiệm vụ, schema và cách biểu diễn trường hợp không đủ căn cứ. Kiểm phản hồi từng dòng, đối chiếu bằng chứng với nguồn và đo chất lượng trên mẫu gán nhãn. Giữ lỗi riêng với kết quả đã xác nhận. Đây là kỹ năng thực hành hiện đại hỗ trợ quy trình xử lý dữ liệu.

Nguồn kỹ thuật: [Gemini API Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output).

## Ví dụ

Một nhận xét được chuyển thành mã định danh, nhãn cảm xúc và đoạn bằng chứng, trong đó đoạn trích phải được đối chiếu trực tiếp với văn bản gốc.

## Khi nào cần dùng?

Xử lý văn bản có nhiều cách diễn đạt khó mô tả bằng mẫu ổn định.

## Câu hỏi ôn lại

Structured output có bảo đảm nhãn đúng không?

<details><summary>Xem đáp án</summary>

Không. Nó hỗ trợ cấu trúc; nội dung vẫn cần kiểm tra và đánh giá.

</details>

## Thuật ngữ liên quan

- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
- [Histogram](./histogram.md)
