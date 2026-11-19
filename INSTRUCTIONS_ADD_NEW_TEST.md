# 📚 Hướng Dẫn Thêm Đề Thi Mới Định Kỳ Vào Bluebook App

Ứng dụng **Digital SAT Bluebook Practice App** đã được cấu trúc lại hoàn toàn theo kiến trúc **Multi-Exam Engine** (Đa đề thi độc lập). Thầy Mike Pham Bá Hồng Sơn có thể định kỳ thêm bất kỳ đề thi mới nào (ví dụ: Tháng 11/2026, Tháng 12/2026,...) một cách nhanh chóng chỉ qua 3 bước đơn giản.

---

## 🚀 Cách 1: Thêm Tự Động Bằng Python CLI (`add_new_test.py`)

Công cụ `add_new_test.py` tự động đọc file đề PDF và file Answer Key PDF, phân tích toàn bộ 98 câu hỏi, sinh gợi ý 4 tầng Socratic, và đăng ký đề thi vào hệ thống:

```bash
# 1. Di chuyển vào thư mục ứng dụng
cd "SAT Coach/BluebookOct2026App"

# 2. Chạy lệnh thêm đề thi mới
python3 add_new_test.py \
    --test-id nov2026 \
    --title "Digital SAT Practice Test — November 2026 (INT-C)" \
    --short-title "Tháng 11/2026 (INT-C)" \
    --date "2026-11" \
    --pdf-test "/đường/dẫn/tới/File_De_Thi.pdf" \
    --pdf-key "/đường/dẫn/tới/File_Key.pdf" \
    --drive-id "ID_FILE_GOOGLE_DRIVE"
```

### Giải thích các tham số:
- `--test-id`: Mã định danh đề thi (chữ thường, viết liền, ví dụ: `nov2026`, `dec2026`).
- `--title`: Tên đầy đủ hiển thị trên báo cáo bài làm.
- `--short-title`: Tên rút gọn hiển thị trên thanh chọn (ví dụ: `Tháng 11/2026 (INT-C)`).
- `--date`: Năm - tháng của đề thi (ví dụ: `2026-11`).
- `--pdf-test`: Đường dẫn file PDF đề bài đầy đủ.
- `--pdf-key`: Đường dẫn file PDF đáp án chính thức (chứa danh sách câu, đáp án đúng và chủ đề).
- `--drive-id`: ID của file PDF đề thi trên Google Drive (để nhúng vào trình đọc bên trái).

---

## 🛠️ Cách 2: Thêm Thủ Công Qua File JSON

> [!IMPORTANT]
> ### 🎯 QUY TẮC BẮT BUỘC KHI ĐỊNH DẠNG PHƯƠNG ÁN A, B, C, D CHO ĐỀ THI REAL TEST
> 1. **KHÔNG chứa nội dung trích từ PDF vào mảng `options`**: Các phương án trắc nghiệm bắt buộc phải định dạng tinh giản theo quy chuẩn:
>    `"options": ["Lựa chọn A", "Lựa chọn B", "Lựa chọn C", "Lựa chọn D"]`
>    Học sinh luôn đọc câu hỏi và các phương án từ PDF Viewer bên trái. Nội dung chi tiết của các phương án cùng phân tích bẫy/tại sao đúng/tại sao sai được đặt trong `option_explanations`, `pooe_breakdown`, và `tier3_hint`.
> 2. **Tuyệt đối dùng dấu gạch nối tiêu chuẩn `-`**: Không dùng dấu gạch ngang dài `—` (em-dash) hoặc `–` (en-dash).
> 3. **Câu hỏi tự điền đáp số (Grid-in)**: Đặt `is_grid_in: true`, `options: []`, `correct_answer` chứa giá trị số (ví dụ: `"25"`, `"-6"`, `"1/2, .5, 0.5"`).

Nếu Thầy đã chuẩn bị sẵn file câu hỏi:

1. **Tạo file dữ liệu câu hỏi:** Lưu tại `data/<test_id>.json` (ví dụ `data/nov2026.json`).
2. **Đăng ký vào `data/manifest.json`:** Thêm 1 object vào danh sách:

```json
{
  "id": "nov-2026",
  "code": "nov2026",
  "title": "Digital SAT Practice Test — November 2026 (INT-C)",
  "short_title": "Tháng 11/2026 (INT-C)",
  "badge": "Mới nhất",
  "date": "2026-11",
  "dataFile": "data/nov2026.json",
  "pdfDriveId": "1dt6Up_Tz-B_h48JVLeIPF8vMwWWPxVSL",
  "pdfPreviewUrl": "https://drive.google.com/file/d/1dt6Up_Tz-B_h48JVLeIPF8vMwWWPxVSL/preview",
  "pdfViewUrl": "https://drive.google.com/file/d/1dt6Up_Tz-B_h48JVLeIPF8vMwWWPxVSL/view",
  "poster": "poster_nov.png",
  "total_questions": 98,
  "storageKey": "bluebook_nov2026_student_state_v1",
  "description": "Đề thi Real Test Digital SAT quốc tế tháng 11/2026 kèm giải thích chi tiết 4 tầng Socratic."
}
```

3. **Cập nhật `data/tests.js`:** Gán mảng `window.TESTS_MANIFEST = [...]` tương ứng để ứng dụng nạp ngay lập tức trên mọi trình duyệt tĩnh.

---

## 🌐 Đẩy Lên GitHub Pages Để Cập Nhật Cho Học Sinh

Sau khi thêm đề mới, chỉ cần chạy 2 lệnh Git:

```bash
git add .
git commit -m "feat: add Digital SAT Real Test November 2026 to exam bank"
git push origin main
```

Trang web `https://mikepham358.github.io/vinschool-sat-team/` sẽ tự động cập nhật ngay lập tức. Học sinh có thể chọn đề mới từ menu dropdown hoặc thẻ đề thi trên trang chủ, hoặc truy cập trực tiếp bằng đường link:
`https://mikepham358.github.io/vinschool-sat-team/?test=nov2026`
