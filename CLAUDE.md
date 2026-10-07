# StudyHub (UETệ) — hướng dẫn cho trợ lý AI

Website ôn tập VitePress cho sinh viên UET. Nội dung bằng tiếng Việt. Mỗi bài giảng gồm ba phần trên một trang: **Slides** (`docs/.vitepress/course-catalog.mjs`), **Notes** (`docs/<môn>/bai-giang/<slug>.md`), **Kiến thức nền** (`prerequisites` → `docs/.vitepress/concepts.mjs` → `docs/wiki/<id>.md`). Tài liệu gốc của môn nằm trong `raw_materials/<môn>/`.

## Skill phải dùng

- Soạn, sửa, rà một bài giảng, thêm thuật ngữ Wiki, hoặc xuất slide PDF/PPTX từ một bài → `.claude/skills/studyhub-lecture`. Đọc `references/repo-format.md` của skill trước khi sửa file của site.
- Người dùng dán một đoạn giáo trình và nhờ giảng, hoặc gửi bài làm để sửa → `.claude/skills/textbook-passage-explainer`.

Nguyên tắc chung khi viết nội dung học: đúng giả thiết và điều kiện của nguồn; mở bước khó thay vì khẳng định; mọi con số được tính lại bằng code; không bịa trích dẫn, năm tháng, số liệu hay “lỗi thường gặp”; tiếng Việt chuyên ngành tự nhiên, không khẩu hiệu.

## Lệnh

```sh
npm ci
npm run dev                 # http://localhost:5173
npm run ci:build            # sync + build; phải exit 0 trước khi commit nội dung
node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs --all     # tích hợp catalog/Wiki/hình
python3 -I .claude/skills/studyhub-lecture/scripts/tests/test_tools.py   # test của skill
```

`npm run build` còn xuất file tĩnh ra thư mục gốc (đã gitignore). `scripts/verify-courses.mjs` kiểm giao diện bằng Puppeteer, cần server preview và Chrome.

Push vào `main` sẽ tự deploy lên GitHub Pages qua `.github/workflows/deploy.yml`.
