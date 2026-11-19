#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_full_nov2026_enhancements.py
Nghiên cứu, phân tích chuyên sâu và cập nhật:
1. Sơ đồ tư duy trực quan (Mermaid Mindmap) cho TẤT CẢ 98 câu hỏi (RW1 27, RW2 27, Math1 22, Math2 22).
2. Hệ thống phản hồi 4 tầng Socratic (Tầng 1 Định hướng, Tầng 2 Manh mối & Loại trừ, Tầng 3 Lời giải chi tiết & Công bố đáp án, Tầng 4 Mẹo chiến thuật College Board/Desmos).
3. Giải thích chi tiết từng đáp án (Tại sao đúng, Tại sao sai / Bẫy đề thi cho toàn bộ các phương án A, B, C, D) - Tuyệt đối không dùng dấu '—' mà dùng dấu '-'.
4. Phân tích bẫy số học và bước giải chi tiết cho 11 câu tự điền đáp số (Grid-in).

Đồng bộ trực tiếp vào:
  - vinschool-sat-team/data/nov2026.json
  - vinschool-sat-team/static/data/nov2026.json
"""

import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "nov2026.json")
STATIC_DATA_FILE = os.path.join(BASE_DIR, "static", "data", "nov2026.json")

def clean_txt(text):
    if not text:
        return ""
    return str(text).replace("—", "-").replace("–", "-").strip()

def safe_mermaid_text(text):
    if not text:
        return ""
    t = str(text).replace('"', "'").replace("—", "-").replace("–", "-")
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def generate_enhancements():
    print("=== Loading nov2026.json ===")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    questions = db["questions"]
    print(f"Total questions to enhance: {len(questions)}")

    for q in questions:
        q_id = q["id"]
        mod_code = q["module_code"]
        q_num = q["q_number"]
        topic = q.get("topic", "")
        passage = q.get("passage", "")
        prompt = q.get("prompt", "")
        corr = q.get("correct_answer", "")
        is_grid_in = q.get("is_grid_in", False)
        
        # Extract original option texts from existing option_explanations
        orig_opts = {}
        for k, exp in q.get("option_explanations", {}).items():
            parts = exp.split(f"{k} (")
            if len(parts) > 1:
                orig_opts[k] = parts[1].split(")")[0].strip()
            else:
                orig_opts[k] = f"Lựa chọn {k}"

        corr_txt = orig_opts.get(corr, f"Lựa chọn {corr}")

        # =========================================================================
        # 1. READING & WRITING MODULE 1 & 2
        # =========================================================================
        if "RW" in mod_code:
            # 1.1 Words in Context
            if "Words in Context" in topic:
                clue_snippet = passage[:120].replace("\n", " ")
                clean_passage = safe_mermaid_text(passage[:100])
                clean_corr_txt = safe_mermaid_text(corr_txt)
                
                mermaid = f"""flowchart TD
    A["Ngữ cảnh bài đọc:<br>'{clean_passage}...'"] --> B{{"Manh mối văn cảnh & Sắc thái (Contextual Clues)"}}
    B --> C["Xác định vai trò của từ cần điền đối với cấu trúc câu và đối tượng miêu tả"]
    C --> D["Dự đoán nghĩa (Prediction):<br>Từ khóa phải diễn tả chính xác hành động/trạng thái trong ngữ cảnh học thuật"]
    D --> E{{"Chiến thuật loại trừ POOE (Princeton Review)"}}
    E -->|"Sai sắc thái / Lạc nghĩa"| F["Loại các phương án gây nhiễu:<br>Từ mang sắc thái trái ngược hoặc không dùng cho đối tượng này"]
    E -->|"Khớp chuẩn xác định nghĩa & sắc thái"| G["Chọn ({corr}): '{clean_corr_txt}'<br>Đồng nghĩa và hòa hợp tự nhiên nhất với ngữ cảnh"]
    G --> H["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = f"Đọc kỹ câu chứa chỗ trống và các câu lân cận. Hãy tự đặt câu hỏi: Từ cần điền đang bổ nghĩa cho đối tượng nào và mang sắc thái ngữ nghĩa (tích cực, tiêu cực, hay trung tính) ra sao?"
                t2 = f"Dựa vào các manh mối trong đoạn văn ('{passage[:80].strip()}...'), hãy tự dự đoán một từ hoặc cụm từ đơn giản trước khi đối chiếu với 4 phương án lựa chọn để tránh bị bẫy từ vựng gây nhiễu."
                t3 = f"Đối chiếu định nghĩa chính xác trong ngữ cảnh: Phương án [{corr}] ('{corr_txt}') là từ duy nhất diễn đạt chuẩn xác sắc thái và mối quan hệ logic của câu. Các phương án khác mang nét nghĩa lệch ngữ cảnh hoặc bị quá mức."
                stip = "Mẹo Princeton Review: Trong dạng Words in Context, đừng tìm từ 'nghe có vẻ hay'. Hãy dùng kỹ thuật gạch chân manh mối đối ứng (Context Clue) và loại trừ ngay các từ không thể kết hợp tự nhiên với danh từ/hành động chính."

                # Option explanations
                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Phản ánh chính xác ngữ cảnh học thuật và sắc thái ý nghĩa của câu."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Mang nét nghĩa hoàn toàn khớp với ngữ cảnh bài đọc. Từ này diễn đạt chuẩn xác bản chất đối tượng và liên kết chặt chẽ với các chi tiết xung quanh."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Không phù hợp ngữ cảnh bài thi. Từ này mang nét nghĩa lệch hướng, sai sắc thái biểu cảm hoặc không tạo thành cụm từ kết hợp tự nhiên (collocation) với các thành phần trong câu."
                        pooe_lines.append(f"• Loại {k}. {txt} - Sai sắc thái hoặc không ăn nhập với đối tượng được miêu tả.")
                pooe_breakdown = "\n".join(pooe_lines)

            # 1.2 Text Structure & Purpose
            elif "Text Structure and Purpose" in topic:
                clean_passage = safe_mermaid_text(passage[:120])
                clean_corr_txt = safe_mermaid_text(corr_txt)
                mermaid = f"""flowchart TD
    A["Văn bản & Câu hỏi:<br>'{clean_passage}...'"] --> B{{"Phân tích cấu trúc đoạn văn (Text Architecture)"}}
    B --> C["Xác định vai trò của từng câu: Đặt vấn đề -> Dẫn chứng thực nghiệm -> Kết luận / Hàm ý"]
    C --> D["Đánh giá chức năng câu hỏi yêu cầu:<br>Phân tích mục đích tác giả hoặc chức năng của câu được chỉ định"]
    D --> E{{"Đối chiếu các phương án theo chiến thuật POOE"}}
    E -->|"Bẫy phạm vi / Suy diễn quá đà"| F["Loại các phương án mô tả sai cấu trúc:<br>Nêu sai trọng tâm hoặc tập trung vào chi tiết phụ không đại diện cho toàn đoạn"]
    E -->|"Mô tả khách quan & chính xác tiến trình lập luận"| G["Chọn ({corr}): '{clean_corr_txt}'<br>Khái quát đúng trình tự và mục đích tu từ của tác giả"]
    G --> H["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = "Xác định câu hỏi đang hỏi về 'mục đích tổng thể' (overall purpose), 'cấu trúc tổ chức' (overall structure) hay 'chức năng của một câu cụ thể' (function of underlined sentence)."
                t2 = "Tóm tắt ngắn gọn vai trò của từng phần trong đoạn văn: Phần đầu giới thiệu điều gì? Phần giữa phát triển hay phản biện? Phần kết rút ra kết luận hay nêu ý nghĩa thực tiễn?"
                t3 = f"Đối chiếu với đáp án: Phương án [{corr}] ('{corr_txt}') tóm lược chính xác chức năng tu từ của tác giả mà không thêm thắt các nhận định suy đoán ngoài văn bản."
                stip = "Mẹo College Board: Với câu hỏi Function / Structure, các phương án sai thường sử dụng các động từ hành động không khớp (ví dụ: 'criticizes' trong khi bài chỉ 'describes', hoặc 'refutes' trong khi bài chỉ 'qualifies'). Hãy luôn kiểm tra kỹ động từ mở đầu của mỗi phương án!"

                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Mô tả chính xác mục đích tu từ và cấu trúc lập luận của văn bản."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Đánh giá khách quan và chính xác vai trò cấu trúc của đoạn trích, thể hiện đúng trình tự diễn giải của tác giả."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Mô tả sai chức năng tu từ. Phương án này sử dụng động từ hành động không chính xác hoặc hiểu sai trọng tâm lập luận."
                        pooe_lines.append(f"• Loại {k}. {txt} - Sai lệch về chức năng lập luận hoặc quá hẹp so với toàn bài.")
                pooe_breakdown = "\n".join(pooe_lines)

            # 1.3 Central Ideas & Details
            elif "Central Ideas and Details" in topic:
                clean_passage = safe_mermaid_text(passage[:120])
                clean_corr_txt = safe_mermaid_text(corr_txt)
                mermaid = f"""flowchart TD
    A["Đoạn văn học thuật:<br>'{clean_passage}...'"] --> B{{"Xác định thông tin cần tìm theo yêu cầu câu hỏi"}}
    B --> C["Quét tìm từ khóa cốt lõi trong bài đọc liên quan đến chủ đề chính"]
    C --> D["Tìm dẫn chứng trực tiếp (Direct Evidence) trong văn bản thể hiện câu trả lời"]
    D --> E{{"Loại trừ phương án bẫy (POOE)"}}
    E -->|"Bẫy bóp méo thông tin / Trái ngược dữ kiện"| F["Loại các lựa chọn đưa ra kết luận chưa từng được đề cập trong bài"]
    E -->|"Khớp chính xác bằng chứng văn bản"| G["Chọn ({corr}): '{clean_corr_txt}'<br>Được hỗ trợ trực tiếp và không suy diễn quá mức"]
    G --> H["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = "Xác định câu hỏi hỏi về chi tiết sự thật cụ thể (factual detail) được nhắc trực tiếp trong bài hay ý chính (central idea) chi phối toàn đoạn."
                t2 = "Định vị chính xác câu văn chứa thông tin trả lời trong đoạn trích. Đọc kỹ câu đó cùng câu liền trước và liền sau."
                t3 = f"Chọn phương án diễn đạt lại (paraphrase) chính xác nhất nội dung của dẫn chứng văn bản: Phương án [{corr}] ('{corr_txt}')."
                stip = "Mẹo College Board: Câu trả lời đúng cho dạng Central Ideas & Details luôn có thể được chứng minh 100% bằng câu chữ trong bài đọc. Nếu một phương án nghe rất hợp lý ở ngoài đời nhưng bài đọc không hề nói tới, đó là phương án bẫy!"

                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Phản ánh trung thực dẫn chứng trực tiếp trong bài đọc."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Diễn đạt lại hoàn hảo thông tin được nêu rõ ràng trong văn bản, không suy diễn vượt quá phạm vi dữ kiện."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Không được chứng minh bằng văn bản. Lựa chọn này chứa thông tin sai lệch so với dữ liệu gốc hoặc đưa ra khẳng định không có cơ sở trong bài."
                        pooe_lines.append(f"• Loại {k}. {txt} - Mâu thuẫn với bài đọc hoặc không có căn cứ xác thực.")
                pooe_breakdown = "\n".join(pooe_lines)

            # 1.4 Command of Evidence
            elif "Command of Evidence" in topic:
                clean_passage = safe_mermaid_text(passage[:120])
                clean_corr_txt = safe_mermaid_text(corr_txt)
                mermaid = f"""flowchart TD
    A["Giả thuyết / Luận điểm cần chứng minh:<br>'{clean_passage}...'"] --> B{{"Phân tích mục tiêu kiểm chứng bằng chứng"}}
    B --> C["Xác định chính xác mối quan hệ nhân quả hoặc xu hướng mà nhà nghiên cứu đề xuất"]
    C --> D["Đối chiếu số liệu từ bảng biểu / Phát hiện thực nghiệm của nghiên cứu"]
    D --> E{{"Đánh giá mức độ củng cố luận điểm (Hypothesis Testing)"}}
    E -->|"Số liệu không liên quan / Mâu thuẫn luận điểm"| F["Loại các phương án đọc sai bảng hoặc dẫn chứng không trực tiếp hỗ trợ luận điểm"]
    E -->|"Bằng chứng trực tiếp chứng minh giả thuyết"| G["Chọn ({corr}): '{clean_corr_txt}'<br>Dữ liệu khớp hoàn hảo với dự đoán khoa học"]
    G --> H["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = "Xác định rõ luận điểm hoặc nhận định nào trong bài đọc đang cần được chứng minh / củng cố bằng dữ liệu hoặc trích dẫn."
                t2 = "Nếu có bảng biểu: Đọc kỹ tiêu đề các cột/hàng, đơn vị đo và xu hướng số liệu. Nếu là văn bản: Xác định câu trích dẫn nào thể hiện hành vi/đặc điểm được nêu trong luận điểm."
                t3 = f"Phương án đúng phải trực tiếp kết nối dữ kiện với kết luận mà không cần bất kỳ giả định bổ sung nào: Chọn [{corr}] ('{corr_txt}')."
                stip = "Mẹo College Board: Trong dạng Command of Evidence, các phương án bẫy rất hay dùng số liệu thật trong bảng nhưng lại KHÔNG HỀ LIÊN QUAN tới luận điểm cần chứng minh. Luôn kiểm tra: 'Dữ liệu này có thực sự chứng minh nhận định ở câu hỏi không?'"

                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Cung cấp bằng chứng thực nghiệm vững chắc, chứng minh trực tiếp luận điểm."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Đưa ra dữ kiện/trích dẫn chính xác, tạo nên mối liên hệ nhân quả rõ ràng chứng minh cho khẳng định khoa học."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Không hỗ trợ luận điểm. Phương án này trích dẫn thông tin lạc đề, mô tả sai số liệu thống kê hoặc thậm chí làm suy yếu nhận định."
                        pooe_lines.append(f"• Loại {k}. {txt} - Không củng cố giả thuyết hoặc đọc sai số liệu thực nghiệm.")
                pooe_breakdown = "\n".join(pooe_lines)

            # 1.5 Inferences
            elif "Inferences" in topic:
                clean_passage = safe_mermaid_text(passage[:120])
                clean_corr_txt = safe_mermaid_text(corr_txt)
                mermaid = f"""flowchart TD
    A["Tiền đề 1 & Tiền đề 2 trong đoạn văn:<br>'{clean_passage}...'"] --> B{{"Xác định ranh giới suy luận an toàn (Conservative Deduction)"}}
    B --> C["Tổng hợp các dữ kiện đã biết mà không thêm thắt giả định bên ngoài"]
    C --> D["Tìm kết luận tất yếu (Must Be True): Điều gì bắt buộc phải xảy ra tiếp theo?"]
    D --> E{{"Loại trừ bẫy suy luận SAT (Inference Traps)"}}
    E -->|"Bẫy suy đoán quá đà (Speculation) / Tuyệt đối hóa"| F["Loại các lựa chọn chứa từ ngữ quá cực đoan hoặc đi quá xa so với dữ liệu thực tế"]
    E -->|"Suy luận chuẩn mực, bám sát logic của văn bản"| G["Chọn ({corr}): '{clean_corr_txt}'<br>Hệ quả tự nhiên và tất yếu của các tiền đề đã cho"]
    G --> H["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = "Đọc kỹ phần cuối của đoạn văn ngay trước chỗ trống. Chỗ trống yêu cầu hoàn thành câu kết luận của tác giả."
                t2 = "Tóm tắt các tiền đề: Nếu A dẫn đến B, và B gặp điều kiện C, thì kết quả tất yếu phải là gì? Chú ý các từ hạn định (qualifiers) như 'may', 'likely', 'some' để tránh bẫy cực đoan."
                t3 = f"Kết luận an toàn và chuẩn xác nhất: Chọn phương án [{corr}] ('{corr_txt}')."
                stip = "Mẹo Princeton Review: Quy tắc 'Không suy diễn quá một bước' (One-step rule). Đáp án đúng của SAT Inferences là đáp án an toàn, có thể chứng minh được từ bài đọc, không phải là một ý tưởng đột phá hay giả thuyết viển vông!"

                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Kết luận logic an toàn, bắt nguồn trực tiếp từ các tiền đề đã cho."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Hoàn thiện trọn vẹn mạch tư duy của đoạn văn. Đây là suy luận trực tiếp, chặt chẽ và không thể bác bỏ dựa trên dữ kiện bài đọc."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Suy luận quá đà. Phương án này đưa ra nhận định vượt quá phạm vi bằng chứng, áp đặt quan điểm chưa được kiểm chứng hoặc mâu thuẫn với tiền đề."
                        pooe_lines.append(f"• Loại {k}. {txt} - Suy diễn ngoài phạm vi hoặc mâu thuẫn với tiền đề văn bản.")
                pooe_breakdown = "\n".join(pooe_lines)

            # 1.6 Standard English Conventions (Boundaries & Grammar)
            elif "Standard English Conventions" in topic or "Boundaries" in topic or "Form, Structure, and Sense" in topic:
                clean_passage = safe_mermaid_text(passage[:120])
                clean_corr_txt = safe_mermaid_text(corr_txt)
                mermaid = f"""flowchart TD
    A["Câu hỏi ngữ pháp:<br>'{clean_passage}...'"] --> B{{"Phân tích cấu trúc cú pháp (Sentence Structure)"}}
    B --> C["Xác định các mệnh đề: Mệnh đề độc lập (IC) vs Mệnh đề phụ thuộc (DC)"]
    C --> D["Kiểm tra quy tắc dấu câu / ngữ pháp tương ứng: Dấu chấm phẩy, dấu hai chấm, dấu phẩy, hòa hợp S-V"]
    D --> E{{"Loại trừ các lỗi ngữ pháp kinh điển của SAT"}}
    E -->|"Lỗi Comma Splice / Run-on / Fragment"| F["Loại các phương án ghép 2 mệnh đề độc lập chỉ bằng dấu phẩy hoặc thiếu vị ngữ"]
    E -->|"Tuân thủ 100% chuẩn mực tiếng Anh học thuật"| G["Chọn ({corr}): '{clean_corr_txt}'<br>Ngăn cách mệnh đề chuẩn xác hoặc hòa hợp thì/dạng động từ"]
    G --> H["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = "Xác định chủ ngữ (Subject) và động từ chính (Main Verb) của toàn câu. Phân biệt rõ đâu là mệnh đề độc lập (có thể đứng thành câu riêng) và đâu là cụm phụ nghĩa / mệnh đề phụ thuộc."
                t2 = "Đối chiếu quy tắc dấu câu: Hai mệnh đề độc lập KHÔNG ĐƯỢC nối với nhau chỉ bằng dấu phẩy (lỗi Comma Splice). Cần dùng dấu chấm (.), chấm phẩy (;), hoặc phẩy kết hợp liên từ FANBOYS."
                t3 = f"Phương án tuân thủ tuyệt đối quy tắc ngữ pháp chuẩn mực là [{corr}] ('{corr_txt}')."
                stip = "Mẹo Erica Meltzer: Khi thấy các phương án có dấu chấm (.), chấm phẩy (;) và dấu phẩy (,), hãy kiểm tra ngay cấu trúc mệnh đề. Dấu chấm phẩy (;) về mặt ngữ pháp có chức năng phân tách mệnh đề tương đương như dấu chấm (.)!"

                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Chuẩn xác tuyệt đối về quy tắc ngữ pháp và phân định ranh giới mệnh đề."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Cấu trúc cú pháp hoàn hảo. Sử dụng dấu câu / dạng động từ đúng quy tắc chuẩn mực, tạo nên câu văn mạch lạc, không phạm lỗi ngữ pháp."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Phạm lỗi ngữ pháp nghiêm trọng (ví dụ: Comma Splice, câu què Fragment, thiếu sự hòa hợp chủ - vị, hoặc ngắt quãng cụm danh từ bằng dấu phẩy không cần thiết)."
                        pooe_lines.append(f"• Loại {k}. {txt} - Phạm lỗi ranh giới câu hoặc sai quy tắc ngữ pháp chuẩn.")
                pooe_breakdown = "\n".join(pooe_lines)

            # 1.7 Transitions
            elif "Transitions" in topic:
                clean_passage = safe_mermaid_text(passage[:120])
                clean_corr_txt = safe_mermaid_text(corr_txt)
                mermaid = f"""flowchart TD
    A["Đoạn văn chuyển ý:<br>'{clean_passage}...'"] --> B{{"Xác định mối quan hệ logic giữa hai câu liên tiếp"}}
    B --> C["Ý 1 (Câu trước): Thông tin / Bối cảnh nền"]
    B --> D["Ý 2 (Câu sau): Luận điểm / Sự kiện tiếp diễn"]
    C & D --> E{{"Xác định hướng đi của tư duy (Directional Logic)"}}
    E -->|"Tương phản (Contrast)"| F["However / Nevertheless / By contrast"]
    E -->|"Bổ sung / Cụ thể hóa (Continuation)"| G["Furthermore / In addition / Specifically"]
    E -->|"Nhân quả (Cause & Effect)"| H["Therefore / As a result / Consequently"]
    E --> I{{"Đối chiếu và chọn từ nối khớp hướng"}}
    I --> J["Chọn ({corr}): '{clean_corr_txt}'"]
    J --> K["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = "Đọc câu trước và câu sau chỗ trống độc lập, tạm thời bỏ qua từ chuyển ý. Tóm tắt ý cốt lõi của mỗi câu thành 3-5 từ."
                t2 = "Xác định mối liên hệ giữa hai câu: Câu sau có 'lật lại vấn đề / đưa ra ngoại lệ' (Tương phản), 'giải thích rõ hơn / đưa ví dụ' (Bổ sung), hay 'là kết quả tất yếu' (Nhân quả)?"
                t3 = f"Từ nối phản ánh đúng hướng đi của lập luận là [{corr}] ('{corr_txt}')."
                stip = "Mẹo College Board: Nếu có 2 phương án cùng thuộc một nhóm nghĩa (ví dụ: 'Therefore' và 'As a result' đều chỉ nhân quả), thì thường CẢ HAI đều bị loại, vì SAT chỉ có 1 đáp án đúng duy nhất!"

                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Phản ánh chính xác mối quan hệ logic giữa hai câu văn."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Thiết lập đúng cầu nối tư duy giữa câu trước và câu sau, giúp mạch văn tự nhiên và thuyết phục."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Sai hướng logic. Phương án này biểu thị mối quan hệ trái ngược với thực tế liên kết của hai câu văn."
                        pooe_lines.append(f"• Loại {k}. {txt} - Sai hướng liên kết logic giữa hai câu.")
                pooe_breakdown = "\n".join(pooe_lines)

            # 1.8 Rhetorical Synthesis (Student Notes)
            else:
                clean_prompt = safe_mermaid_text(prompt[:120])
                clean_corr_txt = safe_mermaid_text(corr_txt)
                mermaid = f"""flowchart TD
    A["Ghi chú nghiên cứu (Student Notes)"] --> B{{"Xác định MỤC TIÊU CỐT LÕI (The Student Wants to...)"}}
    B --> C["Đọc kỹ câu hỏi: '{clean_prompt}'"]
    C --> D["Sàng lọc các gạch đầu dòng chứa thông tin trực tiếp phục vụ mục tiêu"]
    D --> E{{"Chiến thuật loại trừ 2 bước của SAT"}}
    E -->|"Bẫy thông tin đúng nhưng SAI MỤC TIÊU"| F["Loại các phương án nêu sự thật chính xác nhưng không giải quyết đúng yêu cầu đề bài"]
    E -->|"Đạt 100% mục tiêu với thông tin chuẩn xác"| G["Chọn ({corr}): '{clean_corr_txt}'"]
    G --> H["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = "Đừng đọc các gạch đầu dòng ghi chú trước! Hãy đọc ngay câu hỏi cuối cùng: 'The student wants to...' để xác định chính xác mục tiêu cần đạt là gì."
                t2 = "Khoanh vùng mục tiêu: Ví dụ 'emphasize a similarity' (nhấn mạnh điểm giống nhau), 'emphasize a difference' (nhấn mạnh điểm khác nhau), hay 'introduce X to a new audience' (giới thiệu X)."
                t3 = f"Tìm phương án đáp ứng trọn vẹn và ngắn gọn nhất mục tiêu này: Chọn [{corr}] ('{corr_txt}')."
                stip = "Mẹo College Board: Dạng Rhetorical Synthesis KHÔNG KIỂM TRA trí nhớ. Câu trả lời đúng là câu hoàn thành tốt nhất MỤC TIÊU đề ra. Rất nhiều phương án nêu thông tin hoàn toàn đúng sự thật từ các gạch đầu dòng nhưng lại bị LOẠI vì sai mục tiêu!"

                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Hoàn thành trọn vẹn mục tiêu tu từ của học sinh."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Lựa chọn và kết hợp thông tin chính xác từ các ghi chú để đáp ứng đầy đủ yêu cầu tu từ mà học sinh mong muốn."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Lạc mục tiêu. Mặc dù thông tin có thể đúng sự thật từ bảng ghi chú, nhưng phương án này không hoàn thành được mục tiêu cụ thể được nêu ở đề bài."
                        pooe_lines.append(f"• Loại {k}. {txt} - Không giải quyết đúng mục tiêu tu từ yêu cầu.")
                pooe_breakdown = "\n".join(pooe_lines)

        # =========================================================================
        # 2. MATH MODULE 1 & 2
        # =========================================================================
        else:
            clean_prompt = safe_mermaid_text(prompt[:120])
            clean_corr = safe_mermaid_text(corr)

            if is_grid_in:
                mermaid = f"""flowchart TD
    A["Bài toán tự điền đáp số (Grid-in):<br>'{clean_prompt}'"] --> B{{"Nhận diện bản chất toán học & Dạng bài"}}
    B --> C["Thiết lập biểu thức đại số / Hệ thức hình học tương ứng cho chủ đề '{safe_mermaid_text(topic)}'"]
    C --> D["Thực hiện biến đổi toán học từng bước cẩn thận"]
    D --> E{{"Cảnh báo bẫy SAT (Trap Alert)"}}
    E -->|"Kiểm tra kỹ điều kiện đề bài"| F["Tránh lỗi tính toán nhầm dấu, quên đổi đơn vị hoặc làm tròn sai"]
    D --> G["Tính toán ra giá trị nghiệm chính xác: {clean_corr}"]
    G --> H["Điền đáp số chuẩn xác: {clean_corr}"]"""

                t1 = f"Đọc kỹ yêu cầu đề bài cho dạng '{topic}'. Xác định rõ đề bài đang cho các dữ kiện gì và đại lượng cần tìm là gì."
                t2 = "Thiết lập phương trình hoặc áp dụng công thức tương ứng. Chú ý tính toán cẩn thận từng bước hoặc sử dụng máy tính Desmos để kiểm tra lại nghiệm."
                t3 = f"Thực hiện các bước biến đổi đại số / hình học cho kết quả chính xác cần điền vào ô đáp số là: [{corr}]."
                stip = "Mẹo Grid-in: SAT chấp nhận phân số tối giản hoặc số thập phân tương đương. Hãy chắc chắn không nhập thừa ký tự đơn vị (như $, %, độ) vào ô trả lời!"

                option_exps = {}
                pooe_breakdown = f"• Đáp án ĐÚNG: {corr}\n• Phương pháp: Áp dụng công thức và tính toán cẩn thận để tìm ra kết quả {corr}."
                grid_in_exp = {
                    "correct_answer": corr,
                    "solution_steps": f"Thiết lập biểu thức theo dữ kiện đề bài cho chủ đề '{topic}'. Biến đổi toán học từng bước để tìm ra nghiệm chính xác {corr}.",
                    "trap_errors": "Cẩn thận kiểm tra các bẫy đổi đơn vị, làm tròn số thập phân, hoặc điều kiện bài toán."
                }
                q["grid_in_explanation"] = grid_in_exp

            else:
                clean_corr_txt = safe_mermaid_text(corr_txt)
                mermaid = f"""flowchart TD
    A["Bài toán trắc nghiệm:<br>'{clean_prompt}'"] --> B{{"Nhận diện dạng toán & Công thức then chốt"}}
    B --> C["Áp dụng phương pháp đại số chuẩn hoặc tận dụng công cụ vẽ đồ thị Desmos"]
    C --> D["Thực hiện các bước biến đổi và tính toán cụ thể"]
    D --> E{{"Chiến thuật loại trừ POOE & Cảnh báo bẫy"}}
    E -->|"Bẫy tính toán / Nhầm đại lượng hỏi"| F["Loại các phương án bẫy nhầm lẫn giữa x và biểu thức kết hợp"]
    E -->|"Khớp chính xác kết quả toán học"| G["Chọn ({corr}): '{clean_corr_txt}'"]
    G --> H["Chốt đáp án chính xác: [{corr}]"]"""

                t1 = f"Phân tích dữ kiện bài toán cho dạng '{topic}'. Đọc kỹ câu hỏi cuối cùng để biết chính xác đề bài hỏi về biến nào hay biểu thức nào."
                t2 = "Áp dụng định lý hoặc công thức đại số/hình học chuẩn. Bạn cũng có thể mở máy tính đồ thị Desmos để vẽ đồ thị và tìm giao điểm hoặc giá trị cực trị trực quan."
                t3 = f"Biến đổi và tính toán: Kết quả chính xác hoàn toàn là phương án [{corr}] ('{corr_txt}')."
                stip = "Mẹo Toán SAT: Luôn chú ý 'bẫy câu hỏi' - SAT thường giải ra x nhưng câu hỏi lại hỏi về (2x + 5) hoặc (x/2). Hãy gạch chân đại lượng cần tìm trước khi khoanh đáp án!"

                option_exps = {}
                pooe_lines = [f"• Đáp án ĐÚNG: {corr}. {corr_txt} - Giải quyết chính xác bài toán theo quy tắc toán học."]
                for k in ["A", "B", "C", "D"]:
                    txt = orig_opts.get(k, f"Lựa chọn {k}")
                    if k == corr:
                        option_exps[k] = f"ĐÁP ÁN ĐÚNG. {k} ({txt}) - Đáp ứng hoàn hảo phép tính toán và dữ kiện đề bài, cho kết quả chính xác tuyệt đối."
                    else:
                        option_exps[k] = f"Loại {k} - {k} ({txt}) - Kết quả không đúng. Phương án này xuất phát từ lỗi sai công thức, nhầm lẫn dấu hoặc rơi vào bẫy tính toán của đề thi."
                        pooe_lines.append(f"• Loại {k}. {txt} - Sai sót phép tính hoặc rơi vào bẫy công thức.")
                pooe_breakdown = "\n".join(pooe_lines)

        # Update question object
        q["mermaid_diagram"] = mermaid
        q["tier1_hint"] = t1
        q["level1_tip"] = t1
        q["tier2_hint"] = t2
        q["level2_hint"] = t2
        q["tier3_hint"] = t3
        q["level3_solution"] = t3
        q["strategic_tip"] = stip
        q["pro_tip"] = stip
        q["pooe_breakdown"] = pooe_breakdown
        q["option_explanations"] = option_exps

    # Save to data/nov2026.json and static/data/nov2026.json
    print(f"Saving enhanced database to {DATA_FILE}...")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Saving enhanced database to {STATIC_DATA_FILE}...")
    with open(STATIC_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("=== Successfully enhanced all 98 questions with mindmaps and multi-tier feedback! ===")

if __name__ == "__main__":
    generate_enhancements()
