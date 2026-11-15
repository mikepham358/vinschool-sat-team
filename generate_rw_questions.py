#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_rw_questions.py
All 27 Reading & Writing Questions for Princeton Review Digital SAT Advanced - Harder Module
Cross-referenced with Keys - Harder Verbal.pdf.
Strict zero-leak Socratic hints for Tier 1 and Tier 2.
"""

def get_rw_questions():
    questions = [
        # --- Q1 ---
        {
            "id": 1,
            "master_id": "PR_RW_1",
            "q_number": 1,
            "q_label": "RW #1",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Craft and Structure • Words in Context (Precision)",
            "passage": "UC Berkeley research scientist Eti Ben Simon and UC Berkeley professor of psychology Matthew Walker led a study showing that lack of sleep can ________ the propensity towards altruistic behavior in people. Simon and Walker found that study participants who experienced poor sleep were less willing to help others the following day.",
            "prompt": "Which choice completes the text with the most logical and precise word or phrase?",
            "options": [
                {"key": "A", "text": "elevate"},
                {"key": "B", "text": "hinder"},
                {"key": "C", "text": "develop"},
                {"key": "D", "text": "assist"}
            ],
            "options_raw": "A. elevate\nB. hinder\nC. develop\nD. assist",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 2,
            "difficulty": "Hard",
            "princeton_strategy": "POOE - Contextual Clues & Tone Matching",
            "tier1_hint": "Xác định vai trò của động từ cần điền mô tả mối tương quan giữa tình trạng thiếu ngủ và xu hướng hành động vị tha (altruistic behavior). Đọc kỹ câu văn tiếp theo để tìm dẫn chứng trực tiếp về thái độ của người thiếu ngủ.",
            "tier2_hint": "Chú ý chi tiết 'less willing to help others the following day' (ít sẵn lòng giúp đỡ người khác hơn). Xu hướng giúp đỡ bị giảm đi, do đó cần một động từ mang nghĩa 'làm giảm' hoặc 'cản trở'. Áp dụng kỹ thuật POOE: loại trừ các từ mang sắc thái tích cực (ngược hướng).",
            "tier3_hint": "Phương án đúng là **[B]** (*hinder*).\n\n**Phân tích chi tiết:**\nĐoạn văn chỉ ra rằng người thiếu ngủ ít sẵn lòng giúp đỡ người khác vào ngày hôm sau, tức là sự thiếu ngủ làm suy giảm/cản trở lòng vị tha. Từ 'hinder' (cản trở/làm suy giảm) khớp hoàn hảo với nghĩa 'diminish/reduce'.\n\n• (A) *elevate* (nâng cao), (C) *develop* (phát triển), và (D) *assist* (hỗ trợ) đều sai vì mang sắc thái tích cực ngược lại (Opposite Tone).",
            "strategic_tip": "Mẹo Princeton Review (Vocabulary): Luôn gạch chân manh mối ngữ cảnh (contextual clue) trong câu trước khi nhìn các lựa chọn. Dự đoán một từ đồng nghĩa đơn giản (như 'reduce') rồi dùng POOE loại trừ các từ trái nghĩa.",
            "pooe_breakdown": "• [B] ĐÚNG: hinder (cản trở/làm giảm) phản ánh chính xác việc ít sẵn lòng giúp đỡ người khác.\n• [A] Loại elevate (nâng cao) vì mang nghĩa tích cực ngược chiều.\n• [C] Loại develop (phát triển) vì không hợp logic bị thiếu ngủ.\n• [D] Loại assist (hỗ trợ) vì mang sắc thái tích cực.",
            "option_explanations": {
                "A": "Loại A — elevate (nâng cao) mang nghĩa tích cực, ngược với dẫn chứng 'less willing to help'.",
                "B": "ĐÁP ÁN ĐÚNG. hinder (cản trở/làm suy giảm) khớp hoàn hảo với dẫn chứng người thiếu ngủ ít sẵn lòng giúp đỡ người khác.",
                "C": "Loại C — develop (phát triển) mang nghĩa tăng cường, ngược với logic thực nghiệm.",
                "D": "Loại D — assist (hỗ trợ/giúp đỡ) mang nghĩa tích cực, trái ngược hoàn toàn với ngữ cảnh thiếu ngủ gây hại."
            }
        },
        # --- Q2 ---
        {
            "id": 2,
            "master_id": "PR_RW_2",
            "q_number": 2,
            "q_label": "RW #2",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Craft and Structure • Words in Context (Tone & Contrast)",
            "passage": "In a recent Duke University study, subjects expressing more curiosity about the outcome of a video were less likely, not more likely as expected by researchers, to use a provided ‘spoiler’ button to skip to the video’s conclusion than were subjects reporting indifference. In response to these findings, lead researcher Johnny Hsiung noted that while human curiosity has been heavily studied, it remains poorly understood.",
            "prompt": "Which choice completes the text with the most logical and precise word or phrase?",
            "options": [
                {"key": "A", "text": "unprecedented"},
                {"key": "B", "text": "ambivalent"},
                {"key": "C", "text": "paradoxical"},
                {"key": "D", "text": "vague"}
            ],
            "options_raw": "A. unprecedented\nB. ambivalent\nC. paradoxical\nD. vague",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 2,
            "difficulty": "Hard",
            "princeton_strategy": "POOE - Contextual Clues & Extreme Language Trap",
            "tier1_hint": "Câu hỏi từ vựng yêu cầu tìm tính từ miêu tả bản chất kết quả nghiên cứu của Đại học Duke. Hãy đối chiếu kỳ vọng ban đầu của các nhà nghiên cứu với hành vi thực tế của đối tượng tham gia.",
            "tier2_hint": "Chú ý sự tương phản: những người tò mò hơn đáng lẽ phải bấm nút xem trước ('spoiler'), nhưng thực tế họ lại 'less likely, not more likely' (ít bấm hơn). Đây là một kết quả mâu thuẫn trái ngược với logic thông thường. Cần một từ mang nghĩa 'trái ngược/nghịch lý'.",
            "tier3_hint": "Phương án đúng là **[C]** (*paradoxical*).\n\n**Phân tích chi tiết:**\nNghiên cứu phát hiện người tò mò về kết quả video lại ít có xu hướng xem trước, trái ngược với kỳ vọng ban đầu của các nhà khoa học. Từ 'paradoxical' (nghịch lý/mâu thuẫn bề ngoài) mô tả chính xác phát hiện này.\n\n• (A) *unprecedented* (chưa từng có tiền lệ) sai vì là Extreme Language (ngôn từ cực đoan không có bằng chứng).\n• (B) *ambivalent* (lưỡng lự) sai vì là Recycled Language (lạm dụng sai từ 'indifference' trong bài).\n• (D) *vague* (mơ hồ) sai vì kết quả nghiên cứu rất rõ ràng, không hề mơ hồ.",
            "strategic_tip": "Mẹo Princeton Review: Cảnh giác với bẫy 'Extreme Language' (như unprecedented, never, always) khi bài đọc chỉ là một nghiên cứu thực nghiệm thông thường.",
            "pooe_breakdown": "• [C] ĐÚNG: paradoxical (nghịch lý) mô tả kết quả mâu thuẫn giữa kỳ vọng và thực tế.\n• [A] Loại unprecedented vì quá cực đoan (Extreme Language).\n• [B] Loại ambivalent vì dùng sai nghĩa từ indifference.\n• [D] Loại vague vì số liệu rất rõ ràng, không mơ hồ.",
            "option_explanations": {
                "A": "Loại A — unprecedented là Extreme Language; bài đọc không khẳng định trước đây chưa từng có nghiên cứu nào tìm ra kết quả tương tự.",
                "B": "Loại B — ambivalent là Recycled Language; từ này lạm dụng chữ 'indifference' nhưng sai chủ thể miêu tả kết quả.",
                "C": "ĐÁP ÁN ĐÚNG. paradoxical (nghịch lý) miêu tả hoàn hảo kết quả 'càng tò mò thì càng ít bấm xem trước'.",
                "D": "Loại D — vague (mơ hồ) sai vì số liệu thực nghiệm đưa ra rất rõ ràng và chuẩn xác."
            }
        },
        # --- Q3 ---
        {
            "id": 3,
            "master_id": "PR_RW_3",
            "q_number": 3,
            "q_label": "RW #3",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Craft and Structure • Words in Context (Domain Precision)",
            "passage": "While there is disagreement about whether the Water Tribunal of Spain dates from Roman times or centuries later during the Spanish Caliphate, it is widely recognized as the world’s oldest court and thus remains a significant topic of study for anyone looking to understand the history of judicial bodies that have ________ cases related to water use or irrigation.",
            "prompt": "Which choice completes the text with the most logical and precise word or phrase?",
            "options": [
                {"key": "A", "text": "dismissed"},
                {"key": "B", "text": "validated"},
                {"key": "C", "text": "registered"},
                {"key": "D", "text": "adjudicated"}
            ],
            "options_raw": "A. dismissed\nB. validated\nC. registered\nD. adjudicated",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 3,
            "difficulty": "Hard",
            "princeton_strategy": "POOE - Technical Precision in Domain",
            "tier1_hint": "Câu hỏi từ vựng yêu cầu điền một động từ diễn tả hành động pháp lý của các cơ quan tư pháp (judicial bodies) đối với các vụ án/vụ việc (cases) tranh chấp nguồn nước hoặc tưới tiêu.",
            "tier2_hint": "Chú ý các từ khóa mang tính chuyên ngành tư pháp: 'court' (tòa án), 'judicial bodies' (cơ quan xét xử), 'cases' (vụ án). Cần một thuật ngữ pháp lý chuẩn chỉ việc 'xét xử/phân xử' các vụ kiện.",
            "tier3_hint": "Phương án đúng là **[D]** (*adjudicated*).\n\n**Phân tích chi tiết:**\nTòa án Nước của Tây Ban Nha là cơ quan tư pháp lâu đời nhất xử lý các tranh chấp về nước. Động từ pháp lý 'adjudicate' có nghĩa là chính thức xét xử/phân xử một vụ kiện.\n\n• (A) *dismissed* (bác bỏ) — quá hẹp, tòa án không chỉ bác bỏ mà còn thụ lý xét xử.\n• (B) *validated* (chứng thực/phê chuẩn) — không dùng cho xét xử tranh chấp.\n• (C) *registered* (đăng ký) — không phản ánh thẩm quyền phán quyết của tòa án.",
            "strategic_tip": "Mẹo Princeton Review: Khi văn bản mang chủ đề chuyên ngành (luật pháp, khoa học), College Board thường kiểm tra các thuật ngữ chuẩn xác (Precise Language) tương ứng với chức năng của chủ thể.",
            "pooe_breakdown": "• [D] ĐÚNG: adjudicated (phân xử/xét xử vụ án) là thuật ngữ tư pháp chuẩn xác khi đi với judicial bodies và cases.\n• [A] Loại dismissed vì quá hạn hẹp.\n• [B] Loại validated vì không đúng tính chất xét xử.\n• [C] Loại registered vì đăng ký không mang quyền lực phán quyết.",
            "option_explanations": {
                "A": "Loại A — dismissed (bác bỏ) quá hẹp; tòa án không chỉ bác bỏ đơn kiện mà mục đích chính là phân xử.",
                "B": "Loại B — validated (phê chuẩn) không phù hợp với chức năng thụ lý tranh chấp giữa các bên.",
                "C": "Loại C — registered (đăng ký) không phản ánh quyền lực phán quyết tư pháp của tòa án.",
                "D": "ĐÁP ÁN ĐÚNG. adjudicated (phân xử/xét xử theo luật định) là thuật ngữ tư pháp chuẩn xác khi đi với 'cases'."
            }
        },
        # --- Q4 ---
        {
            "id": 4,
            "master_id": "PR_RW_4",
            "q_number": 4,
            "q_label": "RW #4",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Craft and Structure • Words in Context (Negative Constraints)",
            "passage": "New research conducted by Jakob Wikström and Etty Bachar-Wikström was inspired by reports of the remarkable ability of sharks to heal from wounds sustained in the wild. Despite previous data suggesting that chemicals found in shark skin may have significant biomedical potential, researchers before Wikström and Bachar-Wikström had not ________ the comprehensive and numerous experiments necessary to explore this phenomenon in controlled laboratory conditions.",
            "prompt": "Which choice completes the text with the most logical and precise word or phrase?",
            "options": [
                {"key": "A", "text": "halted"},
                {"key": "B", "text": "executed"},
                {"key": "C", "text": "dissimulated"},
                {"key": "D", "text": "decried"}
            ],
            "options_raw": "A. halted\nB. executed\nC. dissimulated\nD. decried",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 3,
            "difficulty": "Hard",
            "princeton_strategy": "POOE - Grammatical Collocation & Negative Reversal",
            "tier1_hint": "Xác định động từ cần điền đi với tân ngữ 'the comprehensive and numerous experiments' (các thí nghiệm toàn diện và quy mô lớn). Lưu ý từ phủ định 'not' đứng trước ô trống.",
            "tier2_hint": "Các nhà nghiên cứu trước đây 'chưa từng tiến hành/thực hiện' các thí nghiệm cần thiết trong điều kiện phòng thí nghiệm được kiểm soát. Cần một từ mang nghĩa 'thực hiện/tiến hành' (conducted/carried out).",
            "tier3_hint": "Phương án đúng là **[B]** (*executed*).\n\n**Phân tích chi tiết:**\nĐi với 'experiments', động từ 'execute' mang nghĩa là 'tiến hành/thực thi' (perform/carry out). Các nhà khoa học trước đó chưa từng thực hiện các thí nghiệm này.\n\n• (A) *halted* (tạm dừng) — họ chưa từng bắt đầu nên không thể nói là tạm dừng.\n• (C) *dissimulated* (che đậy/ngụy trang) — sai nét nghĩa hoàn toàn.\n• (D) *decried* (lên án/chỉ trích) — không hợp lý trong nghiên cứu khoa học.",
            "strategic_tip": "Mẹo Princeton Review: Chú ý từ phủ định 'not' hoặc 'hardly' trước ô trống. Thiếu từ 'not' sẽ khiến học sinh dễ bị chọn nhầm từ trái nghĩa.",
            "pooe_breakdown": "• [B] ĐÚNG: executed mang nghĩa tiến hành/thực thi thí nghiệm.\n• [A] Loại halted vì họ chưa làm nên không thể dừng.\n• [C] Loại dissimulated vì không ai ngụy trang thí nghiệm.\n• [D] Loại decried vì không có ai chỉ trích nghiên cứu này.",
            "option_explanations": {
                "A": "Loại A — halted (đình chỉ/dừng lại) ngụ ý đã làm rồi phải dừng, trái với thực tế chưa ai làm quy mô này.",
                "B": "ĐÁP ÁN ĐÚNG. executed (tiến hành/thực thi) kết hợp tự nhiên với 'experiments' để chỉ việc triển khai nghiên cứu.",
                "C": "Loại C — dissimulated (che giấu cảm xúc/ngụy trang) hoàn toàn không phù hợp ngữ cảnh khoa học.",
                "D": "Loại D — decried (chỉ trích công khai) sai nghĩa khi nói về việc làm thí nghiệm."
            }
        },
        # --- Q5 ---
        {
            "id": 5,
            "master_id": "PR_RW_5",
            "q_number": 5,
            "q_label": "RW #5",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Craft and Structure • Text Structure and Purpose (Sentence Function)",
            "passage": "The following text is adapted from James Weldon’s 1912 book. In the text, Johnson discusses the skilled workers of the cigar-making trade.\nHe was able to make a bundle of one hundred cigars in a day, not one of which could be told from the others by any difference in size or shape, or even by any appreciable difference in weight. This was the acme of artistic skill in cigar making. Workmen of this class were rare, never more than three or four in one factory, and it was never necessary for them to remain out of work. There were men who made two, three, and four hundred cigars of the cheaper grades in a day; they had to be very fast in order to make a decent week’s wages.",
            "prompt": "Which choice best describes the function of the underlined sentence in the text as a whole?",
            "options": [
                {"key": "A", "text": "It emphasizes the competence with which the cigar-maker engages in his daily work."},
                {"key": "B", "text": "It compares the technique of cigar-making to the craft of making a piece of art."},
                {"key": "C", "text": "It suggests that the more skilled workers do not make the cheaper cigars."},
                {"key": "D", "text": "It shows how the workmen are affected by the conditions of the cigar factory."}
            ],
            "options_raw": "A. It emphasizes the competence with which the cigar-maker engages in his daily work.\nB. It compares the technique of cigar-making to the craft of making a piece of art.\nC. It suggests that the more skilled workers do not make the cheaper cigars.\nD. It shows how the workmen are affected by the conditions of the cigar factory.",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 3,
            "difficulty": "Hard",
            "princeton_strategy": "Purpose & Structure - Semantic Function Mapping",
            "tier1_hint": "Câu hỏi yêu cầu xác định vai trò của câu được gạch chân trong toàn bộ đoạn trích. Hãy đọc kỹ câu gạch chân và xác định đối tượng mà tác giả đang ca ngợi.",
            "tier2_hint": "Câu gạch chân miêu tả: người thợ có thể làm 100 điếu xì gà trong một ngày mà 'không một điếu nào bị phân biệt với các điếu khác bởi bất kỳ sự khác biệt nào về kích thước, hình dạng hay thậm chí trọng lượng'. Tác giả sau đó gọi đây là 'đỉnh cao kỹ năng nghệ thuật' (acme of artistic skill). Hãy tìm lựa chọn thể hiện sự lành nghề/kỹ năng điêu luyện này.",
            "tier3_hint": "Phương án đúng là **[A]** (*It emphasizes the competence with which the cigar-maker engages in his daily work.*).\n\n**Phân tích chi tiết:**\nCâu văn nhấn mạnh sự đồng đều hoàn hảo của 100 điếu xì gà về kích thước, hình dáng và trọng lượng, qua đó làm nổi bật sự tài hoa và tay nghề bậc thầy (competence) của người thợ.\n\n• (B) sai vì bài viết chỉ ví von kỹ năng đó là đỉnh cao nghệ thuật, chứ không so sánh kỹ thuật làm xì gà với việc tạo ra tác phẩm nghệ thuật nói chung.\n• (C) sai vì câu gạch chân không nói về việc thợ giỏi không làm xì gà giá rẻ.\n• (D) sai vì câu không đề cập đến điều kiện làm việc trong nhà máy ảnh hưởng đến công nhân.",
            "strategic_tip": "Mẹo Princeton Review (Purpose): Khi phân tích chức năng câu gạch chân, hãy xác định mối quan hệ của nó với câu đi liền sau (ví dụ: 'This was the acme of artistic skill'). Câu sau thường giải thích trực tiếp ý đồ của câu trước.",
            "pooe_breakdown": "• [A] ĐÚNG: emphasizes the competence miêu tả hoàn hảo sự thuần thục tuyệt đỉnh trong tay nghề của người thợ.\n• [B] Loại vì so sánh làm xì gà với tác phẩm nghệ thuật là suy diễn vượt văn bản.\n• [C] Loại vì ý xì gà rẻ nằm ở cuối đoạn.\n• [D] Loại vì không nhắc đến điều kiện làm việc tiêu cực.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. emphasizes the competence (nhấn mạnh năng lực/tay nghề vượt trội) khớp chuẩn xác với sự hoàn hảo của 100 điếu xì gà không tì vết.",
                "B": "Loại B — so sánh kỹ thuật làm xì gà với tạo tác phẩm nghệ thuật là suy diễn vượt văn bản (Beyond the Text).",
                "C": "Loại C — chi tiết về xì gà rẻ tiền nằm ở cuối đoạn văn, không phải chức năng của câu gạch chân này.",
                "D": "Loại D — đoạn văn không nói về điều kiện làm việc khắc nghiệt ảnh hưởng đến thợ."
            }
        },
        # --- Q6 ---
        {
            "id": 6,
            "master_id": "PR_RW_6",
            "q_number": 6,
            "q_label": "RW #6",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Craft and Structure • Text Structure and Purpose (Main Purpose)",
            "passage": "The following text is from Charles Dickens’s 1861 novel Great Expectations. Pip, the narrator, has just gained a considerable fortune from an anonymous benefactor.\nI took it upon myself to impress Biddy (and through Biddy, Joe) with the grave obligation I considered my friends under, to know nothing and say nothing about the maker of my fortune. It would all come out in good time, I observed, and in the meanwhile nothing was to be said, save that I had come into great expectations from a mysterious patron.",
            "prompt": "Which choice best states the main purpose of the text?",
            "options": [
                {"key": "A", "text": "To explain that Pip finds his new fortune both stressful and immensely rejuvenating"},
                {"key": "B", "text": "To describe Pip’s resolve to not discuss the identity of his benefactor"},
                {"key": "C", "text": "To detail a conflict between Pip’s internal excitement and external confidence"},
                {"key": "D", "text": "To highlight Pip’s desire to impress his friends with his newfound wealth"}
            ],
            "options_raw": "A. To explain that Pip finds his new fortune both stressful and immensely rejuvenating\nB. To describe Pip’s resolve to not discuss the identity of his benefactor\nC. To detail a conflict between Pip’s internal excitement and external confidence\nD. To highlight Pip’s desire to impress his friends with his newfound wealth",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 4,
            "difficulty": "Hard",
            "princeton_strategy": "Purpose & Structure - Character Action Focus",
            "tier1_hint": "Xác định mục đích chính của nhân vật Pip trong đoạn trích tiểu thuyết Great Expectations. Pip đang dặn dò Biddy và Joe điều gì về số tài sản mới nhận?",
            "tier2_hint": "Chú ý cụm từ then chốt: 'grave obligation... to know nothing and say nothing about the maker of my fortune' và 'nothing was to be said'. Pip kiên quyết yêu cầu bạn bè không được bàn tán hay tìm hiểu về danh tính của ân nhân bí mật.",
            "tier3_hint": "Phương án đúng là **[B]** (*To describe Pip’s resolve to not discuss the identity of his benefactor.*).\n\n**Phân tích chi tiết:**\nToàn bộ đoạn văn thể hiện quyết tâm (resolve) của Pip trong việc yêu cầu bạn bè tuyệt đối giữ bí mật và không được bàn tán về người đã ban tặng gia tài cho mình ('know nothing and say nothing about the maker of my fortune').\n\n• (A) sai vì Pip không hề cảm thấy căng thẳng (stressful) hay trẻ hóa (rejuvenated).\n• (C) sai vì không có xung đột nội tâm nào giữa phấn khích và tự tin được nhắc đến.\n• (D) sai vì mục đích chính của Pip ở đây là phong tỏa thông tin về ân nhân, chứ không phải muốn khoe khoang để gây ấn tượng về sự giàu có.",
            "strategic_tip": "Mẹo Princeton Review: Với câu hỏi Main Purpose trong văn học, hãy bám sát hành động cốt lõi của nhân vật (gạch chân các động từ chính: 'know nothing and say nothing'). Tránh chọn các phương án gán cảm xúc quá đà không có trong bài.",
            "pooe_breakdown": "• [B] ĐÚNG: Pip's resolve to not discuss the identity of his benefactor phản ánh chính xác mệnh lệnh 'know nothing and say nothing'.\n• [A] Loại vì không có cảm xúc stressful/rejuvenating.\n• [C] Loại vì không có xung đột nội tâm.\n• [D] Loại vì Pip muốn giữ bí mật chứ không phải khoe mẽ.",
            "option_explanations": {
                "A": "Loại A — bài đọc không hề nhắc đến việc Pip cảm thấy 'stressful' hay 'rejuvenated'.",
                "B": "ĐÁP ÁN ĐÚNG. To describe Pip’s resolve to not discuss the identity of his benefactor miêu tả chuẩn xác yêu cầu 'know nothing and say nothing'.",
                "C": "Loại C — Pip không trải qua xung đột nội tâm (conflict) nào trong đoạn trích này.",
                "D": "Loại D — Pip dặn bạn bè giữ im lặng về ân nhân chứ không phải khoe khoang của cải."
            }
        },
        # --- Q7 ---
        {
            "id": 7,
            "master_id": "PR_RW_7",
            "q_number": 7,
            "q_label": "RW #7",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Craft and Structure • Text Structure and Purpose (Overall Structure)",
            "passage": "Yoshioka Tokujin, a Japanese artist acclaimed for his works, incorporates nature into his creations, bringing the ephemeral and natural together in a controlled setting. Tokujin’s “Tornado,” for example, used more than two million translucent plastic straws to simulate a transparent whirlwind, creating an experience of nature while reflecting modern environmental concerns. In a more explicit combination of nature and music, Tokujin created a painting called “Swan Lake,” which was crystallized over a period of six months while the music of the famous Tchaikovsky ballet was played nearby. The music caused vibrations in the liquid, shaping the crystals that formed the artwork.",
            "prompt": "Which choice best describes the overall structure of the text?",
            "options": [
                {"key": "A", "text": "It discusses Tokujin’s work in detail, then draws a conclusion about Tokujin’s reception by the art world."},
                {"key": "B", "text": "It introduces an artist’s general approach, then describes a specific instance of his art."},
                {"key": "C", "text": "It contrasts the crystallized painting derived from “Swan Lake” with the one made from straws."},
                {"key": "D", "text": "It describes Tokujin’s approach, then explains how the music of “Swan Lake” inspired that approach."}
            ],
            "options_raw": "A. It discusses Tokujin’s work in detail, then draws a conclusion about Tokujin’s reception by the art world.\nB. It introduces an artist’s general approach, then describes a specific instance of his art.\nC. It contrasts the crystallized painting derived from “Swan Lake” with the one made from straws.\nD. It describes Tokujin’s approach, then explains how the music of “Swan Lake” inspired that approach.",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 4,
            "difficulty": "Hard",
            "princeton_strategy": "Purpose & Structure - Macro Structure Mapping",
            "tier1_hint": "Xác định cấu trúc chuyển dịch ý tưởng của toàn đoạn văn: Câu đầu tiên nêu điều gì về phong cách nghệ thuật của Yoshioka Tokujin? Các câu tiếp theo đóng vai trò gì?",
            "tier2_hint": "Câu đầu giới thiệu triết lý nghệ thuật chung của Tokujin: 'incorporates nature into his creations' (đưa thiên nhiên vào tác phẩm). Các câu tiếp theo đưa ra các ví dụ cụ thể như tác phẩm 'Tornado' và bức tranh kết tinh 'Swan Lake'. Tìm phương án thể hiện cấu trúc: từ khái quát đến cụ thể.",
            "tier3_hint": "Phương án đúng là **[B]** (*It introduces an artist’s general approach, then describes a specific instance of his art.*).\n\n**Phân tích chi tiết:**\nĐoạn văn mở đầu bằng cách giới thiệu phương pháp tiếp cận chung của nghệ sĩ Tokujin (lồng ghép thiên nhiên vào sáng tác trong môi trường có kiểm soát), sau đó minh họa chi tiết qua các tác phẩm cụ thể ('Tornado' và 'Swan Lake').\n\n• (A) sai vì bài không đưa ra kết luận nào về sự đón nhận của công chúng đối với nghệ thuật của Tokujin.\n• (C) sai vì bài không so sánh đối lập giữa hai tác phẩm.\n• (D) sai vì bài không giải thích âm nhạc hồ thiên nga đã ảnh hưởng thế nào đến ý tưởng của nghệ sĩ mà chỉ mô tả rung động cơ học tạo tinh thể.",
            "strategic_tip": "Mẹo Princeton Review (Overall Structure): Đọc lướt và xác định 'nhịp điệu' của đoạn văn: General Rule/Approach -> Specific Examples/Instances. Đây là cấu trúc kinh điển của College Board.",
            "pooe_breakdown": "• [B] ĐÚNG: introduces general approach -> describes specific instances thể hiện chuẩn xác bố cục từ khái quát đến chi tiết.\n• [A] Loại vì không có kết luận về sự tiếp nhận của giới nghệ thuật.\n• [C] Loại vì bài không so sánh đối lập.\n• [D] Loại vì âm nhạc không phải nguồn cảm hứng sinh ra triết lý.",
            "option_explanations": {
                "A": "Loại A — bài đọc không hề rút ra kết luận về sự đón nhận của công chúng (conclusion about reception).",
                "B": "ĐÁP ÁN ĐÚNG. introduces an artist's general approach, then describes a specific instance phản ánh hoàn hảo cấu trúc từ triết lý chung đến tác phẩm cụ thể.",
                "C": "Loại C — bài đọc liệt kê hai tác phẩm chứ không hề tạo ra sự tương phản (contrasts) giữa chúng.",
                "D": "Loại D — bài đọc nói về rung động vật lý tạo tinh thể chứ không giải thích âm nhạc truyền cảm hứng cho triết lý chung như thế nào."
            }
        },
        # --- Q8 ---
        {
            "id": 8,
            "master_id": "PR_RW_8",
            "q_number": 8,
            "q_label": "RW #8",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Craft and Structure • Text Structure and Purpose (Sentence Function)",
            "passage": "A study by a team led by cardiology professor Maciej Banach found that, over a lower limit, increasing the number of daily steps walked reduced the risk of death from cardiovascular disease as well as any cause. The study analyzed 226,889 people from 17 worldwide studies and analyzed the health data of individuals who had walked from 5,000 steps up to 20,000 steps a day. The team found that extra steps led to a decrease in the risk of death from cardiovascular disease, additional extra steps led to a decrease in the risk of death from any cause, and no upper limit to these health benefits has been found.",
            "prompt": "Which choice best states the function of the underlined sentence in the overall structure of the text?",
            "options": [
                {"key": "A", "text": "To present an obstacle encountered by the team during its study"},
                {"key": "B", "text": "To summarize the conclusions reached by the team"},
                {"key": "C", "text": "To introduce a specific example that demonstrates the team’s conclusions"},
                {"key": "D", "text": "To detail the data utilized in the team’s analysis"}
            ],
            "options_raw": "A. To present an obstacle encountered by the team during its study\nB. To summarize the conclusions reached by the team\nC. To introduce a specific example that demonstrates the team’s conclusions\nD. To detail the data utilized in the team’s analysis",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 5,
            "difficulty": "Hard",
            "princeton_strategy": "Purpose & Structure - Empirical Data Identification",
            "tier1_hint": "Câu hỏi yêu cầu xác định chức năng của câu được gạch chân ('The study analyzed 226,889 people from 17 worldwide studies...'). Câu này cung cấp thông tin gì về quy mô và số liệu của nghiên cứu?",
            "tier2_hint": "Câu trước nêu kết luận chung của nghiên cứu. Câu gạch chân đưa ra các con số cụ thể: 226.889 người tham gia, 17 nghiên cứu trên toàn cầu, phạm vi từ 5.000 đến 20.000 bước mỗi ngày. Đây là các dữ liệu thực nghiệm được sử dụng để phân tích.",
            "tier3_hint": "Phương án đúng là **[D]** (*To detail the data utilized in the team’s analysis.*).\n\n**Phân tích chi tiết:**\nCâu gạch chân trình bày cụ thể quy mô mẫu và các chỉ số đo lường (226.889 đối tượng từ 17 nghiên cứu, lượng bước chân từ 5.000 - 20.000 bước). Chức năng của nó là chi tiết hóa dữ liệu được sử dụng trong phân tích của nhóm tác giả.\n\n• (A) sai vì các con số này không đại diện cho trở ngại hay khó khăn (obstacle).\n• (B) sai vì câu này cung cấp dữ liệu đầu vào, không phải tóm tắt kết luận.\n• (C) sai vì câu này không nêu một ví dụ minh họa đơn lẻ nào mà đưa ra tổng thể bộ dữ liệu.",
            "strategic_tip": "Mẹo Princeton Review: Khi một câu trong bài đọc khoa học chứa đầy những con số về cỡ mẫu (sample size) và phạm vi khảo sát, chức năng của nó luôn là cung cấp thông tin chi tiết về dữ liệu/phương pháp nghiên cứu.",
            "pooe_breakdown": "• [D] ĐÚNG: detail the data utilized in the analysis phản ánh hoàn hảo việc trình bày quy mô 226.889 người và 17 nghiên cứu.\n• [A] Loại vì không có khó khăn trở ngại.\n• [B] Loại vì kết luận nằm ở câu đầu và câu cuối.\n• [C] Loại vì đây là tập dữ liệu tổng quát chứ không phải ví dụ đơn lẻ.",
            "option_explanations": {
                "A": "Loại A — câu văn mô tả quy mô nghiên cứu, không nói về bất kỳ trở ngại (obstacle) nào.",
                "B": "Loại B — kết luận của nghiên cứu nằm ở câu đầu và câu cuối, câu gạch chân là dữ liệu.",
                "C": "Loại C — đây là toàn bộ tập dữ liệu mẫu chứ không phải một ví dụ cá biệt (specific example).",
                "D": "ĐÁP ÁN ĐÚNG. detail the data utilized in the team’s analysis mô tả chính xác mục đích liệt kê số lượng người và nghiên cứu tham gia."
            }
        },
        # --- Q9 ---
        {
            "id": 9,
            "master_id": "PR_RW_9",
            "q_number": 9,
            "q_label": "RW #9",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Information and Ideas • Cross-Text Connections (Dual Texts Synthesis)",
            "passage": "Text 1\nThe origin of mitochondria has long been assumed to be a single-celled prokaryote swallowing a bacterium, forming a eukaryote. But when a group of scientists led by Toni Gabaldón started sequencing modern genomes, they found evidence of more than two “partners” in the original synthesis. Gabaldón and his team hypothesize that these simple cellular ancestors shared genetic material via a variety of partners that led to the development of eukaryotes in a more “horizontal,” or branching, fashion. This discovery may lead to the rewriting of our narrative of how our genes evolved.\n\nText 2\nWhile Gabaldón and colleagues advocate for a “gradual” evolution of cell symbionts involving multiple genetic partners, it’s too soon to recast the beginnings of mitochondria. For the cells to employ such a multidirectional evolutionary pathway, they would more likely already have been more complex eukaryotic cells, not simple prokaryotes. Gabaldón’s observations of modern host eukaryotes may therefore not reveal as much about the behavior of ancestral prokaryotes as originally believed.",
            "prompt": "Based on the texts, what would the author of Text 2 say about Gabaldón and his team’s hypothesis regarding the evidence found in Text 1?",
            "options": [
                {"key": "A", "text": "It is understandable given that the gene sequencing performed by Gabaldón is the first use of this groundbreaking technology."},
                {"key": "B", "text": "It is surprising given that the traditional assumptions of the origin of the mitochondria contradict Gabaldón’s theory."},
                {"key": "C", "text": "It may not accurately depict the nature of the organism involved in the evolutionary process described by the theory."},
                {"key": "D", "text": "It is overly simplistic given the complexity of the genome sequencing performed by Gabaldón."}
            ],
            "options_raw": "A. It is understandable given that the gene sequencing performed by Gabaldón is the first use of this groundbreaking technology.\nB. It is surprising given that the traditional assumptions of the origin of the mitochondria contradict Gabaldón’s theory.\nC. It may not accurately depict the nature of the organism involved in the evolutionary process described by the theory.\nD. It is overly simplistic given the complexity of the genome sequencing performed by Gabaldón.",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 5,
            "difficulty": "Hard",
            "princeton_strategy": "Dual-Text Synthesis - Contrast & Counter-Argument",
            "tier1_hint": "Câu hỏi yêu cầu xác định quan điểm của tác giả Đoạn 2 về giả thuyết của nhóm Gabaldón trong Đoạn 1. Đoạn 2 đánh giá thế nào về việc suy luận từ tế bào nhân thực hiện đại sang tế bào nhân sơ cổ đại?",
            "tier2_hint": "Tác giả Đoạn 2 cho rằng để có con đường tiến hóa đa chiều như vậy, các tế bào nhiều khả năng đã là tế bào nhân thực phức tạp rồi chứ không phải tế bào nhân sơ đơn giản. Do đó, việc quan sát các tế bào hiện đại chưa chắc đã phản ánh đúng bản chất của sinh vật cổ đại tham gia vào quá trình tiến hóa ban đầu.",
            "tier3_hint": "Phương án đúng là **[C]** (*It may not accurately depict the nature of the organism involved in the evolutionary process described by the theory.*).\n\n**Phân tích chi tiết:**\nTác giả Đoạn 2 lập luận rằng quan sát của Gabaldón trên các sinh vật nhân thực hiện đại có thể không tiết lộ chính xác hành vi của các sinh vật nhân sơ tổ tiên, vì con đường tiến hóa phức tạp đó đòi hỏi tế bào phải phức tạp hơn. Nói cách khác, giả thuyết này có thể không miêu tả chính xác bản chất sinh vật cổ đại.\n\n• (A) sai vì Đoạn 2 không nói giải trình tự gen của Gabaldón là lần đầu tiên công nghệ này được dùng.\n• (B) sai vì là Half-Right: dù lý thuyết của Gabaldón mâu thuẫn giả định truyền thống, Đoạn 2 không lấy lý do đó để phản bác mà phản bác dựa trên tính chất tế bào.\n• (D) sai vì Đoạn 2 không cho rằng giả thuyết quá đơn giản hóa (overly simplistic).",
            "strategic_tip": "Mẹo Princeton Review (Dual Texts): Luôn gạch chân câu chốt ở cuối Đoạn 2 ('may therefore not reveal as much about the behavior of ancestral prokaryotes'). Đáp án đúng phải là sự diễn đạt lại (paraphrase) trực tiếp câu kết luận đó.",
            "pooe_breakdown": "• [C] ĐÚNG: may not accurately depict the nature of the organism paraphrase chuẩn xác kết luận ở cuối Đoạn 2.\n• [A] Loại vì không đề cập đến công nghệ lần đầu tiên.\n• [B] Loại bẫy Half-Right.\n• [D] Loại vì không chỉ trích là overly simplistic.",
            "option_explanations": {
                "A": "Loại A — Đoạn 2 không nói công nghệ giải trình tự này là lần đầu tiên được sử dụng.",
                "B": "Loại B — bẫy Half-Right; Đoạn 2 phản bác dựa trên cấu trúc tế bào chứ không phải vì nó mâu thuẫn quan điểm truyền thống.",
                "C": "ĐÁP ÁN ĐÚNG. It may not accurately depict the nature of the organism paraphrase chuẩn xác câu kết Đoạn 2 về việc không phản ánh đúng sinh vật tổ tiên.",
                "D": "Loại D — Đoạn 2 không chỉ trích lý thuyết của Gabaldón là quá đơn giản hóa."
            }
        },
        # --- Q10 ---
        {
            "id": 10,
            "master_id": "PR_RW_10",
            "q_number": 10,
            "q_label": "RW #10",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Information and Ideas • Command of Evidence (Quantitative / Tables)",
            "passage": "Tickets Sold and Box Office Revenue from 1996–2000\nYear | Tickets sold (in billions) | Box Office Revenue (in billions of dollars)\n1996 | 1.3 | 5.8\n1997 | 1.4 | 6.2\n1998 | 1.5 | 6.8\n1999 | 1.4 | 7.3\n2000 | 1.4 | 7.5\n\nSome writers interested in the rise of the modern blockbuster movie have begun to focus on the technological innovations that gave rise to this era of film during the 1990s, noting that the increased usage of special effects raised production costs and led to increased ticket prices as a means to meet those costs. The impact of higher ticket prices can be observed by examining both the number of tickets sold and box office revenue during the same period. Box office revenue continued to rise through the 1990s despite ticket sales decreasing towards the end of the decade, which can be seen by comparing ________",
            "prompt": "Which choice most effectively uses data from the table to complete the example?",
            "options": [
                {"key": "A", "text": "the tickets sold and revenue generated in the year 1998 to the tickets sold and revenue generated in the year 2000."},
                {"key": "B", "text": "the tickets sold and revenue generated in the year 1997 to the tickets sold and the revenue generated in the year 1999."},
                {"key": "C", "text": "the tickets sold in the year 1997 to the tickets sold in the year 1998."},
                {"key": "D", "text": "the tickets sold in the year 1996 to the tickets sold in the year 1997."}
            ],
            "options_raw": "A. the tickets sold and revenue generated in the year 1998 to the tickets sold and revenue generated in the year 2000.\nB. the tickets sold and revenue generated in the year 1997 to the tickets sold and the revenue generated in the year 1999.\nC. the tickets sold in the year 1997 to the tickets sold in the year 1998.\nD. the tickets sold in the year 1996 to the tickets sold in the year 1997.",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 6,
            "difficulty": "Hard",
            "princeton_strategy": "Command of Evidence - Dual Trend Verification",
            "tier1_hint": "Đọc kỹ câu chứa ô trống: Cần tìm một phép so sánh giữa 2 mốc thời gian thể hiện đúng 2 điều kiện đồng thời: (1) Doanh thu phòng vé (Box office revenue) TIẾP TỤC TĂNG, và (2) Lượng vé bán ra (Tickets sold) GIẢM đi.",
            "tier2_hint": "Tra cứu bảng số liệu từ năm 1998 đến năm 2000:\n- Năm 1998: Vé = 1.5 tỉ, Doanh thu = 6.8 tỉ.\n- Năm 2000: Vé = 1.4 tỉ (GIẢM từ 1.5 xuống 1.4), Doanh thu = 7.5 tỉ (TĂNG từ 6.8 lên 7.5).\nHãy kiểm tra xem cặp năm nào thỏa mãn hoàn hảo cả hai tiêu chí này.",
            "tier3_hint": "Phương án đúng là **[A]** (*the tickets sold and revenue generated in the year 1998 to the tickets sold and revenue generated in the year 2000.*).\n\n**Phân tích chi tiết:**\nBảng số liệu cho thấy từ năm 1998 sang năm 2000:\n• Số vé bán ra giảm từ 1.5 tỉ xuống 1.4 tỉ (ticket sales decreasing).\n• Doanh thu phòng vé tăng từ 6.8 tỉ lên 7.5 tỉ đô la (revenue continued to rise).\nCặp năm 1998 và 2000 chứng minh hoàn hảo luận điểm trong bài.\n\n• (B) sai vì từ 1997 (1.4 tỉ vé) sang 1999 (1.4 tỉ vé), lượng vé giữ nguyên chứ không giảm.\n• (C) sai vì từ 1997 sang 1998 lượng vé tăng từ 1.4 lên 1.5 tỉ.\n• (D) sai vì từ 1996 sang 1997 cả vé và doanh thu đều tăng.",
            "strategic_tip": "Mẹo Princeton Review (Charts & Tables): Khi đề bài yêu cầu chứng minh 2 xu hướng trái ngược nhau (A tăng nhưng B giảm), hãy kiểm tra từng lựa chọn bằng bảng kiểm 2 cột (+ / -). Chỉ lựa chọn thỏa mãn cả 2 dấu mới được chọn.",
            "pooe_breakdown": "• [A] ĐÚNG: So sánh 1998 và 2000: vé giảm (1.5 -> 1.4) trong khi doanh thu tăng (6.8 -> 7.5), khớp 100% luận điểm.\n• [B] Loại so sánh 1997 và 1999 vì lượng vé không đổi (đều 1.4 tỉ).\n• [C] Loại vì lượng vé tăng từ 1.4 lên 1.5 tỉ.\n• [D] Loại vì cả vé lẫn doanh thu đều tăng.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. So sánh 1998 và 2000: vé giảm (1.5 -> 1.4) trong khi doanh thu tăng (6.8 -> 7.5), khớp 100% luận điểm.",
                "B": "Loại B — so sánh 1997 và 1999: lượng vé không đổi (đều là 1.4 tỉ), không chứng minh được xu hướng giảm.",
                "C": "Loại C — từ 1997 sang 1998 lượng vé tăng từ 1.4 lên 1.5 tỉ, đi ngược lại luận điểm vé giảm.",
                "D": "Loại D — từ 1996 sang 1997 cả vé lẫn doanh thu đều tăng, không thể hiện việc vé giảm."
            }
        },
        # --- Q11 ---
        {
            "id": 11,
            "master_id": "PR_RW_11",
            "q_number": 11,
            "q_label": "RW #11",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Information and Ideas • Command of Evidence (Textual Claims)",
            "passage": "Recently discovered in China, Proterocladus antique is the scientific name for an algae fossil approximately a billion years old. Using samples from the well-preserved Nanfen formation (an ancient seabed), Qing Tang, Ke Pang, Xunlai Yuan and Shuhai Xiao found that P. antique was a green alga that could, like its modern relative seaweed, photosynthesize—that is, manufacture sugars and oxygen from light and carbon dioxide. Tang maintains that P. antique indicates that green algae first evolved in the oceans instead of in freshwater environments such as lakes and rivers.",
            "prompt": "Which of the following, if true, would most directly support Tang’s claim?",
            "options": [
                {"key": "A", "text": "The fossils are visible to the naked eye, which indicates that P. antique was one of the largest creatures of the era, sharing the seas with smaller organisms such as bacteria."},
                {"key": "B", "text": "The fossils of P. antique are evenly distributed in the Nanfen formation with fossils of freshwater algae and other photosynthesizing organisms from the same era."},
                {"key": "C", "text": "Green algae such as P. antique and sea lettuce do the majority of photosynthesis on the planet, while land plants, which evolved later, are responsible for a less substantial proportion of the process."},
                {"key": "D", "text": "The oldest scientifically legitimized fossil of green algae from a freshwater environment is confirmed to be only about 800 million years old."}
            ],
            "options_raw": "A. The fossils are visible to the naked eye, which indicates that P. antique was one of the largest creatures of the era, sharing the seas with smaller organisms such as bacteria.\nB. The fossils of P. antique are evenly distributed in the Nanfen formation with fossils of freshwater algae and other photosynthesizing organisms from the same era.\nC. Green algae such as P. antique and sea lettuce do the majority of photosynthesis on the planet, while land plants, which evolved later, are responsible for a less substantial proportion of the process.\nD. The oldest scientifically legitimized fossil of green algae from a freshwater environment is confirmed to be only about 800 million years old.",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 6,
            "difficulty": "Hard",
            "princeton_strategy": "Command of Evidence - Evolutionary Timeline Verification",
            "tier1_hint": "Câu hỏi tìm bằng chứng củng cố (support) tuyên bố của Tang: tảo lục tiến hóa đầu tiên ở đại dương (oceans) chứ không phải ở môi trường nước ngọt (freshwater).",
            "tier2_hint": "Hóa thạch tảo biển P. antique có tuổi đời khoảng 1 tỷ năm. Để chứng minh tảo biển xuất hiện trước tảo nước ngọt, cần tìm bằng chứng cho thấy hóa thạch tảo nước ngọt có niên đại muộn hơn (trẻ hơn 1 tỷ năm).",
            "tier3_hint": "Phương án đúng là **[D]** (*The oldest scientifically legitimized fossil of green algae from a freshwater environment is confirmed to be only about 800 million years old.*).\n\n**Phân tích chi tiết:**\nHóa thạch tảo biển P. antique có niên đại 1 tỷ năm. Nếu hóa thạch tảo nước ngọt cổ nhất chỉ có khoảng 800 triệu năm tuổi (trẻ hơn 200 triệu năm), điều này trực tiếp chứng minh tảo lục đã tiến hóa ở biển trước khi xuất hiện ở nước ngọt.\n\n• (A) sai vì kích thước nhìn thấy bằng mắt thường không liên quan đến nguồn gốc môi trường tiến hóa.\n• (B) sai vì nếu có hóa thạch tảo nước ngọt cùng niên đại 1 tỷ năm thì sẽ làm suy yếu luận điểm của Tang.\n• (C) sai vì tỷ lệ quang hợp hiện đại không chứng minh được môi trường tiến hóa ban đầu.",
            "strategic_tip": "Mẹo Princeton Review (Claims): Khi một giả thuyết khẳng định A xuất hiện trước B trong lịch sử tiến hóa, bằng chứng củng cố mạnh nhất là niên đại hóa thạch của A cổ hơn niên đại sớm nhất của B.",
            "pooe_breakdown": "• [D] ĐÚNG: Hóa thạch nước ngọt cổ nhất chỉ 800 triệu năm (trẻ hơn 1 tỷ năm của tảo biển) chứng minh tảo biển có trước.\n• [A] Loại vì kích thước không liên quan đến nguồn gốc tiến hóa.\n• [B] Loại vì xuất hiện cùng thời với tảo nước ngọt sẽ phản bác Tang.\n• [C] Loại vì tỉ lệ quang hợp hiện tại không nói lên lịch sử tiến hóa.",
            "option_explanations": {
                "A": "Loại A — kích thước hóa thạch không chứng minh được sinh vật xuất hiện ở biển trước hay nước ngọt trước.",
                "B": "Loại B — nếu có hóa thạch tảo nước ngọt cùng niên đại 1 tỷ năm thì tuyên bố của Tang sẽ bị phản bác.",
                "C": "Loại C — tỷ lệ quang hợp của thực vật hiện nay không liên quan đến thứ tự tiến hóa cách đây 1 tỷ năm.",
                "D": "ĐÁP ÁN ĐÚNG. Hóa thạch tảo nước ngọt cổ nhất chỉ 800 triệu năm chứng minh tảo biển 1 tỷ năm đã xuất hiện trước."
            }
        },
        # --- Q12 ---
        {
            "id": 12,
            "master_id": "PR_RW_12",
            "q_number": 12,
            "q_label": "RW #12",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Information and Ideas • Command of Evidence (Quantitative / Charts)",
            "passage": "Intervention Likelihood Based on Presence of ASD and Bystander Count\n(Graph showing Likelihood of intervention on 4-point scale with 4 being 'most likely' across bystander counts: One, Two, Six, Ten for non-autistic vs autistic employees).\n\nSeeking to understand the impact of autism spectrum disorder (ASD) on an individual’s tendency towards acting on behalf of others, researcher Lorne Hartman led a study that asked participants to rate their willingness to intervene in situations involving workplace dysfunction or inefficiency with varying numbers of bystanders, or uninvolved observers to a situation. The research showed that autistic employees were more likely to speak up on workplace issues than non-autistic employees, regardless of the number of bystanders.",
            "prompt": "Which choice best describes data from the graph that support the researcher’s conclusion?",
            "options": [
                {"key": "A", "text": "The average likelihood of intervention was higher in autistic employees than in non-autistic employees in all scenarios."},
                {"key": "B", "text": "There was no apparent change in the reported likelihood of intervention from non-autistic employees whether there was 1 bystander or 6 bystanders."},
                {"key": "C", "text": "The reported likelihood of intervention was nearly identical when there were 6 bystanders."},
                {"key": "D", "text": "The reported likelihood of intervention from autistic employees declined as the number of bystanders increased."}
            ],
            "options_raw": "A. The average likelihood of intervention was higher in autistic employees than in non-autistic employees in all scenarios.\nB. There was no apparent change in the reported likelihood of intervention from non-autistic employees whether there was 1 bystander or 6 bystanders.\nC. The reported likelihood of intervention was nearly identical when there were 6 bystanders.\nD. The reported likelihood of intervention from autistic employees declined as the number of bystanders increased.",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 7,
            "difficulty": "Hard",
            "princeton_strategy": "Command of Evidence - Graph Pattern Extraction",
            "tier1_hint": "Câu hỏi yêu cầu tìm dữ liệu từ biểu đồ củng cố kết luận của Hartman: nhân viên tự kỷ (autistic) có xu hướng can thiệp / lên tiếng về vấn đề nơi làm việc cao hơn nhân viên không tự kỷ (non-autistic), bất kể số lượng người đứng xem (bystanders).",
            "tier2_hint": "Nhìn vào biểu đồ cột: ở tất cả các mức số người đứng xem (1, 2, 6, 10 bystanders), hãy so sánh chiều cao cột của nhóm autistic so với nhóm non-autistic.",
            "tier3_hint": "Phương án đúng là **[A]** (*The average likelihood of intervention was higher in autistic employees than in non-autistic employees in all scenarios.*).\n\n**Phân tích chi tiết:**\nBiểu đồ cho thấy ở mọi kịch bản số lượng người đứng xem (1, 2, 6 hay 10 người), điểm số khả năng can thiệp trung bình của nhóm autistic luôn cao hơn nhóm non-autistic, khớp hoàn toàn với kết luận 'more likely... regardless of bystander count'.\n\n• (B) sai vì không hỗ trợ cho kết luận so sánh giữa 2 nhóm nhân viên.\n• (C) sai vì ở mốc 6 người đứng xem, hai cột vẫn có sự chênh lệch rõ rệt.\n• (D) sai vì mô tả xu hướng giảm không phải là trọng tâm so sánh giữa 2 nhóm đối tượng.",
            "strategic_tip": "Mẹo Princeton Review (Charts): Đọc kỹ trục tung (Y-axis: Likelihood of intervention) và trục hoành (X-axis: Bystander count), đồng thời chú ý chú giải (Key/Legend) phân biệt giữa 2 nhóm đối tượng.",
            "pooe_breakdown": "• [A] ĐÚNG: Khả năng can thiệp của nhóm autistic cao hơn nhóm non-autistic trong tất cả các kịch bản.\n• [B] Loại vì chỉ nói về nhóm non-autistic, không so sánh.\n• [C] Loại vì số liệu không hề tương đồng (nearly identical).\n• [D] Loại vì xu hướng giảm không chứng minh được sự vượt trội.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. Nhóm autistic có điểm can thiệp cao hơn nhóm non-autistic ở tất cả các trường hợp (1, 2, 6, 10 người).",
                "B": "Loại B — lựa chọn này chỉ nhìn vào nhóm không tự kỷ, không hỗ trợ việc so sánh giữa hai nhóm.",
                "C": "Loại C — số liệu ở mốc 6 người không hề giống nhau (cột autistic cao hơn rõ ràng).",
                "D": "Loại D — việc điểm số giảm không trực tiếp hỗ trợ kết luận rằng nhóm autistic can thiệp nhiều hơn nhóm non-autistic."
            }
        },
        # --- Q13 ---
        {
            "id": 13,
            "master_id": "PR_RW_13",
            "q_number": 13,
            "q_label": "RW #13",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Information and Ideas • Command of Evidence (Textual Claims)",
            "passage": "Mineralogists are often asked to determine whether certain impact events are caused by asteroids (comprised of metals and rock) or fragments of comets (comprised of ice, dust, and rock). In 1927, Soviet mineralogist Leonid Kulik concluded that one of the Earth’s major impacts, the 1908 Tunguska event, occurred when an asteroid exploded a few miles above the ground. According to Kulik, his conclusion was supported by the fact that though the impact flattened miles of forest, it left no crater, which suggests that the object primarily collided with the Earth’s atmosphere rather than the surface.",
            "prompt": "Which finding, if true, would most directly weaken Kulik’s conclusion?",
            "options": [
                {"key": "A", "text": "Researchers tested material from tree cores within the zone of impact, and found high levels of material rarely found in comets but frequently found in rocky asteroids."},
                {"key": "B", "text": "A comet fragment would have disintegrated before reaching the lower atmosphere, but the Tunguska event object stayed intact through most of the lower atmosphere."},
                {"key": "C", "text": "As the celestial body that caused the Tunguska event passed through the atmosphere, such pressures and temperatures developed that the object abruptly exploded."},
                {"key": "D", "text": "After the event, researchers and locals searched for metal-laced rock fragments over the area of impact, but no such objects were ever reported discovered."}
            ],
            "options_raw": "A. Researchers tested material from tree cores within the zone of impact, and found high levels of material rarely found in comets but frequently found in rocky asteroids.\nB. A comet fragment would have disintegrated before reaching the lower atmosphere, but the Tunguska event object stayed intact through most of the lower atmosphere.\nC. As the celestial body that caused the Tunguska event passed through the atmosphere, such pressures and temperatures developed that the object abruptly exploded.\nD. After the event, researchers and locals searched for metal-laced rock fragments over the area of impact, but no such objects were ever reported discovered.",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 7,
            "difficulty": "Hard",
            "princeton_strategy": "Command of Evidence - Counter-Evidence Formulation",
            "tier1_hint": "Câu hỏi yêu cầu tìm dữ liệu làm suy yếu (weaken) kết luận của Kulik rằng vụ nổ Tunguska do một tiểu hành tinh (asteroid - cấu tạo từ kim loại và đá) gây ra.",
            "tier2_hint": "Phân biệt hai loại thiên thể trong bài: thiên thạch/sao chổi (comet - cấu tạo từ băng tuyết, bụi và đá, dễ tan biến) và tiểu hành tinh (asteroid - kim loại và đá). Nếu là tiểu hành tinh chứa kim loại, đáng lẽ phải tìm thấy mảnh vụn đá chứa kim loại sau vụ nổ. Dẫn chứng làm suy yếu sẽ chỉ ra sự vắng mặt của các mảnh kim loại này.",
            "tier3_hint": "Phương án đúng là **[D]** (*After the event, researchers and locals searched for metal-laced rock fragments over the area of impact, but no such objects were ever reported discovered.*).\n\n**Phân tích chi tiết:**\nTiểu hành tinh chứa nhiều kim loại và đá. Nếu sau vụ nổ, các nhà nghiên cứu tìm kiếm trên diện rộng nhưng tuyệt đối không phát hiện bất kỳ mảnh đá chứa kim loại nào, điều này làm suy yếu nghiêm trọng kết luận vật thể đó là tiểu hành tinh (nhiều khả năng là sao chổi băng bụi đã bốc hơi).\n\n• (A) sai vì tìm thấy vật liệu của tiểu hành tinh sẽ củng cố chứ không làm suy yếu kết luận.\n• (B) sai vì việc vật thể nguyên vẹn qua tầng khí quyển dưới cũng củng cố giả thuyết tiểu hành tinh bền chắc hơn sao chổi.\n• (C) sai vì giải thích cơ chế nổ không giúp phân biệt vật thể là sao chổi hay tiểu hành tinh.",
            "strategic_tip": "Mẹo Princeton Review (Weaken): Để làm suy yếu một kết luận loại trừ (A chứ không phải B), hãy tìm bằng chứng mâu thuẫn trực tiếp với đặc tính vật lý cốt lõi của A.",
            "pooe_breakdown": "• [D] ĐÚNG: Không tìm thấy mảnh đá chứa kim loại làm suy yếu kết luận về tiểu hành tinh kim loại.\n• [A] Loại vì củng cố (support) kết luận của Kulik.\n• [B] Loại vì cũng củng cố giả thuyết tiểu hành tinh.\n• [C] Loại vì cơ chế nổ không chứng minh thiên thể là loại nào.",
            "option_explanations": {
                "A": "Loại A — tìm thấy khoáng chất đặc trưng của tiểu hành tinh trong thân cây củng cố chứ không làm suy yếu kết luận.",
                "B": "Loại B — vật thể không bị vỡ vụn sớm củng cố tính bền vững của tiểu hành tinh so với sao chổi.",
                "C": "Loại C — áp suất và nhiệt độ làm nổ vật thể xảy ra với cả sao chổi lẫn tiểu hành tinh, không làm suy yếu luận điểm.",
                "D": "ĐÁP ÁN ĐÚNG. Không tìm thấy bất kỳ mảnh vụn kim loại nào chứng minh thiên thể không phải tiểu hành tinh chứa kim loại."
            }
        },
        # --- Q14 ---
        {
            "id": 14,
            "master_id": "PR_RW_14",
            "q_number": 14,
            "q_label": "RW #14",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Information and Ideas • Command of Evidence (Textual Claims)",
            "passage": "Following a prolific career producing paintings and mixed media art centered around her Native American heritage and focused on socio-political commentary, Jaune Quick-to-See Smith became the first Native American painter whose work has appeared in the National Gallery of Art. According to an Associated Press journalist, Smith was shocked that her “I See Red: Target” was the first painting on canvas done by a Native American artist to enter the museum’s collection, although the journalist went on to clarify that the museum had previously featured Indigenous art.",
            "prompt": "Which finding, if true, would most directly support the journalist’s clarification?",
            "options": [
                {"key": "A", "text": "Smith had other pieces of mixed-media art that had previously appeared in the museum."},
                {"key": "B", "text": "The museum featured a traveling exhibition consisting entirely of pottery by Native American artists shortly before the acquisition of Smith’s piece."},
                {"key": "C", "text": "Earlier museum exhibitions that featured Indigenous art only included works that were on loan from other cultural institutions."},
                {"key": "D", "text": "Smith believed that art by Native Americans was undervalued and thus that the museum’s failure to acquire Native American art was unsurprising."}
            ],
            "options_raw": "A. Smith had other pieces of mixed-media art that had previously appeared in the museum.\nB. The museum featured a traveling exhibition consisting entirely of pottery by Native American artists shortly before the acquisition of Smith’s piece.\nC. Earlier museum exhibitions that featured Indigenous art only included works that were on loan from other cultural institutions.\nD. Smith believed that art by Native Americans was undervalued and thus that the museum’s failure to acquire Native American art was unsurprising.",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 8,
            "difficulty": "Hard",
            "princeton_strategy": "Command of Evidence - Nuanced Distinction",
            "tier1_hint": "Câu hỏi tìm thông tin củng cố lời giải thích của nhà báo: bảo tàng trước đây ĐÃ TỪNG trưng bày nghệ thuật của người bản địa (Indigenous art), dù bức tranh của Smith mới là bức tranh sơn dầu trên toan đầu tiên ĐƯỢC MUA VÀO BỘ SƯU TẬP (entered the museum's collection).",
            "tier2_hint": "Chú ý sự khác biệt giữa 'tác phẩm nằm trong bộ sưu tập vĩnh viễn của bảo tàng' (permanent collection) và 'tác phẩm được bảo tàng mang ra trưng bày' (exhibited / featured). Cần một lý do giải thích vì sao bảo tàng từng trưng bày tác phẩm của người bản địa nhưng chưa từng sở hữu chúng trong bộ sưu tập.",
            "tier3_hint": "Phương án đúng là **[C]** (*Earlier museum exhibitions that featured Indigenous art only included works that were on loan from other cultural institutions.*).\n\n**Phân tích chi tiết:**\nNếu các triển lãm nghệ thuật bản địa trước đây của bảo tàng chỉ bao gồm các tác phẩm mượn tạm từ các tổ chức văn hóa khác (on loan), điều này giải thích trọn vẹn tại sao bảo tàng vừa từng trưng bày nghệ thuật bản địa, vừa chưa từng có bức tranh nào của người bản địa trong bộ sưu tập chính thức của mình.\n\n• (A) sai vì bài đọc chỉ rõ tác phẩm của Smith là lần đầu tiên xuất hiện trong bộ sưu tập.\n• (B) sai vì đồ gốm (pottery) không giải thích được sự phân biệt giữa việc sở hữu bộ sưu tập và trưng bày tranh toan.\n• (D) sai vì suy nghĩ cá nhân của Smith không làm rõ được thực tế trưng bày của bảo tàng.",
            "strategic_tip": "Mẹo Princeton Review: Phân biệt rõ sự khác nhau giữa 'sở hữu/thuộc bộ sưu tập' (in the collection) và 'mượn để triển lãm' (on loan / exhibited).",
            "pooe_breakdown": "• [C] ĐÚNG: Các tác phẩm bản địa trước đây chỉ là đồ mượn (on loan) giải thích vì sao bảo tàng đã từng trưng bày nhưng chưa từng sở hữu trong bộ sưu tập.\n• [A] Loại vì mâu thuẫn với thông tin Smith lần đầu vào bảo tàng.\n• [B] Loại vì đồ gốm không làm rõ được sự việc.\n• [D] Loại vì quan điểm cá nhân không chứng minh được sự việc.",
            "option_explanations": {
                "A": "Loại A — mâu thuẫn trực tiếp với thông tin rằng đây là tác phẩm đầu tiên của Smith xuất hiện ở bảo tàng.",
                "B": "Loại B — triển lãm đồ gốm lưu động không giải thích rõ tại sao tranh bản địa chưa từng nằm trong bộ sưu tập vĩnh viễn.",
                "C": "ĐÁP ÁN ĐÚNG. Các triển lãm trước chỉ mượn hiện vật từ nơi khác (on loan) giải thích hoàn hảo vì sao bảo tàng từng trưng bày nhưng bộ sưu tập chưa từng sở hữu.",
                "D": "Loại D — niềm tin của cá nhân Smith không cung cấp dữ liệu khách quan để chứng minh lời nhà báo."
            }
        },
        # --- Q15 ---
        {
            "id": 15,
            "master_id": "PR_RW_15",
            "q_number": 15,
            "q_label": "RW #15",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Information and Ideas • Inferences (Logical Completion)",
            "passage": "A drawback when studying how people evaluate others’ ideologies upon a first meeting is that the studies are conducted in controlled settings with proscribed inputs, which may not fully account for the intricacies of spontaneous daily interactions. To properly simulate circumstances that can affect initial impressions of ideologies, researchers strive to include a broad range of conditions for these initial meetings. But since the researchers can’t reasonably mimic every potential kind of social encounter, they therefore ________",
            "prompt": "Which choice most logically completes the text?",
            "options": [
                {"key": "A", "text": "must allow for a reasonable margin of error in their studies and understand that the controlled nature of the study may affect the authenticity of the interactions."},
                {"key": "B", "text": "can’t create a meaningful study without compromising the rigorous research conditions that the scientific method demands."},
                {"key": "C", "text": "should focus on other questions of behavioral research, which better lend themselves to a practical implementation and are thus more useful."},
                {"key": "D", "text": "will need to supplement the data by having the subjects give additional information about how their first impressions change after more interactions."}
            ],
            "options_raw": "A. must allow for a reasonable margin of error in their studies and understand that the controlled nature of the study may affect the authenticity of the interactions.\nB. can’t create a meaningful study without compromising the rigorous research conditions that the scientific method demands.\nC. should focus on other questions of behavioral research, which better lend themselves to a practical implementation and are thus more useful.\nD. will need to supplement the data by having the subjects give additional information about how their first impressions change after more interactions.",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 8,
            "difficulty": "Hard",
            "princeton_strategy": "Inferences - Restraint & Logical Consequence",
            "tier1_hint": "Đọc kỹ câu dẫn trước ô trống: Các nhà nghiên cứu không thể mô phỏng mọi tình huống giao tiếp xã hội trong đời thực. Từ nối 'therefore' đòi hỏi một kết luận thực tế và hợp lý về thái độ của họ đối với kết quả nghiên cứu.",
            "tier2_hint": "Vì môi trường phòng thí nghiệm có kiểm soát (controlled nature) không thể tái hiện 100% sự phức tạp tự phát ngoài đời, nên các nhà khoa học phải chấp nhận điều gì? Hãy tìm lựa chọn thể hiện sự chấp nhận sai số hợp lý (margin of error) và tính xác thực tương đối của tương tác.",
            "tier3_hint": "Phương án đúng là **[A]** (*must allow for a reasonable margin of error in their studies and understand that the controlled nature of the study may affect the authenticity of the interactions.*).\n\n**Phân tích chi tiết:**\nDo không thể mô phỏng mọi tình huống giao tiếp tự phát hàng ngày, các nhà nghiên cứu buộc phải chấp nhận một biên độ sai số nhất định (margin of error) và hiểu rằng tính chất kiểm soát có thể ảnh hưởng đến tính chân thực của tương tác.\n\n• (B) sai vì là Extreme Language (khẳng định không thể tạo ra nghiên cứu có ý nghĩa là quá tiêu cực).\n• (C) sai vì khuyên từ bỏ nghiên cứu để chuyển sang chủ đề khác là quá đà.\n• (D) sai vì bài đọc chỉ nghiên cứu về ấn tượng lần đầu gặp mặt (first meeting), không nghiên cứu sự thay đổi sau nhiều lần gặp.",
            "strategic_tip": "Mẹo Princeton Review (Inferences): Trong phần hoàn thành câu suy luận, đáp án đúng luôn là nhận định vừa phải, thận trọng (Restraint), không bao giờ là kết luận cực đoan hoặc khuyên từ bỏ nghiên cứu.",
            "pooe_breakdown": "• [A] ĐÚNG: Chấp nhận biên độ sai số (margin of error) là hệ quả logic khi không thể mô phỏng toàn bộ đời thực.\n• [B] Loại vì Extreme Language (khẳng định không thể làm nghiên cứu ý nghĩa).\n• [C] Loại vì khuyên từ bỏ đề tài là vô lý.\n• [D] Loại vì bài chỉ tập trung vào lần gặp đầu tiên.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. Chấp nhận biên sai số (margin of error) và nhận thức được giới hạn của phòng thí nghiệm là kết luận thận trọng và chuẩn xác.",
                "B": "Loại B — cực đoan quá mức khi cho rằng không thể thực hiện một nghiên cứu có ý nghĩa nếu không làm hỏng phương pháp khoa học.",
                "C": "Loại C — văn bản không hề khuyến nghị các nhà nghiên cứu nên bỏ cuộc và chuyển sang hướng nghiên cứu khác.",
                "D": "Loại D — bài đọc tập trung vào ấn tượng đầu tiên (first impressions) chứ không mở rộng ra các lần tương tác sau này."
            }
        },
        # --- Q16 ---
        {
            "id": 16,
            "master_id": "PR_RW_16",
            "q_number": 16,
            "q_label": "RW #16",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Information and Ideas • Inferences (Logical Completion)",
            "passage": "A ritualistic artistic tradition, sand drawing has become a means of communication among inhabitants of the Vanuatu islands and has been recognized by UNESCO as a Masterpiece of the Oral and Intangible Heritage of Humanity. The drawings serve as records and means of communicating rituals, lore, local history, farming techniques, choreography, and architectural designs. However, sand drawings have more recently come to be used for advertising and tourism. In response to formal protests against the use of sand drawing for profit, UNESCO has sponsored the creation of the Save Sand Drawings Action Committee program, as ________",
            "prompt": "Which choice most logically completes the text?",
            "options": [
                {"key": "A", "text": "the rich history behind this art form has been celebrated by the international art community."},
                {"key": "B", "text": "there is growing concern that an art form is being employed for reasons other than its original purpose."},
                {"key": "C", "text": "the inhabitants of the islands recognize the importance of change and progress in any art form."},
                {"key": "D", "text": "sand drawings continue to be used to communicate information by evolving to include modern cultural events."}
            ],
            "options_raw": "A. the rich history behind this art form has been celebrated by the international art community.\nB. there is growing concern that an art form is being employed for reasons other than its original purpose.\nC. the inhabitants of the islands recognize the importance of change and progress in any art form.\nD. sand drawings continue to be used to communicate information by evolving to include modern cultural events.",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 9,
            "difficulty": "Hard",
            "princeton_strategy": "Inferences - Contextual Motivation Alignment",
            "tier1_hint": "Chú ý lý do dẫn đến hành động của UNESCO: 'In response to formal protests against the use of sand drawing for profit...' (Để đáp lại các cuộc biểu tình chính thức chống lại việc thương mại hóa tranh cát). Ô trống bắt đầu bằng 'as...' (bởi vì...), yêu cầu giải thích nguyên nhân UNESCO thành lập Ủy ban hành động bảo vệ tranh cát.",
            "tier2_hint": "Tranh cát vốn là truyền thống nghi lễ và giao tiếp thiêng liêng, nhưng nay lại bị lợi dụng cho quảng cáo và du lịch kiếm lời. Người dân phản đối vì nghệ thuật đang bị sử dụng sai mục đích ban đầu. Hãy tìm phương án phản ánh mối lo ngại này.",
            "tier3_hint": "Phương án đúng là **[B]** (*there is growing concern that an art form is being employed for reasons other than its original purpose.*).\n\n**Phân tích chi tiết:**\nUNESCO thành lập ủy ban bảo vệ tranh cát để phản hồi lại các khiếu nại về việc tranh cát bị trục lợi thương mại (quảng cáo, du lịch), tức là có mối lo ngại ngày càng tăng về việc loại hình nghệ thuật này bị sử dụng ngoài mục đích ban đầu của nó.\n\n• (A) sai vì việc quốc tế tôn vinh không giải thích được lý do lập ủy ban phản ứng trước các phản đối thương mại hóa.\n• (C) sai vì người dân đảo phản đối (protest) chứ không hề hoan nghênh sự thay đổi này.\n• (D) sai vì tranh cát không chỉ đơn giản là tiến hóa để thêm sự kiện hiện đại mà đang bị lạm dụng thương mại.",
            "strategic_tip": "Mẹo Princeton Review: Khi mệnh đề kết quả là 'phản ứng lại sự phản đối' (in response to protests), mệnh đề nguyên nhân bắt buộc phải giải thích mối lo ngại hay vấn đề tiêu cực đang diễn ra.",
            "pooe_breakdown": "• [B] ĐÚNG: growing concern that art is employed for reasons other than original purpose khớp hoàn hảo với lý do người dân biểu tình chống thương mại hóa.\n• [A] Loại vì việc tôn vinh không giải thích lý do biểu tình.\n• [C] Loại vì người dân phản đối chứ không ủng hộ thay đổi.\n• [D] Loại vì không nhắc đến khía cạnh trục lợi thương mại.",
            "option_explanations": {
                "A": "Loại A — lịch sử phong phú được quốc tế tôn vinh không giải thích được tại sao UNESCO phải lập ban bảo vệ trước sự thương mại hóa.",
                "B": "ĐÁP ÁN ĐÚNG. Mối lo ngại ngày càng tăng về việc nghệ thuật bị dùng sai mục đích ban đầu giải thích hoàn hảo việc thành lập ủy ban bảo vệ.",
                "C": "Loại C — cư dân biểu tình phản đối việc thương mại hóa, họ không coi đó là sự tiến bộ được hoan nghênh.",
                "D": "Loại D — phương án này né tránh vấn đề thương mại hóa vì lợi nhuận vốn là nguyên nhân dẫn đến biểu tình."
            }
        },
        # --- Q17 ---
        {
            "id": 17,
            "master_id": "PR_RW_17",
            "q_number": 17,
            "q_label": "RW #17",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Standard English Conventions • Boundaries (Clauses & Conjunctions)",
            "passage": "Extreme trans-Neptunian objects (ETNOs) are a group of objects in the outer region of the Solar System whose orbits seem to cluster. Some astronomers have hypothesized the existence of a Planet Nine that is affecting the ETNOs’ ________ though other astronomers assert that the orbits are a result of observational bias.",
            "prompt": "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "options": [
                {"key": "A", "text": "orbits:"},
                {"key": "B", "text": "orbits;"},
                {"key": "C", "text": "orbits"},
                {"key": "D", "text": "orbits,"}
            ],
            "options_raw": "A. orbits:\nB. orbits;\nC. orbits\nD. orbits,",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 9,
            "difficulty": "Hard",
            "princeton_strategy": "Grammar - Dependent Clause Boundary",
            "tier1_hint": "Xác định cấu trúc ngữ pháp giữa hai vế câu: Vế đầu là mệnh đề độc lập 'Some astronomers have hypothesized the existence of a Planet Nine that is affecting the ETNOs' orbits'. Vế sau mở đầu bằng liên từ phụ thuộc 'though'.",
            "tier2_hint": "Mệnh đề phụ thuộc chỉ sự tương phản mở đầu bằng 'though' (though other astronomers assert...) đứng ở cuối câu sau một mệnh đề độc lập. Theo quy tắc dấu câu tiếng Anh chuẩn, khi một mệnh đề phụ thuộc trạng ngữ tương phản đứng sau mệnh đề chính, cần dùng dấu phẩy để ngăn cách.",
            "tier3_hint": "Phương án đúng là **[D]** (*orbits,*).\n\n**Phân tích chi tiết:**\nPhần đầu là mệnh đề độc lập hoàn chỉnh. Mệnh đề sau là mệnh đề phụ thuộc tương phản mở đầu bằng liên từ 'though' (*though other astronomers assert...*). Dấu phẩy trước 'though' là quy tắc chuẩn xác để phân cách mệnh đề phụ thuộc này.\n\n• (A) dấu hai chấm (:) sai vì vế sau không phải danh sách liệt kê hay lời giải thích cho 'orbits'.\n• (B) dấu chấm phẩy (;) sai vì sau dấu chấm phẩy bắt buộc phải là một mệnh đề độc lập (nhưng ở đây vế sau có liên từ phụ thuộc 'though').\n• (C) không có dấu câu sai vì tạo ra sự dính câu giữa hai mệnh đề.",
            "strategic_tip": "Mẹo Princeton Review (Punctuation): Dấu chấm phẩy (;) chỉ được nối hai mệnh đề độc lập (Independent Clauses). Nếu mệnh đề sau có liên từ phụ thuộc như 'though, although, because, since', tuyệt đối KHÔNG dùng dấu chấm phẩy.",
            "pooe_breakdown": "• [D] ĐÚNG: Dấu phẩy phân tách mệnh đề chính và mệnh đề phụ thuộc tương phản mở đầu bằng 'though'.\n• [A] Loại dấu hai chấm vì vế sau không giải thích định nghĩa.\n• [B] Loại dấu chấm phẩy vì vế sau có though nên không độc lập.\n• [C] Loại vì thiếu dấu câu ngăn cách.",
            "option_explanations": {
                "A": "Loại A — dấu hai chấm dùng để báo hiệu danh sách hoặc giải thích, không dùng trước mệnh đề nhượng bộ 'though'.",
                "B": "Loại B — dấu chấm phẩy bắt buộc phải nối 2 mệnh đề độc lập; vế sau có 'though' là mệnh đề phụ thuộc.",
                "C": "Loại C — không có dấu phẩy sẽ khiến câu bị dính liền và ngắt nhịp sai cú pháp.",
                "D": "ĐÁP ÁN ĐÚNG. Dấu phẩy ngăn cách mệnh đề chính với mệnh đề phụ thuộc trạng ngữ chỉ sự tương phản mở đầu bằng 'though'."
            }
        },
        # --- Q18 ---
        {
            "id": 18,
            "master_id": "PR_RW_18",
            "q_number": 18,
            "q_label": "RW #18",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Standard English Conventions • Boundaries (Compound Sentences & FANBOYS)",
            "passage": "By monitoring the gases that are emitted from the regions surrounding volcanoes, scientists can make predictions about what volcanic activity—or inactivity—can be expected. For example, a volcano releases sulfur dioxide (SO2) when magma is close to the surface, indicating that an eruption might occur soon. In other instances, magma releases sulfur gases, which interact with the groundwater to produce hydrogen sulfide ________ the presence of this compound signifies that the volcano is stable.",
            "prompt": "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "options": [
                {"key": "A", "text": "(H2S)"},
                {"key": "B", "text": "(H2S) but"},
                {"key": "C", "text": "(H2S),"},
                {"key": "D", "text": "(H2S), but"}
            ],
            "options_raw": "A. (H2S)\nB. (H2S) but\nC. (H2S),\nD. (H2S), but",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 9,
            "difficulty": "Hard",
            "princeton_strategy": "Grammar - FANBOYS & Comma Splice Prevention",
            "tier1_hint": "Xác định các thành phần câu trước và sau ô trống: Vế trước 'In other instances, magma releases sulfur gases, which interact with the groundwater to produce hydrogen sulfide (H2S)' là một mệnh đề hoàn chỉnh. Vế sau 'the presence of this compound signifies that the volcano is stable' cũng là một mệnh đề độc lập có đầy đủ Chủ ngữ và Vị ngữ.",
            "tier2_hint": "Để nối hai mệnh đề độc lập (Independent Clauses), tiếng Anh chuẩn mực yêu cầu phải dùng cấu trúc: 'Dấu phẩy + Liên từ đẳng lập FANBOYS' (, but / , and) hoặc 'Dấu chấm phẩy'. Kiểm tra xem phương án nào có đầy đủ cả dấu phẩy lẫn liên từ phù hợp.",
            "tier3_hint": "Phương án đúng là **[D]** (*(H2S), but*).\n\n**Phân tích chi tiết:**\nCả hai vế trước và sau ô trống đều là mệnh đề độc lập (có đầy đủ Chủ ngữ và Động từ chia thì). Hai mệnh đề độc lập chỉ có thể được kết nối bằng công thức: `, + FANBOYS` (dấu phẩy kèm liên từ kết hợp như *but*).\n\n• (A) sai vì tạo ra lỗi Run-on sentence (hai mệnh đề độc lập ghép liền nhau không có dấu hay từ nối).\n• (B) sai vì thiếu dấu phẩy trước liên từ *but* khi nối hai mệnh đề độc lập.\n• (C) sai vì tạo ra lỗi Comma Splice (dùng dấu phẩy đơn độc để nối hai mệnh đề độc lập).",
            "strategic_tip": "Mẹo Princeton Review (FANBOYS): Công thức vàng của College Board: Independent Clause + `, + FANBOYS` + Independent Clause. Thiếu dấu phẩy (phương án B) hay thiếu liên từ (phương án C - Comma Splice) đều là các lỗi ngữ pháp nghiêm trọng.",
            "pooe_breakdown": "• [D] ĐÚNG: , but kết nối chuẩn xác hai mệnh đề độc lập.\n• [A] Loại vì lỗi Run-on (không dấu câu).\n• [B] Loại vì thiếu dấu phẩy trước liên từ but.\n• [C] Loại vì lỗi Comma Splice (chỉ có dấu phẩy đơn độc).",
            "option_explanations": {
                "A": "Loại A — lỗi Run-on sentence: hai mệnh đề độc lập dính liền vào nhau không có dấu câu hay liên từ.",
                "B": "Loại B — khi nối 2 mệnh đề độc lập bằng FANBOYS (but), bắt buộc phải có dấu phẩy đứng trước.",
                "C": "Loại C — lỗi kinh điển Comma Splice: dùng một dấu phẩy đơn lẻ để nối hai mệnh đề độc lập là sai quy tắc.",
                "D": "ĐÁP ÁN ĐÚNG. Cấu trúc chuẩn mực: dấu phẩy kết hợp liên từ đẳng lập ', but' kết nối 2 mệnh đề độc lập."
            }
        },
        # --- Q19 ---
        {
            "id": 19,
            "master_id": "PR_RW_19",
            "q_number": 19,
            "q_label": "RW #19",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Standard English Conventions • Boundaries (Conjunctive Adverbs & Semicolons)",
            "passage": "Iridescence in fish is generally a result of tiny crystals in their scales or skin. The ghost catfish, a transparent aquatic species, doesn’t have those ________ its muscles have microscopic striped structures that bend light.",
            "prompt": "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "options": [
                {"key": "A", "text": "crystals instead,"},
                {"key": "B", "text": "crystals, instead;"},
                {"key": "C", "text": "crystals; instead,"},
                {"key": "D", "text": "crystals, instead,"}
            ],
            "options_raw": "A. crystals instead,\nB. crystals, instead;\nC. crystals; instead,\nD. crystals, instead,",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 10,
            "difficulty": "Hard",
            "princeton_strategy": "Grammar - Conjunctive Adverbs Transition Punctuation",
            "tier1_hint": "Xác định hai mệnh đề độc lập trong câu:\nMệnh đề 1: 'The ghost catfish, a transparent aquatic species, doesn't have those crystals'.\nMệnh đề 2: 'its muscles have microscopic striped structures that bend light'.\nTừ nối ở đây là trạng từ liên kết 'instead'.",
            "tier2_hint": "Khi dùng một trạng từ liên kết (Conjunctive Adverb như however, therefore, instead) để kết nối hai mệnh đề độc lập, quy tắc dấu câu bắt buộc là:\n`Mệnh đề 1 ; trạng từ liên kết , Mệnh đề 2` (Dấu chấm phẩy trước trạng từ, dấu phẩy sau trạng từ).",
            "tier3_hint": "Phương án đúng là **[C]** (*crystals; instead,*).\n\n**Phân tích chi tiết:**\nCả hai vế đều là mệnh đề độc lập hoàn chỉnh. Trạng từ liên kết 'instead' đứng giữa hai mệnh đề độc lập đòi hỏi phải có dấu chấm phẩy đi trước và dấu phẩy đi sau: `; instead,`.\n\n• (A) và (D) đều tạo thành lỗi Comma Splice vì chỉ dùng dấu phẩy để nối hai mệnh đề độc lập.\n• (B) đặt dấu phẩy trước 'instead' và dấu chấm phẩy sau là sai vị trí, biến 'instead' thành phần phụ vô nghĩa của mệnh đề 1.",
            "strategic_tip": "Mẹo Princeton Review: Nhớ quy tắc kinh điển cho Conjunctive Adverbs nối 2 mệnh đề độc lập: `; however,` | `; therefore,` | `; instead,` | `; furthermore,`.",
            "pooe_breakdown": "• [C] ĐÚNG: ; instead, chuẩn mực cú pháp nối 2 mệnh đề độc lập bằng trạng từ liên kết.\n• [A] Loại vì lỗi Comma Splice.\n• [B] Loại vì đảo ngược vị trí dấu câu.\n• [D] Loại vì dấu phẩy không thể nối 2 câu độc lập.",
            "option_explanations": {
                "A": "Loại A — thiếu dấu chấm phẩy để ngắt hai mệnh đề độc lập, tạo thành lỗi Comma Splice.",
                "B": "Loại B — dấu phẩy đặt trước 'instead' và dấu chấm phẩy đặt sau là sai trật tự cú pháp tiếng Anh.",
                "C": "ĐÁP ÁN ĐÚNG. Quy tắc chuẩn mực nối 2 câu độc lập bằng trạng từ liên kết: '; instead,'.",
                "D": "Loại D — hai dấu phẩy kẹp 'instead' không thể thay thế dấu chấm phẩy để nối hai mệnh đề độc lập."
            }
        },
        # --- Q20 ---
        {
            "id": 20,
            "master_id": "PR_RW_20",
            "q_number": 20,
            "q_label": "RW #20",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Standard English Conventions • Form, Structure, and Sense (Verb Tense & Aspect)",
            "passage": "The G.I. Bill was enacted in 1944 to ensure that veterans returning from World War II could access housing and education. By 1951, about 8 million veterans ________ advantage of the bill’s educational benefits, leading to a more than twofold increase in the number of degrees issued by American colleges and universities.",
            "prompt": "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "options": [
                {"key": "A", "text": "had taken"},
                {"key": "B", "text": "took"},
                {"key": "C", "text": "take"},
                {"key": "D", "text": "will take"}
            ],
            "options_raw": "A. had taken\nB. took\nC. take\nD. will take",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 10,
            "difficulty": "Hard",
            "princeton_strategy": "Grammar - Past Perfect with 'By + Past Time'",
            "tier1_hint": "Quan sát trạng từ chỉ thời gian ở đầu câu: 'By 1951' (Tính đến trước năm 1951). Cần xác định thì của động từ diễn tả hành động hoàn tất trước một thời điểm cụ thể trong quá khứ.",
            "tier2_hint": "Quy tắc thời thì tiếng Anh: Cụm trạng từ 'By + mốc thời gian trong quá khứ' (By 1951, By the time...) là dấu hiệu nhận biết đặc trưng của thì Quá khứ hoàn thành (Past Perfect: had + V3/ed), diễn tả hành động đã xảy ra và hoàn tất trước mốc thời gian đó.",
            "tier3_hint": "Phương án đúng là **[A]** (*had taken*).\n\n**Phân tích chi tiết:**\nCụm từ chỉ thời gian 'By 1951' (Tính đến trước năm 1951) đòi hỏi động từ phải chia ở thì Quá khứ hoàn thành (Past Perfect) để biểu thị 8 triệu cựu chiến binh đã hoàn tất việc hưởng lợi ích trước mốc năm 1951.\n\n• (B) *took* (Quá khứ đơn) sai vì không diễn tả được tính hoàn tất trước một mốc thời gian 'By + past year'.\n• (C) *take* (Hiện tại đơn) và (D) *will take* (Tương lai đơn) sai hoàn toàn về dòng thời gian lịch sử.",
            "strategic_tip": "Mẹo Princeton Review (Verbs): 'By + past date' (ví dụ: By 1951, By yesterday) $\\rightarrow$ luôn luôn chọn Past Perfect (had + V3/ed). Không bao giờ chọn Simple Past.",
            "pooe_breakdown": "• [A] ĐÚNG: had taken (Quá khứ hoàn thành) khớp hoàn hảo với cấu trúc 'By 1951'.\n• [B] Loại took vì Quá khứ đơn không thể hiện tính hoàn tất trước mốc thời gian.\n• [C] Loại hiện tại đơn.\n• [D] Loại tương lai đơn.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. Cấu trúc 'By + mốc quá khứ' (By 1951) bắt buộc dùng thì Quá khứ hoàn thành 'had taken'.",
                "B": "Loại B — thì quá khứ đơn 'took' chỉ dùng cho mốc thời gian xác định (In 1951), không dùng với giới từ 'By'.",
                "C": "Loại C — sự việc xảy ra từ thập niên 1950, không thể dùng thì hiện tại đơn 'take'.",
                "D": "Loại D — thì tương lai đơn 'will take' hoàn toàn sai lệch niên đại lịch sử."
            }
        },
        # --- Q21 ---
        {
            "id": 21,
            "master_id": "PR_RW_21",
            "q_number": 21,
            "q_label": "RW #21",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Standard English Conventions • Form, Structure, and Sense (Subject-Verb Agreement)",
            "passage": "In a study published in 2023, geneticist Paul Schmidt and colleagues demonstrated that cold weather selects for certain traits in the fruit fly Drosophila melanogaster, showing that the seasonal fluctuation of autumn and winter temperatures ________ the frequency of over 100 alleles in the fruit fly population.",
            "prompt": "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "options": [
                {"key": "A", "text": "were influencing"},
                {"key": "B", "text": "have influenced"},
                {"key": "C", "text": "influence"},
                {"key": "D", "text": "influences"}
            ],
            "options_raw": "A. were influencing\nB. have influenced\nC. influence\nD. influences",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 10,
            "difficulty": "Hard",
            "princeton_strategy": "Grammar - Subject-Verb Agreement with Prepositional Phrases",
            "tier1_hint": "Xác định chủ ngữ cốt lõi của mệnh đề sau từ 'that': 'the seasonal fluctuation of autumn and winter temperatures'. Hãy loại bỏ các cụm giới từ phụ để tìm danh từ hạt nhân.",
            "tier2_hint": "Cụm 'of autumn and winter temperatures' là cụm giới từ bổ nghĩa, không làm chủ ngữ. Danh từ hạt nhân là 'the seasonal fluctuation' (danh từ số ít không đếm được). Chủ ngữ số ít ở thì hiện tại đòi hỏi một động từ chia số ít (thêm đuôi -s/-es).",
            "tier3_hint": "Phương án đúng là **[D]** (*influences*).\n\n**Phân tích chi tiết:**\nChủ ngữ thực sự của động từ là danh từ số ít 'fluctuation' (sự dao động). Các danh từ số nhiều đứng gần như 'temperatures' chỉ nằm trong cụm giới từ 'of autumn and winter temperatures'. Chủ ngữ số ít đi với động từ số ít 'influences'.\n\n• (A) *were influencing*, (B) *have influenced*, và (C) *influence* đều là các dạng động từ số nhiều, sai hoàn toàn quy tắc hòa hợp Chủ-Vị.",
            "strategic_tip": "Mẹo Princeton Review (Subject-Verb Agreement): Khi có cụm giới từ dài chèn giữa (ví dụ: 'The fluctuation of temperatures'), hãy lấy bút gạch tạm cụm giới từ đó đi để nhìn thấy ngay Chủ ngữ hạt nhân: 'The fluctuation [influences]'.",
            "pooe_breakdown": "• [D] ĐÚNG: influences (động từ số ít) hòa hợp chuẩn xác với chủ ngữ số ít 'the seasonal fluctuation'.\n• [A] Loại were số nhiều.\n• [B] Loại have số nhiều.\n• [C] Loại influence số nhiều.",
            "option_explanations": {
                "A": "Loại A — 'were influencing' là dạng số nhiều, trong khi chủ ngữ chính là danh từ số ít 'fluctuation'.",
                "B": "Loại B — 'have influenced' là dạng số nhiều, không hòa hợp với chủ ngữ số ít.",
                "C": "Loại C — 'influence' là động từ nguyên mẫu số nhiều, không hòa hợp với 'fluctuation'.",
                "D": "ĐÁP ÁN ĐÚNG. 'influences' (ngôi thứ 3 số ít) hòa hợp hoàn hảo với danh từ trung tâm 'the seasonal fluctuation'."
            }
        },
        # --- Q22 ---
        {
            "id": 22,
            "master_id": "PR_RW_22",
            "q_number": 22,
            "q_label": "RW #22",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Standard English Conventions • Boundaries (Parallel Structures & Modifiers)",
            "passage": "Suki Seokyeong Kang, a visual artist from South Korea, combines painting, sculpture, video, and dance to create multimedia installations informed by historical art forms. Her project Black Mat Oriole explores the subject of gridded space, with influences ranging from Jeongganbo, a Korean musical notation system written on ________ to woven reed mats.",
            "prompt": "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "options": [
                {"key": "A", "text": "paper divided into regular boxes"},
                {"key": "B", "text": "paper, divided into regular boxes"},
                {"key": "C", "text": "paper divided into regular boxes,"},
                {"key": "D", "text": "paper, divided into regular boxes,"}
            ],
            "options_raw": "A. paper divided into regular boxes\nB. paper, divided into regular boxes\nC. paper divided into regular boxes,\nD. paper, divided into regular boxes,",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 10,
            "difficulty": "Hard",
            "princeton_strategy": "Grammar - Parallel Idiom 'ranging from X to Y'",
            "tier1_hint": "Nhận diện cấu trúc song hành của thành ngữ: 'with influences ranging from X to Y' (với những ảnh hưởng trải dài từ X đến Y). Ở đây X là 'Jeongganbo, a Korean musical notation system written on paper divided into regular boxes', còn Y là 'woven reed mats'.",
            "tier2_hint": "Cụm danh từ 'a Korean musical notation system written on paper divided into regular boxes' là phần giải thích đồng vị (appositive) cho 'Jeongganbo'. Cụm này mở đầu bằng dấu phẩy sau 'Jeongganbo', do đó bắt buộc phải kết thúc bằng một dấu phẩy để đóng thành phần phụ trước khi sang từ nối 'to' của cấu trúc 'ranging from X to Y'. Giữa 'paper' và 'divided' không được ngắt dấu phẩy vì 'divided into regular boxes' là mệnh đề phân từ hạn định cần thiết để bổ nghĩa cho 'paper'.",
            "tier3_hint": "Phương án đúng là **[C]** (*paper divided into regular boxes,*).\n\n**Phân tích chi tiết:**\nCấu trúc 'ranging from X to Y' có X là cụm đồng vị giải nghĩa cho Jeongganbo. Mệnh đề phân từ 'divided into regular boxes' là thành phần hạn định bổ nghĩa trực tiếp cho 'paper' (không dùng dấu phẩy giữa chúng). Cần dấu phẩy ở cuối cụm để đóng thành phần đồng vị trước khi tiếp tục cấu trúc song hành với 'to woven reed mats'.\n\n• (A) thiếu dấu phẩy đóng cụm đồng vị trước 'to'.\n• (B) và (D) ngắt dấu phẩy sai giữa danh từ và cụm phân từ bổ nghĩa hạn định.",
            "strategic_tip": "Mẹo Princeton Review: Trong cấu trúc 'ranging from X, [appositive modifier], to Y', luôn cần cặp dấu phẩy bao quanh thành phần đồng vị bổ nghĩa. Không bao giờ đặt dấu phẩy tùy tiện giữa danh từ và cụm phân từ hạn định (essential participle).",
            "pooe_breakdown": "• [C] ĐÚNG: paper divided into regular boxes, đóng chuẩn xác cụm đồng vị trước khi chuyển sang 'to Y'.\n• [A] Loại vì thiếu dấu phẩy đóng cụm đồng vị.\n• [B] Loại vì ngắt dấu phẩy sai trước divided và thiếu dấu phẩy sau boxes.\n• [D] Loại vì thừa dấu phẩy sau paper.",
            "option_explanations": {
                "A": "Loại A — thiếu dấu phẩy sau 'boxes' để đóng cụm danh từ đồng vị bổ nghĩa cho Jeongganbo trước từ 'to'.",
                "B": "Loại B — ngắt dấu phẩy sau 'paper' làm gián đoạn cụm phân từ hạn định, lại thiếu dấu phẩy đóng cụm.",
                "C": "ĐÁP ÁN ĐÚNG. 'divided into regular boxes' không có dấu phẩy sau paper (hạn định) và có dấu phẩy sau boxes để đóng cụm đồng vị.",
                "D": "Loại D — thừa dấu phẩy sau 'paper', làm sai quy tắc bổ ngữ hạn định."
            }
        },
        # --- Q23 ---
        {
            "id": 23,
            "master_id": "PR_RW_23",
            "q_number": 23,
            "q_label": "RW #23",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Standard English Conventions • Boundaries (Colons for Explanation)",
            "passage": "A study published by Howard University evolutionary biologist Omar Cirilli and a team of 18 others in 2022 compares two comprehensive taxonomies of horses and features a paleoclimatic analysis, which could explain why modern horses evolved in North America instead of Europe or ________ four million years ago, when the oldest common ancestor of modern equines evolved, the North American continent was significantly drier than that of Eurasia, which yielded more open grasslands, an appropriate habitat for the ancestors of modern horses.",
            "prompt": "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "options": [
                {"key": "A", "text": "Asia,"},
                {"key": "B", "text": "Asia"},
                {"key": "C", "text": "Asia and"},
                {"key": "D", "text": "Asia:"}
            ],
            "options_raw": "A. Asia,\nB. Asia\nC. Asia and\nD. Asia:",
            "is_grid_in": False,
            "correct_answer": "D",
            "pdf_page": 11,
            "difficulty": "Hard",
            "princeton_strategy": "Grammar - Colon for Elaboration & Boundary",
            "tier1_hint": "Xác định cấu trúc của câu văn lớn: Vế đầu 'A study... could explain why modern horses evolved in North America instead of Europe or Asia' là một mệnh đề hoàn chỉnh đầy đủ ý nghĩa. Vế sau 'four million years ago... the North American continent was significantly drier...' đóng vai trò gì đối với vế đầu?",
            "tier2_hint": "Vế thứ hai là một câu hoàn chỉnh đưa ra lời giải thích chi tiết cho lý do vì sao ngựa lại tiến hóa ở Bắc Mỹ (do 4 triệu năm trước khí hậu Bắc Mỹ khô hơn tạo ra nhiều đồng cỏ hơn). Theo quy tắc College Board, sau một mệnh đề độc lập hoàn chỉnh, dấu hai chấm (:) được dùng để giới thiệu phần giải thích chi tiết hoặc minh chứng làm rõ cho mệnh đề đó.",
            "tier3_hint": "Phương án đúng là **[D]** (*Asia:*).\n\n**Phân tích chi tiết:**\nVế trước là một mệnh đề độc lập hoàn chỉnh ('...instead of Europe or Asia'). Vế sau là một mệnh đề độc lập giải thích trực tiếp tại sao ngựa lại tiến hóa ở Bắc Mỹ (lý do khí hậu 4 triệu năm trước). Dấu hai chấm (:) là dấu câu chuẩn xác để phân cách giữa một mệnh đề độc lập và phần giải thích bổ trợ cho nó.\n\n• (A) dấu phẩy (,) sai vì tạo thành lỗi Comma Splice (ghép 2 mệnh đề độc lập bằng dấu phẩy).\n• (B) không có dấu câu sai vì tạo ra lỗi Run-on sentence.\n• (C) 'Asia and' sai vì làm thay đổi nghĩa và gây rối loạn cấu trúc liên kết.",
            "strategic_tip": "Mẹo Princeton Review (Colons): Dấu hai chấm (:) chỉ có thể đứng sau một mệnh đề độc lập hoàn chỉnh (Independent Clause). Khi vế sau giải thích hoặc chứng minh cho vế trước, dấu hai chấm là lựa chọn số 1 của College Board.",
            "pooe_breakdown": "• [D] ĐÚNG: Asia: dấu hai chấm phân cách hoàn hảo giữa câu độc lập và phần giải thích chi tiết đằng sau.\n• [A] Loại vì lỗi Comma Splice.\n• [B] Loại vì lỗi Run-on.\n• [C] Loại vì liên từ 'and' làm hỏng cấu trúc câu.",
            "option_explanations": {
                "A": "Loại A — dùng dấu phẩy tạo thành lỗi Comma Splice vì nối hai mệnh đề độc lập mà không có liên từ FANBOYS.",
                "B": "Loại B — không có dấu câu tạo thành lỗi Run-on sentence nghiêm trọng.",
                "C": "Loại C — 'Asia and' biến vế sau thành một cụm lộn xộn không thể kết nối mạch lạc.",
                "D": "ĐÁP ÁN ĐÚNG. Dấu hai chấm (:) đứng sau mệnh đề độc lập để mở ra lời giải thích chi tiết ở vế sau."
            }
        },
        # --- Q24 ---
        {
            "id": 24,
            "master_id": "PR_RW_24",
            "q_number": 24,
            "q_label": "RW #24",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Expression of Ideas • Transitions (Logical Direction)",
            "passage": "Delos, an Aegean island rich in historical significance and a UNESCO World Heritage Site since 1990, contains one of the most concentrated collections of surviving Hellenistic Greek marble sculpture anywhere in the world. ________ the island is known to contain a high concentration of bronze statues dating from the Roman period that followed the island’s peak Hellenistic era.",
            "prompt": "Which choice completes the text with the most logical transition?",
            "options": [
                {"key": "A", "text": "Similarly,"},
                {"key": "B", "text": "Thus,"},
                {"key": "C", "text": "In addition,"},
                {"key": "D", "text": "Despite this,"}
            ],
            "options_raw": "A. Similarly,\nB. Thus,\nC. In addition,\nD. Despite this,",
            "is_grid_in": False,
            "correct_answer": "A",
            "pdf_page": 11,
            "difficulty": "Hard",
            "princeton_strategy": "Transitions - Parallel Similarity vs Simple Addition",
            "tier1_hint": "Xác định mối quan hệ logic giữa hai câu: Câu 1 nêu đảo Delos có bộ sưu tập tượng điêu khắc cẩm thạch Hy Lạp cổ đại có mật độ cao nhất thế giới (high concentration of Hellenistic Greek marble sculpture). Câu 2 nêu hòn đảo cũng có mật độ tượng đồng La Mã cổ đại rất cao (high concentration of bronze statues).",
            "tier2_hint": "Hai câu văn có cấu trúc và ý nghĩa tương đồng song hành hoàn hảo: cùng chỉ ra sự phong phú đặc biệt về một loại hình cổ vật trên hòn đảo ở hai thời kỳ khác nhau. Khi hai sự kiện hoặc đặc điểm tương đồng được đặt cạnh nhau để so sánh, hãy tìm từ nối chỉ sự tương tự (Similarity).",
            "tier3_hint": "Phương án đúng là **[A]** (*Similarly,*).\n\n**Phân tích chi tiết:**\nCả hai câu đều nêu bật việc đảo Delos chứa một mật độ rất cao các bức tượng lịch sử (câu 1: tượng cẩm thạch thời Hy Lạp; câu 2: tượng đồng thời La Mã). Hai chi tiết này tương tự nhau về mặt bản chất và ý nghĩa, do đó từ nối chỉ sự tương đồng 'Similarly' (Tương tự như vậy) là chính xác nhất.\n\n• (B) *Thus* (Do đó) sai vì câu 2 không phải là kết quả nhân quả từ câu 1.\n• (C) *In addition* (Thêm vào đó) mặc dù là từ nối bổ sung, nhưng không thể hiện được tính tương quan song hành đặc trưng giữa hai đặc điểm giống nhau như 'Similarly'.\n• (D) *Despite this* (Mặc dù vậy) sai vì hai câu không có quan hệ tương phản.",
            "strategic_tip": "Mẹo Princeton Review (Transitions): Khi hai câu cùng chia sẻ một cấu trúc diễn đạt song hành và so sánh hai trường hợp tương tự nhau ('contains one of the most concentrated... / is known to contain a high concentration...'), từ nối 'Similarly' luôn chuẩn xác hơn các từ bổ sung thông thường.",
            "pooe_breakdown": "• [A] ĐÚNG: Similarly thể hiện chính xác mối quan hệ tương đồng giữa 2 phát hiện tượng có mật độ cao trên đảo Delos.\n• [B] Loại Thus vì không phải quan hệ nhân quả.\n• [C] Loại In addition vì kém chính xác hơn sự so sánh tương đồng.\n• [D] Loại Despite this vì không có sự tương phản.",
            "option_explanations": {
                "A": "ĐÁP ÁN ĐÚNG. 'Similarly,' kết nối chuẩn xác hai hiện tượng tương đồng song hành về mật độ tượng cổ phong phú trên đảo.",
                "B": "Loại B — 'Thus,' biểu thị quan hệ nguyên nhân - kết quả, không phù hợp ở đây.",
                "C": "Loại C — 'In addition,' chỉ bổ sung đơn thuần, không làm nổi bật được mối liên kết tương đồng mạnh mẽ như 'Similarly'.",
                "D": "Loại D — 'Despite this,' biểu thị sự nhượng bộ/đối lập, trong khi hai câu đồng thuận hỗ trợ nhau."
            }
        },
        # --- Q25 ---
        {
            "id": 25,
            "master_id": "PR_RW_25",
            "q_number": 25,
            "q_label": "RW #25",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Expression of Ideas • Transitions (General to Specific)",
            "passage": "Honeycomb serves many functions for bee communities: it provides a venue for food storage, a nest for bee larvae and pupae, and housing for adult bees. Bees construct honeycomb from wax they produce in their abdominal glands, but much about the process that bees use to create the combs remains unknown. ________ researchers have yet to determine whether bees rely on genetic instincts or on learned behaviors when building the cells of a honeycomb.",
            "prompt": "Which choice completes the text with the most logical transition?",
            "options": [
                {"key": "A", "text": "Nevertheless,"},
                {"key": "B", "text": "Specifically,"},
                {"key": "C", "text": "Likewise,"},
                {"key": "D", "text": "Still,"}
            ],
            "options_raw": "A. Nevertheless,\nB. Specifically,\nC. Likewise,\nD. Still,",
            "is_grid_in": False,
            "correct_answer": "B",
            "pdf_page": 11,
            "difficulty": "Hard",
            "princeton_strategy": "Transitions - Specification / Elaboration",
            "tier1_hint": "Xác định mối quan hệ giữa hai câu cuối: Câu trước nêu nhận định khái quát rằng 'much about the process that bees use to create the combs remains unknown' (nhiều điều về quá trình ong xây tổ vẫn còn là bí ẩn chưa được biết tới). Câu sau nêu chi tiết: 'researchers have yet to determine whether bees rely on genetic instincts or learned behaviors...'.",
            "tier2_hint": "Câu sau đưa ra một ví dụ cụ thể, làm rõ chính xác một trong những 'điều chưa biết' đó là gì (liệu ong dựa vào bản năng di truyền hay hành vi học hỏi). Mối quan hệ từ ý chung sang chi tiết cụ thể đòi hỏi từ nối chỉ sự cụ thể hóa.",
            "tier3_hint": "Phương án đúng là **[B]** (*Specifically,*).\n\n**Phân tích chi tiết:**\nCâu trước nêu khẳng định chung: quy trình xây tổ của ong vẫn còn nhiều điều chưa sáng tỏ. Câu sau đi vào chi tiết một khía cạnh cụ thể mà giới khoa học chưa xác định được (bản năng di truyền hay học hỏi). Từ nối 'Specifically' (Cụ thể là) là lựa chọn duy nhất phản ánh sự cụ thể hóa này.\n\n• (A) *Nevertheless* và (D) *Still* đều là các từ nối tương phản (Contradictors), trong khi hai câu cùng hướng.\n• (C) *Likewise* sai vì câu sau không so sánh với một sinh vật khác.",
            "strategic_tip": "Mẹo Princeton Review (Transitions): Khi gặp câu hỏi từ nối, hãy phân loại ngay 4 nhóm logic: Tiếp nối/Cụ thể hóa (Continuer/Specifically), Tương phản (Contradictor/However), Nguyên nhân-Kết quả (Cause/Thus). Ở đây 2 đáp án (A) và (D) cùng nhóm tương phản sẽ tự triệt tiêu nhau.",
            "pooe_breakdown": "• [B] ĐÚNG: Specifically (cụ thể là) dẫn dắt từ nhận định chung sang ví dụ cụ thể về điều chưa biết.\n• [A] Loại Nevertheless vì là từ nối tương phản.\n• [C] Loại Likewise vì không so sánh sự tương đương.\n• [D] Loại Still vì cùng nghĩa tương phản với A.",
            "option_explanations": {
                "A": "Loại A — 'Nevertheless,' là từ nối tương phản, trong khi câu sau đi cùng hướng giải thích chi tiết cho câu trước.",
                "B": "ĐÁP ÁN ĐÚNG. 'Specifically,' làm rõ chính xác bí ẩn chưa biết được đề cập ở câu trước là gì.",
                "C": "Loại C — 'Likewise,' dùng để so sánh hai sự vật tương đương, không dùng để nêu chi tiết cụ thể hóa.",
                "D": "Loại D — 'Still,' mang nghĩa tương phản giống Nevertheless, cả hai từ cùng nhóm tự triệt tiêu nhau."
            }
        },
        # --- Q26 ---
        {
            "id": 26,
            "master_id": "PR_RW_26",
            "q_number": 26,
            "q_label": "RW #26",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Expression of Ideas • Rhetorical Synthesis (Goal Alignment)",
            "passage": "While researching a topic, a student has taken the following notes:\n• Los Kjarkas is a musical group from Bolivia.\n• The group’s most widely known song is “Llorando se fue.”\n• An unauthorized translation of “Llorando se fue” was the basis of the 1980s dance hit “Lambada.”\n• Los Kjarkas’s songs often cover themes of romance and loss and incorporate traditional Andean instruments such as the charango and the quena.\n• The charango is a stringed instrument similar to a small guitar.\n• The quena is a type of flute.",
            "prompt": "The student wants to introduce the music of Los Kjarkas to a new audience. Which choice most effectively uses relevant information from the notes to accomplish this goal?",
            "options": [
                {"key": "A", "text": "Los Kjarkas incorporates traditional Andean instruments such as the charango (similar to a small guitar) and the quena (a type of flute)."},
                {"key": "B", "text": "Los Kjarkas’s most widely known song is “Llorando se fue,” an unauthorized translation of which was the basis of the 1980s dance hit “Lambada.”"},
                {"key": "C", "text": "The songs of Los Kjarkas, a musical group from Bolivia, often cover themes of romance and loss and incorporate traditional Andean instruments."},
                {"key": "D", "text": "Los Kjarkas is a musical group from Bolivia whose songs involve the charango and the quena."}
            ],
            "options_raw": "A. Los Kjarkas incorporates traditional Andean instruments such as the charango (similar to a small guitar) and the quena (a type of flute).\nB. Los Kjarkas’s most widely known song is “Llorando se fue,” an unauthorized translation of which was the basis of the 1980s dance hit “Lambada.”\nC. The songs of Los Kjarkas, a musical group from Bolivia, often cover themes of romance and loss and incorporate traditional Andean instruments.\nD. Los Kjarkas is a musical group from Bolivia whose songs involve the charango and the quena.",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 12,
            "difficulty": "Hard",
            "princeton_strategy": "Rhetorical Synthesis - Goal Keyword Matching",
            "tier1_hint": "Đọc kỹ mục tiêu của học sinh trong câu hỏi: 'introduce the music of Los Kjarkas to a new audience' (giới thiệu âm nhạc của nhóm Los Kjarkas cho đối tượng khán giả mới chưa biết đến họ).",
            "tier2_hint": "Để giới thiệu với khán giả mới, câu văn cần cung cấp cả bối cảnh xuất xứ (nhóm nhạc đến từ Bolivia) VÀ đặc trưng tổng quan về âm nhạc của nhóm (chủ đề bài hát và nhạc cụ đặc trưng). Hãy tìm lựa chọn bao hàm đầy đủ thông tin giới thiệu toàn diện này.",
            "tier3_hint": "Phương án đúng là **[C]** (*The songs of Los Kjarkas, a musical group from Bolivia, often cover themes of romance and loss and incorporate traditional Andean instruments.*).\n\n**Phân tích chi tiết:**\nPhương án này hoàn thành xuất sắc mục tiêu giới thiệu âm nhạc của Los Kjarkas cho khán giả mới vì nó vừa nêu rõ nhóm nhạc này đến từ Bolivia, vừa giới thiệu phong cách âm nhạc (chủ đề tình yêu và mất mát, kết hợp nhạc cụ truyền thống vùng Andes).\n\n• (A) sai vì không nói rõ Los Kjarkas là ai, đến từ đâu (khán giả mới sẽ không hiểu).\n• (B) sai vì chỉ tập trung vào một bài hát và vụ dịch bài 'Lambada', không giới thiệu phong cách âm nhạc tổng thể.\n• (D) sai vì quá ngắn ngủi, chỉ nhắc đến tên hai nhạc cụ mà bỏ qua chủ đề âm nhạc cốt lõi.",
            "strategic_tip": "Mẹo Princeton Review (Rhetorical Synthesis): Khi đề bài yêu cầu giới thiệu cho 'a new audience', câu trả lời BẮT BUỘC phải chứa thông tin nền tảng (background info, như: 'a musical group from Bolivia'). Bất kỳ câu nào bỏ quên thông tin xuất xứ đều bị loại ngay.",
            "pooe_breakdown": "• [C] ĐÚNG: Nêu rõ xuất xứ (Bolivia) và đặc trưng âm nhạc (romance, loss, Andean instruments) cho khán giả mới.\n• [A] Loại vì thiếu thông tin xuất xứ nhóm nhạc cho khán giả mới.\n• [B] Loại vì chỉ nói về một bài hát đơn lẻ và Lambada.\n• [D] Loại vì quá hẹp, thiếu bức tranh âm nhạc tổng thể.",
            "option_explanations": {
                "A": "Loại A — thiếu thông tin cơ bản cho khán giả mới: không nêu Los Kjarkas là một nhóm nhạc đến từ Bolivia.",
                "B": "Loại B — tập trung vào vụ dịch lời bài hát 'Lambada' thay vì giới thiệu tổng quan phong cách âm nhạc.",
                "C": "ĐÁP ÁN ĐÚNG. Giới thiệu trọn vẹn nhóm nhạc Bolivia, phong cách chủ đề bài hát và nhạc cụ vùng Andes cho khán giả mới.",
                "D": "Loại D — quá sơ sài, chỉ liệt kê tên 2 nhạc cụ mà không làm nổi bật được bản sắc âm nhạc của nhóm."
            }
        },
        # --- Q27 ---
        {
            "id": 27,
            "master_id": "PR_RW_27",
            "q_number": 27,
            "q_label": "RW #27",
            "module_code": "RW_Harder",
            "module_title": "Module 1: Harder Reading & Writing",
            "section": "Reading and Writing",
            "module_num": 1,
            "topic": "Expression of Ideas • Rhetorical Synthesis (Findings Presentation)",
            "passage": "While researching a topic, a student has taken the following notes:\n• Rats have facial whiskers near their snouts and smaller, finer supraorbital whiskers above their eyes.\n• Neuroscientist Ann Clemens and colleagues conducted a study investigating the supraorbital whiskers of rats.\n• They discovered that the bases of the supraorbital whiskers are surrounded by a ring of nerve cells highly sensitive to movements in all directions.\n• The researchers found that numbing rats’ supraorbital whiskers with lidocaine reduced the rats’ ability to sense wind currents.\n• They hypothesized that supraorbital whiskers are specialized structures used by rats to detect air currents from approaching predators.\n• Previous research found that trimming rats’ facial whiskers reduced the rats’ ability to sense wind currents.",
            "prompt": "The student wants to present Clemens and colleagues’ study and their findings. Which choice most effectively uses relevant information from the notes to accomplish this goal?",
            "options": [
                {"key": "A", "text": "Rats have facial whiskers near their snouts and supraorbital whiskers above their eyes, both of which are associated with their ability to sense wind currents."},
                {"key": "B", "text": "Rats’ supraorbital whiskers are used to detect air currents from approaching predators."},
                {"key": "C", "text": "A study of the supraorbital whiskers of rats found that the bases of these whiskers are surrounded by a ring of nerve cells sensitive to movement and that the application of a numbing chemical to the whiskers reduces the rats’ ability to sense wind currents."},
                {"key": "D", "text": "Research has found that trimming rats’ facial whiskers, which are located near their snouts, reduces the rats’ ability to sense wind currents."}
            ],
            "options_raw": "A. Rats have facial whiskers near their snouts and supraorbital whiskers above their eyes, both of which are associated with their ability to sense wind currents.\nB. Rats’ supraorbital whiskers are used to detect air currents from approaching predators.\nC. A study of the supraorbital whiskers of rats found that the bases of these whiskers are surrounded by a ring of nerve cells sensitive to movement and that the application of a numbing chemical to the whiskers reduces the rats’ ability to sense wind currents.\nD. Research has found that trimming rats’ facial whiskers, which are located near their snouts, reduces the rats’ ability to sense wind currents.",
            "is_grid_in": False,
            "correct_answer": "C",
            "pdf_page": 12,
            "difficulty": "Hard",
            "princeton_strategy": "Rhetorical Synthesis - Study & Findings Articulation",
            "tier1_hint": "Đọc kỹ mục tiêu của học sinh: 'present Clemens and colleagues’ study and their findings' (trình bày nghiên cứu của nhóm Clemens và các phát hiện thực nghiệm của họ).",
            "tier2_hint": "Mục tiêu yêu cầu nêu CẢ nghiên cứu về râu trên mắt (supraorbital whiskers) LẪN các phát hiện thực tế (vòng tế bào thần kinh nhạy cảm chuyển động và việc làm tê râu làm giảm khả năng cảm nhận luồng gió). Lựa chọn đúng phải trực tiếp đề cập đến các phát hiện cụ thể này của nhóm Clemens.",
            "tier3_hint": "Phương án đúng là **[C]** (*A study of the supraorbital whiskers of rats found that the bases of these whiskers are surrounded by a ring of nerve cells sensitive to movement and that the application of a numbing chemical to the whiskers reduces the rats’ ability to sense wind currents.*).\n\n**Phân tích chi tiết:**\nPhương án này nêu bật trọn vẹn cả nghiên cứu lẫn hai phát hiện thực nghiệm then chốt của nhóm Clemens: (1) gốc râu trên mắt được bao quanh bởi vòng tế bào thần kinh nhạy cảm, và (2) bôi thuốc tê lidocaine làm giảm khả năng cảm nhận gió.\n\n• (A) sai vì chỉ khái quát về hai loại râu, không trình bày phát hiện của nghiên cứu.\n• (B) sai vì chỉ nêu giả thuyết (hypothesized) chứ không phải phát hiện thực nghiệm (findings).\n• (D) sai vì nêu phát hiện của nghiên cứu trước đó về râu mặt (facial whiskers), không phải nghiên cứu của Clemens.",
            "strategic_tip": "Mẹo Princeton Review: Phân biệt rõ giữa 'Giả thuyết' (hypothesis) và 'Phát hiện thực nghiệm' (findings). Khi đề bài yêu cầu trình bày findings, hãy tìm các câu tóm tắt dữ liệu đo lường cụ thể được tìm thấy trong thí nghiệm.",
            "pooe_breakdown": "• [C] ĐÚNG: Trình bày chính xác nghiên cứu về râu trên mắt và 2 phát hiện thực nghiệm then chốt.\n• [A] Loại vì không nhắc đến nghiên cứu của Clemens.\n• [B] Loại vì chỉ nêu giả thuyết về kẻ săn mồi.\n• [D] Loại vì nói về nghiên cứu cũ đối với râu mặt.",
            "option_explanations": {
                "A": "Loại A — chỉ giới thiệu cấu tạo chung của hai loại râu chuột, hoàn toàn bỏ qua nghiên cứu và phát hiện của Clemens.",
                "B": "Loại B — đây chỉ là giả thuyết về kẻ săn mồi (hypothesized), không phải phát hiện thực nghiệm chứng minh.",
                "C": "ĐÁP ÁN ĐÚNG. Nêu bật trọn vẹn nghiên cứu về râu trên mắt và cả hai phát hiện khoa học cụ thể của nhóm.",
                "D": "Loại D — nói về nghiên cứu trước đó (previous research) về râu quanh mõm, lạc đề hoàn toàn."
            }
        }
    ]
    return questions
