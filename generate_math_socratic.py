# -*- coding: utf-8 -*-
"""
generate_math_socratic.py
Deep, mathematically rigorous 4-tier Socratic explanations, POOE breakdowns,
step-by-step arithmetic/algebraic proofs, Desmos shortcuts, and Mermaid mindmaps
for Math Module 1 (Q1-Q22) and Math Module 2 (Q1-Q22).
"""

MATH_SOLUTIONS = {
    # =========================================================================
    # MATH MODULE 1 (Q1 - Q22)
    # =========================================================================
    55: { # M1 Q1 (Grid-in)
        "tier1_hint": "Nhận diện tính chất tam giác cân: Hai cạnh bên có độ dài bằng nhau. Chu vi là tổng độ dài của cả 3 cạnh. Đề bài đã cho độ dài của hai cạnh bằng nhau và chu vi tổng là bao nhiêu?",
        "tier2_hint": "Thiết lập phương trình chu vi: P = a + b + c. Vì tam giác cân có hai cạnh bằng 24 inches, ta có phương trình: 24 + 24 + c = 73. Hãy tính tổng hai cạnh đã biết rồi lấy chu vi trừ đi.",
        "tier3_hint": "Bước 1: Tính tổng độ dài hai cạnh bên bằng nhau: 24 + 24 = 48 inches.\nBước 2: Tìm độ dài cạnh thứ ba: c = 73 - 48 = 25 inches.\nChốt đáp án chính xác: [25].",
        "strategic_tip": "Mẹo kiểm tra nhanh: 24 + 24 = 48 > 25 (thỏa mãn bất đẳng thức tam giác: tổng hai cạnh luôn lớn hơn cạnh còn lại). Luôn đọc kỹ xem đề bài hỏi cạnh bên hay cạnh đáy!",
        "grid_in_explanation": {
            "correct_answer": "25",
            "solution_steps": "1. Thiết lập biểu thức chu vi tam giác cân: P = 24 + 24 + x = 73.\n2. Thu gọn: 48 + x = 73.\n3. Trừ 48 ở cả hai vế: x = 73 - 48 = 25.",
            "trap_errors": "Bẫy thường gặp: Lấy 73 chia 3 (nhầm sang tam giác đều) hoặc chỉ lấy 73 - 24 (quên mất có 2 cạnh bằng nhau)."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 25 - Thỏa mãn 24 + 24 + 25 = 73 inches và tạo thành tam giác hợp lệ.",
        "mermaid_diagram": 'flowchart TD\n    A["Tam giác cân: Chu vi P = 73 in, hai cạnh bằng nhau = 24 in"] --> B["Công thức chu vi: P = 24 + 24 + c"]\n    B --> C["Tính tổng 2 cạnh bên: 24 + 24 = 48 in"]\n    C --> D["Tìm cạnh thứ ba: c = 73 - 48"]\n    D --> E["Kết quả: c = 25 in"]\n    E --> F["Điền đáp án: 25"]'
    },

    56: { # M1 Q2 (x = 7, y = x^2 + 5)
        "tier1_hint": "Đề bài cho hệ gồm hai phương trình x = 7 và y = x^2 + 5. Tọa độ giao điểm (x, y) thỏa mãn đồng thời cả hai phương trình. Hãy thay giá trị x đã biết vào phương trình thứ hai.",
        "tier2_hint": "Thực hiện phép thế x = 7 vào biểu thức y = x^2 + 5. Cẩn thận tính lũy thừa 7^2 trước khi cộng với 5.",
        "tier3_hint": "Bước 1: Thay x = 7 vào y = x^2 + 5, ta được y = (7)^2 + 5.\nBước 2: Tính 7^2 = 49.\nBước 3: y = 49 + 5 = 54.\nChốt đáp án chính xác: [D].",
        "strategic_tip": "Mẹo Desmos: Nhập dòng 1 'x = 7', dòng 2 'y = x^2 + 5'. Click trực tiếp vào điểm giao nhau trên đồ thị, Desmos sẽ hiển thị ngay tọa độ (7, 54). Giá trị y cần tìm là 54.",
        "option_explanations": {
            "A": "Loại A - (−2): Bẫy nhầm dấu hoặc trừ sai 5 - 7 = -2 thay vì bình phương x.",
            "B": "Loại B - (14): Bẫy nhầm x^2 thành 2x (lấy 2 * 7 = 14) và bỏ quên số hạng +5.",
            "C": "Loại C - (25): Bẫy nhầm lẫn khi thay số hoặc tính nhầm 7^2.",
            "D": "ĐÁP ÁN ĐÚNG. D (54): Thay x = 7 vào phương trình: y = 7^2 + 5 = 49 + 5 = 54."
        },
        "pooe_breakdown": "• Loại A, B, C: Do tính toán sai lũy thừa x^2 hoặc nhầm lẫn phép toán.\n• Chọn D: 7^2 + 5 = 49 + 5 = 54 chuẩn xác.",
        "mermaid_diagram": 'flowchart TD\n    A["Hệ phương trình: x = 7 và y = x^2 + 5"] --> B["Phương pháp thế: Thay x = 7 vào y = x^2 + 5"]\n    B --> C["Tính lũy thừa: 7^2 = 49"]\n    C --> D["Cộng hằng số: 49 + 5 = 54"]\n    D --> E["Chọn đáp án D: 54"]'
    },

    57: { # M1 Q3 (Right triangle, acute angle 31)
        "tier1_hint": "Trong một tam giác vuông, tổng số đo ba góc bằng 180°, trong đó góc vuông bằng 90°. Điều này có ý nghĩa gì đối với tổng số đo của hai góc nhọn còn lại?",
        "tier2_hint": "Hai góc nhọn trong tam giác vuông luôn phụ nhau (tổng bằng 90°). Đã biết một góc là 31°, góc còn lại sẽ bằng 90° - 31°.",
        "tier3_hint": "Bước 1: Áp dụng định lý: Trong tam giác vuông, hai góc nhọn có tổng bằng 90°.\nBước 2: Số đo góc nhọn còn lại là 90° - 31° = 59°.\nChốt đáp án chính xác: [B].",
        "strategic_tip": "Mẹo nhanh SAT: Luôn lấy 90° trừ đi góc nhọn đã cho thay vì lấy 180° - 90° - 31° để tiết kiệm 10 giây và tránh nhầm lẫn số học.",
        "option_explanations": {
            "A": "Loại A - (31): Bẫy nhầm sang tam giác vuông cân (hai góc nhọn bằng nhau).",
            "B": "ĐÁP ÁN ĐÚNG. B (59): Hai góc nhọn phụ nhau: 90° - 31° = 59°.",
            "C": "Loại C - (62): Bẫy nhân đôi góc 31° * 2 = 62°.",
            "D": "Loại D - (149): Bẫy lấy 180° - 31° = 149° (quên trừ đi góc vuông 90°)."
        },
        "pooe_breakdown": "• Loại A, C, D: Sai quy tắc góc nhọn tam giác vuông.\n• Chọn B: 90 - 31 = 59° tuyệt đối chính xác.",
        "mermaid_diagram": 'flowchart TD\n    A["Tam giác vuông có một góc nhọn = 31°"] --> B["Định lý: Tổng hai góc nhọn = 90°"]\n    B --> C["Tính góc nhọn còn lại: 90° - 31°"]\n    C --> D["Kết quả = 59°"]\n    D --> E["Chọn đáp án B: 59"]'
    },

    58: { # M1 Q4 (16x = 13x + 15, find 5x)
        "tier1_hint": "Hãy giải phương trình bậc nhất 16x = 13x + 15 để tìm x trước. Sau đó đọc lại thật kỹ câu hỏi: Đề bài yêu cầu tìm x hay tìm 5x?",
        "tier2_hint": "Bước 1: Chuyển 13x sang vế trái: 16x - 13x = 15 => 3x = 15 => x = 5.\nBước 2: Đề bài hỏi giá trị của 5x, hãy nhân x vừa tìm được với 5.",
        "tier3_hint": "Bước 1: 16x - 13x = 15 => 3x = 15 => x = 5.\nBước 2: Tính giá trị yêu cầu: 5x = 5 * 5 = 25.\nChốt đáp án chính xác: [25].",
        "strategic_tip": "BẪY KINH ĐIỂN CỦA COLLEGE BOARD: Học sinh thường vội vàng điền '5' ngay sau khi giải ra x = 5. Luôn gạch chân đại lượng cần tìm ở cuối câu hỏi (ở đây là '5x')!",
        "grid_in_explanation": {
            "correct_answer": "25",
            "solution_steps": "1. 16x - 13x = 15.\n2. 3x = 15 => x = 5.\n3. Đề bài hỏi giá trị của 5x => 5 * 5 = 25.",
            "trap_errors": "Bẫy điền nhầm x = 5 thay vì tính 5x = 25."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 25 - Giá trị của 5x khi x = 5.",
        "mermaid_diagram": 'flowchart TD\n    A["Phương trình: 16x = 13x + 15"] --> B["Chuyển vế: 16x - 13x = 15 => 3x = 15"]\n    B --> C["Tìm x: x = 15 / 3 = 5"]\n    C --> D{"Cảnh báo bẫy: Đề bài hỏi 5x!"}\n    D --> E["Tính 5x: 5 * 5 = 25"]\n    E --> F["Điền đáp án: 25"]'
    },

    59: { # M1 Q5 (f(t) = 11t + 6, meaning of 6)
        "tier1_hint": "Hàm số f(t) = 11t + 6 biểu diễn chiều dài của cây theo số tháng t kể từ lúc mua. Số 6 là hằng số tự do (y-intercept). Khi t = 0 (thời điểm Malcolm vừa mua cây), f(0) bằng bao nhiêu?",
        "tier2_hint": "Trong mô hình tuyến tính y = mt + b, hệ số góc m = 11 là tốc độ tăng trưởng hàng tháng, còn hệ số tự do b = 6 là giá trị ban đầu tại thời điểm t = 0.",
        "tier3_hint": "Tại thời điểm Malcolm mua cây (t = 0), chiều dài ước tính của cây là f(0) = 11(0) + 6 = 6 inches. Do đó, 6 đại diện cho chiều dài ban đầu của cây khi mới mua.\nChốt đáp án chính xác: [A].",
        "strategic_tip": "Mẹo đọc đồ thị hàm số: Hằng số không gắn với biến số luôn là 'Initial Value' (Giá trị ban đầu lúc t = 0), còn hệ số đi kèm biến số là 'Rate of Change' (Tốc độ thay đổi mỗi đơn vị thời gian).",
        "option_explanations": {
            "A": "ĐÁP ÁN ĐÚNG. A: 6 là chiều dài ước tính ban đầu của cây khi Malcolm mới mua (t = 0).",
            "B": "Loại B: 6 không phải chiều dài tối đa (hàm số tăng liên tục theo thời gian).",
            "C": "Loại C: 6 không phải tốc độ tăng mỗi tháng (tốc độ tăng mỗi tháng là hệ số góc 11).",
            "D": "Loại D: t là số tháng, 6 không phải là tổng số tháng Malcolm giữ cây."
        },
        "pooe_breakdown": "• Loại B: Nhầm lẫn với giá trị cực đại.\n• Loại C: Nhầm lẫn giữa y-intercept (6) và slope (11).\n• Loại D: Nhầm lẫn biến thời gian t với hằng số.\n• Chọn A: Khớp định nghĩa giá trị ban đầu tại t = 0.",
        "mermaid_diagram": 'flowchart TD\n    A["Hàm số: f(t) = 11t + 6"] --> B["Phân tích cấu trúc y = mt + b"]\n    B --> C["m = 11: Tốc độ tăng trưởng mỗi tháng"]\n    B --> D["b = 6: Giá trị ban đầu khi t = 0 (khi mới mua)"]\n    D --> E["Chọn đáp án A"]'
    },

    60: { # M1 Q6 (y = 22^x table)
        "tier1_hint": "Hàm số mũ y = 22^x. Hãy tính giá trị của y ứng với các giá trị x = 0, x = 1, và x = 2.",
        "tier2_hint": "Quy tắc lũy thừa:\n• Khi x = 0: y = 22^0 = 1 (bất kỳ số nào khác 0 mũ 0 đều bằng 1).\n• Khi x = 1: y = 22^1 = 22.\n• Khi x = 2: y = 22^2 = 22 * 22 = 484.",
        "tier3_hint": "Bảng giá trị đúng phải chứa các cặp:\n(0, 1), (1, 22), (2, 484).\nĐối chiếu với 4 phương án, bảng C khớp chính xác hoàn toàn.\nChốt đáp án chính xác: [C].",
        "strategic_tip": "Bẫy số học thường gặp: Học sinh hay nhầm 22^0 = 0 (như bảng A) hoặc nhầm 22^2 = 22 * 2 = 44 (như bảng B và D). Hãy nhớ x là số mũ, không phải phép nhân!",
        "option_explanations": {
            "A": "Loại A: Nhầm 22^0 = 0 (bẫy kinh điển, số mũ 0 luôn cho kết quả 1).",
            "B": "Loại B: Nhầm 22^0 = 22 và 22^2 = 44.",
            "C": "ĐÁP ÁN ĐÚNG. C: 22^0 = 1, 22^1 = 22, 22^2 = 484.",
            "D": "Loại D: Nhầm 22^2 thành 22 * 2 = 44."
        },
        "pooe_breakdown": "• Loại A vì y(0) = 1 khác 0.\n• Loại B vì y(0) = 1 khác 22.\n• Loại D vì y(2) = 484 khác 44.\n• Chọn C: Đúng mọi giá trị.",
        "mermaid_diagram": 'flowchart TD\n    A["Phương trình y = 22^x"] --> B["Thay x = 0: y = 22^0 = 1"]\n    A --> C["Thay x = 1: y = 22^1 = 22"]\n    A --> D["Thay x = 2: y = 22^2 = 484"]\n    B & C & D --> E["Bảng giá trị: (0,1), (1,22), (2,484)"]\n    E --> F["Chọn đáp án C"]'
    },

    61: { # M1 Q7 (Scatterplot slope)
        "tier1_hint": "Đường hồi quy (line of best fit) dốc xuống từ trái qua phải. Điều này cho biết hệ số góc (slope) mang dấu âm hay dương?",
        "tier2_hint": "Vì đường thẳng dốc xuống nên slope phải âm => Loại ngay C (0.8) và D (2.4). Tiếp theo, chọn hai điểm thuận lợi trên đường thẳng để ước lượng độ dốc m = (y2 - y1) / (x2 - x1).",
        "tier3_hint": "Đường thẳng đi qua khoảng các điểm (0, 10) và (10, 2). Độ dốc ước lượng: m ≈ (2 - 10) / (10 - 0) = -8 / 10 = -0.8. Giá trị gần nhất là -0.8.\nChốt đáp án chính xác: [B].",
        "strategic_tip": "Chiến thuật POOE 2 bước: Bước 1 loại ngay các phương án sai dấu (dốc xuống => loại số dương). Bước 2 kiểm tra độ dốc thoai thoải (|m| < 1) hay dốc đứng (|m| > 1) để chọn -0.8 thay vì -2.4.",
        "option_explanations": {
            "A": "Loại A - (−2.4): Quá dốc so với đường thẳng thực tế trên đồ thị.",
            "B": "ĐÁP ÁN ĐÚNG. B (−0.8): Hệ số góc âm và có độ dốc phù hợp với đường thẳng.",
            "C": "Loại C - (0.8): Sai dấu (đường thẳng dốc xuống nên slope phải âm).",
            "D": "Loại D - (2.4): Sai dấu và sai độ lớn."
        },
        "pooe_breakdown": "• Loại C, D: Đồ thị dốc xuống từ trái sang phải nên slope bắt buộc phải âm.\n• Loại A: -2.4 biểu thị đường dốc rất đứng, không khớp với đồ thị thoai thoải.\n• Chọn B: -0.8 chuẩn xác.",
        "mermaid_diagram": 'flowchart TD\n    A["Đồ thị phân tán với đường xu hướng"] --> B{"Hướng của đường thẳng"}\n    B -->|"Dốc xuống từ trái qua phải"| C["Slope mang dấu ÂM => Loại C, D"]\n    C --> D{"Độ nghiêng của đường thẳng"}\n    D -->|"Thoai thoải, giảm khoảng 8 đơn vị y trên 10 đơn vị x"| E["Slope xấp xỉ -0.8"]\n    E --> F["Chọn đáp án B"]'
    },

    62: { # M1 Q8 (Exponential y-intercept (0, 25))
        "tier1_hint": "Giao điểm với trục tung (y-intercept) của đồ thị y = f(x) là điểm có tọa độ (0, 25). Tọa độ này cho biết khi x = 0 thì y bằng bao nhiêu?",
        "tier2_hint": "Theo định nghĩa hàm số y = f(x), điểm (x, y) nằm trên đồ thị có nghĩa là f(x) = y. Với điểm (0, 25), ta có x = 0 và y = 25.",
        "tier3_hint": "Điểm (0, 25) thuộc đồ thị y = f(x) đồng nghĩa với f(0) = 25. Mọi phương án khác đều gán sai giá trị đầu vào x hoặc đầu ra y.\nChốt đáp án chính xác: [D].",
        "strategic_tip": "Khái niệm cốt lõi SAT: Điểm (a, b) thuộc đồ thị hàm số y = f(x) LUÔN TƯƠNG ĐƯƠNG VỚI đẳng thức f(a) = b.",
        "option_explanations": {
            "A": "Loại A - f(0) = 0: Sai, y-intercept là (0, 25) chứ không phải gốc tọa độ (0, 0).",
            "B": "Loại B - f(25) = 0: Nhầm lẫn giữa x-intercept và y-intercept.",
            "C": "Loại C - f(25) = 25: Gán sai biến x thành 25.",
            "D": "ĐÁP ÁN ĐÚNG. D - f(0) = 25: Đúng định nghĩa y-intercept tại x = 0 thì f(0) = 25."
        },
        "pooe_breakdown": "• Điểm (0, 25) => x = 0, y = 25 => f(0) = 25. Chỉ có D thỏa mãn.",
        "mermaid_diagram": 'flowchart TD\n    A["Đồ thị có y-intercept là (0, 25)"] --> B["Định nghĩa: Điểm (x, y) thuộc đồ thị y = f(x)"]\n    B --> C["Thay x = 0, y = 25 vào hàm số"]\n    C --> D["Suy ra: f(0) = 25"]\n    D --> E["Chọn đáp án D"]'
    },

    63: { # M1 Q9 (Shaded inequality 2y < 16x + 22)
        "tier1_hint": "Quan sát đường biên: Đường nét đứt (dashed line) có hệ số góc dương hay âm, và miền nghiệm được tô màu ở phía trên hay phía dưới đường biên?",
        "tier2_hint": "Miền nghiệm được tô màu phía DƯỚI đường biên => Dấu bất đẳng thức ở dạng y < mx + b phải là dấu nhỏ hơn ('<'). Chia 2 ở cả hai vế của 2y < 16x + 22 ta được y < 8x + 11.",
        "tier3_hint": "Bước 1: Đường biên đi qua (0, 11) và có độ dốc dương m = 8 => Phương trình biên: y = 8x + 11.\nBước 2: Miền nghiệm nằm phía dưới đường thẳng => y < 8x + 11.\nBước 3: Nhân cả hai vế với 2 => 2y < 16x + 22.\nChốt đáp án chính xác: [C].",
        "strategic_tip": "Mẹo Desmos: Nhập 4 phương án vào Desmos, quan sát hình dạng miền tô màu và so sánh trực tiếp với hình vẽ đề bài để chọn ngay đáp án đúng trong 15 giây.",
        "option_explanations": {
            "A": "Loại A: Dấu '>' biểu thị miền tô phía TRÊN đường thẳng.",
            "B": "Loại B: Hệ số góc -16x là sai (đường biên dốc lên, slope phải dương).",
            "C": "ĐÁP ÁN ĐÚNG. C: 2y < 16x + 22 tương đương y < 8x + 11 (slope dương = 8, tô phía dưới).",
            "D": "Loại D: Slope âm -16x sai hướng đường thẳng."
        },
        "pooe_breakdown": "• Loại B, D vì đường biên dốc lên (slope dương > 0).\n• Loại A vì miền tô nằm bên dưới đường biên (phải dùng dấu '<').\n• Chọn C chuẩn xác.",
        "mermaid_diagram": 'flowchart TD\n    A["Hình vẽ miền nghiệm bất đẳng thức"] --> B["Đường biên dốc lên => Slope dương (+16x) => Loại B, D"]\n    B --> C["Miền tô phía DƯỚI đường biên => Dấu nhỏ hơn (<) => Loại A"]\n    C --> D["Bất đẳng thức đúng: 2y < 16x + 22"]\n    D --> E["Chọn đáp án C"]'
    },

    64: { # M1 Q10 (Decreasing exponential table)
        "tier1_hint": "Xem xét bảng giá trị: Khi x tăng đều 1 đơn vị (1, 2, 3, 4), giá trị f(x) tăng hay giảm? Tốc độ thay đổi là trừ đi một số cố định hay nhân với một tỷ lệ cố định?",
        "tier2_hint": "Quan sát: 2000 -> 400 -> 80 -> 16. Mỗi bước f(x) đều chia cho 5 (nhân với 1/5 = 0.2). Vì tỷ lệ nhân là hằng số (common ratio < 1) nên đây là hàm số mũ giảm (Decreasing exponential).",
        "tier3_hint": "Hàm tuyến tính thay đổi bằng phép cộng/trừ hằng số (constant difference). Hàm số mũ thay đổi bằng phép nhân/chia tỷ lệ hằng số (constant ratio). Vì 400/2000 = 80/400 = 16/80 = 0.2 < 1, hàm số là Decreasing exponential.\nChốt đáp án chính xác: [A].",
        "strategic_tip": "Phân biệt Tuyến tính vs Số mũ: 'Equal differences over equal intervals' = Linear; 'Equal ratios over equal intervals' = Exponential.",
        "option_explanations": {
            "A": "ĐÁP ÁN ĐÚNG. A: f(x) giảm theo tỷ lệ nhân không đổi (r = 1/5) nên là Decreasing exponential.",
            "B": "Loại B: Giá trị f(x) giảm dần, không phải tăng.",
            "C": "Loại C: Hiệu số giữa các bước không bằng nhau (2000-400=1600 khác 400-80=320), nên không phải hàm tuyến tính.",
            "D": "Loại D: Sai cả tính chất tuyến tính và chiều tăng/giảm."
        },
        "pooe_breakdown": "• Loại B, D vì giá trị giảm từ 2000 xuống 16.\n• Loại C vì độ giảm không cố định (1600 != 320).\n• Chọn A: Tỷ lệ cố định 1/5 => Decreasing exponential.",
        "mermaid_diagram": 'flowchart TD\n    A["Bảng f(x): 2000, 400, 80, 16"] --> B["Kiểm tra chiều biến thiên: Giảm dần => Loại B, D"]\n    B --> C["Kiểm tra tỷ lệ: 400/2000 = 80/400 = 1/5 (Hằng số nhân)"]\n    C --> D["Tỷ lệ nhân cố định => Hàm số mũ (Exponential)"]\n    D --> E["Kết luận: Decreasing exponential => Chọn A"]'
    },

    65: { # M1 Q11 (Margin of error 8.5% +- 2.88%)
        "tier1_hint": "Khoảng tin cậy (Confidence Interval) được tính bằng cách lấy ước lượng mẫu cộng và trừ sai số biên (Margin of Error). Khoảng giá trị hợp lý là gì?",
        "tier2_hint": "Tính cận dưới: 8.5% - 2.88% = 5.62%. Tính cận trên: 8.5% + 2.88% = 11.38%. Khoảng tỷ lệ phần trăm hợp lý cho toàn bộ sản phẩm là từ 5.62% đến 11.38%.",
        "tier3_hint": "Dựa trên ước tính 8.5% và sai số biên 2.88%, tỷ lệ sản phẩm lỗi hợp lý trong toàn bộ quần thể nằm trong khoảng [8.5 - 2.88, 8.5 + 2.88] = [5.62%, 11.38%]. Phương án B kết luận chính xác và khách quan.\nChốt đáp án chính xác: [B].",
        "strategic_tip": "Quy tắc thống kê SAT: Sai số biên KHÔNG khẳng định con số chính xác tuyệt đối (loại A, C) và KHÔNG khẳng định vượt quá cận trên (loại D). Nó chỉ khẳng định giá trị thực 'nhiều khả năng / hợp lý' nằm trong khoảng [Estimate - MoE, Estimate + MoE].",
        "option_explanations": {
            "A": "Loại A: 2.88% là sai số biên, không phải tỷ lệ lỗi ước tính.",
            "B": "ĐÁP ÁN ĐÚNG. B: Khoảng giá trị hợp lý là 8.5% ± 2.88%, tức từ 5.62% đến 11.38%.",
            "C": "Loại C: Khẳng định tuyệt đối 8.5% là sai vì có sai số biên kèm theo.",
            "D": "Loại D: Khẳng định 'lớn hơn 11.38%' đi ngược lại khoảng tin cậy."
        },
        "pooe_breakdown": "• Loại A: Nhầm sai số biên thành tỷ lệ lỗi.\n• Loại C: Quá tuyệt đối, bỏ qua sai số.\n• Loại D: Nằm ngoài khoảng tin cậy.\n• Chọn B: Phản ánh đúng khoảng tin cậy 5.62% - 11.38%.",
        "mermaid_diagram": 'flowchart TD\n    A["Ước lượng: 8.5%, Sai số biên: 2.88%"] --> B["Khoảng tin cậy: [8.5% - 2.88%, 8.5% + 2.88%]"]\n    B --> C["Cận dưới = 5.62%, Cận trên = 11.38%"]\n    C --> D["Kết luận hợp lý: Tỷ lệ lỗi nằm trong khoảng 5.62% đến 11.38%"]\n    D --> E["Chọn đáp án B"]'
    },

    66: { # M1 Q12 (f(x) = x+4, g(x) = 4x, find 5f(2) - g(2))
        "tier1_hint": "Đây là bài toán tính giá trị hàm số hợp. Hãy tính riêng f(2) và g(2), sau đó thay vào biểu thức 5f(2) - g(2).",
        "tier2_hint": "• f(2) = 2 + 4 = 6.\n• g(2) = 4 * 2 = 8.\n• Thay vào biểu thức: 5 * f(2) - g(2) = 5 * 6 - 8.",
        "tier3_hint": "Bước 1: f(2) = 2 + 4 = 6.\nBước 2: g(2) = 4(2) = 8.\nBước 3: 5f(2) - g(2) = 5(6) - 8 = 30 - 8 = 22.\nChốt đáp án chính xác: [D].",
        "strategic_tip": "Mẹo Desmos: Nhập f(x) = x + 4, g(x) = 4x. Ở dòng thứ 3 gõ trực tiếp '5*f(2) - g(2)', Desmos sẽ tính ngay ra kết quả 22 mà không lo nhầm lẫn thứ tự tính toán.",
        "option_explanations": {
            "A": "Loại A - (−2): Tính nhầm f(2) - g(2) mà quên nhân hệ số 5 (6 - 8 = -2).",
            "B": "Loại B - (6): Nhầm lẫn trong các bước trừ số học.",
            "C": "Loại C - (20): Tính nhầm 5 * 4 = 20.",
            "D": "ĐÁP ÁN ĐÚNG. D (22): 5 * f(2) - g(2) = 5 * 6 - 8 = 30 - 8 = 22."
        },
        "pooe_breakdown": "• Loại A do quên nhân 5 vào f(2).\n• Loại B, C do lỗi tính toán.\n• Chọn D: 30 - 8 = 22 chính xác.",
        "mermaid_diagram": 'flowchart TD\n    A["f(x) = x + 4 và g(x) = 4x"] --> B["Tính f(2) = 2 + 4 = 6"]\n    A --> C["Tính g(2) = 4 * 2 = 8"]\n    B & C --> D["Tính biểu thức: 5 * f(2) - g(2)"]\n    D --> E["5 * 6 - 8 = 30 - 8 = 22"]\n    E --> F["Chọn đáp án D: 22"]'
    },

    67: { # M1 Q13 (System: 1/4 x - 24 = 6y and 3/4 x - 13 = -6y)
        "tier1_hint": "Quan sát hệ phương trình: Vế phải của phương trình 1 có 6y và phương trình 2 có -6y. Điều gì sẽ xảy ra nếu ta cộng từng vế của hai phương trình lại với nhau?",
        "tier2_hint": "Áp dụng phương pháp cộng đại số (Elimination): (1/4 x - 24) + (3/4 x - 13) = 6y + (-6y). Hai số hạng chứa y triệt tiêu nhau, chỉ còn lại phương trình bậc nhất theo x.",
        "tier3_hint": "Bước 1: Cộng vế theo vế:\n(1/4 x + 3/4 x) + (-24 - 13) = 6y - 6y\nBước 2: 1x - 37 = 0 => x = 37.\nChốt đáp án chính xác: [37].",
        "strategic_tip": "Mẹo nhận diện cấu trúc đối xứng: Khi thấy +6y và -6y, việc cộng hai phương trình sẽ khử hoàn toàn y trong đúng 5 giây!",
        "grid_in_explanation": {
            "correct_answer": "37",
            "solution_steps": "1. Cộng hai phương trình vế theo vế: (1/4 x + 3/4 x) - 24 - 13 = 6y - 6y.\n2. Thu gọn: x - 37 = 0.\n3. x = 37.",
            "trap_errors": "Bẫy tính toán: Trừ nhầm phân số hoặc quên đổi dấu khi cộng số âm: (-24) + (-13) = -37."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 37 - Tìm được ngay bằng phương pháp khử đại số.",
        "mermaid_diagram": 'flowchart TD\n    A["Hệ: (1/4)x - 24 = 6y và (3/4)x - 13 = -6y"] --> B["Quan sát: +6y và -6y triệt tiêu khi cộng"]\n    B --> C["Cộng vế với vế: [(1/4) + (3/4)]x - 24 - 13 = 0"]\n    C --> D["Thu gọn: 1x - 37 = 0"]\n    D --> E["Nghiệm: x = 37"]\n    E --> F["Điền đáp số: 37"]'
    },

    68: { # M1 Q14 (Salt x grams vs water y liters)
        "tier1_hint": "Bảng cho biết mối quan hệ giữa lượng muối x (gam) và lượng nước y (lít): (259g, 7L), (296g, 8L), (333g, 9L). Hãy tìm tỉ số giữa lượng muối và lượng nước.",
        "tier2_hint": "Tính tỉ số: 259 / 7 = 37; 296 / 8 = 37; 333 / 9 = 37. Điều này có nghĩa là mỗi lít nước có 37 gam muối: x = 37y. Từ đó biến đổi tìm y theo x.",
        "tier3_hint": "Từ x = 37y, chia cả hai vế cho 37 ta được y = (1/37)x.\nChốt đáp án chính xác: [B].",
        "strategic_tip": "Cẩn thận biến độc lập và phụ thuộc: Đề bài yêu cầu biểu diễn y theo x (y = ... x). Tỉ số x/y = 37 => y = x / 37 = (1/37)x. Tránh bẫy chọn nhầm C (y = 37x)!",
        "option_explanations": {
            "A": "Loại A: y = (1/74)x sai tỷ lệ.",
            "B": "ĐÁP ÁN ĐÚNG. B: y = (1/37)x (vì x = 37y => y = x/37).",
            "C": "Loại C: y = 37x là bẫy đảo ngược x và y (đúng phải là x = 37y).",
            "D": "Loại D: y = 74x sai tỷ lệ số học."
        },
        "pooe_breakdown": "• Loại C vì nếu y = 37x thì với x = 259 => y = 37 * 259 = 9583 (vô lý so với y = 7).\n• Loại A, D vì sai tỉ lệ 37.\n• Chọn B chuẩn xác.",
        "mermaid_diagram": 'flowchart TD\n    A["Bảng: (259g, 7L), (296g, 8L), (333g, 9L)"] --> B["Tính tỉ số: x / y = 259 / 7 = 37"]\n    B --> C["Hệ thức: x = 37y"]\n    C --> D["Biểu diễn y theo x: y = (1/37)x"]\n    D --> E["Chọn đáp án B"]'
    },

    69: { # M1 Q15 ((2x-4)(x-3)(x-7) = 0, sum of solutions)
        "tier1_hint": "Tích của các nhân tử bằng 0 khi ít nhất một nhân tử bằng 0. Hãy tìm nghiệm của từng nhân tử trong phương trình (2x - 4)(x - 3)(x - 7) = 0.",
        "tier2_hint": "Giải từng phương trình con:\n• 2x - 4 = 0 => 2x = 4 => x = 2.\n• x - 3 = 0 => x = 3.\n• x - 7 = 0 => x = 7.\nĐề bài hỏi TỔNG các nghiệm (sum of the solutions).",
        "tier3_hint": "Bước 1: Các nghiệm của phương trình là x1 = 2, x2 = 3, x3 = 7.\nBước 2: Tổng các nghiệm = 2 + 3 + 7 = 12.\nChốt đáp án chính xác: [C].",
        "strategic_tip": "Mẹo giải nhanh: Đừng nhân tung đa thức ra! Tìm ngay nghiệm của từng ngoặc đơn. Cẩn thận ngoặc (2x - 4) cho nghiệm x = 2 chứ không phải x = 4.",
        "option_explanations": {
            "A": "Loại A - (−14): Sai dấu và sai nghiệm.",
            "B": "Loại B - (−12): Sai dấu của tổng nghiệm.",
            "C": "ĐÁP ÁN ĐÚNG. C (12): Ba nghiệm là 2, 3, 7 => Tổng = 2 + 3 + 7 = 12.",
            "D": "Loại D - (14): Bẫy lấy nhầm nghiệm đầu tiên là 4 (quên chia 2): 4 + 3 + 7 = 14."
        },
        "pooe_breakdown": "• Loại D vì bẫy quên chia 2 ở nhân tử đầu (2x - 4 = 0 => x = 2, không phải 4).\n• Loại A, B vì nghiệm đều dương nên tổng phải dương.\n• Chọn C: 2 + 3 + 7 = 12.",
        "mermaid_diagram": 'flowchart TD\n    A["Phương trình: (2x - 4)(x - 3)(x - 7) = 0"] --> B["2x - 4 = 0 => x1 = 2"]\n    A --> C["x - 3 = 0 => x2 = 3"]\n    A --> D["x - 7 = 0 => x3 = 7"]\n    B & C & D --> E["Tính tổng: 2 + 3 + 7 = 12"]\n    E --> F["Chọn đáp án C: 12"]'
    },

    70: { # M1 Q16 (Circle translation from A to B)
        "tier1_hint": "Phương trình đường tròn chuẩn là (x - h)^2 + (y - k)^2 = r^2 với tâm là (h, k). Hãy xác định tọa độ tâm của đường tròn A và đường tròn B.",
        "tier2_hint": "• Đường tròn A: x^2 + (y - 2)^2 = 7 => Tâm A = (0, 2).\n• Đường tròn B: (x - 2)^2 + y^2 = 7 => Tâm B = (2, 0).\nHãy xem tâm đã dịch chuyển như thế nào từ (0, 2) sang (2, 0).",
        "tier3_hint": "Tọa độ x thay đổi từ 0 lên 2 => Dịch sang phải 2 đơn vị (2 units right).\nTọa độ y thay đổi từ 2 xuống 0 => Dịch xuống dưới 2 đơn vị (2 units down).\nVậy phép tịnh tiến là 2 units right and 2 units down.\nChốt đáp án chính xác: [D].",
        "strategic_tip": "Quy tắc tịnh tiến: (x - 2) nghĩa là dịch sang PHẢI 2 đơn vị; (y - 2) thành y nghĩa là dịch XUỐNG 2 đơn vị.",
        "option_explanations": {
            "A": "Loại A: Dịch sang trái là sai hướng của trục x.",
            "B": "Loại B: Thiếu phép dịch chuyển theo trục y.",
            "C": "Loại C: Sai hướng cả trục x (phải sang phải) và trục y (phải đi xuống).",
            "D": "ĐÁP ÁN ĐÚNG. D: Tâm A (0, 2) -> Tâm B (2, 0): Dịch sang phải 2 đơn vị và xuống dưới 2 đơn vị."
        },
        "pooe_breakdown": "• Tâm A = (0, 2), Tâm B = (2, 0).\n• x tăng 2 (sang phải), y giảm 2 (xuống dưới).\n• Chỉ có D mô tả đúng cả 2 trục.",
        "mermaid_diagram": 'flowchart TD\n    A["Đường tròn A: x^2 + (y - 2)^2 = 7 => Tâm (0, 2)"] --> B["Đường tròn B: (x - 2)^2 + y^2 = 7 => Tâm (2, 0)"]\n    B --> C["So sánh tọa độ x: Từ 0 -> 2 (Sang phải 2 đơn vị)"]\n    B --> D["So sánh tọa độ y: Từ 2 -> 0 (Xuống dưới 2 đơn vị)"]\n    C & D --> E["Kết luận: 2 units right and 2 units down => Chọn D"]'
    },

    71: { # M1 Q17 (Line j and Line k intersection)
        "tier1_hint": "Đường thẳng j đi qua các điểm (0, 16), (1, 20), (2, 24). Hãy viết phương trình của đường thẳng j. Sau đó tìm giao điểm với đường thẳng k: y = 8x.",
        "tier2_hint": "• Đường thẳng j có hệ số góc m = (20 - 16)/(1 - 0) = 4 và y-intercept = 16 => Phương trình: y = 4x + 16.\n• Giao điểm thỏa mãn: 8x = 4x + 16.",
        "tier3_hint": "Bước 1: 8x = 4x + 16 => 4x = 16 => x = 4.\nBước 2: Thay x = 4 vào y = 8x => y = 8 * 4 = 32.\nTọa độ giao điểm là (4, 32).\nChốt đáp án chính xác: [A].",
        "strategic_tip": "Mẹo Desmos: Nhập bảng điểm của j hoặc nhập thẳng 'y - 16 = 4x' và 'y = 8x'. Click vào điểm giao nhau, Desmos hiển thị ngay (4, 32).",
        "option_explanations": {
            "A": "ĐÁP ÁN ĐÚNG. A (4, 32): 8(4) = 4(4) + 16 = 32, thỏa mãn cả hai đường thẳng.",
            "B": "Loại B: (4, 68) không thỏa mãn y = 8x (8*4 = 32 khác 68).",
            "C": "Loại C: (5, 40) thỏa mãn y = 8x nhưng không nằm trên đường thẳng j (4*5 + 16 = 36 khác 40).",
            "D": "Loại D: (5, 36) thỏa mãn đường thẳng j nhưng không nằm trên đường thẳng k."
        },
        "pooe_breakdown": "• Thay tọa độ vào y = 8x: Chỉ có A (4, 32) và C (5, 40) thỏa mãn.\n• Thay vào đường j: y = 4x + 16: Chỉ có A thỏa mãn (4*4 + 16 = 32).\n• Chọn A.",
        "mermaid_diagram": 'flowchart TD\n    A["Đường j qua (0, 16), (1, 20) => y = 4x + 16"] --> B["Đường k: y = 8x"]\n    B --> C["Phương trình hoành độ giao điểm: 8x = 4x + 16"]\n    C --> D["4x = 16 => x = 4"]\n    D --> E["Tìm y: y = 8 * 4 = 32 => Tọa độ (4, 32)"]\n    E --> F["Chọn đáp án A"]'
    },

    72: { # M1 Q18 (Prism lateral face area)
        "tier1_hint": "Hình hộp chữ nhật đứng có đáy là hình vuông diện tích 484 cm^2. Hãy tìm độ dài cạnh đáy và chiều cao của hình hộp dựa vào thể tích V = 3,388 cm^3.",
        "tier2_hint": "• Cạnh đáy: s = sqrt(484) = 22 cm.\n• Thể tích: V = Diện tích đáy * Chiều cao = 484 * h = 3388 => h = 3388 / 484 = 7 cm.\n• Diện tích một mặt bên (lateral face) là hình chữ nhật kích thước s * h.",
        "tier3_hint": "Bước 1: s = sqrt(484) = 22 cm.\nBước 2: h = 3388 / 484 = 7 cm.\nBước 3: Diện tích một mặt bên = 22 * 7 = 154 cm^2.\nChốt đáp án chính xác: [C].",
        "strategic_tip": "Đọc kỹ câu hỏi: Đề bài hỏi 'area of ONE of the four lateral faces' (diện tích MỘT mặt bên = 154), không phải diện tích xung quanh cả 4 mặt (4 * 154 = 616, bẫy A).",
        "option_explanations": {
            "A": "Loại A - (616): Bẫy tính tổng diện tích cả 4 mặt bên (4 * 154 = 616).",
            "B": "Loại B - (605): Tính toán sai.",
            "C": "ĐÁP ÁN ĐÚNG. C (154): Diện tích 1 mặt bên = s * h = 22 * 7 = 154 cm^2.",
            "D": "Loại D - (7): Đây mới chỉ là chiều cao h, chưa nhân với cạnh đáy."
        },
        "pooe_breakdown": "• Loại D vì 7 chỉ là chiều cao h.\n• Loại A vì 616 là diện tích của cả 4 mặt bên gộp lại.\n• Chọn C: 22 * 7 = 154 cm^2.",
        "mermaid_diagram": 'flowchart TD\n    A["Đáy vuông: Diện tích = 484 cm^2 => Cạnh s = sqrt(484) = 22 cm"] --> B["Thể tích V = 3388 cm^3"]\n    B --> C["Chiều cao h = V / Đáy = 3388 / 484 = 7 cm"]\n    C --> D["Diện tích 1 mặt bên = s * h = 22 * 7"]\n    D --> E["Kết quả: 154 cm^2"]\n    E --> F["Chọn đáp án C: 154"]'
    },

    73: { # M1 Q19 (Wood bison population doubling model)
        "tier1_hint": "Quần thể nhân đôi từ cuối năm 1994 (t = 0) đến cuối năm 1998 (t = 4). Chu kỳ nhân đôi là 4 năm. Số mũ của cơ số 2 phải có dạng t/4 hay 4t?",
        "tier2_hint": "Công thức tăng trưởng nhân đôi với chu kỳ d năm là P = P0 * 2^(t/d). Ở đây d = 4 năm nên số mũ phải là t/4 (loại B và D). Tại t = 1 (cuối 1995), P ≈ 175.",
        "tier3_hint": "Với t = 1, P(1) = P0 * 2^(1/4) = 175 => P0 = 175 / 2^(0.25) ≈ 175 / 1.1892 ≈ 147.16 ≈ 147.\nPhương trình chuẩn xác là P = 147(2)^(t/4).\nChốt đáp án chính xác: [A].",
        "strategic_tip": "Kiểm tra số mũ: Khi t = 4 năm thì số lần nhân đôi là 1 => số mũ phải là 4/4 = 1 => dạng 2^(t/4). Tránh bẫy nhầm P0 là 175 (175 là dân số ở t = 1, không phải t = 0).",
        "option_explanations": {
            "A": "ĐÁP ÁN ĐÚNG. A: P = 147(2)^(t/4), đúng chu kỳ nhân đôi 4 năm và cho P(1) ≈ 175.",
            "B": "Loại B: Số mũ 4t là sai (nghĩa là nhân đôi 4 lần mỗi năm).",
            "C": "Loại C: Bẫy gán 175 làm giá trị ban đầu P0 tại t = 0 (thực tế 175 là tại t = 1).",
            "D": "Loại D: Sai cả giá trị ban đầu và số mũ."
        },
        "pooe_breakdown": "• Loại B, D: Chu kỳ nhân đôi 4 năm phải có số mũ là t/4, không thể là 4t.\n• Loại C: Tại t = 0 dân số là 147 để đến t = 1 đạt 175. C gán P0 = 175 là sai.\n• Chọn A.",
        "mermaid_diagram": 'flowchart TD\n    A["Quần thể nhân đôi sau 4 năm (1994 đến 1998)"] --> B["Dạng hàm số mũ: P = P0 * 2^(t/4) => Loại B, D"]\n    B --> C["Dữ kiện: Cuối 1995 (t = 1) có P = 175 con"]\n    C --> D["Tính P0: P0 * 2^(1/4) = 175 => P0 ≈ 147"]\n    D --> E["Mô hình: P = 147(2)^(t/4) => Chọn đáp án A"]'
    },

    74: { # M1 Q20 (x^2 - 14x = p, solution 7 + sqrt(86))
        "tier1_hint": "Nghiệm của phương trình có dạng 7 + sqrt(86). Hãy nhớ lại công thức nghiệm hoặc phương pháp thêm bớt để tạo thành bình phương hoàn hảo (completing the square).",
        "tier2_hint": "Thêm bớt tạo bình phương hoàn chỉnh:\nx^2 - 14x + 49 = p + 49\n=> (x - 7)^2 = p + 49\n=> x - 7 = ±sqrt(p + 49)\n=> x = 7 ± sqrt(p + 49).",
        "tier3_hint": "Đề bài cho nghiệm là 7 + sqrt(86), so sánh với công thức:\np + 49 = 86\n=> p = 86 - 49 = 37.\nChốt đáp án chính xác: [37].",
        "strategic_tip": "Cách kiểm tra bằng Desmos: Nhập x = 7 + sqrt(86). Sau đó nhập 'x^2 - 14x', Desmos sẽ tính ngay ra giá trị chính xác là 37!",
        "grid_in_explanation": {
            "correct_answer": "37",
            "solution_steps": "1. Biến đổi: (x - 7)^2 - 49 = p => (x - 7)^2 = p + 49.\n2. x = 7 ± sqrt(p + 49).\n3. Đối chiếu với 7 + sqrt(86) => p + 49 = 86.\n4. p = 86 - 49 = 37.",
            "trap_errors": "Bẫy tính toán: Lấy 86 + 49 = 135 (chuyển vế sai dấu)."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 37 - Thỏa mãn p + 49 = 86.",
        "mermaid_diagram": 'flowchart TD\n    A["Phương trình: x^2 - 14x = p"] --> B["Thêm 49 vào 2 vế: (x - 7)^2 = p + 49"]\n    B --> C["Khai căn: x = 7 ± sqrt(p + 49)"]\n    C --> D["So sánh với nghiệm 7 + sqrt(86): p + 49 = 86"]\n    D --> E["Giải tìm p: p = 86 - 49 = 37"]\n    E --> F["Điền đáp án: 37"]'
    },

    75: { # M1 Q21 ((x+2)^2 + 4(x+2) + 4 = 0)
        "tier1_hint": "Hãy đặt ẩn phụ u = x + 2. Phương trình trở thành phương trình bậc hai nào theo biến u?",
        "tier2_hint": "Phương trình có dạng u^2 + 4u + 4 = 0. Đây là hằng đẳng thức (u + 2)^2 = 0. Hãy tìm số nghiệm thực phân biệt của phương trình.",
        "tier3_hint": "Bước 1: u^2 + 4u + 4 = (u + 2)^2 = 0 => u = -2 (nghiệm kép).\nBước 2: Thay lại u = x + 2: x + 2 = -2 => x = -4.\nPhương trình chỉ có duy nhất một nghiệm thực phân biệt x = -4.\nChốt đáp án chính xác: [A].",
        "strategic_tip": "Mẹo biệt thức Delta: Với Au^2 + Bu + C = 0, Delta = 4^2 - 4(1)(4) = 16 - 16 = 0. Delta = 0 luôn tương đương với DUY NHẤT MỘT NGHIỆM THỰC PHÂN BIỆT (Exactly one distinct real solution).",
        "option_explanations": {
            "A": "ĐÁP ÁN ĐÚNG. A (Exactly one): Phương trình là dạng bình phương hoàn chỉnh (x + 4)^2 = 0 nên có đúng 1 nghiệm phân biệt x = -4.",
            "B": "Loại B - Exactly two: Nhầm lẫn do phương trình bậc hai thông thường có 2 nghiệm.",
            "C": "Loại C - Infinitely many: Đây là phương trình đại số bậc 2, không phải đồng nhất thức.",
            "D": "Loại D - Zero: Phương trình có nghiệm thực x = -4."
        },
        "pooe_breakdown": "• Delta = 0 => Phương trình có đúng 1 nghiệm thực phân biệt (nghiệm kép).\n• Chọn A.",
        "mermaid_diagram": 'flowchart TD\n    A["Phương trình: (x+2)^2 + 4(x+2) + 4 = 0"] --> B["Đặt u = x + 2 => u^2 + 4u + 4 = 0"]\n    B --> C["Hằng đẳng thức: (u + 2)^2 = 0 => u = -2"]\n    C --> D["Tìm x: x + 2 = -2 => x = -4"]\n    D --> E["Có duy nhất 1 nghiệm thực phân biệt => Chọn đáp án A"]'
    },

    76: { # M1 Q22 (474 is 1450% of (b + c), b is 58% of c)
        "tier1_hint": "Đề bài cho hai mối quan hệ tỷ lệ phần trăm: (1) 474 = 1,450% * (b + c) và (2) b = 58% * c. Hãy biểu diễn tổng (b + c) theo biến c.",
        "tier2_hint": "• Đổi phần trăm ra số thập phân: 1,450% = 14.5; 58% = 0.58.\n• Ta có b = 0.58c => b + c = 0.58c + c = 1.58c.\n• Thay vào phương trình 1: 474 = 14.5 * (1.58c).",
        "tier3_hint": "Bước 1: 474 = 14.5 * 1.58c = 22.91c.\nBước 2: Tìm c = 474 / 22.91 = 47400 / 2291 ≈ 20.689655.\nBước 3: Tìm b = 0.58c = 0.58 * (474 / 22.91) = (0.58 * 474) / 22.91 = 274.92 / 22.91 = 12.\nChốt đáp án chính xác: [12].",
        "strategic_tip": "Kỹ thuật triệt tiêu số học: b = 0.58 * c = 0.58 * [474 / (14.5 * 1.58)] = (0.58 / 1.58) * (474 / 14.5) = (29 / 79) * (948 / 29) = 948 / 79 = 12 tròn trịa!",
        "grid_in_explanation": {
            "correct_answer": "12",
            "solution_steps": "1. 474 = 14.5 * (b + c).\n2. b = 0.58c => b + c = 1.58c.\n3. 474 = 14.5 * 1.58c = 22.91c.\n4. b = 0.58 * c = 0.58 * (474 / 22.91) = 274.92 / 22.91 = 12.",
            "trap_errors": "Bẫy tính ra c ≈ 20.69 rồi điền c thay vì tính b."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 12 - Kết quả chính xác sau khi khử biến.",
        "mermaid_diagram": 'flowchart TD\n    A["474 = 14.5(b + c) và b = 0.58c"] --> B["Thay b = 0.58c vào tổng: b + c = 1.58c"]\n    B --> C["474 = 14.5 * 1.58c = 22.91c"]\n    C --> D["Tìm b = 0.58c = 0.58 * (474 / 22.91)"]\n    D --> E["Tính toán: b = 274.92 / 22.91 = 12"]\n    E --> F["Điền đáp án: 12"]'
    },

    # =========================================================================
    # MATH MODULE 2 (Q1 - Q22) -> IDs 77 to 98
    # =========================================================================
    77: { # M2 Q1 (Sunflower height after 6 weeks)
        "tier1_hint": "Trục hoành x biểu thị số tuần quan sát (weeks of observation), trục tung y biểu thị chiều cao tính bằng cm. Hãy tra cứu giá trị y tương ứng khi x = 6.",
        "tier2_hint": "Từ vị trí x = 6 trên trục hoành, dóng thẳng đứng lên đường đồ thị để tìm điểm tương ứng, rồi dóng sang trục tung để đọc giá trị chiều cao y.",
        "tier3_hint": "Tại x = 6, điểm trên đồ thị có tung độ y nằm ở mức 80 cm. Như vậy sau 6 tuần quan sát, chiều cao cây hoa hướng dương ước tính đạt 80 cm.\nChốt đáp án chính xác: [D].",
        "strategic_tip": "Đọc trục tọa độ cẩn thận: Quan sát bước nhảy của các vạch chia trên trục tung (mỗi vạch lớn là 20 đơn vị).",
        "option_explanations": {
            "A": "Loại A - (6): Nhầm lẫn lấy chính giá trị của trục x (số tuần).",
            "B": "Loại B - (10): Chiều cao ở khoảng tuần thứ 2-3.",
            "C": "Loại C - (20): Chiều cao ở khoảng tuần thứ 4.",
            "D": "ĐÁP ÁN ĐÚNG. D (80): Tại x = 6 tuần, đồ thị chỉ rõ y = 80 cm."
        },
        "pooe_breakdown": "• Dóng x = 6 lên đồ thị cắt đúng vạch y = 80. Chọn D.",
        "mermaid_diagram": 'flowchart TD\n    A["Đồ thị chiều cao theo tuần"] --> B["Xác định x = 6 tuần trên trục hoành"]\n    B --> C["Dóng lên đường đồ thị tìm điểm tương ứng"]\n    C --> D["Dóng sang trục tung đọc giá trị y = 80 cm"]\n    D --> E["Chọn đáp án D: 80"]'
    },

    78: { # M2 Q2 (Rational function y-intercept = -6)
        "tier1_hint": "Giao điểm với trục tung (y-intercept) là điểm mà đồ thị cắt trục thẳng đứng y (tại đó x = 0). Hãy quan sát vị trí đồ thị cắt trục tung.",
        "tier2_hint": "Nhìn vào trục y (x = 0), nhánh đồ thị đi qua vạch số nào ở phía dưới trục hoành?",
        "tier3_hint": "Đồ thị hàm phân thức cắt trục tung tại điểm có tọa độ (0, -6). Tung độ của y-intercept là -6.\nChốt đáp án chính xác: [-6].",
        "strategic_tip": "Quy tắc Grid-in với số âm: Dấu âm '-' được phép nhập trong các câu tự điền đáp số của Digital SAT. Hãy chắc chắn nhập dấu trừ trước số 6.",
        "grid_in_explanation": {
            "correct_answer": "-6",
            "solution_steps": "1. Tìm giao điểm của đồ thị hàm số với trục tung (trục y).\n2. Điểm giao cắt nằm ở tọa độ (0, -6).\n3. y-coordinate là -6.",
            "trap_errors": "Bẫy quên dấu âm hoặc đọc nhầm x-intercept."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: -6 - Tung độ giao điểm với trục y.",
        "mermaid_diagram": 'flowchart TD\n    A["Đồ thị hàm số phân thức"] --> B["Tìm giao điểm với trục tung (trục y tại x = 0)"]\n    B --> C["Điểm cắt nằm ở dưới trục hoành 6 đơn vị"]\n    C --> D["Tung độ: y = -6"]\n    D --> E["Điền đáp án: -6"]'
    },

    79: { # M2 Q3 (Oil mix: 5.3x + 4.0y = 18)
        "tier1_hint": "Xác định các đại lượng: Mỗi gallon xăng cho máy xới (tiller, x) cần 5.3 ounces dầu. Mỗi gallon xăng cho máy cắt cỏ (lawnmower, y) cần 4.0 ounces dầu. Tổng lượng dầu sử dụng là 18 ounces.",
        "tier2_hint": "Tổng lượng dầu = (Lượng dầu cho máy xới) + (Lượng dầu cho máy cắt cỏ) = 5.3 * x + 4.0 * y = 18.",
        "tier3_hint": "Số ounces dầu cho máy xới là 5.3x. Số ounces dầu cho máy cắt cỏ là 4.0y. Tổng lượng dầu là 5.3x + 4.0y = 18.\nChốt đáp án chính xác: [C].",
        "strategic_tip": "Kiểm tra đơn vị: (ounces/gallon) * (gallons) = ounces. Cả 5.3x và 4.0y đều có đơn vị là ounces, cộng lại bằng 18 ounces là hoàn toàn đồng nhất về thứ nguyên.",
        "option_explanations": {
            "A": "Loại A: x + y = 18 bỏ quên hệ số tiêu thụ dầu 5.3 và 4.0.",
            "B": "Loại B: Phép chia 5.3/x + 4.0/y là sai mô hình tỷ lệ thuận.",
            "C": "ĐÁP ÁN ĐÚNG. C: 5.3x + 4.0y = 18 biểu diễn chính xác tổng lượng dầu.",
            "D": "Loại D: 9.3(x + y) = 18 giả định sai rằng hai máy có cùng lượng xăng."
        },
        "pooe_breakdown": "• Loại A, B, D sai công thức lượng dầu.\n• Chọn C: 5.3x + 4.0y = 18 chuẩn xác.",
        "mermaid_diagram": 'flowchart TD\n    A["Dầu máy xới: 5.3 oz/gal cho x gal => 5.3x"] --> C["Tổng lượng dầu = 18 oz"]\n    B["Dầu máy cắt: 4.0 oz/gal cho y gal => 4.0y"] --> C\n    C --> D["Phương trình: 5.3x + 4.0y = 18"]\n    D --> E["Chọn đáp án C"]'
    },

    80: { # M2 Q4 (Dominique budget 274 - 118 = 156)
        "tier1_hint": "Ngân sách tối đa của Dominique là 274 dollars. Cô ấy đã chi 118 dollars. Số tiền tối đa cô ấy CÒN CÓ THỂ CHI THÊM (additional money) mà không vượt quá ngân sách là bao nhiêu?",
        "tier2_hint": "Thiết lập bất phương trình chi tiêu: Đã chi + Chi thêm <= Ngân sách => 118 + x <= 274 => x <= 274 - 118.",
        "tier3_hint": "Số tiền tối đa có thể chi thêm là: 274 - 118 = 156 dollars.\nChốt đáp án chính xác: [B].",
        "strategic_tip": "Đọc kỹ câu hỏi: Đề bài hỏi 'additional money' (số tiền chi thêm), không phải số tiền đã chi (118) hay tổng ngân sách (274).",
        "option_explanations": {
            "A": "Loại A - (118 dollars): Đây là số tiền ĐÃ chi, không phải số tiền có thể chi thêm.",
            "B": "ĐÁP ÁN ĐÚNG. B (156 dollars): 274 - 118 = 156 dollars.",
            "C": "Loại C - (274 dollars): Đây là tổng ngân sách ban đầu.",
            "D": "Loại D - (392 dollars): Bẫy cộng dồn 274 + 118 = 392."
        },
        "pooe_breakdown": "• 274 - 118 = 156 dollars. Chọn B.",
        "mermaid_diagram": 'flowchart TD\n    A["Ngân sách = 274$, Đã chi = 118$"] --> B["Số tiền chi thêm tối đa: x = 274 - 118"]\n    B --> C["x = 156 dollars"]\n    C --> D["Chọn đáp án B: 156 dollars"]'
    },

    81: { # M2 Q5 (Speed = 12 cm / 6 s = 2 cm/s)
        "tier1_hint": "Vận tốc không đổi (constant speed) được tính bằng quãng đường chia cho thời gian: v = s / t.",
        "tier2_hint": "Hạt di chuyển quãng đường s = 12 centimeters trong thời gian t = 6 seconds. Áp dụng công thức v = 12 / 6.",
        "tier3_hint": "Vận tốc của hạt là: v = 12 / 6 = 2 centimeters per second.\nChốt đáp án chính xác: [A].",
        "strategic_tip": "Kiểm tra đơn vị: centimeters / seconds = cm/s. Không cần đổi đơn vị trong bài này.",
        "option_explanations": {
            "A": "ĐÁP ÁN ĐÚNG. A (2): 12 cm / 6 s = 2 cm/s.",
            "B": "Loại B - (6): Nhầm lẫn thời gian t = 6 s.",
            "C": "Loại C - (12): Nhầm lẫn quãng đường s = 12 cm.",
            "D": "Loại D - (72): Bẫy lấy quãng đường nhân thời gian (12 * 6 = 72)."
        },
        "pooe_breakdown": "• Vận tốc v = 12 / 6 = 2 cm/s. Chọn A.",
        "mermaid_diagram": 'flowchart TD\n    A["Quãng đường s = 12 cm, Thời gian t = 6 s"] --> B["Công thức vận tốc: v = s / t"]\n    B --> C["v = 12 / 6 = 2 cm/s"]\n    C --> D["Chọn đáp án A: 2"]'
    },

    82: { # M2 Q6 (6x + 1 = 55 => 6x = 54)
        "tier1_hint": "Phương trình đã cho là 6x + 1 = 55. Hãy chuyển số hạng tự do +1 sang vế phải.",
        "tier2_hint": "Trừ 1 ở cả hai vế: 6x = 55 - 1 => 6x = 54. Quan sát các phương án để tìm phương trình tương đương.",
        "tier3_hint": "6x + 1 = 55 tương đương với 6x = 54 (nghiệm x = 9). Phương trình ở đáp án D có cùng nghiệm x = 9.\nChốt đáp án chính xác: [D].",
        "strategic_tip": "Không cần giải ra x = 9: Chỉ cần biến đổi tương đương 1 bước bằng cách trừ 1 ở hai vế là ra ngay 6x = 54.",
        "option_explanations": {
            "A": "Loại A: 6x = -54 sai dấu.",
            "B": "Loại B: 6x = 1 sai số hạng vế phải.",
            "C": "Loại C: 6x = 7 sai phép tính.",
            "D": "ĐÁP ÁN ĐÚNG. D (6x = 54): Trừ 1 ở cả hai vế của 6x + 1 = 55 ta được 6x = 54."
        },
        "pooe_breakdown": "• 6x + 1 = 55 <=> 6x = 54. Chọn D.",
        "mermaid_diagram": 'flowchart TD\n    A["Phương trình: 6x + 1 = 55"] --> B["Trừ 1 ở cả hai vế"]\n    B --> C["6x = 55 - 1 = 54"]\n    C --> D["Chọn đáp án D: 6x = 54"]'
    },

    83: { # M2 Q7 (Parallel lines r and s, x = 26)
        "tier1_hint": "Hai đường thẳng r và s được cắt bởi cát tuyến t. Hai góc ở vị trí so le trong (alternate interior angles) hoặc đồng vị (corresponding angles) có mối quan hệ gì khi hai đường thẳng song song?",
        "tier2_hint": "Theo định lý hình học: Nếu hai đường thẳng cắt một cát tuyến tạo ra hai góc so le trong bằng nhau thì hai đường thẳng đó song song. Góc đã cho là 26°, góc tương ứng là x.",
        "tier3_hint": "Để r song song với s, hai góc so le trong phải bằng nhau: x = 26.\nChốt đáp án chính xác: [B].",
        "strategic_tip": "Quy tắc song song: Hai góc bằng nhau (x = 26) là điều kiện cần và đủ để chứng minh song song. Các bất đẳng thức x < 26 hay x > 26 không chứng minh được tính song song.",
        "option_explanations": {
            "A": "Loại A: x < 26 không đảm bảo hai đường thẳng song song.",
            "B": "ĐÁP ÁN ĐÚNG. B (x = 26): Hai góc so le trong bằng nhau chứng minh r // s.",
            "C": "Loại C: x > 26 làm hai đường thẳng cắt nhau.",
            "D": "Loại D: x - 26 = 360 là điều kiện vô lý."
        },
        "pooe_breakdown": "• Chỉ có đẳng thức x = 26 đảm bảo góc so le trong bằng nhau => r // s. Chọn B.",
        "mermaid_diagram": 'flowchart TD\n    A["Đường thẳng r, s cắt bởi cát tuyến t"] --> B["Hai góc ở vị trí so le trong: 26° và x"]\n    B --> C["Định lý: Hai đường song song <=> Hai góc so le trong bằng nhau"]\n    C --> D["Điều kiện: x = 26"]\n    D --> E["Chọn đáp án B"]'
    },

    84: { # M2 Q8 (Combine terms x^2 + 4x^2 + 5x + 7x)
        "tier1_hint": "Hãy gom các số hạng đồng dạng (like terms) lại với nhau: các số hạng chứa x^2 gom lại với nhau, các số hạng chứa x gom lại với nhau.",
        "tier2_hint": "• Nhóm x^2: (1 + 4)x^2 = 5x^2.\n• Nhóm x: (5 + 7)x = 12x.\n• Biểu thức thu gọn: 5x^2 + 12x.",
        "tier3_hint": "x^2 + 4x^2 + 5x + 7x = (1 + 4)x^2 + (5 + 7)x = 5x^2 + 12x.\nChốt đáp án chính xác: [C].",
        "strategic_tip": "Lưu ý hệ số ẩn: x^2 có hệ số là 1 (tức 1x^2). Không được quên số 1 này khi cộng với 4x^2!",
        "option_explanations": {
            "A": "Loại A - (3x^2 + 12x): Bẫy lấy 4 - 1 = 3 thay vì 4 + 1 = 5.",
            "B": "Loại B - (4x^2 + 35x): Bẫy nhân 5 * 7 = 35 thay vì cộng.",
            "C": "ĐÁP ÁN ĐÚNG. C (5x^2 + 12x): (1+4)x^2 + (5+7)x = 5x^2 + 12x.",
            "D": "Loại D - (9x^2 + 8x): Bẫy cộng sai các hệ số."
        },
        "pooe_breakdown": "• 1x^2 + 4x^2 = 5x^2, 5x + 7x = 12x => 5x^2 + 12x. Chọn C.",
        "mermaid_diagram": 'flowchart TD\n    A["Biểu thức: x^2 + 4x^2 + 5x + 7x"] --> B["Gom nhóm bậc 2: (1 + 4)x^2 = 5x^2"]\n    A --> C["Gom nhóm bậc 1: (5 + 7)x = 12x"]\n    B & C --> D["Kết quả thu gọn: 5x^2 + 12x"]\n    D --> E["Chọn đáp án C"]'
    },

    85: { # M2 Q9 (Rectangle area 28 x 19)
        "tier1_hint": "Công thức tính diện tích hình chữ nhật là Chiều dài nhân Chiều rộng: Area = length * width.",
        "tier2_hint": "Chiều dài l = 28 cm, Chiều rộng w = 19 cm. Tính tích 28 * 19.",
        "tier3_hint": "Diện tích hình chữ nhật là: A = 28 * 19 = 532 cm^2.\nChốt đáp án chính xác: [532].",
        "strategic_tip": "Mẹo tính nhẩm nhanh: 28 * 19 = 28 * (20 - 1) = 560 - 28 = 532.",
        "grid_in_explanation": {
            "correct_answer": "532",
            "solution_steps": "1. Diện tích hình chữ nhật: A = dài * rộng.\n2. A = 28 * 19 = 532.",
            "trap_errors": "Bẫy tính chu vi 2*(28 + 19) = 94 thay vì tính diện tích."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 532 - Tích 28 * 19.",
        "mermaid_diagram": 'flowchart TD\n    A["Hình chữ nhật: Dài = 28 cm, Rộng = 19 cm"] --> B["Công thức diện tích: Area = dài * rộng"]\n    B --> C["Tính toán: 28 * 19 = 532 cm^2"]\n    C --> D["Điền đáp án: 532"]'
    },

    86: { # M2 Q10 (Parallel lines, find x = 44)
        "tier1_hint": "Quan sát hai đường thẳng song song r và s. Các góc trong hình có quan hệ đồng vị, so le trong hoặc kề bù.",
        "tier2_hint": "Góc kề bù có tổng bằng 180°, góc trong cùng phía có tổng bằng 180°. Tính toán số đo góc x dựa trên các góc đã cho trong hình.",
        "tier3_hint": "Dựa trên hình vẽ hình học, góc liên kết có số đo 136°. Do hai góc trong cùng phía bù nhau (hoặc góc đồng vị kề bù): x = 180° - 136° = 44°.\nChốt đáp án chính xác: [44].",
        "strategic_tip": "Quy tắc góc giữa hai đường thẳng song song: Mọi góc chỉ có thể bằng nhau HOẶC bù nhau (tổng bằng 180°).",
        "grid_in_explanation": {
            "correct_answer": "44",
            "solution_steps": "1. Xác định quan hệ góc kề bù / trong cùng phía với góc 136°.\n2. x = 180° - 136° = 44°.",
            "trap_errors": "Bẫy trừ nhầm từ 90° hoặc điền góc đối đỉnh 136°."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 44 - Bù với góc 136°.",
        "mermaid_diagram": 'flowchart TD\n    A["Hai đường thẳng song song r // s"] --> B["Góc liên kết trên hình = 136°"]\n    B --> C["Quan hệ góc bù nhau: x + 136° = 180°"]\n    C --> D["Tính x: x = 180° - 136° = 44°"]\n    D --> E["Điền đáp án: 44"]'
    },

    87: { # M2 Q11 (A(t) = 15(2)^t, meaning of A(7) = 1920)
        "tier1_hint": "Hàm số A(t) = 15(2)^t: Biến t biểu thị số giây (seconds) và A(t) biểu thị diện tích bằng pixel. Trong biểu thức A(7) = 1,920, số 7 là gì và số 1,920 là gì?",
        "tier2_hint": "Số 7 nằm trong ngoặc f(t) nên t = 7 giây. Giá trị đầu ra là 1,920 nên diện tích là 1,920 pixels.",
        "tier3_hint": "A(7) = 1,920 có nghĩa là: Đúng 7 giây sau khi diện tích bắt đầu tăng, diện tích của hình đạt 1,920 pixels.\nChốt đáp án chính xác: [B].",
        "strategic_tip": "Nguyên tắc đọc ký hiệu hàm số: Trong f(input) = output, input luôn là biến số t (thời gian), còn output là biến số phụ thuộc (diện tích A).",
        "option_explanations": {
            "A": "Loại A: Đảo ngược biến (bẫy nhầm 1,920 giây và 7 pixels).",
            "B": "ĐÁP ÁN ĐÚNG. B: 7 giây sau khi bắt đầu, diện tích đạt 1,920 pixels.",
            "C": "Loại C: Gán nhầm t = 0 giây.",
            "D": "Loại D: Gán nhầm t = 0 giây."
        },
        "pooe_breakdown": "• Input t = 7 seconds, Output A = 1,920 pixels. Chọn B.",
        "mermaid_diagram": 'flowchart TD\n    A["Hàm số: A(t) = 15(2)^t và đẳng thức A(7) = 1920"] --> B["Đầu vào t = 7 (Thời gian là 7 giây)"]\n    A --> C["Đầu ra A(7) = 1920 (Diện tích là 1920 pixels)"]\n    B & C --> D["Ý nghĩa: Sau 7 giây, diện tích là 1920 pixels"]\n    D --> E["Chọn đáp án B"]'
    },

    88: { # M2 Q12 (Similar triangles cos B = cos E = 1/58)
        "tier1_hint": "Hai tam giác ABC và DEF đồng dạng (similar triangles). Các góc tương ứng có bằng nhau không, và các tỉ số lượng giác của các góc tương ứng có mối quan hệ gì?",
        "tier2_hint": "Vì tam giác ABC đồng dạng tam giác DEF, các góc tương ứng bằng nhau: góc A = góc D, góc C = góc F = 90° => góc B = góc E. Hai góc bằng nhau thì có cùng giá trị cosin.",
        "tier3_hint": "Do góc B = góc E, ta có cos E = cos B = 1/58.\nChốt đáp án chính xác: [A].",
        "strategic_tip": "Quy tắc vàng Lượng giác trong Tam giác đồng dạng: Tỉ số lượng giác (sin, cos, tan) CHỈ PHỤ THUỘC VÀO ĐỘ LỚN CỦA GÓC, không phụ thuộc vào kích thước tam giác. Hai góc bằng nhau luôn có sin, cos, tan bằng nhau!",
        "option_explanations": {
            "A": "ĐÁP ÁN ĐÚNG. A (1/58): Tam giác đồng dạng => góc B = góc E => cos E = cos B = 1/58.",
            "B": "Loại B: 1/59 không có căn cứ.",
            "C": "Loại C: 57/58 là bẫy tính sin theo hệ thức sin^2 + cos^2 = 1.",
            "D": "Loại D: 58/59 sai tỷ số."
        },
        "pooe_breakdown": "• Tam giác đồng dạng => góc tương ứng bằng nhau => cos E = cos B = 1/58. Chọn A.",
        "mermaid_diagram": 'flowchart TD\n    A["Tam giác ABC đồng dạng tam giác DEF"] --> B["Các góc tương ứng bằng nhau: Góc B = Góc E"]\n    B --> C["Tỉ số lượng giác bảo toàn: cos E = cos B"]\n    C --> D["Đề bài cho cos B = 1/58 => cos E = 1/58"]\n    D --> E["Chọn đáp án A: 1/58"]'
    },

    89: { # M2 Q13 (Scatterplot temperature slope interpretation)
        "tier1_hint": "Đường hồi quy dốc lên từ trái qua phải biểu thị nhiệt độ tăng hay giảm theo thời gian?",
        "tier2_hint": "Đường thẳng dốc lên => Nhiệt độ TĂNG (increases) => Loại A và B. Hãy tính độ dốc m = delta y / delta x bằng cách lấy hai điểm trên đường thẳng.",
        "tier3_hint": "Tại x = 0, y ≈ 100°F. Tại x = 10, y ≈ 500°F. Độ dốc m ≈ (500 - 100) / (10 - 0) = 400 / 10 = 40°F mỗi giờ. Vậy nhiệt độ ước tính tăng khoảng 40°F mỗi giờ.\nChốt đáp án chính xác: [D].",
        "strategic_tip": "Kỹ thuật loại trừ 2 bước: Bước 1 loại A, B vì 'decreases' (đồ thị thực tế dốc lên). Bước 2 chọn 40°F/h thay vì 190°F/h vì tổng tăng trong 10 giờ là 400°F (400/10 = 40).",
        "option_explanations": {
            "A": "Loại A: Sai chiều biến thiên ('decreases').",
            "B": "Loại B: Sai chiều biến thiên ('decreases').",
            "C": "Loại C: 190°F mỗi giờ là quá lớn (nếu tăng 190°F/h thì sau 10h nhiệt độ phải tăng 1900°F).",
            "D": "ĐÁP ÁN ĐÚNG. D: Nhiệt độ tăng với tốc độ xấp xỉ 40°F mỗi giờ."
        },
        "pooe_breakdown": "• Loại A, B vì đồ thị dốc lên (increases).\n• Loại C vì tốc độ 190 quá cao.\n• Chọn D: Tăng 40°F/giờ.",
        "mermaid_diagram": 'flowchart TD\n    A["Đường hồi quy nhiệt độ theo giờ"] --> B["Đồ thị dốc lên => Nhiệt độ TĂNG (Increases) => Loại A, B"]\n    B --> C["Tính độ dốc: Delta y / Delta x ≈ (500 - 100) / 10 = 40°F/h"]\n    C --> D["Chọn đáp án D: Tăng khoảng 40°F mỗi giờ"]'
    },

    90: { # M2 Q14 (f(x) = 3(x^3 - 1), find f(2))
        "tier1_hint": "Để tính f(2), hãy thay x = 2 vào biểu thức của hàm số f(x) = 3(x^3 - 1).",
        "tier2_hint": "Tính giá trị trong ngoặc trước: 2^3 = 8 => x^3 - 1 = 8 - 1 = 7. Sau đó nhân với hệ số 3 ở ngoài.",
        "tier3_hint": "f(2) = 3 * (2^3 - 1) = 3 * (8 - 1) = 3 * 7 = 21.\nChốt đáp án chính xác: [C].",
        "strategic_tip": "Mẹo Desmos: Nhập f(x) = 3(x^3 - 1), ở dòng dưới gõ 'f(2)', Desmos lập tức hiển thị 21.",
        "option_explanations": {
            "A": "Loại A - (7): Đây mới chỉ là giá trị trong ngoặc (8 - 1 = 7), quên nhân 3.",
            "B": "Loại B - (8): Nhầm lẫn lấy 2^3 = 8.",
            "C": "ĐÁP ÁN ĐÚNG. C (21): f(2) = 3 * (8 - 1) = 3 * 7 = 21.",
            "D": "Loại D - (24): Bẫy lấy 3 * 2^3 = 24 mà quên trừ 1."
        },
        "pooe_breakdown": "• 3 * (2^3 - 1) = 3 * 7 = 21. Chọn C.",
        "mermaid_diagram": 'flowchart TD\n    A["Hàm số: f(x) = 3(x^3 - 1)"] --> B["Thay x = 2 vào hàm số"]\n    B --> C["Tính trong ngoặc: 2^3 - 1 = 8 - 1 = 7"]\n    C --> D["Nhân hệ số 3: 3 * 7 = 21"]\n    D --> E["Chọn đáp án C: 21"]'
    },

    91: { # M2 Q15 (Line parallel to y = 1/2 x + 8 has slope = 1/2)
        "tier1_hint": "Đường thẳng k có phương trình y = (1/2)x + 8. Hệ số góc của đường thẳng k là bao nhiêu?",
        "tier2_hint": "Hai đường thẳng song song trong mặt phẳng tọa độ luôn có HỆ SỐ GÓC BẰNG NHAU (equal slopes). Vì đường thẳng j song song với k nên slope của j bằng slope của k.",
        "tier3_hint": "Đường thẳng k có slope m = 1/2. Vì j // k nên hệ số góc của j cũng là 1/2 (hoặc 0.5).\nChốt đáp án chính xác: [1/2, .5, 0.5].",
        "strategic_tip": "Quy tắc song song vs vuông góc: Parallel lines => m1 = m2. Perpendicular lines => m1 * m2 = -1.",
        "grid_in_explanation": {
            "correct_answer": "1/2, .5, 0.5",
            "solution_steps": "1. Đường thẳng k: y = (1/2)x + 8 có hệ số góc m = 1/2.\n2. Hai đường thẳng song song có cùng hệ số góc.\n3. Slope của đường j là 1/2 (chấp nhận 1/2, .5, hoặc 0.5).",
            "trap_errors": "Bẫy lấy tung độ gốc 8 thay vì hệ số góc 1/2."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 1/2 hoặc 0.5 - Hệ số góc của hai đường thẳng song song.",
        "mermaid_diagram": 'flowchart TD\n    A["Đường thẳng k: y = (1/2)x + 8"] --> B["Xác định hệ số góc của k: m = 1/2"]\n    B --> C["Định lý: Hai đường song song có cùng hệ số góc"]\n    C --> D["Hệ số góc của j = 1/2 = 0.5"]\n    D --> E["Điền đáp án: 1/2 hoặc 0.5"]'
    },

    92: { # M2 Q16 (Graph passes (0, 8) and (5, 16) => f(x) = 1.60x + 8)
        "tier1_hint": "Đồ thị đường thẳng cắt trục tung tại (0, 8) và đi qua điểm (5, 16). Hãy xác định tung độ gốc (y-intercept) và tính hệ số góc (slope).",
        "tier2_hint": "• y-intercept = 8 => Phương trình có dạng f(x) = mx + 8 (loại B và D có -8).\n• Tính slope: m = (16 - 8) / (5 - 0) = 8 / 5 = 1.60.",
        "tier3_hint": "Phương trình đường thẳng là f(x) = 1.60x + 8.\nChốt đáp án chính xác: [A].",
        "strategic_tip": "Mẹo nhanh: Điểm cắt trục tung là (0, 8) nên đuôi phương trình bắt buộc phải là +8 => Loại ngay B và D! Tiếp theo 8/5 = 1.60 => Chọn A thay vì C (0.63 là 5/8, bẫy nghịch đảo slope).",
        "option_explanations": {
            "A": "ĐÁP ÁN ĐÚNG. A: f(x) = 1.60x + 8 (slope m = 8/5 = 1.60, y-intercept = +8).",
            "B": "Loại B: Sai y-intercept (-8).",
            "C": "Loại C: Bẫy nghịch đảo độ dốc (lấy delta x / delta y = 5/8 ≈ 0.63 thay vì delta y / delta x).",
            "D": "Loại D: Sai cả slope và y-intercept."
        },
        "pooe_breakdown": "• Loại B, D vì y-intercept là +8.\n• Loại C vì slope m = (16-8)/5 = 8/5 = 1.60, không phải 5/8 = 0.63.\n• Chọn A.",
        "mermaid_diagram": 'flowchart TD\n    A["Đồ thị đi qua (0, 8) và (5, 16)"] --> B["y-intercept = 8 => Dạng y = mx + 8 => Loại B, D"]\n    B --> C["Tính slope m = (16 - 8) / (5 - 0) = 8 / 5 = 1.60"]\n    C --> D["Phương trình: f(x) = 1.60x + 8"]\n    D --> E["Chọn đáp án A"]'
    },

    93: { # M2 Q17 (27x^2 = 27(9), negative solution)
        "tier1_hint": "Phương trình: 27x^2 = 27(9). Cả hai vế đều có thừa số 27. Hãy chia cả hai vế cho 27 để đơn giản hóa phương trình.",
        "tier2_hint": "Sau khi chia cả hai vế cho 27, ta được x^2 = 9. Lấy căn bậc hai hai vế: x = ±3. Đề bài yêu cầu tìm NGHIỆM ÂM (negative solution).",
        "tier3_hint": "Bước 1: Chia hai vế cho 27: x^2 = 9.\nBước 2: x = ±3.\nBước 3: Đề bài yêu cầu 'negative solution' => Chọn x = -3.\nChốt đáp án chính xác: [-3].",
        "strategic_tip": "Đọc kỹ từ khóa: Đề bài yêu cầu 'negative solution'. Nếu điền +3 sẽ bị mất điểm đáng tiếc!",
        "grid_in_explanation": {
            "correct_answer": "-3",
            "solution_steps": "1. 27x^2 = 27 * 9.\n2. Chia 27 ở hai vế: x^2 = 9.\n3. x = ±3.\n4. Nghiệm âm là -3.",
            "trap_errors": "Bẫy điền nghiệm dương 3 thay vì nghiệm âm -3."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: -3 - Nghiệm âm của phương trình x^2 = 9.",
        "mermaid_diagram": 'flowchart TD\n    A["Phương trình: 27x^2 = 27(9)"] --> B["Chia cả hai vế cho 27: x^2 = 9"]\n    B --> C["Khai căn: x = ±3"]\n    C --> D{"Đề bài hỏi: Negative solution!"}\n    D --> E["Chọn nghiệm âm: x = -3"]\n    E --> F["Điền đáp án: -3"]'
    },

    94: { # M2 Q18 (y-intercept of y = (8/13)^(x+1))
        "tier1_hint": "Giao điểm với trục tung (y-intercept) của bất kỳ đồ thị nào luôn xảy ra tại x = 0. Hãy thay x = 0 vào hàm số để tìm tung độ y tương ứng.",
        "tier2_hint": "Thay x = 0 vào y = (8/13)^(x + 1): y = (8/13)^(0 + 1) = (8/13)^1 = 8/13. Tọa độ điểm là (0, y).",
        "tier3_hint": "Tại x = 0, y = (8/13)^1 = 8/13. Giao điểm với trục tung là (0, 8/13).\nChốt đáp án chính xác: [D].",
        "strategic_tip": "Bẫy thường gặp: Học sinh hay nhớ máy móc 'hàm số mũ luôn có y-intercept là (0, 1)' vì nhầm với a^x. Ở đây số mũ là x + 1 nên khi x = 0 số mũ là 1, cho ra a^1 = 8/13!",
        "option_explanations": {
            "A": "Loại A - (8, 13): Bẫy lấy tử và mẫu làm tọa độ (x, y).",
            "B": "Loại B - (0, 13): Lấy mẫu số làm giá trị y.",
            "C": "Loại C - (0, 8): Lấy tử số làm giá trị y.",
            "D": "ĐÁP ÁN ĐÚNG. D (0, 8/13): Thay x = 0 vào ta được y = (8/13)^1 = 8/13 => (0, 8/13)."
        },
        "pooe_breakdown": "• y-intercept luôn có x = 0 => Loại A.\n• y = (8/13)^(0+1) = 8/13 => Điểm (0, 8/13). Chọn D.",
        "mermaid_diagram": 'flowchart TD\n    A["Hàm số: y = (8/13)^(x + 1)"] --> B["Định nghĩa y-intercept: Thay x = 0"]\n    B --> C["y = (8/13)^(0 + 1) = (8/13)^1"]\n    C --> D["y = 8/13 => Tọa độ (0, 8/13)"]\n    D --> E["Chọn đáp án D"]'
    },

    95: { # M2 Q19 (Equivalent to (x)^(1/16) => 16th root of x)
        "tier1_hint": "Quy tắc lũy thừa với số mũ hữu tỉ: x^(1/n) tương đương với căn bậc mấy của x?",
        "tier2_hint": "Theo định nghĩa căn thức: x^(m/n) = căn bậc n của x^m. Khi m = 1 và n = 16, ta có x^(1/16) = căn bậc 16 của x (16th root of x).",
        "tier3_hint": "Áp dụng định nghĩa số mũ hữu tỉ: (x)^(1/16) = \u221b[16]{x} (căn bậc 16 của x).\nChốt đáp án chính xác: [B].",
        "strategic_tip": "Quy tắc 'Power over Root': x^(m/n) thì tử số m là số Mũ (Power), mẫu số n là Căn (Root). Mẫu số là 16 => Căn bậc 16.",
        "option_explanations": {
            "A": "Loại A - (1/16)x: Nhầm lũy thừa thành phép nhân hệ số.",
            "B": "ĐÁP ÁN ĐÚNG. B (\u221b[16]{x}): Đúng quy tắc chuyển đổi số mũ hữu tỉ thành căn bậc n.",
            "C": "Loại C - 16x: Nhầm lẫn phép toán.",
            "D": "Loại D - (x)^16: Nghịch đảo số mũ 1/16 thành 16."
        },
        "pooe_breakdown": "• x^(1/16) = căn bậc 16 của x. Chọn B.",
        "mermaid_diagram": 'flowchart TD\n    A["Biểu thức: (x)^(1/16)"] --> B["Quy tắc số mũ phân số: x^(1/n) = căn bậc n của x"]\n    B --> C["Ở đây n = 16 => Căn bậc 16 của x"]\n    C --> D["Chọn đáp án B"]'
    },

    96: { # M2 Q20 (Range of lemur groups: 16, 4, 19, 16, 17, 6)
        "tier1_hint": "Khoảng biến thiên (Range) của một tập dữ liệu trong thống kê được định nghĩa như thế nào?",
        "tier2_hint": "Range = Giá trị lớn nhất (Maximum) - Giá trị nhỏ nhất (Minimum). Hãy tìm số lớn nhất và số nhỏ nhất trong dãy: 16, 4, 19, 16, 17, 6.",
        "tier3_hint": "Bước 1: Sắp xếp dãy số tăng dần: 4, 6, 16, 16, 17, 19.\nBước 2: Giá trị lớn nhất là Max = 19; giá trị nhỏ nhất là Min = 4.\nBước 3: Range = 19 - 4 = 15.\nChốt đáp án chính xác: [15].",
        "strategic_tip": "Mẹo Desmos: Nhập L = [16, 4, 19, 16, 17, 6], sau đó gõ 'max(L) - min(L)', Desmos sẽ trả về kết quả 15 ngay lập tức.",
        "grid_in_explanation": {
            "correct_answer": "15",
            "solution_steps": "1. Tìm giá trị lớn nhất: Max = 19.\n2. Tìm giá trị nhỏ nhất: Min = 4.\n3. Range = Max - Min = 19 - 4 = 15.",
            "trap_errors": "Bẫy nhầm Range với Mean (trung bình cộng) hoặc Median (trung vị)."
        },
        "pooe_breakdown": "• Đáp án ĐÚNG: 15 - Hiệu giữa Max (19) và Min (4).",
        "mermaid_diagram": 'flowchart TD\n    A["Dãy số: 16, 4, 19, 16, 17, 6"] --> B["Xác định Max = 19 và Min = 4"]\n    B --> C["Công thức: Range = Max - Min"]\n    C --> D["Tính toán: 19 - 4 = 15"]\n    D --> E["Điền đáp án: 15"]'
    },

    97: { # M2 Q21 (Percent increase from $7 to $70 = 900%)
        "tier1_hint": "Công thức tính phần trăm tăng giá: Percent Increase = (Số tiền tăng / Giá gốc ban đầu) * 100%.",
        "tier2_hint": "• Số tiền tăng: 70 - 7 = 63 dollars.\n• Giá gốc ban đầu: 7 dollars.\n• Tính phần trăm: (63 / 7) * 100%.",
        "tier3_hint": "Bước 1: Lượng tăng = 70 - 7 = 63 dollars.\nBước 2: Tỉ lệ tăng = 63 / 7 = 9.\nBước 3: Đổi sang phần trăm: 9 * 100% = 900%.\nChốt đáp án chính xác: [D].",
        "strategic_tip": "BẪY TÂM LÝ KINH ĐIỂN: Rất nhiều học sinh chọn nhầm 90% hoặc 63%. Hãy nhớ: Giá tăng gấp 10 lần (từ 7 lên 70) thì lượng tăng là gấp 9 lần giá cũ => Tăng 900%, KHÔNG PHẢI 90%!",
        "option_explanations": {
            "A": "Loại A - (10%): Bẫy lấy 70/7 = 10 rồi chia 100.",
            "B": "Loại B - (63%): Bẫy lấy số tiền tăng tuyệt đối ($63) gán trực tiếp làm phần trăm.",
            "C": "Loại C - (90%): Bẫy nhầm lẫn số học do thiếu một chữ số 0 (9 * 100% = 900%).",
            "D": "ĐÁP ÁN ĐÚNG. D (900%): (70 - 7) / 7 * 100% = 63 / 7 * 100% = 900%."
        },
        "pooe_breakdown": "• Lượng tăng là 63$. Tỉ lệ so với giá gốc 7$ là 63/7 = 9 => 900%. Chọn D.",
        "mermaid_diagram": 'flowchart TD\n    A["Giá tăng từ 7$ lên 70$"] --> B["Số tiền tăng = 70 - 7 = 63$"]\n    B --> C["Tỉ lệ tăng so với giá ban đầu: 63 / 7 = 9"]\n    C --> D["Đổi sang phần trăm: 9 * 100% = 900%"]\n    D --> E["Chọn đáp án D: 900%"]'
    },

    98: { # M2 Q22 (System with infinitely many solutions)
        "tier1_hint": "Một hệ hai phương trình bậc nhất hai ẩn có vô số nghiệm (infinitely many solutions) khi hai phương trình thực chất là MỘT đường thẳng trùng nhau (hai phương trình tương đương và tỷ lệ với nhau).",
        "tier2_hint": "Điều kiện trùng nhau: a1/a2 = b1/b2 = c1/c2. Hãy kiểm tra xem trong 4 phương án, hệ nào có phương trình dưới là một bội số nhân của phương trình trên.",
        "tier3_hint": "Xét hệ C:\nPhương trình 1: x + 6y = 12.\nPhương trình 2: 4x + 24y = 48.\nChia cả hai vế của phương trình 2 cho 4 ta được: (4x + 24y) / 4 = 48 / 4 => x + 6y = 12.\nHai phương trình hoàn toàn trùng khớp, biểu diễn cùng một đường thẳng => Hệ có vô số nghiệm.\nChốt đáp án chính xác: [C].",
        "strategic_tip": "Mẹo kiểm tra tỷ lệ: Với hệ C, ta có 4/1 = 24/6 = 48/12 = 4 (tất cả các hệ số đều nhân với 4). Nếu tỷ lệ hệ số x và y bằng nhau nhưng khác tỷ lệ hằng số tự do thì hệ VÔ NGHIỆM (no solution - hai đường song song).",
        "option_explanations": {
            "A": "Loại A: 4x+6y=12 và 4x+24y=48 cắt nhau tại 1 nghiệm duy nhất.",
            "B": "Loại B: x+6y=12 và x+24y=48 cắt nhau tại 1 nghiệm duy nhất.",
            "C": "ĐÁP ÁN ĐÚNG. C: Nhân phương trình 1 với 4 ta được chính xác phương trình 2: 4(x + 6y) = 4(12) <=> 4x + 24y = 48 => Vô số nghiệm.",
            "D": "Loại D: Cắt nhau tại 1 nghiệm duy nhất."
        },
        "pooe_breakdown": "• Xét hệ C: Nhân phương trình 1 với 4 ra đúng phương trình 2 => Trùng nhau => Vô số nghiệm. Chọn C.",
        "mermaid_diagram": 'flowchart TD\n    A["Hệ có vô số nghiệm <=> Hai đường thẳng trùng nhau"] --> B["Kiểm tra tỷ lệ hệ số: a1/a2 = b1/b2 = c1/c2"]\n    B --> C["Hệ C: 4/1 = 24/6 = 48/12 = 4 (Tỷ lệ 1:4 hoàn hảo)"]\n    C --> D["Phương trình 2 gấp đúng 4 lần phương trình 1"]\n    D --> E["Kết luận: Vô số nghiệm => Chọn đáp án C"]'
    }
}
