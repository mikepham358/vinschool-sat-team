#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Complete College Panda SAT Math Database (330 Questions across 27 Chapters)
Source Excel: /Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/26-27 Grand Plan /Study Plan/Math/Template - Full Nielson Phu SAT Math.xlsx
Source Book & PDF: SAT Coach/Books/Nielson Phu - SAT Math The College Panda.pdf (317 pages)
Target: data/panda_math.json (and mirrors)

Strict pedagogical No-Leak Policy:
- Tier 1 (L1) and Tier 2 (L2) hints strictly do NOT leak or contain the answer
  (neither choice letters A/B/C/D nor target answer numerical/algebraic values).
- Exact per-question exercise PDF page mapping verified directly from scanned book.
"""

import json
import os
import re
import openpyxl

EXCEL_PATH = "/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/26-27 Grand Plan /Study Plan/Math/Template - Full Nielson Phu SAT Math.xlsx"
PANDA_APP_DB = "/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/SAT Coach/PandaMathApp/database.json"
PDF_PATH = "SAT Coach/Books/Nielson Phu - SAT Math The College Panda.pdf"
PDF_DRIVE_ID = "1z4CC7X-L3e3XZr04uc7RgMZBK5lYs8Gb"
PDF_PREVIEW_URL = f"https://drive.google.com/file/d/{PDF_DRIVE_ID}/preview"
PDF_VIEW_URL = f"https://drive.google.com/file/d/{PDF_DRIVE_ID}/view?usp=drive_open"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_JSON = os.path.join(BASE_DIR, "data", "panda_math.json")

# Verified Chapter Page Mappings from Book Table of Contents & Exercises
CHAPTER_MAPPING = {
    1: {"name": "Exponents & Radicals", "vn_sub": "Lũy thừa & Căn thức", "book_page": 7, "pdf_page": 9, "ex_start": 15, "domain": "Passport to Advanced Math"},
    2: {"name": "Percent", "vn_sub": "Phần trăm & Biến thiên phần trăm", "book_page": 15, "pdf_page": 17, "ex_start": 23, "domain": "Problem Solving & Data Analysis"},
    3: {"name": "Exponential vs. Linear Growth", "vn_sub": "Mô hình Tuyến tính vs Số mũ", "book_page": 24, "pdf_page": 26, "ex_start": 29, "domain": "Problem Solving & Data Analysis"},
    4: {"name": "Proportion", "vn_sub": "Tỷ lệ thức & Biến thiên", "book_page": 31, "pdf_page": 33, "ex_start": 34, "domain": "Problem Solving & Data Analysis"},
    5: {"name": "Rates", "vn_sub": "Tốc độ & Hệ số chuyển đổi", "book_page": 36, "pdf_page": 38, "ex_start": 38, "domain": "Problem Solving & Data Analysis"},
    6: {"name": "Expressions", "vn_sub": "Biểu thức đại số & Phân thức", "book_page": 42, "pdf_page": 44, "ex_start": 49, "domain": "Passport to Advanced Math"},
    7: {"name": "Manipulating & Solving Equations", "vn_sub": "Biến đổi & Giải phương trình", "book_page": 49, "pdf_page": 51, "ex_start": 59, "domain": "Heart of Algebra"},
    8: {"name": "More Equation Solving Strategies", "vn_sub": "Đổi biến & Chiến thuật giải nhanh", "book_page": 58, "pdf_page": 60, "ex_start": 67, "domain": "Passport to Advanced Math"},
    9: {"name": "Systems of Equations", "vn_sub": "Hệ phương trình tuyến tính", "book_page": 67, "pdf_page": 69, "ex_start": 77, "domain": "Heart of Algebra"},
    10: {"name": "Inequalities", "vn_sub": "Bất đẳng thức & Hệ bất phương trình", "book_page": 79, "pdf_page": 81, "ex_start": 87, "domain": "Heart of Algebra"},
    11: {"name": "Word Problems", "vn_sub": "Giải toán bằng cách lập phương trình", "book_page": 90, "pdf_page": 92, "ex_start": 98, "domain": "Heart of Algebra / Problem Solving"},
    12: {"name": "Lines", "vn_sub": "Đường thẳng & Hàm tuyến tính", "book_page": 99, "pdf_page": 101, "ex_start": 108, "domain": "Heart of Algebra"},
    13: {"name": "Interpreting Linear Models", "vn_sub": "Giải nghĩa mô hình thực tế", "book_page": 109, "pdf_page": 111, "ex_start": 113, "domain": "Heart of Algebra"},
    14: {"name": "Functions", "vn_sub": "Hàm số & Đồ thị hàm số", "book_page": 115, "pdf_page": 117, "ex_start": 123, "domain": "Passport to Advanced Math"},
    15: {"name": "Quadratics", "vn_sub": "Phương trình bậc hai & Parabol", "book_page": 126, "pdf_page": 128, "ex_start": 140, "domain": "Passport to Advanced Math"},
    16: {"name": "Synthetic Division", "vn_sub": "Chia đa thức & Định lý số dư", "book_page": 141, "pdf_page": 143, "ex_start": 150, "domain": "Passport to Advanced Math"},
    17: {"name": "Complex Numbers", "vn_sub": "Số phức & Đơn vị ảo i", "book_page": 150, "pdf_page": 152, "ex_start": 154, "domain": "Additional Topics in Math"},
    18: {"name": "Absolute Value", "vn_sub": "Giá trị tuyệt đối", "book_page": 154, "pdf_page": 156, "ex_start": 159, "domain": "Heart of Algebra"},
    19: {"name": "Angles", "vn_sub": "Góc & Đa giác", "book_page": 160, "pdf_page": 162, "ex_start": 166, "domain": "Additional Topics in Math"},
    20: {"name": "Triangles", "vn_sub": "Tam giác & Radian", "book_page": 168, "pdf_page": 170, "ex_start": 181, "domain": "Additional Topics in Math"},
    21: {"name": "Circles", "vn_sub": "Đường tròn & Phương trình đường tròn", "book_page": 189, "pdf_page": 191, "ex_start": 196, "domain": "Additional Topics in Math"},
    22: {"name": "Trigonometry", "vn_sub": "Lượng giác (Sin, Cos, Tan)", "book_page": 198, "pdf_page": 200, "ex_start": 204, "domain": "Additional Topics in Math"},
    23: {"name": "Reading Data", "vn_sub": "Đọc và Phân tích biểu đồ dữ liệu", "book_page": 205, "pdf_page": 207, "ex_start": 208, "domain": "Problem Solving & Data Analysis"},
    24: {"name": "Probability", "vn_sub": "Xác suất & Bảng tần số 2 chiều", "book_page": 214, "pdf_page": 216, "ex_start": 217, "domain": "Problem Solving & Data Analysis"},
    25: {"name": "Statistics I", "vn_sub": "Thống kê I: Trung bình, Trung vị, Độ phân tán", "book_page": 223, "pdf_page": 225, "ex_start": 229, "domain": "Problem Solving & Data Analysis"},
    26: {"name": "Statistics II", "vn_sub": "Thống kê II: Mẫu, Thí nghiệm & Sai số", "book_page": 233, "pdf_page": 235, "ex_start": 242, "domain": "Problem Solving & Data Analysis"},
    27: {"name": "Volume", "vn_sub": "Thể tích & Diện tích toàn phần", "book_page": 246, "pdf_page": 248, "ex_start": 250, "domain": "Additional Topics in Math"}
}

# Verified Exact Per-Question Exercise Page Partitions
# Format: (start_qid, end_qid, pdf_page)
EXACT_PAGE_PARTITIONS = [
    # Ch 1: Exponents & Radicals (pp. 15-16)
    (1, 8, 15), (9, 15, 16),
    # Ch 2: Percent (pp. 23-25)
    (16, 21, 23), (22, 27, 24), (28, 33, 25),
    # Ch 3: Exponential vs. Linear Growth (pp. 29-31)
    (34, 36, 29), (37, 40, 30), (41, 41, 31),
    # Ch 4: Proportion (pp. 34-35)
    (42, 46, 34), (47, 49, 35),
    # Ch 5: Rates (pp. 38-41)
    (50, 53, 38), (54, 59, 39), (60, 64, 40), (65, 65, 41),
    # Ch 6: Expressions (pp. 49-50)
    (66, 72, 49), (73, 77, 50),
    # Ch 7: Manipulating & Solving Equations (pp. 59-60)
    (78, 85, 59), (86, 89, 60),
    # Ch 8: More Equation Solving Strategies (pp. 67-68)
    (90, 96, 67), (97, 101, 68),
    # Ch 9: Systems of Equations (pp. 77-80)
    (102, 106, 77), (107, 111, 78), (112, 116, 79), (117, 117, 80),
    # Ch 10: Inequalities (pp. 87-91)
    (118, 121, 87), (122, 125, 88), (126, 127, 89), (128, 132, 90), (133, 133, 91),
    # Ch 11: Word Problems (pp. 98-100)
    (134, 140, 98), (141, 146, 99), (147, 148, 100),
    # Ch 12: Lines (pp. 108-110)
    (149, 152, 108), (153, 157, 109), (158, 160, 110),
    # Ch 13: Interpreting Linear Models (pp. 113-116)
    (161, 164, 113), (165, 168, 114), (169, 172, 115), (173, 176, 116),
    # Ch 14: Functions (pp. 123-125)
    (177, 180, 123), (181, 187, 124), (188, 192, 125),
    # Ch 15: Quadratics (pp. 140-142)
    (193, 199, 140), (200, 204, 141), (205, 206, 142),
    # Ch 16: Synthetic Division (pp. 150-151)
    (207, 211, 150), (212, 219, 151),
    # Ch 17: Complex Numbers (pp. 154-155)
    (220, 226, 154), (227, 231, 155),
    # Ch 18: Absolute Value (pp. 159-161)
    (232, 236, 159), (237, 242, 160), (243, 243, 161),
    # Ch 19: Angles (pp. 166-169)
    (244, 247, 166), (248, 251, 167), (252, 255, 168), (256, 258, 169),
    # Ch 20: Triangles (pp. 181-184)
    (259, 262, 181), (263, 267, 182), (268, 271, 183), (272, 274, 184),
    # Ch 21: Circles (pp. 196-197)
    (275, 278, 196), (279, 282, 197),
    # Ch 22: Trigonometry (pp. 204-205)
    (283, 288, 204), (289, 290, 205),
    # Ch 23: Reading Data (pp. 208-211)
    (291, 292, 208), (293, 294, 209), (295, 296, 210), (297, 298, 211),
    # Ch 24: Probability (pp. 217-221)
    (299, 299, 217), (300, 301, 218), (302, 303, 219), (304, 305, 220), (306, 306, 221),
    # Ch 25: Statistics I (pp. 229-231)
    (307, 309, 229), (310, 311, 230), (312, 314, 231),
    # Ch 26: Statistics II (pp. 242-245)
    (315, 316, 242), (317, 319, 243), (320, 321, 244), (322, 322, 245),
    # Ch 27: Volume (pp. 250-252)
    (323, 326, 250), (327, 329, 251), (330, 330, 252)
]

QUESTION_TO_PDF_PAGE = {}
for _qs, _qe, _p in EXACT_PAGE_PARTITIONS:
    for _q in range(_qs, _qe + 1):
        QUESTION_TO_PDF_PAGE[_q] = _p

# Pedagogical L1 Cleanups: Replace raw calculation notes from Excel with conceptual formulas
CUSTOM_L1_CLEANUPS = {
    19: 'Công thức tính tỷ lệ phần trăm: Tỷ lệ = (Giá trị thành phần / Tổng số) * 100%.',
    28: 'Công thức biến thiên phần trăm liên tiếp: Giá trị mới = Giá trị ban đầu * (1 - r1) * (1 + r2).',
    46: 'Mối liên hệ giữa tỷ số thể tích và tỷ số bán kính khối cầu: Tỷ số bán kính bằng căn bậc ba của tỷ số thể tích.',
    47: 'Diện tích hình học tỷ lệ với bình phương cạnh tương ứng: Area_ratio = (s_new / s_old)^2. Hãy tính tỷ số cạnh s_new / s_old rồi suy ra phần trăm giảm.',
    49: 'Mối quan hệ giữa khoảng cách và độ sáng: Tỷ lệ khoảng cách d bằng căn bậc hai của tỷ lệ độ sáng.',
    78: 'Nhận xét biểu thức đại số: Đề bài đã cho trực tiếp giá trị của (a + b), hãy thay trực tiếp vào lũy thừa bậc ba.',
    79: 'Khai triển hai vế theo hằng đẳng thức bậc hai (n - 4)^2 và (n + 4)^2, sau đó triệt tiêu các hạng tử giống nhau để giải tìm n.',
    80: 'Từ (1/a) * (b/c) = 1, suy ra b/(ac) = 1. Hãy quy đồng hoặc nhân chéo để tìm mối liên hệ giữa b và ac.',
    81: 'Từ phương trình 3x - 8 = -23, hãy tìm giá trị của 3x (hoặc x), sau đó nhân đôi để tìm 6x rồi trừ 7.',
    82: 'Để giải tìm m từ 4/9 = (8/3)m, hãy nhân cả hai vế với phân số nghịch đảo của 8/3.',
    83: 'Giải phương trình bậc nhất 3x + 1 = -8 để tìm x, sau đó tính x + 2 rồi nâng lên lũy thừa bậc 3.',
    84: 'Nhân chéo hai vế của phân thức 4 / (k + 2) = x / 3, sau đó phân phối và biến đổi để cô lập k theo x.',
    85: 'Khai căn hai vế của (x - 3)^2 = 36: lưu ý x - 3 = 6 hoặc x - 3 = -6. Kết hợp điều kiện x < 0 để chọn nghiệm x.',
    87: 'Từ m / (2n) = 2, hãy rút ra tỷ số n/m hoặc biểu diễn m theo n, rồi thay vào biểu thức n / (2m).',
    88: 'Từ x^2 - 12 = 4, suy ra x^2 = 16. Khai căn hai vế và lưu ý điều kiện x < 0 để xác định dấu của nghiệm.',
    89: 'Từ x^2 + 7 = 21, hãy trừ cả hai vế cho 7 để tìm giá trị x^2, rồi cộng 3 vào giá trị vừa tìm được.',
    94: 'Khai triển (2x + n)^2 = 4x^2 + 4nx + n^2 rồi đồng nhất hệ số với 4x^2 + mx + 9. Lưu ý điều kiện n < 0.',
    96: 'Khai triển (2x + a)(3x + b) rồi đồng nhất hệ số tự do ab và hệ số của x: c = 3a + 2b.',
    99: 'Đồng nhất hệ số của x^3 ở cả hai vế sau khi nhân đa thức (x^3 + kx^2 - 3)(x - 2).',
    104: 'Cộng hoặc trừ vế với vế của hai phương trình để tạo ra biểu thức chứa x - y hoặc y - x mà không cần giải riêng x, y.',
    105: 'Quan sát hệ số của hai phương trình: trừ trực tiếp phương trình thứ hai cho phương trình thứ nhất để xuất hiện x + y.',
    106: 'Giải hệ phương trình bằng phương pháp thế hoặc cộng đại số để tìm cặp nghiệm (x, y), sau đó tính tích xy.',
    109: 'So sánh tỷ số các cặp hệ số a1/a2 và b1/b2 trong hệ hai phương trình bậc nhất ax + by = c để xác định xem hai đường thẳng cắt nhau, song song hay trùng nhau.',
    118: 'Chuyển các hạng tử chứa x sang một vế và hằng số sang vế còn lại. Lưu ý: khi chia cả hai vế của bất đẳng thức cho một số âm, phải ĐỔI CHIỀU bất đẳng thức.',
    121: 'Độ lệch tuyệt đối giữa n và m không vượt quá 10 được biểu diễn bằng |n - m| <= 10. Hãy khai triển -d <= n - m <= d để đưa về dạng bất phương trình kép.',
    122: 'Lập bất phương trình M >= N tương ứng: 12P + 100 >= -3P + 970, chuyển vế để tìm chặn dưới của P.',
    123: 'Khai triển 3(n - 2) > -4(n - 9), chuyển các số hạng chứa n sang một vế để tìm giá trị nguyên nhỏ nhất của n.',
    124: 'Quan sát vùng giới hạn theo trục tung y: miền bị chặn giữa hai đường nằm ngang y = -3 và y = 3.',
    125: 'Thời gian đi lại = Quãng đường / Vận tốc. Tổng thời gian đi xe buýt và tàu hỏa không vượt quá 1 giờ.',
    129: 'Lập hệ bất phương trình theo thời gian làm việc (<= 30 giờ) và doanh thu mục tiêu (>= $900).',
    132: 'Diện tích hình chữ nhật xy >= 300; chu vi 2(x + y) >= 70, suy ra điều kiện cho tổng hai kích thước x + y.',
    134: 'Bình phương của tổng hai số là (x + y)^2; tích của hai số là xy.',
    136: 'Thiết lập phương trình: 5 + sqrt(x) = 9, giải tìm sqrt(x) rồi bình phương để tìm x.',
    140: 'Thiết lập phương trình tỷ lệ phần trăm: 75% * 68 = 85% * n, từ đó giải tìm n.',
    142: 'Gọi số bút ban đầu của mỗi bạn là x. Thiết lập phương trình sau khi Alice cho Julie 16 bút: x + 16 = 2(x - 16).',
    144: 'Thiết lập phương trình cân bằng: 20 + x = 44 - x với x là số thẻ Jason chuyển cho Ian.',
    145: 'Thiết lập phương trình từ lời văn đề bài để tìm x, sau đó tính một nửa của x rồi cộng với 8.',
    146: 'Biểu diễn mối quan hệ: Giá cà vạt bằng 3 lần giá áo sơ mi trừ đi k đô la.',
    147: 'Gọi số lượng từng loại phiếu giảm giá theo tỷ lệ x, lập phương trình tổng giá trị bằng $360.',
    148: 'Biểu diễn số tiền của từng người theo một ẩn số chung rồi thiết lập phương trình tổng số tiền bằng $60.',
    162: 'Hệ số góc của phương trình tuyến tính b = 200 - 18h biểu diễn tốc độ thay đổi số bánh mì nướng mỗi giờ.',
    163: 'Tung độ gốc (y-intercept) biểu diễn giá trị của đại lượng ban đầu khi biến số độc lập bằng 0.',
    170: 'Biến đổi phân thức về dạng hàm bậc nhất y = mx + b để xác định hệ số góc biểu diễn tốc độ tải.',
    177: 'Quan sát bảng giá trị: khi x tăng, kiểm tra tốc độ tăng của f(x) để chọn mô hình hàm số thích hợp.',
    179: 'Định nghĩa tính đối xứng của hàm số qua đồ thị để tìm các hoành độ có cùng tung độ f(x) = -2.',
    181: 'Đặc trưng hàm chẵn: hàm số thỏa mãn f(-x) = f(x) với mọi x.',
    183: 'Thay giá trị x đã cho vào biểu thức phân thức f(x) rồi thực hiện các phép tính rút gọn ở tử và mẫu.',
    184: 'Dùng các điểm (0, -2) và (1, 3) để xác định hệ số b và a của parabol f(x) = ax^2 + b.',
    187: 'Quy tắc hàm hợp: tính giá trị g(2) trước, sau đó lấy kết quả thay vào biến x của f(x).',
    188: 'Số nghiệm của phương trình f(x) = c chính là số giao điểm giữa đồ thị f(x) và đường thẳng nằm ngang y = c.',
    189: 'Từ g(x) = 2f(x), hãy tìm giá trị của f(k) tương ứng khi g(k) = 8, sau đó tra bảng để tìm k.',
    190: 'Tính giá trị của f(18) và f(11) bằng cách thay vào f(x) = sqrt(x - 2), sau đó lấy hiệu số để so sánh với các đáp án.',
    192: 'Từ g(a) = 6 và g(x) = sqrt(3x), thiết lập phương trình sqrt(3a) = 6 rồi bình phương hai vế để tìm a.',
    193: 'Khoảng cách giữa hai giao điểm trục hoành bằng trị tuyệt đối của hiệu hai nghiệm: |x1 - x2|.',
    195: 'Phân tích đa thức bậc hai thành nhân tử để giải tìm các nghiệm, sau đó chọn nghiệm thỏa mãn điều kiện a < 1.',
    196: 'Định lý Viète hoặc phân tích nhân tử để tìm hai nghiệm a, b, sau đó tính b^2 với b là nghiệm âm.',
    197: 'Định lý Viète: Tổng hai nghiệm của phương trình ax^2 + bx + c = 0 bằng -b / a.',
    201: 'Hoành độ đỉnh của parabol biểu diễn thời điểm đạt giá trị cực đại: t_vertex = -b / (2a).',
    202: 'Giải phương trình lợi nhuận bằng 0 để tìm điểm hòa vốn bằng cách phân tích đa thức thành nhân tử.',
    203: 'Hệ phương trình có đúng 1 nghiệm khi phương trình hoành độ giao điểm có biệt thức Delta = 0.',
    204: 'Đưa tam thức bậc hai về dạng chính tắc (Vertex form) bằng phương pháp thêm bớt tạo bình phương hoàn chỉnh.',
    208: 'Thực hiện phép chia đa thức hoặc phân tích tử số theo mẫu số (2x + 1) để tìm phần thương Q(x) và phần dư.',
    209: 'Định lý số dư: Khi chia đa thức P(x) cho (2x - 1), số dư R chính bằng giá trị P(1/2).',
    210: 'Định lý số dư: Số dư khi chia đa thức g(x) cho (x + 3) chính là giá trị của g(-3).',
    211: 'Vì (z - 1) là nhân tử của đa thức nên giá trị của đa thức tại z = 1 phải bằng 0.',
    213: 'Thực hiện phép chia đa thức (3x^2 - 8x - 4) cho (3x - 2) để tìm biểu thức thương A(x).',
    214: 'Sử dụng phép chia đa thức hoặc đồng nhất hệ số hai vế của 2x^2 - 4x - 3 = A(x)(x + 1) + B để tìm biểu thức thương A(x).',
    218: 'Đa thức có nghiệm x = 1 và x = -1 nên P(1) = 0 và P(-1) = 0, giải hệ phương trình để tìm hệ số.',
    222: 'Lũy thừa của đơn vị ảo i có tính chu kỳ 4: i^1 = i, i^2 = -1, i^3 = -i, i^4 = 1.',
    223: 'Nhân hai số phức bằng quy tắc phân phối và thay i^2 = -1, sau đó gom phần thực riêng và phần ảo riêng.',
    225: 'Phân phối i vào trong ngoặc và sử dụng đẳng thức i^2 = -1 để viết số phức dưới dạng chuẩn a + bi.',
    229: 'Quy tắc trục căn thức số phức: nhân cả tử và mẫu với liên hợp của mẫu (hoặc nhân với i).',
    238: 'Định nghĩa hàm giá trị tuyệt đối y = |f(x)|: với những phần có f(x) >= 0 thì giữ nguyên giá trị tung độ y = f(x); với những phần có f(x) < 0 thì y = -f(x) (đổi dấu tung độ sang giá trị dương).',
    241: 'Mô hình hóa khoảng dung sai (Tolerance Interval): Giá trị x nằm trong khoảng (a; b) được biểu diễn bằng |x - Midpoint| < Tolerance, với Midpoint = (a + b) / 2 và Tolerance = (b - a) / 2.',
    242: 'Xét các trường hợp giá trị của x và y để tìm tích xy có giá trị nhỏ nhất.',
    245: 'Sử dụng tính chất hai góc đồng vị hoặc so le trong bằng nhau khi có các đường thẳng song song.',
    248: 'Định lý góc ngoài của tam giác: Góc ngoài tại một đỉnh bằng tổng hai góc trong không kề với nó.',
    260: 'Trong tam giác vuông 30-60-90, cạnh đối diện góc 30 độ bằng một nửa cạnh huyền.',
    264: 'Bất đẳng thức tam giác và tính chất tam giác cân: xác định cạnh nào là cạnh đáy để chu vi đạt giá trị lớn nhất.',
    266: 'Kẻ đường cao từ đỉnh của tam giác cân xuống đáy để chia đáy thành hai đoạn bằng nhau, dùng Pythagore tính chiều cao.',
    267: 'Tìm độ dài cạnh hình vuông từ diện tích đã cho, rồi kẻ đường cao tam giác đều để tạo hai tam giác vuông 30°-60°-90° và tính diện tích tam giác theo công thức (1/2) * đáy * chiều cao.',
    269: 'Bất đẳng thức tam giác: cạnh lớn nhất z phải nhỏ hơn nửa chu vi của tam giác.',
    273: 'Bất đẳng thức tam giác: độ dài cạnh thứ ba p nằm trong khoảng (hiệu hai cạnh; tổng hai cạnh).',
    274: 'Sử dụng tính chất tam giác đồng dạng để thiết lập tỷ số đồng dạng giữa các cặp cạnh tương ứng.',
    276: 'Diện tích hình tròn tỷ lệ thuận với bình phương bán kính: nếu bán kính tăng k lần thì diện tích tăng k^2 lần.',
    279: 'Số đo góc ở tâm gấp đôi số đo góc nội tiếp cùng chắn một cung; diện tích hình quạt tỷ lệ với số đo góc ở tâm.',
    280: 'Tam giác đều nội tiếp đường tròn chia đường tròn thành 3 cung bằng nhau có số đo mỗi cung là 120 độ.',
    282: 'Góc nội tiếp chắn nửa đường tròn (đường kính AC) là góc vuông (góc B = 90°). Dùng tỉ số lượng giác cos(BAC) = cạnh kề / cạnh huyền trong tam giác vuông ABC để suy ra số đo góc đặc biệt.',
    284: 'Sử dụng hệ thức lượng trong tam giác vuông: cos = cạnh kề / cạnh huyền; định lý Pythagore giữa các cạnh.',
    286: 'Định nghĩa cosin trong tam giác vuông: cos(A) = cạnh kề / cạnh huyền, từ đó suy ra độ dài cạnh cần tìm.',
    287: 'Biểu diễn các hàm lượng giác bằng tam giác vuông: đặt cạnh đối là m, cạnh kề là 1, tính cạnh huyền theo Pythagore rồi lập tỷ số sin = đối / huyền.',
    288: 'Vẽ tam giác vuông minh họa từ tan(B) = đối / kề để tính cạnh huyền, sau đó tính tổng sin + cos.',
    290: 'Định nghĩa sin trong tam giác vuông: sin(A) = đối / cạnh huyền, từ đó thiết lập phương trình tìm cạnh đối BC.',
    294: 'Công thức tỷ lệ phần trăm: lấy lượng mưa của tháng 9 chia cho lượng mưa của tháng 5 rồi nhân với 100%.',
    300: 'Xác suất có điều kiện: Lấy số lượng đối tượng thỏa mãn chia cho tổng số đối tượng trong nhóm được xét.',
    301: 'Xác suất: Lấy số lao động có từ 4 năm kinh nghiệm trở lên chia cho tổng số lao động toàn bộ hai ngành.',
    302: 'Tổng xác suất của toàn bộ các biến cố xung khắc trong không gian mẫu bằng 100%.',
    303: 'Xác suất có điều kiện: lấy số trận đội yếu thắng chia cho tổng số trận các đội yếu đã thi đấu.',
    304: 'Đọc dữ liệu từ bảng: tính tổng số lượng ở hai tuần được yêu cầu rồi chia cho tổng toàn bộ 4 tuần.',
    306: 'Đọc dữ liệu bảng 2 chiều: tính tỷ lệ ở từng quốc gia rồi lấy hiệu số giữa hai tỷ lệ.',
    308: 'Tổng điểm 5 bài thi bằng trung bình nhân 5; tổng điểm 3 bài thi cuối bằng trung bình nhân 3. Hiệu số cho tổng 2 bài đầu.',
    310: 'Công thức số trung bình cộng: Tổng tất cả các giá trị của các điểm dữ liệu chia cho tổng số mẫu (24).',
    314: 'Trung vị của dãy 28 số là trung bình cộng của giá trị thứ 14 và giá trị thứ 15 sau khi sắp xếp theo thứ tự.',
    318: 'Tính tỷ lệ ủng hộ trong mẫu điều tra, sau đó nhân với tổng số cử tri toàn thành phố để ước lượng số phiếu chênh lệch.',
    319: 'Tung độ gốc trên biểu đồ biểu diễn giá trị của biến phụ thuộc khi biến độc lập nhận giá trị 0.',
    322: 'Ước lượng tổng doanh thu bằng cách nhân giá vé dự kiến với lượng khán giả tương ứng từ đồ thị phân tán.',
    323: 'Thể tích của nửa hình trụ bằng một nửa thể tích của hình trụ ban đầu: V = (1/2) * pi * r^2 * h.',
    324: 'Diện tích toàn phần của hình hộp chữ nhật đáy vuông: SA = 2 * (Diện tích đáy) + Chu vi đáy * Chiều cao.',
    327: 'Thể tích hình trụ bao quanh: V = pi * r^2 * h với chiều cao h bằng tổng đường kính của các quả bóng tennis.',
    328: 'Độ dâng của mực nước bằng thể tích của vật thể chìm trong nước chia cho diện tích đáy của bể.',
    329: 'Công thức số khối lập phương con không bị sơn mặt nào: (n - 2)^3 với n là số khối trên mỗi cạnh.',
    330: 'Thể tích của hình gồm một hình nón và một nửa hình cầu: tính riêng thể tích từng phần rồi cộng lại.'
}

# Bespoke Socratic Tier 2 Setups for complex / edge-case questions
CUSTOM_L2_SETUPS = {
    31: 'Dây lưng chiếm phần trăm còn lại sau khi trừ khăn (20%) và cà vạt (60%), suy ra 20% tổng hàng hóa ứng với 40 sản phẩm. Hãy tính tổng số sản phẩm, số lượng mỗi loại ban đầu, rồi cộng thêm một nửa số cà vạt khi chuyển sang khăn.',
    39: 'Mỗi tháng Albert bớt 2 cuốn và thêm 1 cuốn nên tổng số sách giảm đều một lượng không đổi theo từng tháng => Hãy xác định mô hình biến thiên tuyến tính tương ứng (tăng hay giảm).',
    66: 'Tìm ước chung lớn nhất của hai hạng tử 6x^2 y và 6x y^2 (gồm hệ số chung và lũy thừa thấp nhất của x, y) rồi đặt nhân tử chung đó ra ngoài dấu ngoặc.',
    67: 'Chọn mẫu thức chung là 4a: nhân tử và mẫu của phân thức 1/a với 4, phân thức 3/4 với a, sau đó cộng hai tử số để rút gọn.',
    72: 'Tử số: x(y - x) = -x(x - y). Mẫu số: y(x - y). Hãy triệt tiêu thừa số chung (x - y) để tìm phân thức rút gọn.',
    73: 'Trước hết quy đồng và rút gọn biểu thức ở mẫu số: (x - 1)/2 + (x + 5)/3 với mẫu chung là 6, sau đó lấy nghịch đảo của phân thức thu được.',
    74: 'Nhân cả tử thức và mẫu thức của phân thức lớn với x (mẫu thức chung nhỏ nhất của các phân số con) rồi thu gọn hai hạng tử ở tử và mẫu.',
    115: 'Chia hai vế phương trình thứ nhất cho 3 và phương trình thứ hai cho -2 để đưa cả hai về dạng tối giản rồi so sánh xem hai đường thẳng cắt nhau, song song hay trùng nhau.',
    118: 'Chuyển hạng tử: -x - 4 > 4x - 14 => -5x > -10. Chia cả hai vế cho -5 và nhớ ĐỔI CHIỀU bất đẳng thức để tìm miền nghiệm của x, rồi đối chiếu các lựa chọn.',
    125: 'Thời gian đi xe buýt là 8/x và thời gian đi tàu là 16/y. Cụm "at most 1 hour" có nghĩa tổng thời gian nhỏ hơn hoặc bằng 1 giờ — hãy chọn bất đẳng thức phù hợp.',
    127: 'Xác định đường biên thứ nhất y = (3/2)x + 2 (dốc lên, cắt trục tung tại +2) và đường biên thứ hai y = -2x - 5 (dốc xuống, cắt trục tung tại -5). Cặp bất đẳng thức y >= ... (phần phía trên đường 1) và y <= ... (phần phía dưới đường 2) xác định miền tô bóng giao nhau trong 4 đồ thị A, B, C, D trang 89.',
    129: 'Tổng số giờ làm việc là (1/3)m + (1/2)p (tối đa 30 giờ) và tổng thu nhập là 25m + 40p (tối thiểu $900). Hãy chọn đúng cặp chiều bất đẳng thức <= và >= tương ứng.',
    130: (
        'Phân tích bất đẳng thức kép k <= x <= 3k + 12 theo từng mệnh đề:\n'
        '• Xét mệnh đề I: Từ x <= 3k + 12, hãy trừ 12 cả hai vế để so sánh x - 12 với 3k.\n'
        '• Xét mệnh đề II: Từ k <= 3k + 12, chuyển k sang một vế để giải bất phương trình bậc nhất tìm chặn dưới của k.\n'
        '• Xét mệnh đề III: Từ k <= x, hãy chuyển k sang vế trái để suy ra dấu của x - k.\n'
        'Hãy đối chiếu tính đúng đắn của từng mệnh đề I, II, III để xác định kết luận chung.'
    ),
    131: 'Trừ 4 ở cả ba vế của -20/3 < -2x + 4 < -9/2, rồi chia cho -2 và ĐỔI CHIỀU bất đẳng thức để tìm khoảng của x. Từ đó suy ra khoảng giá trị của (x - 2) để chọn đáp án nằm trong khoảng này.',
    134: 'Biểu diễn riêng hai cụm đại số: "square of the sum of x and y" (bình phương của tổng hai số) và "product of x and y" (tích hai số), rồi thực hiện phép trừ ("decreased by").',
    138: 'Tính tổng chi phí cố định và tiền lương nhân viên trong 1 tháng, sau đó nhân toàn bộ biểu thức chi phí hàng tháng với 12 tháng để thu được công thức tổng chi phí cả năm c.',
    170: 'Biến đổi phân thức về dạng hàm bậc nhất: t = (2/5)x + 9/5. Đại lượng đi kèm với biến số x chính là tốc độ tải mỗi ảnh.',
    190: 'Thay lần lượt x = 18 và x = 11 vào f(x) = sqrt(x - 2) để tính hiệu f(18) - f(11), sau đó thay các giá trị trong đáp án vào f(x) để kiểm tra biểu thức nào cho cùng kết quả.',
    191: 'Một điểm (x, y) KHÔNG thuộc đồ thị hàm phân thức khi hoành độ x làm mẫu số bằng 0 (khiến hàm số không xác định) hoặc cặp tọa độ (x, y) không thỏa mãn phương trình.',
    202: 'Giải bất phương trình P = m^2 - 100m - 120,000 >= 0 bằng cách phân tích tam thức bậc hai thành tích hai nhị thức bậc nhất, rồi chọn nghiệm dương phù hợp với điều kiện số sản phẩm m > 0.',
    208: 'Tách tử số 6x^2 + 5x + 2 theo bội của (2x + 1) hoặc thực hiện phép chia đa thức (6x^2 + 5x + 2) cho (2x + 1) để xác định phần thương nguyên Q.',
    213: 'Thực hiện phép chia đa thức 3x^2 - 8x - 4 cho (3x - 2) bằng cách đặt tính chia hoặc biến đổi tử số thành bội của (3x - 2) cộng phần dư -8, phần thương chính là biểu thức A.',
    214: 'Thực hiện phép chia đa thức 2x^2 - 4x - 3 cho (x + 1) để xác định phần thương bậc nhất A(x) sao cho số dư B là một hằng số.',
    215: 'Theo Định lý nhân tử (Factor Theorem): nếu p(c) = 0 thì đa thức p(x) chắc chắn chia hết cho (x - c), tức là (x - c) là một nhân tử của p(x). Áp dụng với nghiệm được cho.',
    219: 'Xác định nghiệm hữu tỉ x = p/q làm đa thức triệt tiêu từ dữ kiện bài toán; khi đó nhị thức (qx - p) tương ứng sẽ là một nhân tử của đa thức.',
    233: 'Nhớ rằng |u| >= 0 với mọi số thực u. Hãy thay từng biểu thức lần lượt bằng -5 rồi chuyển vế để kiểm tra phương trình nào cho |...| bằng một số âm (vô nghiệm) hay số không âm.',
    235: 'Từ |x - 3| > 10, tách thành hai trường hợp: x - 3 > 10 hoặc x - 3 < -10. Giải hai bất phương trình để tìm hai khoảng nghiệm của x rồi kiểm tra các đáp án.',
    238: 'Quan sát đồ thị gốc f(x) ở trang 160 trong PDF: với các điểm có tung độ y < 0 (nằm dưới trục hoành Ox), phép lấy trị tuyệt đối y = |f(x)| sẽ lật đối xứng qua trục Ox lên phía trên; các phần ở trên trục Ox giữ nguyên.',
    240: 'Tính điểm chính giữa (trung điểm) của hai đầu mút 6 1/4 và 6 3/4, đồng thời tính khoảng sai số tối đa từ trung điểm đến mỗi đầu mút để lập dạng |h - Trung điểm| < Sai số.',
    241: (
        'Bài toán khoảng dung sai (Tolerance Interval):\n'
        '• Tìm giá trị trung tâm (Midpoint) của khoảng [400; 410]: Midpoint = (400 + 410) / 2.\n'
        '• Tìm độ lệch tối đa (Tolerance) từ điểm trung tâm đến hai đầu mút: Tolerance = (410 - 400) / 2.\n'
        '• Công thức khoảng giá trị tuyệt đối chuẩn: |x - Midpoint| < Tolerance. Hãy thay số để đối chiếu dạng biểu thức.'
    ),
    243: 'Từ |a| < 1 suy ra -1 < a < 1. Hãy kiểm tra lần lượt ba mệnh đề I, II, III bằng cách thử các giá trị tiêu biểu thuộc khoảng (-1; 1), đặc biệt thử một phân số âm (ví dụ a = -0.5) để loại mệnh đề sai.',
    267: 'Từ diện tích hình vuông bằng 4 suy ra cạnh tam giác đều s = 2. Kẻ đường cao chia tam giác đều thành hai tam giác vuông 30°-60°-90° để tìm chiều cao theo căn bậc hai rồi tính diện tích (1/2) * đáy * cao.',
    291: 'Với mỗi ngày A, B, C, D, hãy cộng hai khoảng thời gian đi và về (commute to + commute from) hoặc đọc tổng chiều dài trên biểu đồ để tìm ngày có tổng thời gian lớn nhất.',
    297: 'Quan sát điểm dữ liệu nằm thấp nhất theo trục tung (số giờ ngủ ít nhất) trên biểu đồ phân tán ở trang 211 trong PDF, rồi gióng thẳng xuống trục hoành để đọc độ tuổi tương ứng.',
    309: 'Với 20 người biên tập được sắp xếp theo thứ tự, trung vị là trung bình cộng của giá trị thứ 10 và thứ 11. Vì cả hai phần tử này đều rơi vào nhóm 10–15 cuốn sách nên giá trị trung vị phải nằm trong khoảng đó.'
}

def clean_topic_str(topic):
    """Strip any formula, equation, or answer value from topic name."""
    if not topic:
        return ""
    t = str(topic).strip()
    t = re.sub(r'\s*[=<>≤≥\|].*$', '', t)
    t = re.sub(r'\s*\b\d+%\b', '', t)
    return t.strip()

def parse_options(options_raw):
    if not options_raw:
        return []
    lines = str(options_raw).strip().split('\n')
    parsed = []
    current_key = None
    current_val = []

    for line in lines:
        line_s = line.strip()
        match = re.match(r'^([A-D])[\.\:\)]\s*(.*)$', line_s)
        if match:
            if current_key:
                parsed.append({"key": current_key, "text": " ".join(current_val).strip()})
            current_key = match.group(1)
            current_val = [match.group(2)]
        else:
            if current_key:
                current_val.append(line_s)
            elif line_s:
                current_val.append(line_s)
    if current_key:
        parsed.append({"key": current_key, "text": " ".join(current_val).strip()})

    if not parsed:
        for opt in ['A', 'B', 'C', 'D']:
            pattern = rf'{opt}[\.\:\)]\s*([^\n]+)'
            m = re.search(pattern, str(options_raw))
            if m:
                parsed.append({"key": opt, "text": m.group(1).strip()})
    return parsed

def sanitize_l1(q_id, raw_l1, correct_ans, opt_text):
    """Generate 100% leak-free conceptual formula & tip for Tier 1."""
    if q_id in CUSTOM_L1_CLEANUPS:
        return CUSTOM_L1_CLEANUPS[q_id]
    
    text = str(raw_l1 or '').strip()
    text = re.sub(r'\s*~\s*.*$', '', text)
    text = re.sub(rf'\b[đĐ]áp án[:\s]+{correct_ans}\b', '', text)
    text = re.sub(rf'\b[cC]họn\s+{correct_ans}\b', '', text)
    text = re.sub(rf'\b[pP]hương án\s+{correct_ans}\b', '', text)
    text = re.sub(rf'=>\s*{correct_ans}\b', '', text)
    text = re.sub(rf'=\s*{correct_ans}\b', '', text)
    if opt_text and len(opt_text.strip()) >= 2:
        esc = re.escape(opt_text.strip())
        text = re.sub(rf'\s*=\s*{esc}\b', '= ...', text, flags=re.I)
        text = re.sub(rf'\s*=>\s*{esc}\b', '=> ...', text, flags=re.I)
    return text.strip()

def sanitize_l2(q_id, raw_l2, correct_ans, opt_text):
    """Generate 100% leak-free intermediate setup & Socratic clue for Tier 2."""
    if q_id in CUSTOM_L2_SETUPS:
        return CUSTOM_L2_SETUPS[q_id]
        
    if not raw_l2:
        return (
            "Chiến thuật giải:\n"
            "• Thiết lập phương trình biểu diễn các đại lượng trong đề bài.\n"
            "• Biến đổi đại số hoặc thay thế giá trị trung gian để cô lập đại lượng cần tìm."
        )

    text = raw_l2.strip().rstrip('.')

    # Strip tildes (approximate results e.g. ~ 37% or ~ 0.433)
    text = re.sub(r'\s*~\s*.*$', '', text)

    # Strip final '= opt_text' or '=> opt_text'
    if opt_text and len(opt_text.strip()) > 0:
        clean_opt = opt_text.strip()
        esc = re.escape(clean_opt)
        text = re.sub(rf'\s*(?:=>|=|là)\s*{esc}\b.*$', '', text, flags=re.I)
        text = re.sub(rf'\s*=\s*{esc}(?:\s+[a-zA-Z]+)?\s*$', '', text, flags=re.I)

    # Strip final '= [number]' or '=> [var] = [number]' (never strip inside <=, >=, !=, or <=>)
    text = re.sub(r'\s*(?<![<>])=>\s*[a-zA-Z]\s*(?<![<>!])=\s*[\-0-9\/\.,]+\s*$', '', text)
    text = re.sub(r'\s*(?<![<>])=>\s*[\-0-9\/\.,]+\s*$', '', text)
    text = re.sub(r'\s*(?<![<>!])=\s*[\-0-9\/\.,]+\s*(?:số|hộp|lít|gam|km|đô la|tuần|mét|đơn vị|giây|phút|giờ|độ)?\s*$', '', text)

    # If steps are joined by => (never split inside <=>), drop final evaluation step
    parts = [p.strip() for p in re.split(r'(?<![<>])=>', text) if p.strip()]
    if len(parts) >= 2:
        last = parts[-1]
        if re.search(r'(?<![<>!])=\s*[\-0-9\/\.,]+', last) or len(last.split()) <= 4:
            text = ' => '.join(parts[:-1])

    # Remove answer letter leaks
    text = re.sub(rf'\b[đĐ]áp án[:\s]+{correct_ans}\b', '', text)
    text = re.sub(rf'\b[cC]họn\s+{correct_ans}\b', '', text)
    text = re.sub(rf'\b[pP]hương án\s+{correct_ans}\b', '', text)
    text = re.sub(rf'=>\s*{correct_ans}\b', '', text)
    text = re.sub(rf'=\s*{correct_ans}\b', '', text)

    # If opt_text appears as '= opt_text', replace with '= ...'
    if opt_text and len(opt_text.strip()) >= 2:
        esc = re.escape(opt_text.strip())
        text = re.sub(rf'=\s*{esc}\b', '= ...', text, flags=re.I)
        text = re.sub(rf'=>\s*{esc}\b', '=> ...', text, flags=re.I)

    text = text.strip()
    if not text.endswith('.'):
        text += '.'
    text += "\n• Hãy tiếp tục thực hiện phép tính / biến đổi đại số còn lại để suy ra kết quả cuối cùng."
    return text

def build_socratic_hints(q_id, ch_num, topic_raw, question_text, calc_mode, correct_ans, opt_text, raw_l1, raw_l2, core_strat, traps):
    """
    Generate 4-tier pedagogical Socratic hints adhering strictly to the No-Leak Policy.
    Tier 1 & Tier 2 MUST NOT reveal the correct option letter (A/B/C/D) or the final target answer.
    """
    ch_info = CHAPTER_MAPPING.get(ch_num, {})
    ch_name = ch_info.get("name", f"Chương {ch_num}")
    vn_sub = ch_info.get("vn_sub", "")

    clean_topic = clean_topic_str(topic_raw)
    l1_formula = sanitize_l1(q_id, raw_l1, correct_ans, opt_text)
    l2_clue = sanitize_l2(q_id, raw_l2, correct_ans, opt_text)

    # Tier 1: Context & Core Formula Direction
    mode_text = "Không dùng máy tính (No Calculator)" if "No Calculator" in calc_mode else "Được dùng máy tính (Calculator Allowed - hỗ trợ Desmos)"
    tier1 = (
        f"Xác định dạng toán: **{clean_topic}** trong chuyên đề **Chương {ch_num}: {ch_name} ({vn_sub})**.\n"
        f"• Chế độ làm bài: {mode_text}.\n"
        f"• Đọc kỹ đề bài để nắm đại lượng đã cho và đại lượng cần tìm.\n"
        f"• Quy tắc / Công thức then chốt: {l1_formula if l1_formula else 'Áp dụng các định lý và tính chất đại số / hình học cơ bản của chương.'}"
    )

    # Tier 2: Intermediate Algebraic / Geometric Clue (0-Leak)
    tier2 = (
        f"Manh mối bước giải trung gian:\n"
        f"• {l2_clue}"
    )

    # Tier 3: Complete Step-by-Step Solution & Walkthrough (The College Panda)
    sol_body = raw_l2
    if q_id == 130:
        sol_body = (
            "Phân tích bất đẳng thức kép k <= x <= 3k + 12:\n"
            "1. Xét I: x <= 3k + 12 => x - 12 <= 3k. (I luôn đúng).\n"
            "2. Xét II: Vì k <= x <= 3k + 12 nên k <= 3k + 12 => -12 <= 2k => k >= -6. (II luôn đúng).\n"
            "3. Xét III: Từ k <= x => x - k >= 0. (III luôn đúng).\n"
            "Do đó cả 3 mệnh đề I, II và III đều bắt buộc phải đúng."
        )
    elif q_id == 241:
        sol_body = (
            "Dạng toán mô hình hóa khoảng giá trị bằng bất phương trình giá trị tuyệt đối:\n"
            "• Điểm chính giữa (Midpoint): (400 + 410) / 2 = 405.\n"
            "• Khoảng cách tối đa cho phép (Bán kính khoảng): (410 - 400) / 2 = 5.\n"
            "• Bất phương trình tương ứng là |l - 405| < 5 (tương đương -5 < l - 405 < 5 <=> 400 < l < 410)."
        )

    tier3 = (
        f"**Đáp án chính xác là [{correct_ans}]**"
        + (f" ({opt_text})\n\n" if opt_text else "\n\n")
        + f"**Lời giải chi tiết từng bước (The College Panda):**\n"
        f"{sol_body}\n\n"
        f"• **Kết luận:** Phương án **[{correct_ans}]** hoàn toàn chuẩn xác theo phương pháp giải của Nielson Phu."
    )

    # Tier 4: Core Theory, Traps, and Pro-Tips from College Panda
    strat_snippet = core_strat or f"Nắm vững các tính chất toán học của {ch_name}."
    traps_snippet = traps or "Cẩn thận kiểm tra điều kiện nghiệm và các phép biến đổi dấu."

    tier4 = (
        f"**🎯 Chiến thuật cốt lõi & Công thức then chốt (The College Panda - Chương {ch_num}):**\n"
        f"{strat_snippet}\n\n"
        f"**⚠️ Bẫy SAT thường gặp cần tránh:**\n"
        f"{traps_snippet}"
    )

    return tier1.strip(), tier2.strip(), tier3.strip(), tier4.strip()

def generate_mermaid(q_id, ch_num, topic, correct_ans):
    ch_info = CHAPTER_MAPPING.get(ch_num, {})
    ch_name = ch_info.get("name", f"Chương {ch_num}")

    clean_topic = re.sub(r'[^a-zA-Z0-9\s]', '', topic)[:30]
    clean_ch = re.sub(r'[^a-zA-Z0-9\s]', '', ch_name)[:25]

    return f"""flowchart TD
    A["Câu hỏi {q_id}: Ch.{ch_num} {clean_ch}"] --> B["Dạng bài: {clean_topic}"]
    B --> C{{"Công thức & Chiến thuật then chốt"}}
    C --> D["Biến đổi đại số & Giải bước trung gian"]
    D --> E["Đáp án chính xác: {correct_ans}"]"""

def main():
    print(f"Loading PandaApp database: {PANDA_APP_DB}")
    with open(PANDA_APP_DB, "r", encoding="utf-8") as f:
        panda_raw = json.load(f)

    print(f"Loading Excel workbook: {EXCEL_PATH}")
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=False)

    # 1. Parse Overview_Strategies
    strategies = {}
    if 'Overview_Strategies' in wb.sheetnames:
        ws_strat = wb['Overview_Strategies']
        for r in range(4, ws_strat.max_row + 1):
            ch_label = ws_strat.cell(r, 1).value
            topic_full = ws_strat.cell(r, 2).value
            domain = ws_strat.cell(r, 3).value
            core_theory = ws_strat.cell(r, 4).value
            traps = ws_strat.cell(r, 5).value

            if ch_label:
                m = re.search(r'\d+', str(ch_label))
                if m:
                    ch_num = int(m.group(0))
                    strategies[ch_num] = {
                        "core_theory": str(core_theory or "").strip(),
                        "traps": str(traps or "").strip(),
                        "domain": str(domain or "").strip(),
                        "topic_title": str(topic_full or "").strip()
                    }

    # 2. Parse Master_All_330_Questions
    ws_master = wb['Master_All_330_Questions']
    raw_qs = []

    for r in range(5, 335):
        qid = ws_master.cell(r, 1).value
        chapter_str = ws_master.cell(r, 2).value
        topic_str = ws_master.cell(r, 3).value
        question_text = ws_master.cell(r, 4).value
        calc_mode = ws_master.cell(r, 5).value
        options_raw = ws_master.cell(r, 6).value
        formula_l1 = ws_master.cell(r, 8).value
        hint_formula = ws_master.cell(r, 16).value
        tip_text = ws_master.cell(r, 17).value

        if not qid:
            continue

        ch_num = 1
        m_ch = re.search(r'Ch(\d+)', str(chapter_str))
        if m_ch:
            ch_num = int(m_ch.group(1))

        ans_match = re.search(r'\"([A-D0-9\/\.\-]+)\"', str(formula_l1))
        correct_ans = ans_match.group(1) if ans_match else ''

        hint_match = re.findall(r'\"([^\"]+)\"', str(hint_formula))
        clean_hints = [h for h in hint_match if not any(x in h for x in ['Nhập A/B/C/D', 'Hoàn hảo!', 'Đúng', 'Sai', '💡 Gợi ý: '])]
        hint_clean = ' '.join(clean_hints).strip() if clean_hints else ''

        raw_qs.append({
            "id": int(qid),
            "chapter_num": ch_num,
            "chapter_str": str(chapter_str or "").strip(),
            "topic": str(topic_str or "").strip(),
            "question": str(question_text or "").strip(),
            "calc_mode": str(calc_mode or "No Calculator").strip(),
            "options_raw": str(options_raw or "").strip(),
            "correct_ans": correct_ans,
            "hint_clean": hint_clean,
            "tip_text": str(tip_text or "").strip()
        })

    print(f"Loaded {len(raw_qs)} questions from Excel Master sheet.")

    # 3. Assemble Questions and Chapter Modules
    processed_questions = []
    chapter_counters = {ch: 0 for ch in range(1, 28)}

    # Leak Audit Tracker
    leak_failures = []

    for item in raw_qs:
        qid = item["id"]
        cnum = item["chapter_num"]
        chapter_counters[cnum] += 1
        q_idx_in_ch = chapter_counters[cnum]

        c_info = CHAPTER_MAPPING.get(cnum, {
            "name": f"Chapter {cnum}", "vn_sub": "", "book_page": 1, "pdf_page": 1, "ex_start": 15, "domain": "Math"
        })
        strat = strategies.get(cnum, {})

        options = parse_options(item["options_raw"])
        corr_ans = item["correct_ans"]

        # Get correct option text
        opt_text = ""
        for opt in options:
            if opt["key"] == corr_ans:
                opt_text = opt["text"].strip()
                break

        # Generate strictly sanitized Socratic hints
        t1, t2, t3, t4 = build_socratic_hints(
            qid, cnum, item["topic"], item["question"], item["calc_mode"],
            corr_ans, opt_text, item["tip_text"], item["hint_clean"],
            strat.get("core_theory", ""), strat.get("traps", "")
        )

        # Audit Tier 1 and Tier 2 for leaks, truncations, and spoiler options
        prompt_lower = item["question"].lower()
        t2_body = "\n".join(
            l for l in t2.split("\n")
            if not l.startswith("Manh mối bước giải") and not l.startswith("• Hãy tiếp tục")
        ).strip()
        t1_formula = t1.split("Quy tắc / Công thức then chốt:", 1)[-1].strip() if "Quy tắc / Công thức then chốt:" in t1 else t1

        for tier_name, check_text in [("Tier 1", t1_formula), ("Tier 2", t2_body)]:
            # 1. Letter leaks
            letter_patterns = [
                rf"\b[đĐ]áp án\s*(?:là|chính xác)?\s*\[?{corr_ans}\]?",
                rf"\b[cC]họn\s*\[?{corr_ans}\]?",
                rf"\b[pP]hương án\s*\[?{corr_ans}\]?",
                rf"\b[vV]ậy\s+{corr_ans}\s*\.?$",
                rf"\b{corr_ans}\s+(?:lớn nhất|nhỏ nhất)\b",
                rf"(?<![<>!])=\s*\[?{corr_ans}\]?(?:\s|$|\.)",
                rf"(?<![<>])=>\s*\[?{corr_ans}\]?(?:\s|$|\.)"
            ]
            for pat in letter_patterns:
                if re.search(pat, check_text):
                    leak_failures.append((qid, tier_name, f"Letter leak '{corr_ans}': {pat}"))

            # 2. Option text / calculated result leaks (when not quoted verbatim from the prompt)
            if opt_text and len(opt_text) >= 2 and opt_text not in {'x', 'y', 'a', 'b', 'c', 'd', '1', '0', '-1', '2'}:
                if opt_text.lower() not in prompt_lower:
                    esc_opt = re.escape(opt_text)
                    if re.search(rf"(?<![A-Za-z0-9%]){esc_opt}(?![A-Za-z0-9%])", check_text, re.I):
                        leak_failures.append((qid, tier_name, f"Exact option leak '{opt_text}'"))
                    elif any(c in opt_text for c in ['%', '^', '/', '+', '=', '<', '>']) and opt_text in check_text:
                        leak_failures.append((qid, tier_name, f"Expr option leak '{opt_text}'"))

            # 3. Truncated hint operators at end of hint
            if tier_name == "Tier 2" and re.search(r'(?:<=|>=|<|>|=|:|,)\s*\.$', check_text):
                leak_failures.append((qid, tier_name, f"Truncated Tier 2 ending: {check_text!r}"))

        # 4. Visual / Asymmetric Spoiler Option check
        if len(options) == 4 and opt_text:
            other_lens = [len(o["text"].strip()) for o in options if o["key"] != corr_ans]
            avg_other = sum(other_lens) / 3.0 if other_lens else 0
            if any(w in prompt_lower for w in ["which graph", "scatterplot"]) and avg_other > 0 and len(opt_text) >= 2.0 * avg_other:
                leak_failures.append((qid, "Options", f"Visual option spoiler '{opt_text}'"))

        mermaid_code = generate_mermaid(qid, cnum, clean_topic_str(item["topic"]), corr_ans)
        code_name = f"Ch{cnum}_{c_info['name'].replace(' ', '_').replace('&', 'and').replace('.', '').replace('-', '_')}"

        # Assign exact question PDF page from verified partitions
        exact_pdf_page = QUESTION_TO_PDF_PAGE.get(qid, c_info["ex_start"])
        printed_book_page = max(1, exact_pdf_page - 2)

        processed_questions.append({
            "id": qid,
            "master_id": f"Panda_Math_Q{qid}",
            "q_number": qid,
            "q_label": f"Ch.{cnum} - Câu {q_idx_in_ch}",
            "category": "practice",
            "category_label": "Luyện tập SAT Math",
            "module_code": code_name,
            "module_title": f"Chương {cnum}: {c_info['name']} ({c_info['vn_sub']})",
            "section": "Math",
            "chapter": f"Chương {cnum}: {c_info['name']}",
            "chapter_num": cnum,
            "topic": clean_topic_str(item["topic"]),
            "passage": "",
            "prompt": item["question"],
            "options": options,
            "options_raw": item["options_raw"],
            "is_grid_in": False,
            "correct_answer": corr_ans,
            "acceptable_answers": [corr_ans],
            "calc_mode": item["calc_mode"],
            "is_calculator": "Calculator Allowed" in item["calc_mode"],
            "tier1_hint": t1,
            "tier2_hint": t2,
            "tier3_hint": t3,
            "strategic_tip": t4,
            "mermaid_diagram": mermaid_code,
            "pdf_page": exact_pdf_page,
            "book_page": printed_book_page,
            "difficulty": "Advanced" if cnum in [15, 16, 21, 22, 27] else ("Hard" if cnum in [8, 9, 10, 14, 20, 25, 26] else "Medium"),
            "domain": c_info["domain"]
        })

    print("\n--- NO-LEAK AUDIT RESULTS ---")
    if leak_failures:
        print(f"❌ AUDIT FAILED: {len(leak_failures)} leaks found!")
        for fail in leak_failures[:15]:
            print(f"  Q{fail[0]} in {fail[1]}: {fail[2]}")
        raise ValueError(f"No-leak audit failed with {len(leak_failures)} leaks!")
    else:
        print("✅ NO-LEAK AUDIT PASSED: 0 leaks found across all 330 questions in Tier 1 and Tier 2!")

    # 4. Build Modules list
    modules_list = []
    for cnum in range(1, 28):
        c_info = CHAPTER_MAPPING.get(cnum, {})
        strat = strategies.get(cnum, {})
        code_name = f"Ch{cnum}_{c_info['name'].replace(' ', '_').replace('&', 'and').replace('.', '').replace('-', '_')}"
        mod_qs = [q for q in processed_questions if q["chapter_num"] == cnum]

        ex_start_page = c_info.get("ex_start", c_info["pdf_page"])

        modules_list.append({
            "id": f"panda_ch{cnum}",
            "code": code_name,
            "chapter_num": cnum,
            "title": f"Chương {cnum}: {c_info['name']} ({c_info['vn_sub']})",
            "short_title": f"Chương {cnum}: {c_info['name']}",
            "sub_title": c_info["vn_sub"],
            "domain": c_info["domain"],
            "section": "Math",
            "time_minutes": max(10, round(len(mod_qs) * 1.5)),
            "question_count": len(mod_qs),
            "pdf_start_page": ex_start_page,
            "book_page": max(1, ex_start_page - 2),
            "strategy": strat.get("core_theory", "Các công thức và định lý cốt lõi của The College Panda."),
            "traps": strat.get("traps", "Cẩn thận kiểm tra bẫy thử nghiệm và phép toán biến đổi dấu."),
            "question_ids": [q["id"] for q in mod_qs]
        })

    # 5. Full Database Object
    final_db = {
        "test_title": "The College Panda: SAT Math Advanced Guide & Workbook (Nielson Phu)",
        "source_attribution": "The College Panda - SAT Math (Nielson Phu)",
        "credits": "Biên soạn và cấu trúc hóa bởi SAT Master Coach Vinschool theo phương pháp Socratic 4 tầng.",
        "pdf_drive_id": PDF_DRIVE_ID,
        "pdf_path": PDF_PATH,
        "pdf_drive_preview": PDF_PREVIEW_URL,
        "pdf_drive_view": PDF_VIEW_URL,
        "total_questions": len(processed_questions),
        "total_chapters": len(modules_list),
        "time_minutes": 360,
        "modules_count": len(modules_list),
        "structure_mode": "chapter_by_chapter",
        "modules": modules_list,
        "questions": processed_questions
    }

    # Save to data/panda_math.json
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(final_db, f, ensure_ascii=False, indent=2)
    print(f"✅ Successfully exported {len(processed_questions)} questions to {OUTPUT_JSON} ({os.path.getsize(OUTPUT_JSON)} bytes)")

    # Mirror copies
    mirrors = [
        os.path.join(BASE_DIR, "data", "pandamath.json"),
        os.path.join(BASE_DIR, "static", "data", "panda_math.json"),
        os.path.join(BASE_DIR, "static", "data", "pandamath.json")
    ]
    for mirror in mirrors:
        os.makedirs(os.path.dirname(mirror), exist_ok=True)
        with open(mirror, "w", encoding="utf-8") as f:
            json.dump(final_db, f, ensure_ascii=False, indent=2)
        print(f"✅ Mirrored to {mirror}")

if __name__ == "__main__":
    main()
