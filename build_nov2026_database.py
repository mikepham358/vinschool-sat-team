#!/usr/bin/env python3
"""
Digital SAT Database Generator - November 2026 (INT-A)
Author: Mike Pham Bá Hồng Sơn - Google for Education Innovator
Pairs 2026 Nov INT - A Test Booklet PDF with Answer Key PDF.
Generates: data/nov2026.json adhering to 4-tier Socratic Feedback & Golden Blueprint.
"""

import os
import sys
import json
import re
import fitz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
STATIC_DATA_DIR = os.path.join(BASE_DIR, "static", "data")

KEY_PDF_PATH = "/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/SAT Coach/Real Tests/Nov 26/2026 Nov INT - A - Answer Key.pdf"
TEST_PDF_PATH = "/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/SAT Coach/Real Tests/Nov 26/2026 Nov INT - A - Test.pdf"
DRIVE_ID = "1OCnVgziQ2ZxoYzUZD9oF_warcJYTGppi"

# Verified Answer Key
ANSWER_KEYS = {
    "RW_Module1": {
        1: "B", 2: "C", 3: "D", 4: "D", 5: "D", 6: "A", 7: "D", 8: "B", 9: "A", 10: "C",
        11: "D", 12: "A", 13: "A", 14: "A", 15: "B", 16: "C", 17: "C", 18: "A", 19: "A", 20: "D",
        21: "B", 22: "C", 23: "C", 24: "A", 25: "C", 26: "B", 27: "D"
    },
    "RW_Module2": {
        1: "D", 2: "D", 3: "C", 4: "D", 5: "C", 6: "D", 7: "D", 8: "A", 9: "B", 10: "A",
        11: "B", 12: "A", 13: "C", 14: "C", 15: "C", 16: "D", 17: "B", 18: "A", 19: "A", 20: "C",
        21: "B", 22: "B", 23: "A", 24: "D", 25: "C", 26: "C", 27: "C"
    },
    "Math_Module1": {
        1: "25", 2: "D", 3: "B", 4: "25", 5: "A", 6: "C", 7: "B", 8: "D", 9: "C", 10: "A",
        11: "B", 12: "D", 13: "37", 14: "B", 15: "C", 16: "D", 17: "A", 18: "C", 19: "A", 20: "37",
        21: "A", 22: "12"
    },
    "Math_Module2": {
        1: "D", 2: "-6", 3: "C", 4: "B", 5: "A", 6: "D", 7: "B", 8: "C", 9: "532", 10: "44",
        11: "B", 12: "A", 13: "D", 14: "C", 15: "1/2, .5, 0.5", 16: "A", 17: "-3", 18: "D", 19: "B", 20: "15",
        21: "D", 22: "C"
    }
}

GRID_IN_SETS = {
    "Math_Module1": {1, 4, 13, 20, 22},
    "Math_Module2": {2, 9, 10, 15, 17, 20}
}

STRATEGY_MAP = {
    "Words in Context": "POOE - Contextual Clues & Tone Matching",
    "Text Structure and Purpose": "Structure & Purpose - Text Mapping",
    "Cross-Text Connections": "Dual-Text Synthesis - Contrast & Agreement",
    "Central Ideas and Details": "Central Idea - Core Thesis Identification",
    "Command of Evidence": "Data & Textual Evidence - Hypothesis Testing",
    "Inferences": "Logical Completion - Restraint & Direct Evidence",
    "Boundaries": "Sentence Boundaries - Independent vs Dependent Clauses",
    "Form, Structure, and Sense": "Grammar - Subject-Verb Agreement & Modifiers",
    "Transitions": "Directional Logic - Contrast vs Continuation vs Cause",
    "Rhetorical Synthesis": "Rhetorical Goal Alignment - Note Selection",
    "Linear equations": "Algebra - Systematic Isolation & Desmos Solve",
    "Linear functions": "Linear Modeling - Slope & Y-Intercept Meaning",
    "Linear inequalities": "Inequality Modeling - Boundary Conditions",
    "Systems of two linear equations": "Linear Systems - Intersection & Matrix Elimination",
    "Nonlinear functions": "Advanced Math - Quadratic/Exponential Vertex & Factors",
    "Nonlinear equations": "Algebraic Substitution & Graph Intersection",
    "Equivalent expressions": "Algebra - Expansion, Factoring & Exponent Laws",
    "One-variable data": "Statistics - Mean, Median, Range & Outliers",
    "Two-variable data": "Data Analysis - Line of Best Fit & Trends",
    "Ratios, rates": "Proportions - Unit Rates & Dimensional Analysis",
    "Percentages": "Percentages - Multipliers & Percent Change",
    "Probability": "Probability - Part over Whole & Conditional Subsets",
    "Lines, angles, and triangles": "Geometry - Angle Relationships & Triangle Sum",
    "Right triangles and trigonometry": "Trigonometry - SOH CAH TOA & Pythagorean Theorem",
    "Area and volume": "Geometry - Standard Area & Volume Formulas",
    "Circles": "Geometry - Standard Circle Equation & Arc Length"
}

def clean_page(page):
    text = page.get_text()
    text = re.sub(r'Digital SAT Practice Test — 2026 Nov INT - A\s*\n', '', text)
    text = re.sub(r'sattest\.hocsat.com\s*\|\s*Page \d+\s*\n', '', text)
    text = re.sub(r'Digital SAT®?\s*\n', '', text)
    text = re.sub(r'Section \d, Module \d: [^\n]+\s*\n', '', text)
    text = re.sub(r'STOP\s*\nIf you finish before time is called[^\n]*\n(?:test\.\s*\n)?', '', text)
    return text

def classify_rw(stem, opts):
    s = stem.lower()
    if 'student has taken the following notes' in s or 'from the notes' in s or 'given sentences' in s:
        return 'Expression of Ideas · Rhetorical Synthesis'
    if 'most nearly mean' in s or 'logical and precise word' in s:
        return 'Craft and Structure · Words in Context'
    if 'main purpose' in s or 'function of the underlined' in s or 'overall structure' in s or 'how the text is organized' in s:
        return 'Craft and Structure · Text Structure and Purpose'
    if 'author of text 2' in s or 'both texts' in s:
        return 'Craft and Structure · Cross-Text Connections'
    if 'central idea' in s or 'main idea' in s or 'according to the text' in s or 'benefit the forest' in s:
        return 'Information and Ideas · Central Ideas and Details'
    if 'data from the table' in s or 'data from the graph' in s or 'support the' in s or 'illustrates the claim' in s:
        return 'Information and Ideas · Command of Evidence'
    if 'logically completes the text' in s or 'conclude' in s:
        return 'Information and Ideas · Inferences'
    if 'logical transition' in s:
        return 'Expression of Ideas · Transitions'
    if 'conforms to the conventions of standard english' in s:
        sample_opt = list(opts.values())[0] if opts else ''
        if any(p in sample_opt for p in [';', ':', '—', ',', '.']):
            return 'Standard English Conventions · Boundaries'
        return 'Standard English Conventions · Form, Structure, and Sense'
    return 'Information and Ideas · Central Ideas and Details'

def classify_math(stem, is_spr, q_num, mod_code):
    s = stem.lower()
    if 'circle' in s:
        return 'Geometry and Trigonometry · Circles'
    if 'triangle' in s or 'cos' in s or 'sin' in s or 'tan' in s or 'similar' in s or 'angle' in s:
        if 'right triangle' in s or 'cos' in s or 'sin' in s or 'tan' in s or 'similar' in s:
            return 'Geometry and Trigonometry · Right triangles and trigonometry'
        return 'Geometry and Trigonometry · Lines, angles, and triangles'
    if 'prism' in s or 'volume' in s or 'area' in s or 'rectangle' in s or 'length' in s and 'width' in s:
        return 'Geometry and Trigonometry · Area and volume'
    if 'scatterplot' in s or 'line of best fit' in s:
        return 'Problem-Solving and Data Analysis · Two-variable data: Models and scatterplots'
    if 'percent' in s or '%' in s:
        return 'Problem-Solving and Data Analysis · Percentages'
    if 'mean' in s or 'median' in s or 'range' in s or 'sample' in s or 'standard deviation' in s:
        return 'Problem-Solving and Data Analysis · One-variable data: Distributions and measures of center and spread'
    if 'gallons' in s or 'ounces' in s or 'speed' in s or 'travels' in s or 'rate' in s or 'ratio' in s:
        return 'Problem-Solving and Data Analysis · Ratios, rates, proportional relationships, and units'
    if 'exponential' in s or '22x' in s or 'population' in s and 'year' in s or '8 13' in s:
        return 'Advanced Math · Nonlinear functions'
    if 'x2' in s or 'quadratic' in s or 'solutions' in s and 'distinct' in s or 'roots' in s:
        return 'Advanced Math · Nonlinear equations in one variable and systems of equations in two variables'
    if 'equivalent' in s or 'expression' in s:
        return 'Advanced Math · Equivalent expressions'
    if 'system of' in s or 'infinitely many solutions' in s or 'system' in s:
        return 'Algebra · Systems of two linear equations in two variables'
    if 'inequality' in s or '<' in s or '>' in s or '≤' in s or '≥' in s or 'shaded region' in s:
        return 'Algebra · Linear inequalities in one or two variables'
    if 'linear function' in s or 'slope' in s or 'intercept' in s or 'f(t)' in s or 'f(x)' in s:
        return 'Algebra · Linear functions'
    return 'Algebra · Linear equations in one variable'

def build_database():
    print("=== Compiling Digital SAT November 2026 Database ===")
    doc = fitz.open(TEST_PDF_PATH)
    
    modules_meta = [
        ("RW_Module1", 2, 12, 27, "Reading & Writing: Module 1", "Reading and Writing", 1, 32, 2),
        ("RW_Module2", 14, 24, 27, "Reading & Writing: Module 2", "Reading and Writing", 2, 32, 14),
        ("Math_Module1", 27, 34, 22, "Math: Module 1", "Math", 1, 35, 26),
        ("Math_Module2", 37, 45, 22, "Math: Module 2", "Math", 2, 35, 36)
    ]

    all_questions = []
    global_id = 1
    modules_json = []

    mod_id_map = {
        "RW_Module1": "rw1",
        "RW_Module2": "rw2",
        "Math_Module1": "math1",
        "Math_Module2": "math2"
    }

    for mod_code, start_p, end_p, total_q, mod_title, section, mod_num, time_min, pdf_start_p in modules_meta:
        full_text = ""
        page_offsets = []
        for p in range(start_p, end_p + 1):
            page_offsets.append((len(full_text), p + 1))
            full_text += f"\n[PAGE_{p+1}]\n" + clean_page(doc[p])

        q_spans = []
        curr_pos = 0
        for q_num in range(1, total_q + 1):
            pattern = rf"\n{q_num}(?:\s*\(Student-produced response\))?\s*\n"
            m = re.search(pattern, full_text[curr_pos:])
            if not m:
                print(f"Error: Question {q_num} not found in {mod_code}")
                sys.exit(1)
            start = curr_pos + m.start()
            end = curr_pos + m.end()
            page_num = start_p + 1
            for off, p in page_offsets:
                if off <= start:
                    page_num = p
                else:
                    break
            
            # Special adjustment for Math 2 Q13: prompt & graph are at top of p.43
            if mod_code == "Math_Module2" and q_num == 13:
                page_num = 43

            is_spr = (q_num in GRID_IN_SETS.get(mod_code, set()))
            q_spans.append((q_num, start, end, page_num, is_spr))
            curr_pos = end

        mod_q_ids = []

        for i in range(len(q_spans)):
            q_num, s_start, s_end, page_num, is_spr = q_spans[i]
            next_start = q_spans[i+1][1] if i + 1 < len(q_spans) else len(full_text)
            block = full_text[s_end:next_start]
            clean_block = re.sub(r"\[PAGE_\d+\]", "", block).strip()

            opt_matches = list(re.finditer(r"(?:^|\n)([A-D])\.\s+(.*?)(?=(?:\n[A-D]\.|\Z))", clean_block, re.DOTALL))
            orig_opts = {}
            if len(opt_matches) == 4:
                stem = clean_block[:opt_matches[0].start()].strip()
                orig_opts = {om.group(1): om.group(2).strip().replace("\n", " ").replace("—", "-").replace("–", "-") for om in opt_matches}
            else:
                stem = clean_block

            # Split passage and prompt
            prompt_keywords = [
                'Which choice', 'Which finding', 'Which quotation', 'Which statement',
                'Which equation', 'Which expression', 'Which of the following',
                'What is the', 'What was the', 'How many', 'According to', 'As used in',
                'The student wants', 'Based on the', 'In the figure', 'If '
            ]
            lines = [l.strip() for l in stem.split("\n") if l.strip()]
            split_idx = -1
            for idx in range(len(lines) - 1, -1, -1):
                line = lines[idx]
                if any(line.startswith(kw) for kw in prompt_keywords) and '?' in ' '.join(lines[idx:]):
                    split_idx = idx
                    break
            if split_idx > 0:
                passage = "\n\n".join(lines[:split_idx]).strip()
                prompt = "\n".join(lines[split_idx:]).strip()
            else:
                passage = ""
                prompt = stem

            corr_ans = ANSWER_KEYS[mod_code][q_num]

            # Topic and Strategy
            if "RW" in mod_code:
                topic = classify_rw(stem, orig_opts)
            else:
                topic = classify_math(stem, is_spr, q_num, mod_code)

            strat = "POOE - Process of Elimination"
            for k_top, v_strat in STRATEGY_MAP.items():
                if k_top in topic:
                    strat = v_strat
                    break

            # Socratic hints (4-tier)
            if "RW" in mod_code:
                corr_txt = orig_opts.get(corr_ans, f"Lựa chọn {corr_ans}")
                t1 = f"Xác định từ khóa trọng tâm, cấu trúc văn bản hoặc mối liên kết logic trong đoạn văn cho chủ đề '{topic}'."
                t2 = f"Đối chiếu các manh mối ngữ cảnh; loại bỏ các phương án bẫy (quá cực đoan, sai phạm vi dữ kiện hoặc lạc đề)."
                t3 = f"Phương án đúng hoàn toàn là [{corr_ans}]: '{corr_txt}'."
                stip = f"Mẹo College Board: Với dạng '{topic}', luôn dựa vào bằng chứng trực tiếp trong bài đọc, không suy đoán ngoài văn bản."
            else:
                if is_spr:
                    t1 = f"Phân tích yêu cầu bài toán và thiết lập phương trình / biểu thức toán học cho dạng '{topic}'."
                    t2 = f"Biến đổi đại số từng bước hoặc sử dụng máy tính Desmos để tìm nghiệm chính xác."
                    t3 = f"Kết quả chính xác cần điền vào ô trống là [{corr_ans}]."
                    stip = "Mẹo Grid-in: Kiểm tra kỹ dấu âm/dương, rút gọn phân số tối giản hoặc kiểm tra điều kiện đề bài."
                else:
                    corr_txt = orig_opts.get(corr_ans, f"Lựa chọn {corr_ans}")
                    t1 = f"Xác định đại lượng cần tìm và các mối quan hệ cho trước trong câu hỏi thuộc chủ đề '{topic}'."
                    t2 = f"Áp dụng định lý/công thức chuẩn hoặc vẽ đồ thị / thế số trên Desmos để loại bỏ phương án sai."
                    t3 = f"Phương án chính xác là [{corr_ans}]: '{corr_txt}'."
                    stip = "Mẹo Toán SAT: Đọc kỹ câu hỏi hỏi về x, y hay giá trị của một biểu thức kết hợp."

            # Golden Rule: Options formatted as 'Lựa chọn A/B/C/D'
            if is_spr:
                options = []
                options_raw = "Student-Produced Response (Grid-in)"
                option_exps = {}
                pooe_breakdown = f"• Đáp án ĐÚNG: {corr_ans}\n• Phương pháp: Áp dụng công thức và tính toán cẩn thận để tìm ra kết quả {corr_ans}."
            else:
                options = [
                    {"key": "A", "text": "Lựa chọn A"},
                    {"key": "B", "text": "Lựa chọn B"},
                    {"key": "C", "text": "Lựa chọn C"},
                    {"key": "D", "text": "Lựa chọn D"}
                ]
                options_raw = "A. Lựa chọn A\nB. Lựa chọn B\nC. Lựa chọn C\nD. Lựa chọn D"
                
                # Detailed why-right / why-wrong with NO em dashes (only '-')
                option_exps = {}
                pooe_breakdown_lines = []
                corr_txt = orig_opts.get(corr_ans, f"Lựa chọn {corr_ans}")
                
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr_ans:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Đáp ứng hoàn hảo yêu cầu đề bài và khớp với dữ kiện trong bài đọc / phép tính toán."
                        pooe_breakdown_lines.insert(0, f"• Đáp án ĐÚNG: {k}. {txt} - Thỏa mãn đầy đủ tiêu chí logic và bằng chứng học thuật.")
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Không phù hợp với dữ kiện đề bài, chứa bẫy sai lệch hoặc suy diễn ngoài phạm vi."
                        pooe_breakdown_lines.append(f"• Loại {k}. {txt} - Sai sót thông tin hoặc không trả lời đúng câu hỏi.")
                
                pooe_breakdown = "\n".join(pooe_breakdown_lines)

            # Difficulty estimation
            diff = "Easy" if q_num <= 8 else ("Hard" if q_num >= 20 else "Medium")

            q_obj = {
                "id": global_id,
                "master_id": f"M{global_id}",
                "q_number": q_num,
                "q_label": f"Q{q_num}",
                "module_code": mod_code,
                "module_title": mod_title,
                "section": section,
                "module_num": mod_num,
                "topic": topic,
                "passage": passage,
                "prompt": prompt,
                "options": options,
                "options_raw": options_raw,
                "is_grid_in": is_spr,
                "correct_answer": corr_ans,
                "tier1_hint": t1,
                "tier2_hint": t2,
                "tier3_hint": t3,
                "strategic_tip": stip,
                "level1_tip": t1,
                "level2_hint": t2,
                "level3_solution": t3,
                "pdf_page": page_num,
                "difficulty": diff,
                "target_clue": f"Dữ kiện trọng tâm liên quan đến '{topic}' trong đề bài.",
                "solution_steps": f"Phân tích dữ kiện và áp dụng phương pháp chuẩn cho {topic}.",
                "princeton_strategy": strat,
                "pro_tip": "Tận dụng tối đa phương pháp loại trừ (POOE) và máy tính Desmos để tối ưu tốc độ và độ chính xác.",
                "pooe_breakdown": pooe_breakdown,
                "option_explanations": option_exps
            }

            if is_spr:
                q_obj["grid_in_explanation"] = {
                    "correct_answer": corr_ans,
                    "solution_steps": f"Thực hiện các bước giải toán theo chủ đề '{topic}' để tìm ra đáp số {corr_ans}.",
                    "trap_errors": "Cẩn thận kiểm tra các bẫy đổi đơn vị, làm tròn số thập phân, hoặc điều kiện bài toán."
                }

            all_questions.append(q_obj)
            mod_q_ids.append(global_id)
            global_id += 1

        modules_json.append({
            "id": mod_id_map.get(mod_code, mod_code.lower()),
            "code": mod_code,
            "title": mod_title,
            "section": section,
            "module_num": mod_num,
            "time_minutes": time_min,
            "question_count": total_q,
            "pdf_start_page": pdf_start_p,
            "question_ids": mod_q_ids
        })

    pdf_preview = f"https://drive.google.com/file/d/{DRIVE_ID}/preview"
    pdf_view = f"https://drive.google.com/file/d/{DRIVE_ID}/view"

    db_obj = {
        "test_title": "Digital SAT Practice Test - November 2026 (INT-A)",
        "test_id": "nov2026",
        "source_attribution": "Real Test Tháng 11/2026 (INT-A)",
        "credits": "Curated & Pedagogically Structured by Mike Pham Bá Hồng Sơn - Google for Education Innovator",
        "pdf_path": TEST_PDF_PATH,
        "pdf_drive_preview": pdf_preview,
        "pdf_drive_view": pdf_view,
        "excel_path": "",
        "total_questions": len(all_questions),
        "modules": modules_json,
        "questions": all_questions,
        "initial_error_logs": [],
        "strategies": []
    }

    # Save to data/nov2026.json
    out_file = os.path.join(DATA_DIR, "nov2026.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(db_obj, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}!")

    # Mirror to static/data/nov2026.json
    static_out_file = os.path.join(STATIC_DATA_DIR, "nov2026.json")
    with open(static_out_file, "w", encoding="utf-8") as f:
        json.dump(db_obj, f, indent=2, ensure_ascii=False)
    print(f"Mirrored to {static_out_file}!")

    return db_obj

if __name__ == "__main__":
    build_database()
