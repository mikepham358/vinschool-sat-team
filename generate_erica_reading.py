# -*- coding: utf-8 -*-
"""
Builder for Erica Meltzer Digital SAT Reading Master Guide
Extracts all 74 questions from:
[Edited] Template - Full Erica Meltzer SAT Reading.xlsx
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
        "short_name": "Ch. 2: Vocabulary in Context",
        "domain": "Craft and Structure",
        "start_page": 25,
        "module_code": "RW_Module1",
        "module_num": 1,
        "module_title": "Reading: Part 1 - Foundations & Core Reading (Chương 2 - 4)"
    },
    {
        "sheet": "Ch3_MakingTheLeap",
        "num": 3,
        "name": "Chương 3: Making the Leap (Đại từ & Danh từ nén)",
        "short_name": "Ch. 3: Making the Leap",
        "domain": "Information and Ideas",
        "start_page": 61,
        "module_code": "RW_Module1",
        "module_num": 1,
        "module_title": "Reading: Part 1 - Foundations & Core Reading (Chương 2 - 4)"
    },
    {
        "sheet": "Ch4_BigPicture",
        "num": 4,
        "name": "Chương 4: The Big Picture / Main Idea (Ý chính & Đại ý)",
        "short_name": "Ch. 4: The Big Picture",
        "domain": "Information and Ideas",
        "start_page": 85,
        "module_code": "RW_Module1",
        "module_num": 1,
        "module_title": "Reading: Part 1 - Foundations & Core Reading (Chương 2 - 4)"
    },
    {
        "sheet": "Ch5_LiteralComprehension",
        "num": 5,
        "name": "Chương 5: Literal Comprehension (Đọc hiểu Trực tiếp)",
        "short_name": "Ch. 5: Literal Comprehension",
        "domain": "Information and Ideas",
        "start_page": 111,
        "module_code": "RW_Module2",
        "module_num": 2,
        "module_title": "Reading: Part 2 - Advanced & Rhetorical Reading (Chương 5 - 10)"
    },
    {
        "sheet": "Ch6_ReadingForFunction",
        "num": 6,
        "name": "Chương 6: Reading for Function (Đọc theo Chức năng Diễn ngôn)",
        "short_name": "Ch. 6: Reading for Function",
        "domain": "Craft and Structure",
        "start_page": 139,
        "module_code": "RW_Module2",
        "module_num": 2,
        "module_title": "Reading: Part 2 - Advanced & Rhetorical Reading (Chương 5 - 10)"
    },
    {
        "sheet": "Ch7_TextCompletions",
        "num": 7,
        "name": "Chương 7: Text Completions (Hoàn thành Văn bản / Suy luận)",
        "short_name": "Ch. 7: Text Completions",
        "domain": "Information and Ideas",
        "start_page": 171,
        "module_code": "RW_Module2",
        "module_num": 2,
        "module_title": "Reading: Part 2 - Advanced & Rhetorical Reading (Chương 5 - 10)"
    },
    {
        "sheet": "Ch8_SupportUndermining",
        "num": 8,
        "name": "Chương 8: Supporting & Undermining (Củng cố & Làm suy yếu)",
        "short_name": "Ch. 8: Supporting & Undermining",
        "domain": "Information and Ideas",
        "start_page": 205,
        "module_code": "RW_Module2",
        "module_num": 2,
        "module_title": "Reading: Part 2 - Advanced & Rhetorical Reading (Chương 5 - 10)"
    },
    {
        "sheet": "Ch9_GraphsCharts",
        "num": 9,
        "name": "Chương 9: Graphs & Charts (Biểu đồ & Bảng số liệu)",
        "short_name": "Ch. 9: Graphs & Charts",
        "domain": "Information and Ideas",
        "start_page": 249,
        "module_code": "RW_Module2",
        "module_num": 2,
        "module_title": "Reading: Part 2 - Advanced & Rhetorical Reading (Chương 5 - 10)"
    },
    {
        "sheet": "Ch10_PairedPassages",
        "num": 10,
        "name": "Chương 10: Paired Passages (Đoạn văn Kép)",
        "short_name": "Ch. 10: Paired Passages",
        "domain": "Cross-Text Connections",
        "start_page": 287,
        "module_code": "RW_Module2",
        "module_num": 2,
        "module_title": "Reading: Part 2 - Advanced & Rhetorical Reading (Chương 5 - 10)"
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
    m1_q_num = 0
    m2_q_num = 0

    for ch in CHAPTER_CONFIG:
        sname = ch["sheet"]
        if sname not in wb.sheetnames:
            print(f"Warning: Sheet {sname} not found!")
            continue

        ws = wb[sname]
        ch_strategy = str(ws.cell(row=3, column=1).value or '')
        ch_traps = str(ws.cell(row=3, column=9).value or '')

        for r in range(5, ws.max_row + 1):
            raw_q_label = ws.cell(row=r, column=1).value
            topic_str = ws.cell(row=r, column=2).value
            passage = ws.cell(row=r, column=3).value
            prompt = ws.cell(row=r, column=4).value
            options_raw = ws.cell(row=r, column=5).value
            formula = str(ws.cell(row=r, column=7).value or '')
            hint_formula = str(ws.cell(row=r, column=15).value or '')
            strat_tip = str(ws.cell(row=r, column=16).value or '')

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
            if ch["module_num"] == 1:
                m1_q_num += 1
                q_num = m1_q_num
            else:
                m2_q_num += 1
                q_num = m2_q_num

            # Format hints
            # Tier 1: Context & Core Clues
            tier1 = f"Đọc kỹ đoạn văn và xác định ngữ cảnh trọng tâm của câu hỏi: {topic_str}. Chú ý mối liên hệ logic giữa các câu văn và từ nối chuyển ý."
            
            # Tier 2: Socratic Direction & Trap Avoidance (from Excel Hint & Erica Meltzer strategy)
            clean_hint = raw_hint
            # ensure no explicit letter leak in tier 2
            for letter in ["A", "B", "C", "D"]:
                clean_hint = re.sub(rf'\b(đáp án|chọn|phương án)\s+{letter}\b', 'phương án này', clean_hint, flags=re.IGNORECASE)
            
            if clean_hint:
                tier2 = f"{clean_hint} Áp dụng quy tắc vàng Erica Meltzer: {strat_tip if strat_tip else 'Tìm dẫn chứng trực tiếp từ đoạn văn, loại trừ phương án quá cực đoan hoặc suy diễn ngoài bài.'}"
            else:
                tier2 = f"Áp dụng chiến thuật cốt lõi: {strat_tip if strat_tip else 'Loại trừ các phương án bẫy ngoài phạm vi văn bản hoặc thay đổi quan điểm của tác giả.'}"

            # Tier 3: Official Answer & Detailed Rationale
            target_opt = next((o for o in options if o['key'] == correct_ans), None)
            target_text = target_opt['text'] if target_opt else ''
            tier3 = (
                f"Đáp án chính xác là **{correct_ans}** ({target_text}).\n\n"
                f"**Phân tích chi tiết:**\n"
                f"• Văn bản cung cấp manh mối: {raw_hint if raw_hint else prompt}\n"
                f"• Chiến thuật trọng tâm ({ch['short_name']}): {strat_tip}\n"
                f"• Phương án **{correct_ans}** khớp hoàn hảo với logic và nội dung trong bài, không mắc các bẫy cực đoan hay suy diễn quá đà."
            )

            # Mermaid Flowchart
            mermaid = (
                f"flowchart TD\n"
                f"    A[\"Ngữ cảnh ({ch['short_name']})<br>{topic_str}\"] --> B{{\"Manh mối cốt lõi\"}}\n"
                f"    B --> C[\"{strat_tip[:60] if strat_tip else 'Phân tích logic lập luận'}\"]\n"
                f"    C --> D[\"Đáp án tối ưu: Phương án {correct_ans}\"]"
            )

            q_obj = {
                "id": global_id,
                "master_id": f"EM_{global_id}",
                "q_number": q_num,
                "q_label": f"Q{q_num}",
                "module_code": ch["module_code"],
                "module_title": ch["module_title"],
                "section": "Reading and Writing",
                "module_num": ch["module_num"],
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

    modules = [
        {
            "id": "mod_rw1",
            "code": "RW_Module1",
            "title": "Reading: Part 1 - Foundations & Core Reading (Chương 2 - 4)",
            "section": "Reading and Writing",
            "module_num": 1,
            "time_minutes": 35,
            "question_count": 37,
            "pdf_start_page": 25,
            "question_ids": list(range(1, 38))
        },
        {
            "id": "mod_rw2",
            "code": "RW_Module2",
            "title": "Reading: Part 2 - Advanced & Rhetorical Reading (Chương 5 - 10)",
            "section": "Reading and Writing",
            "module_num": 2,
            "time_minutes": 35,
            "question_count": 37,
            "pdf_start_page": 111,
            "question_ids": list(range(38, 75))
        }
    ]

    db_data = {
        "test_title": "The Critical Reader: Complete Guide to SAT Reading (Erica Meltzer)",
        "source_attribution": "Erica Lynn Meltzer - The Critical Reader: The Complete Guide to SAT Reading (Digital SAT)",
        "credits": "Compiled and Enhanced by Mike Pham Bá Hong Son - Google for Education Innovator",
        "pdf_drive_id": "10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z",
        "pdf_path": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/preview",
        "pdf_drive_preview": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/preview",
        "pdf_drive_view": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/view",
        "total_questions": 74,
        "time_minutes": 70,
        "modules": modules,
        "questions": questions
    }

    out_file = os.path.join(os.path.dirname(__file__), OUTPUT_JSON)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(db_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully exported to {out_file} ({os.path.getsize(out_file)} bytes)")

if __name__ == "__main__":
    build()
