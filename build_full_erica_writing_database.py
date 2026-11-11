#!/usr/bin/env python3
"""Build the complete Digital SAT Writing/Grammar dataset from Erica Meltzer 6th Edition.

Combines the instructor Excel template (`Edited Template - Full Erica Meltzer SAT Writing.xlsx`
via `excel_writing_dump.json`) with missing worked examples, exercises, page mappings, and
official Answer Key explanations verified against:
`Book - Erica Lynn Meltzer - 6th Grammar Digital SAT.pdf` (PDF pages 1..218; book_page = pdf_page - 2).

Guarantees:
- All 62 worked examples + 272 practice questions = 334 total questions across 17 TOC modules.
- Exact `pdf_page` (1..218) and `book_page` (`pdf_page - 2`) on every question.
- Strict zero-leak check so `tier1_hint` and `tier2_hint` never reveal `correct_answer`.
"""

import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT_DIR / "data"
STATIC_DATA_DIR = ROOT_DIR / "static" / "data"
SCRATCH_DIR = Path(
    "/Users/mike/.gemini/antigravity/brain/752cbd7d-b8fe-4bab-b7a2-71473c95bb69/scratch"
)
EXCEL_DUMP_PATH = SCRATCH_DIR / "excel_writing_dump.json"
OCR_PAGES_PATH = SCRATCH_DIR / "erica_grammar_ocr_pages.json"

PDF_DRIVE_ID = "1RRTBIfpSDD6AyaPJNmfK54fyoXmvNu-s"
PDF_PREVIEW = f"https://drive.google.com/file/d/{PDF_DRIVE_ID}/preview"
PDF_VIEW = f"https://drive.google.com/file/d/{PDF_DRIVE_ID}/view"

# Ordered 17 TOC modules matching Book - Erica Lynn Meltzer - 6th Grammar Digital SAT.pdf
MODULES_META = [
    {
        "id": "ew_ch1",
        "code": "Ch1_Transitions",
        "chapter_num": 1,
        "card_heading": "Chương 1: Transitions (Từ Nối Logic)",
        "btn_label": "Luyện Tập Chương 1 ➔",
        "title": "Chương 1: Transitions (Từ Nối Logic Giữa Các Câu)",
        "short_title": "Chương 1: Transitions",
        "sub_title": "Expression of Ideas",
        "domain": "Expression of Ideas",
        "section": "Reading and Writing",
        "time_minutes": 25,
        "pdf_start_page": 13,
        "pdf_end_page": 28,
        "strategy": "• Gạch bỏ tạm từ nối, đọc trọn hai câu liền kề để xác định quan hệ: Tiếp nối (Continuer), Nguyên nhân–Kết quả (Cause-and-Effect), hay Tương phản (Contradictor). Chú ý 'However' kẹp giữa câu vẫn nối với câu liền trước.",
        "traps": "• Hai đáp án cùng nghĩa trong 1 nhóm logic (ví dụ However & Nevertheless) sẽ tự triệt tiêu nhau • Nhầm 'Actually/In fact' nhấn mạnh thành đối lập.",
    },
    {
        "id": "ew_ch2",
        "code": "Ch2_StudentNotes",
        "chapter_num": 2,
        "card_heading": 'Chương 2: Specific Focus ("Student Notes")',
        "btn_label": "Luyện Tập Chương 2 ➔",
        "title": 'Chương 2: Specific Focus ("Student Notes" / Tổng Hợp Ghi Chú)',
        "short_title": "Chương 2: Student Notes",
        "sub_title": "Rhetorical Synthesis",
        "domain": "Expression of Ideas",
        "section": "Reading and Writing",
        "time_minutes": 12,
        "pdf_start_page": 29,
        "pdf_end_page": 38,
        "strategy": "• Khoanh tròn cụm từ khóa sau động từ mục tiêu ('emphasize...', 'present a similarity...', 'unfamiliar audience...'). Quét 4 đáp án tìm phương án khớp chính xác mục tiêu trước khi đọc kỹ bullet notes.",
        "traps": "• Chọn câu hoàn toàn đúng sự thật theo Notes nhưng lệch khỏi yêu cầu trọng tâm của đề bài • Thiếu thông tin nền (background) khi đề yêu cầu viết cho 'unfamiliar audience'.",
    },
    {
        "id": "ew_pos",
        "code": "PartsOfSpeech_Intro",
        "chapter_num": None,
        "card_heading": "Nền tảng: Parts of Speech (Từ Loại)",
        "btn_label": "Luyện Tập Parts of Speech ➔",
        "title": "Nền tảng Ngữ pháp: Identifying Parts of Speech (Nhận Diện Từ Loại)",
        "short_title": "Nền tảng: Parts of Speech",
        "sub_title": "Grammar Foundations",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 10,
        "pdf_start_page": 41,
        "pdf_end_page": 46,
        "strategy": "• Nhận diện nhanh 8 từ loại cốt lõi (Verb, Noun, Pronoun, Adjective, Adverb, Preposition, Conjunction) bằng vị trí cú pháp thay vì cảm tính dịch nghĩa.",
        "traps": "• Nhầm động từ chia thì với danh động từ (gerund) hoặc phân từ • Nhầm liên từ đẳng lập/phụ thuộc (although, but, because) với trạng từ liên kết (however).",
    },
    {
        "id": "ew_ch3",
        "code": "Ch3_SentencesFragments",
        "chapter_num": 3,
        "card_heading": "Chương 3: Sentences & Fragments",
        "btn_label": "Luyện Tập Chương 3 ➔",
        "title": "Chương 3: Sentences and Fragments (Câu Hoàn Chỉnh & Mảnh Câu)",
        "short_title": "Chương 3: Sentences & Fragments",
        "sub_title": "Independent vs. Dependent Clauses",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 25,
        "pdf_start_page": 47,
        "pdf_end_page": 60,
        "strategy": "• Một câu độc lập bắt buộc phải có Chủ ngữ (Subject) và Động từ chính chia thì (Main Verb), đồng thời không mở đầu bằng từ phụ thuộc (Although, Because, Which, Who...). Đừng phán đoán câu dựa vào độ dài hay việc 'có hiểu nghĩa đứng một mình hay không'.",
        "traps": "• Nhầm V-ing (having, using, considering) là động từ chia thì • Nhầm mệnh đề mở đầu bằng 'Which/Whom/When/Although' là câu hoàn chỉnh • Dùng thừa liên từ nối ('Although..., but...').",
    },
    {
        "id": "ew_ch4",
        "code": "Ch4_JoiningSeparating",
        "chapter_num": 4,
        "card_heading": "Chương 4: Joining & Separating Sentences",
        "btn_label": "Luyện Tập Chương 4 ➔",
        "title": "Chương 4: Joining and Separating Sentences (Ghép & Tách Câu)",
        "short_title": "Chương 4: Joining & Separating",
        "sub_title": "Periods, Semicolons, Colons & FANBOYS",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 25,
        "pdf_start_page": 61,
        "pdf_end_page": 73,
        "strategy": "• Áp dụng 5 cách ghép hai Independent Clauses hợp lệ: Period (.), Semicolon (;), Comma + FANBOYS (, and/but/so...), Colon (:), Dash (—). Nhớ quy tắc 'Period = Semicolon = Comma + FANBOYS': nếu 2 đáp án có cấu trúc này giống hệt nhau thì CẢ HAI đều sai.",
        "traps": "• Lỗi Comma Splice (dùng dấu phẩy nối 2 câu độc lập, đặc biệt trước đại từ he/she/it/they hoặc trước trạng từ however/therefore) • Dùng dấu hai chấm (:) hoặc chấm phẩy (;) sai quy tắc mệnh đề đứng trước.",
    },
    {
        "id": "ew_ch5",
        "code": "Ch5_JoiningClauses",
        "chapter_num": 5,
        "card_heading": "Chương 5: Joining Sentences & Fragments",
        "btn_label": "Luyện Tập Chương 5 ➔",
        "title": "Chương 5: Joining Sentences and Fragments (Ghép Câu & Mệnh Đề Phụ)",
        "short_title": "Chương 5: Sentences & Clauses",
        "sub_title": "Double Conjunctions & Subordinate Clauses",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 20,
        "pdf_start_page": 74,
        "pdf_end_page": 82,
        "strategy": "• Luôn đọc lùi về ĐẦU câu và kéo hết CUỐI câu để phát hiện Subordinating Conjunction ('Although/Because...') hoặc FANBOYS ('but/and/yet...') đứng trước/sau chỗ trống. Dấu hai chấm (:) và dấu gạch ngang đơn (—) theo sau một Câu Độc Lập có thể dẫn vào danh sách hoặc mảnh câu giải thích.",
        "traps": "• Bẫy Song liên từ (Double Conjunction: 'Although ..., but ...') • Đặt dấu chấm (.) hoặc chấm phẩy (;) trước mảnh câu mở đầu bằng V-ing hoặc 'which'.",
    },
    {
        "id": "ew_ch6",
        "code": "Ch6_NonEssentialClauses",
        "chapter_num": 6,
        "card_heading": "Chương 6: Non-Essential & Essential Clauses",
        "btn_label": "Luyện Tập Chương 6 ➔",
        "title": "Chương 6: Non-Essential & Essential Clauses (Mệnh Đề Phụ & Chính)",
        "short_title": "Chương 6: Non-Essential Clauses",
        "sub_title": "Commas, Dashes, Parentheses, Names & 'That/Which'",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 40,
        "pdf_start_page": 83,
        "pdf_end_page": 107,
        "strategy": "• Kiểm tra 'Cross-out Test': gạch bỏ cụm đứng giữa hoặc cụm kẹp 2 dấu câu; nếu phần còn lại vẫn đủ S+V và giữ trọn nghĩa logic thì cụm đó là Non-Essential (phải kẹp CẶP dấu giống nhau: 2 phẩy, 2 gạch ngang, hoặc 2 ngoặc đơn). Với tên riêng/chức danh giữa câu: có nghĩa rõ khi bỏ -> 2 phẩy; mất nghĩa định danh -> KHÔNG dấu phẩy.",
        "traps": "• Trộn dấu (, ... —) hoặc (( ... ,) cho cùng 1 cụm xen giữa • Đặt 1 dấu phẩy đơn lẻ trước/sau tên riêng không cần thiết • Đặt dấu phẩy trước 'that'.",
    },
    {
        "id": "ew_ch7",
        "code": "Ch7_CommaUsesMisuses",
        "chapter_num": 7,
        "card_heading": "Chương 7: Additional Comma Uses & Misuses",
        "btn_label": "Luyện Tập Chương 7 ➔",
        "title": "Chương 7: Additional Comma Uses and Misuses (Các Quy Tắc Dấu Phẩy)",
        "short_title": "Chương 7: Comma Uses & Misuses",
        "sub_title": "Comma Rules & Forbidden Commas",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 10,
        "pdf_start_page": 108,
        "pdf_end_page": 114,
        "strategy": "• Nắm vững 4 vị trí CẤM đặt dấu phẩy đơn lẻ: giữa Chủ ngữ và Động từ, trước/sau Giới từ (of/for/by/with/in...), giữa 2 Tính từ/Danh từ nối bằng 'and/or', và trước 'that'. Dùng dấu phẩy phân cách chuỗi 3+ mục song song hoặc hai tính từ đồng đẳng (chèn được 'and').",
        "traps": "• Đặt dấu phẩy nghỉ hơi tự nhiên sau chủ ngữ dài hoặc trước cụm giới từ • Nhầm tính từ bổ nghĩa tích lũy (cumulative adjectives) với đồng đẳng.",
    },
    {
        "id": "ew_cr1",
        "code": "Cumulative_Review_1",
        "chapter_num": None,
        "card_heading": "Cumulative Review 1 (Chapters 1–7)",
        "btn_label": "Luyện Tập Tổng Hợp 1 ➔",
        "title": "Cumulative Review 1: Punctuation, Sentence Structure & Transitions (Ch. 1–7)",
        "short_title": "Cumulative Review 1 (Ch. 1–7)",
        "sub_title": "Comprehensive Review Ch. 1–7",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 25,
        "pdf_start_page": 115,
        "pdf_end_page": 120,
        "strategy": "• Phối hợp linh hoạt phân tích ranh giới mệnh đề (Ch. 3–5), cặp dấu Non-Essential (Ch. 6), vị trí cấm phẩy (Ch. 7) và logic từ nối (Ch. 1) trong cùng một bài ôn tập tổng hợp.",
        "traps": "• Bỏ qua từ nối đầu câu khi chọn dấu câu ở cuối cụm trạng ngữ • Nhầm lẫn ranh giới mệnh đề với bổ ngữ xen giữa.",
    },
    {
        "id": "ew_ch8",
        "code": "Ch8_VerbsAgreementTense",
        "chapter_num": 8,
        "card_heading": "Chương 8: Verbs — Agreement & Tense",
        "btn_label": "Luyện Tập Chương 8 ➔",
        "title": "Chương 8: Verbs: Subject-Verb Agreement & Tense (Hòa Hợp Chủ-Vị & Thì)",
        "short_title": "Chương 8: Verbs & Tense",
        "sub_title": "SVA, Tense Sequences, Passive & To vs. -ING",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 30,
        "pdf_start_page": 123,
        "pdf_end_page": 144,
        "strategy": "• Khi 4 đáp án có cả động từ chia Số Ít (-s/has/is/was) và Số Nhiều (nguyên mẫu/have/are/were): gạch bỏ cụm giới từ (of/in/by...) và mệnh đề xen giữa để tìm Chủ ngữ gốc ở đầu câu. Nếu cùng số -> xét mốc thời gian ('by the time' -> had + V3; năm quá khứ trước năm mốc -> would/V2) và Gerund vs Infinitive.",
        "traps": "• Chia động từ theo danh từ đứng ngay sát chỗ trống bên trong cụm giới từ • Nhầm Subject-Verb Agreement ngụy trang thành câu hỏi Thì (tense distraction) • Dùng V-ing khi câu cần động từ chính chia thì.",
    },
    {
        "id": "ew_ch9",
        "code": "Ch9_Pronouns",
        "chapter_num": 9,
        "card_heading": "Chương 9: Pronouns (Đại Từ & Sở Hữu)",
        "btn_label": "Luyện Tập Chương 9 ➔",
        "title": "Chương 9: Pronouns (Hòa Hợp Đại Từ & Tính Minh Bạch)",
        "short_title": "Chương 9: Pronouns",
        "sub_title": "Antecedent Agreement, Case & Clarity",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 18,
        "pdf_start_page": 145,
        "pdf_end_page": 156,
        "strategy": "• Truy ngược tìm Danh từ tiền vị (Antecedent) chính xác về Số Ít/Số Nhiều. Khi đại từ đứng một mình ('it/this/that/they') gây mơ hồ về đối tượng quy chiếu, luôn ưu tiên đáp án lặp lại Danh từ cụ thể ('Noun > Pronoun'). Giữ nhất quán cặp đại từ phiếm chỉ ('one -> one's').",
        "traps": "• Dùng đại từ số nhiều 'they/them' thay thế danh từ số ít không xác định giới tính hoặc ngược lại • Bị đánh lừa bởi 'it/this' mơ hồ không rõ quy chiếu.",
    },
    {
        "id": "ew_ch10",
        "code": "Ch10_Apostrophes",
        "chapter_num": 10,
        "card_heading": "Chương 10: Apostrophes (Dấu Nháy Đơn)",
        "btn_label": "Luyện Tập Chương 10 ➔",
        "title": "Chương 10: Apostrophes (Sở Hữu Cách Danh Từ & Đại Từ)",
        "short_title": "Chương 10: Apostrophes",
        "sub_title": "Possessive Nouns & Contractions",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 12,
        "pdf_start_page": 157,
        "pdf_end_page": 163,
        "strategy": "• Quy tắc Danh từ: Số nhiều không cần sở hữu -> s; Sở hữu 1 đối tượng -> 's; Sở hữu nhiều đối tượng (sẵn -s) -> s'. Quy tắc Đại từ (its/their/whose vs it's/they're/who's): thay thử 'it is', 'they are', 'who is' vào câu; nếu vô nghĩa -> BỎ dấu nháy đơn!",
        "traps": "• Dạng sai 'its'' (không bao giờ tồn tại trong tiếng Anh chuẩn) • Dùng sai contraction ('they're / it's') trước danh từ.",
    },
    {
        "id": "ew_ch11",
        "code": "Ch11_Modification",
        "chapter_num": 11,
        "card_heading": "Chương 11: Modification (Bổ Ngữ Lơ Lửng)",
        "btn_label": "Luyện Tập Chương 11 ➔",
        "title": "Chương 11: Modification (Dangling & Misplaced Modifiers)",
        "short_title": "Chương 11: Modification",
        "sub_title": "Dangling & Misplaced Modifiers",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 15,
        "pdf_start_page": 164,
        "pdf_end_page": 170,
        "strategy": "• Khi câu mở đầu bằng cụm mô tả đứng trước dấu phẩy ('Born in...', 'One of the greatest...', 'Used to...'), Chủ ngữ đứng NGAY SAU dấu phẩy bắt buộc phải là đối tượng được cụm đó mô tả (chủ thể thực hiện/sở hữu đặc điểm). Không được dùng dạng sở hữu ('Clara Wieck's studies') thay cho chính chủ thể ('Clara Wieck').",
        "traps": "• Đặt chủ ngữ bị động hoặc sở hữu cách (e.g., '...studies', 'more than 50 miles...') ngay sau dấu phẩy cụm mở đầu • Đặt cụm trạng ngữ xen giữa làm sai lệch nghĩa bổ nghĩa.",
    },
    {
        "id": "ew_ch12",
        "code": "Ch12_ParallelStructure",
        "chapter_num": 12,
        "card_heading": "Chương 12: Parallel Structure (Cấu Trúc Song Song)",
        "btn_label": "Luyện Tập Chương 12 ➔",
        "title": "Chương 12: Parallel Structure (Cấu Trúc Song Song & Liệt Kê)",
        "short_title": "Chương 12: Parallel Structure",
        "sub_title": "Lists, Correlative Pairs & Comparisons",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 15,
        "pdf_start_page": 171,
        "pdf_end_page": 175,
        "strategy": "• Mọi thành phần trong danh sách (A, B, and C) hoặc đi theo cặp liên từ ('not only... but also', 'rather than', 'so... that') phải cùng dạng từ loại/cụm từ (cùng V nguyên mẫu, cùng danh từ, hoặc cùng mệnh đề). Dấu ngăn cách trong danh sách phải đồng bộ hoàn toàn (toàn phẩy hoặc toàn chấm phẩy nếu bên trong mục đã chứa phẩy).",
        "traps": "• Xen câu độc lập hoặc dạng -ing/to-V lạc tông vào chuỗi động từ nguyên mẫu • Trộn dấu phẩy và dấu chấm phẩy trong cùng một danh sách.",
    },
    {
        "id": "ew_cr2",
        "code": "Cumulative_Review_2",
        "chapter_num": None,
        "card_heading": "Cumulative Review 2 (Chapters 8–12)",
        "btn_label": "Luyện Tập Tổng Hợp 2 ➔",
        "title": "Cumulative Review 2: Verbs, Pronouns, Apostrophes, Modifiers & Parallelism (Ch. 8–12)",
        "short_title": "Cumulative Review 2 (Ch. 8–12)",
        "sub_title": "Comprehensive Review Ch. 8–12",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 20,
        "pdf_start_page": 176,
        "pdf_end_page": 179,
        "strategy": "• Luyện tổng hợp toàn bộ Phần Ngữ pháp (Ch. 8–12): phát hiện ngay câu đang kiểm tra Hòa hợp Chủ-Vị, Thì động từ, Đại từ, Bổ ngữ lơ lửng hay Cấu trúc song song từ dấu hiệu đáp án.",
        "traps": "• Đọc lướt thiếu bước xác định loại lỗi chính của câu dẫn đến bẫy SVA giả thì hoặc bẫy Dangling Modifier.",
    },
    {
        "id": "ew_sets",
        "code": "Practice_Sets_All",
        "chapter_num": None,
        "card_heading": "Practice Sets 1–5 (50 Câu Thực Chiến)",
        "btn_label": "Luyện Tập 5 Practice Sets ➔",
        "title": "Practice Sets 1–5: All Chapters Combined (50 Câu Thực Chiến Chuẩn Bluebook)",
        "short_title": "Practice Sets 1–5 (50 Câu)",
        "sub_title": "Mixed Full-Format Sets (Ch. 1–12)",
        "domain": "Reading and Writing",
        "section": "Reading and Writing",
        "time_minutes": 45,
        "pdf_start_page": 180,
        "pdf_end_page": 194,
        "strategy": "• 5 đề thực chiến (mỗi Set 10 câu) trộn đều Transitions, Rhetorical Synthesis, Punctuation và Grammar đúng cấu trúc bài thi Digital SAT chính thức, kèm phân tích chuẩn từ Answer Key chính thức của Erica Meltzer (Sách trang 206–213).",
        "traps": "• Rút ngắn phạm vi đọc — hãy luôn đọc trọn từ đầu câu chứa chỗ trống đến dấu chấm kết thúc câu và nhận diện dạng câu hỏi từ 4 đáp án.",
    },
    {
        "id": "ew_app",
        "code": "Appendix_QuestionMarks",
        "chapter_num": None,
        "card_heading": "Appendix: Word Pairs, Comparisons & Question Marks",
        "btn_label": "Luyện Tập Phụ Lục ➔",
        "title": "Appendix: Word Pairs, Comparisons & Question Marks (Cặp Từ & Dấu Chấm Hỏi)",
        "short_title": "Appendix: Question Marks",
        "sub_title": "Indirect vs. Direct Questions",
        "domain": "Standard English Conventions",
        "section": "Reading and Writing",
        "time_minutes": 5,
        "pdf_start_page": 195,
        "pdf_end_page": 202,
        "strategy": "• Phân biệt Câu hỏi trực tiếp (Direct Question -> kết thúc bằng '?') và Câu hỏi gián tiếp lồng trong câu trần thuật (Indirect Question mở đầu bằng 'whether / if / how / why' -> giữ trật tự Chủ ngữ + Động từ và kết thúc bằng dấu chấm '.').",
        "traps": "• Đặt dấu hỏi chấm '?' sau mệnh đề tường thuật gián tiếp bắt đầu bằng 'speculate about whether...' hoặc đảo trợ động từ lên trước chủ ngữ ('can bees' thay vì 'bees can').",
    },
]

# Missing items & verified overrides (each entry specifies exact field values from PDF & Answer Key)
# Page numbers are PDF pages (1..218); book_page is always computed as pdf_page - 2.
CH1_MISSING_EXAMPLES = [
    {
        "q_number": 6,
        "q_label": "Ch.1 - Ví dụ 6",
        "category": "example",
        "pdf_page": 19,
        "topic": "Ch. 1: Transitions • Mid/End-Sentence Contradictors",
        "passage": "Healthy arctic marine mammals have a thick layer of fat beneath their skin, allowing them to dwell in the frigid waters surrounding the Earth's poles. Tropical marine mammals have few fat reserves in their bodies, ______ As a result, they are largely confined to the warm waters that surround coral reefs.",
        "prompt": "Which choice completes the text with the most logical transition?",
        "options": [
            ("A", "therefore,"),
            ("B", "however,"),
            ("C", "moreover,"),
            ("D", "in fact,"),
        ],
        "correct_answer": "B",
        "l1_rule": "Xác định xem từ nối đặt sau một câu hoàn chỉnh (trước câu 'As a result...') đang nối câu chứa nó với câu liền trước hay câu liền sau.",
        "l2_rule": "Dù từ nối nằm ở cuối câu thứ 2 sát ngay chữ 'As a result', nhiệm vụ của nó là liên kết Câu 2 ('few fat reserves') với Câu 1 ('thick layer of fat'). Hai câu mang ý tương phản hoàn toàn.",
        "explanation": "Đáp án chính xác là **B** (however,).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 17):**\n• Dù từ nối nằm ngay sát câu *As a result...*, nó nằm TRONG câu nói về loài thú biển nhiệt đới (vế *few fat reserves*) nên vẫn kết nối câu này với câu liền trước về thú biển Bắc Cực (*thick layer of fat*).\n• Hai ý đối lập nhau nên cần từ nối tương phản (*contradictor*). Các đáp án A (*therefore*), C (*moreover*), D (*in fact*) đều là từ tiếp nối/kết quả (*continuers*).",
    },
    {
        "q_number": 7,
        "q_label": "Ch.1 - Ví dụ 7",
        "category": "example",
        "pdf_page": 20,
        "topic": "Ch. 1: Transitions • Single-Comma Within-Sentence Transition",
        "passage": "Tropical marine mammals have few fat reserves in their bodies and dwell primarily in the warm waters that surround coral reefs. In contrast, healthy arctic marine mammals have a thick layer of fat beneath their skin, ______ they are able to tolerate much colder waters.",
        "prompt": "Which choice completes the text with the most logical transition?",
        "options": [
            ("A", "so"),
            ("B", "for"),
            ("C", "yet"),
            ("D", "whereas"),
        ],
        "correct_answer": "A",
        "l1_rule": "Chú ý câu chỉ có MỘT dấu phẩy duy nhất trước chỗ trống để nối hai mệnh đề trong cùng một câu, đồng thời xác định chiều Nhân – Quả giữa hai mệnh đề đó.",
        "l2_rule": "Vế 1 là nguyên nhân ('thick layer of fat'), Vế 2 là kết quả ('able to tolerate much colder waters'). Loại các từ tương phản trước rồi xét đúng chiều logic giữa hai từ chỉ Nhân–Quả.",
        "explanation": "Đáp án chính xác là **A** (so).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 18):**\n• Khi từ nối chỉ theo sau MỘT dấu phẩy để nối hai vế trong cùng một câu, ta xét trực tiếp quan hệ giữa hai vế của câu đó: Vế 1 (có lớp mỡ dày) dẫn đến kết quả ở Vế 2 (chịu được nước lạnh).\n• Loại C (*yet*) và D (*whereas*) vì chúng chỉ sự tương phản.\n• *for* khi đứng làm liên từ có nghĩa là *because* (vì) — sẽ làm đảo ngược logic nhân quả (không phải có lớp mỡ dày *vì* chịu được nước lạnh). Chỉ *so* tạo quan hệ nguyên nhân -> kết quả đúng chiều.",
    },
]

CH1_T2_MISSING_1_TO_8 = [
    {
        "q_number": 11,
        "q_label": "Ch.1 (Transitions 2) - Câu 1",
        "pdf_page": 26,
        "topic": "Exercise: Transitions 2 • Specific Illustration",
        "passage": "Rather than embrace the type of abstract work that many artists of her generation preferred, Gwendolyn Knight preferred to depict figures in a spontaneous and personal manner. ______ she painted oil portraits of friends as well as studies of dancers in motion.",
        "options": [("A", "Moreover,"), ("B", "Specifically,"), ("C", "Nevertheless,"), ("D", "Besides,")],
        "correct_answer": "B",
        "l1_rule": "Xác định xem câu thứ hai là một ý bổ sung ngang hàng, ý đối lập, hay ví dụ cụ thể hóa nhận định ở câu thứ nhất.",
        "l2_rule": "Câu 1 nêu xu hướng chung ('depict figures in a spontaneous and personal manner'); câu 2 nêu rõ thể loại cụ thể cô vẽ ('oil portraits of friends as well as studies of dancers').",
        "explanation": "Đáp án **B** (*Specifically,*). Câu sau cụ thể hóa phong cách vẽ hình khối con người (*depict figures*) bằng ví dụ cụ thể (tranh chân dung sơn dầu bạn bè và vũ công chuyển động). Không dùng C (tương phản) hay A/D (thêm ý mới tách biệt).",
    },
    {
        "q_number": 12,
        "q_label": "Ch.1 (Transitions 2) - Câu 2",
        "pdf_page": 26,
        "topic": "Exercise: Transitions 2 • Contradictor vs Continuer (Mid-sentence)",
        "passage": "Discarded electronic devices such as cell phones and tablets are a rapidly growing source of waste. One way to mitigate the problem, ______ could be to include components made with renewable resources.",
        "options": [("A", "therefore,"), ("B", "moreover,"), ("C", "nevertheless,"), ("D", "however,")],
        "correct_answer": "D",
        "l1_rule": "Chú ý từ nối đặt kẹp giữa hai dấu phẩy trong câu thứ hai nối vấn đề nêu ở câu đầu với giải pháp giảm thiểu ở câu thứ hai.",
        "l2_rule": "Câu 1 nêu thực trạng tiêu cực ('growing source of waste'), Câu 2 chuyển hướng sang một giải pháp tích cực ('way to mitigate the problem'). Lưu ý loại hai từ nối cùng nhóm hoặc sai logic hệ quả.",
        "explanation": "Đáp án **D** (*however,* — Sách Answer Key trang 201: `2. D`). Câu 1 nói về sự gia tăng rác thải điện tử, câu 2 đưa ra hướng khắc phục trái ngược với chiều tăng rác thải đó nên cần *however*.",
    },
    {
        "q_number": 13,
        "q_label": "Ch.1 (Transitions 2) - Câu 3",
        "pdf_page": 26,
        "topic": "Exercise: Transitions 2 • Chronological Progression",
        "passage": "While doing fieldwork on Gorgonilla Island in Colombia in 2014, Hermann Bermúdez found spherule deposits—layers of sediment filled with tiny glass beads. These beads formed when the heat and pressure from an asteroid impact melted and scattered the crust of the Earth, ejecting tiny liquid blobs into the atmosphere. ______ they fell back to earth in solid form under the influence of gravity.",
        "options": [("A", "Therefore,"), ("B", "Meanwhile,"), ("C", "Subsequently,"), ("D", "Additionally,")],
        "correct_answer": "C",
        "l1_rule": "Xem xét trình tự diễn biến vật lý giữa việc bắn các giọt lỏng lên khí quyển ở câu trước và việc rơi trở lại mặt đất ở câu sau.",
        "l2_rule": "Hai hành động xảy ra nối tiếp nhau theo thời gian (đầu tiên bắn vào khí quyển -> tiếp sau đó rơi xuống đất), chứ không đồng thời hoặc chỉ là liệt kê thêm ý.",
        "explanation": "Đáp án **C** (*Subsequently,* — 'sau đó'). Theo trình tự thời gian, giọt lỏng bắn vào khí quyển trước rồi *sau đó* rơi xuống đất dưới tác động trọng lực. Loại B (cùng lúc), A (kết quả thuần túy không chính xác bằng trình tự bước tiếp theo), D (bổ sung).",
    },
    {
        "q_number": 14,
        "q_label": "Ch.1 (Transitions 2) - Câu 4",
        "pdf_page": 26,
        "topic": "Exercise: Transitions 2 • Cause-and-Effect",
        "passage": "Blue whales recognize when the wind is changing their habitat and identify places where ocean currents produce large aggregations of krill. The tiny shrimp are the primary food sources for the massive animals, which can weigh 165 tons or more. ______ their ability to locate these dense concentrations of nutrients is a matter of survival.",
        "options": [("A", "Consequently,"), ("B", "For instance,"), ("C", "Furthermore,"), ("D", "Alternatively,")],
        "correct_answer": "A",
        "l1_rule": "Xác định mối liên hệ giữa vai trò 'nguồn thức ăn chính cho động vật nặng 165 tấn' với việc định vị đàn nhuyễn thể là 'vấn đề sinh tồn'.",
        "l2_rule": "Vì nhuyễn thể là nguồn thức ăn chính nuôi cơ thể khổng lồ, HỆ QUẢ tất yếu là khả năng tìm kiếm chúng trở thành điều sống còn.",
        "explanation": "Đáp án **A** (*Consequently,*). Câu cuối nêu kết quả logic trực tiếp từ dữ kiện thức ăn thiết yếu ở câu trước.",
    },
    {
        "q_number": 15,
        "q_label": "Ch.1 (Transitions 2) - Câu 5",
        "pdf_page": 27,
        "topic": "Exercise: Transitions 2 • Contrast Within Timeline",
        "passage": "In 1959, Project Mercury became the first human spaceflight program led by NASA. Aimed at putting an American into orbit before the Soviet Union could accomplish that goal, it was shut down after less than half a decade. ______ in the four years of its existence, seven astronauts were able to travel into space.",
        "options": [("A", "For instance,"), ("B", "Still,"), ("C", "Accordingly,"), ("D", "Indeed,")],
        "correct_answer": "B",
        "l1_rule": "Đối chiếu thông tin câu thứ hai ('bị đóng cửa chỉ sau chưa đầy nửa thập kỷ') với thành tựu ở câu thứ ba ('7 phi hành gia đã bay vào vũ trụ').",
        "l2_rule": "Dù thời gian tồn tại rất ngắn ngủi và bị đóng cửa sớm (ý hạn chế/tiêu cực), chương trình vẫn đưa được 7 phi hành gia lên vũ trụ (ý tích cực). Đây là quan hệ nhượng bộ/tương phản.",
        "explanation": "Đáp án **B** (*Still,* — 'Tuy vậy'). Chương trình bị đóng sớm, *tuy vậy* trong 4 năm ngắn ngủi vẫn đưa được 7 phi hành gia vào vũ trụ.",
    },
    {
        "q_number": 16,
        "q_label": "Ch.1 (Transitions 2) - Câu 6",
        "pdf_page": 27,
        "topic": "Exercise: Transitions 2 • Subordinating Transition (Cause)",
        "passage": "Bacteria have one or many appendages known as a flagellum, which is made of thousands of identical subunits. ______ a tail that was straight or only slightly flexible would leave an organism unable to move, bacteria have evolved rotating, corkscrew-shaped propellers that push them forward. Scientists call the formation of this shape \"supercoiling,\" and now, after more than half a century, they understand how the process works.",
        "options": [("A", "Although"), ("B", "Despite"), ("C", "Because"), ("D", "Unless")],
        "correct_answer": "C",
        "l1_rule": "Kiểm tra quan hệ logic giữa hai mệnh đề trong chính câu có chỗ trống: 'một chiếc đuôi thẳng sẽ khiến vi khuẩn không di chuyển được' vs 'vi khuẩn đã tiến hóa thành cấu trúc xoắn xoay'.",
        "l2_rule": "Vế chứa chỗ trống giải thích LÝ DO khiến vi khuẩn phải tiến hóa cấu trúc xoắn ốc ở vế sau (đồng thời loại bỏ các từ không đi với mệnh đề hoàn chỉnh hoặc mang nghĩa tương phản/điều kiện sai).",
        "explanation": "Đáp án **C** (*Because*). Do chiếc đuôi thẳng khiến sinh vật không thể di chuyển, vi khuẩn đã tiến hóa chân vịt hình nút chai xoay (*cause -> adaptation*). Loại D (*Because* vs *Unless*), A (*Although* ngược nghĩa), B (*Despite* là giới từ không đứng trước mệnh đề).",
    },
    {
        "q_number": 17,
        "q_label": "Ch.1 (Transitions 2) - Câu 7",
        "pdf_page": 27,
        "topic": "Exercise: Transitions 2 • Cause-and-Effect",
        "passage": "Although Shakespeare portrayed King Richard III as a villain, historians argue that he was in fact a far more sympathetic figure. The Tudors, on whose patronage Shakespeare was dependent, had conquered the English throne from Richard. ______ the playwright was obliged to portray the king in an unflattering light.",
        "options": [("A", "Hence,"), ("B", "Still,"), ("C", "In contrast,"), ("D", "Moreover,")],
        "correct_answer": "A",
        "l1_rule": "Tìm mối quan hệ giữa việc Shakespeare lệ thuộc sự bảo trợ của triều Tudor (vốn cướp ngôi của Richard) với việc ông phải khắc họa Richard theo hướng tiêu cực.",
        "l2_rule": "Vì Shakespeare phụ thuộc vào dòng họ Tudor (kẻ thù của Richard), HỆ QUẢ tất yếu là ông buộc phải miêu tả vua Richard một cách bất lợi.",
        "explanation": "Đáp án **A** (*Hence,* — 'Do đó'). B và C đều mang nghĩa tương phản nên loại; D (*Moreover*) chỉ thêm thông tin ngang hàng mà không nêu hệ quả trực tiếp.",
    },
    {
        "q_number": 18,
        "q_label": "Ch.1 (Transitions 2) - Câu 8",
        "pdf_page": 27,
        "topic": "Exercise: Transitions 2 • Concession (Subordinating)",
        "passage": "Trade on the Silk Road was a significant factor in the development of China, India, and Europe, opening long-distance political and economic interactions. ______ silk was certainly the major trade item from China, numerous other types of goods, including textiles, cloth, and pottery, also traveled along the Silk Road.",
        "options": [("A", "Because"), ("B", "Although"), ("C", "Until"), ("D", "When")],
        "correct_answer": "B",
        "l1_rule": "Đối chiếu vế đầu câu cuối ('lụa chắc chắn là mặt hàng chính từ Trung Quốc') với vế sau ('nhiều mặt hàng khác cũng được vận chuyển trên Con đường Tơ lụa').",
        "l2_rule": "Một bên nhấn mạnh vai trò áp đảo của lụa (*certainly the major trade item*), bên còn lại bổ sung sự hiện diện của nhiều mặt hàng khác — đây là quan hệ nhượng bộ (Mặc dù...).",
        "explanation": "Đáp án **B** (*Although*). *Mặc dù* lụa là mặt hàng giao thương chính từ Trung Quốc, nhiều loại hàng hóa khác cũng lưu thông trên tuyến đường này.",
    },
]

# Parts of Speech (PDF P45-46, #1-8) - Balanced A/B/C/D options matching P203 Answer Key
PARTS_OF_SPEECH_ITEMS = [
    {
        "q_number": 1,
        "pdf_page": 45,
        "passage": "Some (A) planets that are very different from our own may have the (B) potential to turn current theories (C) about solar system (D) formation upside down.",
        "options": [
            ("A", "A: verb; B: adjective; C: conjunction; D: noun"),
            ("B", "A: noun; B: adjective; C: preposition; D: verb"),
            ("C", "A: noun; B: noun; C: preposition; D: noun"),
            ("D", "A: adjective; B: noun; C: adverb; D: noun"),
        ],
        "correct_answer": "C",
        "l1_rule": "Xét chức năng ngữ pháp của từng từ (A) sau từ hạn định 'Some', (B) đứng sau mạo từ 'the', (C) đứng trước cụm danh từ 'solar system...', và (D) làm tân ngữ kết thúc cụm giới từ.",
        "l2_rule": "Chú ý từ nào đi sau 'the' thường giữ vai trò gì; từ ngắn như 'about' nối danh từ với phần giải thích phía sau là từ loại nào?",
        "explanation": "Đáp án **C** (`A: noun; B: noun; C: preposition; D: noun` — Answer Key trang 201).\n• (A) *planets* = danh từ (sau *Some*).\n• (B) *potential* = danh từ (sau mạo từ *the*).\n• (C) *about* = giới từ dẫn cụm *about solar system formation*.\n• (D) *formation* = danh từ.",
    },
    {
        "q_number": 2,
        "pdf_page": 45,
        "passage": "Flamingoes (A) are generally viewed as elegant and graceful, (B) but they also exhibit surprisingly (C) rowdy behavior. As a result, (D) they have recently become the subject of serious scientific examination.",
        "options": [
            ("A", "A: noun; B: preposition; C: adverb; D: noun"),
            ("B", "A: verb; B: conjunction; C: adjective; D: pronoun"),
            ("C", "A: verb; B: adverb; C: adjective; D: pronoun"),
            ("D", "A: verb; B: conjunction; C: adverb; D: adjective"),
        ],
        "correct_answer": "B",
        "l1_rule": "Nhận diện trợ động từ 'to be', thành phần thuộc nhóm FANBOYS, từ bổ nghĩa ngay trước danh từ 'behavior', và từ thay thế 'Flamingoes'.",
        "l2_rule": "'but' là liên từ FANBOYS; từ nằm giữa trạng từ 'surprisingly' và danh từ 'behavior' đóng vai trò bổ nghĩa cho danh từ là từ loại gì?",
        "explanation": "Đáp án **B** (`A: verb; B: conjunction; C: adjective; D: pronoun` — Answer Key trang 201).\n• (A) *are* = động từ.\n• (B) *but* = liên từ (FANBOYS).\n• (C) *rowdy* = tính từ bổ nghĩa cho danh từ *behavior*.\n• (D) *they* = đại từ thay cho *Flamingoes*.",
    },
    {
        "q_number": 3,
        "pdf_page": 45,
        "passage": "In response to their critics, (A) advocates of genetically modified foods (B) insist that such crops are beneficial (C) because they grow faster, require fewer pesticides, and reduce (D) stress on natural resources.",
        "options": [
            ("A", "A: noun; B: verb; C: conjunction; D: noun"),
            ("B", "A: verb; B: noun; C: preposition; D: verb"),
            ("C", "A: noun; B: verb; C: preposition; D: adjective"),
            ("D", "A: verb; B: verb; C: conjunction; D: noun"),
        ],
        "correct_answer": "A",
        "l1_rule": "Phân biệt từ có gốc dùng được cho cả danh từ lẫn động từ ở (A) 'advocates of...' và (D) 'reduce stress', dựa vào vị trí Chủ ngữ vs Tân ngữ.",
        "l2_rule": "(A) là chủ ngữ của câu (có 'of...' bổ nghĩa ngay sau -> không phải động từ); (B) là động từ chính nối với 'that...'; (C) đứng trước một mệnh đề hoàn chỉnh S+V; (D) đi sau ngoại động từ 'reduce'.",
        "explanation": "Đáp án **A** (`A: noun; B: verb; C: conjunction; D: noun` — Answer Key trang 201).\n• (A) *advocates* = danh từ số nhiều ('những người ủng hộ').\n• (B) *insist* = động từ chính.\n• (C) *because* = liên từ phụ thuộc.\n• (D) *stress* = danh từ ('áp lực') làm tân ngữ cho *reduce*.",
    },
    {
        "q_number": 4,
        "pdf_page": 45,
        "passage": "The fig tree (A) plays an important role in rain forest (B) ecosystems because (C) it provides food for many different types of animals as well as cloth for local (D) inhabitants.",
        "options": [
            ("A", "A: noun; B: noun; C: noun; D: adjective"),
            ("B", "A: verb; B: adjective; C: pronoun; D: noun"),
            ("C", "A: verb; B: noun; C: preposition; D: verb"),
            ("D", "A: verb; B: noun; C: pronoun; D: noun"),
        ],
        "correct_answer": "D",
        "l1_rule": "Kiểm tra vai trò của (A) sau chủ ngữ 'The fig tree', (B) đứng sau danh từ ghép 'rain forest...', (C) đại diện lại cho 'the fig tree', và (D) sau tính từ 'local'.",
        "l2_rule": "Lưu ý 'local' đứng trước (D) là tính từ, do đó (D) chắc chắn thuộc nhóm từ gì?",
        "explanation": "Đáp án **D** (`A: verb; B: noun; C: pronoun; D: noun` — Answer Key trang 201).\n• (A) *plays* = động từ.\n• (B) *ecosystems* = danh từ.\n• (C) *it* = đại từ thay cho *the fig tree*.\n• (D) *inhabitants* = danh từ (sau tính từ *local*).",
    },
    {
        "q_number": 5,
        "pdf_page": 46,
        "passage": "(A) Although she never (B) obtained any formal academic credentials, the Austrian-born psychoanalyst Melanie Klein (C) became renowned as an (D) innovator for her work with young children.",
        "options": [
            ("A", "A: preposition; B: verb; C: adjective; D: noun"),
            ("B", "A: conjunction; B: verb; C: verb; D: noun"),
            ("C", "A: adverb; B: verb; C: verb; D: adjective"),
            ("D", "A: conjunction; B: adjective; C: verb; D: noun"),
        ],
        "correct_answer": "B",
        "l1_rule": "Phân biệt từ nối mệnh đề phụ thuộc ở đầu câu ('Although') với giới từ, và xác định hai động từ thì quá khứ đơn + danh từ sau mạo từ 'an'.",
        "l2_rule": "'Although' mở đầu cả một mệnh đề đầy đủ S+V ('she never obtained...'); 'obtained' và 'became' chia ở quá khứ đơn; (D) đi sau mạo từ 'an'.",
        "explanation": "Đáp án **B** (`A: conjunction; B: verb; C: verb; D: noun` — Answer Key trang 201).\n• (A) *Although* = liên từ phụ thuộc.\n• (B) *obtained* = động từ.\n• (C) *became* = động từ.\n• (D) *innovator* = danh từ.",
    },
    {
        "q_number": 6,
        "pdf_page": 46,
        "passage": "Edith Kanaka'ole was an (A) internationally acclaimed hula teacher, composer, chanter and performer. (B) Today, she (C) is credited (D) with playing a vital role in passing down the teachings of hula during the Hawaiian Renaissance of the 1970s.",
        "options": [
            ("A", "A: adjective; B: noun; C: verb; D: conjunction"),
            ("B", "A: adverb; B: noun; C: adjective; D: preposition"),
            ("C", "A: adverb; B: adverb; C: verb; D: preposition"),
            ("D", "A: adverb; B: adverb; C: noun; D: preposition"),
        ],
        "correct_answer": "C",
        "l1_rule": "Chú ý từ kết thúc đuôi '-ly' bổ nghĩa cho tính từ/phân từ ('acclaimed'), từ chỉ thời gian đứng độc lập đầu câu ('Today,'), trợ động từ 'is', và từ đi kèm sau 'credited ... playing'.",
        "l2_rule": "(B) 'Today' trả lời cho câu hỏi 'When?' bổ nghĩa cho cả mệnh đề chính -> trạng từ; (D) đứng ngay trước V-ing ('playing').",
        "explanation": "Đáp án **C** (`A: adverb; B: adverb; C: verb; D: preposition` — Answer Key trang 201).\n• (A) *internationally* = trạng từ bổ nghĩa cho *acclaimed*.\n• (B) *Today* = trạng từ chỉ thời gian.\n• (C) *is* = động từ (*is credited*).\n• (D) *with* = giới từ.",
    },
    {
        "q_number": 7,
        "pdf_page": 46,
        "passage": "The importance of neurons in (A) cognition is well documented; (B) however, neurons are interspersed with glial cells, whose role in the cognition (C) process is not well understood (D) by researchers.",
        "options": [
            ("A", "A: noun; B: conjunction/adverb; C: noun; D: preposition"),
            ("B", "A: adjective; B: preposition; C: verb; D: conjunction"),
            ("C", "A: noun; B: conjunction/adverb; C: verb; D: adverb"),
            ("D", "A: noun; B: adjective; C: noun; D: preposition"),
        ],
        "correct_answer": "A",
        "l1_rule": "Kiểm tra vai trò của (A) sau giới từ 'in', (B) từ liên kết kẹp giữa chấm phẩy và phẩy, (C) trong cụm danh từ 'the cognition...', và (D) trong cấu trúc bị động '...understood ___ researchers'.",
        "l2_rule": "Từ 'process' vừa có thể là động từ vừa có thể là danh từ — đứng trong cụm 'the cognition ___ is not...' (trước động từ chính 'is') thì nó đóng vai trò gì?",
        "explanation": "Đáp án **A** (`A: noun; B: conjunction/adverb; C: noun; D: preposition` — Answer Key trang 201).\n• (A) *cognition* = danh từ.\n• (B) *however* = trạng từ liên kết (trong sách ghi *conjunction/adverb*).\n• (C) *process* = danh từ (thuộc cụm chủ ngữ *whose role in the cognition process*).\n• (D) *by* = giới từ.",
    },
    {
        "q_number": 8,
        "pdf_page": 46,
        "passage": "Developing tools for precise (A) control of biological activities is one of the main goals of synthetic biology. To create such instruments, researchers (B) borrow principles from numerous fields, enabling (C) them to discover potentially (D) transformative applications.",
        "options": [
            ("A", "A: verb; B: noun; C: pronoun; D: noun"),
            ("B", "A: noun; B: verb; C: preposition; D: adverb"),
            ("C", "A: noun; B: verb; C: pronoun; D: adjective"),
            ("D", "A: adjective; B: verb; C: pronoun; D: adjective"),
        ],
        "correct_answer": "C",
        "l1_rule": "Nhận diện vai trò của (A) đứng sau tính từ 'precise', (B) đứng sau chủ ngữ 'researchers', (C) 'them', và (D) đứng giữa trạng từ 'potentially' và danh từ 'applications'.",
        "l2_rule": "(A) đi sau tính từ 'precise' và trước 'of' -> không phải động từ; (D) đi ngay sau trạng từ '-ly' ('potentially') và bổ nghĩa cho danh từ 'applications'.",
        "explanation": "Đáp án **C** (`A: noun; B: verb; C: pronoun; D: adjective` — Answer Key trang 201).\n• (A) *control* = danh từ (sau tính từ *precise*).\n• (B) *borrow* = động từ chính của chủ ngữ *researchers*.\n• (C) *them* = đại từ tân ngữ thay cho *researchers*.\n• (D) *transformative* = tính từ bổ nghĩa cho danh từ *applications*.",
    },
]

# Chapter 4 missing questions #9 & #10 (PDF P72, Answer Key P205)
CH4_MISSING_9_10 = [
    {
        "q_number": 9,
        "q_label": "Ch.4 - Câu 9",
        "pdf_page": 72,
        "topic": "Exercise: Joining and Separating Sentences • Colons",
        "passage": "Bats can perceive and stalk their prey in complete darkness: they use a system of ultrasonic sounds to produce echoes that identify its location.",
        "prompt": "Determine whether the punctuation joining the two clauses is correct, or choose the revision that correctly fixes the sentence boundary.",
        "options": [
            ("A", "No error (colon correctly joins two independent clauses where the second explains the first)"),
            ("B", "Change colon to comma: ...darkness, they use..."),
            ("C", "Delete colon (fused sentence): ...darkness they use..."),
            ("D", "Change colon to comma + which: ...darkness, which they use..."),
        ],
        "correct_answer": "A",
        "l1_rule": "Kiểm tra xem vế trước dấu hai chấm (:) có phải một câu độc lập hoàn chỉnh không, và vế sau có đóng vai trò giải thích chi tiết cho vế trước không.",
        "l2_rule": "'Bats can perceive and stalk their prey in complete darkness' là một câu độc lập hoàn chỉnh; vế sau dấu hai chấm giải thích cách dơi thực hiện điều đó (dùng sóng siêu âm).",
        "explanation": "Đáp án **A** (*No error* — Answer Key trang 203: `9. Correct`). Dấu hai chấm (:) đặt sau một Independent Clause hoàn chỉnh dùng để giới thiệu lời giải thích (kể cả khi lời giải thích đó là một Independent Clause khác).",
    },
    {
        "q_number": 10,
        "q_label": "Ch.4 - Câu 10",
        "pdf_page": 72,
        "topic": "Exercise: Joining and Separating Sentences • Comma Splice Fix",
        "passage": "As an undergraduate, Theodore Roosevelt began a systematic study of the United States Navy's role in the War of 1812, assisted by two uncles, he studied original source materials and official records, ultimately publishing The Naval War of 1812 in 1882.",
        "prompt": "In the sentence above, identify and fix the sentence boundary error by adding or changing one punctuation mark.",
        "options": [
            ("A", "No error (sentence is punctuated correctly)"),
            ("B", "Change comma after '1812' to period (or semicolon/colon): ...War of 1812. Assisted by two uncles, he studied..."),
            ("C", "Change comma after 'uncles' to semicolon: ...two uncles; he studied..."),
            ("D", "Delete comma before 'he': ...assisted by two uncles he studied..."),
        ],
        "correct_answer": "B",
        "l1_rule": "Tách rõ hai mệnh đề chính trong đoạn và xác định ranh giới thực sự nằm giữa năm 1812 hay sau cụm phân từ 'assisted by two uncles'.",
        "l2_rule": "Mệnh đề 1 kết thúc ở 'the War of 1812'. Cụm 'assisted by two uncles' mở đầu bổ nghĩa cho 'he' ('he studied...'). Không thể chỉ dùng dấu phẩy nối 2 câu độc lập.",
        "explanation": "Đáp án **B** (Answer Key trang 203: `...War of 1812. Assisted by two uncles...` — hoặc dùng `;` / `:`). Đoạn chứa lỗi *comma splice* khi nối câu độc lập thứ nhất (đến *War of 1812*) với câu độc lập thứ hai (*Assisted by two uncles, he studied...*) chỉ bằng dấu phẩy. Không đặt `;` ở *two uncles* vì *Assisted by two uncles* là mảnh câu.",
    },
]

# Chapter 5 missing #1-4 (PDF P79, Answer Key P205)
CH5_MISSING_1_TO_4 = [
    {
        "q_number": 1,
        "q_label": "Ch.5 - Câu 1",
        "pdf_page": 79,
        "topic": "Exercise: Joining Sentences and Clauses • Period Boundary",
        "passage": "When light travels for billions of years, it stretches out into its full ______ light ranges from ultraviolet and visible into infrared radiation.",
        "options": [
            ("A", "spectrum, as the universe expands,"),
            ("B", "spectrum. As the universe expands,"),
            ("C", "spectrum as the universe expands,"),
            ("D", "spectrum as the universe expands"),
        ],
        "correct_answer": "B",
        "l1_rule": "Đọc trọn cả hai câu trước và sau chỗ trống để xem cụm 'as the universe expands' thuộc về câu đầu ('light stretches out') hay mở đầu câu thứ hai ('light ranges from...').",
        "l2_rule": "Nếu gắn 'as the universe expands' vào câu đầu mà theo sau là mệnh đề độc lập 'light ranges from...', sẽ mắc lỗi Comma Splice hoặc Fused Sentence. Hãy thử tách hai câu độc lập.",
        "explanation": "Đáp án **B** (`spectrum. As the universe expands,` — Answer Key trang 203: `1. B`). Vế trước dấu chấm (*When light travels..., it stretches out into its full spectrum.*) là một câu hoàn chỉnh; vế sau (*As the universe expands, light ranges...*) là một câu hoàn chỉnh thứ hai, cần dấu chấm tách biệt.",
    },
    {
        "q_number": 2,
        "q_label": "Ch.5 - Câu 2",
        "pdf_page": 79,
        "topic": "Exercise: Joining Sentences and Clauses • Participle Clause",
        "passage": "The artist Lee Lozano was known for her experimental works, some of which were shocking to critics when they first appeared. In 1967, Lozano began her ______ of eleven massive paintings of undulating lines made with shimmery iron-oxide paint. Each piece measured 96 by 42 inches and was created in one sitting: 2 Wave took eight hours, whereas 96 Wave took three days.",
        "options": [
            ("A", "Wave Series, consisting"),
            ("B", "Wave Series. Consisting"),
            ("C", "Wave Series; which consisted"),
            ("D", "Wave Series, it consisted"),
        ],
        "correct_answer": "A",
        "l1_rule": "Kiểm tra xem phần đứng sau chỗ trống ('...of eleven massive paintings...') có phải là một câu độc lập hoàn chỉnh hay là một cụm phân từ/mảnh câu bổ nghĩa.",
        "l2_rule": "Phần sau chỗ trống không có chủ ngữ và động từ chính chia thì, nên tuyệt đối không được dùng Period (.), Semicolon (;), hay tạo thêm một mệnh đề độc lập ngăn bằng dấu phẩy (, it...).",
        "explanation": "Đáp án **A** (`Wave Series, consisting` — Answer Key trang 203: `2. A`). B tạo mảnh câu đứng sau dấu chấm; C dùng sai dấu chấm phẩy trước *which*; D tạo *comma splice* với *it consisted*. A dùng dấu phẩy nối cụm phân từ *consisting of...* bổ nghĩa cho *Wave Series*.",
    },
    {
        "q_number": 3,
        "q_label": "Ch.5 - Câu 3",
        "pdf_page": 79,
        "topic": "Exercise: Joining Sentences and Clauses • Non-Essential Em-Dash + Punct",
        "passage": "Wrangell-St. Elias National Park, the largest national park in the United States, represents everything compelling about Alaska. It is ______ than Belgium. It showcases towering mountains such as Mount St. Elias, which stands more 18,000 feet tall, as well as glaciers.",
        "options": [
            ("A", "immense; larger, in fact,"),
            ("B", "immense, larger—in fact"),
            ("C", "immense—larger, in fact,"),
            ("D", "immense—larger, in fact—"),
        ],
        "correct_answer": "C",
        "l1_rule": "Xác định chức năng của 'It is immense' so với phần giải thích mở rộng 'larger than Belgium', cùng từ xen giữa 'in fact'.",
        "l2_rule": "'larger, in fact, than Belgium' KHÔNG phải là một câu hoàn chỉnh nên không dùng được dấu chấm phẩy (;). Ngoài ra, 'in fact' phải có cặp dấu phẩy ôm hai bên chứ không trộn với gạch ngang (—).",
        "explanation": "Đáp án **C** (`immense—larger, in fact,` — Answer Key trang 203: `3. C`). Mệnh đề chính *It is immense* kết thúc và được mở rộng bằng cụm đồng vị không hoàn chỉnh (*larger than Belgium*) nối bằng một dấu gạch ngang đơn (`—`), bên trong có *in fact* kẹp giữa 2 dấu phẩy (*larger, in fact, than Belgium*). A sai vì `;` đứng trước mảnh câu.",
    },
    {
        "q_number": 4,
        "q_label": "Ch.5 - Câu 4",
        "pdf_page": 79,
        "topic": "Exercise: Joining Sentences and Clauses • Compound Predicate vs Comma",
        "passage": "The \"molecular trees\" that biologists use to map out similarities between species often contradict the classifications that group organisms by their appearance. Researchers compared both kinds of trees and mapped them based on animals' ______ molecularly similar species were more likely to live near one another than those that looked similar.",
        "options": [
            ("A", "locations, and found that"),
            ("B", "locations; finding that"),
            ("C", "locations, they found that"),
            ("D", "locations, finding that"),
        ],
        "correct_answer": "D",
        "l1_rule": "Kiểm tra chủ ngữ trước chỗ trống ('Researchers compared ... and mapped...') và phân biệt cách nối cụm V-ing bổ trợ kết quả vs lỗi Comma Splice / Semicolon trước mảnh câu.",
        "l2_rule": "Chú ý: muốn dùng ', and + động từ' cho hai hành động cùng 1 chủ ngữ thì thông thường không đặt dấu phẩy trước 'and' (hơn nữa đặt ', and found' sau 'compared ... and mapped' tạo cấu trúc song song khập khiễng). B sai chấm phẩy trước 'finding'; C tạo Comma Splice (, they found).",
        "explanation": "Đáp án **D** (`locations, finding that` — Answer Key trang 203: `4. D`). *Comma + and* tương đương dấu chấm dùng để nối 2 Independent Clauses — nhưng sau *and found that* không có chủ ngữ nên A sai (không được đặt dấu phẩy trước *and* nối hai động từ chung chủ ngữ). B sai chấm phẩy trước mảnh câu *finding...*; C là lỗi *comma splice* (*, they found*). D dùng dấu phẩy mở cụm phân từ *finding that...* là chuẩn xác nhất.",
    },
]

# Chapter 6 missing worked examples (PDF P91, P101, P104)
CH6_MISSING_EXAMPLES = [
    {
        "q_number": 3,
        "q_label": "Ch.6 - Ví dụ 3",
        "category": "example",
        "pdf_page": 91,
        "topic": "Ch. 6: Non-Essential Clauses • Punctuating Transitions (Semicolon vs Comma)",
        "passage": "Led by a team from the University of California, San Diego, researchers have developed a new series of algorithms enabling four-legged robots to navigate challenging terrain while avoiding obstacles. Until now, most approaches have involved either vision or speed and sense of ______ the new system combines both options, allowing robots to anticipate changes in their environment and change course when an object is in their way.",
        "options": [
            ("A", "movement, however,"),
            ("B", "movement, however;"),
            ("C", "movement; however,"),
            ("D", "movement however,"),
        ],
        "correct_answer": "C",
        "l1_rule": "Đọc kỹ phần trước và phần sau từ nối 'however' (bỏ qua tạm 'however') để xác định cả hai bên đều là Câu Độc Lập (Independent Clauses) hay chỉ là 1 câu.",
        "l2_rule": "Câu 1: 'Until now, most approaches have involved either vision or speed and sense of movement.' Câu 2: 'The new system combines both options...'. Vì đây là 2 câu độc lập nối trực tiếp, 'however' đứng đầu Câu 2 phải đi sau dấu gì?",
        "explanation": "Đáp án **C** (`movement; however,`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 89):**\n• Đọc hai vế khi bỏ *however*: Vế 1 (*Until now, most approaches have involved...*) là một Câu Độc Lập; Vế 2 (*The new system combines both options...*) cũng là một Câu Độc Lập.\n• Vì hai câu mang ý đối lập nhau và *however* mở đầu cho câu thứ hai, nó bắt buộc phải đứng SAU dấu chấm/chấm phẩy/hai chấm và có dấu phẩy theo sau (`; however,`).",
    },
    {
        "q_number": 10,
        "q_label": "Ch.6 - Ví dụ 10",
        "category": "example",
        "pdf_page": 101,
        "topic": "Ch. 6: Non-Essential Clauses • Commas with Names and Titles",
        "passage": "Ada Lovelace and her ______ were two of the most influential figures in the history of computer science. After Babbage sketched out his ideas for an \"analytical engine,\" Lovelace demonstrated that the machine might be able to carry out a variety of complex tasks.",
        "options": [
            ("A", "acquaintance, Charles Babbage,"),
            ("B", "acquaintance Charles Babbage"),
            ("C", "acquaintance Charles Babbage,"),
            ("D", "acquaintance, Charles Babbage"),
        ],
        "correct_answer": "B",
        "l1_rule": "Áp dụng phép thử 'Gạch bỏ tên riêng' (Charles Babbage): nếu bỏ tên này đi, câu còn lại có còn xác định được nhân vật được nhắc ở câu sau ('After Babbage sketched...') và có hợp lý không?",
        "l2_rule": "Khi tên riêng nằm giữa câu, chỉ có 2 khả năng: HOẶC có hai dấu phẩy (cụm phụ), HOẶC không có dấu phẩy nào (thông tin thiết yếu). Bỏ 'Charles Babbage' thì câu chỉ còn 'her acquaintance' (cụm từ mơ hồ, hơn nữa cặp phẩy còn ngụ ý cô ấy chỉ có duy nhất 1 người quen!).",
        "explanation": "Đáp án **B** (`acquaintance Charles Babbage`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 99):**\n• Tên nằm giữa câu -> loại ngay C và D (dùng 1 dấu phẩy lẻ loi).\n• Nếu đặt 2 dấu phẩy quanh *Charles Babbage*, ta có thể gạch bỏ cái tên đó -> chỉ còn *her acquaintance*, khiến việc nhắc đích danh *Babbage* ở câu sau trở nên thiếu hụt thông tin (và còn mang hàm ý sai rằng Ada Lovelace chỉ có đúng 1 người quen). Do đó tên là **thông tin thiết yếu** -> KHÔNG dùng dấu phẩy.",
    },
    {
        "q_number": 14,
        "q_label": "Ch.6 - Ví dụ 14",
        "category": "example",
        "pdf_page": 104,
        "topic": "Ch. 6: Non-Essential Clauses • Essential vs. Non-Essential 'Who' Clause",
        "passage": "The advantages of growing up in a bilingual home can start as early as six months of age. A study conducted by York University's Institute of Health found that ______ show better attentional control than infants being raised in monolingual environments. The findings suggest that early exposure to multiple languages could set the stage for lifelong cognitive benefits.",
        "options": [
            ("A", "infants, who are regularly exposed to more than one language,"),
            ("B", "infants who are regularly exposed to more than one language,"),
            ("C", "infants, who are regularly exposed to more than one language"),
            ("D", "infants who are regularly exposed to more than one language"),
        ],
        "correct_answer": "D",
        "l1_rule": "Loại trừ các đáp án dùng dấu phẩy lẻ loi rồi dùng phép thử Gạch bỏ mệnh đề 'who...': nếu xóa đi, câu còn lại 'found that infants show better attentional control than infants being raised in monolingual environments' có vô lý không?",
        "l2_rule": "Đoạn văn không nói đến trẻ sơ sinh nói chung, mà đang so sánh một NHÓM TRẺ CỤ THỂ (những em tiếp xúc với nhiều ngôn ngữ) với nhóm trẻ đơn ngữ.",
        "explanation": "Đáp án **D** (`infants who are regularly exposed to more than one language`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 102):**\n• B và C đặt 1 dấu phẩy lẻ loi (sai cấu trúc kẹp).\n• Nếu chọn A (coi mệnh đề *who* là phụ và gạch bỏ), câu trở thành *infants show better attentional control than infants being raised in monolingual environments* — vô nghĩa về mặt so sánh nhóm. Mệnh đề *who* dùng để định danh nhóm trẻ song ngữ nên **thiết yếu**, không đặt dấu phẩy.",
    },
]

# Cumulative Review 1 missing #9-16 (PDF P117-118, Answer Key P207)
CUMREV1_MISSING_9_16 = [
    {
        "q_number": 9,
        "pdf_page": 117,
        "topic": "Cumulative Review 1 • Punctuating Transitions & Fragments",
        "passage": "Patients who participate in clinical trials hope to gain access to experimental treatments that would not otherwise be available to them. Every clinical drug trial conducted today randomly assigns patients to one of two ______ receives the actual medication.",
        "options": [
            ("A", "groups, however. Only one of which"),
            ("B", "groups; however, only one of which"),
            ("C", "groups, however, only one of them"),
            ("D", "groups; however, only one of them"),
        ],
        "correct_answer": "D",
        "l1_rule": "Phân biệt vế thứ hai 'only one of them receives...' (có chủ ngữ độc lập 'only one of them') với cụm mảnh câu 'only one of which receives...'.",
        "l2_rule": "Bỏ 'however' đi, Vế 2 đọc là 'Only one of ___ receives the actual medication': nếu dùng 'which' thì đó là mảnh câu không thể đứng sau dấu chấm (.) hay chấm phẩy (;); còn nếu là 'them' thì đó là câu độc lập hoàn chỉnh nên KHÔNG được nối bằng dấu phẩy (Comma Splice)!",
        "explanation": "Đáp án **D** (`groups; however, only one of them` — Answer Key trang 205: `9. D`). Vế sau là một Câu Độc Lập hoàn chỉnh (*only one of them receives...*), mang nghĩa đối lập nhẹ so với việc chia hai nhóm -> cần dấu chấm phẩy trước *however* và dấu phẩy sau *however*. Loại A và B (*which* tạo mảnh câu sau dấu ngắt câu); loại C (lỗi *comma splice*).",
    },
    {
        "q_number": 10,
        "pdf_page": 117,
        "topic": "Cumulative Review 1 • Sentence Boundaries & Adverbial Phrase",
        "passage": "Adam Smith argued that self-interested motives can lead to productive behavior that benefits society and not just the actor. Smith first noted the power of this form of ______ The Theory of Moral Sentiments (1759). Then, he made the argument famous in his classic 1776 treatise, The Wealth of Nations.",
        "options": [
            ("A", "motivation, in his first major work,"),
            ("B", "motivation. In his first major work,"),
            ("C", "motivation in his first major work,"),
            ("D", "motivation in his first major work;"),
        ],
        "correct_answer": "B",
        "l1_rule": "Xác định xem cụm giới từ 'in his first major work' kết thúc câu thứ nhất, hay bổ nghĩa mở đầu cho nhan đề sách 'The Theory of Moral Sentiments (1759)' — và lưu ý câu hoàn chỉnh kết thúc ở đâu.",
        "l2_rule": "Kiểm tra kỹ: nếu đặt dấu phẩy sau 'work' mà trước 'work' không có dấu ngắt câu (hoặc chỉ có dấu phẩy), thì cả mệnh đề '...noted the power of this form of motivation...' + 'The Theory of Moral Sentiments (1759)' có ghép đúng ngữ pháp với nhau không? Chú ý A vs B!",
        "explanation": "Đáp án **B** (`motivation. In his first major work,` — Answer Key trang 205: `10. B`). Ô trống ở cuối mệnh đề hoàn chỉnh *Smith first noted the power of this form of motivation.* Sau dấu chấm, câu tiếp theo giới thiệu tên tác phẩm (*In his first major work, The Theory of Moral Sentiments...* — ở dạng danh ngữ/nhãn giới thiệu ngắn hoặc nhấn mạnh, đối chiếu tiếp *Then, he made...*). Thực tế B là đáp án chuẩn trong Sách trang 205 (chú ý phân tích cú pháp cẩn thận: nếu chọn A, *The Theory of Moral Sentiments* thiếu giới từ *in* để nối vào động từ *noted*!).",
    },
    {
        "q_number": 11,
        "pdf_page": 117,
        "topic": "Cumulative Review 1 • Transitions",
        "passage": "The scientific contributions of Svänte Pääbo have shaped the entire field of paleogenetics, not just the study of Neanderthals. ______ his work has spanned all three known species of humans, one of which the world would likely be unaware if not for Pääbo and his research team.",
        "options": [
            ("A", "Indeed,"),
            ("B", "Still,"),
            ("C", "Consequently,"),
            ("D", "In contrast,"),
        ],
        "correct_answer": "A",
        "l1_rule": "Tìm mối quan hệ giữa 'toàn bộ ngành cổ di truyền học, không chỉ người Neanderthal' và việc 'nghiên cứu của ông bao trùm cả 3 loài người đã biết'.",
        "l2_rule": "Câu 2 khẳng định và làm rõ thêm mức độ bao quát rộng lớn đã nêu ở Câu 1 ('không chỉ người Neanderthal -> mà cả 3 loài người').",
        "explanation": "Đáp án **A** (*Indeed,* — Answer Key trang 205: `11. A`). *Indeed* nhấn mạnh và xác nhận nhận định ở câu đầu (đóng góp của ông vượt xa chỉ riêng người Neanderthal).",
    },
    {
        "q_number": 12,
        "pdf_page": 117,
        "topic": "Cumulative Review 1 • Sentence Boundaries + Participle Opener",
        "passage": "Until recently, the polar ice caps on Mars were thought to be frozen solid all the way to their beds due to the cold Martian climate. In 2018, evidence from the European Space Agency's Mars Express satellite challenged this ______ ice-penetrating radar called MARSIS, which can see through the planet's southern ice cap, researchers revealed an area at the base of the ice that was likely to contain liquid water.",
        "options": [
            ("A", "assumption using"),
            ("B", "assumption. Using"),
            ("C", "assumption, using"),
            ("D", "assumption and used"),
        ],
        "correct_answer": "B",
        "l1_rule": "Tìm ranh giới tách giữa câu nói về vệ tinh Mars Express ('evidence ... challenged this assumption') và câu mới nói về nhóm nghiên cứu ('researchers revealed...').",
        "l2_rule": "'Using ice-penetrating radar called MARSIS...' là cụm phân từ mở đầu giải thích cho chủ ngữ 'researchers' ở phía sau. Không thể nối hai câu độc lập không có dấu chấm hoặc chỉ dùng dấu phẩy!",
        "explanation": "Đáp án **B** (`assumption. Using` — Answer Key trang 205: `12. B`). Mệnh đề thứ nhất kết thúc trọn vẹn ở danh từ *assumption.*. Cụm *Using ice-penetrating radar...* bổ nghĩa cho chủ ngữ *researchers* ở đầu câu tiếp theo.",
    },
    {
        "q_number": 13,
        "pdf_page": 118,
        "topic": "Cumulative Review 1 • Non-Essential Clause Boundaries",
        "passage": "The trouble with quantum mechanics was never that it made the wrong prediction. In fact, from the beginning of the twentieth century, when physicists first outlined the ______ it was capable of describing the sub-atomic world with extraordinary accuracy.",
        "options": [
            ("A", "theory,"),
            ("B", "theory;"),
            ("C", "theory"),
            ("D", "theory:"),
        ],
        "correct_answer": "A",
        "l1_rule": "Kiểm tra dấu câu đứng trước cụm ', when physicists first outlined the theory...' để đóng đúng cặp dấu cho mệnh đề xen giữa.",
        "l2_rule": "Trước 'when physicists...' là một dấu phẩy mở mệnh đề trạng ngữ không thiết yếu (, when...); do đó cuối cụm này cần dấu gì để đóng lại trước mệnh đề chính 'it was capable...'?",
        "explanation": "Đáp án **A** (`theory,` — Answer Key trang 205: `13. A`). Mệnh đề *, when physicists first outlined the theory,* là mệnh đề thời gian xen giữa hai dấu phẩy; gạch bỏ đi còn *from the beginning of the twentieth century, it was capable...* vẫn hoàn toàn đúng.",
    },
    {
        "q_number": 14,
        "pdf_page": 118,
        "topic": "Cumulative Review 1 • Commas with Names & Titles",
        "passage": "Best known for the series of 10 plays collectively referred to as \"The Pittsburgh Cycle,\" the ______ explores universal themes while exploring the experiences and heritage of the African American community throughout the twentieth century.",
        "options": [
            ("A", "playwright, August Wilson,"),
            ("B", "playwright, August Wilson"),
            ("C", "playwright August Wilson,"),
            ("D", "playwright August Wilson"),
        ],
        "correct_answer": "D",
        "l1_rule": "Áp dụng phép thử 'Gạch bỏ tên riêng': nếu xóa 'August Wilson', câu còn lại 'the playwright explores...' sau cụm mở đầu có bị mơ hồ hay sai quy tắc ngăn cách Chủ ngữ – Động từ bằng dấu phẩy không?",
        "l2_rule": "Chủ ngữ hoàn chỉnh đứng trước động từ chính 'explores': không bao giờ được chỉ có MỘT dấu phẩy ngăn cách giữa Chủ ngữ và Động từ! Và nếu đặt 2 phẩy quanh tên thì 'the playwright' mơ hồ và ngụ ý vô lý rằng chỉ có đúng 1 nhà viết kịch.",
        "explanation": "Đáp án **D** (`playwright August Wilson` — Answer Key trang 205: `14. D`). Không dùng dấu phẩy lẻ giữa chủ ngữ *playwright August Wilson* và động từ *explores* (loại B, C); bỏ *August Wilson* thì không rõ nhà viết kịch nào -> thông tin thiết yếu -> không đặt dấu phẩy (chọn D).",
    },
    {
        "q_number": 15,
        "pdf_page": 118,
        "topic": "Cumulative Review 1 • Transitions",
        "passage": "In the mid-nineteenth century, governments around the world began to recognize that controlling infectious diseases would require international cooperation. ______ representatives from twelve countries came together in 1851 at the first International Sanitary Conference in an attempt to halt the spread of cholera plague and yellow fever.",
        "options": [
            ("A", "Nonetheless,"),
            ("B", "Accordingly,"),
            ("C", "Moreover,"),
            ("D", "On the other hand,"),
        ],
        "correct_answer": "B",
        "l1_rule": "Xem xét mối liên hệ giữa việc 'các chính phủ nhận ra cần hợp tác quốc tế' và hành động thực tế 'đại diện 12 nước nhóm họp tại Hội nghị Vệ sinh Quốc tế năm 1851'.",
        "l2_rule": "Hành động họp mặt của 12 quốc gia diễn ra ĐÚNG THEO nhận thức về nhu cầu hợp tác quốc tế nêu ở câu trước (Nguyên nhân -> Hành động/Hệ quả phù hợp).",
        "explanation": "Đáp án **B** (*Accordingly,* — Answer Key trang 205: `15. B`). *Accordingly* ('Theo đó / Vì thế') thể hiện hành động tổ chức hội nghị diễn ra tương ứng với nhận thức cần hợp tác ở câu trước.",
    },
    {
        "q_number": 16,
        "pdf_page": 118,
        "topic": "Cumulative Review 1 • Sentence Boundaries",
        "passage": "Since the early nineteenth century, doomsayers have gloomily predicted that increasing populations would exhaust their food ______ shortages would result in catastrophic famines. Yet the world currently produces enough food to feed 10 billion people, and there are only seven billion of us.",
        "options": [
            ("A", "supplies in only a few decades they claimed"),
            ("B", "supplies, in only a few decades, they claimed"),
            ("C", "supplies. In only a few decades, they claimed,"),
            ("D", "supplies in only a few decades they claimed,"),
        ],
        "correct_answer": "C",
        "l1_rule": "Xác định xem cụm 'in only a few decades' thuộc câu đầu hay câu sau ('shortages would result in catastrophic famines'), và xem giữa 'would exhaust their food supplies' với 'shortages would result...' có mấy câu độc lập.",
        "l2_rule": "Câu 1: '...would exhaust their food supplies.' Câu 2: 'In only a few decades, they claimed, shortages would result in catastrophic famines.' Thiếu dấu ngắt câu sẽ thành Fused Sentence hoặc Comma Splice!",
        "explanation": "Đáp án **C** (`supplies. In only a few decades, they claimed,` — Answer Key trang 205: `16. C`). Cần dấu chấm sau *supplies* để tách Câu 1 ra khỏi Câu 2 (*In only a few decades, [they claimed,] shortages would result...*). A và D tạo *fused sentence*; B tạo *comma splice* và sai cặp phẩy.",
    },
]

# Chapter 8 missing worked example (PDF P137 - Martha Graham would become)
CH8_MISSING_EX_P137 = {
    "q_number": 5,
    "q_label": "Ch.8 - Ví dụ 5",
    "category": "example",
    "pdf_page": 137,
    "topic": "Ch. 8: Verbs • Would vs. Will (Past Perspective Future)",
    "passage": "At the age of 14, Martha Graham saw the acclaimed dancer Ruth St. Denis perform and proclaimed that her future profession was \"chosen.\" However, when Graham began dancing shortly afterward, in the early years of the twentieth century, no one could have imagined that she ______ one of the greatest choreographers of all time.",
    "prompt": "Which choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [
        ("A", "will become"),
        ("B", "would become"),
        ("C", "would have become"),
        ("D", "becomes"),
    ],
    "correct_answer": "B",
    "l1_rule": "Kiểm tra mốc thời gian chính của đoạn văn ('in the early years of the twentieth century, no one could have imagined...') để chọn trợ động từ chỉ 'tương lai trong quá khứ'.",
    "l2_rule": "Khi đoạn văn kể sự kiện ở mốc thời gian quá khứ (đầu thế kỷ XX, 'could have imagined') và nói về một kết cục sẽ xảy ra sau mốc quá khứ đó, ta không dùng 'will' (hiện tại/tương lai) hay 'becomes'.",
    "explanation": "Đáp án **B** (`would become`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 135):**\n• Khi câu kể lại một mốc thời gian trong quá khứ (*early years of the twentieth century*, *could have imagined*) và diễn đạt một sự việc tính từ thời điểm quá khứ đó là \"chưa xảy ra\" (tương lai trong quá khứ), ta dùng *would + V nguyên mẫu* thay cho *will*.",
}

# Chapter 9 missing 4 worked examples (PDF P147 x2, P149 x2)
CH9_MISSING_EXAMPLES = [
    {
        "q_number": 2,
        "q_label": "Ch.9 - Ví dụ 2",
        "category": "example",
        "pdf_page": 147,
        "topic": "Ch. 9: Pronouns • Agreement with Named Singular Person",
        "passage": "Mae Jemison became the first African American woman to travel into space when she went into orbit aboard the Space Shuttle Endeavour on September 12, 1992. After ______ medical education and a brief general practice, Jemison served in the Peace Corps for two years.",
        "options": [("A", "one's"), ("B", "her"), ("C", "their"), ("D", "there")],
        "correct_answer": "B",
        "l1_rule": "Tìm danh từ tiền vị cụ thể sở hữu 'medical education' để chọn đại từ sở hữu khớp cả về số lượng và ngôi.",
        "l2_rule": "Đối tượng sở hữu 'medical education' chính là nhân vật duy nhất được nhắc rõ giới tính ở câu trước ('Mae Jemison — first African American woman').",
        "explanation": "Đáp án **B** (`her`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 145):**\n• Đại từ sở hữu quy chiếu về *Mae Jemison* (một cá nhân nữ giới cụ thể -> số ít, nữ). Chỉ có *her* là phù hợp (*their* là số nhiều, *one's* sai đối tượng, *there* là trạng từ nơi chốn).",
    },
    {
        "q_number": 3,
        "q_label": "Ch.9 - Ví dụ 3",
        "category": "example",
        "pdf_page": 147,
        "topic": "Ch. 9: Pronouns • Generic Singular Antecedent ('a person')",
        "passage": "Working memory, the ability to consciously hold and manipulate new information in the mind, is an effortful process. In particular, neurons in a person's prefrontal cortex must work together in synchrony to focus ______ thoughts.",
        "options": [("A", "our"), ("B", "one's"), ("C", "his or her"), ("D", "your")],
        "correct_answer": "C",
        "l1_rule": "Xác định danh từ sở hữu 'thoughts' trong chính câu đó: 'neurons in a person's prefrontal cortex...'.",
        "l2_rule": "Tiền vị là 'a person' (ngôi thứ ba số ít, không xác định giới tính — không phải 'our', 'your', hay đại từ phiếm chỉ 'one').",
        "explanation": "Đáp án **C** (`his or her`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 145):**\n• Theo chuẩn ngữ pháp SAT truyền thống của Erica Meltzer, khi tiền vị là một danh từ số ít không rõ giới tính như *a person*, *an architect*, đại từ tương ứng là *his or her* (không đổi đột ngột sang *our*, *your*, hay *one's*).",
    },
    {
        "q_number": 5,
        "q_label": "Ch.9 - Ví dụ 5",
        "category": "example",
        "pdf_page": 149,
        "topic": "Ch. 9: Pronouns • Ambiguous Antecedent (Noun > Pronoun)",
        "passage": "Daniel Liebeskind and Frank Gehry are among the most celebrated architects in the world. ______ known for using unconventional building materials such as corrugated metal to create tilted geometrical structures.",
        "options": [
            ("A", "He is known"),
            ("B", "It is known"),
            ("C", "Gehry is known"),
            ("D", "He would be known"),
        ],
        "correct_answer": "C",
        "l1_rule": "Kiểm tra xem câu trước nhắc đến bao nhiêu nhân vật nam giới để xem đại từ 'He' có gây mơ hồ đối tượng quy chiếu không.",
        "l2_rule": "Câu 1 nhắc hai kiến trúc sư nam là Daniel Liebeskind và Frank Gehry. Nếu câu 2 viết 'He', người đọc không thể biết đó là ai! Hãy chọn phương án chỉ rõ tên cụ thể (quy tắc Noun > Pronoun).",
        "explanation": "Đáp án **C** (`Gehry is known`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 147):**\n• Vì Daniel và Frank đều là nam giới nên dùng *He* ở A và D gây mơ hồ tiền vị (*ambiguous antecedent*). B sai số/loại (*It*). C (*Gehry is known*) nêu rõ danh từ riêng, xóa bỏ hoàn toàn sự mơ hồ.",
    },
    {
        "q_number": 6,
        "q_label": "Ch.9 - Ví dụ 6",
        "category": "example",
        "pdf_page": 149,
        "topic": "Ch. 9: Pronouns • Missing Antecedent (Noun > Pronoun)",
        "passage": "Produced by the Boston-based startup Superpedestrian, a new device called the Copenhagen Wheel can be slipped onto any bicycle to provide an electronic boost. With a 350-watt motor and a 48-volt lithium battery, it can produce more than four times the energy created by regular pedaling. ______ can use a smartphone to unlock and lock it, change gears, and select how much assistance the motor should provide.",
        "options": [
            ("A", "They"),
            ("B", "Bicycle riders"),
            ("C", "He or she"),
            ("D", "Some"),
        ],
        "correct_answer": "B",
        "l1_rule": "Đọc kỹ các câu trước xem có danh từ chỉ NGƯỜI (những người đi xe đạp) nào đã xuất hiện sẵn để các đại từ như 'They/He or she/Some' thay thế được hay chưa.",
        "l2_rule": "Văn bản chỉ mới nhắc đến công ty 'Superpedestrian', thiết bị 'Copenhagen Wheel', 'bicycle', 'motor' và 'battery' — hoàn toàn CHƯA hề có danh từ chỉ người lái! Theo nguyên tắc vàng SAT: Danh từ cụ thể luôn thắng Đại từ mơ hồ.",
        "explanation": "Đáp án **B** (`Bicycle riders`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 147):**\n• Dù theo ngữ cảnh ta hiểu *người đạp xe* là chủ thể dùng điện thoại, nhưng danh từ *bicycle riders* CHƯA từng xuất hiện trong đoạn văn nên mọi đại từ (A *They*, C *He or she*, D *Some*) đều mắc lỗi thiếu tiền vị (*missing antecedent*). B cung cấp danh từ cụ thể và là đáp án duy nhất đúng.",
    },
]

# Practice Sets missing items: Set 3 #5-8 (PDF P187, Ans P212) & Set 4 #1-4 (PDF P189, Ans P213)
PRACTICE_SET3_5_TO_8 = [
    {
        "q_number": 25,
        "q_label": "Practice Set 3 - Câu 5",
        "pdf_page": 187,
        "topic": "Set 3 • Separating Sentences",
        "passage": "Indo-European languages are the first language of more than 3 billion people in Europe, across northern India, as far east as Siberia, and in North and South America. Beginning almost 500 years ago, scholars began to notice similarities between languages such as ______ it became clear that hundreds of such languages were connected by common root words.",
        "options": [
            ("A", "Sanskrit and Latin as the field of linguistics matured,"),
            ("B", "Sanskrit and Latin, as the field of linguistics matured"),
            ("C", "Sanskrit and Latin. As the field of linguistics matured,"),
            ("D", "Sanskrit and Latin as the field of linguistics matured"),
        ],
        "correct_answer": "C",
        "l1_rule": "Đọc từ đầu câu thứ hai ('Beginning almost 500 years ago...') đến hết chỗ 'connected by common root words' để xác định ranh giới thực sự giữa hai câu độc lập.",
        "l2_rule": "Cụm 'as the field of linguistics matured' tuy nghe hợp nghĩa nếu nối vào 'Sanskrit and Latin', nhưng thực chất nó mở đầu cho Câu 3 ('As the field of linguistics matured, it became clear...'). B sẽ gây lỗi Comma Splice còn A/D tạo Fused Sentence.",
        "explanation": "Đáp án **C** (`Sanskrit and Latin. As the field of linguistics matured,` — Answer Key trang 210).\n• Bỏ qua bẫy ghép nghĩa nối đuôi: câu trước kết thúc hoàn chỉnh tại *Sanskrit and Latin.* Câu tiếp theo bắt đầu bằng mệnh đề phụ *As the field of linguistics matured,* nối với mệnh đề chính *it became clear...*. Chỉ có C tách hai câu độc lập hợp lệ bằng dấu chấm.",
    },
    {
        "q_number": 26,
        "q_label": "Practice Set 3 - Câu 6",
        "pdf_page": 187,
        "topic": "Set 3 • Commas with Names and Titles",
        "passage": "Unlike the binary bits used in standard computers, qubits can exist in multiple states at a time and have much greater processing capacity. However, they require specific conditions to exhibit quantum behavior and are challenging to harness. Synthetic ______ has corrected this problem by creating qubits from the electron spin of molecules with a central metallic atom.",
        "options": [
            ("A", "chemist Danna Freedman,"),
            ("B", "chemist, Danna Freedman,"),
            ("C", "chemist, Danna Freedman"),
            ("D", "chemist Danna Freedman"),
        ],
        "correct_answer": "D",
        "l1_rule": "Thử gạch bỏ tên riêng 'Danna Freedman' xem phần còn lại ('Synthetic chemist has corrected this problem...') có đúng ngữ pháp không (nhớ quy tắc mạo từ trước danh từ nghề nghiệp số ít).",
        "l2_rule": "Khi tên nằm giữa danh từ chức danh ('Synthetic chemist') và động từ chính ('has corrected'), loại ngay phương án có 1 dấu phẩy đơn lẻ rồi kiểm tra xem không có 'Danna Freedman' thì 'Synthetic chemist has...' thiếu mạo từ và vô nghĩa ra sao!",
        "explanation": "Đáp án **D** (`chemist Danna Freedman` — Answer Key trang 210).\n• A và C đặt 1 dấu phẩy đơn lẻ nên loại.\n• Nếu chọn B (coi *Danna Freedman* là phụ và gạch bỏ), câu trở thành *Synthetic chemist has corrected...* — sai ngữ pháp vì *chemist* số ít không có mạo từ xác định. Vậy tên riêng là thiết yếu, KHÔNG dùng dấu phẩy.",
    },
    {
        "q_number": 27,
        "q_label": "Practice Set 3 - Câu 7",
        "pdf_page": 187,
        "topic": "Set 3 • Subject-Verb Agreement & Verb Form",
        "passage": "It is a well-established fact that exercise can help people lose weight and avoid gaining it. However, identifying the cellular mechanisms that underlie this process ______ difficult because so many cells and tissues are involved.",
        "options": [
            ("A", "have proven"),
            ("B", "has proven"),
            ("C", "are proving"),
            ("D", "is proven"),
        ],
        "correct_answer": "B",
        "l1_rule": "Tìm chủ ngữ thực sự của động từ ở chỗ trống (đứng trước cụm 'the cellular mechanisms that underlie this process') để xác định số ít hay số nhiều, đồng thời chú ý dạng chủ động vs bị động.",
        "l2_rule": "Danh từ số nhiều gần chỗ trống nhất ('mechanisms') là tân ngữ; chủ ngữ thực là một Danh động từ (Gerund: 'identifying...') ở đầu mệnh đề chính! Danh động từ luôn chia Số Ít, và phải dùng đúng trợ động từ của Present Perfect ('have/has proven', không dùng 'is proven').",
        "explanation": "Đáp án **B** (`has proven` — Answer Key trang 210).\n• Chủ ngữ thật sự là danh động từ *identifying* (số ít) -> loại động từ số nhiều A (*have*) và C (*are*).\n• *prove difficult* dùng thì hiện tại hoàn thành dạng chủ động (*has proven*), không dùng *is proven* (D). Chọn B.",
    },
    {
        "q_number": 28,
        "q_label": "Practice Set 3 - Câu 8",
        "pdf_page": 187,
        "topic": "Set 3 • Pronoun Agreement",
        "passage": "The algorithms developed by computer scientist Stephanie Gil address such key questions as how robots share information and how each robot enacts an algorithm so that ______ actions are coherent within a group. Her goal is to enable the machines to achieve shared goals more efficiently and accurately.",
        "options": [
            ("A", "its"),
            ("B", "their"),
            ("C", "they're"),
            ("D", "our"),
        ],
        "correct_answer": "A",
        "l1_rule": "Đọc kỹ mệnh đề ngay trước đại từ sở hữu '___ actions' sau liên từ 'and how...': chủ thể thực hiện hành động ở đây là danh từ số ít hay số nhiều?",
        "l2_rule": "Đừng bị đánh lừa bởi chữ 'robots' ở vế đầu ('how robots share...'). Sau chữ 'and', câu mở chủ ngữ mới hoàn toàn: 'how EACH robot enacts an algorithm so that...'. Chữ 'each' luôn là số ít!",
        "explanation": "Đáp án **A** (`its` — Answer Key trang 210).\n• *and how* tách sang mệnh đề phụ mới với chủ ngữ số ít *each robot*.\n• Do đó đại từ sở hữu quy chiếu về *each robot* phải là số ít (*its*), không bị nhiễu bởi *robots* trước đó. *they're* (C) là viết tắt sai loại.",
    },
]

PRACTICE_SET4_1_TO_4 = [
    {
        "q_number": 31,
        "q_label": "Practice Set 4 - Câu 1",
        "pdf_page": 189,
        "topic": "Set 4 • Transitions",
        "passage": "One criticism that is commonly leveled against remote work is that employees, who work from home, have difficulty controlling the boundary between their personal and professional lives. ______ in a recent survey, remote workers reported a fairly good fit—5.3 on a 7-point scale—between their work and non-work lives.",
        "options": [
            ("A", "Therefore,"),
            ("B", "Similarly,"),
            ("C", "However,"),
            ("D", "Moreover,"),
        ],
        "correct_answer": "C",
        "l1_rule": "So sánh lời chỉ trích ở Câu 1 ('khó kiểm soát ranh giới công việc – đời tư') với kết quả khảo sát ở Câu 2 ('cân bằng khá tốt: 5.3/7 điểm').",
        "l2_rule": "Hai câu diễn đạt hai luồng thông tin trái chiều hoàn toàn (khó khăn vs hài lòng/cân bằng tốt).",
        "explanation": "Đáp án **C** (`However,` — Answer Key trang 211).\n• Câu 1 nêu khó khăn phổ biến; câu 2 đưa dẫn chứng khảo sát thực tế cho kết quả tích cực ngược lại -> cần từ nối tương phản (*However,*). A, B, D đều là nhóm Tiếp nối / Kết quả.",
    },
    {
        "q_number": 32,
        "q_label": "Practice Set 4 - Câu 2",
        "pdf_page": 189,
        "topic": "Set 4 • Transitions",
        "passage": "As a college student at Mt. Holyoke, the playwright Suzanne-Lori Parks was steered toward writing plays rather than fiction because of her penchant for drama. ______ she had a tendency to act out all the characters' voices when she read her short stories aloud in class.",
        "options": [
            ("A", "As such,"),
            ("B", "Specifically,"),
            ("C", "In addition,"),
            ("D", "Consequently,"),
        ],
        "correct_answer": "B",
        "l1_rule": "Kiểm tra quan hệ giữa 'thiên hướng kịch tính (penchant for drama)' ở câu 1 với hành động 'diễn xuất giọng các nhân vật khi đọc truyện ngắn trên lớp' ở câu 2.",
        "l2_rule": "Câu 2 KHÔNG phải kết quả của việc viết kịch (cô ấy diễn như vậy ngay từ lúc đọc truyện ngắn trên lớp), mà là ví dụ minh họa cụ thể cho 'penchant for drama'.",
        "explanation": "Đáp án **B** (`Specifically,` — Answer Key trang 211).\n• Câu 2 minh họa cụ thể biểu hiện của *penchant for drama* (khuynh hướng ưa kịch tính). Các đáp án A (*As such*), D (*Consequently*) chỉ hệ quả và C (*In addition*) chỉ ý bổ sung tách biệt đều sai.",
    },
    {
        "q_number": 33,
        "q_label": "Practice Set 4 - Câu 3",
        "pdf_page": 189,
        "topic": "Set 4 • Punctuating Transitions & Colons",
        "passage": "Until recently, the period of rapid cooling that occurred between 7.6 and 5.4 million years ago was attributed to carbon dioxide being drawn from the Earth's atmosphere by the weathering of the Himalayas. Barbara Clementz and Mark Carrapa propose a different contributing ______ a major increase in volcanism in the Andes around 7 million years ago.",
        "options": [
            ("A", "factor, however"),
            ("B", "factor; however,"),
            ("C", "factor however,"),
            ("D", "factor, however:"),
        ],
        "correct_answer": "D",
        "l1_rule": "Xác định từ nối 'however' đứng cuối vế trước dấu hai chấm/chấm phẩy (gắn với câu của nó), và kiểm tra xem phần sau chỗ trống ('a major increase in volcanism...') có phải là một Câu Độc Lập hoàn chỉnh không.",
        "l2_rule": "'a major increase in volcanism in the Andes around 7 million years ago' CHỈ LÀ MỘT CỤM DANH TỪ (Fragment), không có động từ chính chia thì! Vậy không được dùng dấu chấm phẩy (;), mà phải dùng dấu câu gì đứng sau câu độc lập để giới thiệu một danh từ giải thích?",
        "explanation": "Đáp án **D** (`factor, however:` — Answer Key trang 211).\n• *however* phải luôn có dấu phẩy tách biệt -> loại A và C.\n• Vế sau (*a major increase in volcanism...*) là mảnh câu không có động từ chính -> không thể dùng dấu chấm phẩy (`;`), loại B.\n• Đặt *however* ở cuối mệnh đề chính (*...propose a different contributing factor, however:*) và dùng dấu hai chấm (`:`) giới thiệu yếu tố cụ thể ở dạng cụm danh từ là hoàn toàn chuẩn xác.",
    },
    {
        "q_number": 34,
        "q_label": "Practice Set 4 - Câu 4",
        "pdf_page": 189,
        "topic": "Set 4 • Separating Sentences and Fragments",
        "passage": "Many odors are formed by volatile compounds that disintegrate ______ so widely that they can no longer be detected by a person's nose. As a result, smells tend to linger in the air for no more than a few seconds.",
        "options": [
            ("A", "easily, they disperse"),
            ("B", "easily dispersing"),
            ("C", "easily; dispersing"),
            ("D", "easily, dispersing"),
        ],
        "correct_answer": "D",
        "l1_rule": "Kiểm tra mệnh đề 'that disintegrate easily' với phần 'dispersing so widely...' xem cần dấu chấm phẩy, comma + they (dễ thành Comma Splice), hay dấu phẩy ngắt cụm phân từ V-ing.",
        "l2_rule": "Nếu chọn A (', they disperse') sẽ mắc lỗi Comma Splice vì vế trước đã có S+V hoàn chỉnh ('Many odors are formed...'); còn '; dispersing' dùng chấm phẩy trước mảnh câu V-ing là sai; cần dấu phẩy ngắt nhịp giữa 'easily' và cụm phân từ 'dispersing'.",
        "explanation": "Đáp án **D** (`easily, dispersing` — Answer Key trang 211).\n• A tạo *comma splice*; C đặt chấm phẩy trước mảnh câu *dispersing...*.\n• Cần một dấu phẩy để tách mệnh đề chính kết thúc ở *easily* ra khỏi cụm phân từ bổ sung kết quả *dispersing so widely that...* (loại B thiếu phẩy ngăn cách).",
    },
]

# Official Practice Set 1-5 Vietnamese explanations synthesized directly from Answer Key PDF P208-215
PRACTICE_SET_OFFICIAL_EXPLANATIONS = {
    1: "Đáp án **D** (*For example,* — Sách trang 206). Câu đầu nêu mâu thuẫn giữa đô thị và bền vững đã có từ rất lâu (*deep roots*), câu tiếp theo đưa một ví dụ thành phố cổ cụ thể minh họa -> chỉ *For example* đúng.",
    2: "Đáp án **B** (*Indeed,* — Sách trang 207). Câu 1 gọi Samuel Adams là kẻ ngoài vòng pháp luật; câu 2 nhấn mạnh ý đó. C (*Nevertheless*) và D (*On the other hand*) là tương phản nên tự loại; không chọn A (*Specifically*) vì câu 2 mới nêu nhận định nhấn mạnh chứ chưa liệt kê ví dụ hành vi cụ thể.",
    3: "Đáp án **D** (*Still,* — Sách trang 207). Hai câu đối lập (mèo hoang sống độc lập vs mèo biết gắn kết xã hội) -> cần từ nối tương phản (*Still*). A/B/C đều là nhóm Tiếp nối / Hệ quả / Ví dụ.",
    4: "Đáp án **C** (`goals—can` — Sách trang 207). Đọc lại từ đầu câu sẽ thấy một dấu gạch ngang mở (*...self-regulation—a critical factor...*), nên chỗ trống cần dấu gạch ngang đóng tương ứng. Gạch bỏ phần giữa hai gạch ngang câu vẫn trọn vẹn.",
    5: "Đáp án **A** (*their* — Sách trang 207). Danh từ tiền vị chỉ đối tượng có bề mặt sơn được bảo tồn là danh từ số nhiều *works*, tương ứng đại từ sở hữu *their*.",
    6: "Đáp án **B** (`trees, however, a discovery that` — Sách trang 207). Vế sau (*a discovery that suggests...*) là Mảnh Câu (không phải câu độc lập) -> loại A (dấu chấm phẩy trước mảnh câu) và D (comma splice với *this discovery*). C sai vì đặt dấu phẩy ngay sau *that*.",
    7: "Đáp án **C** (*has been* — Sách trang 207). Câu bẫy SVA giả trang câu hỏi Thì! Bỏ cụm giới từ *of genetics*, chủ ngữ chính là danh từ số ít *The role* -> loại A (*are*), B (*have been*), và D (*having been* tạo mảnh câu).",
    8: "Đáp án **D** (`humor, and John F. Kennedy quickly learned` — Sách trang 207). A và B tạo *dangling modifier* vì ngay sau dấu phẩy đầu phần văn bản theo sau là *his humor* (chứ không phải *John F. Kennedy*!). C mắc lỗi *comma splice*. D đảo tên *John F. Kennedy* ra cuối chỗ trống và dùng `, and` nối hai câu độc lập hợp lệ.",
    9: "Đáp án **C** (Sách trang 208). Cụm khóa trong đề là *rapid rise and fall* (lên nhanh và rớt nhanh). Đáp án C có cụm *viewership decreased dramatically only a decade later* khớp hoàn toàn; B chỉ nói thời điểm mất hứng thú chứ không nhấn mạnh sự sụt giảm nhanh chóng.",
    10: "Đáp án **D** (Sách trang 208). Cụm khóa là *honey's medicinal properties* (dược tính/chữa bệnh của mật ong). D nêu rõ công dụng *treat skin problems and relieve allergy symptoms* — khớp trực tiếp với khái niệm *medicinal*.",
    11: "Đáp án **A** (*Therefore,* — Sách trang 208). Câu 2 nêu kết quả tất yếu của Câu 1: vì cơ thể không tự tổng hợp được các khoáng chất này -> *vì thế* chúng ta phải hấp thụ qua thức ăn và đồ uống.",
    12: "Đáp án **D** (*Specifically,* — Sách trang 208). Câu cuối giải thích cụ thể cách nhà toán học dùng thống kê để chứng minh (xây dựng mô hình xác suất cho số tự nhiên/số nguyên).",
    13: "Đáp án **C** (*in contrast,* — Sách trang 208). Câu 1 nói glucose kích hoạt mạch báo tín hiệu đường; câu 2 nói chất làm ngọt nhân tạo *không* làm được điều đó -> đối lập hoàn toàn.",
    14: "Đáp án **C** (`supplies. In only a few decades, they claimed,` — Sách trang 208). Đọc từ đầu câu đến hết sẽ thấy phải tách thành 2 câu độc lập tại *supplies.* (vế sau là *In only a few decades, [they claimed,] shortages would happen...*). A tạo *fused sentence*, B/D sai *comma splice* và đặt phẩy trước giới từ.",
    15: "Đáp án **B** (`hunger. However,` — Sách trang 208). Vế đứng sau là một câu độc lập hoàn chỉnh và không có câu đứng trước đoạn để *however* nối ngược lại theo kiểu xen giữa câu -> phải dùng *however* mở đầu câu mới sau dấu chấm.",
    16: "Đáp án **B** (`They were` — Sách trang 208). Đại từ cần quy chiếu về hai chị em *Jane and Maria Porter* (số nhiều) -> chọn *They were*.",
    17: "Đáp án **A** (`against,` — Sách trang 209). Mệnh đề mở đầu bằng *Although* bắt buộc phải khép lại bằng dấu phẩy. Loại D vì quy tắc cấm Song liên từ (*Although ... yet*).",
    18: "Đáp án **B** (`silkworms has` — Sách trang 209). Chủ ngữ chính số ít là *The silk* (bỏ *naturally produced by silkworms*) -> loại C/D (*have*). Loại A vì đặt dấu phẩy sai giữa Chủ ngữ và Động từ.",
    19: "Đáp án **D** (`give` — Sách trang 209). Chủ ngữ ghép *Its splendid remoteness and moonscape appearance* là Số Nhiều -> dùng động từ số nhiều *give* (các đáp án A/B/C đều số ít chỉ để đánh lạc hướng).",
    20: "Đáp án **C** (Sách trang 209). Đề yêu cầu viết cho khán giả *unfamiliar with the history of papermaking* nên đáp án phải cung cấp thông tin nền cơ bản Cai Lun là ai và vai trò trong phát minh giấy — C đáp ứng trọn vẹn.",
    21: "Đáp án **A** (*For instance,* — Sách trang 209). Câu 1 nói không phải sinh vật quang hợp nào cũng dùng CO2; câu 2 nêu tên cụ thể một loài vi khuẩn không dùng CO2 -> ví dụ minh họa.",
    22: "Đáp án **D** (*Nevertheless,* — Sách trang 209). Bị phê bình vì viết thể sonnet nhưng Claude McKay vẫn tiếp tục sáng tác thể này -> quan hệ nhượng bộ/tương phản.",
    23: "Đáp án **C** (*however,* — Sách trang 210). *however* kẹp giữa 2 dấu phẩy nối câu chứa nó với câu liền trước: 15–20 Hz (câu 1) vs một con cá voi phát tần số 50 Hz (câu 2) -> tương phản.",
    24: "Đáp án **B** (*In fact,* — Sách trang 210). Câu 2 nhấn mạnh thêm quy mô lớn của nhận định ở câu 1 (nuôi sống 10 triệu người) chứ không phải hệ quả tất yếu trực tiếp (*Therefore*) -> *In fact* chính xác hơn.",
    29: "Đáp án **A** (Sách trang 210). Từ khóa *diverse origins* (nguồn gốc đa dạng) khớp trực tiếp với việc món gumbo kết hợp ẩm thực Tây Ban Nha, Caribê, Đức và người Mỹ bản địa.",
    30: "Đáp án **C** (Sách trang 210). Từ khóa *scope and purpose* đòi hỏi vừa nêu quy mô (*thousands of scientists*) vừa nêu mục tiêu (*to investigate the origins of the universe*). B thiếu mục tiêu; A/D thiếu quy mô.",
    35: "Đáp án **C** (Sách trang 211). Từ khóa *large scale* (quy mô lớn) khớp duy nhất với cụm *dozens of panels* (hàng tá bức tranh) trong C.",
    36: "Đáp án **A** (`Pablo Picasso, who added letters and words—` — Sách trang 211). Đọc hết câu thấy dấu gạch ngang đóng (*into still lifes*), nên ở đầu cụm xen giữa cần dấu gạch ngang mở tương ứng (`words—`).",
    37: "Đáp án **D** (*they* — Sách trang 211). Danh từ tiền vị chỉ những người sáng tạo thể loại hài kịch châm biếm là *Romans* (số nhiều) -> chọn *they*.",
    38: "Đáp án **C** (Sách trang 211). Kiểm tra tính đồng nhất dấu ngăn cách danh sách: không thể trộn lẫn chấm phẩy và phẩy. C dùng toàn bộ dấu phẩy chuẩn xác.",
    39: "Đáp án **A** (Sách trang 212). Đặt dấu gạch ngang đơn (`—`) sau câu độc lập hoàn chỉnh (*...known as a cataclysmic variable*) để giới thiệu định nghĩa (*a hot, dense core...* - mảnh câu). B/C/D đặt sai dấu phẩy trước giới từ hoặc tạo bổ ngữ lơ lửng.",
    40: "Đáp án **D** (*Likewise,* — Sách trang 212). Câu cuối bổ sung lý do thứ hai giải thích vì sao tên gọi 'rồng' phù hợp (thân hình nặng, có vảy — song song với cái lưỡi dài chẻ đôi ở câu trước) -> *Likewise*.",
    41: "Đáp án **C** (*However,* — Sách trang 212). Đối lập giữa kỳ vọng về một nền kinh tế vũ trụ phát triển đầy đủ và tương lai còn mờ mịt -> cần *However*.",
    42: "Đáp án **D** (*Thus,* — Sách trang 212). Vì xương không thể tách khỏi đá mà không hư hại -> *Do đó* nhóm nghiên cứu phải chụp cắt lớp CT.",
    43: "Đáp án **B** (*moreover,* — Sách trang 212). Giới thiệu một hệ quả thứ hai song song bên cạnh áp lực giao thông/tài nguyên -> *moreover* (không phải ví dụ hay tương phản).",
    44: "Đáp án **A** (*In fact,* — Sách trang 212). Câu 2 nhấn mạnh và làm rõ hơn nhận định sách in vẫn không bị sách điện tử thay thế (*outsell* ở một số trường hợp) -> dùng *In fact* thay vì *Similarly*.",
    45: "Đáp án **C** (`cold. In July,` — Sách trang 213). Cụm *in July* thuộc câu sau (*In July, the cool maritime winds bring relief*). A/D gây *fused sentence*, B gây *comma splice*.",
    46: "Đáp án **D** (`respiration—that discovery` — Sách trang 213). Cấm đặt phẩy trước *that* trong câu này -> loại A, C. B thiếu dấu ngắt nối câu -> chọn D đặt gạch ngang đơn sau câu hoàn chỉnh.",
    47: "Đáp án **B** (*they* — Sách trang 213). Quy chiếu về danh từ số nhiều *poles* (totem poles). *it* sai số, *these* đứng trơ không có danh từ sau, *some* sai ý toàn thể.",
    48: "Đáp án **D** (`the cyclists rode over mountains and valleys, alternately enduring` — Sách trang 213). Cụm đầu mô tả những người đi xe đạp (*Nicknamed Iron Riders...*), nên ngay sau *United States,* phải là *the cyclists*. Loại C vì *, and + mảnh câu* là sai.",
    49: "Đáp án **C** (Sách trang 213). Từ khóa *a difference in the type of armor* đòi hỏi từ nối đối chiếu sự khác biệt -> chỉ có C chứa *whereas* so sánh trực tiếp giữa áo giáp thời kỳ đầu và thời kỳ sau.",
    50: "Đáp án **A** (Sách trang 213). Từ khóa đề tìm *remain a mystery* khớp chính xác với *of unknown significance* trong A.",
}


def norm_text(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def load_ocr_normalized() -> dict[int, str]:
    raw = json.loads(OCR_PAGES_PATH.read_text(encoding="utf-8"))
    return {int(k): norm_text(v) for k, v in raw.items()}


def infer_pdf_page(passage: str, p_start: int, p_end: int, ocr_norm: dict[int, str], default_page: int) -> int:
    words = [w for w in norm_text(passage).split() if w not in ("notes", "student", "researching", "topic", "while")]
    best_page = None
    best_hits = 0
    for pg in range(p_start, p_end + 1):
        txt = ocr_norm.get(pg, "")
        hits = 0
        for start in range(0, min(len(words), 20), 2):
            chunk = " ".join(words[start : start + 5])
            if len(chunk) > 14 and chunk in txt:
                hits += 1
        if hits > best_hits:
            best_hits = hits
            best_page = pg
    return best_page if best_page is not None else default_page


def parse_options_raw(options_raw: str) -> list[dict]:
    opts = []
    for line in (options_raw or "").splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^([A-D])[\.\)\:]\s*(.+)$", line)
        if m:
            opts.append({"key": m.group(1), "text": m.group(2).strip()})
    return opts


def sanitize_hint_text(text: str, correct_answer: str, options: list[dict], topic: str = "") -> str:
    """Scrub any answer letter, trailing arrow conclusion, or unique correct-option phrase from L1/L2 hints."""
    out = (text or "").strip()
    if not out:
        return out

    is_pos = "Parts of Speech" in (topic or "")
    # Strip explicit letter references (preserve inline word markers (A)-(D) in Parts of Speech stems)
    if not is_pos:
        out = re.sub(r"\(\s*[A-D]\s*\)", "", out)
    out = re.sub(r"(?i)\b(?:đáp án|phương án|lựa chọn|choice|option|answer)\s*[A-D]\b", "phương án phù hợp", out)

    corr_opt = next((o["text"] for o in options if o["key"] == correct_answer), "").strip()
    other_texts = " || ".join(o["text"] for o in options if o["key"] != correct_answer).lower()

    # Strip any trailing `-> <answer conclusion>` when it reveals the option text or Sentence/Fragment label
    def _clean_arrow(m: re.Match) -> str:
        rhs = m.group(1).strip()
        rhs_l = rhs.lower()
        cl = corr_opt.lower()
        if any(o["text"].lower() in rhs_l for o in options if len(o["text"]) >= 2) or (
            cl and len(cl) >= 2 and cl in rhs_l
        ):
            return " — đối chiếu quy tắc để chọn dạng/dấu câu chuẩn."
        return m.group(0)

    out = re.sub(r"\s*->\s*([^.!?\n;]+)", _clean_arrow, out)

    # Replace quoted snippets that match the unique correct option
    for m in list(re.finditer(r"['\"`]([^'\"`]{2,})['\"`]", out)):
        snippet = m.group(1).strip()
        sl = snippet.lower()
        cl = corr_opt.lower()
        if cl and (sl == cl or (len(sl) >= 4 and sl in cl) or (len(cl) >= 4 and cl in sl)) and sl not in other_texts:
            out = out.replace(m.group(0), "cấu trúc/từ khóa đúng trong ngữ cảnh")

    # Scrub any remaining unique correct-option text (>= 3 chars) bounded by non-letters
    cl = corr_opt.lower()
    if corr_opt and len(corr_opt) >= 3 and cl not in other_texts:
        out = re.sub(rf"\([^)]*{re.escape(corr_opt)}[^)]*\)", "", out, flags=re.IGNORECASE)
        out = re.sub(rf":\s*['\"]?[^.\n]*{re.escape(corr_opt)}[^.\n]*['\"]?", ": vận dụng đúng quy tắc vừa nêu", out, flags=re.IGNORECASE)
        if len(options) == 2 and cl in ("sentence", "fragment"):
            out = re.sub(
                r"(?i)\b(?:sẽ tạo thành|là một|->|=)?\s*(?:luôn là\s*)?(?:một\s*)?(?:sentence|fragment)\b",
                "xác định xem cấu trúc có đủ Chủ–Vị độc lập hay chưa hoàn chỉnh",
                out,
            )
            out = re.sub(r"(?i)\b(?:fragment|sentence)\b", "dạng cấu trúc câu", out)
        else:
            pat = r"(?<![A-Za-z])" + re.escape(corr_opt) + r"(?![A-Za-z])"
            out = re.sub(pat, "dạng ngữ pháp đúng quy tắc", out, flags=re.IGNORECASE)

    out = re.sub(r"\s{2,}", " ", out).strip(" .,:;")
    return (out + ".") if out and not out.endswith((".", "!", "?")) else out


CLEAN_L2_RULES = {
    "EW_ew_ch5_Q11": "Vế 1 ('The northern snakehead is aptly named') và vế 2 ('its head tapers to a point...') đều là câu hoàn chỉnh nên không thể nối bằng dấu phẩy đơn lẻ (Comma Splice). Đồng thời cụm chèn '...perhaps a mad scientist—' kết thúc bằng dấu gạch ngang nên phải mở đầu bằng dấu gạch ngang.",
    "EW_ew_ch6_PP5": "Khớp cặp dấu gạch ngang mở–đóng bao quanh phần liệt kê xen giữa để phần còn lại thành câu hoàn chỉnh nói về thủ đô xanh nhất châu Âu.",
    "EW_ew_ch8_SVA4": "Chủ ngữ chính đứng đầu câu là đại từ bất định 'Any' ('bất kỳ một cá nhân nào') mang nghĩa số ít — kiểm tra xem động từ hiện tại đã chia đúng số hay chưa.",
    "EW_ew_ch8_SVA6": "Gạch bỏ các cụm giới từ ('of mysterious cave paintings', 'in the Mississippi Valley'): chủ ngữ gốc ở đầu câu là danh từ số ít nên động từ phải chia ở dạng số ít.",
    "EW_ew_ch10_Q4": "Sở hữu cách với danh từ chỉ thời gian (số ít / hôm nay): đặt dấu nháy đơn vào đúng vị trí trước danh từ 'competitions'.",
    "EW_ew_ch12_Q5": "Cấu trúc song song trong danh sách 3 cụm [Phân từ + Danh từ] ('flaring streaks, floating orbs, and...'): giữ đồng nhất trật tự và dạng phân từ -ing đứng trước danh từ.",
    "EW_ew_cr2_Q13": "Sở hữu cách danh từ số nhiều tận cùng bằng -s ('images'): đặt dấu nháy đơn ở phía sau chữ s (s') để biểu thị nhiều bức ảnh.",
    "EW_ew_sets_S1_Q4": "Đọc lùi về đầu câu để tìm dấu gạch ngang mở ('...self-regulation—a critical factor...'); tìm dấu gạch ngang đóng tương ứng ở chỗ trống.",
    "EW_ew_sets_S1_Q6": "Xét phần sau chỗ trống ('a discovery that suggests...'): đây là cụm danh từ appositive chứ không phải câu độc lập hoàn chỉnh, nên loại dấu chấm phẩy (;), comma splice, và tuyệt đối không đặt phẩy trước 'that'.",
    "EW_ew_app_Ex1": "Câu hỏi gián tiếp lồng trong câu trần thuật ('speculate about whether...'): giữ nguyên trật tự [Chủ ngữ + Động từ] và kết thúc bằng dấu chấm (.), không dùng dấu hỏi chấm (?).",
}


def assert_no_leaks(q: dict) -> None:
    """Fail loudly if tier1_hint or tier2_hint leaks correct_answer letter or unique answer text."""
    ans = q["correct_answer"]
    opts = q["options"]
    corr_text = next((o["text"] for o in opts if o["key"] == ans), "").strip()
    other_texts = " || ".join(o["text"] for o in opts if o["key"] != ans).lower()
    topic_l = (q.get("topic") or "").lower()

    for field in ("tier1_hint", "tier2_hint"):
        txt = q.get(field, "")
        txt_l = txt.lower()
        if re.search(rf"(?i)(?:đáp án|phương án|answer|choice)\s*(?:đúng|chính xác|là|:)?\s*\(?{ans}\)?\b", txt):
            raise ValueError(f"LEAK LETTER in {q['master_id']} {field}: {txt}")
        if "parts of speech" not in topic_l and re.search(rf"\(\s*{ans}\s*\)", txt):
            raise ValueError(f"LEAK PAREN LETTER in {q['master_id']} {field}: {txt}")
        if corr_text and len(corr_text) >= 3 and corr_text.lower() not in other_texts:
            cl = corr_text.lower()
            if len(opts) == 2 and cl in topic_l:
                # For 2-option Sentence/Fragment items, strip topic header before checking for leak
                txt_check = re.sub(r"\([^)]+\)", "", txt_l)
            else:
                txt_check = txt_l
            pat = r"(?:^|[\s\x27\"\(,:;—])" + re.escape(cl) + r"(?:$|[\s\x27\"\),.;:!?\-])"
            if re.search(pat, txt_check):
                raise ValueError(f"LEAK OPTION TEXT '{corr_text}' in {q['master_id']} {field}: {txt}")


def make_tiers_and_diagram(
    q_label: str,
    topic: str,
    is_example: bool,
    correct_answer: str,
    options: list[dict],
    l1_rule: str,
    l2_rule: str,
    explanation: str,
    mod_strategy: str,
) -> tuple[str, str, str, str, str]:
    """Produce (tier1_hint, tier2_hint, tier3_hint, strategic_tip, mermaid_diagram)."""
    kind = "ví dụ minh họa" if is_example else "câu hỏi thực hành"
    safe_l1 = sanitize_hint_text(l1_rule, correct_answer, options, topic)
    safe_l2 = sanitize_hint_text(l2_rule, correct_answer, options, topic)

    tier1 = (
        f"Đọc kỹ toàn bộ ngữ cảnh của {kind} ({topic}). "
        f"{safe_l1 or 'Xác định dạng kiến thức đang được kiểm tra thông qua các điểm khác biệt giữa các phương án.'}"
    )
    tier2 = (
        f"Chiến thuật Erica Meltzer: {safe_l2 or mod_strategy} "
        "Áp dụng quy trình loại trừ từng phương án sai ngữ pháp hoặc lệch logic ngữ cảnh."
    )

    corr_opt = next((o["text"] for o in options if o["key"] == correct_answer), "")
    raw_rule = (l2_rule or mod_strategy).strip()
    if explanation:
        tier3 = explanation.strip()
    else:
        tier3 = (
            f"Đáp án chính xác là **{correct_answer}** ({corr_opt}).\n\n"
            f"**Phân tích ngữ pháp & ngữ cảnh ({topic}):**\n"
            f"• {raw_rule}\n"
            f"• Phương án **{correct_answer}** (`{corr_opt}`) đảm bảo chuẩn xác cả cấu trúc ngữ pháp lẫn liên kết logic của câu văn."
        )

    tip = raw_rule
    short_topic = re.sub(r'["\n\r]', " ", topic)[:42].strip()
    short_tip = re.sub(r'["\n\r]', " ", (safe_l2 or mod_strategy))[:48].strip()
    mermaid = (
        "flowchart TD\n"
        f'    A["{q_label}<br>{short_topic}"] --> B{{"Điểm kiểm tra cốt lõi"}}\n'
        f'    B --> C["{short_tip}"]\n'
        f'    C --> D["Đáp án chuẩn: {correct_answer}"]'
    )
    return tier1, tier2, tier3, tip, mermaid


def reorder_options(options: list[dict], target_letter: str, old_ans: str) -> tuple[list[dict], str]:
    """Rotate options deterministically so correct answer rests on target_letter (eliminates A-heavy bias)."""
    if old_ans == target_letter or len(options) < 4:
        return options, old_ans
    by_key = {o["key"]: o["text"] for o in options}
    letters = ["A", "B", "C", "D"]
    texts = [by_key[k] for k in letters]
    old_idx = letters.index(old_ans)
    new_idx = letters.index(target_letter)
    shift = (new_idx - old_idx) % 4
    rotated = [None] * 4
    for i, t in enumerate(texts):
        rotated[(i + shift) % 4] = t
    return [{"key": letters[i], "text": rotated[i]} for i in range(4)], target_letter


def build_question_obj(
    gid: int,
    master_id: str,
    q_number: int,
    q_label: str,
    category: str,
    mod_meta: dict,
    topic: str,
    passage: str,
    prompt: str,
    options: list[dict],
    correct_answer: str,
    pdf_page: int,
    l1_rule: str = "",
    l2_rule: str = "",
    explanation: str = "",
    difficulty: str = "",
) -> dict:
    is_ex = category == "example"
    tier1, tier2, tier3, tip, mermaid = make_tiers_and_diagram(
        q_label=q_label,
        topic=topic,
        is_example=is_ex,
        correct_answer=correct_answer,
        options=options,
        l1_rule=l1_rule,
        l2_rule=CLEAN_L2_RULES.get(master_id, l2_rule),
        explanation=explanation,
        mod_strategy=mod_meta["strategy"],
    )
    opt_raw = "\n".join(f"{o['key']}. {o['text']}" for o in options)
    chap_title = mod_meta["title"]
    q = {
        "id": gid,
        "master_id": master_id,
        "q_number": q_number,
        "q_label": q_label,
        "category": category,
        "category_label": "Ví dụ minh họa" if is_ex else "Bài tập thực hành",
        "module_code": mod_meta["code"],
        "module_title": chap_title,
        "section": "Reading and Writing",
        "chapter": chap_title,
        "chapter_num": mod_meta["chapter_num"],
        "topic": topic,
        "passage": passage.strip(),
        "prompt": (prompt or "Which choice completes the text so that it conforms to the conventions of Standard English?").strip(),
        "options": options,
        "options_raw": opt_raw,
        "is_grid_in": False,
        "correct_answer": correct_answer,
        "acceptable_answers": [correct_answer],
        "tier1_hint": tier1,
        "tier2_hint": tier2,
        "tier3_hint": tier3,
        "strategic_tip": tip,
        "mermaid_diagram": mermaid,
        "pdf_page": pdf_page,
        "book_page": pdf_page - 2,
        "difficulty": difficulty or ("Foundation" if is_ex else "Medium"),
        "domain": mod_meta["domain"],
    }
    assert_no_leaks(q)
    return q


def excel_item_to_spec(row: dict, pdf_page: int, overrides: dict | None = None) -> dict:
    overrides = overrides or {}
    opts = overrides.get("options")
    if opts is None:
        opts = parse_options_raw(row.get("options_raw", ""))
    elif opts and isinstance(opts[0], tuple):
        opts = [{"key": k, "text": t} for k, t in opts]

    return {
        "topic": overrides.get("topic") or row.get("topic") or "",
        "passage": overrides.get("passage") or row.get("passage") or "",
        "prompt": overrides.get("prompt") or row.get("prompt") or "",
        "options": opts,
        "correct_answer": overrides.get("correct_answer") or row.get("correct_answer") or "",
        "pdf_page": pdf_page,
        "l1_rule": overrides.get("l1_rule") or row.get("l1_hint_excel") or "",
        "l2_rule": overrides.get("l2_rule") or row.get("strategic_tip") or "",
        "explanation": overrides.get("explanation") or "",
        "difficulty": overrides.get("difficulty") or "",
    }


def main() -> None:
    excel = json.loads(EXCEL_DUMP_PATH.read_text(encoding="utf-8"))
    ocr_norm = load_ocr_normalized()
    mod_by_code = {m["code"]: m for m in MODULES_META}

    # Exact verified PDF pages for Excel rows that hit multiple pages (or no-notes Ch2 / blurry P60)
    sva_a_verbs = {
        7: "was",   # Excel index 8: Q9 Punic Wars
        8: "was",   # Excel index 9: Q10 founding
        9: "were",  # Excel index 10: Q11 neither
        10: "has",  # Excel index 11: Q12 lead paint
        11: "changes",  # Excel index 12: Q13 What constitutes
        12: "spreads",  # Excel index 13: Q14 feathers
        13: "reflect",  # Excel index 14: Q15 writings
    }

    no_notes_hint_passage = (
        "[Ghi chú sư phạm Erica Meltzer — Sách trang {bk}]: Ở câu này, tác giả cố tình ẩn phần "
        "Student Notes để em rèn kỹ năng 'Key Word Matching': gạch chân cụm mục tiêu trong câu hỏi "
        "và đối chiếu trực tiếp với 4 phương án."
    )

    all_questions: list[dict] = []
    modules_out: list[dict] = []
    gid_counter = 1

    def add_q(code: str, spec: dict, q_number: int, q_label: str, category: str, suffix: str) -> None:
        nonlocal gid_counter
        mod = mod_by_code[code]
        opts = spec["options"]
        if opts and isinstance(opts[0], tuple):
            opts = [{"key": k, "text": t} for k, t in opts]
        master_id = f"EW_{mod['id']}_{suffix}"
        q_obj = build_question_obj(
            gid=gid_counter,
            master_id=master_id,
            q_number=q_number,
            q_label=q_label,
            category=category,
            mod_meta=mod,
            topic=spec["topic"],
            passage=spec["passage"],
            prompt=spec.get("prompt", ""),
            options=opts,
            correct_answer=spec["correct_answer"],
            pdf_page=spec["pdf_page"],
            l1_rule=spec.get("l1_rule", ""),
            l2_rule=spec.get("l2_rule", ""),
            explanation=spec.get("explanation", ""),
            difficulty=spec.get("difficulty", ""),
        )
        all_questions.append(q_obj)
        gid_counter += 1

    # --- 1. CHAPTER 1: TRANSITIONS (7 Ex + 20 Practice = 27) ---
    ch1_rows = excel["Ch1_Transitions"]["rows"]
    ch1_ex_pages = {1: 14, 2: 16, 3: 17, 4: 17, 5: 18}
    for ex_idx, r_idx in enumerate([1, 2, 3, 4, 5], start=1):  # Skip duplicated row [0]
        r = ch1_rows[r_idx]
        add_q(
            "Ch1_Transitions",
            excel_item_to_spec(r, ch1_ex_pages[ex_idx], {"topic": f"Ch. 1: Transitions • Ví dụ {ex_idx}"}),
            ex_idx,
            f"Ch.1 - Ví dụ {ex_idx}",
            "example",
            f"Ex{ex_idx}",
        )
    for spec in CH1_MISSING_EXAMPLES:
        add_q("Ch1_Transitions", spec, spec["q_number"], spec["q_label"], "example", f"Ex{spec['q_number']}")
    # Transitions 1 #1-10 (Excel [6..15])
    for t1_i in range(10):
        r = ch1_rows[6 + t1_i]
        num = t1_i + 1
        pg = infer_pdf_page(r["passage"], 23, 25, ocr_norm, 23 if num <= 4 else (24 if num <= 8 else 25))
        ov = {}
        if num == 5:  # Pyramids: C (Nevertheless,) is logically right; book Answer Key P203 had typo B
            ov = {
                "correct_answer": "C",
                "l1_rule": "Đối chiếu ý câu 1 ('Kim tự tháp thường gắn liền với Ai Cập cổ đại') với câu 2 ('người Nubia ở Sudan mới là nhóm xây nhiều kim tự tháp hơn hẳn').",
                "l2_rule": "Nhận thức phổ biến về Ai Cập trái ngược với sự thật gây bất ngờ về số kim tự tháp của người Nubia -> cần một Contradictor.",
                "explanation": "Đáp án chính xác là **C** (*Nevertheless,*).\n\n**Phân tích logic:**\n• Câu 1 nêu quan niệm phổ biến (gắn kim tự tháp với Ai Cập); câu 2 đưa sự thật bất ngờ trái ngược (người Nubia xây nhiều kim tự tháp hơn hẳn). Cần từ nối tương phản (*Nevertheless,*).\n• *(Lưu ý quan trọng: Sách giấy Erica Meltzer trang 201 có lỗi in ấn ghi nhầm `5. Cause-and-Effect: B`; về mặt ngữ nghĩa câu văn, *Consequently* không thể kết nối quan niệm phổ biến thành nguyên nhân xây tháp của người Nubia — đáp án chuẩn xác là **C**.)*",
            }
        add_q("Ch1_Transitions", excel_item_to_spec(r, pg, ov), num, f"Ch.1 (Transitions 1) - Câu {num}", "practice", f"T1_{num}")
    # Transitions 2 #1-8 (PDF P26-27) + #9-10 (Excel [16..17])
    for spec in CH1_T2_MISSING_1_TO_8:
        num = spec["q_number"]
        add_q("Ch1_Transitions", spec, num, spec["q_label"], "practice", f"T2_{num - 10}")
    for idx_9_10, r_idx in enumerate([16, 17], start=9):
        r = ch1_rows[r_idx]
        add_q("Ch1_Transitions", excel_item_to_spec(r, 28), 10 + idx_9_10, f"Ch.1 (Transitions 2) - Câu {idx_9_10}", "practice", f"T2_{idx_9_10}")

    # --- 2. CHAPTER 2: STUDENT NOTES (3 Ex + 5 Practice = 8) ---
    ch2_rows = excel["Ch2_StudentNotes"]["rows"]
    # Ex 1 (P30 Dinosaurs, no-notes), Ex 2 (P31-32 Weems [1]), Ex 3 (P33 Wolves [3])
    add_q(
        "Ch2_StudentNotes",
        excel_item_to_spec(ch2_rows[0], 30, {"passage": no_notes_hint_passage.format(bk=28)}),
        1,
        "Ch.2 - Ví dụ 1",
        "example",
        "Ex1",
    )
    add_q("Ch2_StudentNotes", excel_item_to_spec(ch2_rows[1], 31), 2, "Ch.2 - Ví dụ 2", "example", "Ex2")
    add_q("Ch2_StudentNotes", excel_item_to_spec(ch2_rows[3], 33), 3, "Ch.2 - Ví dụ 3", "example", "Ex3")
    # Practice #1-3 (no-notes P34-36), #4-5 (full notes P37-38)
    ch2_pr_map = [(4, 34, True), (5, 35, True), (6, 36, True), (7, 37, False), (8, 38, False)]
    for p_num, (r_idx, pg, hide_notes) in enumerate(ch2_pr_map, start=1):
        r = ch2_rows[r_idx]
        ov = {"passage": no_notes_hint_passage.format(bk=pg - 2)} if hide_notes else {}
        add_q("Ch2_StudentNotes", excel_item_to_spec(r, pg, ov), p_num, f"Ch.2 (Student Notes) - Câu {p_num}", "practice", f"Q{p_num}")

    # --- 3. PARTS OF SPEECH INTRO (0 Ex + 8 Practice = 8) ---
    for spec in PARTS_OF_SPEECH_ITEMS:
        n = spec["q_number"]
        add_q(
            "PartsOfSpeech_Intro",
            {
                **spec,
                "topic": f"Identifying Parts of Speech • Câu {n}",
                "prompt": "Identify the part of speech corresponding to each underlined marker (A), (B), (C), and (D) in order.",
            },
            n,
            f"Parts of Speech - Câu {n}",
            "practice",
            f"Q{n}",
        )

    # --- 4. CHAPTER 3: SENTENCES & FRAGMENTS (1 Ex + 33 Practice = 34) ---
    ch3_rows = excel["Ch3_SentencesFragments"]["rows"]
    ch4_rows = excel["Ch4_JoiningSeparating"]["rows"]
    # Worked Example (P49 Louis Armstrong -> Excel Ch4[0])
    add_q("Ch3_SentencesFragments", excel_item_to_spec(ch4_rows[0], 49), 1, "Ch.3 - Ví dụ 1", "example", "Ex1")
    # Drill 1: Is It a Sentence? #1-18 (Excel Ch3[4..21], P47-48)
    for i in range(18):
        r = ch3_rows[4 + i]
        num = i + 1
        pg = 47 if num <= 6 else 48
        add_q("Ch3_SentencesFragments", excel_item_to_spec(r, pg), num, f"Ch.3 (Is It a Sentence?) - Câu {num}", "practice", f"S{num}")
    # Drill 2: Sentences and Fragments #1-15 (Excel Ch3[22..36], P59-60)
    rot_targets = {2: "B", 3: "C", 4: "D", 5: "A", 6: "C", 7: "D", 8: "B", 9: "C"}
    for i in range(15):
        r = ch3_rows[22 + i]
        num = i + 1
        pg = 59 if num <= 9 else 60
        spec = excel_item_to_spec(r, pg)
        if num in rot_targets:
            spec["options"], spec["correct_answer"] = reorder_options(spec["options"], rot_targets[num], spec["correct_answer"])
        add_q("Ch3_SentencesFragments", spec, 18 + num, f"Ch.3 (Sentences & Fragments) - Câu {num}", "practice", f"SF{num}")

    # --- 5. CHAPTER 4: JOINING & SEPARATING (8 Ex + 15 Practice = 23) ---
    ch4_ex_pages = {1: 62, 2: 63, 3: 64, 4: 66, 5: 67, 6: 67, 7: 68, 8: 69}
    for ex_num in range(1, 9):
        r = ch4_rows[ex_num]  # Excel indices 1..8
        add_q("Ch4_JoiningSeparating", excel_item_to_spec(r, ch4_ex_pages[ex_num]), ex_num, f"Ch.4 - Ví dụ {ex_num}", "example", f"Ex{ex_num}")
    # Practice #1-8 (Excel [9..16], P71) + #9-10 (CH4_MISSING_9_10, P72) + #11-15 (Excel [17..21], P72-73)
    for idx_1_8 in range(8):
        r = ch4_rows[9 + idx_1_8]
        num = idx_1_8 + 1
        add_q("Ch4_JoiningSeparating", excel_item_to_spec(r, 71), num, f"Ch.4 - Câu {num}", "practice", f"Q{num}")
    for spec in CH4_MISSING_9_10:
        n = spec["q_number"]
        add_q("Ch4_JoiningSeparating", spec, n, spec["q_label"], "practice", f"Q{n}")
    for idx_11_15 in range(5):
        r = ch4_rows[17 + idx_11_15]
        num = 11 + idx_11_15
        pg = infer_pdf_page(r["passage"], 72, 73, ocr_norm, 72 if num <= 13 else 73)
        add_q("Ch4_JoiningSeparating", excel_item_to_spec(r, pg), num, f"Ch.4 - Câu {num}", "practice", f"Q{num}")

    # --- 6. CHAPTER 5: JOINING SENTENCES & CLAUSES (3 Ex + 15 Practice = 18) ---
    # 3 Ex (Excel Ch4[22..24], P76-77)
    for ex_idx, r_idx in enumerate([22, 23, 24], start=1):
        pg = 76 if ex_idx == 1 else 77
        add_q("Ch5_JoiningClauses", excel_item_to_spec(ch4_rows[r_idx], pg), ex_idx, f"Ch.5 - Ví dụ {ex_idx}", "example", f"Ex{ex_idx}")
    # Practice #1-4 (CH5_MISSING_1_TO_4, P79) + #5-15 (Excel Ch4[25..35], P80-82)
    for spec in CH5_MISSING_1_TO_4:
        n = spec["q_number"]
        add_q("Ch5_JoiningClauses", spec, n, spec["q_label"], "practice", f"Q{n}")
    for offset in range(11):
        r = ch4_rows[25 + offset]
        num = 5 + offset
        pg = infer_pdf_page(r["passage"], 80, 82, ocr_norm, 80 if num <= 8 else (81 if num <= 12 else 82))
        ov = {}
        if num == 11:  # CRITICAL FIX: Northern snakehead (PNG p81.png + Answer Key logic) -> A!
            ov = {
                "options": [
                    ("A", "named: its head tapers to a point, making it look as if someone—"),
                    ("B", "named, its head tapers to a point, making it look as if someone—"),
                    ("C", "named— its head tapers to a point, making it look as if someone,"),
                    ("D", "named—its head tapers to a point, making it look as if someone,"),
                ],
                "correct_answer": "A",
                "l1_rule": "Kiểm tra dấu kết thúc của cụm chèn giữa ('...perhaps a mad scientist—') để tìm cặp dấu mở tương ứng, đồng thời kiểm tra ranh giới hai câu độc lập.",
                "l2_rule": "Vế 1 ('The northern snakehead is aptly named') và vế 2 ('its head tapers to a point...') đều là câu hoàn chỉnh -> không dùng phẩy (loại B). Đồng thời cụm chèn '...perhaps a mad scientist—' kết thúc bằng dấu gạch ngang nên phải mở đầu bằng dấu gạch ngang!",
                "explanation": "Đáp án **A** (`named: its head tapers to a point, making it look as if someone—`).\n\n**Phân tích trực tiếp từ trang 79 sách gốc:**\n• *The northern snakehead is aptly named* là câu độc lập hoàn chỉnh, theo sau là lời giải thích (*its head tapers...*) -> dấu hai chấm (`:`) ở A là hợp lệ (B tạo *comma splice*).\n• Cụm chèn *—perhaps a mad scientist—* kết thúc bằng dấu gạch ngang nên bắt buộc phải mở đầu bằng dấu gạch ngang sau *someone* (trong bản in sách giấy, C và D đều kết thúc bằng dấu phẩy `someone,` nên sai quy tắc kẹp đôi).",
            }
        add_q("Ch5_JoiningClauses", excel_item_to_spec(r, pg, ov), num, f"Ch.5 - Câu {num}", "practice", f"Q{num}")

    # --- 7. CHAPTER 6: NON-ESSENTIAL & ESSENTIAL CLAUSES (14 Ex + 34 Practice = 48) ---
    ch6_rows = excel["Ch6_NonEssentialClauses"]["rows"]
    # 14 Worked Examples in exact book page order (P84-104)
    ch6_ex_sequence = [
        ("excel", 0, 84),     # Ex 1: London which (D)
        ("excel", 1, 85),     # Ex 2: London fragment (D)
        ("new", CH6_MISSING_EXAMPLES[0], 91),  # Ex 3: UCSD robots ; however, (C)
        ("excel", 17, 92),    # Ex 4: robots , though. (B)
        ("excel", 18, 93),    # Ex 5: Galileo (A)
        ("excel", 23, 95),    # Ex 6: Norman Conquest (B)
        ("excel", 24, 96),    # Ex 7: London parens (D)
        ("excel", 25, 96),    # Ex 8: Tower 1 (D)
        ("excel", 26, 97),    # Ex 9: Tower 2 (C)
        ("new", CH6_MISSING_EXAMPLES[1], 101), # Ex 10: Ada Lovelace (B)
        ("excel", 32, 102),   # Ex 11: Kincaid 1 (B)
        ("excel", 33, 102),   # Ex 12: Kincaid 2 (A)
        ("excel", 34, 103),   # Ex 13: Annie John (B)
        ("new", CH6_MISSING_EXAMPLES[2], 104), # Ex 14: York bilingual infants (D)
    ]
    for ex_idx, (src, payload, pg) in enumerate(ch6_ex_sequence, start=1):
        spec = excel_item_to_spec(ch6_rows[payload], pg) if src == "excel" else payload
        add_q("Ch6_NonEssentialClauses", spec, ex_idx, f"Ch.6 - Ví dụ {ex_idx}", "example", f"Ex{ex_idx}")

    # Ch6 Practice Drills (34 Questions)
    ch6_p_num = 1
    # Drill 1: Identifying Non-Essential Words #1-15 (Excel [2..16], P87-88)
    for i in range(15):
        r = ch6_rows[2 + i]
        pg = infer_pdf_page(r["passage"], 87, 88, ocr_norm, 87 if i < 9 else 88)
        add_q("Ch6_NonEssentialClauses", excel_item_to_spec(r, pg), ch6_p_num, f"Ch.6 (Non-Essential ID) - Câu {i+1}", "practice", f"ID{i+1}")
        ch6_p_num += 1
    # Drill 2: Quick Check Punctuating Transitions #1-4 (Excel [19..22], P94)
    for i in range(4):
        r = ch6_rows[19 + i]
        add_q("Ch6_NonEssentialClauses", excel_item_to_spec(r, 94), ch6_p_num, f"Ch.6 (Punctuating Transitions) - Câu {i+1}", "practice", f"QC{i+1}")
        ch6_p_num += 1
    # Drill 3: Non-Essential Clauses Commas/Dashes/Parens #1-5 (Excel [27..31], P98-99)
    for i in range(5):
        r = ch6_rows[27 + i]
        pg = 98 if i < 3 else 99
        ov = {}
        if i == 0:  # FIX #1 Parrots -> A (cognition—) per PNG p98 + Answer Key P206!
            ov = {
                "correct_answer": "A",
                "l1_rule": "Kiểm tra dấu kết thúc cụm xen giữa '...comparable to those of primates—' để chọn đúng dấu mở tương ứng.",
                "l2_rule": "Cụm giải thích 'their lifespans and relative brain size are comparable to those of primates' đóng lại bằng một dấu gạch ngang (—) ở cuối -> bắt buộc phải mở đầu bằng dấu gì?",
                "explanation": "Đáp án **A** (`cognition—` — Answer Key trang 204: `1. A`). Cụm thông tin phụ *their lifespans and relative brain size are comparable to those of primates—* khép lại bằng dấu gạch ngang nên đầu cụm phải mở bằng dấu gạch ngang tương ứng (không dùng phẩy hay hai chấm).",
            }
        add_q("Ch6_NonEssentialClauses", excel_item_to_spec(r, pg, ov), ch6_p_num, f"Ch.6 (Punctuation Pair) - Câu {i+1}", "practice", f"PP{i+1}")
        ch6_p_num += 1
    # Drill 4: All Non-Essential & Essential Clauses #1-10 (Excel [35..44], P105-107)
    for i in range(10):
        r = ch6_rows[35 + i]
        pg = infer_pdf_page(r["passage"], 105, 107, ocr_norm, 105 if i < 3 else (106 if i < 7 else 107))
        ov = {}
        if i == 7:  # FIX #8 March of Dimes -> C per PNG p107 & P206!
            ov = {
                "correct_answer": "C",
                "l1_rule": "Áp dụng phép thử Gạch bỏ tên tổ chức 'March of Dimes' xem khi có mạo từ 'the Organization' đứng trước, tên riêng đó là thông tin thiết yếu hay bổ sung phụ?",
                "l2_rule": "Trong câu '...having founded the Organization, March of Dimes, to spur...', khi lược bỏ 'March of Dimes', câu còn 'having founded the Organization to spur...' vẫn trọn vẹn cú pháp — đồng thời đáp án viết hoa 'Organization' kết hợp cặp dấu phẩy hai bên.",
                "explanation": "Đáp án **C** (`Organization, March of Dimes,` — Answer Key trang 204: `8. C`). *Organization* viết hoa như danh từ riêng rút gọn đi kèm tên giải thích kẹp hai dấu phẩy (*the Organization, March of Dimes, to spur...*). A và D chỉ có 1 dấu phẩy đơn lẻ giữa cụm; Answer Key trang 204 xác nhận chuẩn đáp án là **C**.",
            }
        elif i == 9:  # FIX #10 Agojie -> C per PNG p107 & P206!
            ov = {
                "correct_answer": "C",
                "l1_rule": "Xét tách biệt hai cụm: (1) dấu phẩy trước mệnh đề trạng ngữ 'when...' và (2) mệnh đề quan hệ 'who were already experienced elephant-hunters' — liệu đó là bất kỳ phụ nữ nào hay nhóm thợ săn voi cụ thể?",
                "l2_rule": "Nếu bỏ cụm 'who were already experienced elephant-hunters' (chặn bằng 2 phẩy), nghĩa bị mơ hồ thành 'một đội gồm những người phụ nữ' chung chung; vậy mệnh đề 'who...' là THIẾT YẾU (không đặt dấu phẩy)!",
                "explanation": "Đáp án **C** (`existence, when a troupe consisting of women who were already experienced elephant-hunters` — Answer Key trang 204: `10. C`).\n• Cần 1 dấu phẩy trước *when* để mở mệnh đề phụ giải thích thời điểm (*existence, when...*).\n• Mệnh đề *who were already experienced elephant-hunters* là thông tin thiết yếu xác định rõ nhóm phụ nữ nào -> KHÔNG đặt dấu phẩy kẹp mệnh đề *who* và KHÔNG ngắt phẩy giữa chủ ngữ *a troupe...* và động từ *was created*.",
            }
        add_q("Ch6_NonEssentialClauses", excel_item_to_spec(r, pg, ov), ch6_p_num, f"Ch.6 (Essential vs Non-Essential) - Câu {i+1}", "practice", f"ALL{i+1}")
        ch6_p_num += 1

    # --- 8. CHAPTER 7: COMMA USES & MISUSES (0 Ex + 6 Practice = 6) ---
    for i, r in enumerate(excel["Ch7_CommaUsesMisuses"]["rows"], start=1):
        pg = infer_pdf_page(r["passage"], 113, 114, ocr_norm, 113 if i <= 4 else 114)
        add_q("Ch7_CommaUsesMisuses", excel_item_to_spec(r, pg), i, f"Ch.7 - Câu {i}", "practice", f"Q{i}")

    # --- 9. CUMULATIVE REVIEW 1 (0 Ex + 20 Practice = 20) ---
    cr1_rows = excel["Cumulative_Review_Punct"]["rows"]
    # #1-8 (Excel [0..7], P115-116)
    for i in range(8):
        r = cr1_rows[i]
        num = i + 1
        pg = infer_pdf_page(r["passage"], 115, 116, ocr_norm, 115 if num <= 4 else 116)
        ov = {}
        if num == 1:  # FIX #1 Voices -> C (However,) per P207!
            ov = {
                "correct_answer": "C",
                "l1_rule": "Đối chiếu đối tượng ở Câu 1 ('tiếng nói của cùng loài và thậm chí khác loài như con người') với đối tượng ở Câu 2 ('chỉ một vài loài động vật, như khỉ đột, mới gắn được giọng nói với ký ức vui/buồn').",
                "l2_rule": "Câu 1 nói nhiều động vật làm được điều A; Câu 2 giới hạn lại: tuy nhiên chỉ một số ít (*a few animals*) tiến tới mức B! Cần một Contradictor mở đầu Câu 2.",
                "explanation": "Đáp án **C** (`However,` — Answer Key trang 205: `1. C`).\n• Câu 1 nói phổ biến nhiều loài nhận ra tiếng nói (*Many animals*); Câu 2 thu hẹp/chuyển hướng sang ngoại lệ hẹp hơn (*a few animals* có khả năng gắn ký ức cảm xúc) -> dùng *However,*.",
            }
        add_q("Cumulative_Review_1", excel_item_to_spec(r, pg, ov), num, f"Cumulative Review 1 - Câu {num}", "practice", f"Q{num}")
    # #9-16 (CUMREV1_MISSING_9_16, P117-118)
    for spec in CUMREV1_MISSING_9_16:
        n = spec["q_number"]
        add_q("Cumulative_Review_1", spec, n, f"Cumulative Review 1 - Câu {n}", "practice", f"Q{n}")
    # #17-20 (Excel [8..11], P119-120)
    for offset in range(4):
        r = cr1_rows[8 + offset]
        num = 17 + offset
        pg = infer_pdf_page(r["passage"], 119, 120, ocr_norm, 119 if num <= 18 else 120)
        add_q("Cumulative_Review_1", excel_item_to_spec(r, pg), num, f"Cumulative Review 1 - Câu {num}", "practice", f"Q{num}")

    # --- 10. CHAPTER 8: VERBS: AGREEMENT & TENSE (7 Ex + 24 Practice = 31) ---
    ch8_rows = excel["Ch8_VerbsAgreementTense"]["rows"]
    # Ex 1 (Alan Chin [0], P124), Ex 2-4 ([15..17], P133, 134, 135), Ex 5 (P137 Martha would become), Ex 6-7 ([18..19], P139, 140)
    ch8_ex_items = [
        ("excel", 0, 124),
        ("excel", 15, 133),
        ("excel", 16, 134),
        ("excel", 17, 135),
        ("new", CH8_MISSING_EX_P137, 137),
        ("excel", 18, 139),
        ("excel", 19, 140),
    ]
    for ex_idx, (src, payload, pg) in enumerate(ch8_ex_items, start=1):
        ov = {}
        if src == "excel" and payload == 17:  # P135 Martha Graham had given typo note
            ov = {
                "explanation": "Đáp án **C** (`had given`).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 133):**\n• Cụm thời gian mốc *By the time she retired from the stage in 1970* báo hiệu hành động xảy ra TRƯỚC một hành động quá khứ khác -> bắt buộc dùng thì **Quá khứ hoàn thành (Past Perfect: had + V3)**.\n• *(Lưu ý: Trong phần lời giải trang 133 của sách giấy có lỗi đánh máy in chữ `(D)` ở câu chốt dù ngay phía trên tác giả giải thích công thức `had + past participle = had given`; đáp án ngữ pháp chuẩn xác là **C**.)*",
            }
        spec = excel_item_to_spec(ch8_rows[payload], pg, ov) if src == "excel" else payload
        add_q("Ch8_VerbsAgreementTense", spec, ex_idx, f"Ch.8 - Ví dụ {ex_idx}", "example", f"Ex{ex_idx}")

    # Practice Drill 1: SVA #1-14 (Excel [1..14], P131-132)
    for i in range(14):
        r = ch8_rows[1 + i]
        num = i + 1
        pg = 131 if num <= 7 else 132
        opts = parse_options_raw(r["options_raw"])
        if i in sva_a_verbs and opts and opts[0]["text"] == "NO CHANGE":
            opts[0]["text"] = f"NO CHANGE ({sva_a_verbs[i]})"
        ov = {"options": opts}
        if num == 4:  # FIX SVA #4 Any of the participants -> A (is permitted) per P207!
            ov["correct_answer"] = "A"
            ov["l1_rule"] = "Xem lại cách Erica Meltzer phân tích chủ ngữ với đại từ 'Any' trong bài tập trang 129 và đáp án trang 205."
            ov["l2_rule"] = "Chủ ngữ chính đứng đầu câu là 'Any' ('bất kỳ một người nào trong số các thí sinh') mang nghĩa số ít -> động từ 'is permitted' hiện tại đã đúng hay sai?"
            ov["explanation"] = "Đáp án **A** (`NO CHANGE (is permitted)` — Answer Key trang 205: `4. Correct: is (subject: any)`). Chủ ngữ thực của câu là đại từ số ít *Any* (bất kỳ một cá nhân nào trong nhóm tham gia), nên động từ số ít *is permitted* hoàn toàn chính xác."
        add_q("Ch8_VerbsAgreementTense", excel_item_to_spec(r, pg, ov), num, f"Ch.8 (SVA) - Câu {num}", "practice", f"SVA{num}")

    # Practice Drill 2: Agreement & Tense #1-10 (Excel [20..29], P142-144)
    for i in range(10):
        r = ch8_rows[20 + i]
        num = i + 1
        pg = infer_pdf_page(r["passage"], 142, 144, ocr_norm, 142 if num <= 3 else (143 if num <= 7 else 144))
        add_q("Ch8_VerbsAgreementTense", excel_item_to_spec(r, pg), 14 + num, f"Ch.8 (Agreement & Tense) - Câu {num}", "practice", f"VT{num}")

    # --- 11. CHAPTER 9: PRONOUNS (7 Ex + 10 Practice = 17) ---
    ch9_rows = excel["Ch9_Pronouns"]["rows"]
    ch9_ex_sequence = [
        ("excel", 0, 145),     # Ex 1: Cacao
        ("new", CH9_MISSING_EXAMPLES[0], 147),  # Ex 2: Mae Jemison
        ("new", CH9_MISSING_EXAMPLES[1], 147),  # Ex 3: Working memory / person
        ("excel", 1, 148),     # Ex 4: Consciously hold / our
        ("new", CH9_MISSING_EXAMPLES[2], 149),  # Ex 5: Liebeskind / Gehry
        ("new", CH9_MISSING_EXAMPLES[3], 149),  # Ex 6: Copenhagen Wheel
        ("excel", 2, 150),     # Ex 7: Internet
    ]
    for ex_idx, (src, payload, pg) in enumerate(ch9_ex_sequence, start=1):
        spec = excel_item_to_spec(ch9_rows[payload], pg) if src == "excel" else payload
        add_q("Ch9_Pronouns", spec, ex_idx, f"Ch.9 - Ví dụ {ex_idx}", "example", f"Ex{ex_idx}")
    for i in range(10):
        r = ch9_rows[3 + i]
        num = i + 1
        pg = infer_pdf_page(r["passage"], 154, 156, ocr_norm, 154 if num <= 4 else (155 if num <= 7 else 156))
        ov = {}
        if num == 4:  # FIX #4 Miles Davis -> C (one) per P207!
            ov = {
                "correct_answer": "C",
                "l1_rule": "Kiểm tra ngữ nghĩa danh từ sau động từ 'joined': câu nói riêng Miles Davis gia nhập hàng ngũ cùng Ella Fitzgerald và Duke Ellington với tư cách là một người trong nhóm đó hay nhiều người?",
                "l2_rule": "Chủ ngữ của câu là MỘT người ('He joined A and B as ___ of the most renowned performers'): một cá nhân gia nhập nhóm những nghệ sĩ hàng đầu thì dùng đại từ số ít!",
                "explanation": "Đáp án **C** (`one` — Answer Key trang 205: `4. C`). *He* (Miles Dewey Davis III — số ít) gia nhập cùng Ella Fitzgerald và Duke Ellington với tư cách là *một trong những* (*one of*) nghệ sĩ jazz nổi tiếng nhất.",
            }
        add_q("Ch9_Pronouns", excel_item_to_spec(r, pg, ov), num, f"Ch.9 - Câu {num}", "practice", f"Q{num}")

    # --- 12. CHAPTER 10: APOSTROPHES (2 Ex + 6 Practice = 8) ---
    ch10_rows = excel["Ch10_Apostrophes"]["rows"]
    add_q("Ch10_Apostrophes", excel_item_to_spec(ch10_rows[0], 158), 1, "Ch.10 - Ví dụ 1", "example", "Ex1")
    add_q(
        "Ch10_Apostrophes",
        excel_item_to_spec(
            ch10_rows[1],
            161,
            {
                "explanation": "Đáp án **C** (*their*).\n\n**Bài giảng chi tiết của Erica Meltzer (Trang 159):**\n• Danh từ tiền vị là *silent synapses* (số nhiều) -> loại *its* (A) và *it's* (B).\n• Thay thử *they are* cho D (*they're*): *suggests that they are role...* -> hoàn toàn vô nghĩa -> loại D, chọn **C** (*their*).\n• *(Lưu ý: Trong sách giấy trang 159 dòng chốt bị in nhầm ký hiệu `(C) can thus be eliminated, leaving (D)`, nhưng phần giải thích ngay phía trên chứng minh *they are* sai nên *their* (C) mới là đáp án đúng.)*",
            },
        ),
        2,
        "Ch.10 - Ví dụ 2",
        "example",
        "Ex2",
    )
    for i in range(6):
        r = ch10_rows[2 + i]
        num = i + 1
        pg = infer_pdf_page(r["passage"], 162, 163, ocr_norm, 162 if num <= 3 else 163)
        add_q("Ch10_Apostrophes", excel_item_to_spec(r, pg), num, f"Ch.10 - Câu {num}", "practice", f"Q{num}")

    # --- 13. CHAPTER 11: MODIFICATION (4 Ex + 6 Practice = 10) ---
    ch11_rows = excel["Ch11_Modification"]["rows"]
    ch11_ex_pages = {1: 165, 2: 166, 3: 167, 4: 167}
    for i in range(4):
        add_q("Ch11_Modification", excel_item_to_spec(ch11_rows[i], ch11_ex_pages[i + 1]), i + 1, f"Ch.11 - Ví dụ {i+1}", "example", f"Ex{i+1}")
    for i in range(6):
        r = ch11_rows[4 + i]
        num = i + 1
        pg = infer_pdf_page(r["passage"], 169, 170, ocr_norm, 169 if num <= 3 else 170)
        add_q("Ch11_Modification", excel_item_to_spec(r, pg), num, f"Ch.11 - Câu {num}", "practice", f"Q{num}")

    # --- 14. CHAPTER 12: PARALLEL STRUCTURE (5 Ex + 5 Practice = 10) ---
    ch12_rows = excel["Ch12_ParallelStructure"]["rows"]
    ch12_ex_pages = {1: 171, 2: 172, 3: 172, 4: 173, 5: 173}
    for i in range(5):
        add_q("Ch12_ParallelStructure", excel_item_to_spec(ch12_rows[i], ch12_ex_pages[i + 1]), i + 1, f"Ch.12 - Ví dụ {i+1}", "example", f"Ex{i+1}")
    for i in range(5):
        r = ch12_rows[5 + i]
        num = i + 1
        pg = infer_pdf_page(r["passage"], 174, 175, ocr_norm, 174 if num <= 3 else 175)
        add_q("Ch12_ParallelStructure", excel_item_to_spec(r, pg), num, f"Ch.12 - Câu {num}", "practice", f"Q{num}")

    # --- 15. CUMULATIVE REVIEW 2 (0 Ex + 15 Practice = 15) ---
    for i, r in enumerate(excel["Cumulative_Review_Grammar"]["rows"], start=1):
        pg = infer_pdf_page(r["passage"], 176, 179, ocr_norm, 176 + min(3, (i - 1) // 4))
        add_q("Cumulative_Review_2", excel_item_to_spec(r, pg), i, f"Cumulative Review 2 - Câu {i}", "practice", f"Q{i}")

    # --- 16. PRACTICE SETS 1-5 (0 Ex + 50 Practice = 50) ---
    ps_rows = excel["PracticeSets_AllChapters"]["rows"]
    # Build ordered list of all 50 questions across Sets 1-5:
    # Set 1 (1..10): ps[0..9], P180-182
    # Set 2 (11..20): ps[10..19], P183-185
    # Set 3 (21..30): ps[20..23] (#1-4 P186), missing 5-8 (P187), ps[24..25] (#9-10 P188)
    # Set 4 (31..40): missing 1-4 (P189), ps[26..31] (#5-10 P190-191)
    # Set 5 (41..50): ps[32..41] (#1-10 P192-194)
    ps_items = []
    for idx in range(0, 24):  # Set 1 (0..9), Set 2 (10..19), Set 3 #1-4 (20..23)
        ps_items.append(("excel", ps_rows[idx]))
    for sp in PRACTICE_SET3_5_TO_8:
        ps_items.append(("new", sp))
    for idx in (24, 25):  # Set 3 #9-10
        ps_items.append(("excel", ps_rows[idx]))
    for sp in PRACTICE_SET4_1_TO_4:
        ps_items.append(("new", sp))
    for idx in range(26, 42):  # Set 4 #5-10 (26..31), Set 5 #1-10 (32..41)
        ps_items.append(("excel", ps_rows[idx]))

    assert len(ps_items) == 50, f"Expected 50 Practice Set questions, got {len(ps_items)}"
    for g_idx, (src, payload) in enumerate(ps_items, start=1):
        set_num = (g_idx - 1) // 10 + 1
        in_set_num = (g_idx - 1) % 10 + 1
        set_start_pg = 180 + (set_num - 1) * 3
        if in_set_num <= 4:
            est_pg = set_start_pg
        elif in_set_num <= 8:
            est_pg = set_start_pg + 1
        else:
            est_pg = set_start_pg + 2
        if src == "excel":
            pg = infer_pdf_page(payload["passage"], set_start_pg, set_start_pg + 2, ocr_norm, est_pg)
            ov = {}
            if g_idx in PRACTICE_SET_OFFICIAL_EXPLANATIONS:
                ov["explanation"] = PRACTICE_SET_OFFICIAL_EXPLANATIONS[g_idx]
            spec = excel_item_to_spec(payload, pg, ov)
        else:
            spec = payload
        add_q(
            "Practice_Sets_All",
            spec,
            g_idx,
            f"Practice Set {set_num} - Câu {in_set_num}",
            "practice",
            f"S{set_num}_Q{in_set_num}",
        )

    # --- 17. APPENDIX: QUESTION MARKS & WORD PAIRS (1 Ex + 0 Practice = 1) ---
    add_q(
        "Appendix_QuestionMarks",
        excel_item_to_spec(ps_rows[42], 201, {"topic": "Appendix: Direct vs. Indirect Questions (Question Marks)"}),
        1,
        "Appendix - Ví dụ 1",
        "example",
        "Ex1",
    )

    # Assemble modules array with dynamic counts + question_ids
    for mod in MODULES_META:
        mod_qs = [q for q in all_questions if q["module_code"] == mod["code"]]
        ex_c = sum(1 for q in mod_qs if q["category"] == "example")
        pr_c = sum(1 for q in mod_qs if q["category"] == "practice")
        modules_out.append({
            **{k: mod[k] for k in ("id", "code", "chapter_num", "card_heading", "btn_label", "title", "short_title", "sub_title", "domain", "section", "time_minutes", "pdf_start_page", "strategy", "traps")},
            "book_start_page": mod["pdf_start_page"] - 2,
            "question_count": len(mod_qs),
            "example_count": ex_c,
            "practice_count": pr_c,
            "question_ids": [q["id"] for q in mod_qs],
        })

    total_ex = sum(1 for q in all_questions if q["category"] == "example")
    total_pr = sum(1 for q in all_questions if q["category"] == "practice")
    total_time = sum(m["time_minutes"] for m in modules_out)

    # Strict validation checks
    assert len(all_questions) == 334, f"Expected 334 total, got {len(all_questions)}"
    assert total_ex == 62, f"Expected 62 examples, got {total_ex}"
    assert total_pr == 272, f"Expected 272 practice, got {total_pr}"
    for q in all_questions:
        keys = [o["key"] for o in q["options"]]
        assert len(keys) in (2, 4) and len(keys) == len(set(keys)), f"Bad options on {q['master_id']}"
        assert all(o["text"] for o in q["options"]), f"Empty option text on {q['master_id']}"
        assert q["correct_answer"] in keys, f"Bad key {q['correct_answer']} on {q['master_id']}"
        assert 1 <= q["pdf_page"] <= 218 and q["book_page"] == q["pdf_page"] - 2, f"Bad page on {q['master_id']}"

    db_obj = {
        "test_title": "The Ultimate Guide to SAT Grammar (Erica Meltzer - 6th Edition)",
        "source_attribution": "Erica Lynn Meltzer - The Critical Reader: The Ultimate Guide to SAT Grammar (6th Edition, Digital SAT)",
        "credits": "Compiled and Enhanced by Mike Pham Bá Hong Son - Google for Education Innovator",
        "pdf_drive_id": PDF_DRIVE_ID,
        "pdf_path": PDF_PREVIEW,
        "pdf_drive_preview": PDF_PREVIEW,
        "pdf_drive_view": PDF_VIEW,
        "total_questions": len(all_questions),
        "total_examples": total_ex,
        "total_practice": total_pr,
        "time_minutes": total_time,
        "modules_count": len(modules_out),
        "structure_mode": "chapter_by_chapter_with_examples",
        "modules": modules_out,
        "questions": all_questions,
    }

    for folder in (DATA_DIR, STATIC_DATA_DIR):
        folder.mkdir(parents=True, exist_ok=True)
        for fname in ("erica_writing.json", "ericawriting.json"):
            out_path = folder / fname
            out_path.write_text(json.dumps(db_obj, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"Wrote {out_path} ({len(all_questions)} questions)")

    print("\n=== MODULE SUMMARY ===")
    for m in modules_out:
        print(f"  {m['code']:24s} | p.{m['pdf_start_page']:3d} (bk.{m['book_start_page']:3d}) | {m['question_count']:2d} Q ({m['example_count']:2d} ex + {m['practice_count']:2d} pr)")
    print(f"TOTAL: {len(all_questions)} questions ({total_ex} examples + {total_pr} practice) across {len(modules_out)} modules | {total_time} min")


if __name__ == "__main__":
    main()
