import os
import sys
import json
import re
import html
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import shutil
import smtplib
import subprocess
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

APP_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(APP_DIR, "static")
DATABASE_FILE = os.path.join(APP_DIR, "database.json")
CONFIG_FILE = os.path.join(APP_DIR, "email_config.json")
FEEDBACK_FILE = os.path.join(APP_DIR, "feedback.json")
STATIC_FEEDBACK_FILE = os.path.join(STATIC_DIR, "feedback.json")
FEEDBACK_LOG_MD = os.path.join(APP_DIR, "FEEDBACK_LOG.md")
SUBMISSIONS_DIR = os.path.join(APP_DIR, "submissions")
os.makedirs(SUBMISSIONS_DIR, exist_ok=True)

# Ensure database exists
if not os.path.exists(DATABASE_FILE):
    print("Database file not found, running extract_data.py...")
    import extract_data
    extract_data.extract_all()

with open(DATABASE_FILE, "r", encoding="utf-8") as f:
    DB = json.load(f)

def load_email_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "teacher_email": "mikepham358@gmail.com",
        "smtp_host": "smtp.gmail.com",
        "smtp_port": 465,
        "smtp_user": "mikepham358@gmail.com",
        "smtp_pass": ""
    }

def load_feedbacks():
    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_feedbacks_and_update_log(feedbacks):
    # 1. Save JSON
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(feedbacks, f, ensure_ascii=False, indent=2)
    try:
        with open(STATIC_FEEDBACK_FILE, "w", encoding="utf-8") as f:
            json.dump(feedbacks, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    # 2. Update FEEDBACK_LOG.md
    total = len(feedbacks)
    cat_err = 0
    cat_feat = 0
    cat_tech = 0
    cat_other = 0
    for x in feedbacks:
        c_low = x.get("category", "").lower()
        if "lỗi" in c_low or "đáp án" in c_low:
            cat_err += 1
        elif "tính năng" in c_low or "đề xuất" in c_low:
            cat_feat += 1
        elif "kỹ thuật" in c_low or "giao diện" in c_low or "desmos" in c_low:
            cat_tech += 1
        else:
            cat_other += 1
    
    resolved = sum(1 for x in feedbacks if "đã" in x.get("status", "").lower() or "triệt tiêu" in x.get("status", "").lower() or "giải quyết" in x.get("status", "").lower())
    pending = total - resolved
    now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    md = f"""# 📋 Nhật Ký Phản Hồi & Đóng Góp Ý Kiến (Feedback Logbook)

> **Dự án:** Digital SAT Practice Based on Learning Science — Vinschool SAT Team  
> **Giáo viên phụ trách:** Mike Pham Bá Hong Son (Google for Education Innovator) — `mikepham358@gmail.com`  
> **Trang làm bài trực tuyến:** [https://mikepham358.github.io/vinschool-sat-team/](https://mikepham358.github.io/vinschool-sat-team/)  
> **Cập nhật tự động lần cuối:** `{now_str}`  
> **Mô tả:** Mọi phản hồi từ học sinh và giáo viên gửi qua nút **`💬 Góp ý & Báo lỗi`** thông minh trên ứng dụng sẽ được tự động lưu trữ và đồng bộ tức thời lên kho mã nguồn GitHub này.

---

## 📊 Bảng Thống Kê Tổng Hợp (Summary Statistics)

| Chỉ số | Số lượng | Mô tả chi tiết |
| :--- | :---: | :--- |
| **Tổng số phản hồi tiếp nhận** | **{total}** | Toàn bộ phản hồi ghi nhận từ giáo viên & học sinh |
| 🎯 **Báo lỗi câu hỏi / Đáp án** | `{cat_err}` | Rà soát và đối chiếu trực tiếp với file gốc `KeyB.pdf` |
| 💡 **Đề xuất tính năng mới** | `{cat_feat}` | Cải tiến phương pháp học tập theo khoa học nhận thức |
| ⚡ **Lỗi giao diện / Kỹ thuật / Desmos** | `{cat_tech}` | Tối ưu trải nghiệm tương tác split-screen & kéo thả |
| 📝 **Góp ý chung & Đánh giá** | `{cat_other}` | Nhận xét chung về đề thi và lớp học |
| ✅ **Đã giải quyết / Đã khắc phục** | `{resolved}` | Đã kiểm tra, chỉnh sửa mã nguồn và đẩy lên GitHub |
| ⏳ **Đang xử lý (Open)** | `{pending}` | Đang trong hàng đợi kiểm tra của giáo viên |

---

## 📝 Danh Sách Nhật Ký Phản Hồi Chi Tiết (Detailed Feedback Log)

| STT | Mã Phản Hồi | Thời Gian | Người Gửi | Phân Loại | Vị Trí / Câu Hỏi | Mức Độ | Nội Dung Phản Hồi | Trạng Thái |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :--- | :---: |
"""
    for idx, item in enumerate(feedbacks, start=1):
        fid = item.get("id", f"FB-{idx:03d}")
        ts = item.get("date_str", item.get("timestamp", ""))
        sender = item.get("student_name", "Ẩn danh")
        email = item.get("student_email", "")
        sender_display = f"{sender}<br><sub>{email}</sub>" if email else sender
        cat = item.get("category", "Góp ý chung")
        pos = item.get("context_label", item.get("question_label", "Hệ thống"))
        prio = item.get("priority", "Bình thường")
        content = item.get("content", "").replace("|", "\\|").replace("\n", "<br>")
        st = item.get("status", "Đang xử lý (Open)")
        md += f"| {idx} | `{fid}` | {ts} | {sender_display} | {cat} | {pos} | {prio} | {content} | {st} |\n"

    md += "\n---\n*Nhật ký này được tạo và cập nhật tự động từ hệ thống Digital SAT Practice Engine.*\n"

    with open(FEEDBACK_LOG_MD, "w", encoding="utf-8") as f:
        f.write(md)

def sync_feedback_to_github_async(fb_item):
    def _worker():
        try:
            fid = fb_item.get("id", "FB")
            sender = fb_item.get("student_name", "Student")
            cat = fb_item.get("category", "Feedback")
            msg = f"docs(feedback): log feedback {fid} from {sender} [{cat}]"
            subprocess.run(["git", "add", "FEEDBACK_LOG.md", "feedback.json", "static/feedback.json"], cwd=APP_DIR, check=True)
            subprocess.run(["git", "commit", "-m", msg], cwd=APP_DIR, check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=APP_DIR, check=True)
            print(f"✅ [GitHub Sync] Feedback {fid} pushed to GitHub repository successfully!")
        except Exception as e:
            print(f"⚠️ [GitHub Sync Warning] Could not push feedback to GitHub: {e}")

    t = threading.Thread(target=_worker, daemon=True)
    t.start()

def generate_student_excel(payload):
    import openpyxl
    local_template = os.path.join(APP_DIR, "template.xlsx")
    excel_path = local_template if os.path.exists(local_template) else DB.get("excel_path", "")
    if not os.path.exists(excel_path):
        excel_path = "/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/26-27 Grand Plan /Study Plan/Module /Template - October 2026.xlsx"

    wb = openpyxl.load_workbook(excel_path, data_only=False)

    student_name = payload.get("student_name", "Student").strip() or "Hoc_Sinh"
    student_email = payload.get("student_email", "").strip() or "Chưa cung cấp"
    student_target = payload.get("student_target", "1400+")
    now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    summary = payload.get("summary", {})
    user_attempts = payload.get("attempts", {})  # { "1": { attempts: ["B"], status: "..." } }
    error_logs = payload.get("error_logs", [])

    # 1. Populate Overview_Strategies with Tong_Quan structure
    if "Overview_Strategies" in wb.sheetnames:
        ws_ov = wb["Overview_Strategies"]
        ws_ov.cell(2, 2, DB.get("test_title", "Digital SAT Practice Test — October 2026 (INT-B)"))
        ws_ov.cell(3, 2, student_name)
        ws_ov.cell(4, 2, student_email)
        ws_ov.cell(5, 2, student_target)
        ws_ov.cell(6, 2, now_str)
        ws_ov.cell(7, 2, "Mike Pham Bá Hong Son (Google for Education Innovator: https://edudirectory.withgoogle.com/profiles/5087615831769088) - mikepham358@gmail.com")
        ws_ov.cell(8, 2, "Tham khảo từ hocsat.com")

        if summary:
            if "total" in summary: ws_ov.cell(11, 2, summary["total"])
            if "answered" in summary: ws_ov.cell(12, 2, summary["answered"])
            if "l1_correct" in summary: ws_ov.cell(13, 2, summary["l1_correct"])
            if "l2_correct" in summary: ws_ov.cell(14, 2, summary["l2_correct"])
            if "l3_correct" in summary: ws_ov.cell(15, 2, summary["l3_correct"])
            if "score_pct" in summary: ws_ov.cell(16, 2, f"{summary['score_pct']}%")
            est = summary.get("estimatedScore") or round(400 + (summary.get("score_pct", 0) / 100) * 1200)
            ws_ov.cell(17, 2, f"{est} / 1600")
            ws_ov.cell(18, 2, len(error_logs))

    # Personalize Performance_Summary header
    if "Performance_Summary" in wb.sheetnames:
        ws_perf = wb["Performance_Summary"]
        ws_perf.cell(1, 1, f"BẢNG TỔNG HỢP KẾT QUẢ: {student_name.upper()} (OCTOBER 2026 TEST)")
        ws_perf.cell(3, 1, f"Học sinh: {student_name} | Thời gian làm bài: {now_str}")

    # Build question lookup by ID
    q_map = {q["id"]: q for q in DB["questions"]}

    # Clear existing attempt inputs first to ensure clean state
    for mod in ["RW_Module1", "RW_Module2", "Math_Module1", "Math_Module2"]:
        if mod in wb.sheetnames:
            ws = wb[mod]
            for r in range(5, ws.max_row + 1):
                ws.cell(r, 6, None)
                ws.cell(r, 8, None)
                ws.cell(r, 10, None)

    if "Master_All_98_Questions" in wb.sheetnames:
        ws_m = wb["Master_All_98_Questions"]
        for r in range(5, ws_m.max_row + 1):
            ws_m.cell(r, 7, None)
            ws_m.cell(r, 9, None)
            ws_m.cell(r, 11, None)

    # Populate student attempts
    for qid_str, q_state in user_attempts.items():
        try:
            qid = int(qid_str)
        except ValueError:
            continue
        q_info = q_map.get(qid)
        if not q_info:
            continue

        attempts = q_state.get("attempts", [])
        if isinstance(attempts, (int, float, str)):
            attempts = [str(attempts)]
        elif not isinstance(attempts, list):
            attempts = []

        # 1. Populate Module Sheet
        mod_code = q_info["module_code"]
        if mod_code in wb.sheetnames:
            ws = wb[mod_code]
            q_label = str(q_info["q_label"]).strip()
            for r in range(5, ws.max_row + 1):
                val = str(ws.cell(r, 1).value or "").strip()
                if val == q_label:
                    if len(attempts) >= 1 and attempts[0]:
                        ws.cell(r, 6, str(attempts[0]).strip().upper())
                    if len(attempts) >= 2 and attempts[1]:
                        ws.cell(r, 8, str(attempts[1]).strip().upper())
                    if len(attempts) >= 3 and attempts[2]:
                        ws.cell(r, 10, str(attempts[2]).strip().upper())
                    break

        # 2. Populate Master_All_98_Questions Sheet
        if "Master_All_98_Questions" in wb.sheetnames:
            ws_m = wb["Master_All_98_Questions"]
            master_id = f"M{qid}"
            for r in range(5, ws_m.max_row + 1):
                val = str(ws_m.cell(r, 1).value or "").strip()
                if val == master_id or r == (qid + 4):
                    if len(attempts) >= 1 and attempts[0]:
                        ws_m.cell(r, 7, str(attempts[0]).strip().upper())
                    if len(attempts) >= 2 and attempts[1]:
                        ws_m.cell(r, 9, str(attempts[1]).strip().upper())
                    if len(attempts) >= 3 and attempts[2]:
                        ws_m.cell(r, 11, str(attempts[2]).strip().upper())
                    break

    # 3. Populate SAT_Error_Log_Tracker Sheet (So_Tay_Loi_Sai_Tu_Vung structure)
    if "SAT_Error_Log_Tracker" in wb.sheetnames:
        ws_err = wb["SAT_Error_Log_Tracker"]
        # Clear old rows from row 2 to 200
        for r in range(2, max(50, ws_err.max_row + 1)):
            for c in range(1, 11):
                ws_err.cell(r, c, None)

        # Write student error logs with exact columns:
        # STT, Mã câu, Module, Chủ đề / Kỹ năng, Nhóm bẫy SAT, Phân tích nguyên nhân & Bài học, Ghi chú tư duy, Từ mới / Thuật ngữ, Tình trạng, Thời gian
        for idx, e in enumerate(error_logs):
            r = 2 + idx
            ws_err.cell(r, 1, idx + 1)
            ws_err.cell(r, 2, str(e.get("q_label") or f"Q{e.get('question_id', '')}"))
            ws_err.cell(r, 3, str(e.get("module") or ""))
            ws_err.cell(r, 4, str(e.get("skill") or ""))
            ws_err.cell(r, 5, str(e.get("root_cause") or "Bẫy SAT"))
            ws_err.cell(r, 6, str(e.get("trap_detail") or ""))
            ws_err.cell(r, 7, str(e.get("student_notes") or ""))
            ws_err.cell(r, 8, str(e.get("vocabulary") or ""))
            ws_err.cell(r, 9, str(e.get("status") or "Đang theo dõi"))
            ws_err.cell(r, 10, str(e.get("date") or datetime.datetime.now().strftime("%d/%m/%Y")))

    safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', student_name) or "Student"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    export_filename = f"October_2026_SAT_{safe_name}_{timestamp}.xlsx"

    import io
    buf = io.BytesIO()
    wb.save(buf)
    content = buf.getvalue()
    return content, export_filename, safe_name

def send_submission_email(student_name, student_email, summary, excel_bytes, excel_filename):
    config = load_email_config()
    teacher_email = config.get("teacher_email", "mikepham358@gmail.com")
    smtp_pass = config.get("smtp_pass", "").strip()
    smtp_host = config.get("smtp_host", "smtp.gmail.com")
    smtp_port = int(config.get("smtp_port", 465))
    smtp_user = config.get("smtp_user", teacher_email).strip()

    recipients = [teacher_email]
    if student_email and student_email != teacher_email and "@" in student_email:
        recipients.append(student_email)

    if not smtp_pass:
        return False, "Chưa thiết lập mật khẩu ứng dụng Gmail (smtp_pass) trong email_config.json. File đã được lưu vào thư mục submissions/ trên máy của Thầy Mike Pham Bá Hong Son.", recipients

    msg = MIMEMultipart()
    msg['From'] = f"Digital SAT Bluebook <{smtp_user}>"
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = f"📘 [Digital SAT Oct 2026] Báo cáo kết quả bài làm: {student_name}"

    answered = summary.get("answered", 0)
    total = summary.get("total", 98)
    l1 = summary.get("l1_correct", 0)
    l2 = summary.get("l2_correct", 0)
    l3 = summary.get("l3_correct", 0)
    score_pct = summary.get("score_pct", 0)
    time_spent = summary.get("time_spent", "N/A")

    html_content = f"""
    <html>
    <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 650px; margin: 0 auto; padding: 20px;">
        <div style="background: #0f172a; color: #ffffff; padding: 20px; border-radius: 8px 8px 0 0; text-align: center;">
            <h2 style="margin: 0 0 6px 0; color: #38bdf8;">📘 BÁO CÁO KẾT QUẢ DIGITAL SAT (BLUEBOOK)</h2>
            <p style="margin: 0; font-size: 14px; opacity: 0.9;">Đề thi: October 2026 Practice Test B</p>
        </div>
        <div style="border: 1px solid #e2e8f0; border-top: none; padding: 24px; border-radius: 0 0 8px 8px; background: #ffffff;">
            <h3 style="margin-top: 0; color: #0284c7; border-bottom: 2px solid #e0f2fe; padding-bottom: 8px;">Thông Tin Học Sinh</h3>
            <table style="width: 100%; margin-bottom: 20px; border-collapse: collapse;">
                <tr><td style="padding: 6px 0; color: #64748b; width: 140px;"><strong>Họ và tên:</strong></td><td style="font-size: 16px; font-weight: bold; color: #0f172a;">{student_name}</td></tr>
                <tr><td style="padding: 6px 0; color: #64748b;"><strong>Email học sinh:</strong></td><td>{student_email or "Chưa cung cấp"}</td></tr>
                <tr><td style="padding: 6px 0; color: #64748b;"><strong>Thời gian nộp:</strong></td><td>{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</td></tr>
                <tr><td style="padding: 6px 0; color: #64748b;"><strong>Thời gian làm bài:</strong></td><td>{time_spent}</td></tr>
            </table>

            <h3 style="color: #0284c7; border-bottom: 2px solid #e0f2fe; padding-bottom: 8px;">Tổng Kết Điểm & Lần Thử</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px; border-radius: 6px; text-align: center;">
                    <div style="font-size: 12px; color: #64748b;">Số câu đã làm</div>
                    <div style="font-size: 20px; font-weight: bold; color: #0f172a;">{answered} / {total}</div>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px; border-radius: 6px; text-align: center;">
                    <div style="font-size: 12px; color: #166534;">Hiệu suất điểm</div>
                    <div style="font-size: 20px; font-weight: bold; color: #15803d;">{score_pct}%</div>
                </div>
            </div>

            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 14px;">
                <tr style="background: #f1f5f9; text-align: left;">
                    <th style="padding: 8px 12px; border: 1px solid #e2e8f0;">Cấp độ thử</th>
                    <th style="padding: 8px 12px; border: 1px solid #e2e8f0;">Số câu đúng</th>
                    <th style="padding: 8px 12px; border: 1px solid #e2e8f0;">Hiệu suất</th>
                </tr>
                <tr>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0;">✅ Lần 1 (Đúng ngay lần đầu)</td>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0; font-weight: bold; color: #16a34a;">{l1}</td>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0;">100%</td>
                </tr>
                <tr>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0;">⚡ Lần 2 (Sau gợi ý Tầng 1)</td>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0; font-weight: bold; color: #d97706;">{l2}</td>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0;">66.7%</td>
                </tr>
                <tr>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0;">💡 Lần 3 (Sau gợi ý Tầng 2)</td>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0; font-weight: bold; color: #2563eb;">{l3}</td>
                    <td style="padding: 8px 12px; border: 1px solid #e2e8f0;">33.3%</td>
                </tr>
            </table>

            <p style="margin: 0; font-size: 13px; color: #64748b;">
                📎 <em>File Excel ghi nhận chi tiết kết quả từng câu hỏi đã được đính kèm cùng email này.</em>
            </p>
        </div>
        <div style="text-align: center; font-size: 12px; color: #94a3b8; margin-top: 16px;">
            Hệ thống Luyện thi Digital SAT Bluebook — Lớp học Thầy Mike Pham Bá Hong Son (Google for Education Innovator)
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_content, 'html', 'utf-8'))

    # Attach Excel
    part = MIMEApplication(excel_bytes, Name=excel_filename)
    part['Content-Disposition'] = f'attachment; filename="{excel_filename}"'
    msg.attach(part)

    try:
        if smtp_port == 465:
            with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=15) as server:
                server.login(smtp_user, smtp_pass)
                server.sendmail(smtp_user, recipients, msg.as_string())
        else:
            with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.sendmail(smtp_user, recipients, msg.as_string())
        return True, "Email đã được gửi thành công đến cả Thầy Mike Pham Bá Hong Son và Học sinh!", recipients
    except Exception as e:
        return False, f"Lỗi gửi email qua SMTP: {str(e)}", recipients

AAR_TEMPLATE_FILE = os.path.join(APP_DIR, "aar_template.xlsx")
AAR_TEACHER_RECIPIENTS = ["v.sonpbh1@vinschool.edu.vn", "mikepham@baoan.ai.vn"]

def generate_aar_excel(payload):
    import openpyxl
    import io

    student_name = str(payload.get("student_name") or "Student").strip() or "Hoc_Sinh"
    student_email = str(payload.get("student_email") or "").strip()
    logs = payload.get("logs") or []
    entry = payload.get("entry")
    if not logs and entry:
        logs = [entry]

    if os.path.exists(AAR_TEMPLATE_FILE):
        wb = openpyxl.load_workbook(AAR_TEMPLATE_FILE)
    else:
        wb = openpyxl.Workbook()
        ws_new = wb.active
        ws_new.title = "AAR Journal"

    ws = wb["AAR Journal"] if "AAR Journal" in wb.sheetnames else wb.active
    ws["B1"] = f"HỆ THỐNG THU THẬP & PHẢN TƯ SAU MỖI BUỔI HỌC - CHU TRÌNH AAR ({student_name} - {student_email or 'N/A'})"
    if logs:
        latest = logs[-1]
        ws["B6"] = f"Học sinh: {student_name} ({student_email or 'N/A'}) | Hiệu suất buổi gần nhất: Đúng {latest.get('correct_count', 0)}/{latest.get('practiced_count', 0)} câu thực hành ({latest.get('accuracy_pct', 0)}%)"

    for r in range(10, 101):
        for c in range(2, 15):
            cell = ws.cell(r, c)
            cell.value = None
            if cell.hyperlink is not None:
                cell.hyperlink = None

    for idx, item in enumerate(logs[:90]):
        r = 10 + idx
        ws.cell(r, 2, str(item.get("session_label") or f"Buổi {idx + 1}"))
        ws.cell(r, 3, str(item.get("date_display") or ""))
        ws.cell(r, 4, str(item.get("sat_module") or ""))
        ws.cell(r, 5, str(item.get("iste_standard") or ""))
        ws.cell(r, 6, str(item.get("goal") or ""))
        ws.cell(r, 7, str(item.get("challenge") or ""))
        ws.cell(r, 8, str(item.get("tools") or ""))
        ws.cell(r, 9, str(item.get("evidence") or ""))
        ws.cell(r, 10, str(item.get("mastery") or ""))
        ws.cell(r, 11, str(item.get("gap") or ""))
        ws.cell(r, 12, str(item.get("feedforward") or ""))
        ws.cell(r, 13, str(item.get("emotion") or ""))
        ws.cell(r, 14, str(item.get("status") or "Hoàn thành"))

    safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', student_name) or "Student"
    date_tag = datetime.datetime.now().strftime("%Y-%m-%d")
    export_filename = f"AAR_Cycle_Tracker_{safe_name}_{date_tag}.xlsx"

    buf = io.BytesIO()
    wb.save(buf)
    return buf.getvalue(), export_filename, safe_name

def send_aar_email(student_name, student_email, entry, excel_bytes, excel_filename):
    config = load_email_config()
    smtp_pass = config.get("smtp_pass", "").strip()
    smtp_host = config.get("smtp_host", "smtp.gmail.com")
    smtp_port = int(config.get("smtp_port", 465))
    smtp_user = config.get("smtp_user", "mikepham358@gmail.com").strip()

    to_list = list(AAR_TEACHER_RECIPIENTS)
    cc_list = [student_email] if (student_email and "@" in student_email and student_email not in to_list) else []
    all_recipients = to_list + cc_list

    if not smtp_pass:
        return False, "Chưa cấu hình smtp_pass trên server; client sẽ mở ứng dụng Email mặc định.", all_recipients

    msg = MIMEMultipart()
    msg['From'] = f"Digital SAT Bluebook <{smtp_user}>"
    msg['To'] = ", ".join(to_list)
    if cc_list:
        msg['Cc'] = ", ".join(cc_list)

    correct_c = int(entry.get("correct_count", 0))
    practiced_c = int(entry.get("practiced_count", 0))
    acc_pct = int(entry.get("accuracy_pct", 0))
    sess_lbl = entry.get("session_label", "Buổi học")
    sat_mod = entry.get("sat_module", "")
    msg['Subject'] = f"[SAT ARR Report] {student_name} - {sess_lbl} ({sat_mod}) - {correct_c}/{practiced_c} câu đúng ({acc_pct}%)"

    e_name = html.escape(str(student_name))
    e_email = html.escape(str(student_email or "Chưa cung cấp"))
    e_mod = html.escape(str(sat_mod))
    e_iste = html.escape(str(entry.get("iste_standard") or "").replace("\n", " "))
    e_goal = html.escape(str(entry.get("goal") or ""))
    e_chal = html.escape(str(entry.get("challenge") or ""))
    e_tools = html.escape(str(entry.get("tools") or ""))
    e_evid = html.escape(str(entry.get("evidence") or ""))
    e_mast = html.escape(str(entry.get("mastery") or ""))
    e_gap = html.escape(str(entry.get("gap") or ""))
    e_feed = html.escape(str(entry.get("feedforward") or ""))
    e_emo = html.escape(str(entry.get("emotion") or ""))
    e_stat = html.escape(str(entry.get("status") or ""))

    html_content = f"""
    <html>
    <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; line-height: 1.6; color: #0f172a; max-width: 680px; margin: 0 auto; padding: 20px;">
      <div style="background: #1e3a8a; color: #fff; padding: 18px 22px; border-radius: 10px 10px 0 0;">
        <h2 style="margin: 0; font-size: 18px;">📝 BÁO CÁO PHẢN TƯ SAU BUỔI HỌC (AAR / ARR CYCLE)</h2>
        <p style="margin: 4px 0 0; font-size: 13px; color: #cbd5e1;">Học sinh: {e_name} ({e_email})</p>
      </div>
      <div style="border: 1px solid #cbd5e1; border-top: none; padding: 20px 22px; border-radius: 0 0 10px 10px; background: #fff;">
        <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 12px 14px; margin-bottom: 16px;">
          <strong>📊 Hiệu suất thực hành trong buổi học:</strong> Đúng <strong>{correct_c} / {practiced_c}</strong> câu ({acc_pct}%)<br>
          <span style="font-size: 13px; color: #334155;">Lần 1: {entry.get('l1_correct', 0)} • Lần 2: {entry.get('l2_correct', 0)} • Lần 3: {entry.get('l3_correct', 0)} • Chưa đúng: {entry.get('missed_count', 0)}</span>
        </div>
        <p><strong>Buổi:</strong> {html.escape(str(sess_lbl))} • <strong>Ngày:</strong> {html.escape(str(entry.get('date_display', '')))} • <strong>Mô-đun:</strong> {e_mod}</p>
        <p><strong>1. Dự đoán (Anticipation):</strong> ISTE: {e_iste}<br>Mục tiêu: {e_goal}<br>Thách thức: {e_chal}</p>
        <p><strong>2. Hành động (Action):</strong> Công cụ: {e_tools}<br>Minh chứng: {e_evid}<br>Mức độ làm chủ: {e_mast}</p>
        <p><strong>3. Phản tư (Reflection):</strong> Gap: {e_gap}<br>Feed-forward: {e_feed}<br>Cảm xúc: {e_emo} • Trạng thái: {e_stat}</p>
      </div>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))
    part = MIMEApplication(excel_bytes, Name=excel_filename)
    part['Content-Disposition'] = f'attachment; filename="{excel_filename}"'
    msg.attach(part)

    try:
        if smtp_port == 465:
            with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=15) as server:
                server.login(smtp_user, smtp_pass)
                server.sendmail(smtp_user, all_recipients, msg.as_string())
        else:
            with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.sendmail(smtp_user, all_recipients, msg.as_string())
        return True, "Đã gửi email báo cáo ARR thành công!", all_recipients
    except Exception as e:
        return False, f"Lỗi gửi email ARR qua SMTP: {str(e)}", all_recipients

def send_feedback_email_notification(fb_item):
    config = load_email_config()
    teacher_email = config.get("teacher_email", "mikepham358@gmail.com")
    smtp_pass = config.get("smtp_pass", "").strip()
    smtp_host = config.get("smtp_host", "smtp.gmail.com")
    smtp_port = int(config.get("smtp_port", 465))
    smtp_user = config.get("smtp_user", teacher_email).strip()

    if not smtp_pass:
        print("ℹ️ [Email Feedback Notification] SMTP password not set. Direct email dispatch ready via mailto / GitHub alerts.")
        return False, "Chưa thiết lập mật khẩu ứng dụng Gmail (App Password)."

    try:
        msg = MIMEMultipart()
        msg["From"] = f"Vinschool SAT Team <{smtp_user}>"
        msg["To"] = teacher_email
        recipients = [teacher_email]
        if fb_item.get("student_email") and "@" in fb_item["student_email"]:
            msg["Cc"] = fb_item["student_email"]
            recipients.append(fb_item["student_email"])

        subject = f"[SAT Bluebook Feedback - {fb_item.get('id', 'FB')}] {fb_item.get('category')} - {fb_item.get('context_label')}"
        msg["Subject"] = subject

        html_body = f"""
        <html>
        <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b;">
          <div style="max-width: 600px; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; background: #ffffff;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 16px;">
              <span style="font-size: 24px;">💬</span>
              <h2 style="margin: 0; color: #0f172a; font-size: 18px;">Phản Hồi & Báo Lỗi Mới từ Học Sinh</h2>
            </div>
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 16px; font-size: 14px;">
              <tr><td style="padding: 6px 0; color: #64748b; width: 140px;">Mã phản hồi:</td><td><strong>{fb_item.get('id')}</strong></td></tr>
              <tr><td style="padding: 6px 0; color: #64748b;">Học sinh:</td><td><strong>{fb_item.get('student_name')}</strong> ({fb_item.get('student_email') or 'Chưa cung cấp'})</td></tr>
              <tr><td style="padding: 6px 0; color: #64748b;">Phân loại:</td><td><span style="padding: 2px 8px; background: #eff6ff; color: #1d4ed8; border-radius: 4px; font-weight: 600;">{fb_item.get('category')}</span></td></tr>
              <tr><td style="padding: 6px 0; color: #64748b;">Mức độ ưu tiên:</td><td><strong>{fb_item.get('priority')}</strong></td></tr>
              <tr><td style="padding: 6px 0; color: #64748b;">Ngữ cảnh / Vị trí:</td><td>{fb_item.get('context_label')}</td></tr>
              <tr><td style="padding: 6px 0; color: #64748b;">Thời gian:</td><td>{fb_item.get('date_str')}</td></tr>
            </table>
            <div style="padding: 14px; background: #f8fafc; border-left: 4px solid #3b82f6; border-radius: 6px; margin-bottom: 20px;">
              <div style="font-size: 12px; font-weight: 700; color: #475569; text-transform: uppercase; margin-bottom: 4px;">Nội dung phản hồi:</div>
              <div style="font-size: 14px; color: #0f172a; white-space: pre-wrap;">{fb_item.get('content')}</div>
            </div>
            <div style="font-size: 12px; color: #94a3b8; text-align: center; border-top: 1px solid #f1f5f9; padding-top: 12px;">
              Digital SAT Bluebook Practice App • Vinschool SAT Team
            </div>
          </div>
        </body>
        </html>
        """
        msg.attach(MIMEText(html_body, "html", "utf-8"))

        if smtp_port == 465:
            with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=15) as server:
                server.login(smtp_user, smtp_pass)
                server.sendmail(smtp_user, recipients, msg.as_string())
        else:
            with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.sendmail(smtp_user, recipients, msg.as_string())

        print(f"✅ [Feedback Email] Notification sent successfully to {teacher_email}!")
        return True, "Email đã được gửi thành công!"
    except Exception as e:
        print(f"⚠️ [Feedback Email Error] {e}")
        return False, str(e)

def notify_feedback_email_async(fb_item):
    t = threading.Thread(target=send_feedback_email_notification, args=(fb_item,), daemon=True)
    t.start()

class BluebookAppHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, DELETE, HEAD')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Range')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_HEAD(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        if path == "/pdf":
            pdf_path = DB["pdf_path"]
            if os.path.exists(pdf_path):
                file_size = os.path.getsize(pdf_path)
                self.send_response(200)
                self.send_header('Content-Type', 'application/pdf')
                self.send_header('Content-Length', str(file_size))
                self.send_header('Accept-Ranges', 'bytes')
                self.end_headers()
            else:
                self.send_error(404, "PDF not found")
            return

        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        if path == "/pdf":
            self.serve_pdf(DB["pdf_path"])
            return

        if path == "/api/manifest":
            manifest_file = os.path.join(APP_DIR, "data", "manifest.json")
            if os.path.exists(manifest_file):
                try:
                    with open(manifest_file, "r", encoding="utf-8") as f:
                        self.send_json(json.load(f))
                    return
                except Exception:
                    pass
            self.send_json([])
            return

        if path == "/api/data":
            parsed_qs = urllib.parse.parse_qs(parsed_url.query)
            test_req = parsed_qs.get("test", [""])[0]
            target_file = DATABASE_FILE
            if test_req:
                clean_test = test_req.replace("-", "").lower()
                cand = os.path.join(APP_DIR, "data", f"{clean_test}.json")
                if os.path.exists(cand):
                    target_file = cand
            try:
                with open(target_file, "r", encoding="utf-8") as f:
                    db_fresh = json.load(f)
                self.send_json(db_fresh)
            except Exception as e:
                self.send_json(DB)
            return

        if path == "/api/feedbacks":
            self.send_json(load_feedbacks())
            return

        if path.startswith("/api/download-submission"):
            parsed_qs = urllib.parse.parse_qs(parsed_url.query)
            filename = parsed_qs.get("file", [""])[0]
            clean_name = os.path.basename(filename)
            file_path = os.path.join(SUBMISSIONS_DIR, clean_name)
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                self.send_header("Content-Disposition", f'attachment; filename="{clean_name}"')
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return
            else:
                self.send_error(404, "File not found")
                return

        # Static files
        self.serve_static(path)

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else "{}"
        
        try:
            payload = json.loads(body)
        except Exception:
            payload = {}

        if path == "/api/export-excel":
            self.handle_export_excel(payload)
            return

        if path == "/api/submit-test":
            self.handle_submit_test(payload)
            return

        if path == "/api/submit-aar":
            self.handle_submit_aar(payload)
            return

        if path == "/api/feedback":
            self.handle_add_feedback(payload)
            return

        self.send_error(404, "Endpoint not found")

    def handle_add_feedback(self, payload):
        try:
            feedbacks = load_feedbacks()
            now = datetime.datetime.now()
            fb_id = f"FB-{now.strftime('%Y%m%d')}-{len(feedbacks)+1:03d}"
            
            fb_item = {
                "id": fb_id,
                "timestamp": now.isoformat(),
                "date_str": now.strftime("%d/%m/%Y %H:%M"),
                "student_name": payload.get("student_name", "Ẩn danh").strip() or "Ẩn danh",
                "student_email": payload.get("student_email", "").strip(),
                "category": payload.get("category", "📝 Góp ý chung").strip(),
                "priority": payload.get("priority", "🟢 Bình thường").strip(),
                "context_label": payload.get("context_label", "Hệ thống").strip(),
                "content": payload.get("content", "").strip(),
                "status": "⏳ Đang xử lý (Open)"
            }

            if not fb_item["content"]:
                self.send_json({"success": False, "error": "Nội dung phản hồi không được để trống."}, 400)
                return

            feedbacks.append(fb_item)
            save_feedbacks_and_update_log(feedbacks)
            sync_feedback_to_github_async(fb_item)
            notify_feedback_email_async(fb_item)

            self.send_json({
                "success": True,
                "item": fb_item,
                "message": f"Phản hồi [{fb_id}] đã được ghi nhận và đang tự động cập nhật vào GitHub!",
                "github_url": "https://github.com/mikepham358/vinschool-sat-team/blob/main/FEEDBACK_LOG.md"
            })
        except Exception as e:
            self.send_json({"success": False, "error": f"Lỗi khi xử lý phản hồi: {str(e)}"}, 500)

    # --- PDF STREAMING WITH HTTP RANGE SUPPORT ---

    def serve_pdf(self, pdf_path):
        if not os.path.exists(pdf_path):
            self.send_error(404, "PDF file not found")
            return

        file_size = os.path.getsize(pdf_path)
        range_header = self.headers.get('Range', None)

        if range_header:
            match = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if match:
                start = int(match.group(1))
                end = int(match.group(2)) if match.group(2) else file_size - 1
                end = min(end, file_size - 1)
                length = end - start + 1

                self.send_response(206)
                self.send_header('Content-Type', 'application/pdf')
                self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
                self.send_header('Content-Length', str(length))
                self.send_header('Accept-Ranges', 'bytes')
                self.end_headers()

                with open(pdf_path, 'rb') as f:
                    f.seek(start)
                    chunk_size = 64 * 1024
                    bytes_remaining = length
                    while bytes_remaining > 0:
                        read_bytes = min(chunk_size, bytes_remaining)
                        data = f.read(read_bytes)
                        if not data:
                            break
                        self.wfile.write(data)
                        bytes_remaining -= len(data)
                return

        self.send_response(200)
        self.send_header('Content-Type', 'application/pdf')
        self.send_header('Content-Length', str(file_size))
        self.send_header('Accept-Ranges', 'bytes')
        self.end_headers()
        with open(pdf_path, 'rb') as f:
            shutil.copyfileobj(f, self.wfile)

    # --- PERSONALIZED EXCEL EXPORT & SUBMISSION ---

    def handle_export_excel(self, payload):
        try:
            content, export_filename, safe_name = generate_student_excel(payload)

            self.send_response(200)
            self.send_header("Content-Type", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            self.send_header("Content-Disposition", f'attachment; filename="{export_filename}"')
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_json({"error": f"Failed to export excel: {str(e)}"}, 500)

    def handle_submit_test(self, payload):
        try:
            student_name = payload.get("student_name", "Student").strip() or "Hoc_Sinh"
            student_email = payload.get("student_email", "").strip()
            summary = payload.get("summary", {})

            # 1. Generate Excel in memory
            content, export_filename, safe_name = generate_student_excel(payload)

            # 2. Save file copy to submissions folder on teacher's machine
            save_path = os.path.join(SUBMISSIONS_DIR, export_filename)
            with open(save_path, "wb") as f:
                f.write(content)

            # 3. Dispatch Email to teacher and student
            sent, msg, recipients = send_submission_email(student_name, student_email, summary, content, export_filename)

            self.send_json({
                "success": True,
                "email_sent": sent,
                "message": msg,
                "recipients": recipients,
                "filename": export_filename,
                "download_url": f"/api/download-submission?file={urllib.parse.quote(export_filename)}"
            })
        except Exception as e:
            self.send_json({"success": False, "error": f"Failed to submit test: {str(e)}"}, 500)

    def handle_submit_aar(self, payload):
        try:
            student_name = str(payload.get("student_name") or "Student").strip() or "Hoc_Sinh"
            student_email = str(payload.get("student_email") or "").strip()
            entry = payload.get("entry") or {}

            content, export_filename, safe_name = generate_aar_excel(payload)
            save_path = os.path.join(SUBMISSIONS_DIR, export_filename)
            with open(save_path, "wb") as f:
                f.write(content)

            sent, msg, recipients = send_aar_email(student_name, student_email, entry, content, export_filename)
            self.send_json({
                "success": True,
                "email_sent": sent,
                "message": msg,
                "recipients": recipients,
                "filename": export_filename,
                "download_url": f"/api/download-submission?file={urllib.parse.quote(export_filename)}"
            })
        except Exception as e:
            self.send_json({"success": False, "error": f"Failed to submit ARR report: {str(e)}"}, 500)

    # --- UTILS ---

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def serve_static(self, path):
        if path == "/" or path == "":
            path = "/index.html"
        clean_path = path.lstrip("/")
        file_path = os.path.join(STATIC_DIR, clean_path)
        if not os.path.exists(file_path):
            file_path = os.path.join(APP_DIR, clean_path)

        if not os.path.exists(file_path) or os.path.isdir(file_path):
            self.send_error(404, "File not found")
            return

        mime = "application/octet-stream"
        if file_path.endswith(".html"):
            mime = "text/html; charset=utf-8"
        elif file_path.endswith(".css"):
            mime = "text/css; charset=utf-8"
        elif file_path.endswith(".js"):
            mime = "application/javascript; charset=utf-8"
        elif file_path.endswith(".json"):
            mime = "application/json; charset=utf-8"
        elif file_path.endswith(".png"):
            mime = "image/png"
        elif file_path.endswith(".svg"):
            mime = "image/svg+xml"

        with open(file_path, "rb") as f:
            content = f.read()

        self.send_response(200)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)

def start_github_issue_polling():
    def _worker():
        import time
        try:
            from sync_github_issues import sync
        except Exception as e:
            print(f"Notice: sync_github_issues module not loaded: {e}")
            return
        # Initial wait before first sync
        time.sleep(5)
        while True:
            try:
                sync()
            except Exception as e:
                pass
            time.sleep(60)

    t = threading.Thread(target=_worker, daemon=True)
    t.start()

def run(port=8085):
    server_address = ('', port)
    httpd = HTTPServer(server_address, BluebookAppHandler)
    print(f"🚀 Bluebook SAT Practice Engine running at: http://localhost:{port}")
    start_github_issue_polling()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8085
    run(port)
