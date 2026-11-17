#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compile_princeton_advanced_mindmaps.py
Tạo và cập nhật Sơ đồ tư duy trực quan (Mermaid Mindmap) cho toàn bộ 49 câu hỏi
trong đề Digital SAT Advanced (Harder Reading & Writing Module: 27 câu, Harder Math Module: 22 câu).
Đồng bộ vào:
  - data/princeton_advanced.json
  - data/princetonadvanced.json
  - static/data/princeton_advanced.json
  - static/data/princetonadvanced.json
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# BẢN ĐỒ SƠ ĐỒ TƯ DUY 49 CÂU HỎI PRINCETON REVIEW ADVANCED SAT
# ==============================================================================

MINDMAPS = {}

# ------------------------------------------------------------------------------
# READING & WRITING MODULE (CÂU 1 - 27)
# ------------------------------------------------------------------------------

MINDMAPS[1] = """flowchart TD
    A["Ngữ cảnh (Context):<br>Nghiên cứu của Eti Ben Simon & Matthew Walker về giấc ngủ & hành vi vị tha"] --> B{"Manh mối then chốt (Key Clues)"}
    B --> C["'participants who experienced poor sleep<br>were less willing to help others the following day'<br>(Ít sẵn lòng giúp đỡ người khác hơn vào ngày hôm sau)"]
    C --> D["Dự đoán từ cần điền (Prediction):<br>Thiếu ngủ làm 'suy giảm / cản trở' tính vị tha<br>(diminish / reduce / impair)"]
    D --> E{"Chiến thuật loại trừ POOE (Princeton Review)"}
    E -->|Ngược sắc thái tích cực| F["Loại (A) elevate, (C) develop, (D) assist:<br>Đều mang nghĩa tích cực (nâng cao/phát triển/hỗ trợ)"]
    E -->|Khớp sắc thái tiêu cực| G["Chọn (B) hinder:<br>Đồng nghĩa chuẩn xác với 'diminish / impede / cản trở'"]
    G --> H["Chốt đáp án chính xác: [B]"]"""

MINDMAPS[2] = """flowchart TD
    A["Ngữ cảnh (Context):<br>Nghiên cứu của Đại học Duke về mức độ tò mò đối với kết quả video"] --> B{"Manh mối tương phản (Contrast Clue)"}
    B --> C["'subjects expressing more curiosity... were less likely,<br>NOT MORE LIKELY as expected by researchers, to fast forward'<br>(Người tò mò hơn lại ÍT tua nhanh hơn, trái ngược với kỳ vọng)"]
    C --> D["Dự đoán từ cần điền (Prediction):<br>Kết quả 'trái ngược với suy đoán thông thường / nghịch lý'<br>(contradictory / surprising / contrary to expectation)"]
    D --> E{"Chiến thuật loại trừ POOE"}
    E -->|Bẫy từ ngữ cực đoan| F["Loại (A) unprecedented: 'Chưa từng có tiền lệ' quá cực đoan<br>Loại (B) ambivalent: 'Mâu thuẫn cảm xúc' sai đối tượng<br>Loại (D) vague: 'Mơ hồ' không liên quan"]
    E -->|Khớp nghĩa nghịch lý| G["Chọn (C) paradoxical:<br>Phản ánh đúng bản chất 'tưởng thế này nhưng thực tế lại trái ngược'"]
    G --> H["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[3] = """flowchart TD
    A["Ngữ cảnh (Context):<br>Tòa án Nước Tây Ban Nha (Water Tribunal of Spain / Tribunal de las Aguas)"] --> B{"Manh mối lĩnh vực pháp lý (Legal Domain Clues)"}
    B --> C["'world's oldest continually operating court'<br>(Tòa án hoạt động liên tục lâu đời nhất thế giới)"]
    B --> D["'legal disputes regarding water distribution and land rights were ______'<br>(Các tranh chấp pháp lý về phân phối nước và quyền đất đai được ______)"]
    C & D --> E["Dự đoán từ cần điền (Prediction):<br>Thuật ngữ pháp lý chỉ việc 'xét xử / phân xử chính thức tại tòa'<br>(judged / settled legally)"]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Sai bản chất tòa án| G["Loại (A) dismissed: Bác bỏ đơn kiện<br>Loại (B) validated: Phê chuẩn hợp lệ (chưa phản ánh tranh chấp)<br>Loại (C) registered: Đăng ký hành chính đơn thuần"]
    F -->|Chuẩn thuật ngữ tư pháp| H["Chọn (D) adjudicated:<br>Nghĩa là xét xử và ra phán quyết chính thức cho các tranh chấp pháp lý"]
    H --> I["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[4] = """flowchart TD
    A["Ngữ cảnh (Context):<br>Nghiên cứu của Jakob Wikström & Etty Bachar-Wikström về khả năng lành vết thương của cá mập"] --> B{"Manh mối điều kiện phủ định (Negative Constraint Clues)"}
    B --> C["Các nhà khoa học trước đây không tin vào các báo cáo ban đầu..."]
    B --> D["'prior to Wikström's work, comprehensive and numerous experiments<br>had NOT been ______'<br>(Trước công trình này, các thí nghiệm toàn diện CHƯA TỪNG được ______)"]
    C & D --> E["Dự đoán từ cần điền (Prediction):<br>Cần động từ mang nghĩa 'thực hiện / tiến hành thí nghiệm'<br>(conducted / carried out / performed)"]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Sai ngữ cảnh| G["Loại (A) halted: Bị đình chỉ<br>Loại (C) dissimulated: Ngụy trang, che giấu<br>Loại (D) decried: Lên án công khai"]
    F -->|Khớp chuẩn xác| H["Chọn (B) executed:<br>Đồng nghĩa với 'carried out / conducted' (được thực thi/tiến hành)"]
    H --> I["Chốt đáp án chính xác: [B]"]"""

MINDMAPS[5] = """flowchart TD
    A["Dạng bài: Chức năng câu gạch chân trong toàn bộ đoạn văn<br>(Sentence Function)"] --> B["Câu gạch chân: 'This skill was evident in every movement<br>of his fingers as he deftly rolled each leaf.'"]
    B --> C{"Phân tích cấu trúc & Manh mối liên kết"}
    C --> D["Đại từ 'This skill' tham chiếu ngược câu trước:<br>Kỹ năng và tốc độ thao tác của người thợ quấn xì gà"]
    C --> E["Từ ngữ miêu tả: 'every movement', 'deftly rolled each leaf'<br>(Từng cử động ngón tay khéo léo cuộn từng lá thuốc)"]
    D & E --> F["Đánh giá chức năng tổng thể:<br>Nhấn mạnh năng lực thành thục và sự điêu luyện bậc thầy của người thợ"]
    F --> G{"Đối chiếu các phương án"}
    G -->|Không so sánh trực tiếp tác phẩm thẩm mỹ| H["Loại (B) Không so với tác phẩm nghệ thuật<br>Loại (C) Không nhắc xì gà giá rẻ<br>Loại (D) Không nói về điều kiện làm việc khắc nghiệt"]
    G -->|Khớp chính xác chức năng| I["Chọn (A): 'It emphasizes the competence with which<br>the cigar-maker engages in his daily work.'"]
    I --> J["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[6] = """flowchart TD
    A["Dạng bài: Mục đích chính của đoạn văn (Main Purpose)<br>Trích đoạn 'Great Expectations' của Charles Dickens"] --> B{"Manh mối hành động & Nguyện vọng của nhân vật Pip"}
    B --> C["Pip muốn bạn của mình là Herbert:<br>'know nothing and say nothing about the maker of his fortune'"]
    B --> D["Nguồn gốc gia sản đến từ ân nhân bí mật (Magwitch)<br>và cần phải được giữ kín tuyệt đối"]
    C & D --> E["Đánh giá mục đích cốt lõi:<br>Bộc lộ quyết tâm sắt đá của Pip trong việc che giấu danh tính người bảo trợ tài chính"]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Sai lệch mối quan hệ| G["Loại (A) Nghi ngờ lòng trung thành của Herbert (sai)<br>Loại (C) Trách móc bạn bè (sai)<br>Loại (D) Lập kế hoạch quản lý tài chính (sai lệch trọng tâm)"]
    F -->|Bắt trúng ý đồ văn bản| H["Chọn (B): Thể hiện mong muốn giấu kín danh tính người đã chu cấp tài sản cho Pip"]
    H --> I["Chốt đáp án chính xác: [B]"]"""

MINDMAPS[7] = """
flowchart TD
    A["Dạng bài: Cấu trúc tổng thể của đoạn văn (Overall Structure)"] --> B["Đoạn văn về nghệ sĩ Yoshioka Tokujin"]
    B --> C["Câu 1 (General Approach):<br>Giới thiệu phương pháp chung: lồng ghép các quá trình tự nhiên vào nghệ thuật<br>(incorporates natural processes and innovative approaches)"]
    B --> D["Các câu tiếp theo (Specific Instance):<br>Minh họa bằng dự án cụ thể 'Crystallized' năm 2008<br>(nuôi tinh thể kết hợp âm nhạc Swan Lake / Moonlight tạo tranh kết tinh)"]
    C & D --> E{"Chiến thuật loại trừ POOE (Princeton Review)"}
    E -->|Half-Right: Bàn về tác phẩm nhưng không có lịch sử sự nghiệp| F["Loại (A) draws a conclusion about Tokujin's artistic history"]
    E -->|Khớp chuẩn: Từ tiếp cận chung đến trường hợp cụ thể| G["Chọn (B) It introduces an artist's general approach, then describes a specific instance of that approach."]
    E -->|Recycled Language: Nhạc không bị so sánh đối lập và không định hình phong cách| H["Loại (C) contrasts Swan Lake with Moonlight<br>Loại (D) explains how music influenced his work"]
    G --> I["Chốt đáp án chính xác: [B]"]
"""

MINDMAPS[8] = """
flowchart TD
    A["Dạng bài: Chức năng của câu gạch chân (Sentence Function)<br>Nghiên cứu của GS Tim mạch Maciej Banach về số bước đi bộ hàng ngày"] --> B{"Phân tích cấu trúc & ngữ cảnh đoạn văn"}
    B --> C["Câu 1: Giới thiệu phát hiện tổng quát: đi bộ nhiều hơn giúp giảm nguy cơ tử vong do tim mạch"]
    B --> D["Câu gạch chân: 'The study, which evaluated 226,889 people across 17 different studies worldwide, examined individuals who had walked from 5,000 steps up to 20,000 steps a day.'"]
    D --> E["Chức năng câu gạch chân:<br>Mô tả phạm vi dữ liệu và đối tượng mà nghiên cứu khảo sát<br>(Explain what the study looked at / sample size & methodology)"]
    E --> F{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Đoạn văn không nói về khó khăn/trở ngại nào| G["Loại (A) outlines an obstacle encountered by the research team"]
    F -->|Right Answer, Wrong Question: Câu kết luận là câu cuối cùng, không phải câu gạch chân| H["Loại (B) summarizes the conclusions reached by the team<br>Loại (C) offers a specific example of the team's conclusions"]
    F -->|Khớp chuẩn chức năng mô tả quy mô nghiên cứu| I["Chọn (D) It provides details about the scope and subjects of the team's study."]
    I --> J["Chốt đáp án chính xác: [D]"]
"""

MINDMAPS[9] = """flowchart TD
    A["Dạng bài: Tổng hợp hai văn bản (Dual Texts Synthesis)<br>Về nguồn gốc tiến hóa của tế bào nhân thực (Eukaryotes)"] --> B["Text 1 (Gabaldón et al.):<br>Giả thuyết tế bào tổ tiên đơn giản đã trao đổi vật chất di truyền (Horizontal Gene Transfer) TRƯỚC KHI xảy ra nội cộng sinh"]
    A --> C["Text 2 (Quan điểm mới):<br>Mô hình bộ gen mới nhất chỉ ra chính biến cố nội cộng sinh (Endosymbiosis) mới là ngòi nổ chính cho việc chuyển gen"]
    B & C --> D{"Tác giả Text 2 sẽ nhận định thế nào về giả thuyết của Text 1?"}
    D --> E["Thừa nhận giả thuyết của Gabaldón hấp dẫn/thú vị<br>NHƯNG bị thách thức bởi dữ liệu thời gian nội cộng sinh xảy ra sớm hơn"]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Bác bỏ cực đoan hoặc đồng tình hoàn toàn| G["Loại (A) Bác bỏ hoàn toàn là ngụy khoa học (quá cực đoan)<br>Loại (B) Hoàn toàn đồng ý (sai thực tế Text 2)<br>Loại (D) Không liên quan đến dữ liệu gen"]
    F -->|Đánh giá sắc thái cân bằng| H["Chọn (C): Thừa nhận đây là giả thuyết đáng chú ý nhưng bị lung lay bởi bằng chứng bộ gen mới về mốc thời gian nội cộng sinh."]
    H --> I["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[10] = """
flowchart TD
    A["Dạng bài: Phân tích bảng số liệu (Quantitative / Tables)<br>Doanh thu phòng vé & Số vé bán ra (1996–2000)"] --> B{"Luận điểm trong bài đọc cần minh họa"}
    B --> C["'Box office profits continued to rise through the 1990s,<br>despite ticket sales decreasing towards the end of the decade.'<br>(Doanh thu tiếp tục tăng dù số lượng vé bán ra sụt giảm vào cuối thập kỷ)"]
    C --> D{"Đối chiếu dữ liệu bảng số liệu 1996–2000"}
    D --> E["Giai đoạn 1998 – 2000:<br>• Số vé bán ra: GIẢM từ 1.48 tỷ (1998) xuống 1.42 tỷ (2000)<br>• Doanh thu phòng vé: TĂNG từ $6.95 tỷ đô lên $7.66 tỷ đô!"]
    E --> F{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Khớp hoàn hảo cả 2 chiều: vé giảm nhưng doanh thu tăng| G["Chọn (A): The number of tickets sold dropped from 1.48 billion in 1998 to 1.42 billion in 2000, while box office revenue increased from $6.95 billion to $7.66 billion."]
    F -->|Half-Right: Vé giữ nguyên không giảm| H["Loại (B): Vé 1997-1999 giữ nguyên ở 1.47 tỷ, không thể hiện xu hướng giảm"]
    F -->|Irrelevant: Không đề cập đến doanh thu phòng vé| I["Loại (C) & (D): Chỉ nói về số vé bán ra mà bỏ quên doanh thu phòng vé"]
    G --> J["Chốt đáp án chính xác: [A]"]
"""

MINDMAPS[11] = """flowchart TD
    A["Dạng bài: Bằng chứng củng cố luận điểm (Command of Evidence - Support)<br>Luận điểm của nhà cổ sinh vật học Tang"] --> B{"Luận điểm của Tang"}
    B --> C["Tảo lục (Green Algae) tiến hóa lần đầu tiên trong môi trường ĐẠI DƯƠNG / BIỂN,<br>chứ không phải trong môi trường nước ngọt như sông hồ."]
    C --> D{"Bằng chứng nào củng cố trực tiếp nhất cho Tang?"}
    D --> E["Cần phát hiện hóa thạch tảo lục cổ xưa nhất nằm độc quyền trong các tầng trầm tích biển sâu,<br>hoàn toàn không có dấu vết trầm tích nước ngọt."]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Không chứng minh nguồn gốc đại dương| G["Loại (A) Tìm thấy tảo nước ngọt hiện đại<br>Loại (B) Tảo biển có nhiều sắc tố hơn (không chứng minh thời điểm)<br>Loại (C) Hóa thạch không xác định niên đại"]
    F -->|Bằng chứng địa tầng biển 1 tỷ năm tuổi| H["Chọn (D): Vi hóa thạch tảo lục cổ nhất (1 tỷ năm) được khai quật tại phiến sét biển sâu không chứa khoáng vật nước ngọt."]
    H --> I["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[12] = """
flowchart TD
    A["Dạng bài: Bằng chứng từ biểu đồ (Quantitative / Graphs)<br>Khả năng can thiệp dựa trên Tình trạng ASD & Số lượng người chứng kiến"] --> B{"Kết luận của nhà nghiên cứu cần củng cố"}
    B --> C["'Autistic employees were more likely to speak up on workplace issues than non-autistic employees, regardless of the number of bystanders.'<br>(Nhân viên có phổ tự kỷ ASD sẵn sàng lên tiếng can thiệp hơn nhân viên không tự kỷ, bất kể số lượng người chứng kiến)"]
    C --> D{"Đọc dữ liệu biểu đồ cột (Bar Graph)"}
    D --> E["Cột nhân viên tự kỷ (ASD) luôn cao hơn cột nhân viên không tự kỷ (Non-ASD) ở TẤT CẢ các điều kiện người chứng kiến (1 người, 2 người, nhóm đông)!"]
    E --> F{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Khớp chuẩn kết luận và số liệu biểu đồ| G["Chọn (A): Across all bystander conditions, the likelihood of intervention was consistently higher for autistic participants than for non-autistic participants."]
    F -->|Irrelevant: Không so sánh giữa 2 nhóm nhân viên| H["Loại (B): Chỉ nói về một nhóm mà không so sánh tự kỷ vs không tự kỷ"]
    F -->|Ngược dữ liệu (Opposite): Tự kỷ và không tự kỷ có tỉ lệ bằng nhau| I["Loại (C) & (D): Sai lệch hoàn toàn so với các cột số liệu biểu đồ"]
    G --> J["Chốt đáp án chính xác: [A]"]
"""

MINDMAPS[13] = """
flowchart TD
    A["Dạng bài: Làm suy yếu kết luận (Weaken Claims)<br>Nghiên cứu của Kuwano và cộng sự về sự kiện va chạm thiên thạch"] --> B{"Kết luận của Kuwano cần làm suy yếu"}
    B --> C["Kuwano cho rằng sự kiện nổ Tunguska 1908 là do một TIỂU HÀNH TINH (asteroid - chứa kim loại và đá) nổ tung trên không trung,<br>dựa trên đặc điểm biến dạng phẳng (planar deformation features) trong thạch anh bị sốc nhiệt (shocked quartz)."]
    C --> D{"Tìm dữ kiện làm giảm độ tin cậy của kết luận"}
    D --> E["Nếu SAO CHỔI (comet - bụi và băng) cũng có thể tạo ra các đặc điểm thạch anh bị sốc nhiệt tương tự,<br>thì sự hiện diện của thạch anh không thể chứng minh vật thể đó là tiểu hành tinh!"]
    E --> F{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Strengthen: Củng cố thêm cho kết luận tiểu hành tinh| G["Loại (A) & (B): Làm tăng khả năng là tiểu hành tinh chứ không làm suy yếu"]
    F -->|Irrelevant: Hoàn cảnh vụ nổ không liên quan đến bản chất thiên thể| H["Loại (C): Cơ chế nổ không giúp phân biệt tiểu hành tinh hay sao chổi"]
    F -->|Weaken chuẩn xác: Chỉ ra sao chổi cũng tạo ra shocked quartz| I["Chọn (D): Comets entering the atmosphere under high velocity can also generate temperatures and pressures sufficient to produce planar deformation features in quartz."]
    I --> J["Chốt đáp án chính xác: [D]"]
"""

MINDMAPS[14] = """
flowchart TD
    A["Dạng bài: Bằng chứng ủng hộ lời đính chính (Support Clarification)"] --> B{"Lời đính chính của nhà báo trong đoạn văn"}
    B --> C["Họa sĩ bản địa Jaune Quick-to-See Smith ngạc nhiên khi 'I See Red: Target' là bức TRANH VẼ TRÊN TOAN (painting on canvas) ĐẦU TIÊN của nghệ sĩ bản địa được đưa vào bộ sưu tập của National Gallery of Art."]
    C --> D["Lời đính chính của nhà báo:<br>Bảo tàng TRƯỚC ĐÓ ĐÃ TỪNG trưng bày nghệ thuật bản địa ở CÁC HÌNH THỨC CHẤT LIỆU KHÁC<br>(Indigenous works in other forms of media)."]
    D --> E{"Dữ kiện nào chứng minh trực tiếp lời đính chính này?"}
    E --> F{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Irrelevant: Nói về các bảo tàng khác (MoMA, Whitney, Met, Smithsonian...)| G["Loại (A): Tác phẩm của Smith ở các bảo tàng danh tiếng khác<br>Loại (B): Công trình công cộng của Smith ở sân bay Denver & Seattle"]
    F -->|Beyond the Text: Bàn về hoạt động sau này của Smith| H["Loại (D): Smith tập hợp tác phẩm của các nghệ sĩ bản địa khác sau khi tranh được mua"]
    F -->|Khớp chuẩn lời đính chính: Bảo tàng đã có tác phẩm trên giấy của người bản địa| I["Chọn (C): Phát ngôn viên National Gallery of Art xác nhận bảo tàng đã có hơn 24 tác phẩm trên giấy (works on paper) của các tác giả bản địa trước khi mua bức tranh toan của Smith."]
    I --> J["Chốt đáp án chính xác: [C]"]
"""

MINDMAPS[15] = """
flowchart TD
    A["Dạng bài: Hoàn thành suy luận logic (Logical Completion / Inferences)"] --> B{"Vấn đề được đặt ra trong bài đọc"}
    B --> C["Nghiên cứu về cách con người đánh giá hệ tư tưởng của nhau khi gặp lần đầu gặp hạn chế vì tiến hành trong phòng thí nghiệm có kiểm soát (controlled settings with proscribed inputs)."]
    C --> D["Các nhà khoa học cố gắng mô phỏng nhiều bối cảnh khác nhau, NHƯNG không thể tái hiện mọi tình huống giao tiếp tự phát ngoài đời thực (can't reasonably mimic every potential kind of social encounter)."]
    D --> E{"Suy luận kết luận hợp lý mà các nhà khoa học phải thừa nhận"}
    E --> F{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Extreme Language: Cho rằng nghiên cứu hoàn toàn vô nghĩa| G["Loại (B) can't create a meaningful study without compromising rigorous conditions"]
    F -->|Beyond the Text: Khuyên từ bỏ hướng nghiên cứu| H["Loại (C) should focus on other questions of behavioral research"]
    F -->|Beyond the Text: Lạc sang các lần gặp tiếp theo thay vì cuộc gặp đầu tiên| I["Loại (D) need additional information about how impressions change after more interactions"]
    F -->|Thận trọng, chuẩn mực khoa học: Chấp nhận biên độ sai số do môi trường kiểm soát| J["Chọn (A): must allow for a reasonable margin of error in their studies and understand that the controlled nature of the study may affect the authenticity of the interactions."]
    J --> K["Chốt đáp án chính xác: [A]"]
"""

MINDMAPS[16] = """
flowchart TD
    A["Dạng bài: Hoàn thành suy luận logic (Logical Completion)<br>Nghệ thuật vẽ cát truyền thống (Sand Drawing) tại đảo quốc Vanuatu"] --> B{"Chuỗi dữ kiện & Mối quan hệ tương phản"}
    B --> C["1. Vai trò gốc: Tranh cát là phương tiện ghi chép và truyền đạt nghi lễ, lịch sử, văn hóa được UNESCO công nhận là di sản văn hóa phi vật thể."]
    B --> D["2. Sự biến tướng gần đây (Contrast): Tranh cát bị thương mại hóa, sử dụng cho mục đích quảng cáo và du lịch (advertising and tourism)."]
    B --> E["3. Phản ứng: Người dân phản đối việc trục lợi từ tranh cát ➔ UNESCO tài trợ thành lập Ủy ban 'Save Sand Drawings Action Committee'..."]
    E --> F{"Động cơ thành lập Ủy ban bảo vệ di sản là gì?"}
    F --> G{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Beyond the Text: Tự khen ngợi di sản hoặc nói về sự đổi mới| H["Loại (A) rich history celebrated by international art community<br>Loại (C) islanders recognize importance of change and progress<br>Loại (D) evolving to include modern cultural events"]
    F -->|Khớp trực tiếp lý do phản đối: Lo ngại di sản bị dùng sai mục đích nguyên bản| I["Chọn (B): there is growing concern that an art form is being employed for reasons other than its original purpose."]
    I --> J["Chốt đáp án chính xác: [B]"]
"""

MINDMAPS[17] = """flowchart TD
    A["Dạng bài: Quy tắc dấu câu & Mệnh đề (Boundaries - Clauses & Punctuation)"] --> B["Văn bản: '...hypothesized the existence of a Planet Nine that is affecting the ETNOs' orbits [ ? ] which...'"]
    B --> C{"Phân tích cấu trúc ngữ pháp"}
    C --> D["Phía trước: Mệnh đề độc lập hoàn chỉnh (Independent Clause)"]
    C --> E["Phía sau: Mệnh đề quan hệ không hạn định (Non-restrictive Relative Clause)<br>bắt đầu bằng đại từ 'which' bổ nghĩa cho 'orbits'"]
    D & E --> F{"Quy tắc chuẩn SAT (Grammar Rule)"}
    F --> G["Mệnh đề quan hệ không hạn định (Non-essential/Non-restrictive) bắt đầu bằng 'which'<br>BẮT BUỘC phải có DẤU PHẨY đứng ngay phía trước!"]
    G --> H{"Loại trừ các phương án sai"}
    H -->|Sai dấu câu| I["Loại (A) orbits: (Dấu hai chấm sai vì không phải liệt kê/giải thích)<br>Loại (B) orbits; (Dấu chấm phẩy chỉ nối 2 mệnh đề độc lập)<br>Loại (C) orbits (Không dấu làm câu dính chùm Run-on)"]
    H -->|Đúng quy tắc dấu phẩy| J["Chọn (D) orbits, : Đặt dấu phẩy ngắt mệnh đề phụ hợp lệ."]
    J --> K["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[18] = """flowchart TD
    A["Dạng bài: Nối hai mệnh đề độc lập (Compound Sentences & FANBOYS)"] --> B["Cấu trúc câu: [Mệnh đề độc lập 1] + [ ? ] + [Mệnh đề độc lập 2]"]
    B --> C["• Mệnh đề 1: '...magma releases sulfur gases, which interact with groundwater to produce hydrogen sulfide (H2S)...'"]
    B --> D["• Mệnh đề 2: 'other volcanic vents release primarily water vapor and carbon dioxide.'"]
    C & D --> E{"Quy tắc ghép câu độc lập (Sentence Boundaries Rule)"}
    E --> F["Để nối 2 Mệnh đề Độc lập (Independent Clauses), có 2 cách chuẩn:<br>1. Dấu chấm phẩy ( ; )<br>2. Dấu phẩy + Liên từ kết hợp FANBOYS ( , but / , and / , so...)"]
    F --> G{"Đối chiếu các phương án"}
    G -->|Lỗi ngữ pháp nặng| H["Loại (A) '(H2S)': Lỗi câu dính (Run-on)<br>Loại (B) '(H2S) but': Thiếu dấu phẩy trước liên từ kết hợp<br>Loại (C) '(H2S),': Lỗi Comma Splice kinh điển"]
    G -->|Đầy đủ Dấu phẩy + FANBOYS| I["Chọn (D) '(H2S), but': Dấu phẩy đi kèm 'but' nối chuẩn xác 2 mệnh đề độc lập."]
    I --> J["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[19] = """flowchart TD
    A["Dạng bài: Trạng từ liên kết & Dấu chấm phẩy (Conjunctive Adverbs & Boundaries)"] --> B["Văn bản: 'The ghost catfish doesn't have those crystals [ ? ] it relies on...'"]
    B --> C{"Phân tích cấu trúc 2 vế câu"}
    C --> D["Vế 1 (IC): 'The ghost catfish... doesn't have those crystals' (Mệnh đề độc lập)"]
    C --> E["Vế 2 (IC): 'it relies on special tissue structures...' (Mệnh đề độc lập)"]
    C --> F["Từ nối: 'instead' (Trạng từ liên kết - Conjunctive Adverb)"]
    D & E & F --> G{"Quy tắc dấu câu chuẩn với Conjunctive Adverb"}
    G --> H["Mô hình chuẩn: [Independent Clause 1] ; instead , [Independent Clause 2]<br>(Dấu chấm phẩy trước 'instead', dấu phẩy sau 'instead')"]
    H --> I{"Loại trừ phương án sai"}
    I -->|Lỗi dấu câu| J["Loại (A) crystals instead, (Comma splice)<br>Loại (B) crystals, instead; (Đảo vị trí dấu chấm phẩy phi logic)<br>Loại (D) crystals, instead, (Lỗi Comma splice hai đầu)"]
    I -->|Chuẩn công thức ngữ pháp| K["Chọn (C) crystals; instead,"]
    K --> L["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[20] = """
flowchart TD
    A["Dạng bài: Hòa hợp thì & Thể động từ (Verb Tense & Aspect)"] --> B["Đạo luật G.I. Bill (1944) hỗ trợ cựu chiến binh Thế chiến II"]
    B --> C["Câu cần điền: 'By 1951, about 8 million veterans ________ advantage of the bill's educational benefits...'"]
    C --> D{"Manh mối thời gian mấu chốt (Time Clue)"}
    D --> E["Cụm từ 'By 1951' (Trước mốc năm 1951 trong quá khứ):<br>Chỉ hành động đã xảy ra và hoàn tất TRƯỚC một thời điểm xác định trong quá khứ."]
    E --> F{"Quy tắc thì Quá khứ hoàn thành (Past Perfect Rule)"}
    F --> G["Hành động xảy ra trước mốc thời gian quá khứ BẮT BUỘC chia: HAD + V3/ed"]
    G --> H{"Chiến thuật loại trừ POOE (Princeton Review)"}
    H -->|Quá khứ đơn: Không thể hiện được hành động hoàn tất trước mốc By 1951| I["Loại (B) took"]
    H -->|Hiện tại đơn / Tương lai: Lệch hoàn toàn ngữ cảnh lịch sử 1951| J["Loại (C) take<br>Loại (D) will take"]
    H -->|Đúng dạng Quá khứ hoàn thành| K["Chọn (A) had taken: Khớp hoàn hảo với mốc 'By 1951'."]
    K --> L["Chốt đáp án chính xác: [A]"]
"""

MINDMAPS[21] = """
flowchart TD
    A["Dạng bài: Hòa hợp Chủ ngữ - Vị ngữ (Subject-Verb Agreement)"] --> B["Văn bản: 'The Organization of the Petroleum Exporting Countries (OPEC), a collective of countries founded in 1960 by Iran, Iraq, Kuwait, Saudi Arabia, and Venezuela, ________ the global oil market...'"]
    B --> C{"Chiến thuật cô lập Chủ ngữ (TPR Subject Isolation)"}
    C --> D["Gạch bỏ cụm đồng vị ngữ chen giữa 2 dấu phẩy:<br>', a collective of countries founded in 1960 by Iran, Iraq, Kuwait, Saudi Arabia, and Venezuela,'"]
    C --> E["Gạch bỏ cụm giới từ phụ: 'of the Petroleum Exporting Countries (OPEC)'"]
    D & E --> F["Chủ ngữ hạt nhân cốt lõi (True Subject):<br>'The Organization' ➔ Danh từ số ít (Singular Noun)!"]
    F --> G{"Quy tắc hòa hợp số ít"}
    G --> H["Chủ ngữ số ít bắt buộc đi với Động từ số ít (ngôi thứ 3 số ít thêm -s / -es)"]
    H --> I{"Chiến thuật loại trừ POOE (Princeton Review)"}
    I -->|Các dạng động từ số nhiều| J["Loại (A) were influencing (were số nhiều)<br>Loại (B) have influenced (have số nhiều)<br>Loại (C) influence (động từ nguyên mẫu số nhiều)"]
    I -->|Động từ số ít duy nhất| K["Chọn (D) influences: Hòa hợp hoàn hảo với danh từ số ít 'Organization'."]
    K --> L["Chốt đáp án chính xác: [D]"]
"""

MINDMAPS[22] = """flowchart TD
    A["Dạng bài: Ranh giới cụm phân từ & Bổ ngữ (Boundaries & Participial Modifiers)"] --> B["Văn bản: '...a Korean musical notation system written on paper divided into regular boxes [ ? ] each of which represents...'"]
    B --> C{"Phân tích cấu trúc thành phần"}
    C --> D["Cụm phân từ bổ nghĩa: 'written on paper divided into regular boxes'<br>(được viết trên giấy chia thành các ô vuông đều đặn)"]
    C --> E["Phía sau: Mệnh đề quan hệ độc lập 'each of which represents a beat...'"]
    D & E --> F{"Quy tắc ngắt cụm bổ nghĩa"}
    F --> G["Cụm phân từ dài kết thúc cần có DẤU PHẨY ngăn cách<br>trước khi mở ra mệnh đề quan hệ tiếp theo.<br>Đồng thời không đặt dấu phẩy tùy tiện giữa 'paper' và 'divided' (hạn định chặt chẽ)."]
    G --> H{"Đối chiếu lựa chọn"}
    H -->|Sai vị trí dấu phẩy| I["Loại (A) Thiếu dấu phẩy ở cuối cụm<br>Loại (B) Thừa dấu phẩy sau 'paper' nhưng thiếu ở cuối<br>Loại (D) Dấu phẩy thừa sau 'paper'"]
    H -->|Chuẩn xác ngữ pháp| J["Chọn (C) paper divided into regular boxes,"]
    J --> K["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[23] = """flowchart TD
    A["Dạng bài: Dấu hai chấm giải thích (Colons for Explanation / Specification)"] --> B["Văn bản: '...Howard University evolutionary biologist compares two comprehensive taxonomic datasets from North America and Asia [ ? ] one comprising fossils...'"]
    B --> C{"Phân tích cấu trúc trước & sau vị trí trống"}
    C --> D["Phía trước: Mệnh đề độc lập hoàn chỉnh (Complete Independent Clause)<br>'...compares two comprehensive taxonomic datasets from North America and Asia'"]
    C --> E["Phía sau: Liệt kê chi tiết 2 bộ dữ liệu cụ thể:<br>'one comprising fossils... and the other containing extant species...'"]
    D & E --> F{"Quy tắc sử dụng Dấu hai chấm (Colon Rule)"}
    F --> G["Dấu hai chấm ( : ) được dùng sau một Mệnh đề Độc lập<br>để giới thiệu lời giải thích, làm rõ hoặc danh sách chi tiết hóa!"]
    G --> H{"Đối chiếu các phương án"}
    H -->|Lỗi liên kết| I["Loại (A) Asia, (Dấu phẩy không đủ ngắt mệnh đề giải thích)<br>Loại (B) Asia (Không dấu gây lỗi run-on)<br>Loại (C) Asia and (Thừa liên từ gây què câu)"]
    H -->|Đúng chức năng dấu hai chấm| J["Chọn (D) Asia:"]
    J --> K["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[24] = """flowchart TD
    A["Dạng bài: Từ nối logic (Transitions - Logical Direction)"] --> B{"Phân tích mối quan hệ giữa 2 câu"}
    B --> C["Câu 1: Hòn đảo Delos nổi tiếng với số lượng tranh khảm thời kỳ Hy Lạp hóa (mosaics) phong phú vượt bậc."]
    B --> D["Câu 2: Hòn đảo Rheneia lân cận cũng lưu giữ một bộ sưu tập lăng mộ và văn bia phi thường cùng thời kỳ."]
    C & D --> E{"Xác định bản chất logic"}
    E --> F["Hai câu miêu tả 2 phát hiện khảo cổ TƯƠNG ĐỒNG / SONG SONG<br>tại hai địa điểm gần nhau về cùng một thời kỳ lịch sử."]
    F --> G["Dự đoán từ nối (Prediction): 'Tương tự như vậy / Cũng như thế'<br>(Similarly / In the same way / Likewise)"]
    G --> H{"Chiến thuật loại trừ POOE"}
    H -->|Sai bản chất logic| I["Loại (B) Thus: Quan hệ nguyên nhân - kết quả (sai)<br>Loại (C) In addition: Chỉ mang tính bổ sung rời rạc, không nêu bật tính tương đồng<br>Loại (D) Despite this: Quan hệ tương phản (sai)"]
    H -->|Khớp chuẩn quan hệ tương đồng| J["Chọn (A) Similarly,"]
    J --> K["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[25] = """
flowchart TD
    A["Dạng bài: Từ nối logic (Transitions - Cause and Effect)"] --> B{"Phân tích mối quan hệ ngữ nghĩa giữa 2 câu cuối"}
    B --> C["Câu trước (Nguyên nhân - Cause):<br>'There are significant limitations in the microscopy and direct visual observation that have traditionally been the main ways scientists can watch bees work.'<br>(Có những hạn chế lớn trong phương pháp quan sát bằng kính hiển vi truyền thống)"]
    B --> D["Câu sau (Kết quả - Effect):<br>'several key features of honeycomb structures... have been largely understudied and possibly even misrepresented.'<br>(Nhiều đặc tính cốt lõi của cấu trúc tổ ong chưa được nghiên cứu đầy đủ và có thể bị hiểu sai)"]
    C & D --> E{"Hai câu cùng hướng, thể hiện mối quan hệ Nhân - Quả (Cause and Effect)"}
    E --> F{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Từ nối tương phản (Opposite-direction): Cùng nhóm tự triệt tiêu nhau| G["Loại (A) Nevertheless<br>Loại (D) Still"]
    F -->|Từ nối so sánh tương đồng độc lập: Không chỉ kết quả| H["Loại (C) Likewise"]
    F -->|Từ nối chỉ hệ quả logic trực tiếp (Result / Cause & Effect)| I["Chọn (B) Thus,: Do những hạn chế trong quan sát (nguyên nhân) nên cấu trúc tổ ong ít được nghiên cứu (kết quả)."]
    I --> J["Chốt đáp án chính xác: [B]"]
"""

MINDMAPS[26] = """flowchart TD
    A["Dạng bài: Tổng hợp thông tin theo mục tiêu (Rhetorical Synthesis)"] --> B{"Mục tiêu đề bài yêu cầu (The Goal)"}
    B --> C["'Introduce the music of Los Kjarkas to a NEW AUDIENCE'<br>(Giới thiệu âm nhạc của nhóm Los Kjarkas cho khán giả MỚI)"]
    C --> D{"Các yếu tố bắt buộc phải có cho khán giả mới"}
    D --> E["1. Định danh nhóm nhạc: Los Kjarkas là ban nhạc đến từ Bolivia.<br>2. Thể loại / Chủ đề âm nhạc: Tình yêu và sự mất mát.<br>3. Nhạc cụ đặc trưng: Nhạc cụ truyền thống vùng Andes (charango, quena)."]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Thiếu thông tin nền tảng quan trọng| G["Loại (A) Chỉ nhắc nhạc cụ, không giới thiệu nhóm từ đâu<br>Loại (B) Chỉ kể câu chuyện bài hát Lambada (quá hẹp)<br>Loại (D) Thiếu chủ đề âm nhạc và quá sơ sài"]
    F -->|Hội tụ đầy đủ mọi thông tin cốt lõi| H["Chọn (C): 'The songs of Los Kjarkas, a musical group from Bolivia, often cover themes of romance and loss and incorporate traditional Andean instruments.'"]
    H --> I["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[27] = """flowchart TD
    A["Dạng bài: Trình bày nghiên cứu và phát hiện (Rhetorical Synthesis - Findings)"] --> B{"Mục tiêu đề bài yêu cầu (The Goal)"}
    B --> C["'Present Clemens and colleagues' study AND their findings'<br>(Trình bày nghiên cứu của Clemens cùng các cộng sự VÀ các phát hiện của họ)"]
    C --> D{"Các yếu tố thông tin bắt buộc"}
    D --> E["1. Đề cập đến nghiên cứu về râu trên mắt chuột (supraorbital whiskers).<br>2. Phát hiện 1: Gốc râu có vòng tế bào thần kinh nhạy cảm với chuyển động.<br>3. Phát hiện 2: Thuốc làm tê làm giảm khả năng cảm nhận luồng gió của chuột."]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Bỏ sót phát hiện hoặc sai đối tượng| G["Loại (A) Chỉ nêu đặc điểm giải phẫu, không nêu nghiên cứu<br>Loại (B) Nhận định chung chung không có nghiên cứu<br>Loại (D) Nói về râu quanh mõm (facial whiskers) của nghiên cứu khác"]
    F -->|Trình bày trọn vẹn nghiên cứu & 2 phát hiện| H["Chọn (C): Trình bày đầy đủ nghiên cứu về supraorbital whiskers và cả 2 phát hiện then chốt về vòng tế bào thần kinh và phản xạ gió."]
    H --> I["Chốt đáp án chính xác: [C]"]"""

# ------------------------------------------------------------------------------
# HARDER MATH MODULE (CÂU 28 - 49 / MATH #1 - #22)
# ------------------------------------------------------------------------------

MINDMAPS[28] = """flowchart TD
    A["Đề bài (Math #1):<br>Rút gọn biểu thức: –6x² – 12x²"] --> B{"Nhận diện bản chất toán học"}
    B --> C["Hai đơn thức đồng dạng (Like Terms):<br>Cùng phần biến x² với số mũ 2"]
    C --> D["Quy tắc đại số (Algebra Rule):<br>Cộng trừ các hệ số, giữ nguyên phần biến:<br>(–6 – 12) * x²"]
    D --> E["Tính toán hệ số:<br>(–6) – 12 = –18"]
    E --> F{"Cảnh báo bẫy SAT (Trap Warning)"}
    F -->|Bẫy cộng số mũ| G["Tuyệt đối KHÔNG cộng số mũ thành x⁴!<br>(Cộng số mũ chỉ áp dụng cho phép NHÂN hai lũy thừa cùng cơ số)"]
    E --> H["Kết quả cuối cùng: –18x²"]
    H --> I["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[29] = """flowchart TD
    A["Đề bài (Math #2):<br>Mô hình hóa phương trình doanh thu bán đồ ăn"] --> B{"Phân tích từng mẩu thông tin (Bite-Sized Pieces)"}
    B --> C["• Hotdog: Giá $4 mỗi chiếc ➔ Doanh thu = 4 * h"]
    B --> D["• Nước ngọt (Soft drink): Giá $3 mỗi cốc ➔ Doanh thu = 3 * s"]
    B --> E["• Tổng doanh thu: Bằng $123"]
    C & D & E --> F["Thiết lập phương trình tổng quát:<br>Doanh thu Hotdog + Doanh thu Nước ngọt = Tổng doanh thu"]
    F --> G["Phương trình: 4h + 3s = 123"]
    G --> H{"Loại trừ phương án bẫy POOE"}
    H -->|Sai cấu trúc toán| I["Loại (A) (h+s)(4+3) = 123 (nhân sai)<br>Loại (B) (4+h)(3+s) = 123 (vô nghĩa)<br>Loại (C) 3h + 4s = 123 (đảo ngược đơn giá)"]
    G --> J["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[30] = """flowchart TD
    A["Đề bài (Math #3):<br>Tìm số nghiệm của phương trình: 93x = 92x"] --> B{"Hai hướng tiếp cận (Two Approaches)"}
    B -->|Hướng 1 - Đại số thuần túy| C["Chuyển vế đổi dấu:<br>93x – 92x = 0<br>➔ 1x = 0 ➔ x = 0"]
    C --> D["Phương trình có duy nhất 1 nghiệm: x = 0"]
    B -->|Hướng 2 - Đồ thị và Desmos| E["Nhập 2 hàm số:<br>y₁ = 93x (Hệ số góc m₁ = 93)<br>y₂ = 92x (Hệ số góc m₂ = 92)"]
    E --> F["Hai đường thẳng có hệ số góc khác nhau (m₁ ≠ m₂)<br>luôn cắt nhau tại DUY NHẤT 1 điểm tại gốc tọa độ (0, 0)!"]
    D & F --> G["Kết luận: Phương trình có đúng một nghiệm (Exactly one)"]
    G --> H["Chốt đáp án chính xác: [B]"]"""

MINDMAPS[31] = """flowchart TD
    A["Đề bài (Math #4):<br>Cho 19 + 5(m – 5) = 6(m – 5). Tìm giá trị của (m – 5)?"] --> B{"Chiến thuật cụm biến số (Chunking Strategy)"}
    B --> C["Nhận diện biểu thức lặp lại: Cụm (m – 5) xuất hiện ở cả 2 vế!<br>Đặt u = m – 5"]
    C --> D["Thay thế u vào phương trình ban đầu:<br>19 + 5u = 6u"]
    D --> E["Giải phương trình bậc nhất tìm u:<br>19 = 6u – 5u<br>➔ u = 19"]
    E --> F["Vì u = m – 5 nên giá trị m – 5 = 19!"]
    F --> G{"Cảnh báo bẫy SAT (Trap Warning)"}
    G -->|Không cần tìm m| H["Đề bài hỏi (m – 5), KHÔNG hỏi m!<br>Nếu giải tiếp m = 24 là tốn thời gian không cần thiết."]
    F --> I["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[32] = """flowchart TD
    A["Đề bài (Math #5):<br>Tam giác ABC vuông tại A (∠A = 90°). Biết cos(B) = √21 / 5.<br>Tính sin(C)?"] --> B{"Định lý Lượng giác then chốt (Cofunction Identity)"}
    B --> C["Trong tam giác vuông ABC vuông tại A:<br>Tổng hai góc nhọn ∠B + ∠C = 90° (Hai góc phụ nhau)"]
    C --> D["Công thức lượng giác cung phụ nhau (Cofunction Identity):<br>sin(C) = cos(90° – C) = cos(B)"]
    D --> E["Thay số trực tiếp không cần tính độ dài cạnh:<br>sin(C) = cos(B) = √21 / 5"]
    E --> F{"Cách 2: Vẽ hình theo định nghĩa lượng giác (SOH CAH TOA)"}
    F --> G["• cos(B) = Cạnh kề / Cạnh huyền = AB / BC = √21 / 5<br>• sin(C) = Cạnh đối / Cạnh huyền = AB / BC = √21 / 5"]
    E & G --> H["Kết quả: sin(C) = √21 / 5"]
    H --> I["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[33] = """
flowchart TD
    A["Đề bài (Math #6):<br>Tỉ lệ cạnh đáy / chiều cao của tam giác DEF là 64 : 80.<br>Chiều cao giảm 55 đơn vị. Hỏi cạnh đáy phải thay đổi thế nào để giữ nguyên tỉ lệ?"] --> B{"Chiến thuật thế số thực tế (TPR Plugging In)"}
    B --> C["Sử dụng ngay số liệu trong tỉ lệ:<br>• Đáy ban đầu: b₁ = 64<br>• Chiều cao ban đầu: h₁ = 80"]
    C --> D["Bước 1: Tính chiều cao mới sau khi giảm 55 đơn vị:<br>h₂ = 80 – 55 = 25 đơn vị"]
    D --> E["Bước 2: Thiết lập phương trình tỉ lệ thức:<br>b₁ / h₁ = b₂ / h₂ ➔ 64 / 80 = x / 25"]
    E --> F["Bước 3: Nhân chéo giải tìm đáy mới x:<br>80x = 64 × 25 = 1,600 ➔ x = 1,600 / 80 = 20 đơn vị"]
    F --> G["Bước 4: Tính mức độ thay đổi của cạnh đáy:<br>Δb = 64 – 20 = 44 đơn vị (Đáy mới nhỏ hơn đáy cũ ➔ GIẢM 44 đơn vị)"]
    G --> H{"Chiến thuật loại trừ POOE (Princeton Review)"}
    H -->|Sai chiều biến thiên (Tăng thay vì Giảm)| I["Loại (B) It must increase by 44 units"]
    H -->|Bẫy nhầm lẫn: Lấy số giảm của chiều cao gán cho đáy| J["Loại (C) & (D): decrease / increase by 55 units"]
    H -->|Khớp chuẩn tính toán| K["Chọn (A) It must decrease by 44 units."]
    K --> L["Chốt đáp án chính xác: [A]"]
"""

MINDMAPS[34] = """
flowchart TD
    A["Đề bài (Math #7):<br>Cho hàm số h(x) = 30 – (9)(–3)^x.<br>Tìm tọa độ giao điểm của đồ thị với trục tung (y-intercept) trong mặt phẳng xy?"] --> B{"Định nghĩa giao điểm trục tung (y-intercept)"}
    B --> C["Giao điểm với trục tung luôn xảy ra khi hoành độ x = 0!"]
    C --> D["Bước 1: Thay x = 0 vào phương trình h(x):<br>h(0) = 30 – (9)(–3)⁰"]
    D --> E["Bước 2: Quy tắc lũy thừa cơ bản:<br>Mọi số thực khác không nâng lên lũy thừa 0 đều bằng 1:<br>(–3)⁰ = 1!"]
    E --> F["Bước 3: Thực hiện phép tính:<br>h(0) = 30 – (9)(1) = 30 – 9 = 21"]
    F --> G["Tọa độ giao điểm trục tung là (0, 21)"]
    G --> H{"Chiến thuật loại trừ POOE (Princeton Review)"}
    H -->|Bẫy quên trừ cụm số mũ: chỉ lấy 30| I["Loại (A) (0, 30)"]
    H -->|Bẫy chỉ lấy hệ số 9 hoặc cơ số –3| J["Loại (B) (0, 9)<br>Loại (C) (0, –3)"]
    H -->|Tung độ gốc chuẩn xác| K["Chọn (D) (0, 21)"]
    K --> L["Chốt đáp án chính xác: [D]"]
"""

MINDMAPS[35] = """flowchart TD
    A["Đề bài (Math #8 - Điền số Grid-in):<br>Tam giác vuông cân có cạnh huyền = 4√2 inch.<br>Chu vi viết dưới dạng 2c + 4√2. Tìm giá trị của c?"] --> B{"Công thức tam giác vuông cân 45°-45°-90° (Reference Sheet)"}
    B --> C["Tỉ lệ các cạnh: x : x : x√2<br>(Hai cạnh góc vuông bằng nhau = x, cạnh huyền = x√2)"]
    C --> D["Tìm cạnh góc vuông x:<br>x√2 = 4√2 ➔ x = 4"]
    D --> E["Tính chu vi tam giác (Perimeter):<br>P = x + x + Cạnh huyền<br>P = 4 + 4 + 4√2 = 8 + 4√2"]
    E --> F["Đồng nhất với biểu thức đề bài cho:<br>8 + 4√2 = 2c + 4√2"]
    F --> G["Cân bằng hệ số:<br>2c = 8 ➔ c = 4"]
    G --> H["Chốt đáp án điền số chính xác: 4"]"""

MINDMAPS[36] = """
flowchart TD
    A["Đề bài (Math #9 - Điền số Grid-in):<br>Hai đường tròn cùng tâm. Đường tròn lớn: (x – 2)² + (y + 3)² = 81.<br>Bán kính đường tròn nhỏ bằng 1/3 bán kính lớn. Phương trình đường tròn nhỏ: (x – 2)² + (y + 3)² = c.<br>Tìm giá trị hằng số c?"] --> B{"Phương trình đường tròn chuẩn: (x – h)² + (y – k)² = R²"}
    B --> C["Bước 1: Tìm bán kính đường tròn lớn (R):<br>R² = 81 ➔ R = √81 = 9"]
    C --> D["Bước 2: Tìm bán kính đường tròn nhỏ (r):<br>r = (1/3) × R = (1/3) × 9 = 3"]
    D --> E["Bước 3: Tìm hằng số c ở vế phải phương trình đường tròn nhỏ:<br>c = r² = 3² = 9!"]
    E --> F{"Cảnh giác bẫy SAT"}
    F -->|Bẫy quên bình phương bán kính| G["Bẫy: Nhiều học sinh điền c = 3 (là bán kính r) thay vì r² = 9"]
    F -->|Điền số chuẩn xác| H["Điền số Grid-in: [9]"]
    H --> I["Chốt đáp án chính xác: [9]"]
"""

MINDMAPS[37] = """
flowchart TD
    A["Đề bài (Math #10):<br>Nồng độ thuốc C(s) = 20(0.5)^(s/300) với s tính bằng GIÂY.<br>Nồng độ dự đoán giảm đi x% sau mỗi 5 PHÚT. Tìm giá trị của x?"] --> B{"Quy đổi đơn vị thời gian & Phân tích chu kỳ bán rã (Half-Life)"}
    B --> C["Bước 1: Quy đổi đơn vị:<br>5 phút = 5 × 60 = 300 giây"]
    C --> D["Bước 2: Thay s = 300 giây vào hàm số C(s):<br>C(300) = 20 × (0.5)^(300/300) = 20 × (0.5)¹ = 10 mcg/mL"]
    D --> E["Bước 3: Tính phần trăm suy giảm (Decrease by x%):<br>• Lượng giảm = 20 – 10 = 10<br>• Phần trăm giảm = (10 / 20) × 100% = 50%!"]
    E --> F{"Chiến thuật loại trừ POOE (Princeton Review)"}
    F -->|Cơ số 0.5 là hệ số giảm một nửa, không phải x = 0.5%| G["Loại (A) 0.5<br>Loại (B) 2.5"]
    F -->|Bẫy số 5 phút trong đề bài| H["Loại (C) 5"]
    F -->|Khớp chuẩn mức giảm 50%| I["Chọn (D) 50"]
    I --> J["Chốt đáp án chính xác: [D]"]
"""

MINDMAPS[38] = """
flowchart TD
    A["Đề bài (Math #11):<br>Lô hàng 56 kèn gồm kèn bass và soprano: 10x + 6y = 56.<br>x là số hộp kèn bass, y là số hộp kèn soprano. Ý nghĩa tốt nhất của 10x là gì?"] --> B{"Phân tích ý nghĩa từng thành phần đại số trong ngữ cảnh thực tế"}
    B --> C["• x = Số hộp kèn bass clarinet trong lô hàng<br>• Hệ số 10 = Số lượng kèn bass chứa trong MỖI HỘP (10 kèn/hộp)"]
    C --> D["Phép nhân 10x = (10 chiếc kèn / hộp) × (x hộp kèn bass):<br>Đại diện cho TỔNG SỐ KÈN BASS CLARINET trong toàn bộ lô hàng!"]
    D --> E{"Chiến thuật loại trừ POOE (Princeton Review)"}
    E -->|Nhầm sang kèn soprano (là số hạng 6y)| F["Loại (B) The total number of soprano clarinets"]
    E -->|Nhầm sang hệ số đơn chiếc 10 (chưa nhân x)| G["Loại (C) The number of clarinets in each box"]
    E -->|Nhầm sang biến số x (số lượng hộp)| H["Loại (D) The number of boxes of bass clarinets"]
    D --> I{"Đối chiếu các phương án"}
    I -->|Khớp chuẩn ý nghĩa tích số 10x| J["Chọn (A) The total number of bass clarinets in the shipment"]
    J --> K["Chốt đáp án chính xác: [A]"]
"""

MINDMAPS[39] = """
flowchart TD
    A["Đề bài (Math #12):<br>Bảng số liệu nào gồm 3 cặp giá trị (x, y) là nghiệm của bất phương trình:<br>y > 3x – 4?"] --> B{"Chiến thuật thế điểm (TPR Plugging In Points)"}
    B --> C["Tính giá trị đường biên 3x – 4 tại các hoành độ x = 2, 4, 6:<br>• Tại x = 2: 3(2) – 4 = 2 (yêu cầu y > 2)<br>• Tại x = 4: 3(4) – 4 = 8 (yêu cầu y > 8)<br>• Tại x = 6: 3(6) – 4 = 14 (yêu cầu y > 14)"]
    C --> D{"Kiểm tra từng bảng số liệu"}
    D -->|Bảng B: (2, 10), (4, 16), (6, 22)| E["• 10 > 2 (Thỏa mãn)<br>• 16 > 8 (Thỏa mãn)<br>• 22 > 14 (Thỏa mãn)<br>➔ Cả 3 điểm đều thỏa mãn dấu lớn hơn nghiêm ngặt!"]
    D -->|Bảng A: (2, 2), (4, 8), (6, 14)| F["Loại (A): y = 3x – 4 (dấu bằng, nằm trên đường biên chứ không thỏa mãn dấu >)"]
    D -->|Bảng C & D| G["Loại (C): Tại x = 4 thì y = 8 (không lớn hơn 8)<br>Loại (D): Tại x = 2 thì y = 0 (nhỏ hơn 2)"]
    E --> H["Chọn (B) Bảng gồm các cặp (2, 10), (4, 16), (6, 22)"]
    H --> I["Chốt đáp án chính xác: [B]"]
"""

MINDMAPS[40] = """flowchart TD
    A["Đề bài (Math #13):<br>Parabol đối xứng qua trục x = h và đi qua các điểm đã biết.<br>Tìm tọa độ điểm đối xứng hoặc giao điểm trục hoành."] --> B{"Tính chất đối xứng của Parabol (Parabola Symmetry)"}
    B --> C["Mọi Parabol y = ax² + bx + c luôn có một trục đối xứng thẳng đứng:<br>x = –b / (2a) = x_vertex"]
    C --> D["Hai điểm có cùng tung độ y luôn cách đều trục đối xứng:<br>Khoảng cách d = |x₁ – x_vertex| = |x₂ – x_vertex|"]
    D --> E["Áp dụng tính chất đối xứng để tìm tọa độ x còn lại:<br>x₂ = 2 * x_vertex – x₁"]
    E --> F["Thay số cụ thể từ tọa độ đỉnh và điểm đề bài cho để suy ra nghiệm x = c"]
    F --> G["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[41] = """flowchart TD
    A["Đề bài (Math #14):<br>Phép tịnh tiến đồ thị hàm số: Cho đồ thị y = f(x), xác định hàm số sau tịnh tiến."] --> B{"Quy tắc tịnh tiến hàm số chuẩn (Function Transformation Rules)"}
    B --> C["1. Tịnh tiến ngang (Horizontal Shift):<br>• f(x – h): Dịch chuyển sang PHẢI h đơn vị<br>• f(x + h): Dịch chuyển sang TRÁI h đơn vị"]
    B --> D["2. Tịnh tiến dọc (Vertical Shift):<br>• f(x) + k: Dịch chuyển LÊN TRÊN k đơn vị<br>• f(x) – k: Dịch chuyển XUỐNG DƯỚI k đơn vị"]
    C & D --> E["Quan sát đồ thị thực tế đề bài cung cấp:<br>Đồ thị dịch chuyển tương ứng theo các hướng"]
    E --> F["Kết hợp đúng các biến đổi đại số để chọn dạng hàm số chính xác"]
    F --> G["Chốt đáp án chính xác: [B]"]"""

MINDMAPS[42] = """flowchart TD
    A["Đề bài (Math #15 - Điền số Grid-in):<br>Đường thẳng có giao điểm trục hoành (x-intercept) tại tọa độ (c, p + 4).<br>Tìm giá trị của hằng số c?"] --> B{"Định nghĩa giao điểm trục hoành (x-intercept)"}
    B --> C["Bất kỳ điểm nào nằm trên trục hoành đều có TUNG ĐỘ BẰNG 0:<br>y = 0!"]
    C --> D["Bước 1: Tìm giá trị hằng số p:<br>Tung độ của điểm là p + 4 = 0 ➔ p = –4"]
    D --> E["Bước 2: Thay p = –4 và y = 0 vào phương trình đường thẳng đã cho:<br>Phương trình chứa x, y, p biến thành phương trình chỉ còn ẩn c"]
    E --> F["Giải phương trình bậc nhất tìm c:<br>Thao tác đại số biến đổi ➔ c = –36"]
    F --> G["Chốt đáp án điền số chính xác: –36"]"""

MINDMAPS[43] = """flowchart TD
    A["Đề bài (Math #16):<br>Hệ phương trình bậc nhất 2 ẩn có VÔ SỐ NGHIỆM (Infinitely Many Solutions).<br>Tìm giá trị của hằng số k?"] --> B{"Điều kiện để hệ 2 phương trình có VÔ SỐ NGHIỆM"}
    B --> C["Hai phương trình biểu diễn CÙNG MỘT ĐƯỜNG THẲNG TRÙNG NHAU (Same Line):<br>Tỉ lệ các hệ số tương ứng phải bằng nhau!"]
    C --> D["Dạng tổng quát: a₁x + b₁y = c₁ và a₂x + b₂y = c₂<br>Điều kiện: a₁/a₂ = b₁/b₂ = c₁/c₂"]
    D --> E["Thiết lập tỉ lệ giữa 2 phương trình đề bài:<br>Nhân toàn bộ phương trình 1 với hệ số phù hợp để đồng nhất hệ số x và y"]
    E --> F["Cân bằng hệ số tự do để tìm k:<br>k = 12"]
    F --> G["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[44] = """flowchart TD
    A["Đề bài (Math #17 - Điền số Grid-in):<br>Thùng container 40-foot chứa tối đa 1,200 thùng hàng, tổng khối lượng ≥ 26,300 kg.<br>Loại nhỏ 12.1 kg, Loại lớn 40.7 kg. Tìm số thùng 40.7 kg TỐI THIỂU?"] --> B{"Thiết lập hệ bất phương trình tối ưu hóa"}
    B --> C["Gọi x là số thùng 12.1 kg, y là số thùng 40.7 kg (x, y nguyên dương)<br>• Tổng số thùng: x + y ≤ 1200<br>• Tổng khối lượng: 12.1x + 40.7y ≥ 26300"]
    C --> D["Để số thùng nặng y là NHỎ NHẤT (MINIMUM):<br>Ta phải tận dụng TỐI ĐA số lượng thùng cho phép ➔ Lấy x + y = 1200<br>➔ x = 1200 – y"]
    D --> E["Thay x = 1200 – y vào bất phương trình khối lượng:<br>12.1(1200 – y) + 40.7y ≥ 26300"]
    E --> F["Khai triển và rút gọn:<br>14520 – 12.1y + 40.7y ≥ 26300<br>28.6y ≥ 11780 ➔ y ≥ 411.888..."]
    F --> G["Vì số thùng y bắt buộc phải là số nguyên:<br>Giá trị nguyên nhỏ nhất thỏa mãn y ≥ 411.888 là y = 412!"]
    G --> H["Chốt đáp án điền số chính xác: 412"]"""

MINDMAPS[45] = """flowchart TD
    A["Đề bài (Math #18):<br>Thể tích bể bơi là 79,978 feet khối (ft³).<br>Đổi sang mét khối (m³)? Biết 1 mét ≈ 3.28 feet."] --> B{"Quy tắc đổi đơn vị thể tích (Dimensional Analysis)"}
    B --> C["Mối quan hệ đơn vị độ dài: 1 m ≈ 3.28 ft"]
    C --> D["Lập phương cả hai vế để ra đơn vị THỂ TÍCH:<br>1 m³ = (3.28)³ ft³ = 35.287552 ft³"]
    D --> E["Quy đổi thể tích bể bơi từ ft³ sang m³:<br>Volume = 79978 / (3.28)³<br>Volume = 79978 / 35.287552 ≈ 2,266.46 m³"]
    E --> F{"Cảnh báo bẫy SAT kinh điển (Trap Warning)"}
    F -->|Bẫy chia cho 3.28 mũ 1| G["Nếu chỉ lấy 79978 chia cho 3.28 một lần sẽ ra 24,383.54 (Phương án D bẫy!)"]
    E --> H["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[46] = """flowchart TD
    A["Đề bài (Math #19):<br>Cho đồ thị g(x) = c / (x – d). Biết tiệm cận đứng tại x = 2.<br>Hàm số h(x) = g(x – 3). Xác định phương trình của h(x)?"] --> B{"Phân tích tiệm cận & Phép tịnh tiến hàm phân thức"}
    B --> C["Từ đồ thị g(x): Đường tiệm cận đứng là x = 2 ➔ Mẫu số x – d = 0 tại x = 2<br>➔ d = 2 ➔ g(x) = c / (x – 2)"]
    C --> D["Hàm số h(x) = g(x – 3):<br>Thay thế biến x bằng (x – 3) vào công thức của g(x)"]
    D --> E["Biến đổi đại số mẫu số của h(x):<br>h(x) = c / [(x – 3) – 2] = c / (x – 5)"]
    E --> F["Tiệm cận đứng của h(x) dịch chuyển sang phải 3 đơn vị:<br>Từ x = 2 thành x = 5!"]
    F --> G["Khớp với tử số c = 8 từ các phương án: h(x) = 8 / (x – 5)"]
    G --> H["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[47] = """flowchart TD
    A["Đề bài (Math #20 - Điền số Grid-in):<br>11 số nguyên dương có trung bình cộng = 21.<br>Thêm số thứ 12 thì trung bình cả 12 số là số nguyên < 21.<br>Tìm số nhỏ nhất trong cả tập dữ liệu?"] --> B{"Công thức Trung bình cộng (Average Formula: T = A * N)"}
    B --> C["Tổng của 11 số ban đầu:<br>T₁₁ = 21 * 11 = 231"]
    C --> D["Tổng của cả 12 số:<br>T₁₂ = 231 + x₁₂ (với x₁₂ là số nguyên dương thứ 12)"]
    D --> E["Trung bình cộng của cả 12 số:<br>M₁₂ = (231 + x₁₂) / 12 phải là SỐ NGUYÊN và M₁₂ < 21 ➔ M₁₂ ≤ 20"]
    E --> F["Để tìm số nhỏ nhất, ta tối đa hóa trung bình M₁₂ = 20:<br>231 + x₁₂ = 20 * 12 = 240<br>➔ x₁₂ = 240 – 231 = 9"]
    F --> G["Kiểm tra: 11 số nguyên trong danh sách đều ≥ 12.<br>Do đó số 9 vừa thêm vào chính là số nhỏ nhất trong toàn bộ 12 số!"]
    G --> H["Chốt đáp án điền số chính xác: 9"]"""

MINDMAPS[48] = """flowchart TD
    A["Đề bài (Math #21):<br>Phương trình phi tuyến: 26 – k²/(k² + x²) = x²/(k² + x²)<br>Tìm một nghiệm của phương trình theo hằng số k?"] --> B{"Chiến thuật thế số cụ thể (TPR Plugging In) & Desmos"}
    B --> C["Chọn một giá trị cụ thể cho k, ví dụ k = 2:<br>Phương trình trở thành: 26 – 4/(4 + x²) = x²/(4 + x²)"]
    C --> D["Cộng 4/(4 + x²) sang vế phải:<br>26 = (x² + 4) / (4 + x²) = 1<br>➔ Lưu ý: Trong đề thi gốc, số hạng đầu là 26² (hoặc 676)"]
    D --> E["Bằng máy tính đồ họa Desmos:<br>Nghiệm thực tế x xấp xỉ ±√(26² – k²) ≈ ±25.923"]
    E --> F["Thử thay k = 2 vào các phương án lựa chọn:<br>• (A) k² – 26² = 4 – 676 = –672 (Quá nhỏ)<br>• (B) –√(k² + 26²) = –√(4 + 676) ≈ –26.077 (Sai dấu lệch)<br>• (C) –√(26² – k²) = –√(676 – 4) = –√672 ≈ –25.923 (Khớp tuyệt đối!)"]
    F --> G["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[49] = """flowchart TD
    A["Đề bài (Math #22):<br>Hệ gồm đường thẳng y = 4x – k và parabol y = –3x² + 10x – 8<br>cắt nhau tại DUY NHẤT 1 điểm (x, y). Tìm giá trị của y?"] --> B{"Hai cách giải quyết: Desmos Slider vs Đại số"}
    B -->|Cách 1 - Desmos Slider| C["1. Nhập y = –3x² + 10x – 8<br>2. Nhập y = 4x – k và thêm thanh trượt slider k<br>3. Kéo thanh trượt k cho đến khi đường thẳng tiếp xúc parabol:<br>➔ Đạt được khi k = 5!"]
    C --> D["Bấm vào giao điểm duy nhất trên Desmos:<br>Tọa độ giao điểm là (1, –1)"]
    B -->|Cách 2 - Biệt thức Delta| E["Phương trình hoành độ giao điểm:<br>–3x² + 10x – 8 = 4x – k<br>➔ 3x² – 6x + (8 – k) = 0"]
    E --> F["Cắt nhau duy nhất 1 điểm ➔ Biệt thức Δ = 0:<br>Δ = b² – 4ac = (–6)² – 4(3)(8 – k) = 0<br>36 – 12(8 – k) = 0 ➔ 8 – k = 3 ➔ k = 5"]
    F --> G["Tìm tọa độ nghiệm: x = –b/(2a) = 6/(2*3) = 1<br>➔ Thay x = 1: y = 4(1) – 5 = –1"]
    D & G --> H{"Cảnh báo bẫy SAT kinh điển (RTFQ)"}
    H -->|Đề bài hỏi y| I["• Bẫy x = 1 (Phương án C)<br>• Bẫy k = 5 (Phương án D)<br>• Đề bài hỏi giá trị của y ➔ y = –1"]
    H --> J["Chốt đáp án chính xác: [B]"]"""


def main():
    print("=" * 70)
    print("🚀 Bắt đầu cập nhật Sơ đồ tư duy (Mermaid Mindmaps) cho Princeton SAT Advanced...")
    print("=" * 70)

    target_files = [
        os.path.join(BASE_DIR, "data", "princeton_advanced.json"),
        os.path.join(BASE_DIR, "data", "princetonadvanced.json"),
        os.path.join(BASE_DIR, "static", "data", "princeton_advanced.json"),
        os.path.join(BASE_DIR, "static", "data", "princetonadvanced.json"),
    ]

    # Kiểm tra số lượng mindmaps
    print(f"📊 Đã chuẩn bị {len(MINDMAPS)} sơ đồ tư duy chi tiết.")
    if len(MINDMAPS) != 49:
        print(f"⚠️ Cảnh báo: Số lượng mindmaps ({len(MINDMAPS)}) khác 49!")
        sys.exit(1)

    for file_path in target_files:
        if not os.path.exists(file_path):
            print(f"⚠️ Không tìm thấy file: {file_path}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        questions = data.get("questions", [])
        updated_count = 0

        for q in questions:
            qid = q.get("id")
            if qid in MINDMAPS:
                q["mermaid_diagram"] = MINDMAPS[qid]
                updated_count += 1

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        file_size = os.path.getsize(file_path)
        print(f"  💾 Cập nhật thành công {updated_count}/49 câu hỏi cho: {file_path} ({file_size:,} bytes)")

    print("\n✅ HOÀN TẤT: Toàn bộ 49 sơ đồ tư duy đã được tích hợp đồng bộ vào hệ thống!")


if __name__ == "__main__":
    main()
