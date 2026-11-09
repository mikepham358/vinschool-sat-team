# -*- coding: utf-8 -*-
"""
Builder for Erica Meltzer Digital SAT Reading Master Guide
Extracts all 74 questions from:
[Edited] Template - Full Erica Meltzer SAT Reading.xlsx
Structured Chapter-by-Chapter (9 Chapters)
Outputs: data/erica_reading.json
"""

import openpyxl
import re
import json
import os

EXCEL_PATH = '/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/26-27 Grand Plan /Study Plan/Reading & Writing/Templates/[Edited] Template - Full Erica Meltzer SAT Reading.xlsx'
OUTPUT_JSON = 'data/erica_reading.json'

CHAPTER_CONFIG = [
    {
        "sheet": "Ch2_Vocabulary",
        "num": 2,
        "name": "Chương 2: Vocabulary in Context (Nghĩa Từ Trong Ngữ Cảnh)",
        "short_name": "Chương 2: Vocabulary in Context",
        "sub_title": "Nghĩa Từ Trong Ngữ Cảnh",
        "domain": "Craft and Structure",
        "start_page": 25,
        "module_code": "Ch2_Vocabulary",
        "time_minutes": 25
    },
    {
        "sheet": "Ch3_MakingTheLeap",
        "num": 3,
        "name": "Chương 3: Making the Leap (Đại từ & Danh từ nén)",
        "short_name": "Chương 3: Making the Leap",
        "sub_title": "Đại từ & Danh từ nén",
        "domain": "Information and Ideas",
        "start_page": 61,
        "module_code": "Ch3_MakingTheLeap",
        "time_minutes": 15
    },
    {
        "sheet": "Ch4_BigPicture",
        "num": 4,
        "name": "Chương 4: The Big Picture / Main Idea (Ý chính & Đại ý)",
        "short_name": "Chương 4: The Big Picture",
        "sub_title": "Ý chính & Đại ý",
        "domain": "Information and Ideas",
        "start_page": 85,
        "module_code": "Ch4_BigPicture",
        "time_minutes": 7
    },
    {
        "sheet": "Ch5_LiteralComprehension",
        "num": 5,
        "name": "Chương 5: Literal Comprehension (Đọc hiểu Trực tiếp)",
        "short_name": "Chương 5: Literal Comprehension",
        "sub_title": "Đọc hiểu Trực tiếp",
        "domain": "Information and Ideas",
        "start_page": 111,
        "module_code": "Ch5_LiteralComprehension",
        "time_minutes": 9
    },
    {
        "sheet": "Ch6_ReadingForFunction",
        "num": 6,
        "name": "Chương 6: Reading for Function (Đọc theo Chức năng Diễn ngôn)",
        "short_name": "Chương 6: Reading for Function",
        "sub_title": "Đọc theo Chức năng Diễn ngôn",
        "domain": "Craft and Structure",
        "start_page": 139,
        "module_code": "Ch6_ReadingForFunction",
        "time_minutes": 9
    },
    {
        "sheet": "Ch7_TextCompletions",
        "num": 7,
        "name": "Chương 7: Text Completions (Hoàn thành Văn bản / Suy luận)",
        "short_name": "Chương 7: Text Completions",
        "sub_title": "Hoàn thành Văn bản / Suy luận",
        "domain": "Information and Ideas",
        "start_page": 171,
        "module_code": "Ch7_TextCompletions",
        "time_minutes": 8
    },
    {
        "sheet": "Ch8_SupportUndermining",
        "num": 8,
        "name": "Chương 8: Supporting & Undermining (Củng cố & Làm suy yếu)",
        "short_name": "Chương 8: Supporting & Undermining",
        "sub_title": "Củng cố & Làm suy yếu",
        "domain": "Information and Ideas",
        "start_page": 205,
        "module_code": "Ch8_SupportUndermining",
        "time_minutes": 10
    },
    {
        "sheet": "Ch9_GraphsCharts",
        "num": 9,
        "name": "Chương 9: Graphs & Charts (Biểu đồ & Bảng số liệu)",
        "short_name": "Chương 9: Graphs & Charts",
        "sub_title": "Biểu đồ & Bảng số liệu",
        "domain": "Information and Ideas",
        "start_page": 249,
        "module_code": "Ch9_GraphsCharts",
        "time_minutes": 7
    },
    {
        "sheet": "Ch10_PairedPassages",
        "num": 10,
        "name": "Chương 10: Paired Passages (Đoạn văn Kép)",
        "short_name": "Chương 10: Paired Passages",
        "sub_title": "Đoạn văn Kép",
        "domain": "Cross-Text Connections",
        "start_page": 287,
        "module_code": "Ch10_PairedPassages",
        "time_minutes": 6
    }
]

def parse_options(raw):
    if not raw:
        return []
    lines = [line.strip() for line in str(raw).split('\n') if line.strip()]
    options = []
    current_key = None
    current_text = []
    
    for line in lines:
        m = re.match(r'^([A-D])[\.\:\)]\s*(.*)$', line)
        if m:
            if current_key:
                options.append({'key': current_key, 'text': ' '.join(current_text).strip()})
            current_key = m.group(1)
            current_text = [m.group(2)]
        else:
            if current_key:
                current_text.append(line)
    if current_key:
        options.append({'key': current_key, 'text': ' '.join(current_text).strip()})
    return options

def build():
    print(f"Loading workbook from: {EXCEL_PATH}")
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=False)

    questions = []
    global_id = 0

    for ch in CHAPTER_CONFIG:
        sname = ch["sheet"]
        if sname not in wb.sheetnames:
            print(f"Warning: Sheet {sname} not found!")
            continue

        ws = wb[sname]
        ch_strategy = str(ws.cell(row=3, column=1).value or '').strip()
        ch_traps = str(ws.cell(row=3, column=9).value or '').strip()
        ch["strategy"] = ch_strategy
        ch["traps"] = ch_traps

        ch_q_num = 0

        for r in range(5, ws.max_row + 1):
            raw_q_label = ws.cell(row=r, column=1).value
            topic_str = ws.cell(row=r, column=2).value
            passage = ws.cell(row=r, column=3).value
            prompt = ws.cell(row=r, column=4).value
            options_raw = ws.cell(row=r, column=5).value
            formula = str(ws.cell(row=r, column=7).value or '')
            hint_formula = str(ws.cell(row=r, column=15).value or '')
            strat_tip = str(ws.cell(row=r, column=16).value or '').strip()

            if not (raw_q_label and prompt):
                continue

            # Extract correct answer from formula
            m_ans = re.search(r'=\"([ABCD])\"', formula)
            correct_ans = m_ans.group(1) if m_ans else ''
            if not correct_ans:
                print(f"Error: Could not extract answer for {sname} row {r}")
                continue

            # Extract Socratic hint
            m_hint = re.search(r'Gợi ý:\s*\"?\s*&\s*\"([^\"]+)', hint_formula)
            if not m_hint:
                m_hint = re.search(r'Gợi ý:\s*([^\"&]+)', hint_formula)
            raw_hint = m_hint.group(1).replace("\\'", "'").strip() if m_hint else ""

            # Options
            options = parse_options(options_raw)

            global_id += 1
            ch_q_num += 1

            # Format hints
            # Tier 1: Context & Core Clues (No leak)
            tier1 = f"Đọc kỹ đoạn văn và xác định ngữ cảnh trọng tâm của câu hỏi: {topic_str}. Chú ý mối liên hệ logic giữa các câu văn và từ nối chuyển ý."

            # Tier 2: Socratic Direction & Trap Avoidance (from Excel Hint & Erica Meltzer strategy)
            clean_hint = raw_hint
            # ensure no explicit letter leak in tier 2
            for letter in ["A", "B", "C", "D"]:
                clean_hint = re.sub(rf'\b(đáp án|chọn|phương án)\s+{letter}\b', 'phương án này', clean_hint, flags=re.IGNORECASE)
            
            strat_note = strat_tip if strat_tip else (ch_strategy if ch_strategy else "Tìm dẫn chứng trực tiếp từ đoạn văn, loại trừ phương án quá cực đoan hoặc suy diễn ngoài bài.")
            if clean_hint:
                tier2 = f"{clean_hint} Áp dụng quy tắc vàng Erica Meltzer: {strat_note}"
            else:
                tier2 = f"Áp dụng chiến thuật cốt lõi: {strat_note}"

            # Tier 3: Official Answer & Detailed Rationale
            target_opt = next((o for o in options if o['key'] == correct_ans), None)
            target_text = target_opt['text'] if target_opt else ''
            tier3 = (
                f"Đáp án chính xác là **{correct_ans}** ({target_text}).\n\n"
                f"**Phân tích chi tiết:**\n"
                f"• Văn bản cung cấp manh mối: {raw_hint if raw_hint else prompt}\n"
                f"• Chiến thuật trọng tâm ({ch['short_name']}): {strat_tip if strat_tip else ch_strategy}\n"
                f"• Phương án **{correct_ans}** khớp hoàn hảo với logic và nội dung trong bài, không mắc các bẫy cực đoan hay suy diễn quá đà."
            )

            # Mermaid Flowchart
            mermaid = (
                f"flowchart TD\n"
                f"    A[\"Ngữ cảnh ({ch['short_name']})<br>{topic_str}\"] --> B{{\"Manh mối cốt lõi\"}}\n"
                f"    B --> C[\"{(strat_tip or ch_strategy)[:60]}\"]\n"
                f"    C --> D[\"Đáp án tối ưu: Phương án {correct_ans}\"]"
            )

            q_obj = {
                "id": global_id,
                "master_id": f"EM_Ch{ch['num']}_Q{ch_q_num}",
                "q_number": ch_q_num,
                "q_label": f"Ch.{ch['num']} - Q{ch_q_num}",
                "module_code": ch["module_code"],
                "module_title": ch["name"],
                "section": "Reading and Writing",
                "chapter": ch["name"],
                "chapter_num": ch["num"],
                "topic": f"{ch['short_name']} • {topic_str}",
                "passage": str(passage or '').strip(),
                "prompt": str(prompt or '').strip(),
                "options": options,
                "options_raw": str(options_raw or '').strip(),
                "is_grid_in": False,
                "correct_answer": correct_ans,
                "acceptable_answers": [correct_ans],
                "tier1_hint": tier1,
                "tier2_hint": tier2,
                "tier3_hint": tier3,
                "strategic_tip": strat_tip,
                "mermaid_diagram": mermaid,
                "pdf_page": ch["start_page"],
                "difficulty": "Medium" if ch["num"] <= 5 else "Hard",
                "domain": ch["domain"]
            }
            questions.append(q_obj)

    print(f"Total compiled questions: {len(questions)}")
    assert len(questions) == 74, f"Expected 74 questions, got {len(questions)}"

    # Audit for leaks in Tier 1 and Tier 2
    leaks = 0
    for q in questions:
        for letter in ["A", "B", "C", "D"]:
            pattern = rf"(đáp án|chọn|phương án)\s+(là\s+)?{letter}\b"
            if re.search(pattern, q["tier1_hint"], re.IGNORECASE):
                print(f"[LEAK] Q{q['id']} Tier 1: {q['tier1_hint']}")
                leaks += 1
            if re.search(pattern, q["tier2_hint"], re.IGNORECASE):
                print(f"[LEAK] Q{q['id']} Tier 2: {q['tier2_hint']}")
                leaks += 1

    if leaks == 0:
        print("✅ NO-LEAK AUDIT PASSED: 0 leaks found across all 74 questions!")
    else:
        print(f"❌ WARNING: {leaks} leaks detected.")

    # Build modules list - one for each chapter
    modules = []
    for ch in CHAPTER_CONFIG:
        ch_qs = [q for q in questions if q["module_code"] == ch["module_code"]]
        modules.append({
            "id": f"em_ch{ch['num']}",
            "code": ch["module_code"],
            "chapter_num": ch["num"],
            "title": ch["name"],
            "short_title": ch["short_name"],
            "sub_title": ch["sub_title"],
            "domain": ch["domain"],
            "section": "Reading and Writing",
            "time_minutes": ch["time_minutes"],
            "question_count": len(ch_qs),
            "pdf_start_page": ch["start_page"],
            "strategy": ch.get("strategy", ""),
            "traps": ch.get("traps", ""),
            "question_ids": [q["id"] for q in ch_qs]
        })

    total_time = sum(ch["time_minutes"] for ch in CHAPTER_CONFIG)

    db_data = {
        "test_title": "The Critical Reader: Complete Guide to SAT Reading (Erica Meltzer)",
        "source_attribution": "Erica Lynn Meltzer - The Critical Reader: The Complete Guide to SAT Reading (Digital SAT)",
        "credits": "Compiled and Enhanced by Mike Pham Bá Hong Son - Google for Education Innovator",
        "pdf_drive_id": "10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z",
        "pdf_path": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/preview",
        "pdf_drive_preview": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/preview",
        "pdf_drive_view": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/view",
        "total_questions": 74,
        "time_minutes": total_time,
        "modules_count": len(modules),
        "structure_mode": "chapter_by_chapter",
        "modules": modules,
        "questions": questions
    }

    out_file = os.path.join(os.path.dirname(__file__), OUTPUT_JSON)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(db_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully exported to {out_file} ({os.path.getsize(out_file)} bytes)")

if __name__ == "__main__":
    build()
