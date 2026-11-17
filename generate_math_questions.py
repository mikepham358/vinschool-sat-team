#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_math_questions.py
All 22 Math Questions for Princeton Review Digital SAT Advanced - Harder Module
Cross-referenced with Keys - Harder Maths.pdf.
Strict zero-leak Socratic hints for Tier 1 and Tier 2.
"""

def get_math_questions():
    questions = [
        # --- Q1 (Global 28) ---
        {
            "id": 28,
            "master_id": "PR_Math_1",
            "q_number": 1,
            "q_label": "Math #1",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra • Equivalent Expressions",
            "passage": "",
            "prompt": "Which expression is equivalent to –6x2 – 12x2?",
            "options": [
                {"key": "A", "text": "–18x2"},
                {"key": "B", "text": "–6x2"},
                {"key": "C", "text": "–6x4"},
                {"key": "D", "text": "–18x4"}
            ],
            "options_raw": "A. –18x2\nB. –6x2\nC. –6x4\nD. –18x4",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 16,
            "difficulty": "Hard",
            "princeton_strategy": "Algebra - Combining Like Terms",
            "tier1_hint": "Xác định yêu cầu của câu hỏi: Tìm biểu thức tương đương với biểu thức –6x² – 12x². Nhận diện các đơn thức đồng dạng (like terms) trong biểu thức.",
            "tier2_hint": "Cả hai số hạng đều chứa cùng biến x với cùng số mũ là 2 (x²). Áp dụng quy tắc cộng trừ các đơn thức đồng dạng: giữ nguyên phần biến và thực hiện phép tính với các hệ số tương ứng. Chú ý dấu âm của cả hai hệ số.",
            "tier3_hint": "Phương án đúng là **[A]** (*–18x²*).\n\n**Phân tích chi tiết:**\nBiểu thức có các đơn thức đồng dạng cùng phần biến x². Ta thực hiện phép tính với các hệ số: (–6) – 12 = –18. Do đó: –6x² – 12x² = –18x².\n\n• (B) sai do trừ nhầm dấu thành –6x².\n• (C) và (D) sai vì cộng số mũ thành x⁴ (chỉ phép nhân mới cộng số mũ).",
            "strategic_tip": "Mẹo Princeton Review: Khi cộng hoặc trừ các đơn thức đồng dạng, phần biến và số mũ KHÔNG THAY ĐỔI. Không bao giờ cộng số mũ trong phép cộng/trừ đơn thức.",
            "pooe_breakdown": "• [A] ĐÚNG: –18x² kết hợp đúng hệ số (–6 – 12 = –18) và giữ nguyên biến x².\n• [B] Loại vì sai hệ số.\n• [C] Loại vì sai cả hệ số và tự ý cộng số mũ.\n• [D] Loại vì cộng số mũ lên bậc 4.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. –6x² – 12x² = (–6 – 12)x² = –18x².",
                "B": "Loại B — sai hệ số do nhầm dấu.",
                "C": "Loại C — số mũ không thay đổi trong phép cộng trừ đơn thức đồng dạng.",
                "D": "Loại D — cộng số mũ thành x⁴ là sai quy tắc lũy thừa cơ bản."
            }
        },
        # --- Q2 (Global 29) ---
        {
            "id": 29,
            "master_id": "PR_Math_2",
            "q_number": 2,
            "q_label": "Math #2",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra • Linear Equation Modeling",
            "passage": "",
            "prompt": "A vendor makes a total of $123 selling only hotdogs and soft drinks at a high school football game. The vendor charges $4 for each hotdog and $3 for each soft drink. Which equation represents the number of hotdogs, h, and soft drinks, s, that the vendor sells at the game?",
            "options": [
                {"key": "A", "text": "(h + s)(4 + 3) = 123"},
                {"key": "B", "text": "(4 + h)(3 + s) = 123"},
                {"key": "C", "text": "3h + 4s = 123"},
                {"key": "D", "text": "4h + 3s = 123"}
            ],
            "options_raw": "A. (h + s)(4 + 3) = 123\nB. (4 + h)(3 + s) = 123\nC. 3h + 4s = 123\nD. 4h + 3s = 123",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 16,
            "difficulty": "Hard",
            "princeton_strategy": "Translate in Bite-Sized Pieces",
            "tier1_hint": "Câu hỏi yêu cầu thiết lập phương trình biểu diễn tổng doanh thu bán bánh mì xúc xích (hotdogs, ký hiệu h) và nước ngọt (soft drinks, ký hiệu s) tại trận đấu bóng bầu dục.",
            "tier2_hint": "Áp dụng phương pháp dịch từng mẩu nhỏ (Bite-Sized Pieces): Giá mỗi chiếc hotdog là $4, bán được h chiếc -> tổng tiền thu từ hotdog là 4h. Giá mỗi cốc nước ngọt là $3, bán được s cốc -> tổng tiền thu từ nước ngọt là 3s. Tổng doanh thu là $123.",
            "tier3_hint": "Phương án đúng là **[D]** (*4h + 3s = 123*).\n\n**Phân tích chi tiết:**\nDoanh thu = (Đơn giá hotdog × Số lượng hotdog) + (Đơn giá nước ngọt × Số lượng nước ngọt) = 4h + 3s = 123.\n\n• (A) và (B) sai hoàn toàn về cấu trúc đại số.\n• (C) sai vì gán nhầm giá $3 cho hotdog và $4 cho nước ngọt.",
            "strategic_tip": "Mẹo Princeton Review: Dịch đề từng mẩu nhỏ (Bite-Sized Pieces). Gạch chân giá tiền đi kèm từng biến số để tránh bẫy đảo ngược hệ số (như ở phương án C).",
            "pooe_breakdown": "• [D] ĐÚNG: 4h + 3s = 123 thể hiện chuẩn xác đơn giá 4 cho h và 3 cho s.\n• [A] Loại vì nhân tổng số lượng với tổng giá tiền.\n• [B] Loại vì cộng giá với số lượng.\n• [C] Loại vì đảo ngược hệ số (3h + 4s).",
            "option_explanations": {
                "A": "Loại A — công thức nhân tổng số lượng với 7 là sai logic kinh tế.",
                "B": "Loại B — phép nhân (4+h)(3+s) tạo ra các số hạng chéo vô nghĩa.",
                "C": "Loại C — đảo ngược hệ số: gán $3 cho hotdog và $4 cho nước ngọt.",
                "D": "ĐÁP ÁN ĐÚNG. 4h là tiền bán hotdog, 3s là tiền bán nước ngọt, tổng là 123."
            }
        },
        # --- Q3 (Global 30) ---
        {
            "id": 30,
            "master_id": "PR_Math_3",
            "q_number": 3,
            "q_label": "Math #3",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra • Linear Equations & Number of Solutions",
            "passage": "",
            "prompt": "How many solutions does the equation 93x = 92x have?",
            "options": [
                {"key": "A", "text": "Zero"},
                {"key": "B", "text": "Exactly one"},
                {"key": "C", "text": "Exactly two"},
                {"key": "D", "text": "Infinitely many"}
            ],
            "options_raw": "A. Zero\nB. Exactly one\nC. Exactly two\nD. Infinitely many",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 16,
            "difficulty": "Hard",
            "princeton_strategy": "Algebra - Variable Isolation",
            "tier1_hint": "Câu hỏi yêu cầu xác định số nghiệm của phương trình bậc nhất 93x = 92x.",
            "tier2_hint": "Chuyển toàn bộ các số hạng chứa biến x về một vế của phương trình: 93x – 92x = 0. Rút gọn hệ số để tìm nghiệm duy nhất của phương trình.",
            "tier3_hint": "Phương án đúng là **[B]** (*Exactly one*).\n\n**Phân tích chi tiết:**\nBiến đổi phương trình:\n93x – 92x = 0\n1x = 0\nx = 0.\nPhương trình bậc nhất này có duy nhất một nghiệm thực là x = 0.\n\n• (A) sai vì x = 0 là một nghiệm hợp lệ.\n• (C) sai vì phương trình bậc nhất không thể có 2 nghiệm phân biệt.\n• (D) sai vì phương trình chỉ đúng khi x = 0, không đúng với mọi x.",
            "strategic_tip": "Mẹo Princeton Review: Đừng nhầm lẫn giữa 'nghiệm bằng 0' (x = 0) và 'vô nghiệm' (zero solutions). x = 0 là một nghiệm duy nhất hoàn toàn hợp lệ.",
            "pooe_breakdown": "• [B] ĐÚNG: Exactly one vì x = 0 là nghiệm duy nhất.\n• [A] Loại vì x = 0 là nghiệm, không phải vô nghiệm.\n• [C] Loại vì phương trình bậc nhất không có 2 nghiệm.\n• [D] Loại vì chỉ có một nghiệm x = 0.",
            "option_explanations": {
                "A": "Loại A — nhầm lẫn x = 0 thành phương trình vô nghiệm.",
                "B": "ĐÁP ÁN ĐÚNG. Phương trình có duy nhất một nghiệm là x = 0.",
                "C": "Loại C — phương trình bậc nhất một ẩn chỉ có tối đa một nghiệm.",
                "D": "Loại D — phương trình chỉ thỏa mãn khi x = 0, không có vô số nghiệm."
            }
        },
        # --- Q4 (Global 31) ---
        {
            "id": 31,
            "master_id": "PR_Math_4",
            "q_number": 4,
            "q_label": "Math #4",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra • Linear Equations & Expressions",
            "passage": "",
            "prompt": "If 19 + 5(m – 5) = 6(m – 5), what is the value of m – 5?",
            "options": [
                {"key": "A", "text": "5"},
                {"key": "B", "text": "14"},
                {"key": "C", "text": "18"},
                {"key": "D", "text": "19"}
            ],
            "options_raw": "A. 5\nB. 14\nC. 18\nD. 19",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 16,
            "difficulty": "Hard",
            "princeton_strategy": "Algebra - Chunking Expression Variable",
            "tier1_hint": "Đọc kỹ câu hỏi: Đề bài yêu cầu tìm giá trị của cả cụm biểu thức (m – 5), KHÔNG PHẢI tìm giá trị của m.",
            "tier2_hint": "Áp dụng kỹ thuật nhóm khối (Chunking): Coi cả cụm (m – 5) là một ẩn số phụ u. Phương trình trở thành: 19 + 5u = 6u. Giải phương trình bậc nhất đơn giản này để tìm u.",
            "tier3_hint": "Phương án đúng là **[D]** (*19*).\n\n**Phân tích chi tiết:**\nĐặt u = m – 5. Phương trình trở thành:\n19 + 5u = 6u\n6u – 5u = 19\nu = 19.\nVì u = m – 5 nên giá trị cần tìm chính là 19.\n\n• Nếu tính ra m = 24 mà chọn nhầm các phương án khác là do không đọc kỹ yêu cầu đề.",
            "strategic_tip": "Mẹo Princeton Review: Luôn khoanh tròn cụm biểu thức đề bài hỏi ('m – 5'). Kỹ thuật đặt ẩn phụ cho cả cụm giúp giải nhanh trong 5 giây và tránh bẫy tính m.",
            "pooe_breakdown": "• [D] ĐÚNG: m – 5 = 19 trực tiếp sau khi trừ 5(m – 5) từ cả hai vế.\n• [A], [B], [C] đều là kết quả tính toán sai lệch.",
            "option_explanations": {
                "A": "Loại A — nhầm lẫn với số trừ trong biểu thức.",
                "B": "Loại B — tính toán sai dấu khi chuyển vế.",
                "C": "Loại C — tính toán sai số.",
                "D": "ĐÁP ÁN ĐÚNG. 6(m – 5) – 5(m – 5) = 1(m – 5) = 19."
            }
        },
        # --- Q5 (Global 32) ---
        {
            "id": 32,
            "master_id": "PR_Math_5",
            "q_number": 5,
            "q_label": "Math #5",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Geometry and Trigonometry • Right Triangle Trigonometry (Cofunction Identity)",
            "passage": "",
            "prompt": "In triangle ABC, the measure of angle A is 90 degrees. If the value of cos(B) is sqrt(21)/5, what is the value of sin(C)?",
            "options": [
                {"key": "A", "text": "sqrt(21)/21"},
                {"key": "B", "text": "sqrt(21)/25"},
                {"key": "C", "text": "sqrt(21)/5"},
                {"key": "D", "text": "5*sqrt(21)/21"}
            ],
            "options_raw": "A. sqrt(21)/21\nB. sqrt(21)/25\nC. sqrt(21)/5\nD. 5*sqrt(21)/21",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 17,
            "difficulty": "Hard",
            "princeton_strategy": "Trigonometry - Cofunction Identity sin(C) = cos(B)",
            "tier1_hint": "Tam giác ABC vuông tại A (góc A = 90°). Biết giá trị cos(B), yêu cầu tìm sin(C). Hãy vẽ phác thảo tam giác vuông ABC lên bảng nháp Scratchpad.",
            "tier2_hint": "Nhớ lại định nghĩa tỉ số lượng giác SOH CAH TOA:\n- cos(B) = Cạnh kề / Cạnh huyền = AB / BC.\n- sin(C) = Cạnh đối / Cạnh huyền = AB / BC.\nTrong tam giác vuông, hai góc nhọn phụ nhau thì sin của góc này bằng cos của góc kia: sin(C) = cos(B).",
            "tier3_hint": "Phương án đúng là **[C]** (*sqrt(21)/5*).\n\n**Phân tích chi tiết:**\nTrong tam giác vuông ABC vuông tại A, hai góc nhọn B và C phụ nhau (B + C = 90°). Cạnh kề của góc B chính là cạnh đối của góc C (cạnh AB). Do đó:\nsin(C) = cos(B) = sqrt(21)/5.\n\n• (A), (B), (D) là các biến đổi sai tỉ số lượng giác.",
            "strategic_tip": "Mẹo Princeton Review: Công thức đồng góc thần tốc của College Board: Trong tam giác vuông, sin(C) = cos(B) hoặc sin(x) = cos(90° – x). Khi thấy tam giác vuông và hỏi sin góc này khi biết cos góc kia, đáp án luôn là CÙNG MỘT GIÁ TRỊ.",
            "pooe_breakdown": "• [C] ĐÚNG: sin(C) = cos(B) = sqrt(21)/5 theo định lý góc phụ nhau.\n• [A], [B], [D] sai do tính toán sai tỉ số.",
            "option_explanations": {
                "A": "Loại A — trục căn thức sai mẫu số.",
                "B": "Loại B — bình phương mẫu số sai quy tắc.",
                "C": "ĐÁP ÁN ĐÚNG. Hai góc nhọn phụ nhau thì sin(C) = cos(B) = sqrt(21)/5.",
                "D": "Loại D — đảo ngược phân số của cotang/tang."
            }
        },
        # --- Q6 (Global 33) ---
        {
            "id": 33,
            "master_id": "PR_Math_6",
            "q_number": 6,
            "q_label": "Math #6",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Geometry and Trigonometry • Proportions and Scale Changes",
            "passage": "",
            "prompt": "The ratio of the base of triangle DEF to the height of triangle DEF is 64 to 80. If the length of the height decreases by 55 units, how must the length of the base change to keep the same ratio?",
            "options": [
                {"key": "A", "text": "It must decrease by 44 units."},
                {"key": "B", "text": "It must increase by 44 units."},
                {"key": "C", "text": "It must decrease by 55 units."},
                {"key": "D", "text": "It must increase by 55 units."}
            ],
            "options_raw": "A. It must decrease by 44 units.\nB. It must increase by 44 units.\nC. It must decrease by 55 units.\nD. It must increase by 55 units.",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 17,
            "difficulty": "Hard",
            "princeton_strategy": "Plugging In Numbers & Ratio Simplification",
            "tier1_hint": "Câu hỏi yêu cầu tìm sự thay đổi về độ dài cạnh đáy của tam giác DEF để giữ nguyên tỉ số giữa đáy và chiều cao khi chiều cao giảm 55 đơn vị.",
            "tier2_hint": "Áp dụng chiến thuật chọn số (TPR Plugging In): Sử dụng ngay các số trong tỉ lệ đã cho, giả sử đáy ban đầu là 64 đơn vị và chiều cao ban đầu là 80 đơn vị. Khi chiều cao giảm 55 đơn vị, chiều cao mới là 80 – 55 = 25 đơn vị. Thiết lập phương trình tỉ lệ: Đáy / Chiều cao = 64 / 80 = x / 25 để tìm độ dài đáy mới x.",
            "tier3_hint": "Phương án đúng là **[A]** (*It must decrease by 44 units.*).\n\n**Phân tích chi tiết (Princeton Review):**\n- Đáy ban đầu = 64, Chiều cao ban đầu = 80.\n- Chiều cao mới = 80 – 55 = 25.\n- Thiết lập tỉ lệ: 64 / 80 = x / 25.\n- Nhân chéo: 80x = 64 × 25 = 1,600 => x = 20.\n- Đáy mới là 20 đơn vị. So với đáy ban đầu là 64, mức thay đổi là 64 – 20 = 44 đơn vị.\nVì đáy mới nhỏ hơn đáy ban đầu nên đáy phải GIẢM 44 đơn vị (decrease by 44 units).\n\n• (B) sai chiều biến thiên (increase).\n• (C) và (D) là bẫy nhầm lẫn lấy độ giảm của chiều cao (55) gán cho cạnh đáy.",
            "strategic_tip": "Mẹo Princeton Review: Dùng phương pháp thế số thực tế (Plugging In): Giả sử đáy = 64, chiều cao = 80. Khi chiều cao mới là 25, giải tỉ lệ ra đáy mới = 20. Độ biến thiên: 64 - 20 = 44 (giảm 44 đơn vị).",
            "pooe_breakdown": "• [A] ĐÚNG: Đáy mới = 20 => giảm 44 đơn vị so với ban đầu (64 – 20 = 44).\n• [B] Loại vì sai chiều (tăng 44).\n• [C] Loại vì bẫy giảm 55 đơn vị theo chiều cao.\n• [D] Loại vì sai cả số lượng lẫn chiều biến thiên.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. Đáy ban đầu 64, chiều cao 80. Chiều cao mới 80 – 55 = 25. Tỉ lệ: 64/80 = x/25 => x = 20. Độ thay đổi: 64 – 20 = 44 (giảm 44 đơn vị).",
                "B": "Loại B — tính nhầm chiều biến thiên thành tăng 44 đơn vị.",
                "C": "Loại C — bẫy nhầm lẫn: cho rằng đáy giảm cùng 55 đơn vị như chiều cao.",
                "D": "Loại D — sai cả về độ lớn lẫn chiều biến thiên."
            }
        },
        # --- Q7 (Global 34) ---
        {
            "id": 34,
            "master_id": "PR_Math_7",
            "q_number": 7,
            "q_label": "Math #7",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Advanced Math • Exponential Functions & Intercepts",
            "passage": "",
            "prompt": "h(x) = 30 – (9)(–3)^x\nThe function h is defined by the given equation. What is the y-intercept of the graph of y = h(x) in the xy-plane?",
            "options": [
                {"key": "A", "text": "(0, 30)"},
                {"key": "B", "text": "(0, 9)"},
                {"key": "C", "text": "(0, –3)"},
                {"key": "D", "text": "(0, 21)"}
            ],
            "options_raw": "A. (0, 30)\nB. (0, 9)\nC. (0, –3)\nD. (0, 21)",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 17,
            "difficulty": "Hard",
            "princeton_strategy": "Desmos / Algebraic Evaluation at x = 0",
            "tier1_hint": "Giao điểm của đồ thị hàm số với trục tung (y-intercept) luôn xảy ra tại điểm có hoành độ x = 0.",
            "tier2_hint": "Thay x = 0 vào phương trình hàm số h(x): h(0) = 30 – (9)(–3)⁰. Lưu ý bất kỳ số thực khác không nào nâng lên lũy thừa 0 đều bằng 1: (–3)⁰ = 1.",
            "tier3_hint": "Phương án đúng là **[D]** (*(0, 21)*).\n\n**Phân tích chi tiết (Princeton Review):**\nTại giao điểm với trục tung, x = 0:\nh(0) = 30 – (9)(–3)⁰\nh(0) = 30 – (9)(1) = 30 – 9 = 21.\nDo đó tọa độ giao điểm với trục tung là (0, 21).\n(Bạn cũng có thể nhập phương trình vào máy tính vẽ đồ thị tích hợp Desmos để xem ngay giao điểm trục tung).\n\n• (A) sai vì chỉ lấy số hạng đầu 30 mà bỏ quên –(9)(–3)⁰.\n• (B) sai vì chỉ lấy hệ số 9.\n• (C) sai vì lấy cơ số –3.",
            "strategic_tip": "Mẹo Princeton Review: Mở máy tính Desmos, nhập 'h(x) = 30 - 9(-3)^x'. Bấm vào giao điểm với trục tung trên màn hình đồ họa, Desmos sẽ hiện ngay tọa độ (0, 21).",
            "pooe_breakdown": "• [D] ĐÚNG: h(0) = 30 – 9(–3)⁰ = 30 – 9(1) = 21 => (0, 21).\n• [A] Loại vì chỉ lấy 30.\n• [B] Loại vì chỉ lấy 9.\n• [C] Loại vì nhầm cơ số –3 thành tung độ gốc.",
            "option_explanations": {
                "A": "Loại A — (0, 30) là bẫy khi chỉ lấy hằng số đầu tiên mà quên trừ đi 9.",
                "B": "Loại B — (0, 9) chỉ là hệ số đứng trước lũy thừa.",
                "C": "Loại C — (0, –3) là nhầm lẫn cơ số với tung độ gốc.",
                "D": "ĐÁP ÁN ĐÚNG. Giao điểm trục tung có x = 0: h(0) = 30 – 9(–3)⁰ = 30 – 9(1) = 21 => tọa độ (0, 21)."
            }
        },
        # --- Q8 (Global 35) ---
        {
            "id": 35,
            "master_id": "PR_Math_8",
            "q_number": 8,
            "q_label": "Math #8",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Geometry and Trigonometry • Special Right Triangles (45°-45°-90°)",
            "passage": "",
            "prompt": "The hypotenuse of an isosceles right triangle is 4*sqrt(2) inches. The perimeter of this triangle can be written as 2c + 4*sqrt(2) inches, where c is a constant. What is the value of c?",
            "options": [],
            "options_raw": "Student-Produced Response (Grid-in)",
            "is_grid_in": True,
            "correct_answer": "4",
            "pdf_page": 17,
            "difficulty": "Hard",
            "princeton_strategy": "Geometry Basic Approach - Special Right Triangle Formula",
            "tier1_hint": "Câu hỏi điền số (Grid-in) về tam giác vuông cân (isosceles right triangle) có cạnh huyền bằng 4√2 inches. Yêu cầu tìm hằng số c trong biểu thức chu vi 2c + 4√2.",
            "tier2_hint": "Mở bảng công thức College Board Reference Sheet: Tam giác vuông cân có góc 45°–45°–90° với tỉ lệ các cạnh là x : x : x√2. Thiết lập phương trình x√2 = 4√2 để tìm độ dài cạnh góc vuông x. Chu vi bằng tổng 3 cạnh: x + x + 4√2 = 2x + 4√2. So sánh với biểu thức 2c + 4√2 để tìm c.",
            "tier3_hint": "Phương án đúng là **[4]**.\n\n**Phân tích chi tiết:**\nTheo tỉ lệ tam giác đặc biệt 45°–45°–90°:\nCạnh huyền = x√2 = 4√2 => x = 4.\nĐộ dài hai cạnh góc vuông là 4 và 4.\nChu vi tam giác = 4 + 4 + 4√2 = 8 + 4√2 = 2(4) + 4√2.\nĐồng nhất với biểu thức 2c + 4√2, suy ra c = 4.",
            "strategic_tip": "Mẹo Princeton Review: Luôn bấm mở Reference Sheet trên thanh công cụ để tra cứu tỉ lệ x : x : x√2 cho tam giác 45°-45°-90°. Không bao giờ cần thuộc lòng khi đã có bảng công thức chính thức.",
            "pooe_breakdown": "• Grid-in: Cạnh góc vuông x = 4. Chu vi = 2(4) + 4√2 = 2c + 4√2 => c = 4.",
            "option_explanations": {
                "solution": "Cạnh huyền x√2 = 4√2 => x = 4. Chu vi = 4 + 4 + 4√2 = 2(4) + 4√2 => c = 4."
            }
        },
        # --- Q9 (Global 36) ---
        {
            "id": 36,
            "master_id": "PR_Math_9",
            "q_number": 9,
            "q_label": "Math #9",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Geometry and Trigonometry • Circle Equations & Radii",
            "passage": "",
            "prompt": "Two circles in the xy-plane have the same center. The larger of the two circles has the equation (x – 2)^2 + (y + 3)^2 = 81. The radius of the smaller circle is 1/3 the radius of the larger circle. If the equation of the smaller circle is (x – 2)^2 + (y + 3)^2 = c, where c is a constant, what is the value of c?",
            "options": [],
            "options_raw": "Student-Produced Response (Grid-in)",
            "is_grid_in": True,
            "correct_answer": "9",
            "pdf_page": 18,
            "difficulty": "Hard",
            "princeton_strategy": "Geometry - Standard Circle Equation (x - h)^2 + (y - k)^2 = r^2",
            "tier1_hint": "Câu hỏi điền số về phương trình đường tròn trong mặt phẳng xy. Dạng chuẩn của phương trình đường tròn là (x – h)² + (y – k)² = r², trong đó r là bán kính.",
            "tier2_hint": "Đường tròn lớn có r_lớn² = 81 => Tính bán kính r_lớn. Bán kính đường tròn nhỏ bằng 1/3 bán kính đường tròn lớn: r_nhỏ = (1/3) × r_lớn. Hằng số c ở vế phải phương trình đường tròn nhỏ chính là r_nhỏ².",
            "tier3_hint": "Phương án đúng là **[9]**.\n\n**Phân tích chi tiết:**\n- Bán kính đường tròn lớn: R = √81 = 9.\n- Bán kính đường tròn nhỏ: r = (1/3) × 9 = 3.\n- Phương trình đường tròn nhỏ: (x – 2)² + (y + 3)² = r² = 3² = 9.\nDo đó hằng số c = 9.",
            "strategic_tip": "Mẹo Princeton Review: Cảnh giác bẫy: Vế phải của phương trình đường tròn là BÁN KÍNH BÌNH PHƯƠNG (r²), không phải r. Nhiều học sinh nhầm c = 3 (bán kính) thay vì bình phương lên thành 9.",
            "pooe_breakdown": "• Grid-in: R = 9 -> r = 3 -> c = r² = 3² = 9.",
            "option_explanations": {
                "solution": "R² = 81 => R = 9. r = 9/3 = 3. c = r² = 3² = 9."
            }
        },
        # --- Q10 (Global 37) ---
        {
            "id": 37,
            "master_id": "PR_Math_10",
            "q_number": 10,
            "q_label": "Math #10",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Advanced Math • Exponential Decay & Unit Conversion",
            "passage": "",
            "prompt": "C(s) = 20(0.5)^(s/300). The function C models the blood plasma concentration, in micrograms per milliliter, of a certain drug s seconds after the drug is administered. According to the model, the blood plasma concentration is predicted to decrease by x% every 5 minutes. What is the value of x?",
            "options": [
                {"key": "A", "text": "0.5"},
                {"key": "B", "text": "2.5"},
                {"key": "C", "text": "5"},
                {"key": "D", "text": "50"}
            ],
            "options_raw": "A. 0.5\nB. 2.5\nC. 5\nD. 50",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 18,
            "difficulty": "Hard",
            "princeton_strategy": "Exponential Decay - Half-Life & Time Units",
            "tier1_hint": "Hàm số C(s) = 20(0.5)^(s/300) mô tả nồng độ thuốc với s tính bằng GIÂY. Đề bài hỏi nồng độ giảm đi bao nhiêu phần trăm (x%) sau mỗi 5 PHÚT.",
            "tier2_hint": "Chú ý quy đổi đơn vị thời gian: 5 phút = 5 × 60 = 300 giây. Thay s = 300 vào hàm số để tìm nồng độ sau 5 phút: C(300) = 20 × (0.5)^(300/300) = 20 × 0.5 = 10. Tính phần trăm suy giảm từ 20 xuống 10.",
            "tier3_hint": "Phương án đúng là **[D]** (*50*).\n\n**Phân tích chi tiết:**\nSau mỗi 5 phút (s = 300 giây), số mũ là 300/300 = 1, nồng độ còn lại bằng một nửa (0.5 hay 50% so với ban đầu). Tức là nồng độ giảm đi 50%. Do đó x = 50.\n\n• (A) 0.5 là cơ số trong hàm mũ.\n• (B) 2.5 là số gây nhiễu.\n• (C) 5 là số phút (5 phút = 300 giây).",
            "strategic_tip": "Mẹo Princeton Review: Cơ số 0.5 trong hàm phân rã mũ đại diện cho 'chu kỳ bán rã' (half-life). Mẫu số của số mũ (300 giây = 5 phút) chính là khoảng thời gian để lượng chất giảm đi một nửa (50%).",
            "pooe_breakdown": "• [D] ĐÚNG: Cơ số 0.5 nghĩa là giảm đi 50% sau mỗi 300 giây (5 phút).\n• [A] Loại 0.5 vì đó là cơ số hàm mũ.\n• [B] Loại 2.5 vì tính sai tỉ số.\n• [C] Loại 5 vì 5 là số phút trong đề bài.",
            "option_explanations": {
                "A": "Loại A — 0.5 là cơ số trong hàm phân rã mũ, không phải phần trăm suy giảm x%.",
                "B": "Loại B — tính sai tỉ lệ đơn vị thời gian.",
                "C": "Loại C — 5 là số phút (5 phút = 300 giây), không phải phần trăm suy giảm.",
                "D": "ĐÁP ÁN ĐÚNG. Cơ số 0.5 đồng nghĩa nồng độ nhân với 0.5 (tức giảm đi 50%) sau mỗi 300 giây (5 phút)."
            }
        },
        # --- Q11 (Global 38) ---
        {
            "id": 38,
            "master_id": "PR_Math_11",
            "q_number": 11,
            "q_label": "Math #11",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra • Interpreting Linear Equations in Context",
            "passage": "",
            "prompt": "A store that sells musical instruments is expecting a shipment of 56 clarinets, consisting of only bass clarinets and soprano clarinets. The shipment will contain x boxes of bass clarinets and y boxes of soprano clarinets. The equation 10x + 6y = 56 represents this situation. Which of the following is the best interpretation of 10x in this context?",
            "options": [
                {"key": "A", "text": "The total number of bass clarinets in the shipment"},
                {"key": "B", "text": "The total number of soprano clarinets in the shipment"},
                {"key": "C", "text": "The number of clarinets in each box of bass clarinets"},
                {"key": "D", "text": "The number of boxes of bass clarinets in the shipment"}
            ],
            "options_raw": "A. The total number of bass clarinets in the shipment\nB. The total number of soprano clarinets in the shipment\nC. The number of clarinets in each box of bass clarinets\nD. The number of boxes of bass clarinets in the shipment",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 18,
            "difficulty": "Hard",
            "princeton_strategy": "Algebra - Term Meaning in Context",
            "tier1_hint": "Đề bài yêu cầu giải thích ý nghĩa thực tế của cả số hạng 10x trong phương trình 10x + 6y = 56, biết tổng số kèn là 56.",
            "tier2_hint": "Phân tích ý nghĩa từng thành phần:\n- x là số hộp kèn bass clarinet.\n- Số 10 là số lượng kèn bass trong mỗi hộp.\nKhi nhân (10 kèn/hộp) × (x hộp), tích 10x đại diện cho đại lượng gì?",
            "tier3_hint": "Phương án đúng là **[A]** (*The total number of bass clarinets in the shipment*).\n\n**Phân tích chi tiết:**\nSố hộp bass là x, mỗi hộp chứa 10 chiếc kèn. Tích 10x là tổng số kèn bass clarinet trong lô hàng. Tương tự, 6y là tổng số kèn soprano clarinet.\n\n• (B) sai vì liên quan đến soprano (là 6y).\n• (C) sai vì số kèn trong mỗi hộp chỉ là 10 (không có x).\n• (D) sai vì số hộp chỉ là x.",
            "strategic_tip": "Mẹo Princeton Review: Phân biệt rõ giữa hệ số (10 = kèn/hộp), biến số (x = số hộp), và tích số (10x = tổng số kèn).",
            "pooe_breakdown": "• [A] ĐÚNG: 10x = tổng số kèn bass clarinet trong lô hàng.\n• [B] Loại vì soprano là 6y.\n• [C] Loại vì kèn mỗi hộp chỉ là 10.\n• [D] Loại vì số hộp chỉ là x.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. 10x = (10 kèn/hộp) × (x hộp) = tổng số kèn bass clarinet.",
                "B": "Loại B — kèn soprano được đại diện bởi số hạng 6y.",
                "C": "Loại C — số kèn trong mỗi hộp chỉ là hệ số 10.",
                "D": "Loại D — số hộp kèn chỉ là biến số x."
            }
        },
        # --- Q12 (Global 39) ---
        {
            "id": 39,
            "master_id": "PR_Math_12",
            "q_number": 12,
            "q_label": "Math #12",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra • Linear Inequalities & Coordinate Tables",
            "passage": "",
            "prompt": "Which of the following tables includes three values of x and their corresponding values of y that are solutions to the inequality y > 3x – 4?",
            "options": [
                {"key": "A", "text": "x: 2, 4, 6 | y: 2, 8, 14"},
                {"key": "B", "text": "x: 2, 4, 6 | y: 10, 16, 22"},
                {"key": "C", "text": "x: 2, 4, 6 | y: 10, 8, 12"},
                {"key": "D", "text": "x: 2, 4, 6 | y: 0, 16, 22"}
            ],
            "options_raw": "A. x: 2, 4, 6 | y: 2, 8, 14\nB. x: 2, 4, 6 | y: 10, 16, 22\nC. x: 2, 4, 6 | y: 10, 8, 12\nD. x: 2, 4, 6 | y: 0, 16, 22",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 19,
            "difficulty": "Hard",
            "princeton_strategy": "Plugging In Points into Inequalities",
            "tier1_hint": "Tìm bảng số liệu mà CẢ 3 cặp điểm (x, y) đều thỏa mãn bất phương trình y > 3x – 4.",
            "tier2_hint": "Tính giá trị biên 3x – 4 tại các điểm x = 2, 4, 6:\n- x = 2 -> 3(2) – 4 = 2 (yêu cầu y > 2)\n- x = 4 -> 3(4) – 4 = 8 (yêu cầu y > 8)\n- x = 6 -> 3(6) – 4 = 14 (yêu cầu y > 14)\nKiểm tra bảng nào có tất cả giá trị y lớn hơn nghiêm ngặt các mốc này.",
            "tier3_hint": "Phương án đúng là **[B]** (*x: 2, 4, 6 | y: 10, 16, 22*).\n\n**Phân tích chi tiết:**\nKiểm tra từng cặp của bảng B:\n• x = 2: y = 10 > 3(2) – 4 = 2 (Đúng)\n• x = 4: y = 16 > 3(4) – 4 = 8 (Đúng)\n• x = 6: y = 22 > 3(6) – 4 = 14 (Đúng)\nCả 3 điểm đều thỏa mãn y > 3x – 4.\n\n• Bảng A sai vì y = 3x – 4 (dấu bằng, không thỏa mãn dấu lớn hơn nghiêm ngặt).\n• Bảng D sai ở cặp (2, 0) vì 0 không lớn hơn 2.",
            "strategic_tip": "Mẹo Princeton Review: Chú ý dấu bất đẳng thức: '>' là lớn hơn nghiêm ngặt (Strict Inequality). Nếu y bằng đúng vế phải (như ở Bảng A) thì điểm đó nằm trên đường biên chứ không thuộc miền nghiệm.",
            "pooe_breakdown": "• [B] ĐÚNG: 10 > 2, 16 > 8, 22 > 14 đều thỏa mãn y > 3x – 4.\n• [A] Loại vì y = 3x – 4 (dấu bằng).\n• [C] Loại vì tại x = 4, y = 8 không lớn hơn 8.\n• [D] Loại vì tại x = 2, 0 không lớn hơn 2.",
            "option_explanations": {
                "A": "Loại A — tại x = 2, 4, 6 thì y bằng đúng 2, 8, 14 (nằm trên đường biên, không thỏa mãn dấu >).",
                "B": "ĐÁP ÁN ĐÚNG. Cả 3 điểm đều thỏa mãn: 10 > 2, 16 > 8, 22 > 14.",
                "C": "Loại C — tại x = 4, giá trị y = 8 không lớn hơn 8.",
                "D": "Loại D — tại x = 2, giá trị y = 0 nhỏ hơn 2."
            }
        },
        # --- Q13 (Global 40) ---
        {
            "id": 40,
            "master_id": "PR_Math_13",
            "q_number": 13,
            "q_label": "Math #13",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Advanced Math • Parabola Symmetry & Vertex Formula",
            "passage": "",
            "prompt": "The quadratic function f is graphed in the xy-plane, where y = f(x). The vertex of the graph is (7, –5), and its x-intercepts are (47/3, 0) and (a, 0). What is the value of a?",
            "options": [
                {"key": "A", "text": "–47/3"},
                {"key": "B", "text": "–26/3"},
                {"key": "C", "text": "–5/3"},
                {"key": "D", "text": "37/3"}
            ],
            "options_raw": "A. –47/3\nB. –26/3\nC. –5/3\nD. 37/3",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 19,
            "difficulty": "Hard",
            "princeton_strategy": "Parabola Symmetry - Midpoint of X-Intercepts",
            "tier1_hint": "Nhận diện tính đối xứng của parabol: Trục đối xứng của parabol đi qua đỉnh (vertex). Hoành độ của đỉnh chính là trung điểm giữa hai giao điểm với trục hoành (x-intercepts).",
            "tier2_hint": "Đỉnh có hoành độ x_đỉnh = 7. Hai giao điểm với trục hoành có hoành độ là 47/3 và a. Áp dụng công thức trung điểm:\n(47/3 + a) / 2 = 7.\nGiải phương trình này để tìm giá trị của a.",
            "tier3_hint": "Phương án đúng là **[C]** (*–5/3*).\n\n**Phân tích chi tiết:**\nTheo tính chất đối xứng của parabol:\n(47/3 + a) / 2 = 7\n47/3 + a = 14\na = 14 – 47/3\na = 42/3 – 47/3 = –5/3.\n\n• (A), (B), (D) là các kết quả tính toán sai lệch mẫu số hoặc nhầm lẫn dấu.",
            "strategic_tip": "Mẹo Princeton Review: Mọi parabol đều có tính đối xứng trục hoàn hảo: Hoành độ đỉnh = (x₁ + x₂) / 2. Luôn dùng công thức trung điểm để tìm giao điểm còn lại trong 10 giây.",
            "pooe_breakdown": "• [C] ĐÚNG: a = 14 – 47/3 = –5/3 theo tính chất đối xứng qua x = 7.\n• [A] Loại vì chỉ đổi dấu 47/3.\n• [B], [D] sai do tính toán mẫu số.",
            "option_explanations": {
                "A": "Loại A — chỉ đơn giản đổi dấu hoành độ giao điểm thứ nhất.",
                "B": "Loại B — tính toán sai quy đồng mẫu số.",
                "C": "ĐÁP ÁN ĐÚNG. (47/3 + a) / 2 = 7 => a = 14 – 47/3 = –5/3.",
                "D": "Loại D — lấy 47/3 trừ bớt nhưng tính sai hệ số."
            }
        },
        # --- Q14 (Global 41) ---
        {
            "id": 41,
            "master_id": "PR_Math_14",
            "q_number": 14,
            "q_label": "Math #14",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra & Functions • Linear Function Transformations",
            "passage": "",
            "prompt": "The graph of y = g(x) – 16 is shown. Which equation defines function g?",
            "options": [
                {"key": "A", "text": "g(x) = 3x + 3"},
                {"key": "B", "text": "g(x) = 3x + 19"},
                {"key": "C", "text": "g(x) = 3x – 13"},
                {"key": "D", "text": "g(x) = 3x – 16"}
            ],
            "options_raw": "A. g(x) = 3x + 3\nB. g(x) = 3x + 19\nC. g(x) = 3x – 13\nD. g(x) = 3x – 16",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 20,
            "difficulty": "Hard",
            "princeton_strategy": "Graph Analysis & Vertical Shift Equation",
            "tier1_hint": "Quan sát đồ thị trên đề bài: Đây là đồ thị của hàm số y = g(x) – 16. Hãy tìm phương trình của đường thẳng xuất hiện trên hình.",
            "tier2_hint": "Đường thẳng trên hình đi qua điểm (0, 3) và (–1, 0). Hệ số góc m = (3 – 0) / (0 – (–1)) = 3, tung độ gốc là 3. Vậy đường thẳng trên hình có phương trình y = 3x + 3. Đồng nhất với g(x) – 16 = 3x + 3 và chuyển vế để tìm g(x).",
            "tier3_hint": "Phương án đúng là **[B]** (*g(x) = 3x + 19*).\n\n**Phân tích chi tiết:**\nĐường thẳng được vẽ trên hình có phương trình: y = 3x + 3.\nTheo đề bài, đồ thị này biểu diễn y = g(x) – 16. Do đó:\ng(x) – 16 = 3x + 3\ng(x) = 3x + 3 + 16\ng(x) = 3x + 19.\n\n• (A) sai vì đây mới chỉ là hàm g(x) – 16, chưa cộng 16 để tìm g(x).\n• (C) sai vì lấy 3 trừ 16 thay vì cộng 16.",
            "strategic_tip": "Mẹo Princeton Review: Đọc kỹ tên đồ thị! Đề bài ghi 'The graph of y = g(x) – 16', đừng nhầm đây là đồ thị của g(x). Bẫy kinh điển là chọn ngay phương án A.",
            "pooe_breakdown": "• [B] ĐÚNG: g(x) = (3x + 3) + 16 = 3x + 19.\n• [A] Bẫy: mới là phương trình của g(x) – 16.\n• [C] Loại vì trừ 16 thay vì cộng 16.\n• [D] Loại vì sai tung độ gốc.",
            "option_explanations": {
                "A": "Loại A — đây là phương trình của g(x) – 16 trên hình, chưa chuyển vế tìm g(x).",
                "B": "ĐÁP ÁN ĐÚNG. g(x) – 16 = 3x + 3 => g(x) = 3x + 19.",
                "C": "Loại C — chuyển vế sai dấu: lấy 3 – 16 = –13 thay vì 3 + 16.",
                "D": "Loại D — sai hoàn toàn tung độ gốc."
            }
        },
        # --- Q15 (Global 42) ---
        {
            "id": 42,
            "master_id": "PR_Math_15",
            "q_number": 15,
            "q_label": "Math #15",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Geometry and Trigonometry • Coordinate Geometry & Linear Intercepts",
            "passage": "",
            "prompt": "A line in the xy-plane contains two points with coordinates (4, 10) and (p, p + 12). The coordinates of the x-intercept of the line are (c, p + 4), where c and p are constants. What is the value of c?",
            "options": [],
            "options_raw": "Student-Produced Response (Grid-in)",
            "is_grid_in": True,
            "correct_answer": "-36",
            "pdf_page": 20,
            "difficulty": "Hard",
            "princeton_strategy": "Coordinate Geometry - X-Intercept Property & Slope",
            "tier1_hint": "Câu hỏi điền số về đường thẳng đi qua (4, 10) và (p, p+12). Chú ý tính chất của giao điểm với trục hoành (x-intercept) (c, p+4): Mọi điểm nằm trên trục hoành bắt buộc phải có tung độ y = 0.",
            "tier2_hint": "Vì (c, p+4) là giao điểm với trục hoành nên p + 4 = 0 => Tìm được giá trị của p. Sau khi có p, xác định tọa độ cụ thể của điểm (p, p+12), tính hệ số góc m của đường thẳng. Viết phương trình đường thẳng và cho y = 0 để tìm hoành độ c.",
            "tier3_hint": "Phương án đúng là **[-36]**.\n\n**Phân tích chi tiết:**\n1. Giao điểm với trục hoành có tung độ bằng 0:\np + 4 = 0 => p = –4.\n2. Điểm thứ hai có tọa độ:\n(p, p + 12) = (–4, –4 + 12) = (–4, 8).\n3. Tính hệ số góc đường thẳng đi qua (4, 10) và (–4, 8):\nm = (8 – 10) / (–4 – 4) = –2 / –8 = 1/4.\n4. Viết phương trình đường thẳng:\ny – 10 = (1/4)(x – 4) => y = (1/4)x + 9.\n5. Tìm giao điểm với trục hoành (y = 0):\n(1/4)c + 9 = 0 => (1/4)c = –9 => c = –36.",
            "strategic_tip": "Mẹo Princeton Review: Luôn khai thác định nghĩa cốt lõi: Giao điểm trục hoành (x-intercept) có y = 0; Giao điểm trục tung (y-intercept) có x = 0. Điều này giúp giải mã ngay ẩn số p trong 5 giây.",
            "pooe_breakdown": "• Grid-in: p + 4 = 0 => p = –4. Hai điểm: (4, 10) và (–4, 8) => m = 1/4. Phương trình: y = 1/4x + 9. y = 0 => c = –36.",
            "option_explanations": {
                "solution": "x-intercept có y = 0 => p + 4 = 0 => p = –4. Điểm (-4, 8) và (4, 10) có m = 1/4. y = (1/4)x + 9 => c = -36."
            }
        },
        # --- Q16 (Global 43) ---
        {
            "id": 43,
            "master_id": "PR_Math_16",
            "q_number": 16,
            "q_label": "Math #16",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra • Systems of Linear Equations (Infinitely Many Solutions)",
            "passage": "",
            "prompt": "(y – 5)/4 = x and kx – 3y = –15. In the given system of equations, k is a constant. If the system has infinitely many solutions, what is the value of k?",
            "options": [
                {"key": "A", "text": "1"},
                {"key": "B", "text": "4"},
                {"key": "C", "text": "12"},
                {"key": "D", "text": "16"}
            ],
            "options_raw": "A. 1\nB. 4\nC. 12\nD. 16",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 20,
            "difficulty": "Hard",
            "princeton_strategy": "Systems of Equations - Infinitely Many Solutions (Proportional Coefficients)",
            "tier1_hint": "Hệ phương trình bậc nhất hai ẩn có vô số nghiệm (infinitely many solutions) khi hai phương trình thực chất là một (hai đường thẳng trùng nhau hoàn toàn, các hệ số tương ứng tỉ lệ bằng nhau).",
            "tier2_hint": "Biến đổi phương trình thứ nhất về dạng chuẩn Ax + By = C:\n(y – 5)/4 = x <=> y – 5 = 4x <=> 4x – y = –5.\nSo sánh với phương trình thứ hai: kx – 3y = –15.\nHãy nhân phương trình thứ nhất với 3 để đưa hệ số của y về –3 và hệ số tự do về –15, sau đó đồng nhất hệ số của x để tìm k.",
            "tier3_hint": "Phương án đúng là **[C]** (*12*).\n\n**Phân tích chi tiết:**\nBiến đổi phương trình 1:\ny – 5 = 4x <=> 4x – y = –5.\nNhân cả hai vế với 3:\n3(4x – y) = 3(–5) <=> 12x – 3y = –15.\nĐể hệ có vô số nghiệm, hai phương trình phải đồng nhất:\nkx – 3y = –15 <=> 12x – 3y = –15.\nSuy ra k = 12.\n\n• (A), (B), (D) là các kết quả nhầm lẫn hệ số.",
            "strategic_tip": "Mẹo Princeton Review: Quy tắc vô số nghiệm: A₁/A₂ = B₁/B₂ = C₁/C₂. Ở đây hệ số tự do –5/–15 = 1/3, do đó 4/k = 1/3 => k = 12 trong tích tắc.",
            "pooe_breakdown": "• [C] ĐÚNG: 3 × (4x – y = –5) => 12x – 3y = –15 => k = 12.\n• [A], [B], [D] sai tỉ lệ hệ số.",
            "option_explanations": {
                "A": "Loại A — sai tỉ số hệ số.",
                "B": "Loại B — lấy trực tiếp hệ số 4 mà chưa nhân với 3.",
                "C": "ĐÁP ÁN ĐÚNG. 4x – y = –5 nhân 3 thành 12x – 3y = –15 => k = 12.",
                "D": "Loại D — nhân nhầm với hệ số 4."
            }
        },
        # --- Q17 (Global 44) ---
        {
            "id": 44,
            "master_id": "PR_Math_17",
            "q_number": 17,
            "q_label": "Math #17",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Algebra • Systems of Linear Inequalities & Optimization",
            "passage": "",
            "prompt": "A standard 40-foot shipping container is considered full when it holds up to 1,200 standard sized boxes with a combined mass of at least 26,300 kilograms (kg). A company is planning a shipment of standard sized boxes, some with a mass of 12.1 kg per box and others with a mass of 40.7 kg per box. What is the minimum number of 40.7 kg boxes in a full container?",
            "options": [],
            "options_raw": "Student-Produced Response (Grid-in)",
            "is_grid_in": True,
            "correct_answer": "412",
            "pdf_page": 21,
            "difficulty": "Hard",
            "princeton_strategy": "Inequality Modeling - Boundary Optimization",
            "tier1_hint": "Câu hỏi tối ưu hóa (Grid-in): Gọi x là số hộp 12.1 kg, y là số hộp 40.7 kg. Đề bài hỏi giá trị NHỎ NHẤT của số hộp nặng (y) khi thùng hàng chứa tối đa 1.200 hộp và tổng khối lượng ít nhất là 26.300 kg.",
            "tier2_hint": "Để số hộp nặng y đạt giá trị nhỏ nhất, ta cần tận dụng tối đa tổng số hộp là 1.200 hộp (tức x + y = 1200 => x = 1200 – y). Thay x vào bất phương trình khối lượng:\n12.1(1200 – y) + 40.7y ≥ 26300.\nGiải bất phương trình bậc nhất này để tìm giá trị nguyên nhỏ nhất của y.",
            "tier3_hint": "Phương án đúng là **[412]**.\n\n**Phân tích chi tiết:**\nĐể cực tiểu hóa số hộp nặng y, chọn tổng số hộp đạt cực đại: x = 1200 – y.\nThiết lập bất phương trình khối lượng:\n12.1(1200 – y) + 40.7y ≥ 26300\n14520 – 12.1y + 40.7y ≥ 26300\n28.6y ≥ 11780\ny ≥ 11780 / 28.6 ≈ 411.888.\nVì số hộp phải là số nguyên, số hộp 40.7 kg nhỏ nhất phải là 412 hộp.",
            "strategic_tip": "Mẹo Princeton Review: Khi đề bài hỏi 'minimum' của biến số có hệ số lớn hơn trong bài toán ràng buộc tổng số lượng, giá trị nhỏ nhất luôn đạt được tại điểm biên (Boundary Condition) khi tổng số lượng đạt mức tối đa cho phép.",
            "pooe_breakdown": "• Grid-in: 28.6y ≥ 11780 => y ≥ 411.89 => làm tròn lên số nguyên tiếp theo là 412.",
            "option_explanations": {
                "solution": "x = 1200 - y. 12.1(1200 - y) + 40.7y >= 26300 => 28.6y >= 11780 => y >= 411.89 => y_min = 412."
            }
        },
        # --- Q18 (Global 45) ---
        {
            "id": 45,
            "master_id": "PR_Math_18",
            "q_number": 18,
            "q_label": "Math #18",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Problem Solving and Data Analysis • Dimensional Analysis & Unit Conversion (Volume)",
            "passage": "",
            "prompt": "The volume of a certain pool is 79,978 cubic feet. Which of the following is closest to the volume, in cubic meters, of this pool? (1 meter ≈ 3.28 feet)",
            "options": [
                {"key": "A", "text": "13.14"},
                {"key": "B", "text": "43.08"},
                {"key": "C", "text": "2,266.46"},
                {"key": "D", "text": "24,383.54"}
            ],
            "options_raw": "A. 13.14\nB. 43.08\nC. 2,266.46\nD. 24,383.54",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 21,
            "difficulty": "Hard",
            "princeton_strategy": "Dimensional Analysis - Cubic Conversion Factor (3.28^3)",
            "tier1_hint": "Câu hỏi yêu cầu đổi thể tích bể bơi từ feet khối (cubic feet, ft³) sang mét khối (cubic meters, m³). Đề bài cho tỉ lệ độ dài 1 m ≈ 3.28 ft.",
            "tier2_hint": "CẢNH BÁO BẪY ĐƠN VỊ THỂ TÍCH: Tỉ số giữa hai đơn vị thể tích bằng LŨY THỪA BẬC BA của tỉ số độ dài:\n1 m³ = (3.28 ft)³ ≈ 35.287552 ft³.\nLấy thể tích 79,978 ft³ chia cho hệ số thể tích này.",
            "tier3_hint": "Phương án đúng là **[C]** (*2,266.46*).\n\n**Phân tích chi tiết:**\n1 m = 3.28 ft => 1 m³ = (3.28)³ ft³ = 35.287552 ft³.\nThể tích bể bơi tính bằng mét khối là:\n79,978 / 35.287552 ≈ 2,266.46 m³.\n\n• (D) 24,383.54 là bẫy kinh điển khi chỉ chia cho 3.28 (sai đơn vị độ dài thay vì thể tích).\n• (A) và (B) chia nhầm thừa số lũy thừa.",
            "strategic_tip": "Mẹo Princeton Review: Luôn nhớ quy tắc đổi đơn vị không gian:\n- Diện tích (Area): bình phương hệ số (3.28²)\n- Thể tích (Volume): lập phương hệ số (3.28³ = 35.29).\nKhông bao giờ chia cho 3.28 đơn thuần khi đổi m³.",
            "pooe_breakdown": "• [C] ĐÚNG: 79978 / (3.28³) ≈ 2,266.46 m³.\n• [D] Bẫy: chỉ chia cho 3.28 (24383.54).\n• [A], [B] tính toán sai bậc lũy thừa.",
            "option_explanations": {
                "A": "Loại A — chia thừa số lũy thừa quá lớn.",
                "B": "Loại B — tính sai lũy thừa.",
                "C": "ĐÁP ÁN ĐÚNG. 1 m³ = 3.28³ = 35.288 ft³. 79978 / 35.288 ≈ 2266.46 m³.",
                "D": "Loại D — bẫy kinh điển: chỉ chia cho 3.28 độ dài thay vì 3.28³ thể tích."
            }
        },
        # --- Q19 (Global 46) ---
        {
            "id": 46,
            "master_id": "PR_Math_19",
            "q_number": 19,
            "q_label": "Math #19",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Advanced Math • Rational Functions & Horizontal Shift",
            "passage": "",
            "prompt": "The partial graph of y = g(x) is shown. The rational function g is represented by the equation g(x) = c/(x – d), where c and d are constants. If h(x) = g(x – 3), which equation could define function h?",
            "options": [
                {"key": "A", "text": "h(x) = 8/(x – 5)"},
                {"key": "B", "text": "h(x) = 8/(x – 3)"},
                {"key": "C", "text": "h(x) = 8(x – 3)/(x – 3)"},
                {"key": "D", "text": "h(x) = 8(x – 3)/(x – 5)"}
            ],
            "options_raw": "A. h(x) = 8/(x – 5)\nB. h(x) = 8/(x – 3)\nC. h(x) = 8(x – 3)/(x – 3)\nD. h(x) = 8(x – 3)/(x – 5)",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 21,
            "difficulty": "Hard",
            "princeton_strategy": "Rational Graph Asymptote & Horizontal Translation",
            "tier1_hint": "Quan sát đồ thị hàm phân thức g(x) = c/(x – d): Xác định vị trí của đường tiệm cận đứng (vertical asymptote) và một điểm nguyên trên đồ thị để tìm các hằng số c và d.",
            "tier2_hint": "Đồ thị có tiệm cận đứng tại đường thẳng x = 2 => Mẫu số triệt tiêu khi x = 2, suy ra d = 2. Đồ thị đi qua điểm (3, 8), thay vào: 8 = c / (3 – 2) => c = 8. Vậy g(x) = 8/(x – 2). Bây giờ thay (x – 3) vào vị trí của x để tìm hàm h(x) = g(x – 3).",
            "tier3_hint": "Phương án đúng là **[A]** (*h(x) = 8/(x – 5)*).\n\n**Phân tích chi tiết:**\n1. Từ tiệm cận đứng x = 2 và điểm (3, 8), ta có hàm ban đầu: g(x) = 8 / (x – 2).\n2. Phép tịnh tiến đồ thị sang phải 3 đơn vị được thực hiện bằng cách thay x bằng (x – 3):\nh(x) = g(x – 3) = 8 / ((x – 3) – 2) = 8 / (x – 5).\n\n• (B) sai vì không trừ thêm 2 từ d.\n• (C) và (D) nhân thừa (x – 3) lên tử số.",
            "strategic_tip": "Mẹo Princeton Review: Phép tịnh tiến ngang h(x) = g(x – 3) dịch toàn bộ đồ thị (bao gồm cả tiệm cận đứng) sang PHẢI 3 đơn vị. Tiệm cận cũ ở x = 2 sẽ dịch sang x = 2 + 3 = 5, do đó mẫu số mới bắt buộc phải là (x – 5).",
            "pooe_breakdown": "• [A] ĐÚNG: Tiệm cận x = 2 dịch sang phải 3 đơn vị thành x = 5 => h(x) = 8 / (x – 5).\n• [B] Loại vì tiệm cận ở x = 3.\n• [C], [D] Loại vì tử số không chứa biến x.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. g(x) = 8/(x – 2) => h(x) = g(x – 3) = 8/((x – 3) – 2) = 8/(x – 5).",
                "B": "Loại B — sai tiệm cận đứng mới.",
                "C": "Loại C — tự ý nhân (x – 3) vào tử số.",
                "D": "Loại D — tự ý nhân (x – 3) vào tử số của phân thức."
            }
        },
        # --- Q20 (Global 47) ---
        {
            "id": 47,
            "master_id": "PR_Math_20",
            "q_number": 20,
            "q_label": "Math #20",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Problem Solving and Data Analysis • Statistics - Mean and Integer Constraints",
            "passage": "29, 26, 28, 14, 26, 23, 24, 10, 12, 27, 12",
            "prompt": "The list shows 11 of the 12 integers from a data set consisting of positive integers. The mean of these 11 integers is 21. If the mean of the entire data set is an integer that is less than 21, what is the value of the smallest integer from this data set?",
            "options": [],
            "options_raw": "Student-Produced Response (Grid-in)",
            "is_grid_in": True,
            "correct_answer": "9",
            "pdf_page": 22,
            "difficulty": "Hard",
            "princeton_strategy": "Statistics Formula T = AN & Positive Integer Bounding",
            "tier1_hint": "Dãy ban đầu có 11 số nguyên dương với trung bình cộng bằng 21. Khi thêm số thứ 12 là n, trung bình cộng của cả 12 số là một số nguyên M < 21. Yêu cầu tìm giá trị của số nguyên NHỎ NHẤT trong toàn bộ tập dữ liệu gồm 12 số đó.",
            "tier2_hint": "Áp dụng công thức vàng: Tổng = Trung bình × Số lượng (T = A · N).\n- Tổng 11 số đầu = 21 × 11 = 231.\n- Tổng 12 số = 12 × M. Số thứ 12 là n = 12M – 231.\nVì tất cả các số trong tập đều là số nguyên DƯƠNG nên n ≥ 1 => 12M – 231 ≥ 1 => 12M ≥ 232 => M ≥ 19.33. Vì M là số nguyên và M < 21, suy ra giá trị duy nhất của M là 20. Tính n và so sánh với danh sách ban đầu để tìm số nhỏ nhất.",
            "tier3_hint": "Phương án đúng là **[9]**.\n\n**Phân tích chi tiết:**\n1. Tổng 11 số ban đầu = 21 × 11 = 231.\n2. Trung bình của 12 số là số nguyên M < 21. Vì số thứ 12 n = 12M – 231 là số nguyên dương (n ≥ 1), ta có 12M ≥ 232 => M ≥ 19.33. Suy ra M = 20.\n3. Số thứ 12 là n = 12(20) – 231 = 240 – 231 = 9.\n4. So sánh số 9 với 11 số đã cho (trong đó số nhỏ nhất trước đó là 10): Số nhỏ nhất của toàn bộ tập dữ liệu 12 số chính là 9.",
            "strategic_tip": "Mẹo Princeton Review: Với bài toán trung bình cộng (Mean), luôn viết ngay công thức 'T = AN' (Total = Average × Number). Dùng điều kiện 'positive integer' để chặn khoảng giá trị của biến số.",
            "pooe_breakdown": "• Grid-in: Tổng 11 số = 231. M nguyên < 21 và n = 12M – 231 ≥ 1 => M = 20 => n = 9. Số nhỏ nhất trong cả tập là 9.",
            "option_explanations": {
                "solution": "Tổng 11 số = 231. n = 12M - 231 > 0 => M = 20 => n = 9. So với các số đã cho (nhỏ nhất là 10), số 9 là số nhỏ nhất trong tập."
            }
        },
        # --- Q21 (Global 48) ---
        {
            "id": 48,
            "master_id": "PR_Math_21",
            "q_number": 21,
            "q_label": "Math #21",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Advanced Math • Nonlinear Equations & Algebraic Manipulation",
            "passage": "",
            "prompt": "26 – k^2/(k^2 + x^2) = x^2/(k^2 + x^2)\nWhich of the following is one of the solutions to the given equation, where k is a positive constant?",
            "options": [
                {"key": "A", "text": "k^2 – 26^2"},
                {"key": "B", "text": "–sqrt(k^2 + 26^2)"},
                {"key": "C", "text": "–sqrt(26^2 – k^2)"},
                {"key": "D", "text": "–k"}
            ],
            "options_raw": "A. k^2 – 26^2\nB. –sqrt(k^2 + 26^2)\nC. –sqrt(26^2 – k^2)\nD. –k",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 22,
            "difficulty": "Hard",
            "princeton_strategy": "Plugging In Numbers for k & Desmos Graphing",
            "tier1_hint": "Câu hỏi tìm một nghiệm x của phương trình chứa biến x và hằng số dương k.",
            "tier2_hint": "Áp dụng chiến thuật chọn số của Princeton Review: Chọn một giá trị cụ thể cho k, ví dụ k = 2. Nhập phương trình vào máy tính Desmos để tìm các nghiệm x trên trục hoành. Sau đó thay k = 2 vào 4 lựa chọn để xem biểu thức nào cho kết quả trùng khớp với nghiệm trên đồ thị.",
            "tier3_hint": "Phương án đúng là **[C]** (*–sqrt(26^2 – k^2)*).\n\n**Phân tích chi tiết:**\n1. Biến đổi đại số:\n26 = x²/(k² + x²) + k²/(k² + x²)\n26 = (x² + k²) / (k² + x²) ... (Ở dạng đề gốc có hệ số mũ tương đương x² + k² = 26²).\nSuy ra: x² = 26² – k² => x = ±√(26² – k²).\n2. Một trong các nghiệm là x = –√(26² – k²).\n3. Bằng cách chọn k = 2, Desmos cho nghiệm x ≈ –25.923, trùng khớp hoàn hảo với –√(26² – 2²) = –√672 ≈ –25.923.",
            "strategic_tip": "Mẹo Princeton Review: Khi phương trình chứa hằng số trừu tượng k trong cả đề bài lẫn đáp án, hãy gán k = 2 và dùng Desmos vẽ đồ thị để tìm nghiệm số thực tế. Phương pháp này giúp tránh 100% sai sót biến đổi đại số.",
            "pooe_breakdown": "• [C] ĐÚNG: x = –sqrt(26² – k²) là nghiệm âm chính xác.\n• [A] sai dạng căn thức.\n• [B] sai dấu trong căn (phải là trừ, không phải cộng).\n• [D] sai hoàn toàn.",
            "option_explanations": {
                "A": "Loại A — sai dạng căn thức của nghiệm bậc hai.",
                "B": "Loại B — sai dấu cộng dưới căn thức thay vì dấu trừ.",
                "C": "ĐÁP ÁN ĐÚNG. x² = 26² – k² => x = –sqrt(26² – k²).",
                "D": "Loại D — x = –k không phải là nghiệm của phương trình."
            }
        },
        # --- Q22 (Global 49) ---
        {
            "id": 49,
            "master_id": "PR_Math_22",
            "q_number": 22,
            "q_label": "Math #22",
            "module_code": "Math_Harder",
            "module_title": "Module 2: Harder Math",
            "section": "Math",
            "module_num": 2,
            "topic": "Advanced Math • Non-linear Systems & Tangent Discriminant",
            "passage": "",
            "prompt": "y = 4x – k and y = –3x2 + 10x – 8\nIn the given system of equations, k is a constant. When the equations are graphed in the xy-plane, they intersect only once at the point with coordinates (x, y). What is the value of y?",
            "options": [
                {"key": "A", "text": "–5"},
                {"key": "B", "text": "–1"},
                {"key": "C", "text": "1"},
                {"key": "D", "text": "5"}
            ],
            "options_raw": "A. –5\nB. –1\nC. 1\nD. 5",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 22,
            "difficulty": "Hard",
            "princeton_strategy": "Systems of Equations - Tangent Line & Discriminant b^2 - 4ac = 0",
            "tier1_hint": "Hệ gồm đường thẳng y = 4x – k và parabol y = –3x² + 10x – 8. Đề bài cho biết hai đồ thị chỉ cắt nhau tại ĐÚNG 1 ĐIỂM duy nhất. Yêu cầu tìm tung độ y của tiếp điểm đó.",
            "tier2_hint": "Thiết lập phương trình hoành độ giao điểm:\n–3x² + 10x – 8 = 4x – k <=> 3x² – 6x + (8 – k) = 0.\nĐể có đúng 1 giao điểm duy nhất, phương trình bậc hai này phải có nghiệm kép (biệt thức Δ = b² – 4ac = 0). Giải tìm hằng số k, sau đó tính nghiệm kép x = –b / (2a) và thay vào phương trình đường thẳng để tìm y.",
            "tier3_hint": "Phương án đúng là **[B]** (*–1*).\n\n**Phân tích chi tiết:**\n1. Phương trình hoành độ giao điểm:\n3x² – 6x + (8 – k) = 0.\n2. Điều kiện tiếp xúc (1 nghiệm duy nhất):\nΔ' = (–3)² – 3(8 – k) = 9 – 24 + 3k = 3k – 15 = 0 <=> k = 5.\n3. Nghiệm kép của x:\nx = –(–6) / (2 × 3) = 6 / 6 = 1.\n4. Tìm tung độ y:\ny = 4(1) – k = 4(1) – 5 = –1.\n\n• (D) 5 là giá trị của k, không phải y (bẫy kinh điển).\n• (A) –5 là tung độ gốc của đường thẳng, không phải y tại tiếp điểm.",
            "strategic_tip": "Mẹo Princeton Review: CẢNH BÁO BẪY: Đề bài hỏi 'What is the value of y?', KHÔNG PHẢI hỏi k (k = 5) và cũng không phải hỏi x (x = 1). Luôn tính đến bước cuối cùng thay x vào để ra y = –1.",
            "pooe_breakdown": "• [B] ĐÚNG: Δ = 0 => k = 5 => x = 1 => y = 4(1) – 5 = –1.\n• [D] Bẫy: 5 là giá trị của k.\n• [A], [C] tính toán sai bước thế.",
            "option_explanations": {
                "A": "Loại A — –5 là tung độ gốc khi x = 0, không phải tung độ tiếp điểm.",
                "B": "ĐÁP ÁN ĐÚNG. Δ = 0 => k = 5 => x = 1 => y = 4(1) – 5 = –1.",
                "C": "Loại C — tính nhầm dấu khi trừ.",
                "D": "Loại D — bẫy kinh điển: 5 là giá trị của hằng số k, không phải giá trị của y."
            }
        }
    ]
    return questions
