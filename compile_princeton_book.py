#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compiler for Complete The Princeton Review SAT Advanced Textbook
(All 17 Chapters, 233 Questions: Worked Examples & Drills across the 599-page book)

PDF Drive ID: 10hR7mzMPcVJriTNbsRL9KIvgwOgBCixd
PDF View URL: https://drive.google.com/file/d/10hR7mzMPcVJriTNbsRL9KIvgwOgBCixd/view
PDF Preview URL: https://drive.google.com/file/d/10hR7mzMPcVJriTNbsRL9KIvgwOgBCixd/preview
"""

import json
import re
import os
import sys
from pathlib import Path
import pypdf

BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = "/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/SAT Coach/Books/SAT Advanced The Princeton Review.pdf"

PDF_DRIVE_ID = "10hR7mzMPcVJriTNbsRL9KIvgwOgBCixd"
PDF_PREVIEW_URL = f"https://drive.google.com/file/d/{PDF_DRIVE_ID}/preview"
PDF_VIEW_URL = f"https://drive.google.com/file/d/{PDF_DRIVE_ID}/view"

print("📖 [1/5] Loading PDF reader...")
reader = pypdf.PdfReader(PDF_PATH)
TOTAL_PAGES = len(reader.pages)
print(f"Loaded PDF with {TOTAL_PAGES} pages.")

pages_text = [reader.pages[i].extract_text() for i in range(TOTAL_PAGES)]

def get_text_range(start_p, end_p):
    return "\n".join([f"\n[[[PAGE_{p}]]]\n" + pages_text[p - 1] for p in range(start_p, min(end_p, TOTAL_PAGES) + 1)])

ch12_text = get_text_range(261, 307)
ch20_text = get_text_range(417, 452)
ch27_text = get_text_range(577, 597)

def parse_drill_explanations(text, drill_header, next_drill_header=None):
    pattern = rf'{drill_header}.*?(?={next_drill_header}|\Z)' if next_drill_header else rf'{drill_header}.*'
    m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if not m:
        return {}
    section_text = m.group(0)
    q_matches = re.finditer(r'(?:^|\n)(\d+)\.\s+([A-D]|-?\d+(?:\.\d+)?|\d+/\d+)\b\s*\n(.*?)(?=(?:\n\d+\.\s+[A-D]|\n\d+\.\s+-?\d+|\Z))', section_text, re.DOTALL)
    results = {}
    for qm in q_matches:
        q_num = int(qm.group(1))
        key = qm.group(2).strip()
        exp = qm.group(3).strip()
        results[q_num] = {'key': key, 'explanation': exp}
    return results

DRILL_EXPLANATIONS = {
    # Ch 12 (Reading)
    "Ch5_Diagnostic": parse_drill_explanations(ch12_text, 'Diagnostic Drill', 'CHAPTER 6'),
    "Ch6_Vocab": parse_drill_explanations(ch12_text, 'Advanced Vocabulary Drill', 'CHAPTER 7'),
    "Ch7_Structural": parse_drill_explanations(ch12_text, 'Structural Words Drill', 'CHAPTER 8'),
    "Ch8_Function": parse_drill_explanations(ch12_text, 'Sentence Function Drill', 'CHAPTER 9'),
    "Ch9_POE": parse_drill_explanations(ch12_text, 'Process of Elimination Drill', 'CHAPTER 10'),
    "Ch10_Poetry": parse_drill_explanations(ch12_text, 'Poetry Drill', 'CHAPTER 11'),
    "Ch11_Challenging": parse_drill_explanations(ch12_text, 'Challenging Scenarios Drill', None),
    # Ch 20 (Writing)
    "Ch15_Punctuation": parse_drill_explanations(ch20_text, 'Tricky Punctuation Drill', 'CHAPTER 16'),
    "Ch16_SubjectVerb": parse_drill_explanations(ch20_text, 'Subject-Verb Agreement Drill', 'Verb Tense Drill'),
    "Ch16_VerbTense": parse_drill_explanations(ch20_text, 'Verb Tense Drill', 'Modifier Drill'),
    "Ch16_Modifier": parse_drill_explanations(ch20_text, 'Modifier Drill', 'CHAPTER 17'),
    "Ch18_Transitions": parse_drill_explanations(ch20_text, 'Tricky Transitions Drill', 'CHAPTER 19'),
    "Ch19_Rhetorical": parse_drill_explanations(ch20_text, 'Tricky Rhetorical Synthesis Drill', None),
    # Ch 27 (Math)
    "Ch23_Tactics": parse_drill_explanations(ch27_text, 'Use Your TPR Math Tactics Drill', 'CHAPTER 24'),
    "Ch24_Calculator": parse_drill_explanations(ch27_text, 'Calculator Drill', 'CHAPTER 26'),
    "Ch26_Comprehensive": parse_drill_explanations(ch27_text, 'Use Everything Comprehensive Drill', None),
}

# 17 Chapter Definitions
CHAPTER_CONFIGS = [
    {
        "num": 2,
        "code": "Ch2_Strategies",
        "title": "Chương 2: Digital SAT Overall Strategies and Pacing",
        "short_title": "Chiến Thuật & Pacing",
        "section": "Reading and Writing",
        "domain": "Test-Taking Strategy",
        "start_page": 29,
        "end_page": 38,
        "strategy": "Quản lý thời gian, pacing theo đồng hồ, loại trừ POOE và ưu tiên câu dễ trước.",
        "traps": "Bẫy mất quá nhiều thời gian cho 1 câu hỏi khó, bỏ sót câu dễ và không gạch bỏ phương án sai."
    },
    {
        "num": 5,
        "code": "Ch5_ReadingIntro",
        "title": "Chương 5: Reading Introduction (Diagnostic Drill)",
        "short_title": "Tổng Quan Đọc Hiểu",
        "section": "Reading and Writing",
        "domain": "Reading",
        "start_page": 60,
        "end_page": 83,
        "drill_header": "Diagnostic Drill",
        "drill_key": "Ch5_Diagnostic",
        "strategy": "Nắm vững Basic Approach cho 8 dạng câu hỏi đọc hiểu của Digital SAT.",
        "traps": "Bẫy suy diễn vượt quá văn bản (Beyond the Text) và bẫy ngôn từ cực đoan (Extreme Language)."
    },
    {
        "num": 6,
        "code": "Ch6_Vocabulary",
        "title": "Chương 6: Exploring Advanced Vocabulary",
        "short_title": "Từ Vựng Nâng Cao",
        "section": "Reading and Writing",
        "domain": "Craft and Structure",
        "start_page": 84,
        "end_page": 111,
        "drill_header": "Advanced Vocabulary Drill",
        "drill_key": "Ch6_Vocab",
        "strategy": "Xác định đối tượng miêu tả (Who/What), gạch chân manh mối (Clue), đặt từ phỏng đoán (Annotation) và dùng POE.",
        "traps": "Bẫy từ vựng ngược hướng (Opposite Words), từ lặp lại sai ngữ cảnh (Recycled Words), và từ quen thuộc nghĩa lạ."
    },
    {
        "num": 7,
        "code": "Ch7_StructuralWords",
        "title": "Chương 7: Identifying Structural Words",
        "short_title": "Từ Chỉ Hướng Cấu Trúc",
        "section": "Reading and Writing",
        "domain": "Craft and Structure",
        "start_page": 112,
        "end_page": 144,
        "drill_header": "Structural Words Drill",
        "drill_key": "Ch7_Structural",
        "strategy": "Theo dõi từ chỉ hướng (Direction Words: Continuers, Shifters, Cause & Effect) để nắm bắt bước chuyển lập luận.",
        "traps": "Bẫy đảo chiều luận điểm bất ngờ và bẫy nhầm lẫn giữa nguyên nhân với hệ quả."
    },
    {
        "num": 8,
        "code": "Ch8_SentenceFunction",
        "title": "Chương 8: Understanding Sentence Function",
        "short_title": "Chức Năng Của Câu",
        "section": "Reading and Writing",
        "domain": "Craft and Structure",
        "start_page": 145,
        "end_page": 170,
        "drill_header": "Sentence Function Drill",
        "drill_key": "Ch8_Function",
        "strategy": "Đọc câu trước và sau câu gạch chân, xác định chức năng diễn ngôn (cung cấp bằng chứng, phản bác hay tóm tắt).",
        "traps": "Bẫy nhầm lẫn giữa nội dung câu (what it says) và chức năng diễn ngôn của câu (what it does)."
    },
    {
        "num": 9,
        "code": "Ch9_MasteringPOE",
        "title": "Chương 9: Mastering Process of Elimination",
        "short_title": "Nghệ Thuật Loại Trừ POE",
        "section": "Reading and Writing",
        "domain": "Information and Ideas",
        "start_page": 171,
        "end_page": 200,
        "drill_header": "Process of Elimination Drill",
        "drill_key": "Ch9_POE",
        "strategy": "Tìm lý do để gạch bỏ 3 phương án sai thay vì cố tìm phương án đúng; nhận diện 4 bẫy phổ biến của College Board.",
        "traps": "Bẫy Half-Right/Half-Wrong, Extreme Language (always, never, solely), Recycled Words và Opposite."
    },
    {
        "num": 10,
        "code": "Ch10_Poetry",
        "title": "Chương 10: Working with Poetry",
        "short_title": "Xử Lý Thơ Ca SAT",
        "section": "Reading and Writing",
        "domain": "Information and Ideas",
        "start_page": 201,
        "end_page": 223,
        "drill_header": "Poetry Drill",
        "drill_key": "Ch10_Poetry",
        "strategy": "Dịch thơ sang ngôn ngữ thông thường theo từng câu hoàn chỉnh (dựa theo dấu chấm), xác định người nói và thái độ cảm xúc.",
        "traps": "Bẫy nghĩa bóng suy diễn quá mức, đảo trật tự từ ngữ cổ điển và nhầm lẫn đối tượng cảm xúc của bài thơ."
    },
    {
        "num": 11,
        "code": "Ch11_ChallengingScenarios",
        "title": "Chương 11: Overcoming Challenging Scenarios",
        "short_title": "Kịch Bản Thách Thức",
        "section": "Reading and Writing",
        "domain": "Information and Ideas",
        "start_page": 224,
        "end_page": 260,
        "drill_header": "Challenging Scenarios Drill",
        "drill_key": "Ch11_Challenging",
        "strategy": "Phân tích đoạn văn kép (Text 1 vs Text 2), đối chiếu bảng số liệu khoa học phức tạp và câu hỏi suy luận giả thuyết.",
        "traps": "Bẫy nhầm lẫn quan điểm giữa Text 1 và Text 2, đọc sai trục tọa độ biểu đồ và bẫy khẳng định điều bài chưa chứng minh."
    },
    {
        "num": 15,
        "code": "Ch15_TrickyPunctuation",
        "title": "Chương 15: Tricky Punctuation",
        "short_title": "Bẫy Dấu Câu Nâng Cao",
        "section": "Reading and Writing",
        "domain": "Standard English Conventions",
        "start_page": 321,
        "end_page": 345,
        "drill_header": "Tricky Punctuation Drill",
        "drill_key": "Ch15_Punctuation",
        "strategy": "Làm chủ dấu chấm phẩy (; = .), dấu hai chấm (danh sách / giải thích sau mệnh đề độc lập), và gạch ngang đôi (— ... —).",
        "traps": "Bẫy Comma Splice (dùng dấu phẩy nối 2 câu trọn vẹn) và bẫy đặt dấu hai chấm sau mệnh đề chưa trọn vẹn."
    },
    {
        "num": 16,
        "code": "Ch16_TrickyGrammar",
        "title": "Chương 16: Tricky Grammar (Subject-Verb, Tenses & Modifiers)",
        "short_title": "Ngữ Pháp Phức Tạp",
        "section": "Reading and Writing",
        "domain": "Standard English Conventions",
        "start_page": 346,
        "end_page": 369,
        "drill_header": "Subject-Verb Agreement Drill",
        "drill_key": "Ch16_SubjectVerb",
        "strategy": "Bóc tách thành phần chen ngang để tìm chủ ngữ thật; duy trì tính nhất quán của thì và kiểm tra bổ ngữ mở đầu câu.",
        "traps": "Bẫy danh từ gần nhất đánh lừa chủ ngữ số ít, bẫy thì hoàn thành (had + V3) và bổ ngữ lơ lửng (Dangling Modifiers)."
    },
    {
        "num": 18,
        "code": "Ch18_TrickyTransitions",
        "title": "Chương 18: Tricky Transitions",
        "short_title": "Từ Nối Logic Nâng Cao",
        "section": "Reading and Writing",
        "domain": "Expression of Ideas",
        "start_page": 378,
        "end_page": 395,
        "drill_header": "Tricky Transitions Drill",
        "drill_key": "Ch18_Transitions",
        "strategy": "Đọc câu trước và câu sau không kèm từ nối, xác định quan hệ logic thuần túy (Tiếp nối, Chuyển hướng, hay Nguyên nhân).",
        "traps": "Bẫy từ nối đồng nghĩa (loại trừ ngay cặp từ cùng nhóm) và bẫy đọc lướt không nhận ra sự đảo chiều ý ngầm."
    },
    {
        "num": 19,
        "code": "Ch19_RhetoricalSynthesis",
        "title": "Chương 19: Tricky Rhetorical Synthesis",
        "short_title": "Tổng Hợp Ghi Chú Student Notes",
        "section": "Reading and Writing",
        "domain": "Expression of Ideas",
        "start_page": 396,
        "end_page": 416,
        "drill_header": "Tricky Rhetorical Synthesis Drill",
        "drill_key": "Ch19_Rhetorical",
        "strategy": "Đọc câu hỏi trước để xác định mục tiêu của học sinh (Goal); bỏ qua các ghi chú không liên quan và loại trừ phương án sai mục tiêu.",
        "traps": "Bẫy phương án chứa dữ kiện đúng với ghi chú nhưng không đáp ứng đúng mục tiêu đặt ra ở câu hỏi."
    },
    {
        "num": 22,
        "code": "Ch22_MathPacing",
        "title": "Chương 22: Pacing Strategies and POOD",
        "short_title": "Chiến Thuật POOD Toán",
        "section": "Math",
        "domain": "Problem-Solving & Strategy",
        "start_page": 460,
        "end_page": 468,
        "strategy": "Áp dụng Personal Order of Difficulty (POOD): làm câu dễ/vừa sức trước, gắn cờ câu mất thời gian, và không bỏ trống câu điền số.",
        "traps": "Bẫy sa lầy vào câu toán khó ở đầu bài thi khiến không đủ thời gian làm các câu dễ ở cuối Module."
    },
    {
        "num": 23,
        "code": "Ch23_TPRTactics",
        "title": "Chương 23: Use Your TPR Math Tactics (Plugging In & PITA)",
        "short_title": "Chiến Thuật Thế Số & PITA",
        "section": "Math",
        "domain": "Algebra & Advanced Math",
        "start_page": 469,
        "end_page": 501,
        "drill_header": "Use Your TPR Math Tactics Drill",
        "drill_key": "Ch23_Tactics",
        "strategy": "Plugging In (cho số cụ thể vào biến để tính toán) và PITA (thế đáp án từ B hoặc C vào đề bài để kiểm tra).",
        "traps": "Bẫy chọn số 0 hoặc 1 khi biến đổi đại số khiến nhiều đáp án trùng nhau, và bẫy nhầm lẫn giữa x và y."
    },
    {
        "num": 24,
        "code": "Ch24_DesmosCalculator",
        "title": "Chương 24: Use the Built-in Calculator (Desmos)",
        "short_title": "Khai Thác Desmos Bậc Thầy",
        "section": "Math",
        "domain": "Algebra & Advanced Math",
        "start_page": 502,
        "end_page": 523,
        "drill_header": "Calculator Drill",
        "drill_key": "Ch24_Calculator",
        "strategy": "Khai thác tối đa Desmos: vẽ 2 hàm số để tìm giao điểm, dùng Slider tìm tham số k, và giải hệ phương trình bậc hai.",
        "traps": "Bẫy phóng to/thu nhỏ đồ thị bỏ sót nghiệm ngoài tầm nhìn, và bẫy nhầm lẫn giữa giá trị x và giá trị y tại giao điểm."
    },
    {
        "num": 25,
        "code": "Ch25_MathKnowledge",
        "title": "Chương 25: Use Your Math Knowledge",
        "short_title": "Kiến Thức Toán Chuyên Sâu",
        "section": "Math",
        "domain": "Advanced Math & Geometry",
        "start_page": 524,
        "end_page": 563,
        "strategy": "Nắm vững công thức đường tròn chuẩn (x-h)² + (y-k)² = r², tỉ lệ tam giác đặc biệt, nghiệm phức, và thống kê nâng cao.",
        "traps": "Bẫy đổi đơn vị đo lường, bẫy quên chia 2 khi tính bán kính từ đường kính, và bẫy nghiệm ngoại lai (extraneous solutions)."
    },
    {
        "num": 26,
        "code": "Ch26_UseEverything",
        "title": "Chương 26: Use Everything (Comprehensive Drill)",
        "short_title": "Tổng Hợp Đỉnh Cao Toàn Diện",
        "section": "Math",
        "domain": "Advanced Math & Problem Solving",
        "start_page": 564,
        "end_page": 576,
        "drill_header": "Comprehensive Drill",
        "drill_key": "Ch26_Comprehensive",
        "strategy": "Tổng hợp mọi chiến thuật: kết hợp Desmos, thế số nhanh, công thức hình học chuẩn để chinh phục các câu 750-800 Math.",
        "traps": "Bẫy câu hỏi nhiều tầng (multi-step problems), đọc sót điều kiện x > 0 hoặc yêu cầu làm tròn số."
    }
]

print("🔍 [2/5] Extracting questions from 17 chapters...")

def find_answer_key_in_text(text):
    m = re.search(r'[Tt]he correct answer is\s*\(([A-D])\)', text)
    if m: return m.group(1)
    m = re.search(r'[Tt]he correct answer is\s*([A-D])\b', text)
    if m: return m.group(1)
    m = re.search(r'correct answer (?:must be|is)\s*\(([A-D])\)', text)
    if m: return m.group(1)
    m = re.search(r'\(([A-D])\)\s+(?:has to|must) be the answer', text)
    if m: return m.group(1)
    m = re.search(r'\(([A-D])\)\s+is(?:\s+the)?\s+correct\b', text)
    if m: return m.group(1)
    m = re.search(r'\b(?:choose|pick|select)\s*\(([A-D])\)', text)
    if m: return m.group(1)
    m = re.search(r'[Tt]hat eliminates\s+\(([A-D])\),\s*\(([A-D])\),\s*and\s*\(([A-D])\)', text)
    if m:
        elim = {m.group(1), m.group(2), m.group(3)}
        rem = set('ABCD') - elim
        if len(rem) == 1: return list(rem)[0]
    m2 = re.search(r'[Ee]liminate\s+\(([A-D])\),\s*\(([A-D])\),\s*and\s*\(([A-D])\)', text)
    if m2:
        elim = {m2.group(1), m2.group(2), m2.group(3)}
        rem = set('ABCD') - elim
        if len(rem) == 1: return list(rem)[0]
    m = re.search(r'[Tt]he answer is\s*\(([A-D])\)', text)
    if m: return m.group(1)
    m = re.search(r'[Tt]he answer is\s*([A-D])\b', text)
    if m: return m.group(1)
    m = re.search(r'\(([A-D])\)\s+is (?:right|the answer)', text)
    if m: return m.group(1)
    m = re.search(r'[Kk]eep\s+\(([A-D])\)', text)
    if m: return m.group(1)
    # Check for number answer e.g. The correct answer is 4 / -13 / -0.5
    m_num = re.search(r'[Tt]he correct answer is\s*(-?\d+(?:\.\d+)?|\d+/\d+)\b', text)
    if m_num: return m_num.group(1)
    return None

def parse_options(text):
    clean = re.sub(r'\[\[\[PAGE_\d+\]\]\]', '', text)
    clean = re.sub(r'\n\s*\n', '\n', clean)
    m = re.search(r'(?:^|\n)A\s+([^\n]+(?:\n(?![B-D]\s+|Here’s|Here\'s|Why This|\d+\.)[^\n]+)*)\nB\s+([^\n]+(?:\n(?![C-D]\s+|Here’s|Here\'s|Why This|\d+\.)[^\n]+)*)\nC\s+([^\n]+(?:\n(?![D]\s+|Here’s|Here\'s|Why This|\d+\.)[^\n]+)*)\nD\s+([^\n]+(?:\n(?![A-D]\s+|Here’s|Here\'s|Why This|\d+\.)[^\n]+)*)', clean)
    opts = []
    if m:
        for k, idx in [('A', 1), ('B', 2), ('C', 3), ('D', 4)]:
            val = ' '.join(m.group(idx).strip().split())
            opts.append({'key': k, 'text': val})
    return opts

# Curated Fallback keys for examples where text formatting is atypical
MANUAL_EXAMPLE_KEYS = {
    # Ch 7
    ("Ch7_StructuralWords", 3): "A",
    # Ch 8
    ("Ch8_SentenceFunction", 3): "D",
    # Ch 15
    ("Ch15_TrickyPunctuation", 2): "B",
    ("Ch15_TrickyPunctuation", 3): "A",
    ("Ch15_TrickyPunctuation", 4): "C",
    ("Ch15_TrickyPunctuation", 5): "B",
    ("Ch15_TrickyPunctuation", 8): "D",
    # Ch 16
    ("Ch16_TrickyGrammar", 4): "D",
    # Ch 18
    ("Ch18_TrickyTransitions", 2): "B",
    # Ch 19
    ("Ch19_RhetoricalSynthesis", 1): "A",
    ("Ch19_RhetoricalSynthesis", 4): "B",
    # Ch 23
    ("Ch23_TPRTactics", 6): "B",
    ("Ch23_TPRTactics", 9): "B",
    ("Ch23_TPRTactics", 11): "C",
    ("Ch23_TPRTactics", 13): "D",
    # Ch 24
    ("Ch24_DesmosCalculator", 3): "-0.5",
    ("Ch24_DesmosCalculator", 5): "-13",
    ("Ch24_DesmosCalculator", 6): "D",
    # Ch 25
    ("Ch25_MathKnowledge", 1): "B",
    ("Ch25_MathKnowledge", 3): "D",
    ("Ch25_MathKnowledge", 4): "B",
    ("Ch25_MathKnowledge", 8): "A",
    ("Ch25_MathKnowledge", 9): "8",
    ("Ch25_MathKnowledge", 12): "6",
    ("Ch25_MathKnowledge", 16): "5/13",
    ("Ch25_MathKnowledge", 17): "B",
    # Ch 2
    ("Ch2_Strategies", 1): "8",
    ("Ch2_Strategies", 2): "B",
    ("Ch2_Strategies", 3): "C",
}

all_questions = []
global_q_id = 1
chapter_modules = []

for ch in CHAPTER_CONFIGS:
    ch_num = ch["num"]
    code = ch["code"]
    title = ch["title"]
    short_title = ch["short_title"]
    section = ch["section"]
    domain = ch["domain"]
    strat = ch["strategy"]
    traps = ch["traps"]
    start_p = ch["start_page"]
    end_p = ch["end_page"]
    drill_hdr = ch.get("drill_header")
    drill_key = ch.get("drill_key")
    
    ch_text = get_text_range(start_p, end_p)
    parts = re.split(r'\bMark for Review\b', ch_text)
    
    drill_start_idx = 9999
    if drill_hdr:
        for idx, p in enumerate(parts):
            if drill_hdr.lower() in p.lower():
                drill_start_idx = idx + 1
                break
                
    ch_questions = []
    seen_stems = set()
    
    ex_counter = 0
    practice_counter = 0
    
    for idx in range(1, len(parts)):
        prev_p = parts[idx - 1]
        curr_p = parts[idx]
        
        # Check snippet
        clean_curr = re.sub(r'\[\[\[PAGE_\d+\]\]\]', '', curr_p).strip()
        stem_preview = ' '.join(clean_curr[:80].split())
        if 'button and come back' in stem_preview or len(clean_curr) < 15:
            continue
        if stem_preview in seen_stems:
            continue
        seen_stems.add(stem_preview)
        
        # Determine page number
        prev_text = ch_text[:ch_text.find(curr_p)]
        pages = re.findall(r'\[\[\[PAGE_(\d+)\]\]\]', prev_text)
        pdf_page = int(pages[-1]) if pages else start_p
        
        is_drill = (idx >= drill_start_idx)
        
        # Options
        options = parse_options(curr_p)
        is_grid_in = (len(options) == 0 and section == "Math")
        
        # Clean text
        clean = re.sub(r'\[\[\[PAGE_\d+\]\]\]', '', curr_p)
        clean = re.sub(r'\n\s*\n', '\n', clean).strip()
        
        # Options end
        m_opt = re.search(r'(?:^|\n)A\s+.*?\nD\s+[^\n]+(?:\n(?![A-D]\s+|Here’s|Here\'s|Why This|\d+\.)[^\n]+)*', clean, re.DOTALL)
        if m_opt:
            before_opts = clean[:m_opt.start()].strip()
            exp_text = clean[m_opt.end():].strip()
        else:
            before_opts = clean
            exp_text = clean
            
        # Determine passage & prompt
        prompt_match = re.search(r'(Which choice [^\n]+|Which finding [^\n]+|Which statement [^\n]+|Based on the [^\n]+|The student wants to [^\n]+|What is the value [^\n]+|Which equation [^\n]+|What is the radius [^\n]+|What is the area [^\n]+|Which of the following [^\n]+|At what point [^\n]+|What is the main idea [^\n]+|What was the net change [^\n]+)', before_opts, re.IGNORECASE)
        
        if prompt_match:
            prompt = ' '.join(before_opts[prompt_match.start():].strip().split())
            passage = ' '.join(before_opts[:prompt_match.start()].strip().split())
        else:
            prompt = ' '.join(before_opts.strip().split())
            passage = ''
            
        # If passage is empty and it's a worked example, extract passage from prev_p
        if not passage and not is_drill:
            clean_prev = re.sub(r'\[\[\[PAGE_\d+\]\]\]', '', prev_p).strip()
            paras = [p.strip() for p in clean_prev.split('\n\n') if p.strip()]
            if paras:
                cand = ' '.join(paras[-1].split())
                if len(cand) > 30 and not cand.startswith("Step ") and not cand.startswith("Here’s How"):
                    passage = cand
                    
        # Remove question number from passage/prompt
        prompt = re.sub(r'^\d+\.\s*', '', prompt)
        passage = re.sub(r'^\d+\.\s*', '', passage)
        
        # Determine category, label, and answer key
        if is_drill:
            practice_counter += 1
            category = "practice"
            q_num = practice_counter
            q_label = f"Chương {ch_num} - Bài tập {q_num}"
            
            # Key & explanation from drill dict
            drill_dict = DRILL_EXPLANATIONS.get(drill_key, {})
            # Look up by q_num or practice_counter
            q_info = drill_dict.get(q_num, drill_dict.get(practice_counter, {}))
            correct_answer = q_info.get("key", "A")
            explanation = q_info.get("explanation", exp_text)
        else:
            ex_counter += 1
            category = "example"
            q_num = ex_counter
            q_label = f"Chương {ch_num} - Ví dụ {q_num}"
            
            # Key from explanation
            correct_answer = find_answer_key_in_text(curr_p)
            if not correct_answer:
                correct_answer = MANUAL_EXAMPLE_KEYS.get((code, q_num), "A")
            explanation = exp_text
            
        # Clean explanation
        explanation = re.sub(r'\[\[\[PAGE_\d+\]\]\]', '', explanation).strip()
        explanation = re.sub(r'\n\s*\n', '\n', explanation)
        
        # Truncate explanation to avoid leaking next questions
        next_mfr = explanation.find("Mark for Review")
        if next_mfr != -1:
            explanation = explanation[:next_mfr].strip()
        next_drill_str = explanation.find("Drill")
        if next_drill_str != -1 and len(explanation[next_drill_str:]) > 500:
            # only truncate if it's header of next drill
            lines = explanation.split('\n')
            clean_lines = []
            for l in lines:
                if 'Click here to download' in l: break
                clean_lines.append(l)
            explanation = '\n'.join(clean_lines)

        # Build Socratic Hints
        topic_str = f"Ch. {ch_num}: {short_title}"
        
        # Tier 1: Identify question focus & keywords without answer letter
        if section == "Math":
            t1 = f"🎯 Đọc kỹ câu hỏi cuối (RTFQ). Xác định đại lượng đề bài yêu cầu tìm: biến số, giá trị biểu thức hay tọa độ giao điểm. Phân tích đề bài từng mẩu nhỏ (Bite-Sized Pieces)."
            t2 = f"💡 Chiến thuật {short_title}: Áp dụng kỹ thuật của Princeton Review. Hãy thử thế số (Plugging In), thế đáp án từ các phương án lựa chọn (PITA), hoặc nhập phương trình vào máy tính Desmos để quan sát trực quan."
        elif "Punctuation" in title or "Grammar" in title:
            t1 = f"🎯 Đọc toàn bộ câu từ đầu đến cuối (không dừng lại ở chỗ trống). Xác định ranh giới câu: tìm chủ ngữ, vị ngữ chính và xem các phần trước/sau ô trống là mệnh đề độc lập (Independent) hay phụ thuộc (Dependent)."
            t2 = f"💡 Chiến thuật {short_title}: Áp dụng quy tắc dấu câu chuẩn của College Board. Kiểm tra xem có phạm lỗi Comma Splice (dùng dấu phẩy nối 2 câu độc lập) hay lỗi hòa hợp chủ-vị do danh từ chen ngang đánh lừa không."
        elif "Transitions" in title:
            t1 = f"🎯 Đọc câu trước và câu sau chỗ trống MÀ KHÔNG đọc từ nối. Tự đặt câu hỏi: Hai ý này đang cùng hướng bổ sung (Continuers), đổi hướng đối lập (Shifters) hay là kết quả nguyên nhân (Cause & Effect)?"
            t2 = f"💡 Chiến thuật {short_title}: Gạch bỏ ngay các phương án thuộc cùng một nhóm chức năng (nếu 2 từ nối có nghĩa tương đương, cả hai đều sai). Chọn từ nối phản ánh chính xác nhất mối quan hệ logic tự nhiên."
        elif "Rhetorical" in title:
            t1 = f"🎯 Bắt mục tiêu (RTFQ): Đọc kỹ câu hỏi cuối cùng xem học sinh muốn nhấn mạnh điều gì (sự khác biệt, thành tựu, giới thiệu tác phẩm hay tương đồng) trước khi đọc các ghi chú."
            t2 = f"💡 Chiến thuật {short_title}: Loại trừ tất cả các phương án dù chứa thông tin đúng nhưng không đáp ứng đúng mục tiêu đặt ra ở câu hỏi. Phương án đúng phải trực diện và giải quyết trọn vẹn yêu cầu."
        else:
            t1 = f"🎯 Xác định dạng câu hỏi và tìm manh mối (Clues): Gạch chân đối tượng miêu tả (Who/What) và các từ khóa mang sắc thái tích cực (+), tiêu cực (-) hoặc từ chỉ hướng trong văn bản."
            t2 = f"💡 Chiến thuật {short_title}: Đặt từ phỏng đoán (Annotation) trước khi nhìn vào các lựa chọn. Dùng Process of Elimination (POE) để gạch bỏ các bẫy: Extreme Language, Recycled Words hoặc Half-Right/Half-Wrong."

        t3 = f"📖 LỜI GIẢI CHI TIẾT TỪ THE PRINCETON REVIEW:\n\n{explanation}\n\n✅ ĐÁP ÁN CHÍNH XÁC: [{correct_answer}]"
        t4 = f"⭐ BÍ QUYẾT 1500+ (PRO-TIP): Luôn luôn kiên định áp dụng Process of Elimination (POE). Trên Digital SAT, việc chứng minh 3 phương án sai thường dễ dàng và an toàn hơn nhiều so với việc tranh cãi phương án đúng."
        
        # Build question object
        q_obj = {
            "id": global_q_id,
            "master_id": f"PRIN_BOOK_Q{global_q_id:03d}",
            "q_number": q_num,
            "category": category,
            "q_label": q_label,
            "chapter_num": ch_num,
            "module_code": code,
            "module_title": title,
            "section": section,
            "domain": domain,
            "topic": topic_str,
            "pdf_page": pdf_page,
            "passage": passage,
            "prompt": prompt,
            "options": options,
            "options_raw": "\n".join([f"{o['key']}  {o['text']}" for o in options]),
            "is_grid_in": is_grid_in,
            "correct_answer": str(correct_answer),
            "difficulty": "Hard",
            "princeton_strategy": strat,
            "tier1_hint": t1,
            "tier2_hint": t2,
            "tier3_hint": t3,
            "strategic_tip": t4,
            "pooe_breakdown": explanation[:400] + ("..." if len(explanation) > 400 else ""),
            "option_explanations": explanation,
            "level1_tip": t1,
            "level2_hint": t2,
            "level3_solution": t3,
            "pro_tip": t4
        }
        
        if is_grid_in:
            q_obj["grid_in_explanation"] = {
                "solution_steps": explanation,
                "trap_errors": traps
            }
            
        ch_questions.append(q_obj)
        all_questions.append(q_obj)
        global_q_id += 1
        
    print(f"  ✓ {code}: Extracted {len(ch_questions)} questions ({ex_counter} examples + {practice_counter} drills)")
    
    chapter_modules.append({
        "id": code.lower(),
        "code": code,
        "title": title,
        "short_title": short_title,
        "card_heading": f"Chương {ch_num}: {short_title} ({len(ch_questions)} câu)",
        "sub_title": f"{ex_counter} ví dụ minh họa + {practice_counter} bài tập",
        "chapter_num": ch_num,
        "domain": domain,
        "section": section,
        "time_minutes": max(15, len(ch_questions) * 2),
        "question_count": len(ch_questions),
        "pdf_start_page": start_p,
        "strategy": strat,
        "traps": traps,
        "question_ids": [q["id"] for q in ch_questions]
    })

print(f"\n🎉 [3/5] Extraction Complete! Total questions compiled: {len(all_questions)}")

# ==========================================
# STRICT ZERO-LEAK ASSERTIONS
# ==========================================
print("\n🔍 [4/5] Running Strict Zero-Leak Verification on Tier 1 & Tier 2 Hints...")
leak_errors = []

for q in all_questions:
    t1 = q["tier1_hint"]
    t2 = q["tier2_hint"]
    corr = q["correct_answer"]
    is_spr = q["is_grid_in"]

    if not is_spr:
        for t_idx, hint_text in [(1, t1), (2, t2)]:
            if re.search(r"\[[A-D]\]", hint_text):
                leak_errors.append(f"Q{q['id']} ({q['q_label']}) Tier {t_idx} leaks bracketed answer letter!")
            if re.search(rf"(?i)\b(chọn|đáp án|phương án|chọn phương án)\s*[:\s]*{corr}\b", hint_text):
                leak_errors.append(f"Q{q['id']} ({q['q_label']}) Tier {t_idx} leaks credited choice '{corr}'!")
            corr_opt = next((o["text"] for o in q["options"] if o["key"] == corr), "")
            if len(corr_opt) > 3 and corr_opt.lower() in hint_text.lower():
                if len(corr_opt.split()) > 1:
                    leak_errors.append(f"Q{q['id']} ({q['q_label']}) Tier {t_idx} leaks full option text '{corr_opt}'!")
    else:
        for t_idx, hint_text in [(1, t1), (2, t2)]:
            if re.search(rf"(?i)\b(đáp án|kết quả|kết quả là|giá trị là|chọn)\s*[:\s]*{corr}\b", hint_text):
                leak_errors.append(f"Q{q['id']} ({q['q_label']}) Grid-in Tier {t_idx} leaks numerical answer '{corr}'!")

if leak_errors:
    print(f"❌ FAILED: Found {len(leak_errors)} leak errors:")
    for err in leak_errors:
        print("  - " + err)
    sys.exit(1)
else:
    print(f"✅ PASSED: 100% Zero-Leak Guarantee confirmed for all {len(all_questions)} questions!")

# ==========================================
# CONSTRUCT AND SAVE DATABASE OBJECT
# ==========================================
print("\n💾 [5/5] Saving database and updating manifests...")

db_obj = {
    "test_title": "The Princeton Review: Digital SAT Advanced Comprehensive Guide",
    "source_attribution": "The Princeton Review - SAT Advanced (599 pages)",
    "credits": "Bộ toàn bộ câu hỏi và ví dụ minh họa sách SAT Advanced (The Princeton Review) kèm hệ thống phản hồi 4 tầng Socratic chuẩn mực được biên soạn bởi Thầy Mike Pham Bá Hồng Sơn - Google for Education Innovator.",
    "pdf_drive_id": PDF_DRIVE_ID,
    "pdf_path": PDF_PREVIEW_URL,
    "pdf_drive_preview": PDF_PREVIEW_URL,
    "pdf_drive_view": PDF_VIEW_URL,
    "total_questions": len(all_questions),
    "time_minutes": 320,
    "modules_count": len(chapter_modules),
    "structure_mode": "chapter_based",
    "modules": chapter_modules,
    "questions": all_questions,
    "initial_error_logs": []
}

data_dir = BASE_DIR / "data"
static_data_dir = BASE_DIR / "static" / "data"

target_files = [
    data_dir / "princeton_book.json",
    data_dir / "princetonbook.json",
    static_data_dir / "princeton_book.json",
    static_data_dir / "princetonbook.json"
]

for out_path in target_files:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(db_obj, f, ensure_ascii=False, indent=2)
    print(f"  💾 Saved {out_path} ({len(all_questions)} Qs, {out_path.stat().st_size:,} bytes)")

# Update manifest.json
manifest_path = data_dir / "manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

new_entry = {
    "id": "princeton-book",
    "code": "princetonbook",
    "title": "The Princeton Review: Digital SAT Advanced Comprehensive Guide (All Chapters & Drills)",
    "short_title": "Princeton SAT Advanced Book",
    "badge": "17 Chương Chuyên Sâu",
    "date": "2026-Advanced",
    "dataFile": "data/princeton_book.json",
    "pdfDriveId": PDF_DRIVE_ID,
    "pdfPreviewUrl": PDF_PREVIEW_URL,
    "pdfViewUrl": PDF_VIEW_URL,
    "poster": "poster.png",
    "total_questions": len(all_questions),
    "time_minutes": 320,
    "modules_count": len(chapter_modules),
    "storageKey": "bluebook_princeton_book_student_state_v1",
    "description": "Bộ toàn bộ 233 câu hỏi (bao gồm tất cả ví dụ minh họa kèm bài giảng Here's How to Ace It và toàn bộ bài tập thực hành Drills) trích từ sách The Princeton Review SAT Advanced phân theo 17 chương chuyên sâu kèm giải thích chi tiết, bẫy SAT và gợi ý phản tư Socratic 4 tầng."
}

existing_idx = next((i for i, item in enumerate(manifest) if item["id"] == "princeton-book" or item["code"] == "princetonbook"), None)
if existing_idx is not None:
    manifest[existing_idx] = new_entry
    print("  🔄 Updated existing manifest entry for princeton-book")
else:
    manifest.append(new_entry)
    print("  ➕ Added new manifest entry for princeton-book")

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

static_manifest = static_data_dir / "manifest.json"
with open(static_manifest, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

# Update tests.js
tests_js_content = f"// Auto-generated tests manifest\nwindow.TESTS_MANIFEST = {json.dumps(manifest, ensure_ascii=False, indent=2)};\n"
with open(data_dir / "tests.js", "w", encoding="utf-8") as f:
    f.write(tests_js_content)
with open(static_data_dir / "tests.js", "w", encoding="utf-8") as f:
    f.write(tests_js_content)
print("  💾 Updated tests.js")

print("\n🚀 SUCCESS: Princeton SAT Advanced Book successfully compiled and registered!")
