#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Complete College Panda SAT Math Database (330 Questions across 27 Chapters)
Source Excel: /Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/26-27 Grand Plan /Study Plan/Math/Template - Full Nielson Phu SAT Math.xlsx
Source Book & PDF: SAT Coach/Books/Nielson Phu - SAT Math The College Panda.pdf (317 pages)
Target: data/panda_math.json (and mirrors)
"""

import json
import os
import re
import openpyxl

EXCEL_PATH = "/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/26-27 Grand Plan /Study Plan/Math/Template - Full Nielson Phu SAT Math.xlsx"
PANDA_APP_DB = "/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/SAT Coach/PandaMathApp/database.json"
PDF_PATH = "SAT Coach/Books/Nielson Phu - SAT Math The College Panda.pdf"
PDF_DRIVE_ID = "1z4CC7X-L3e3XZr04uc7RgMZBK5lYs8Gb"
PDF_PREVIEW_URL = f"https://drive.google.com/file/d/{PDF_DRIVE_ID}/preview"
PDF_VIEW_URL = f"https://drive.google.com/file/d/{PDF_DRIVE_ID}/view?usp=drive_open"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_JSON = os.path.join(BASE_DIR, "data", "panda_math.json")

# Verified Chapter Page Mappings from Book Table of Contents
CHAPTER_MAPPING = {
    1: {"name": "Exponents & Radicals", "vn_sub": "Lũy thừa & Căn thức", "book_page": 7, "pdf_page": 9, "domain": "Passport to Advanced Math"},
    2: {"name": "Percent", "vn_sub": "Phần trăm & Biến thiên phần trăm", "book_page": 15, "pdf_page": 17, "domain": "Problem Solving & Data Analysis"},
    3: {"name": "Exponential vs. Linear Growth", "vn_sub": "Mô hình Tuyến tính vs Số mũ", "book_page": 24, "pdf_page": 26, "domain": "Problem Solving & Data Analysis"},
    4: {"name": "Proportion", "vn_sub": "Tỷ lệ thức & Biến thiên", "book_page": 31, "pdf_page": 33, "domain": "Problem Solving & Data Analysis"},
    5: {"name": "Rates", "vn_sub": "Tốc độ & Hệ số chuyển đổi", "book_page": 36, "pdf_page": 38, "domain": "Problem Solving & Data Analysis"},
    6: {"name": "Expressions", "vn_sub": "Biểu thức đại số & Phân thức", "book_page": 42, "pdf_page": 44, "domain": "Passport to Advanced Math"},
    7: {"name": "Manipulating & Solving Equations", "vn_sub": "Biến đổi & Giải phương trình", "book_page": 49, "pdf_page": 51, "domain": "Heart of Algebra"},
    8: {"name": "More Equation Solving Strategies", "vn_sub": "Đổi biến & Chiến thuật giải nhanh", "book_page": 58, "pdf_page": 60, "domain": "Passport to Advanced Math"},
    9: {"name": "Systems of Equations", "vn_sub": "Hệ phương trình tuyến tính", "book_page": 67, "pdf_page": 69, "domain": "Heart of Algebra"},
    10: {"name": "Inequalities", "vn_sub": "Bất đẳng thức & Hệ bất phương trình", "book_page": 79, "pdf_page": 81, "domain": "Heart of Algebra"},
    11: {"name": "Word Problems", "vn_sub": "Giải toán bằng cách lập phương trình", "book_page": 90, "pdf_page": 92, "domain": "Heart of Algebra / Problem Solving"},
    12: {"name": "Lines", "vn_sub": "Đường thẳng & Hàm tuyến tính", "book_page": 99, "pdf_page": 101, "domain": "Heart of Algebra"},
    13: {"name": "Interpreting Linear Models", "vn_sub": "Giải nghĩa mô hình thực tế", "book_page": 109, "pdf_page": 111, "domain": "Heart of Algebra"},
    14: {"name": "Functions", "vn_sub": "Hàm số & Đồ thị hàm số", "book_page": 115, "pdf_page": 117, "domain": "Passport to Advanced Math"},
    15: {"name": "Quadratics", "vn_sub": "Phương trình bậc hai & Parabol", "book_page": 126, "pdf_page": 128, "domain": "Passport to Advanced Math"},
    16: {"name": "Synthetic Division", "vn_sub": "Chia đa thức & Định lý số dư", "book_page": 141, "pdf_page": 143, "domain": "Passport to Advanced Math"},
    17: {"name": "Complex Numbers", "vn_sub": "Số phức & Đơn vị ảo i", "book_page": 150, "pdf_page": 152, "domain": "Additional Topics in Math"},
    18: {"name": "Absolute Value", "vn_sub": "Giá trị tuyệt đối", "book_page": 154, "pdf_page": 156, "domain": "Heart of Algebra"},
    19: {"name": "Angles", "vn_sub": "Góc & Đa giác", "book_page": 160, "pdf_page": 162, "domain": "Additional Topics in Math"},
    20: {"name": "Triangles", "vn_sub": "Tam giác & Radian", "book_page": 168, "pdf_page": 170, "domain": "Additional Topics in Math"},
    21: {"name": "Circles", "vn_sub": "Đường tròn & Phương trình đường tròn", "book_page": 189, "pdf_page": 191, "domain": "Additional Topics in Math"},
    22: {"name": "Trigonometry", "vn_sub": "Lượng giác (Sin, Cos, Tan)", "book_page": 198, "pdf_page": 200, "domain": "Additional Topics in Math"},
    23: {"name": "Reading Data", "vn_sub": "Đọc và Phân tích biểu đồ dữ liệu", "book_page": 205, "pdf_page": 207, "domain": "Problem Solving & Data Analysis"},
    24: {"name": "Probability", "vn_sub": "Xác suất & Bảng tần số 2 chiều", "book_page": 214, "pdf_page": 216, "domain": "Problem Solving & Data Analysis"},
    25: {"name": "Statistics I", "vn_sub": "Thống kê I: Trung bình, Trung vị, Độ phân tán", "book_page": 223, "pdf_page": 225, "domain": "Problem Solving & Data Analysis"},
    26: {"name": "Statistics II", "vn_sub": "Thống kê II: Mẫu, Thí nghiệm & Sai số", "book_page": 233, "pdf_page": 235, "domain": "Problem Solving & Data Analysis"},
    27: {"name": "Volume", "vn_sub": "Thể tích & Diện tích toàn phần", "book_page": 246, "pdf_page": 248, "domain": "Additional Topics in Math"}
}

def parse_options(options_raw):
    if not options_raw:
        return []
    lines = str(options_raw).strip().split('\n')
    parsed = []
    current_key = None
    current_val = []

    for line in lines:
        line_s = line.strip()
        match = re.match(r'^([A-D])[\.\:\)]\s*(.*)$', line_s)
        if match:
            if current_key:
                parsed.append({"key": current_key, "text": " ".join(current_val).strip()})
            current_key = match.group(1)
            current_val = [match.group(2)]
        else:
            if current_key:
                current_val.append(line_s)
            elif line_s:
                current_val.append(line_s)
    if current_key:
        parsed.append({"key": current_key, "text": " ".join(current_val).strip()})

    if not parsed:
        for opt in ['A', 'B', 'C', 'D']:
            pattern = rf'{opt}[\.\:\)]\s*([^\n]+)'
            m = re.search(pattern, str(options_raw))
            if m:
                parsed.append({"key": opt, "text": m.group(1).strip()})
    return parsed

def build_socratic_hints(q_id, ch_num, topic, question_text, calc_mode, correct_ans, opt_text, raw_l1, raw_l2, core_strat, traps):
    """
    Generate 4-tier pedagogical Socratic hints adhering strictly to the No-Leak Policy.
    Tier 1 & Tier 2 MUST NOT reveal the correct option letter (A/B/C/D) or the final target answer.
    """
    ch_info = CHAPTER_MAPPING.get(ch_num, {})
    ch_name = ch_info.get("name", f"Chương {ch_num}")
    vn_sub = ch_info.get("vn_sub", "")
    domain = ch_info.get("domain", "Math")

    # Clean raw_l1: remove any explicit answer letter or "= [ans]"
    sanitized_l1 = raw_l1 or ""
    # Remove direct leaks like "= B" or "=> B" or "= 10/27" if it is the answer
    sanitized_l1 = re.sub(r'=\s*([A-D])\b', '= ...', sanitized_l1)
    if opt_text:
        sanitized_l1 = sanitized_l1.replace(f"= {opt_text}", "= ...")

    # Tier 1: Context & Core Formula Direction
    mode_text = "Không dùng máy tính (No Calculator)" if "No Calculator" in calc_mode else "Được dùng máy tính (Calculator Allowed - hỗ trợ Desmos)"
    tier1 = (
        f"Xác định dạng toán: **{topic}** trong chuyên đề **Chương {ch_num}: {ch_name} ({vn_sub})**.\n"
        f"• Chế độ làm bài: {mode_text}.\n"
        f"• Đọc kỹ đề bài để nắm đại lượng đã cho và đại lượng cần tìm.\n"
        f"• Quy tắc / Công thức then chốt: {sanitized_l1 if sanitized_l1 else 'Áp dụng các định lý và tính chất đại số / hình học cơ bản của chương.'}"
    )

    # Tier 2: Intermediate Algebraic / Geometric Clue (No-Leak)
    # We provide the setup or first transformation, but do NOT finish the calculation or name the option.
    tier2 = ""
    # Custom setups for specific questions with missing raw_l2
    if q_id == 130:
        tier2 = (
            "Phân tích bất đẳng thức kép k <= x <= 3k + 12 theo từng mệnh đề:\n"
            "• Xét mệnh đề I: Từ x <= 3k + 12, hãy trừ 12 cả hai vế để so sánh x - 12 với 3k.\n"
            "• Xét mệnh đề II: Từ k <= 3k + 12, chuyển k sang một vế để giải bất phương trình bậc nhất tìm chặn dưới của k.\n"
            "• Xét mệnh đề III: Từ k <= x, hãy chuyển k sang vế trái để suy ra dấu của x - k.\n"
            "Hãy đối chiếu tính đúng đắn của từng mệnh đề I, II, III để xác định kết luận chung."
        )
    elif q_id == 241:
        tier2 = (
            "Bài toán khoảng dung sai (Tolerance Interval):\n"
            "• Tìm giá trị trung tâm (Midpoint) của khoảng [400; 410]: Midpoint = (400 + 410) / 2.\n"
            "• Tìm độ lệch tối đa (Tolerance) từ điểm trung tâm đến hai đầu mút: Tolerance = (410 - 400) / 2.\n"
            "• Công thức khoảng giá trị tuyệt đối chuẩn: |x - Midpoint| < Tolerance. Hãy thay số để đối chiếu dạng biểu thức."
        )
    elif raw_l2:
        # Generate clean intermediate guidance from raw_l2
        steps = [s.strip() for s in re.split(r'=>|;', raw_l2) if s.strip()]
        if len(steps) >= 3:
            setup = " => ".join(steps[:2])
            tier2 = f"Manh mối bước giải trung gian:\n• Thiết lập bước biến đổi đầu tiên: {setup}.\n• Hãy tiếp tục rút gọn và thực hiện phép tính còn lại để suy ra kết quả cuối cùng."
        elif len(steps) == 2:
            setup = steps[0]
            tier2 = f"Manh mối bước giải trung gian:\n• Thiết lập mối liên hệ: {setup}.\n• Hãy giải phương trình / tính biểu thức còn lại để xác định giá trị cần tìm."
        else:
            tier2 = f"Phương pháp tiếp cận:\n• {raw_l2}.\n• Cẩn thận kiểm tra các phép biến đổi đại số tương đương để không bỏ sót điều kiện."
    else:
        tier2 = (
            "Chiến thuật giải toán:\n"
            "• Thiết lập phương trình hoặc hệ thức liên hệ trực tiếp giữa các dữ kiện đề bài.\n"
            "• Biến đổi đại số hoặc thay thế giá trị trung gian để cô lập đại lượng cần tìm."
        )

    # Sanitize tier 2 from any accidental option leak
    tier2 = re.sub(rf'\b[đĐ]áp án[:\s]+[A-D]\b', '', tier2)
    tier2 = re.sub(rf'\b[cC]họn\s+[A-D]\b', '', tier2)
    tier2 = re.sub(rf'\b[pP]hương án\s+[A-D]\b', '', tier2)

    # Tier 3: Complete Step-by-Step Solution & Walkthrough
    sol_body = raw_l2
    if q_id == 130:
        sol_body = (
            "Phân tích bất đẳng thức kép k <= x <= 3k + 12:\n"
            "1. Xét I: x <= 3k + 12 => x - 12 <= 3k. (I luôn đúng).\n"
            "2. Xét II: Vì k <= x <= 3k + 12 nên k <= 3k + 12 => -12 <= 2k => k >= -6. (II luôn đúng).\n"
            "3. Xét III: Từ k <= x => x - k >= 0. (III luôn đúng).\n"
            "Do đó cả 3 mệnh đề I, II và III đều bắt buộc phải đúng."
        )
    elif q_id == 241:
        sol_body = (
            "Dạng toán mô hình hóa khoảng giá trị bằng bất phương trình giá trị tuyệt đối:\n"
            "• Điểm chính giữa (Midpoint): (400 + 410) / 2 = 405.\n"
            "• Khoảng cách tối đa cho phép (Bán kính khoảng): (410 - 400) / 2 = 5.\n"
            "• Bất phương trình tương ứng là |l - 405| < 5 (tương đương -5 < l - 405 < 5 <=> 400 < l < 410)."
        )

    tier3 = (
        f"**Đáp án chính xác là [{correct_ans}]**"
        + (f" ({opt_text})\n\n" if opt_text else "\n\n")
        + f"**Lời giải chi tiết từng bước (The College Panda):**\n"
        f"{sol_body}\n\n"
        f"• **Kết luận:** Phương án **[{correct_ans}]** hoàn toàn chuẩn xác theo phương pháp giải của Nielson Phu."
    )

    # Tier 4: Core Theory, Traps, and Pro-Tips from College Panda
    strat_snippet = core_strat or f"Nắm vững các tính chất toán học của {ch_name}."
    traps_snippet = traps or "Cẩn thận kiểm tra điều kiện nghiệm và các phép biến đổi dấu."
    
    tier4 = (
        f"**🎯 Chiến thuật cốt lõi & Công thức then chốt (The College Panda - Chương {ch_num}):**\n"
        f"{strat_snippet}\n\n"
        f"**⚠️ Bẫy SAT thường gặp cần tránh:**\n"
        f"{traps_snippet}"
    )

    return tier1.strip(), tier2.strip(), tier3.strip(), tier4.strip()

def generate_mermaid(q_id, ch_num, topic, correct_ans):
    ch_info = CHAPTER_MAPPING.get(ch_num, {})
    ch_name = ch_info.get("name", f"Chương {ch_num}")
    
    clean_topic = re.sub(r'[^a-zA-Z0-9\s]', '', topic)[:30]
    clean_ch = re.sub(r'[^a-zA-Z0-9\s]', '', ch_name)[:25]
    
    return f"""flowchart TD
    A["Câu hỏi {q_id}: Ch.{ch_num} {clean_ch}"] --> B["Dạng bài: {clean_topic}"]
    B --> C{{"Công thức & Chiến thuật then chốt"}}
    C --> D["Biến đổi đại số & Giải bước trung gian"]
    D --> E["Đáp án chính xác: {correct_ans}"]"""

def main():
    print(f"Loading PandaApp database: {PANDA_APP_DB}")
    with open(PANDA_APP_DB, "r", encoding="utf-8") as f:
        panda_raw = json.load(f)

    print(f"Loading Excel workbook: {EXCEL_PATH}")
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=False)
    
    # 1. Parse Overview_Strategies
    strategies = {}
    if 'Overview_Strategies' in wb.sheetnames:
        ws_strat = wb['Overview_Strategies']
        for r in range(4, ws_strat.max_row + 1):
            ch_label = ws_strat.cell(r, 1).value
            topic_full = ws_strat.cell(r, 2).value
            domain = ws_strat.cell(r, 3).value
            core_theory = ws_strat.cell(r, 4).value
            traps = ws_strat.cell(r, 5).value
            
            if ch_label:
                m = re.search(r'\d+', str(ch_label))
                if m:
                    ch_num = int(m.group(0))
                    strategies[ch_num] = {
                        "core_theory": str(core_theory or "").strip(),
                        "traps": str(traps or "").strip(),
                        "domain": str(domain or "").strip(),
                        "topic_title": str(topic_full or "").strip()
                    }

    # 2. Parse Master_All_330_Questions
    ws_master = wb['Master_All_330_Questions']
    raw_qs = []
    
    for r in range(5, 335):
        qid = ws_master.cell(r, 1).value
        chapter_str = ws_master.cell(r, 2).value
        topic_str = ws_master.cell(r, 3).value
        question_text = ws_master.cell(r, 4).value
        calc_mode = ws_master.cell(r, 5).value
        options_raw = ws_master.cell(r, 6).value
        formula_l1 = ws_master.cell(r, 8).value
        hint_formula = ws_master.cell(r, 16).value
        tip_text = ws_master.cell(r, 17).value
        
        if not qid:
            continue
            
        ch_num = 1
        m_ch = re.search(r'Ch(\d+)', str(chapter_str))
        if m_ch:
            ch_num = int(m_ch.group(1))
            
        ans_match = re.search(r'\"([A-D0-9\/\.\-]+)\"', str(formula_l1))
        correct_ans = ans_match.group(1) if ans_match else ''
        
        hint_match = re.findall(r'\"([^\"]+)\"', str(hint_formula))
        clean_hints = [h for h in hint_match if not any(x in h for x in ['Nhập A/B/C/D', 'Hoàn hảo!', 'Đúng', 'Sai', '💡 Gợi ý: '])]
        hint_clean = ' '.join(clean_hints).strip() if clean_hints else ''
        
        raw_qs.append({
            "id": int(qid),
            "chapter_num": ch_num,
            "chapter_str": str(chapter_str or "").strip(),
            "topic": str(topic_str or "").strip(),
            "question": str(question_text or "").strip(),
            "calc_mode": str(calc_mode or "No Calculator").strip(),
            "options_raw": str(options_raw or "").strip(),
            "correct_ans": correct_ans,
            "hint_clean": hint_clean,
            "tip_text": str(tip_text or "").strip()
        })

    print(f"Loaded {len(raw_qs)} questions from Excel Master sheet.")

    # 3. Assemble Questions and Chapter Modules
    processed_questions = []
    chapter_counters = {ch: 0 for ch in range(1, 28)}
    
    # Audit tracking
    leak_failures = []

    for item in raw_qs:
        qid = item["id"]
        cnum = item["chapter_num"]
        chapter_counters[cnum] += 1
        q_idx_in_ch = chapter_counters[cnum]
        
        c_info = CHAPTER_MAPPING.get(cnum, {
            "name": f"Chapter {cnum}", "vn_sub": "", "book_page": 1, "pdf_page": 1, "domain": "Math"
        })
        strat = strategies.get(cnum, {})

        options = parse_options(item["options_raw"])
        corr_ans = item["correct_ans"]
        
        # Get correct option text
        opt_text = ""
        for opt in options:
            if opt["key"] == corr_ans:
                opt_text = opt["text"]
                break

        t1, t2, t3, t4 = build_socratic_hints(
            qid, cnum, item["topic"], item["question"], item["calc_mode"],
            corr_ans, opt_text, item["tip_text"], item["hint_clean"],
            strat.get("core_theory", ""), strat.get("traps", "")
        )

        # Audit Tier 1 and Tier 2 for leaks
        for tier_name, tier_text in [("Tier 1", t1), ("Tier 2", t2)]:
            # Check for direct answer announcements
            patterns = [
                rf"\b[đĐ]áp án\s+là\s+{corr_ans}\b",
                rf"\b[cC]họn\s+{corr_ans}\b",
                rf"\b[pP]hương án\s+{corr_ans}\b",
                rf"\bĐáp án chính xác là\s+\[?{corr_ans}\]?",
            ]
            for pat in patterns:
                if re.search(pat, tier_text):
                    leak_failures.append((qid, tier_name, pat))

        mermaid_code = generate_mermaid(qid, cnum, item["topic"], corr_ans)

        code_name = f"Ch{cnum}_{c_info['name'].replace(' ', '_').replace('&', 'and').replace('.', '').replace('-', '_')}"

        processed_questions.append({
            "id": qid,
            "master_id": f"Panda_Math_Q{qid}",
            "q_number": qid,
            "q_label": f"Ch.{cnum} - Câu {q_idx_in_ch}",
            "category": "practice",
            "category_label": "Luyện tập SAT Math",
            "module_code": code_name,
            "module_title": f"Chương {cnum}: {c_info['name']} ({c_info['vn_sub']})",
            "section": "Math",
            "chapter": f"Chương {cnum}: {c_info['name']}",
            "chapter_num": cnum,
            "topic": item["topic"],
            "passage": "",
            "prompt": item["question"],
            "options": options,
            "options_raw": item["options_raw"],
            "is_grid_in": False,
            "correct_answer": corr_ans,
            "acceptable_answers": [corr_ans],
            "calc_mode": item["calc_mode"],
            "is_calculator": "Calculator Allowed" in item["calc_mode"],
            "tier1_hint": t1,
            "tier2_hint": t2,
            "tier3_hint": t3,
            "strategic_tip": t4,
            "mermaid_diagram": mermaid_code,
            "pdf_page": c_info["pdf_page"],
            "book_page": c_info["book_page"],
            "difficulty": "Advanced" if cnum in [15, 16, 21, 22, 27] else ("Hard" if cnum in [8, 9, 10, 14, 20, 25, 26] else "Medium"),
            "domain": c_info["domain"]
        })

    print("\n--- NO-LEAK AUDIT RESULTS ---")
    if leak_failures:
        print(f"❌ AUDIT FAILED: {len(leak_failures)} leaks found!")
        for fail in leak_failures[:10]:
            print(f"  Q{fail[0]} in {fail[1]}: pattern '{fail[2]}'")
        raise ValueError("No-leak audit failed!")
    else:
        print("✅ NO-LEAK AUDIT PASSED: 0 leaks found across all 330 questions!")

    # 4. Build Modules list
    modules_list = []
    for cnum in range(1, 28):
        c_info = CHAPTER_MAPPING.get(cnum, {})
        strat = strategies.get(cnum, {})
        code_name = f"Ch{cnum}_{c_info['name'].replace(' ', '_').replace('&', 'and').replace('.', '').replace('-', '_')}"
        mod_qs = [q for q in processed_questions if q["chapter_num"] == cnum]
        
        modules_list.append({
            "id": f"panda_ch{cnum}",
            "code": code_name,
            "chapter_num": cnum,
            "title": f"Chương {cnum}: {c_info['name']} ({c_info['vn_sub']})",
            "short_title": f"Chương {cnum}: {c_info['name']}",
            "sub_title": c_info["vn_sub"],
            "domain": c_info["domain"],
            "section": "Math",
            "time_minutes": max(10, round(len(mod_qs) * 1.5)),
            "question_count": len(mod_qs),
            "pdf_start_page": c_info["pdf_page"],
            "book_page": c_info["book_page"],
            "strategy": strat.get("core_theory", "Các công thức và định lý cốt lõi của The College Panda."),
            "traps": strat.get("traps", "Cẩn thận kiểm tra bẫy thử nghiệm và phép toán biến đổi dấu."),
            "question_ids": [q["id"] for q in mod_qs]
        })

    # 5. Full Database Object
    final_db = {
        "test_title": "The College Panda: SAT Math Advanced Guide & Workbook (Nielson Phu)",
        "source_attribution": "The College Panda - SAT Math (Nielson Phu)",
        "credits": "Biên soạn và cấu trúc hóa bởi SAT Master Coach Vinschool theo phương pháp Socratic 4 tầng.",
        "pdf_drive_id": PDF_DRIVE_ID,
        "pdf_path": PDF_PATH,
        "pdf_drive_preview": PDF_PREVIEW_URL,
        "pdf_drive_view": PDF_VIEW_URL,
        "total_questions": len(processed_questions),
        "total_chapters": len(modules_list),
        "time_minutes": 360,
        "modules_count": len(modules_list),
        "structure_mode": "chapter_by_chapter",
        "modules": modules_list,
        "questions": processed_questions
    }

    # Save to data/panda_math.json
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(final_db, f, ensure_ascii=False, indent=2)
    print(f"✅ Successfully exported {len(processed_questions)} questions to {OUTPUT_JSON} ({os.path.getsize(OUTPUT_JSON)} bytes)")

    # Mirror copies
    mirrors = [
        os.path.join(BASE_DIR, "data", "pandamath.json"),
        os.path.join(BASE_DIR, "static", "data", "panda_math.json"),
        os.path.join(BASE_DIR, "static", "data", "pandamath.json")
    ]
    for mirror in mirrors:
        os.makedirs(os.path.dirname(mirror), exist_ok=True)
        with open(mirror, "w", encoding="utf-8") as f:
            json.dump(final_db, f, ensure_ascii=False, indent=2)
        print(f"✅ Mirrored to {mirror}")

if __name__ == "__main__":
    main()
