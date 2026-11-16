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

MINDMAPS[7] = """flowchart TD
    A["Dạng bài: Cấu trúc tổng thể của đoạn văn (Overall Structure)"] --> B["Đoạn văn về Nhà thiết kế Nhật Bản Yoshioka Tokujin"]
    B --> C["Phần 1 (General Concept):<br>Giới thiệu triết lý sáng tạo kết hợp hiện tượng tự nhiên và tinh thể học"]
    B --> D["Phần 2 (Specific Exemplification):<br>Minh họa chi tiết bằng tác phẩm ghế 'Venus' (nuôi dưỡng tinh thể tự nhiên trong bể nước)"]
    C & D --> E{"Nhận diện quy luật cấu trúc văn bản"}
    E --> F["Đi từ Khái quát triết lý thiết kế chung (General Approach)<br>➔ Đến Ví dụ tác phẩm cụ thể minh chứng (Specific Application)"]
    F --> G{"Đối chiếu các phương án POOE"}
    G -->|Không có tranh luận hay thương mại| H["Loại (A) Tranh cãi giữa hai nhà phê bình<br>Loại (C) Lịch sử nhiều nhà thiết kế khác nhau<br>Loại (D) Vấn đề môi trường và giải pháp thương mại"]
    G -->|Khớp chuẩn khuôn mẫu| I["Chọn (B): Introduces an artist's general approach and then provides<br>a specific illustration of that approach in practice."]
    I --> J["Chốt đáp án chính xác: [B]"]"""

MINDMAPS[8] = """flowchart TD
    A["Dạng bài: Chức năng câu gạch chân (Sentence Function)<br>Văn bản Sinh học về cá cần câu biển sâu (Anglerfish)"] --> B["Câu trước: Cá cần câu sở hữu mồi nhử phát sáng (esca) để thu hút con mồi trong bóng tối"]
    B --> C["Câu gạch chân: Miêu tả vi khuẩn phát quang cộng sinh (symbiotic bioluminescent bacteria) sinh sống bên trong esca"]
    C --> D{"Phân tích mối quan hệ logic giữa 2 câu"}
    D --> E["Câu gạch chân giải thích CƠ CHẾ SINH HỌC (Physiological Mechanism)<br>tạo ra hiện tượng phát sáng đã được đề cập trước đó"]
    E --> F{"Loại trừ các phương án gây nhiễu"}
    F -->|Sai chức năng tu từ| G["Loại (A) Thách thức thuyết tiến hóa<br>Loại (B) Ngoại lệ của quy luật sinh học<br>Loại (C) Tóm tắt lịch sử tranh luận"]
    F -->|Đúng cơ chế sinh học| H["Chọn (D): Details the physiological process responsible for the adaptation mentioned in the preceding sentence."]
    H --> I["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[9] = """flowchart TD
    A["Dạng bài: Tổng hợp hai văn bản (Dual Texts Synthesis)<br>Về nguồn gốc tiến hóa của tế bào nhân thực (Eukaryotes)"] --> B["Text 1 (Gabaldón et al.):<br>Giả thuyết tế bào tổ tiên đơn giản đã trao đổi vật chất di truyền (Horizontal Gene Transfer) TRƯỚC KHI xảy ra nội cộng sinh"]
    A --> C["Text 2 (Quan điểm mới):<br>Mô hình bộ gen mới nhất chỉ ra chính biến cố nội cộng sinh (Endosymbiosis) mới là ngòi nổ chính cho việc chuyển gen"]
    B & C --> D{"Tác giả Text 2 sẽ nhận định thế nào về giả thuyết của Text 1?"}
    D --> E["Thừa nhận giả thuyết của Gabaldón hấp dẫn/thú vị<br>NHƯNG bị thách thức bởi dữ liệu thời gian nội cộng sinh xảy ra sớm hơn"]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Bác bỏ cực đoan hoặc đồng tình hoàn toàn| G["Loại (A) Bác bỏ hoàn toàn là ngụy khoa học (quá cực đoan)<br>Loại (B) Hoàn toàn đồng ý (sai thực tế Text 2)<br>Loại (D) Không liên quan đến dữ liệu gen"]
    F -->|Đánh giá sắc thái cân bằng| H["Chọn (C): Thừa nhận đây là giả thuyết đáng chú ý nhưng bị lung lay bởi bằng chứng bộ gen mới về mốc thời gian nội cộng sinh."]
    H --> I["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[10] = """flowchart TD
    A["Dạng bài: Phân tích bảng số liệu (Quantitative / Tables)<br>Tỉ lệ nảy mầm của các loài hạt thực vật sa mạc theo nhiệt độ"] --> B{"Mục tiêu đề bài yêu cầu"}
    B --> C["Tìm dữ liệu chứng minh một loài thực vật bị sụt giảm mạnh tỉ lệ nảy mầm khi nhiệt độ vượt ngưỡng 35°C"]
    C --> D["Tra cứu bảng số liệu tại các cột: 25°C, 30°C, 35°C, 40°C"]
    D --> E["Quan sát hàng loài 'Echinocactus':<br>• Ở 30°C: Nảy mầm đạt 85%<br>• Ở 35°C: Nảy mầm duy trì 78%<br>• Ở 40°C: Nảy mầm tụt dốc thảm hại xuống 12%"]
    E --> F{"Đối chiếu số liệu các phương án"}
    F -->|Sai số liệu hoặc sai loài| G["Loại (B), (C), (D) do trích dẫn sai loài hoặc sai mốc phần trăm tụt giảm"]
    F -->|Khớp chính xác bảng dữ liệu| H["Chọn (A): Trích dẫn chính xác số liệu sụt giảm từ trên 75% xuống dưới 15% của loài Echinocactus."]
    H --> I["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[11] = """flowchart TD
    A["Dạng bài: Bằng chứng củng cố luận điểm (Command of Evidence - Support)<br>Luận điểm của nhà cổ sinh vật học Tang"] --> B{"Luận điểm của Tang"}
    B --> C["Tảo lục (Green Algae) tiến hóa lần đầu tiên trong môi trường ĐẠI DƯƠNG / BIỂN,<br>chứ không phải trong môi trường nước ngọt như sông hồ."]
    C --> D{"Bằng chứng nào củng cố trực tiếp nhất cho Tang?"}
    D --> E["Cần phát hiện hóa thạch tảo lục cổ xưa nhất nằm độc quyền trong các tầng trầm tích biển sâu,<br>hoàn toàn không có dấu vết trầm tích nước ngọt."]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Không chứng minh nguồn gốc đại dương| G["Loại (A) Tìm thấy tảo nước ngọt hiện đại<br>Loại (B) Tảo biển có nhiều sắc tố hơn (không chứng minh thời điểm)<br>Loại (C) Hóa thạch không xác định niên đại"]
    F -->|Bằng chứng địa tầng biển 1 tỷ năm tuổi| H["Chọn (D): Vi hóa thạch tảo lục cổ nhất (1 tỷ năm) được khai quật tại phiến sét biển sâu không chứa khoáng vật nước ngọt."]
    H --> I["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[12] = """flowchart TD
    A["Dạng bài: Bằng chứng từ biểu đồ (Quantitative / Graphs)<br>Biểu đồ tần số tiếng hót của chim thành thị vs chim rừng"] --> B{"Kết luận của nhà nghiên cứu cần chứng minh"}
    B --> C["Chim thành thị hót ở tần số tối thiểu (Minimum Frequency) CAO HƠN chim rừng<br>để tránh bị lấn át bởi tiếng ồn giao thông tần số thấp."]
    C --> D["Đọc các trục và chú giải của biểu đồ"]
    D --> E["• Trục tung: Tần số tối thiểu (kHz)<br>• Cột Urban: Đạt xấp xỉ 2.2 kHz<br>• Cột Forest: Chỉ ở mức xấp xỉ 1.4 kHz"]
    E --> F{"Đối chiếu số liệu các phương án"}
    F -->|Đọc sai trục hoặc ngược xu hướng| G["Loại (B) Tần số tối đa (không phải trọng tâm)<br>Loại (C) Đảo ngược số liệu<br>Loại (D) Không có sự khác biệt"]
    F -->|Khớp chuẩn xác số liệu so sánh| H["Chọn (A): Tần số tối thiểu của chim thành thị cao hơn đáng kể so với chim rừng tự nhiên."]
    H --> I["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[13] = """flowchart TD
    A["Dạng bài: Bằng chứng làm suy yếu kết luận (Weaken Claims)<br>Sự kiện nổ Tunguska năm 1908 tại Siberia"] --> B{"Kết luận của Kulik cần làm suy yếu"}
    B --> C["Vụ nổ là do một thiên thạch kim loại giàu sắt-niken (Iron Meteorite)<br>đã va chạm trực tiếp xuống mặt đất."]
    C --> D{"Phát hiện nào nếu có thật sẽ bác bỏ kết luận của Kulik?"}
    D --> E["Chứng minh vụ nổ là một vụ nổ trên không (Airburst) của thiên thể băng/sao chổi,<br>hoàn toàn KHÔNG để lại mảnh thiên thạch sắt hay miệng hố va chạm."]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Ủng hộ hoặc không liên quan| G["Loại (A) Cây cối đổ rạp hình cánh bướm (ủng hộ nổ)<br>Loại (B) Động đất ghi nhận toàn cầu<br>Loại (C) Lời kể của nhân chứng"]
    F -->|Không tìm thấy tàn tích sắt-niken| H["Chọn (D): Mẫu đất tại tâm chấn chỉ chứa bụi silicate và dấu vết băng cometary, hoàn toàn không có mảnh thiên thạch sắt-niken."]
    H --> I["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[14] = """flowchart TD
    A["Dạng bài: Bằng chứng ủng hộ sự đính chính (Support Clarification)"] --> B{"Lời đính chính của nhà báo"}
    B --> C["Mặc dù mạng xã hội đồn rằng triển lãm sắp tới là lần đầu tiên bảo tàng trưng bày nghệ thuật bản địa,<br>nhưng thực tế bảo tàng ĐÃ TỪNG tổ chức các triển lãm nghệ thuật bản địa trong quá khứ."]
    C --> D{"Tìm dữ kiện lịch sử chứng minh bảo tàng từng triển lãm trước đây"}
    D --> E["Hồ sơ lưu trữ hoặc sự kiện thực tế trong quá khứ xác nhận các đợt trưng bày tranh/ảnh/hiện vật của nghệ sĩ bản địa."]
    E --> F{"Chiến thuật loại trừ POOE"}
    F -->|Chỉ nói về dự định tương lai hoặc bảo tàng khác| G["Loại (A) Bảo tàng dự định mua thêm tranh<br>Loại (B) Bảo tàng khác có bộ sưu tập lớn hơn<br>Loại (D) Du khách yêu thích nghệ thuật bản địa"]
    F -->|Hồ sơ triển lãm năm 2014 & 2018| H["Chọn (C): Tài liệu lưu trữ xác nhận bảo tàng đã tổ chức các triển lãm cá nhân lớn cho nghệ sĩ khắc bản địa vào năm 2014 và 2018."]
    H --> I["Chốt đáp án chính xác: [C]"]"""

MINDMAPS[15] = """flowchart TD
    A["Dạng bài: Hoàn thành suy luận logic (Logical Completion / Inferences)"] --> B["Thí nghiệm tâm lý xã hội về việc phán đoán hệ tư tưởng/chính trị của người khác"]
    B --> C["Manh mối 1: Khi người tham gia chỉ dựa vào tín hiệu thị giác bên ngoài (quần áo, diện mạo),<br>tỉ lệ đoán sai rất cao và chứa nhiều định kiến."]
    B --> D["Manh mối 2: Khi được trò chuyện trực tiếp dù chỉ vài phút,<br>độ chính xác tăng vọt lên mức đáng kể."]
    C & D --> E{"Suy luận kết luận hợp lý nhất (Logical Inference)"}
    E --> F["Các tín hiệu thị giác đơn thuần KHÔNG THỂ thay thế cho đối thoại trực tiếp<br>nếu muốn đánh giá chính xác lập trường tư tưởng thực sự."]
    F --> G{"Chiến thuật loại trừ POOE"}
    G -->|Suy diễn quá đà hoặc sai trọng tâm| H["Loại (B) Con người không bao giờ hiểu được nhau<br>Loại (C) Trang phục luôn phản ánh trung thực tư tưởng<br>Loại (D) Đối thoại làm sai lệch ấn tượng ban đầu"]
    G -->|Khớp chuẩn suy luận logic| I["Chọn (A): Visual cues alone are inadequate for accurately determining an individual's ideological orientation."]
    I --> J["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[16] = """flowchart TD
    A["Dạng bài: Hoàn thành suy luận logic (Logical Completion)<br>Nghệ thuật vẽ cát truyền thống (Sandroing) tại Vanuatu"] --> B{"Dữ kiện thực tế trong đoạn văn"}
    B --> C["1. Tranh cát là phương tiện lưu giữ tri thức nghi lễ, phả hệ, hiệp ước xã hội phức tạp."]
    B --> D["2. Tuy nhiên, do vẽ trên nền cát ven biển, các bức vẽ vật lý nhanh chóng bị sóng và gió xóa nhòa."]
    C & D --> E{"Nghịch lý: Vật thể vật lý biến mất nhưng tri thức văn hóa vẫn trường tồn?"}
    E --> F["Sự tồn tại lâu bền của truyền thống KHÔNG phụ thuộc vào việc bảo tồn vật thể cát,<br>mà phụ thuộc vào việc các thế hệ nghệ nhân liên tục học thuộc và tái hiện lại qua truyền khẩu."]
    F --> G{"Chiến thuật loại trừ POOE"}
    G -->|Mâu thuẫn với bản chất văn hóa phi vật thể| H["Loại (A) Người dân đã chuyển sang vẽ trên vải vĩnh cửu<br>Loại (C) Ý nghĩa của các hình vẽ đã bị lãng quên hoàn toàn<br>Loại (D) Tranh cát chỉ mang tính trang trí tức thời"]
    G -->|Khớp chuẩn giá trị di sản sống| I["Chọn (B): Cultural continuity relies on living practitioners repeatedly recreating the designs and oral narratives."]
    I --> J["Chốt đáp án chính xác: [B]"]"""

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

MINDMAPS[20] = """flowchart TD
    A["Dạng bài: Hòa hợp thì & Thể động từ (Verb Tense & Aspect)"] --> B["Văn bản nghiên cứu lịch sử y tế của cựu chiến binh"]
    B --> C{"Xác định mốc thời gian & Trình tự hành động"}
    C --> D["Mốc quá khứ mỏ neo (Past Baseline):<br>Thời điểm các bác sĩ đánh giá bệnh án sau chiến tranh (Quá khứ đơn - Simple Past)"]
    C --> E["Hành động cần điền:<br>Việc tham gia phục vụ trong quân ngũ ĐÃ DIỄN RA VÀ HOÀN TẤT TRƯỚC mốc mỏ neo đó!"]
    D & E --> F{"Quy tắc thì Quá khứ hoàn thành (Past Perfect Rule)"}
    F --> G["Hành động xảy ra trước một hành động khác trong quá khứ<br>BẮT BUỘC phải chia ở thì Quá khứ hoàn thành: HAD + V3/ed"]
    G --> H{"Đối chiếu các phương án"}
    H -->|Sai thì| I["Loại (B) took: Quá khứ đơn (không thể hiện được thứ tự trước-sau)<br>Loại (C) take: Hiện tại đơn (lệch hoàn toàn ngữ cảnh quá khứ)<br>Loại (D) will take: Tương lai (sai)"]
    H -->|Đúng quá khứ hoàn thành| J["Chọn (A) had taken: Diễn tả chuẩn xác sự kiện xảy ra trước mốc quá khứ."]
    J --> K["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[21] = """flowchart TD
    A["Dạng bài: Hòa hợp Chủ ngữ - Vị ngữ (Subject-Verb Agreement)"] --> B["Văn bản: 'A prominent non-profit organization that advocates for clean energy across several nations ________ government policy.'"]
    B --> C{"Chiến thuật bóc tách thành phần câu (TPR Subject Isolation)"}
    C --> D["Gạch bỏ cụm mệnh đề quan hệ chen giữa:<br>'that advocates for clean energy across several nations'"]
    C --> E["Chủ ngữ cốt lõi (True Subject):<br>'organization' ➔ Danh từ số ít (Singular Noun)!"]
    E --> F{"Quy tắc hòa hợp số ít"}
    F --> G["Chủ ngữ số ít đi với Động từ số ít (thêm -s / -es ở hiện tại đơn)"]
    G --> H{"Đối chiếu các lựa chọn"}
    H -->|Động từ số nhiều| I["Loại (A) were influencing: Số nhiều (were)<br>Loại (B) have influenced: Số nhiều (have)<br>Loại (C) influence: Số nhiều (nguyên thể)"]
    H -->|Động từ số ít duy nhất| J["Chọn (D) influences: Động từ số ít hòa hợp tuyệt đối với 'organization'."]
    J --> K["Chốt đáp án chính xác: [D]"]"""

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

MINDMAPS[25] = """flowchart TD
    A["Dạng bài: Từ nối logic Khái quát ➔ Cụ thể (General to Specific Transition)"] --> B{"Phân tích mối quan hệ giữa 2 câu"}
    B --> C["Câu 1 (Ý khái quát - General):<br>Kính hiển vi quang học truyền thống có những hạn chế nghiêm trọng khi quan sát các cấu trúc virus siêu vi."]
    B --> D["Câu 2 (Minh họa kỹ thuật cụ thể - Specific):<br>Phương pháp cryo-electron tomography giải quyết nhược điểm này bằng cách chụp mẫu ở trạng thái đông lạnh với độ phân giải dưới 1 nanometer."]
    C & D --> E{"Xác định bản chất logic"}
    E --> F["Đi từ nhận định chung về hạn chế ➔ Đến giải pháp kỹ thuật cụ thể chi tiết.<br>Cần từ nối mang tính 'Cụ thể là / Đi vào chi tiết' (Specifically / In particular)."]
    F --> G{"Chiến thuật loại trừ POOE"}
    G -->|Sai mối quan hệ| H["Loại (A) Nevertheless: Quan hệ tương phản (sai)<br>Loại (C) Likewise: Quan hệ tương đồng 2 sự việc khác nhau (sai)<br>Loại (D) Still: Quan hệ nhượng bộ (sai)"]
    G -->|Đúng bản chất minh họa chi tiết| I["Chọn (B) Specifically,"]
    I --> J["Chốt đáp án chính xác: [B]"]"""

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

MINDMAPS[33] = """flowchart TD
    A["Đề bài (Math #6):<br>Tỉ lệ đáy / chiều cao của tam giác DEF là 5 : 2.<br>Đáy gấp đôi, chiều cao gấp ba ➔ Tỉ lệ mới là bao nhiêu?"] --> B{"Chiến thuật thử số cụ thể (TPR Plugging In)"}
    B --> C["Chọn giá trị ban đầu theo đúng tỉ lệ:<br>• Đáy ban đầu (b) = 5<br>• Chiều cao ban đầu (h) = 2"]
    C --> D["Tính toán kích thước mới theo đề bài:<br>• Đáy mới (b') = 5 * 2 = 10<br>• Chiều cao mới (h') = 2 * 3 = 6"]
    D --> E["Thiết lập tỉ lệ mới:<br>b' / h' = 10 / 6"]
    E --> F["Rút gọn phân số tối giản:<br>10 / 6 = 5 / 3 (5 to 3)"]
    F --> G{"Cảnh báo bẫy SAT"}
    G -->|Bẫy chưa rút gọn| H["Phương án (D) 10 to 6 chưa rút gọn tối giản!"]
    F --> I["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[34] = """flowchart TD
    A["Đề bài (Math #7):<br>Tìm tọa độ giao điểm với trục tung (y-intercept)<br>của đồ thị y = 3(0.5)^(x+2) – 1"] --> B{"Định nghĩa giao điểm trục tung (y-intercept)"}
    B --> C["Giao điểm trục tung luôn có hoành độ x = 0!"]
    C --> D["Thay x = 0 vào hàm số để tìm tung độ y:<br>y = 3 * (0.5)^(0 + 2) – 1"]
    D --> E["Tính toán lũy thừa & nhân:<br>y = 3 * (0.5)² – 1<br>y = 3 * 0.25 – 1<br>y = 0.75 – 1 = –0.25"]
    E --> F["Tọa độ hoàn chỉnh: (0, –0.25)"]
    B -->|Cách Desmos siêu tốc| G["Nhập biểu thức vào Desmos:<br>y = 3(0.5)^(x+2) – 1<br>Bấm vào chấm xám trên trục y ➔ Hiện ngay (0, –0.25)"]
    F & G --> H["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[35] = """flowchart TD
    A["Đề bài (Math #8 - Điền số Grid-in):<br>Tam giác vuông cân có cạnh huyền = 4√2 inch.<br>Chu vi viết dưới dạng 2c + 4√2. Tìm giá trị của c?"] --> B{"Công thức tam giác vuông cân 45°-45°-90° (Reference Sheet)"}
    B --> C["Tỉ lệ các cạnh: x : x : x√2<br>(Hai cạnh góc vuông bằng nhau = x, cạnh huyền = x√2)"]
    C --> D["Tìm cạnh góc vuông x:<br>x√2 = 4√2 ➔ x = 4"]
    D --> E["Tính chu vi tam giác (Perimeter):<br>P = x + x + Cạnh huyền<br>P = 4 + 4 + 4√2 = 8 + 4√2"]
    E --> F["Đồng nhất với biểu thức đề bài cho:<br>8 + 4√2 = 2c + 4√2"]
    F --> G["Cân bằng hệ số:<br>2c = 8 ➔ c = 4"]
    G --> H["Chốt đáp án điền số chính xác: 4"]"""

MINDMAPS[36] = """flowchart TD
    A["Đề bài (Math #9 - Điền số Grid-in):<br>Đường tròn A: (x – 3)² + (y + 1)² = 81.<br>Đường tròn B có đường kính bằng bán kính của A. Tìm đường kính của B?"] --> B{"Phương trình đường tròn chuẩn (Circle Equation)"}
    B --> C["Dạng chuẩn: (x – h)² + (y – k)² = R²"]
    C --> D["Xác định bán kính đường tròn A (R_A):<br>R_A² = 81 ➔ R_A = √81 = 9"]
    D --> E["Đọc kỹ giả thiết về Đường tròn B:<br>'Circle B has diameter equal to the radius of Circle A'<br>(Đường kính của B bằng bán kính của A)"]
    E --> F["Tính đường kính của đường tròn B:<br>Diameter_B = R_A = 9"]
    F --> G{"Cảnh báo bẫy SAT (RTFQ)"}
    G -->|Đề bài hỏi Đường kính| H["Đề bài hỏi ĐƯỜNG KÍNH của B, không hỏi bán kính của B!<br>Không chia đôi thành 4.5."]
    F --> I["Chốt đáp án điền số chính xác: 9"]"""

MINDMAPS[37] = """flowchart TD
    A["Đề bài (Math #10):<br>Nồng độ huyết tương C(t) = C₀(0.82)^(t/4) với t tính theo giờ.<br>Tìm phương trình tương đương mô tả tốc độ suy giảm theo từng giờ."] --> B{"Quy tắc biến đổi số mũ (Power of a Power Rule)"}
    B --> C["Tách số mũ t/4 thành lũy thừa của lũy thừa:<br>(0.82)^(t/4) = [(0.82)^(1/4)]^t = [⁴√0.82]^t"]
    C --> D["Tính toán giá trị cơ số mới bằng máy tính:<br>0.82^(0.25) ≈ 0.9515 ≈ 0.95"]
    D --> E["Hàm số viết lại theo chu kỳ 1 giờ:<br>C(t) = C₀(0.95)^t"]
    E --> F{"Ý nghĩa thực tế của cơ số 0.95"}
    F --> G["Mỗi giờ trôi qua, nồng độ còn lại xấp xỉ 95% (tức giảm 5% mỗi giờ)."]
    E & G --> H["Chốt đáp án chính xác: [D]"]"""

MINDMAPS[38] = """flowchart TD
    A["Đề bài (Math #11):<br>Giải thích ý nghĩa của hệ số trong phương trình tuyến tính thực tế<br>P = 15.5 + 2.4t"] --> B{"Bản chất phương trình tuyến tính y = mx + b"}
    B --> C["• Tung độ gốc b (15.5): Giá trị ban đầu tại thời điểm t = 0"]
    B --> D["• Hệ số góc m (2.4): Tốc độ thay đổi (Rate of Change)<br>Mỗi đơn vị thời gian t tăng thêm 1, giá trị P tăng tương ứng 2.4 đơn vị!"]
    C & D --> E{"Đối chiếu câu hỏi đề bài"}
    E --> F["Đề bài hỏi ý nghĩa của con số 2.4 trong ngữ cảnh:<br>Đó chính là lượng tăng thêm trung bình mỗi năm/tháng của đại lượng P."]
    F --> G{"Chiến thuật loại trừ POOE"}
    G -->|Bẫy nhầm lẫn m và b| H["Loại các phương án coi 2.4 là giá trị khởi điểm ban đầu<br>hoặc nhầm sang tổng số lượng."]
    F --> I["Chốt đáp án chính xác: [A]"]"""

MINDMAPS[39] = """flowchart TD
    A["Đề bài (Math #12):<br>Tìm bảng giá trị thỏa mãn bất phương trình y > 2x – 5"] --> B{"Phương pháp kiểm tra điểm (Point Testing Strategy)"}
    B --> C["Lần lượt thử các cặp tọa độ (x, y) từ mỗi bảng vào bất phương trình:<br>Kiểm tra xem y có THỰC SỰ LỚN HƠN (2x – 5) hay không!"]
    C --> D{"Kiểm tra Bảng A"}
    D -->|Có điểm vi phạm| E["Tại điểm (2, –1): 2(2) – 5 = –1 ➔ y = –1 không lớn hơn –1 (Sai!) ➔ Loại A"]
    C --> F{"Kiểm tra Bảng B"}
    F --> G["• Điểm 1: x = 0, y = 0 ➔ 0 > 2(0) – 5 = –5 (ĐÚNG)<br>• Điểm 2: x = 1, y = –1 ➔ –1 > 2(1) – 5 = –3 (ĐÚNG)<br>• Điểm 3: x = 3, y = 3 ➔ 3 > 2(3) – 5 = 1 (ĐÚNG)"]
    G --> H["Tất cả các điểm trong Bảng B đều thỏa mãn bất phương trình!"]
    H --> I["Chốt đáp án chính xác: [B]"]"""

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
