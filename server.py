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

def _clean_text_for_excel(raw, max_len=30000):
    if raw is None:
        return ""
    s = str(raw)
    s = re.sub(r"<\s*br\s*/?>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"</\s*(p|div|li|h[1-6]|tr)\s*>", "\n", s, flags=re.IGNORECASE)
    s = re.sub(r"<li[^>]*>", "• ", s, flags=re.IGNORECASE)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n[ \t]+", "\n", s)
    s = re.sub(r"[ \t]{2,}", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    if len(s) > max_len:
        s = s[: max_len - 3] + "..."
    return s


def _parse_socratic_vocab_entries(vocab_text):
    if not vocab_text:
        return []
    lines = [ln.strip() for ln in re.split(r"[\n;]+", str(vocab_text)) if ln.strip()]
    parsed = []
    for ln in lines:
        m = re.match(r"^(.*?)\s*(?:[:=–—]|\s+-\s+)\s*(.+)$", ln)
        if m and m.group(1).strip() and m.group(2).strip():
            parsed.append({"term": m.group(1).strip(), "meaning": m.group(2).strip()})
        else:
            parsed.append({"term": ln, "meaning": ""})
    return parsed


def _build_question_tier_feedbacks(q):
    if not q:
        return {"tier1": "", "tier2": "", "tier3": "", "tier4": ""}
    tier1 = _clean_text_for_excel(q.get("tier1_hint") or q.get("level1_tip") or "")
    tier2 = _clean_text_for_excel(q.get("tier2_hint") or q.get("level2_hint") or "")

    t3_parts = []
    base_t3 = _clean_text_for_excel(q.get("tier3_hint") or q.get("level3_solution") or "")
    if base_t3:
        t3_parts.append(base_t3)
    for key, label in [
        ("solution_steps", "Các bước giải"),
        ("pooe_breakdown", "Phân tích loại trừ (POOE)"),
        ("grid_in_explanation", "Hướng dẫn điền số (Grid-In)"),
    ]:
        val = _clean_text_for_excel(q.get(key) or "")
        if val and (not base_t3 or val[:40] not in base_t3):
            t3_parts.append(f"{label}:\n{val}")
    tier3 = _clean_text_for_excel("\n\n".join(t3_parts))

    t4_parts = []
    if q.get("princeton_strategy"):
        t4_parts.append(f"Chiến thuật Princeton Review: {_clean_text_for_excel(q.get('princeton_strategy'))}")
    if q.get("target_clue"):
        t4_parts.append(f"Phân tích manh mối & Target: {_clean_text_for_excel(q.get('target_clue'))}")
    if q.get("pro_tip"):
        t4_parts.append(f"Mẹo độc quyền Pro-Tip: {_clean_text_for_excel(q.get('pro_tip'))}")
    strat_tip = _clean_text_for_excel(q.get("strategic_tip") or "")
    if strat_tip:
        t4_parts.append(f"Chiến thuật / Công thức cốt lõi: {strat_tip}" if t4_parts else strat_tip)
    tier4 = _clean_text_for_excel("\n\n".join(t4_parts))

    return {"tier1": tier1, "tier2": tier2, "tier3": tier3, "tier4": tier4}


def _format_question_prompt_for_excel(q):
    if not q:
        return ""
    parts = []
    passage = _clean_text_for_excel(q.get("passage") or "", 12000)
    prompt = _clean_text_for_excel(q.get("prompt") or "", 4000)
    if passage:
        parts.append(f"[Ngữ liệu]: {passage}")
    if prompt:
        parts.append(f"[Câu hỏi]: {prompt}")
    if q.get("is_grid_in"):
        parts.append("[Hình thức]: Tự luận điền đáp án (Grid-in)")
    elif isinstance(q.get("options"), list) and q.get("options"):
        opts = " | ".join(f"{o.get('key', '')}) {_clean_text_for_excel(o.get('text', ''), 1000)}" for o in q["options"])
        if opts:
            parts.append(f"[Phương án]: {opts}")
    elif q.get("options_raw"):
        parts.append(f"[Phương án]: {_clean_text_for_excel(q.get('options_raw'), 4000)}")
    return _clean_text_for_excel("\n".join(parts), 20000)


def _build_export_data_from_legacy_payload(payload):
    student_name = (payload.get("student_name") or "Hoc_Sinh").strip() or "Hoc_Sinh"
    student_email = (payload.get("student_email") or "").strip() or "Chưa cung cấp"
    student_target = payload.get("student_target") or "1400+"
    user_attempts = payload.get("attempts") or {}
    raw_errors = [e for e in (payload.get("error_logs") or []) if isinstance(e, dict) and not str(e.get("id", "")).startswith("err_oct_")]

    questions = DB.get("questions", []) if isinstance(DB, dict) else []
    q_by_id = {str(q.get("id")): q for q in questions}
    test_short = (DB.get("test_title") if isinstance(DB, dict) else "") or "Digital SAT"

    err_by_qid = {}
    for err in raw_errors:
        err_by_qid.setdefault(str(err.get("question_id") or ""), []).append(err)

    practiced_rows = []
    by_module = {}
    total_practiced = total_correct = total_l1 = total_l2 = total_l3 = 0
    total_weight = 0.0

    for q in questions:
        qid_str = str(q.get("id"))
        st = user_attempts.get(qid_str) or user_attempts.get(q.get("id"))
        if not isinstance(st, dict):
            continue
        atts = st.get("attempts") or []
        if not isinstance(atts, list) or len(atts) == 0:
            continue

        status = str(st.get("status") or "")
        try:
            eff = float(st.get("efficiency") or 0)
        except (TypeError, ValueError):
            eff = 0.0
        is_l1 = eff >= 0.99 or status == "mastered_l1"
        is_l2 = (not is_l1) and (eff >= 0.6 or status == "mastered_l2")
        is_l3 = (not is_l1) and (not is_l2) and (eff >= 0.3 or status == "mastered_l3")
        is_corr = is_l1 or is_l2 or is_l3

        status_label = "Đang thử lại (Chưa hoàn thành)"
        if is_l1:
            status_label = "Đúng Lần 1 (L1 - 100%)"
        elif is_l2:
            status_label = "Đúng Lần 2 (L2 - 66.7%)"
        elif is_l3:
            status_label = "Đúng Lần 3 (L3 - 33.3%)"
        elif status == "missed" or len(atts) >= 3:
            status_label = "Sai cả 3 lần (0%)"

        total_practiced += 1
        if is_corr:
            total_correct += 1
        if is_l1:
            total_l1 += 1
        elif is_l2:
            total_l2 += 1
        elif is_l3:
            total_l3 += 1
        total_weight += eff

        mod_title = q.get("module_title") or q.get("module_code") or "SAT"
        m_stat = by_module.setdefault(
            mod_title,
            {"test_short": test_short, "module_title": mod_title, "practiced": 0, "correct": 0, "l1": 0, "l2": 0, "l3": 0, "weight": 0.0},
        )
        m_stat["practiced"] += 1
        if is_corr:
            m_stat["correct"] += 1
        if is_l1:
            m_stat["l1"] += 1
        elif is_l2:
            m_stat["l2"] += 1
        elif is_l3:
            m_stat["l3"] += 1
        m_stat["weight"] += eff

        tiers = _build_question_tier_feedbacks(q)
        err_summary = "\n".join(
            f"[{e.get('root_cause') or 'Sổ thử sai'}] {_clean_text_for_excel(e.get('trap_detail') or '')}"
            + (f" | Ghi chú: {_clean_text_for_excel(e.get('student_notes'))}" if e.get("student_notes") else "")
            for e in err_by_qid.get(qid_str, [])
        )
        practiced_rows.append({
            "stt": len(practiced_rows) + 1,
            "test_short": test_short,
            "module_title": mod_title,
            "q_label": q.get("q_label") or f"Q{qid_str}",
            "topic": q.get("topic") or "",
            "page_label": f"PDF tr.{q['pdf_page']}" if q.get("pdf_page") else "",
            "difficulty": q.get("difficulty") or "",
            "question_content": _format_question_prompt_for_excel(q),
            "attempt_1": str(atts[0]) if len(atts) >= 1 else "",
            "attempt_2": str(atts[1]) if len(atts) >= 2 else "",
            "attempt_3": str(atts[2]) if len(atts) >= 3 else "",
            "correct_answer": str(q.get("correct_answer") or ""),
            "status_label": status_label,
            "efficiency_pct": round(eff * 100),
            "tier1_feedback": tiers["tier1"],
            "tier2_feedback": tiers["tier2"],
            "tier3_feedback": tiers["tier3"],
            "tier4_feedback": tiers["tier4"],
            "error_note_summary": err_summary,
            "practiced_at": str(st.get("last_practiced_at") or ""),
        })

    error_logs_out = []
    vocab_out = []
    for err in raw_errors:
        q = q_by_id.get(str(err.get("question_id") or ""))
        wrongs = err.get("wrong_attempts")
        wrongs_text = ", ".join(str(w) for w in wrongs) if isinstance(wrongs, list) else str(wrongs or "")
        vocab_raw = _clean_text_for_excel(err.get("vocabulary") or "")
        row = {
            "stt": len(error_logs_out) + 1,
            "test_short": test_short,
            "q_label": str(err.get("q_label") or (q.get("q_label") if q else "") or f"Q{err.get('question_id', '')}"),
            "module": _clean_text_for_excel(err.get("module") or (q.get("module_title") if q else "") or "SAT"),
            "skill": _clean_text_for_excel(err.get("skill") or (q.get("topic") if q else "") or ""),
            "wrong_attempts": wrongs_text,
            "correct_answer": str(err.get("correct_answer") or (q.get("correct_answer") if q else "") or ""),
            "root_cause": _clean_text_for_excel(err.get("root_cause") or "Bẫy SAT"),
            "trap_detail": _clean_text_for_excel(err.get("trap_detail") or ""),
            "student_notes": _clean_text_for_excel(err.get("student_notes") or ""),
            "vocabulary": vocab_raw,
            "socratic_analysis": _clean_text_for_excel(err.get("socratic_analysis") or (q.get("tier1_hint") or q.get("level1_tip") if q else "") or ""),
            "status": _clean_text_for_excel(err.get("status") or "Đang theo dõi"),
            "date": str(err.get("date") or datetime.datetime.now().strftime("%d/%m/%Y")),
        }
        error_logs_out.append(row)
        if vocab_raw:
            for vt in _parse_socratic_vocab_entries(vocab_raw):
                vocab_out.append({
                    "stt": len(vocab_out) + 1,
                    "test_short": test_short,
                    "q_label": row["q_label"],
                    "module_skill": " • ".join(p for p in [row["module"], row["skill"]] if p),
                    "term": vt["term"],
                    "meaning": vt["meaning"],
                    "context_note": " | ".join(p for p in [row["root_cause"], row["student_notes"]] if p),
                    "date": row["date"],
                })

    acc_pct = round((total_correct / total_practiced) * 100) if total_practiced > 0 else 0
    w_pct = round((total_weight / total_practiced) * 100) if total_practiced > 0 else 0
    by_test = [{
        "test_short": test_short,
        "practiced": total_practiced,
        "correct": total_correct,
        "unfinished_or_missed": max(0, total_practiced - total_correct),
        "l1": total_l1,
        "l2": total_l2,
        "l3": total_l3,
        "accuracy_pct": acc_pct,
        "weighted_pct": w_pct,
    }] if total_practiced > 0 else []

    by_mod_list = []
    for m in by_module.values():
        p = m["practiced"]
        by_mod_list.append({
            "test_short": m["test_short"],
            "module_title": m["module_title"],
            "practiced": p,
            "correct": m["correct"],
            "unfinished_or_missed": max(0, p - m["correct"]),
            "l1": m["l1"],
            "l2": m["l2"],
            "l3": m["l3"],
            "accuracy_pct": round((m["correct"] / p) * 100) if p > 0 else 0,
            "weighted_pct": round((m["weight"] / p) * 100) if p > 0 else 0,
        })

    return {
        "generated_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "student": {
            "name": student_name,
            "email": student_email,
            "target": student_target,
            "sources_summary": f"{test_short} ({total_correct}/{total_practiced})" if total_practiced else test_short,
        },
        "overall": {
            "total_practiced": total_practiced,
            "total_correct": total_correct,
            "total_unfinished_or_missed": max(0, total_practiced - total_correct),
            "l1_correct": total_l1,
            "l2_correct": total_l2,
            "l3_correct": total_l3,
            "accuracy_pct": acc_pct,
            "weighted_pct": w_pct,
            "error_logs_count": len(error_logs_out),
            "vocab_notes_count": sum(1 for e in error_logs_out if e["vocabulary"]),
            "vocab_terms_count": len(vocab_out),
            "session_practiced": total_practiced,
            "session_correct": total_correct,
            "session_accuracy_pct": acc_pct,
        },
        "by_test": by_test,
        "by_module": by_mod_list,
        "practiced_questions": practiced_rows,
        "error_logs": error_logs_out,
        "vocab_entries": vocab_out,
    }


def generate_student_excel(payload):
    import io
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter

    export_data = payload.get("export_data")
    if not isinstance(export_data, dict) or "practiced_questions" not in export_data:
        export_data = _build_export_data_from_legacy_payload(payload)

    st_info = export_data.get("student") or {}
    ov = export_data.get("overall") or {}

    student_name = str(st_info.get("name") or payload.get("student_name") or "Hoc_Sinh").strip() or "Hoc_Sinh"
    student_email = str(st_info.get("email") or payload.get("student_email") or "Chưa cung cấp").strip() or "Chưa cung cấp"
    student_target = str(st_info.get("target") or payload.get("student_target") or "1400+")
    now_str = str(export_data.get("generated_at") or datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    wb = openpyxl.Workbook()
    ws_perf = wb.active
    ws_perf.title = "Hieu_Suat_Lam_Bai"

    # Shared styles
    title_fill = PatternFill(start_color="1A73E8", end_color="1A73E8", fill_type="solid")
    sub_fill = PatternFill(start_color="E8F0FE", end_color="E8F0FE", fill_type="solid")
    sec_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
    th_fill = PatternFill(start_color="1D4ED8", end_color="1D4ED8", fill_type="solid")
    zebra_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    total_fill = PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")
    green_fill = PatternFill(start_color="E6F4EA", end_color="E6F4EA", fill_type="solid")
    amber_fill = PatternFill(start_color="FEF7E0", end_color="FEF7E0", fill_type="solid")
    red_fill = PatternFill(start_color="FCE8E6", end_color="FCE8E6", fill_type="solid")

    font_title = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    font_sub = Font(name="Calibri", size=10, italic=True, color="1E3A8A")
    font_sec = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    font_th = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
    font_bold = Font(name="Calibri", size=10, bold=True, color="0F172A")
    font_body = Font(name="Calibri", size=10, color="1E293B")

    thin_side = Side(style="thin", color="CBD5E1")
    border_thin = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
    align_left = Alignment(horizontal="left", vertical="top", wrap_text=True)
    align_center = Alignment(horizontal="center", vertical="top", wrap_text=True)
    align_banner = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # ---- Sheet 1: Hieu_Suat_Lam_Bai ----
    ws_perf.merge_cells("A1:I1")
    ws_perf["A1"] = "BÁO CÁO TỔNG HỢP THỰC HÀNH DIGITAL SAT BLUEBOOK (SOCRATIC)"
    ws_perf["A1"].font = font_title
    ws_perf["A1"].fill = title_fill
    ws_perf["A1"].alignment = align_banner
    ws_perf.row_dimensions[1].height = 30

    ws_perf.merge_cells("A2:I2")
    ws_perf["A2"] = "Thông tin học sinh & Hiệu suất làm bài • Phản hồi đa tầng • Sổ tay Thử sai & Từ vựng Socratic"
    ws_perf["A2"].font = font_sub
    ws_perf["A2"].fill = sub_fill
    ws_perf["A2"].alignment = align_banner
    ws_perf.row_dimensions[2].height = 20

    def _add_perf_section_bar(row_idx, text):
        ws_perf.merge_cells(start_row=row_idx, start_column=1, end_row=row_idx, end_column=9)
        c = ws_perf.cell(row_idx, 1, text)
        c.font = font_sec
        c.fill = sec_fill
        c.alignment = Alignment(horizontal="left", vertical="center")
        ws_perf.row_dimensions[row_idx].height = 22

    _add_perf_section_bar(4, "1. THÔNG TIN HỌC SINH & PHIÊN XUẤT BÁO CÁO")
    meta_rows = [
        ("Họ và tên học sinh", student_name),
        ("Email học sinh", student_email),
        ("Mục tiêu điểm SAT", student_target),
        ("Nguồn tài liệu / Bộ đề đã thực hành", st_info.get("sources_summary") or "Chưa có dữ liệu"),
        ("Thời gian xuất báo cáo", now_str),
        ("Giáo viên hướng dẫn", "Mike Pham Bá Hong Son • mikepham358@gmail.com"),
    ]
    r_cur = 5
    for label, val in meta_rows:
        c1 = ws_perf.cell(r_cur, 1, label)
        c1.font = font_bold
        c1.fill = zebra_fill
        c1.border = border_thin
        c1.alignment = align_left
        ws_perf.merge_cells(start_row=r_cur, start_column=2, end_row=r_cur, end_column=9)
        for col_i in range(2, 10):
            cell_m = ws_perf.cell(r_cur, col_i)
            cell_m.border = border_thin
        c2 = ws_perf.cell(r_cur, 2, val)
        c2.font = font_body
        c2.alignment = align_left
        ws_perf.row_dimensions[r_cur].height = 20
        r_cur += 1

    r_cur += 1
    _add_perf_section_bar(r_cur, "2. HIỆU SUẤT LÀM BÀI TỔNG HỢP")
    r_cur += 1
    for c_i, h_text in enumerate(["Chỉ số hiệu suất", "Giá trị", "Diễn giải / Ghi chú"], start=1):
        c = ws_perf.cell(r_cur, c_i, h_text)
        c.font = font_th
        c.fill = th_fill
        c.border = border_thin
        c.alignment = align_center
    ws_perf.merge_cells(start_row=r_cur, start_column=3, end_row=r_cur, end_column=9)
    for col_i in range(3, 10):
        ws_perf.cell(r_cur, col_i).fill = th_fill
        ws_perf.cell(r_cur, col_i).border = border_thin
    ws_perf.row_dimensions[r_cur].height = 22
    r_cur += 1

    kpi_rows = [
        ("Tổng số câu đã thực hành", ov.get("total_practiced", 0), "Tổng số câu đã có ít nhất 1 lần chọn đáp án xuyên suốt các bộ đề"),
        ("Số câu hoàn thành đúng", ov.get("total_correct", 0), "Trả lời chính xác ở Lần 1, Lần 2 hoặc Lần 3"),
        ("Chưa hoàn thành / Sai cả 3 lần", ov.get("total_unfinished_or_missed", 0), "Cần ôn lại gợi ý đa tầng và ghi chú Sổ thử sai"),
        ("Tỷ lệ chính xác (Đúng / Đã làm)", f"{ov.get('accuracy_pct', 0)}%", "Tỷ lệ số câu hoàn thành đúng trên tổng số câu đã thực hành"),
        ("Hiệu suất Socratic (Có trọng số)", f"{ov.get('weighted_pct', 0)}%", "Trọng số Socratic: Đúng Lần 1 = 100%, Lần 2 = 66.7%, Lần 3 = 33.3%"),
        ("Đúng ngay Lần 1 (L1 - 100%)", ov.get("l1_correct", 0), "Làm đúng độc lập không cần mở gợi ý"),
        ("Đúng ở Lần 2 (L2 - 66.7%)", ov.get("l2_correct", 0), "Điều chỉnh đúng sau Phản hồi Tầng 1"),
        ("Đúng ở Lần 3 (L3 - 33.3%)", ov.get("l3_correct", 0), "Hoàn thành sau Phản hồi Tầng 2"),
        ("Tổng ghi chép Sổ tay Thử sai Socratic", ov.get("error_logs_count", 0), "Số thẻ phân tích bẫy SAT & bài học đã lưu"),
        ("Số mục Từ vựng Socratic đã ghi", ov.get("vocab_terms_count", 0), f"{ov.get('vocab_notes_count', 0)} thẻ ghi chép có từ mới / thuật ngữ"),
        ("Phiên học hiện tại (Bộ đếm ARR)", f"{ov.get('session_correct', 0)}/{ov.get('session_practiced', 0)} câu ({ov.get('session_accuracy_pct', 0)}%)", "Thống kê xuyên suốt phiên học hiện tại (khi chuyển đổi giữa các bộ đề)"),
    ]
    for idx_k, (lbl, val, desc) in enumerate(kpi_rows):
        fill_use = zebra_fill if idx_k % 2 == 1 else PatternFill(fill_type=None)
        c1 = ws_perf.cell(r_cur, 1, lbl)
        c1.font = font_bold
        c1.alignment = align_left
        c1.border = border_thin
        if fill_use.fill_type:
            c1.fill = fill_use

        c2 = ws_perf.cell(r_cur, 2, val)
        c2.font = font_bold
        c2.alignment = align_center
        c2.border = border_thin
        if fill_use.fill_type:
            c2.fill = fill_use

        ws_perf.merge_cells(start_row=r_cur, start_column=3, end_row=r_cur, end_column=9)
        c3 = ws_perf.cell(r_cur, 3, desc)
        c3.font = font_body
        c3.alignment = align_left
        for col_i in range(3, 10):
            cell_d = ws_perf.cell(r_cur, col_i)
            cell_d.border = border_thin
            if fill_use.fill_type:
                cell_d.fill = fill_use
        ws_perf.row_dimensions[r_cur].height = 20
        r_cur += 1

    r_cur += 1
    _add_perf_section_bar(r_cur, "3. HIỆU SUẤT THEO TỪNG NGUỒN TÀI LIỆU / BỘ ĐỀ")
    r_cur += 1
    by_test_headers = [
        "Nguồn tài liệu / Bộ đề", "Đã thực hành", "Số câu đúng", "Chưa đúng / Chờ xử lý",
        "L1 (100%)", "L2 (66.7%)", "L3 (33.3%)", "Tỷ lệ đúng (%)", "Hiệu suất Socratic (%)"
    ]
    for col_i, h_text in enumerate(by_test_headers, start=1):
        c = ws_perf.cell(r_cur, col_i, h_text)
        c.font = font_th
        c.fill = th_fill
        c.border = border_thin
        c.alignment = align_center
    ws_perf.row_dimensions[r_cur].height = 22
    r_cur += 1

    by_test = export_data.get("by_test") or []
    if not by_test:
        row_vals = ["Chưa có câu hỏi nào được thực hành", 0, 0, 0, 0, 0, 0, "0%", "0%"]
        for col_i, v in enumerate(row_vals, start=1):
            c = ws_perf.cell(r_cur, col_i, v)
            c.font = font_body
            c.border = border_thin
            c.alignment = align_left if col_i == 1 else align_center
        r_cur += 1
    else:
        for t in by_test:
            row_vals = [
                t.get("test_short", ""),
                t.get("practiced", 0),
                t.get("correct", 0),
                t.get("unfinished_or_missed", 0),
                t.get("l1", 0),
                t.get("l2", 0),
                t.get("l3", 0),
                f"{t.get('accuracy_pct', 0)}%",
                f"{t.get('weighted_pct', 0)}%",
            ]
            for col_i, v in enumerate(row_vals, start=1):
                c = ws_perf.cell(r_cur, col_i, v)
                c.font = font_bold if col_i == 1 else font_body
                c.border = border_thin
                c.alignment = align_left if col_i == 1 else align_center
            ws_perf.row_dimensions[r_cur].height = 20
            r_cur += 1
        tot_vals = [
            "TỔNG CỘNG TẤT CẢ BỘ ĐỀ",
            ov.get("total_practiced", 0),
            ov.get("total_correct", 0),
            ov.get("total_unfinished_or_missed", 0),
            ov.get("l1_correct", 0),
            ov.get("l2_correct", 0),
            ov.get("l3_correct", 0),
            f"{ov.get('accuracy_pct', 0)}%",
            f"{ov.get('weighted_pct', 0)}%",
        ]
        for col_i, v in enumerate(tot_vals, start=1):
            c = ws_perf.cell(r_cur, col_i, v)
            c.font = font_bold
            c.fill = total_fill
            c.border = border_thin
            c.alignment = align_left if col_i == 1 else align_center
        ws_perf.row_dimensions[r_cur].height = 22
        r_cur += 1

    r_cur += 1
    _add_perf_section_bar(r_cur, "4. CHI TIẾT HIỆU SUẤT THEO MODULE / CHƯƠNG / CHUYÊN ĐỀ")
    r_cur += 1
    by_mod_headers = [
        "Nguồn tài liệu", "Module / Chương / Chuyên đề", "Đã thực hành", "Số câu đúng",
        "Chưa đúng", "L1", "L2", "L3", "Tỷ lệ đúng (%)"
    ]
    for col_i, h_text in enumerate(by_mod_headers, start=1):
        c = ws_perf.cell(r_cur, col_i, h_text)
        c.font = font_th
        c.fill = th_fill
        c.border = border_thin
        c.alignment = align_center
    ws_perf.row_dimensions[r_cur].height = 22
    r_cur += 1

    by_mod = export_data.get("by_module") or []
    if not by_mod:
        row_vals = ["Chưa có dữ liệu module / chương", "", 0, 0, 0, 0, 0, 0, "0%"]
        for col_i, v in enumerate(row_vals, start=1):
            c = ws_perf.cell(r_cur, col_i, v)
            c.font = font_body
            c.border = border_thin
            c.alignment = align_left if col_i <= 2 else align_center
        r_cur += 1
    else:
        for idx_m, m in enumerate(by_mod):
            row_vals = [
                m.get("test_short", ""),
                m.get("module_title", ""),
                m.get("practiced", 0),
                m.get("correct", 0),
                m.get("unfinished_or_missed", 0),
                m.get("l1", 0),
                m.get("l2", 0),
                m.get("l3", 0),
                f"{m.get('accuracy_pct', 0)}%",
            ]
            for col_i, v in enumerate(row_vals, start=1):
                c = ws_perf.cell(r_cur, col_i, v)
                c.font = font_body
                c.border = border_thin
                if idx_m % 2 == 1:
                    c.fill = zebra_fill
                c.alignment = align_left if col_i <= 2 else align_center
            ws_perf.row_dimensions[r_cur].height = 20
            r_cur += 1

    for col_i, w in enumerate([36, 34, 16, 18, 12, 12, 12, 16, 20], start=1):
        ws_perf.column_dimensions[get_column_letter(col_i)].width = w

    def _populate_table_sheet(ws, banner_title, headers, rows_matrix, widths, center_cols=None, status_col=None):
        center_set = set(center_cols or [])
        num_cols = len(headers)
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=num_cols)
        b_cell = ws.cell(1, 1, banner_title)
        b_cell.font = font_title
        b_cell.fill = title_fill
        b_cell.alignment = align_banner
        ws.row_dimensions[1].height = 28

        for c_i, h_text in enumerate(headers, start=1):
            hc = ws.cell(2, c_i, h_text)
            hc.font = font_th
            hc.fill = th_fill
            hc.border = border_thin
            hc.alignment = align_center
            ws.column_dimensions[get_column_letter(c_i)].width = widths[c_i - 1]
        ws.row_dimensions[2].height = 28
        ws.freeze_panes = "A3"

        for r_idx, row_vals in enumerate(rows_matrix, start=3):
            is_zebra = (r_idx % 2 == 0)
            for c_i, val in enumerate(row_vals, start=1):
                cell = ws.cell(r_idx, c_i, val)
                cell.font = font_body
                cell.border = border_thin
                cell.alignment = align_center if c_i in center_set else align_left
                if status_col and c_i == status_col:
                    s_val = str(val or "")
                    if "Lần 1" in s_val or "Đã triệt tiêu" in s_val:
                        cell.fill = green_fill
                        cell.font = font_bold
                    elif "Lần 2" in s_val or "Lần 3" in s_val or "Đang theo dõi" in s_val:
                        cell.fill = amber_fill
                    elif "Sai" in s_val or "Chưa xử lý" in s_val:
                        cell.fill = red_fill
                elif is_zebra:
                    cell.fill = zebra_fill

    # ---- Sheet 2: Cau_Hoi_Da_Thuc_Hanh ----
    ws_q = wb.create_sheet("Cau_Hoi_Da_Thuc_Hanh")
    q_headers = [
        "STT", "Nguồn tài liệu / Bộ đề", "Module / Chương", "Mã câu",
        "Chủ đề / Kỹ năng", "Trang (PDF / Sách)", "Độ khó",
        "Nội dung câu hỏi & Phương án", "Lần thử 1", "Lần thử 2",
        "Lần thử 3", "Đáp án đúng", "Kết quả & Mức đạt", "Hiệu suất (%)",
        "Phản hồi Tầng 1 (Định hướng tư duy)",
        "Phản hồi Tầng 2 (Manh mối cấu trúc & Loại trừ)",
        "Phản hồi Tầng 3 (Chốt phương pháp & Lời giải chi tiết)",
        "Phản hồi Tầng 4 (Chiến thuật & Công thức cốt lõi)",
        "Ghi chú Sổ thử sai Socratic (nếu có)", "Thời gian thực hành",
    ]
    p_rows = export_data.get("practiced_questions") or []
    if not p_rows:
        q_matrix = [[
            1, "", "", "", "", "", "",
            "Chưa có câu hỏi nào được thực hành. Hãy chọn đáp án trong bài luyện tập để hệ thống lưu lại câu hỏi và phản hồi đa tầng.",
            "", "", "", "", "", "", "", "", "", "", "", "",
        ]]
    else:
        q_matrix = [
            [
                q.get("stt", idx + 1),
                q.get("test_short", ""),
                q.get("module_title", ""),
                q.get("q_label", ""),
                q.get("topic", ""),
                q.get("page_label", ""),
                q.get("difficulty", ""),
                q.get("question_content", ""),
                q.get("attempt_1", ""),
                q.get("attempt_2", ""),
                q.get("attempt_3", ""),
                q.get("correct_answer", ""),
                q.get("status_label", ""),
                f"{q.get('efficiency_pct', 0)}%",
                q.get("tier1_feedback", ""),
                q.get("tier2_feedback", ""),
                q.get("tier3_feedback", ""),
                q.get("tier4_feedback", ""),
                q.get("error_note_summary", ""),
                q.get("practiced_at", ""),
            ]
            for idx, q in enumerate(p_rows)
        ]
    _populate_table_sheet(
        ws_q,
        f"DANH SÁCH CÂU HỎI ĐÃ THỰC HÀNH & PHẢN HỒI ĐA TẦNG — {student_name.upper()}",
        q_headers,
        q_matrix,
        [6, 24, 30, 14, 28, 18, 12, 52, 10, 10, 10, 12, 22, 13, 44, 46, 54, 48, 40, 20],
        center_cols=[1, 4, 7, 9, 10, 11, 12, 14],
        status_col=13,
    )

    # ---- Sheet 3: So_Tay_Thu_Sai_Socratic ----
    ws_err = wb.create_sheet("So_Tay_Thu_Sai_Socratic")
    err_headers = [
        "STT", "Nguồn tài liệu / Bộ đề", "Mã câu", "Module / Chương",
        "Chủ đề / Kỹ năng", "Các lần chọn sai", "Đáp án đúng",
        "Nhóm bẫy SAT / Nguyên nhân gốc",
        "Phân tích nguyên nhân thử sai & Bài học rút ra",
        "Ghi chú tư duy cá nhân", "Từ mới & Thuật ngữ Socratic đã ghi",
        "Gợi ý Socratic tham chiếu (Tầng 1)", "Tình trạng xử lý", "Ngày ghi chép",
    ]
    e_rows = export_data.get("error_logs") or []
    if not e_rows:
        err_matrix = [[
            1, "", "", "", "", "", "", "",
            "Chưa có ghi chép nào trong Sổ tay Thử sai Socratic.",
            "", "", "", "", "",
        ]]
    else:
        err_matrix = [
            [
                e.get("stt", idx + 1),
                e.get("test_short", ""),
                e.get("q_label", ""),
                e.get("module", ""),
                e.get("skill", ""),
                e.get("wrong_attempts", ""),
                e.get("correct_answer", ""),
                e.get("root_cause", ""),
                e.get("trap_detail", ""),
                e.get("student_notes", ""),
                e.get("vocabulary", ""),
                e.get("socratic_analysis", ""),
                e.get("status", ""),
                e.get("date", ""),
            ]
            for idx, e in enumerate(e_rows)
        ]
    _populate_table_sheet(
        ws_err,
        f"SỔ TAY THỬ SAI SOCRATIC & BÀI HỌC PHẢN TƯ — {student_name.upper()}",
        err_headers,
        err_matrix,
        [6, 24, 14, 28, 26, 16, 12, 32, 46, 36, 36, 40, 18, 14],
        center_cols=[1, 3, 6, 7, 14],
        status_col=13,
    )

    # ---- Sheet 4: Tu_Vung_Socratic ----
    ws_vocab = wb.create_sheet("Tu_Vung_Socratic")
    vocab_headers = [
        "STT", "Nguồn tài liệu / Bộ đề", "Mã câu liên quan", "Module / Chủ đề",
        "Từ mới / Thuật ngữ Socratic", "Nghĩa / Giải thích học sinh đã ghi",
        "Ngữ cảnh bẫy SAT & Ghi chú liên quan", "Ngày ghi chép",
    ]
    v_rows = export_data.get("vocab_entries") or []
    if not v_rows:
        vocab_matrix = [[
            1, "", "", "",
            "Chưa có từ vựng / thuật ngữ nào được ghi chép trong Sổ tay Socratic.",
            "", "", "",
        ]]
    else:
        vocab_matrix = [
            [
                v.get("stt", idx + 1),
                v.get("test_short", ""),
                v.get("q_label", ""),
                v.get("module_skill", ""),
                v.get("term", ""),
                v.get("meaning", ""),
                v.get("context_note", ""),
                v.get("date", ""),
            ]
            for idx, v in enumerate(v_rows)
        ]
    _populate_table_sheet(
        ws_vocab,
        f"TỪ VỰNG & THUẬT NGỮ SOCRATIC ĐÃ GHI CHÉP — {student_name.upper()}",
        vocab_headers,
        vocab_matrix,
        [6, 24, 16, 30, 28, 44, 42, 14],
        center_cols=[1, 3, 8],
    )

    safe_name = re.sub(r"[^a-zA-Z0-9_\-]", "_", student_name) or "Student"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    export_filename = f"SAT_Tong_Hop_Thuc_Hanh_{safe_name}_{timestamp}.xlsx"

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
