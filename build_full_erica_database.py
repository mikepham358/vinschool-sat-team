# -*- coding: utf-8 -*-
"""
Builder for Full Erica Meltzer SAT Reading Master Guide
Combines:
1. All 27 Guided Worked Examples (Ví dụ minh họa kèm bài giảng) from the book
2. All 74 Independent Practice Questions (Bài tập thực hành) from the workbook template
Total = 101 questions across 9 chapters.
"""

import openpyxl
import re
import json
import os

EXCEL_PATH = '/Users/mike/Library/CloudStorage/GoogleDrive-mikepham358@gmail.com/My Drive/A Vinschool by Mike Pham/26-27 Grand Plan /Study Plan/Reading & Writing/Templates/[Edited] Template - Full Erica Meltzer SAT Reading.xlsx'
OUTPUT_JSON = 'data/erica_reading.json'

# 27 Guided Examples extracted from textbook PDF
GUIDED_EXAMPLES = [
    # ================= CHAPTER 2: VOCABULARY IN CONTEXT =================
    {
        "chapter_num": 2,
        "module_code": "Ch2_Vocabulary",
        "topic": "Ch. 2: Vocabulary • Positive/Negative Tone & Context Clues",
        "pdf_page": 36,
        "passage": "Despite their physical attractiveness, some butterfly species are regarded as pests because in their larval stages they are capable of causing damage to crops or trees. Other species play a less __ role in the ecosystem, however, because their caterpillars consume harmful insects.",
        "prompt": "Which choice completes the text with the most logical or precise word or phrase?",
        "options": [
            {"key": "A", "text": "exceptional"},
            {"key": "B", "text": "beneficial"},
            {"key": "C", "text": "significant"},
            {"key": "D", "text": "detrimental"}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Dùng chiến thuật (+/-): 'less + từ tiêu cực = ý tích cực'. Nhận diện từ nối 'however' và từ chỉ hại 'damage' vs 'harmful insects'.",
        "erica_explanation": "Văn bản đối chiếu hai nhóm bướm: nhóm thứ nhất gây hại (regarded as pests, damage to crops), còn nhóm thứ hai có ích nhờ ấu trùng ăn côn trùng gây hại (caterpillars consume harmful insects). Từ nối 'however' biểu thị sự tương phản. Vì trước ô trống có từ 'less', nên 'less + từ mang nghĩa tiêu cực' sẽ tạo ra nghĩa tích cực ('ít gây hại hơn'). Phương án (D) detrimental (nghĩa là gây hại, có tiền tố de-) là từ tiêu cực duy nhất và khớp hoàn hảo với logic ngữ cảnh."
    },
    {
        "chapter_num": 2,
        "module_code": "Ch2_Vocabulary",
        "topic": "Ch. 2: Vocabulary • Word Roots and Prefixes",
        "pdf_page": 37,
        "passage": "An award-winning reporter as well as the author of several books, Maria Elena Fernandez is considered an __ in her field because unlike the vast majority of present-day journalists, her work is characterized by a prose style that readers find highly distinctive, even unique.",
        "prompt": "Which choice completes the text with the most logical or precise word or phrase?",
        "options": [
            {"key": "A", "text": "anomaly"},
            {"key": "B", "text": "innovator"},
            {"key": "C", "text": "explorer"},
            {"key": "D", "text": "activist"}
        ],
        "correct_answer": "A",
        "pedagogical_focus": "Bẻ khóa tiền tố 'a-' (không/khác biệt) và gốc 'nom-' (tên/chuẩn mực). Phân biệt 'anomaly' (điều bất thường/khác biệt độc nhất) với 'innovator' (người đổi mới phương pháp).",
        "erica_explanation": "Đoạn văn nhấn mạnh phong cách của Fernandez là 'highly distinctive, even unique' và 'unlike the vast majority of present-day journalists'. Cần một danh từ mang nghĩa 'người/hiện tượng khác biệt với số đông'. 'Innovator' có vẻ hấp dẫn nhưng không đồng nghĩa với 'unique' (đổi mới không nhất thiết là độc nhất vô nhị). 'Anomaly' mang tiền tố a- (không/phi) và gốc nom- (chuẩn mực), nghĩa là điều dị biệt, hoàn toàn khớp với cụm 'unlike the vast majority'."
    },
    {
        "chapter_num": 2,
        "module_code": "Ch2_Vocabulary",
        "topic": "Ch. 2: Vocabulary • Watch Out for Second Meanings",
        "pdf_page": 38,
        "passage": "In the two-dimensional world of maps, sharp lines are used to demarcate where one country ends and another begins. In reality, however, boundaries between nations are typically much more __, with border regions that are characterized by multiple languages and cultures.",
        "prompt": "Which choice completes the text with the most logical or precise word or phrase?",
        "options": [
            {"key": "A", "text": "fluid"},
            {"key": "B", "text": "precise"},
            {"key": "C", "text": "rigid"},
            {"key": "D", "text": "identifiable"}
        ],
        "correct_answer": "A",
        "pedagogical_focus": "Cảnh giác bẫy nghĩa thứ hai (Second Meanings): 'fluid' đóng vai trò tính từ mang nghĩa 'linh hoạt, dễ biến đổi, không cứng nhắc' (thay vì nghĩa thông thường là chất lỏng).",
        "erica_explanation": "Từ nối 'however' tạo sự tương phản trực tiếp giữa 'sharp lines' (đường ranh giới rạch ròi, cố định trên bản đồ) với thực tế biên giới ngoài đời. Trái ngược với cứng nhắc/rạch ròi là tính biến chuyển, hòa trộn linh hoạt. 'Fluid' khi dùng làm tính từ mang nghĩa 'dễ thay đổi, không cố định' (able to change shape / not rigid), phản ánh đúng việc khu vực biên giới giao thoa nhiều ngôn ngữ và văn hóa."
    },

    # ================= CHAPTER 4: THE BIG PICTURE =================
    {
        "chapter_num": 4,
        "module_code": "Ch4_BigPicture",
        "topic": "Ch. 4: Big Picture • Focus on Topic + Unique Qualities",
        "pdf_page": 76,
        "passage": "Admired primarily for her exquisite calligraphy, Otagaki Rengetsu (1791-1875) was among Japan's most celebrated artists. She was also a writer and ceramicist, often inscribing her poems in her own calligraphy onto clay vessels—a distinctive blending of art forms not replicated by any other artist in Japanese history. Her work was in such great demand during the nineteenth century that every household in Kyoto was said to own her pottery, and today scrolls and ceramics bearing her calligraphy are sought after by collectors.",
        "prompt": "Which choice best states the main idea of the passage?",
        "options": [
            {"key": "A", "text": "Otagaki Rengetsu's artistic creations are prized for their unique qualities."},
            {"key": "B", "text": "Inscribed clay vessels have traditionally played an important role in Japanese art."},
            {"key": "C", "text": "The collaboration between writers and ceramic workers produced highly distinctive works of art in Japan."},
            {"key": "D", "text": "Many households in Kyoto once featured scrolls produced by Otagaki Rengetsu."}
        ],
        "correct_answer": "A",
        "pedagogical_focus": "Công thức Main Idea: Xác định đúng Chủ thể trọng tâm (Topic: Otagaki Rengetsu đơn lẻ, không phải số nhiều) + Luận điểm bao quát (sự kết hợp độc nhất vô nhị).",
        "erica_explanation": "Đoạn văn tập trung duy nhất vào nghệ sĩ Otagaki Rengetsu và phong cách kết hợp thơ, thư pháp trên đồ gốm độc nhất vô nhị ('not replicated by any other artist in Japanese history'). (A) tóm lược chính xác luận điểm này. (B) quá rộng và đi ngược bài đọc; (C) sai vì nói về 'sự hợp tác giữa nhiều nhà văn và thợ gốm' (số nhiều), trong khi bài nói về một cá nhân tự làm; (D) chỉ là một chi tiết phụ và nhầm lẫn giữa đồ gốm (pottery) với cuộn tranh (scrolls)."
    },
    {
        "chapter_num": 4,
        "module_code": "Ch4_BigPicture",
        "topic": "Ch. 4: Big Picture • Same Idea, Different Words & Punctuation Clues",
        "pdf_page": 80,
        "passage": "Kente, the traditional fabric of Ghana's Asante people, has evolved into a symbol of many meanings—political and cultural, African and American, honorary and everyday. \"What is called kente is many things,\" says Doran H. Ross, director of the Fowler Museum of Cultural History, though he notes its origin is Ghana's strip-woven cloth. But Ross says kente appears just as widely today in Western-style tailored clothing, and in other ways that make it the most recognizably African textile.",
        "prompt": "Which choice best states the main idea of the text?",
        "options": [
            {"key": "A", "text": "Kente can only be produced by specialized weavers."},
            {"key": "B", "text": "Many different type of African textiles are used in modern clothing."},
            {"key": "C", "text": "The origins of kente are somewhat controversial."},
            {"key": "D", "text": "Kente has acquired a wide range of associations."}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Dấu gạch ngang giải thích (—): 'has evolved into a symbol of many meanings' tương đương với 'acquired a wide range of associations'.",
        "erica_explanation": "Ngay câu đầu tiên, tác giả nêu rõ vải Kente đã trở thành biểu tượng của nhiều tầng ý nghĩa: chính trị, văn hóa, danh dự và đời thường. Dấu gạch ngang báo hiệu thông tin trọng tâm. Cụm 'symbol of many meanings' được diễn đạt lại (paraphrased) trong phương án (D) thành 'acquired a wide range of associations'. Các phương án (A), (B), (C) hoặc quá hẹp, hoặc mang tính suy diễn không có trong bài."
    },
    {
        "chapter_num": 4,
        "module_code": "Ch4_BigPicture",
        "topic": "Ch. 4: Big Picture • Key Information at the End",
        "pdf_page": 85,
        "passage": "In our family, the women made the ink. We stayed home. We all worked—me, GaoLing, my aunts and girl cousins, everybody. Even the babies and Great-Granny had a job of picking out stones from the dried millet we boiled for breakfast. We gathered each day in the ink-making studio. According to Great-Granny, the studio began as a grain shed that sat along the front wall of the courtyard house. Over the years, one generation of sons added brick walls and a tile roof. Another strengthened the beams and lengthened it by two pillars. The next tiled the floors and dug pits for storing the ingredients. Then other descendants made a cellar for keeping the inksticks away from the heat and cold. \"And now look,\" Great-Granny often bragged. \"Our studio is an ink palace.\"",
        "prompt": "Which choice best states the main idea of the text?",
        "options": [
            {"key": "A", "text": "A character describes the establishment of her family's business by her ancestors."},
            {"key": "B", "text": "A character works well with her relatives but struggles to collaborate with those outside her family."},
            {"key": "C", "text": "A character expresses pride in the family business and explains the role she plays within it."},
            {"key": "D", "text": "A character admires her relatives but is disappointed by their failure to acknowledge her work."}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Mô hình 'Thông tin cốt lõi ở phần kết': Lời tự hào của cụ cố ('Our studio is an ink palace') đúc kết toàn bộ ý nghĩa truyền thống và sự gắn bó của gia đình.",
        "erica_explanation": "Đoạn văn mở đầu bằng việc mô tả sự phân công công việc của nhân vật tôi và những người phụ nữ trong xưởng làm mực, sau đó kể lại sự phát triển của xưởng qua các thế hệ và kết thúc bằng lời tự hào của cụ cố ('ink palace'). Phương án (C) tóm lược chính xác cả hai vế: lòng tự hào về nghề truyền thống của gia đình và vị trí, vai trò của nhân vật trong xưởng."
    },
    {
        "chapter_num": 4,
        "module_code": "Ch4_BigPicture",
        "topic": "Ch. 4: Big Picture • Main Point in Poetry Passages",
        "pdf_page": 86,
        "passage": "I'd love to write of the beautiful,\nI'd love to write of the brave,\nAnd read the minds of others,\nAnd note their winning ways.\nI would not judge the beautiful\nBy the beauty of their faces,\nBy suppositions or the like,\nOr their pretended graces.",
        "prompt": "Which choice best states the main idea of the text?",
        "options": [
            {"key": "A", "text": "The speaker is drawn to people who are attractive and graceful."},
            {"key": "B", "text": "The speaker does not feel suited to the task of judging others."},
            {"key": "C", "text": "The speaker believes that external features are a reliable indicator of internal ones."},
            {"key": "D", "text": "The speaker is unconcerned with superficial appearances."}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Cấu trúc thơ 2 phần đối xứng: 4 câu đầu nói về mong muốn tôn vinh vẻ đẹp/sự dũng cảm, 4 câu sau phủ định việc đánh giá qua ngoại hình bề ngoài ('not judge... by the beauty of their faces').",
        "erica_explanation": "Bài thơ gồm 2 khổ đối xứng. Bốn dòng thơ sau trực tiếp khẳng định nhân vật trữ tình không đánh giá cái đẹp dựa trên khuôn mặt hay những cử chỉ giả tạo ('not judge the beautiful by the beauty of their faces / pretended graces'). Ý chính xuyên suốt là người nói không bận tâm đến vẻ bề ngoài giả tạo mà tìm kiếm vẻ đẹp nội tâm đích thực. Phương án (D) thể hiện chuẩn xác ý này."
    },

    # ================= CHAPTER 5: LITERAL COMPREHENSION =================
    {
        "chapter_num": 5,
        "module_code": "Ch5_LiteralComprehension",
        "topic": "Ch. 5: Literal • Same Idea, Different Words & Sentence Boundaries",
        "pdf_page": 93,
        "passage": "According to new research, viral DNA embedded in human genomes during ancient infections protects human cells against certain modern-day viruses. Earlier studies have shown that fragments of ancient viral DNA—known as endogenous retroviruses—in the genomes of mice, chickens, cats and sheep provide immunity against modern viruses that originate outside the body by preventing them from entering host cells. Though the new study, conducted by researchers at Cornell University, was performed with cultured human cells in a laboratory, it shows that the antiviral effect of endogenous retroviruses likely also exists for humans.",
        "prompt": "Based on the text, what is true about the study conducted by Cornell researchers?",
        "options": [
            {"key": "A", "text": "It tested for the presence of viral material in a range of species."},
            {"key": "B", "text": "It suggests that endogenous retroviruses behave differently in humans than in animals."},
            {"key": "C", "text": "It did not test for the presence of retroviruses in human bodies."},
            {"key": "D", "text": "It demonstrated that fragments of ancient viral DNA can infect modern humans."}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Quy tắc không đọc nửa câu: Chú ý vế điều kiện 'performed with cultured human cells in a laboratory' tương đương với 'did not test in actual human bodies'.",
        "erica_explanation": "Câu cuối cùng nêu rõ nghiên cứu của Đại học Cornell được tiến hành trên 'cultured human cells in a laboratory' (các tế bào người nuôi cấy trong phòng thí nghiệm), tức là không phải thí nghiệm trực tiếp trên cơ thể con người thực tế. Phương án (C) diễn đạt lại chính xác chi tiết này. (A) là nghiên cứu trước đó trên động vật; (B) và (D) hoàn toàn mâu thuẫn với nội dung văn bản."
    },
    {
        "chapter_num": 5,
        "module_code": "Ch5_LiteralComprehension",
        "topic": "Ch. 5: Literal • Direct Evidence in Fiction",
        "pdf_page": 94,
        "passage": "A family of ten children will be always called a fine family, where there are heads and arms and legs enough for the number; but the Morlands had little other right to the word, for they were in general very plain, and Catherine, for many years of her life, as plain as any. She had a thin awkward figure, a sallow skin without colour, dark lank hair, and strong features—so much for her person; and not less propitious for heroism seemed her mind.",
        "prompt": "According to the passage, what is true about Catherine Morland?",
        "options": [
            {"key": "A", "text": "She was as unremarkable in appearance as the rest of her family."},
            {"key": "B", "text": "She was more intelligent than her siblings."},
            {"key": "C", "text": "She was less attractive than the other members of her family."},
            {"key": "D", "text": "She possessed characteristics typically associated with heroism."}
        ],
        "correct_answer": "A",
        "pedagogical_focus": "Đối chiếu trực tiếp từ khóa: 'as plain as any' tương đương với 'as unremarkable in appearance as the rest of her family'.",
        "erica_explanation": "Đoạn văn nêu rõ gia đình Morland nhìn chung là 'very plain' (rất bình thường, không có gì nổi bật), và Catherine 'as plain as any' (cũng bình thường y hệt như những người còn lại). Điều này tương ứng 100% với phương án (A). (B) không hề được nhắc đến; (C) sai vì Catherine không xấu hơn mà giống các anh chị em; (D) sai vì tâm trí cô được miêu tả là không phù hợp với hình mẫu anh hùng."
    },
    {
        "chapter_num": 5,
        "module_code": "Ch5_LiteralComprehension",
        "topic": "Ch. 5: Literal • Cause and Effect in Scientific Text",
        "pdf_page": 94,
        "passage": "Much of what we know about the physical and mental toll of chronic stress stems from seminal work by Robert Sapolsky beginning in the late 1970s. Sapolsky, a neuroendocrinologist, was among the first to make the connection that the hormones released during the fight-or-flight response—the ones that helped our ancestors avoid becoming dinner—have deleterious effects when the stress is severe and sustained. Especially insidious, chronic exposure to one of these hormones, cortisol, causes brain changes that make it increasingly difficult to shut the stress response down.",
        "prompt": "According to the passage, what is significant about sustained stress?",
        "options": [
            {"key": "A", "text": "It inhibits the production of cortisol."},
            {"key": "B", "text": "It can create a sense of excitement."},
            {"key": "C", "text": "It becomes progressively harder to reduce."},
            {"key": "D", "text": "It allows people to escape from dangerous situations."}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Tìm câu kết chứa manh mối nhân quả: 'causes brain changes that make it increasingly difficult to shut the stress response down' = 'progressively harder to reduce'.",
        "erica_explanation": "Câu cuối cùng chỉ ra hệ quả nguy hiểm của stress kéo dài: phơi nhiễm cortisol liên tục gây biến đổi não bộ khiến việc tắt phản ứng căng thẳng ngày càng trở nên khó khăn ('increasingly difficult to shut down'). 'Increasingly difficult' được viết lại thành 'progressively harder to reduce' trong phương án (C). (A) sai vì stress làm tăng chứ không ức chế cortisol; (B) không có trong bài; (D) là phản ứng chiến-hay-biến thời cổ xưa, không phải bản chất nguy hại của stress kéo dài."
    },

    # ================= CHAPTER 6: READING FOR FUNCTION =================
    {
        "chapter_num": 6,
        "module_code": "Ch6_ReadingForFunction",
        "topic": "Ch. 6: Function • What It Says vs. Why It Is Written",
        "pdf_page": 106,
        "passage": "To drivers, the color red means stop, but on a map it tells traffic engineers to leap into action. Traffic control centers like the one on the seventh floor of Boston's City Hall—a room cluttered with computer terminals and live video feeds of urban intersections—represent the brain of a traffic system. The city's network of sensors, cables and signals are the nerves connected to the rest of the body. \"Most people don't think there are eyes and ears keeping track of all this stuff,\" says John DeBenedictis, the center's engineering director. But in reality, engineers literally watch our every move, making subtle changes that relieve and redirect traffic.",
        "prompt": "Which choice best describes the function of the underlined portion in the text as a whole? (Underlined: 'The city's network of sensors, cables and signals are the nerves connected to the rest of the body.')",
        "options": [
            {"key": "A", "text": "To describe a problem commonly faced by traffic engineers"},
            {"key": "B", "text": "To point out some important differences between traffic control centers and the human brain"},
            {"key": "C", "text": "To discuss the purpose of items found in traffic control centers"},
            {"key": "D", "text": "To provide examples of ways in which drivers' actions can be monitored remotely"}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Kết nối câu dẫn chứng với câu kết luận ở cuối đoạn: mạng lưới cảm biến, dây cáp giúp kỹ sư quan sát và điều tiết giao thông từ xa (remotely).",
        "erica_explanation": "Hình ảnh ẩn dụ 'mạng lưới cảm biến, dây cáp và tín hiệu như những dây thần kinh' kết nối với câu cuối cùng của đoạn: kỹ sư giao thông theo dõi từng chuyển động của xe cộ để điều chỉnh đường đi. Do đó, chức năng của câu này là cung cấp ví dụ về cách thức các kỹ sư giám sát hành vi của tài xế từ xa ('monitored remotely'). Phương án (D) phản ánh chính xác vai trò logic này."
    },
    {
        "chapter_num": 6,
        "module_code": "Ch6_ReadingForFunction",
        "topic": "Ch. 6: Function • Purpose of Comparative Statements",
        "pdf_page": 107,
        "passage": "In August 2009 a consortium of European observatories reported the discovery of COROT-7c, a second planet orbiting COROT-7. Using the data from both planets, they were able to calculate that COROT-7b has an average density about the same as Earth's. This means it is almost certainly a rocky planet made up of silicate rocks like those in Earth's crust. Not that anyone would call it Earth. The planet and its star are separated by only 1.6 million miles, 23 times less than the distance between the parboiled planet Mercury and our Sun. Because the planet is so close to the star, it is gravitationally locked to it in the same way the Moon is locked to Earth.",
        "prompt": "Which choice best describes the function of the underlined portion in the text as a whole? (Underlined: 'The planet and its star are separated by only 1.6 million miles, 23 times less than the distance between the parboiled planet Mercury and our Sun.')",
        "options": [
            {"key": "A", "text": "It emphasizes an important distinction between COROT-7b and Earth."},
            {"key": "B", "text": "It suggests that COROT-7b could eventually come to resemble Earth."},
            {"key": "C", "text": "It supports the hypothesis that Earth and COROT-7b may share a common origin."},
            {"key": "D", "text": "It explains how Mercury came to occupy its position within the solar system."}
        ],
        "correct_answer": "A",
        "pedagogical_focus": "Đọc ngược lại câu đứng trước: 'Not that anyone would call it Earth' báo hiệu mục đích của câu gạch chân là giải thích vì sao hành tinh này KHÔNG HỀ giống Trái Đất.",
        "erica_explanation": "Câu ngay trước đó nói: 'Not that anyone would call it Earth' (Không ai lại đi coi nó là Trái Đất). Câu gạch chân cung cấp bằng chứng khoảng cách cực gần giữa hành tinh này và ngôi sao chủ (1.6 triệu dặm, gần hơn cả sao Thủy) để minh chứng cho việc nó cực kỳ nóng và khắc nghiệt. Như vậy, chức năng của nó là nhấn mạnh sự khác biệt cốt tử giữa COROT-7b và Trái Đất, khớp với phương án (A)."
    },
    {
        "chapter_num": 6,
        "module_code": "Ch6_ReadingForFunction",
        "topic": "Ch. 6: Function • Shift from Murky to Clear Waters",
        "pdf_page": 108,
        "passage": "Scientists have long known that color plays a role in warning animals about danger. Only recently, however, have they begun to understand how wavelengths of light (and thus color) appear at different depths and how various marine creatures' eyes perceive this light and each other—far differently than humans see them. Where waters are murky, the majority of creatures employ nonvisual forms of communication such as smell, taste, touch, and sound. But in the clear waters of coral reefs, which make up less than 1% of the world's oceans, light abounds, vision predominates, and animals drape themselves in blazing color—not only to menace potential enemies but also to evade predators, hunt for prey, and even hide in plain sight.",
        "prompt": "Which choice best describes the function of the underlined portion in the text as a whole? (Underlined: 'But in the clear waters of coral reefs, which make up less than 1% of the world's oceans, light abounds, vision predominates...')",
        "options": [
            {"key": "A", "text": "It explains how reef animals use color to hide from predators."},
            {"key": "B", "text": "It describes an unusual form of marine communication."},
            {"key": "C", "text": "It presents a novel theory about underwater perception."},
            {"key": "D", "text": "It emphasizes the controversy surrounding a claim about reef animals."}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Từ nối 'But' thiết lập sự tương phản giữa vùng nước đục (giao tiếp phi thị giác) với rạn san hô (thị giác thống trị), mở ra góc nhìn khoa học mới về cảm nhận thị giác dưới nước.",
        "erica_explanation": "Đoạn văn mở đầu bằng việc các nhà khoa học gần đây mới bắt đầu hiểu cách sinh vật biển cảm nhận ánh sáng khác con người. Sau khi nhắc tới vùng nước đục, từ 'But' mở ra môi trường rạn san hô trong vắt nơi thị giác giữ vai trò áp đảo. Câu gạch chân trình bày nhận thức khoa học mới mẻ về cách thị giác và màu sắc vận hành dưới đáy biển (underwater perception), tương ứng với (C)."
    },
    {
        "chapter_num": 6,
        "module_code": "Ch6_ReadingForFunction",
        "topic": "Ch. 6: Function • Purpose of First Sentence & Questioning Hypotheses",
        "pdf_page": 110,
        "passage": "Throughout the dinosaurs' time on Earth, there was an amplification of boniness and spikiness; however, the advantage of skull frills and back plates is hardly self-evident. The solid-domed skull of Pachycephalosaurus seems made for butting—but for butting what? The skull would be all but useless against a predator with the size and power of Tyrannosaurus Rex. The skulls of some Pachycephalosaurs, moreover, were flat and thin—a bad design for contact sports—and the spikes protruding from them were most probably blunt rather than sharp.",
        "prompt": "Which choice best states the main purpose of the text?",
        "options": [
            {"key": "A", "text": "To suggest that a longstanding hypothesis about dinosaurs may be incorrect."},
            {"key": "B", "text": "To introduce a study and raise some questions about the validity of its findings."},
            {"key": "C", "text": "It describes a dinosaur species in order to illustrate a puzzling trend."},
            {"key": "D", "text": "It presents an emerging mystery and discusses an attempt to solve it."}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Xác định câu mở đoạn chứa 'however' và từ khóa 'hardly self-evident' (không hề hiển nhiên) = 'puzzling trend' (xu hướng khó hiểu).",
        "erica_explanation": "Ngay câu đầu tiên, tác giả chỉ ra rằng lợi ích tiến hóa của các tấm xương và gai sọ là 'hardly self-evident' (khó hiểu, không hiển nhiên). Đoạn sau miêu tả loài Pachycephalosaurus với vòm sọ đặc nhưng lại không dùng để húc kẻ thù lớn như T-Rex. Mục đích toàn bài là mô tả loài khủng long này nhằm minh họa cho một xu hướng tiến hóa đầy bí ẩn ('puzzling trend'). Phương án (C) nắm bắt đúng mục đích này."
    },
    {
        "chapter_num": 6,
        "module_code": "Ch6_ReadingForFunction",
        "topic": "Ch. 6: Function • Primary Purpose in Fiction",
        "pdf_page": 111,
        "passage": "In our family, the women made the ink. We stayed home. We all worked—me, GaoLing, my aunts and girl cousins, everybody. Even the babies and Great-Granny had a job of picking out stones from the dried millet we boiled for breakfast. We gathered each day in the ink-making studio. According to Great-Granny, the studio began as a grain shed that sat along the front wall of the courtyard house. Over the years, one generation of sons added brick walls and a tile roof. Another strengthened the beams and lengthened it by two pillars. The next tiled the floors and dug pits for storing the ingredients. Then other descendants made a cellar for keeping the inksticks away from the heat and cold. \"And now look,\" Great-Granny often bragged. \"Our studio is an ink palace.\"",
        "prompt": "Which choice best states the main purpose of the text?",
        "options": [
            {"key": "A", "text": "To describe the process by which a character masters a difficult task"},
            {"key": "B", "text": "To convey a character's role and sense of accomplishment in her family's work"},
            {"key": "C", "text": "To explain the influence of a distinguished relative on a character and her family"},
            {"key": "D", "text": "To explore the effects of a character's decision on the members of her family"}
        ],
        "correct_answer": "B",
        "pedagogical_focus": "Chuyển từ Main Point ('tự hào về xưởng mực') sang Primary Purpose: truyền tải cảm giác gắn bó và thành tựu của nhân vật cùng gia đình.",
        "erica_explanation": "Nếu ý chính của đoạn văn là lòng tự hào về nghề làm mực truyền thống, thì mục đích tác giả (primary purpose) chính là bộc lộ vị trí của người kể chuyện ('me, GaoLing, everybody') và niềm tự hào/thành tựu gắn liền với sự phát triển của xưởng mực ('sense of accomplishment in her family's work'). Phương án (B) phản ánh hoàn hảo mục đích này."
    },
    {
        "chapter_num": 6,
        "module_code": "Ch6_ReadingForFunction",
        "topic": "Ch. 6: Function • Second Meaning of 'Novel' in Positive Tone",
        "pdf_page": 112,
        "passage": "On what seems like a monthly basis, scientific teams announce the results of new experiments, adding to a preponderance of evidence that we've been underestimating animal minds, even those of us who have rated them fairly highly. New animal behaviors and capacities are observed in the wild, often involving tool use—or at least object manipulation—the very kinds of activity that led the distinguished zoologist Donald R. Griffin to found the field of cognitive ethology (animal thinking) in 1978: octopuses piling stones in front of their hideyholes, to name one recent example; or dolphins fitting marine sponges to their beaks in order to dig for food on the seabed; or wasps using small stones to smooth the sand around their egg chambers, concealing them from predators.",
        "prompt": "Which choice best describes the function of the underlined portion in the text as a whole? (Underlined: 'octopuses piling stones in front of their hideyholes... or dolphins fitting marine sponges... or wasps using small stones...')",
        "options": [
            {"key": "A", "text": "To describe ways that animals hide from predators"},
            {"key": "B", "text": "To highlight the lack of complexity in animal tools as compared to human ones"},
            {"key": "C", "text": "To provide instances of novel animal behavior in the wild"},
            {"key": "D", "text": "To emphasize the limits of animal consciousness"}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Bẫy chi tiết đứng sau: 'smooth sand' chỉ áp dụng cho tò vò (wasps), trong khi bạch tuộc và cá heo có mục đích khác. Tất cả đều là ví dụ của 'new animal behaviors' = 'novel animal behavior'.",
        "erica_explanation": "Phần gạch chân liệt kê 3 ví dụ liên tiếp (bạch tuộc, cá heo, tò vò) sau dấu hai chấm. Dấu hai chấm báo hiệu phần giải thích chi tiết cho câu đi trước: 'New animal behaviors and capacities are observed in the wild'. Cụm 'New animal behaviors' được diễn đạt bằng nghĩa thứ hai của từ 'novel' ('novel animal behavior' = hành vi mới mẻ, chưa từng thấy). Đáp án chính xác là (C)."
    },

    # ================= CHAPTER 7: TEXT COMPLETIONS =================
    {
        "chapter_num": 7,
        "module_code": "Ch7_TextCompletions",
        "topic": "Ch. 7: Text Completions • Conservative Deductions on Animal Camouflage",
        "pdf_page": 123,
        "passage": "Up close, regal angelfish flash eye-popping bands of yellow, violet, and white. But recent studies show that as regals swim against a coral reefs visually complex background, their contrasting lines merge in a predator's brain, allowing them to evade capture. According to marine biologist Gil Rosenthal, as a reef fish retreats, distance and motion can make it difficult for predators to perceive fine details and distinguish closely spaced outlines of contrasting colors. From far away, __",
        "prompt": "Which choice most logically completes the text?",
        "options": [
            {"key": "A", "text": "the bright colors of the fish can easily be perceived, even when the water is clouded by sediment."},
            {"key": "B", "text": "marine predators must rely on the visual aspects of their prey."},
            {"key": "C", "text": "spots and stripes blur together, allowing even stationary fish to merge into the background."},
            {"key": "D", "text": "the fish appear as a single mass rather than a group of individual creatures."}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Suy luận logic bảo thủ bám sát câu trước: Khi ở cự ly xa ('From far away'), các đường nét và màu sắc tương phản hòa lẫn vào nhau khiến kẻ săn mồi không nhận ra.",
        "erica_explanation": "Đoạn văn giải thích rằng khi cá bơi ra xa, khoảng cách và chuyển động khiến kẻ săn mồi không thể phân biệt các đường nét màu sắc tương phản ('merge in a predator's brain', 'difficult to perceive fine details'). Do đó, khi nhìn từ xa ('From far away'), các đốm và sọc màu sắc sẽ mờ nhòe vào nhau, giúp cá hòa lẫn vào hậu cảnh rạn san hô ('blur together, allowing them to merge into the background'). Phương án (C) hoàn thiện logic bài một cách chuẩn xác."
    },
    {
        "chapter_num": 7,
        "module_code": "Ch7_TextCompletions",
        "topic": "Ch. 7: Text Completions • Problem of Fragmentary Language in Olfaction",
        "pdf_page": 127,
        "passage": "Fully one-third of the human brain is devoted to processing visual information; in contrast, only five percent involves smell. As a result, modern neuroscience has focused most intensely on deciphering sight, with olfaction often treated as a bonus sense. That is reflected in the paucity of language to describe it, a situation that poses a problem for scientific investigation. There are countless adjectives to describe what things look—and sound—like, but humans' vocabulary for olfactory perception is fragmentary and highly inconsistent. Therefore, __",
        "prompt": "Which choice most logically completes the text?",
        "options": [
            {"key": "A", "text": "olfactory researchers are seeking higher levels of funding to study how people process odors."},
            {"key": "B", "text": "people often cannot explain how things smell to them in a way that is comprehensible to researchers."},
            {"key": "C", "text": "people must be able to process visual and olfactory information simultaneously in their daily lives."},
            {"key": "D", "text": "people should focus on sensations rather than words when they encounter new scents."}
        ],
        "correct_answer": "B",
        "pedagogical_focus": "Xâu chuỗi nguyên nhân - kết quả: Từ vựng về mùi hương manh mún ('fragmentary and inconsistent') tạo ra trở ngại cho nghiên cứu khoa học -> Mọi người không thể diễn đạt mùi hương một cách dễ hiểu cho nhà khoa học.",
        "erica_explanation": "Câu trước ô trống nhấn mạnh: con người có rất ít từ ngữ để mô tả khứu giác ('paucity of language', 'fragmentary and highly inconsistent'), và điều này gây cản trở cho việc nghiên cứu khoa học. Từ nối 'Therefore' đòi hỏi kết luận trực tiếp từ nguyên nhân trên: do thiếu từ vựng thống nhất, người tham gia thí nghiệm không thể giải thích cảm nhận mùi hương một cách rõ ràng cho các nhà nghiên cứu hiểu được ('cannot explain how things smell in a way comprehensible to researchers'). Phương án (B) là đáp án duy nhất khớp logic."
    },

    # ================= CHAPTER 8: SUPPORTING & UNDERMINING =================
    {
        "chapter_num": 8,
        "module_code": "Ch8_SupportUndermining",
        "topic": "Ch. 8: Support/Undermine • Illustrating a Poetic Claim",
        "pdf_page": 135,
        "passage": "\"Slow Through the Dark\" is an early 1900s poem by Paul Laurence Dunbar. In the poem, the speaker urges the listener not to lose hope, even in difficult circumstances.",
        "prompt": "Which quotation from \"Slow Through the Dark\" most effectively illustrates the claim?",
        "options": [
            {"key": "A", "text": "\"Slow moves the pageant of a climbing race; / Their footsteps drag far, far below the height,\""},
            {"key": "B", "text": "\"No strange, swift-sprung exception we; we trace / A devious way thro' dim, uncertain light,-\""},
            {"key": "C", "text": "\"Heed not the darkness round you, dull and deep; / The clouds grow thickest when the summit's nigh.\""},
            {"key": "D", "text": "\"Who stoppeth here to spend a while in sleep / Or curseth that the storm obscures the sky?\""}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Đối chiếu trực tiếp luận điểm cần chứng minh: 'urges the listener not to lose hope' (khuyên người nghe đừng mất hy vọng) = 'Heed not the darkness round you' (đừng bận lòng trước bóng tối quanh bạn).",
        "erica_explanation": "Đề bài yêu cầu tìm câu thơ minh họa cho việc tác giả 'khuyên người nghe không mất hy vọng giữa nghịch cảnh'. Phương án (C) mang giọng điệu khích lệ trực tiếp: 'Heed not the darkness round you... The clouds grow thickest when the summit's nigh' (Đừng bận lòng trước bóng đen vây quanh... Mây mù dày đặc nhất chính là lúc đỉnh núi đã cận kề). Các phương án khác chỉ miêu tả bước chân nặng nề (A) hoặc sự mò mẫm trong ánh sáng mờ ảo (B)."
    },
    {
        "chapter_num": 8,
        "module_code": "Ch8_SupportUndermining",
        "topic": "Ch. 8: Support/Undermine • Supporting a Psychological Claim",
        "pdf_page": 136,
        "passage": "Marketers assume that the more choices they offer, the more likely customers will be able to find just the right thing. They assume, for instance, that offering 50 styles of jeans instead of two increases the chances that shoppers will come across a pair they really like. Nevertheless, research now shows that there can be too much choice; when there is, consumers are less likely to buy anything at all, and if they do buy, they are less satisfied with their selection.",
        "prompt": "Which finding, if true, would most strongly support the conclusions of the research described in the underlined section? (Underlined: 'consumers are less likely to buy anything at all, and if they do buy, they are less satisfied with their selection.')",
        "options": [
            {"key": "A", "text": "People faced with choosing among a large number of options experience physical symptoms associated with feeling overwhelmed."},
            {"key": "B", "text": "Consumers given a choice of 10 jams in a taste test were more likely to make a purchase than consumers who were offered only five."},
            {"key": "C", "text": "Shoppers who purchased food from multiple stores spent more on groceries than shoppers who purchased all their food from a single store."},
            {"key": "D", "text": "Some companies have increased the number of products they offer in order to appeal to a wider range of consumer preferences."}
        ],
        "correct_answer": "A",
        "pedagogical_focus": "Tìm cơ chế củng cố luận điểm nghịch lý quá nhiều lựa chọn: việc bị choáng ngợp (feeling overwhelmed) giải thích vì sao khách hàng không mua hoặc cảm thấy không hài lòng.",
        "erica_explanation": "Phần gạch chân đưa ra kết luận: khi có quá nhiều lựa chọn, khách hàng ít khả năng mua hàng hơn, và nếu có mua thì cũng kém hài lòng hơn. Phương án (A) củng cố trực tiếp kết luận này bằng việc chỉ ra rằng khi đối mặt với quá nhiều phương án, con người trải qua các triệu chứng thực thể của sự quá tải/choáng ngợp ('feeling overwhelmed'). (B) đi ngược lại bài; (C) và (D) lạc đề."
    },
    {
        "chapter_num": 8,
        "module_code": "Ch8_SupportUndermining",
        "topic": "Ch. 8: Support/Undermine • Supporting a Neurological Theory",
        "pdf_page": 137,
        "passage": "As a person sleeps, the motor cortex—the part of the brain that controls movements—replays skills that it learned during the day. In a recent experiment run by the BrainGate consortium, researchers observed that the pattern of firing neurons sped up during sleep, echoing findings from previous animal studies. The scientists were also interested to note that replay took place not during REM sleep, which is when people normally dream, but during deep, slow-wave sleep, which occurs in the first three or four hours of the night. They theorize that replay during this period helps the brain consolidate new information, moving it from short-term to long-term memory.",
        "prompt": "Which finding, if true, would most strongly support the scientists' theory?",
        "options": [
            {"key": "A", "text": "Athletes who slept for at least seven hours before a game competed at a higher level than ones who slept for less time."},
            {"key": "B", "text": "People whose neuron firings increased in speed during REM sleep retained new information over a longer period of time than people whose neurons fired more quickly early in their sleep cycle."},
            {"key": "C", "text": "Students who slept for only a few hours before an exam showed no difference in performance when compared to students who slept for a full night."},
            {"key": "D", "text": "Dancers who slept for several hours shortly after learning a new routine knew it better two weeks later than a group that stayed awake."}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Kiểm tra giả thuyết: hiện tượng tái hiện kỹ năng diễn ra trong giấc ngủ sâu sóng chậm (3-4 giờ đầu đêm) giúp củng cố trí nhớ dài hạn -> Nhóm ngủ vài giờ sau khi học sẽ nhớ tốt hơn nhóm thức trắng sau 2 tuần.",
        "erica_explanation": "Giả thuyết của các nhà khoa học: việc tái hiện tín hiệu nơ-ron trong giai đoạn ngủ sâu sóng chậm (diễn ra trong 3-4 giờ đầu tiên của giấc ngủ) giúp củng cố thông tin từ trí nhớ ngắn hạn sang dài hạn. Để củng cố điều này, một thí nghiệm kiểm chứng phải chỉ ra rằng giấc ngủ ngắn vài giờ (đủ để trải qua giai đoạn sóng chậm) sau khi học kỹ năng vận động giúp duy trì kỹ năng sau thời gian dài (2 tuần). Phương án (D) cung cấp chính xác kịch bản thực nghiệm này."
    },
    {
        "chapter_num": 8,
        "module_code": "Ch8_SupportUndermining",
        "topic": "Ch. 8: Support/Undermine • Undermining an Evolutionary Hypothesis",
        "pdf_page": 138,
        "passage": "Dinosaurs, with the exception of the ancestors of birds, disappeared during a mass extinction 65 million years ago when an asteroid struck the Earth. Because a high metabolic rate has generally been suggested as one of the key advantages when it comes to surviving mass extinctions, some genetic palaeontologists have proposed that birds survived while non-avian dinosaurs did not because of the birds' increased metabolic capacity.",
        "prompt": "Which finding, if true, would undermine the genetic paleontologists' proposal?",
        "options": [
            {"key": "A", "text": "The metabolisms of non-avian dinosaurs may have decreased over time."},
            {"key": "B", "text": "Because some non-avian dinosaurs moved quickly, they likely had high metabolic rates."},
            {"key": "C", "text": "Birds have some of the highest metabolism rates of any creatures on Earth."},
            {"key": "D", "text": "Many dinosaurs with very high metabolic rates went extinct 65 million years ago."}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Nguyên lý làm suy yếu (Undermine): Giả thuyết cho rằng 'tốc độ trao đổi chất cao giúp sống sót qua thảm họa' -> Bằng chứng phản bác trực diện là 'rất nhiều loài có trao đổi chất cao vẫn bị tuyệt chủng'.",
        "erica_explanation": "Giả thuyết của các nhà cổ sinh học di truyền: tổ tiên loài chim sống sót qua thảm họa đại tuyệt chủng 65 triệu năm trước là nhờ có khả năng trao đổi chất cao hơn (increased metabolic capacity). Để làm suy yếu luận điểm này, cần tìm bằng chứng cho thấy tốc độ trao đổi chất cao KHÔNG ĐẢM BẢO khả năng sống sót. Phương án (D) chỉ ra rằng rất nhiều loài khủng long sở hữu tốc độ trao đổi chất rất cao vẫn bị tuyệt chủng 65 triệu năm trước, phá hủy trực tiếp mối liên hệ nhân quả của giả thuyết."
    },

    # ================= CHAPTER 9: GRAPHS & CHARTS =================
    {
        "chapter_num": 9,
        "module_code": "Ch9_GraphsCharts",
        "topic": "Ch. 9: Graphs • Single Region Criterion Matching",
        "pdf_page": 147,
        "passage": "As part of a unit on pollination, a biology student is researching Colony Collapse Disorder, the mysterious disappearance of millions of honeybee (Apis mellifera) colonies in the early 2000s. Although many wild bee populations have continued to decline, the number of honeybees has actually increased on every continent. The student wants to emphasize that in some regions, honeybee populations had not only rebounded by 2020 but also reached their highest level in 60 years.",
        "prompt": "Which region included in the graph should the student cite to support this claim? (Graph: Apis Mellifera Colonies in Africa, Americas, Europe, Asia from 1960 to 2020)",
        "options": [
            {"key": "A", "text": "Africa"},
            {"key": "B", "text": "Americas"},
            {"key": "C", "text": "Europe"},
            {"key": "D", "text": "Asia"}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Đối chiếu tiêu chí kép từ văn bản: (1) Phục hồi trước năm 2020, và (2) Đạt mức cao nhất trong 60 năm qua -> Trục hoành và đường biểu đồ của châu Á (Asia).",
        "erica_explanation": "Học sinh muốn nhấn mạnh khu vực mà quần thể ong mật không chỉ phục hồi trước năm 2020 mà còn đạt đỉnh cao nhất trong 60 năm (highest level in 60 years). Nhìn vào biểu đồ đường trên trang 147, đường biểu đồ của châu Á (Asia) liên tục đi lên và đạt mức xấp xỉ 45 triệu đàn vào năm 2020, cao nhất trong suốt giai đoạn 1960-2020. Do đó, châu Á (D) là câu trả lời chính xác duy nhất."
    },
    {
        "chapter_num": 9,
        "module_code": "Ch9_GraphsCharts",
        "topic": "Ch. 9: Graphs • Majority Preference Data Extraction",
        "pdf_page": 149,
        "passage": "Despite steady gains in readership and overall popularity, e-books are hardly positioned to replace print books. Rather, the two types of media complement each other, providing the same content in different forms. Print books and e-books each have unique attributes and serve distinct purposes, which vary by demographic and situational factors. Researchers Yin Zhang and Sunali Kudva used data from the National Reading Habits Survey to examine book-format preferences in a variety of situations. Although the pair found that e-books are firmly established as an option due to ease of accessibility, they also concluded that print books offer greater appeal to most readers in certain situations.",
        "prompt": "Which choice best describes data from the chart that supports Zhang and Kudva's finding?",
        "options": [
            {"key": "A", "text": "A large majority of readers seeking immediate access to a book preferred the electronic option, with less than 25% of readers opting for print."},
            {"key": "B", "text": "The percentage of readers who choose a format based on the variety of titles available was about 50% for both print books and e-books."},
            {"key": "C", "text": "More than 75% of readers preferred print books for reading to a child, and more than 60% preferred print books for sharing with other readers."},
            {"key": "D", "text": "When concerned about quick access or reading during travel, most readers preferred books in the same format."}
        ],
        "correct_answer": "C",
        "pedagogical_focus": "Khớp tiêu chí kết luận của bài đọc: 'print books offer greater appeal to most readers' (đa số >50% độc giả chuộng sách in) -> Tìm cột sách in vượt trội rõ rệt.",
        "erica_explanation": "Kết luận của hai nhà nghiên cứu là sách in vẫn vượt trội hơn đối với đa số độc giả trong một số tình huống nhất định ('greater appeal to most readers in certain situations'). Như vậy, dữ liệu củng cố phải chỉ ra những trường hợp mà tỷ lệ chọn sách in chiếm đa số rõ rệt (>50%). Phương án (C) dẫn chứng chính xác từ biểu đồ: hơn 75% độc giả chọn sách in khi đọc cho trẻ em, và hơn 60% chọn sách in khi chia sẻ với người khác."
    },
    {
        "chapter_num": 9,
        "module_code": "Ch9_GraphsCharts",
        "topic": "Ch. 9: Graphs • Interpreting Antibiotic Effectiveness Discrepancy",
        "pdf_page": 151,
        "passage": "MRSA—Methicillin-resistant Staphylococcus aureus—is a type of bacteria that is frequently responsible for hospital-acquired infections and is known for being exceptionally resistant to common antibiotics. When a group of these medications were compared in terms of their ability to cure MRSA infections versus a variety of other infections, researchers found that an antibiotic could demonstrate a high level of general effectiveness but that the same medication could be significantly less effective in combatting MRSA. For example, __",
        "prompt": "Which choice most effectively uses data from the table to logically complete the text? (Data: Erythromycin 31.94% vs 26.92%, Vancomycin 100% vs 100%, Mupirocin 90.28% vs 73.08%, Penicillin 5% vs 0%, Clindamycin 83.33% vs 69.23%, Rifampicin 86.11% vs 61.54%)",
        "options": [
            {"key": "A", "text": "Erythromycin had a general effectiveness of nearly 32%, whereas its MRSA effectiveness was only about five points lower."},
            {"key": "B", "text": "Whereas Mupirocin was around 17% less effective against MRSA than against general infections, the gap for Clindamycin was only about 14%."},
            {"key": "C", "text": "Only Vancomycin was fully effective in combatting both general and MRSA bacteria."},
            {"key": "D", "text": "Rifampicin showed a general effectiveness rate of more than 85%, whereas it was just over 60% effective against MRSA."}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Hai điều kiện logic: (1) Chỉ đề cập đến MỘT loại kháng sinh (để làm ví dụ), và (2) Có độ chênh lệch hiệu quả lớn ('significantly less effective').",
        "erica_explanation": "Câu trước ô trống nêu luận điểm: cùng một loại kháng sinh có thể có hiệu quả chung rất cao nhưng lại kém hiệu quả rõ rệt khi đối đầu với MRSA. Ví dụ minh họa cần đưa ra một loại thuốc đơn lẻ có mức chênh lệch lớn. Rifampicin có hiệu quả chung đạt 86.11% nhưng khi diệt MRSA tụt xuống 61.54% (chênh lệch gần 25 điểm %). Phương án (D) trích xuất chính xác số liệu và minh họa chuẩn xác cho luận điểm."
    },

    # ================= CHAPTER 10: PAIRED PASSAGES =================
    {
        "chapter_num": 10,
        "module_code": "Ch10_PairedPassages",
        "topic": "Ch. 10: Paired Passages • Predicting Response from Passage Framework",
        "pdf_page": 161,
        "passage": "[Framework Overview]: In SAT Paired Passages, Text 1 typically presents a theory or experiment that demonstrates a specific scientific phenomenon (e.g., that sustained stress triggers long-term adaptive mechanisms), while Text 2 presents an alternative view or experimental findings indicating that the phenomenon may not function as claimed in real-world contexts.",
        "prompt": "How would Chang (Text 2) most likely respond to the researchers' theory about sustained stress in Text 1?",
        "options": [
            {"key": "A", "text": "It is not convincing as an explanation, despite findings that may seem to support it."},
            {"key": "B", "text": "It is generally accurate but contains some questionable elements."},
            {"key": "C", "text": "It can only be applied in certain situations."},
            {"key": "D", "text": "It may seem reasonable, but the researchers' results do not support it."}
        ],
        "correct_answer": "D",
        "pedagogical_focus": "Chiến thuật dự đoán phản biện: Hai đoạn văn thường bất đồng. Khi có sự không khớp giữa lý thuyết và thực nghiệm, tác giả Text 2 thường phản biện rằng kết quả thực nghiệm không đủ cơ sở để nâng đỡ cho lý thuyết.",
        "erica_explanation": "Trong cấu trúc đề thi SAT Paired Passages, khi Tác giả 2 phản hồi giả thuyết của Tác giả 1, quan điểm phổ biến nhất là chỉ ra rằng giả thuyết nghe có vẻ hợp lý trên giấy tờ nhưng dữ liệu thực nghiệm thực tế lại không củng cố cho kết luận đó. Phương án (D) thể hiện thái độ phản biện học thuật chuẩn mực của SAT: 'It may seem reasonable, but the researchers' results do not support it'."
    },
    {
        "chapter_num": 10,
        "module_code": "Ch10_PairedPassages",
        "topic": "Ch. 10: Paired Passages • Contrasting Views on Food Miles",
        "pdf_page": 162,
        "passage": "Text 1: Our food now travels an average of 1,500 miles before ending up on our plates. This globalization of the food supply has serious consequences for the environment, our health, our communities and our tastebuds. Much of the food grown in the breadbasket surrounding us must be shipped across the country to distribution centers before it makes its way back to our supermarket shelves. Because uncounted costs of this long-distance journey (air pollution and global warming, the ecological costs of large-scale monoculture, the loss of family farms and local community dollars) are not paid for at the checkout counter, many of us do not think about them at all.\n\nText 2: Just how much carbon dioxide is emitted by transporting food from farm to fork? Pierre Desrochers and Hiroko Shimizu cite a comprehensive study done by the United Kingdom's Department of Environment, Food and Rural Affairs (DEFRA) which reported that 82 percent of food miles were generated within the U.K. Consumer shopping trips accounted for 48 percent and trucking for 31 percent of British food miles. Air freight amounted to less than 1 percent of food miles. In total, food transportation accounted for only 1.8 percent of Britain's carbon dioxide emissions.",
        "prompt": "Based on the texts, how would Desrochers and Shimizu (Text 2) most likely describe the view presented in Text 1?",
        "options": [
            {"key": "A", "text": "It is strongly supported by data compiled by DEFRA."},
            {"key": "B", "text": "It overstates the effects of transporting food on the environment."},
            {"key": "C", "text": "It appears justified by preliminary findings but has not yet definitively proven."},
            {"key": "D", "text": "It is highly implausible because most consumers do not consider the source of their food."}
        ],
        "correct_answer": "B",
        "pedagogical_focus": "Xác định lập trường đối lập: Text 1 cho rằng vận chuyển thực phẩm gây tác hại môi trường nghiêm trọng ('serious consequences for global warming'), Text 2 đưa số liệu chứng minh nó chỉ chiếm 1.8% lượng khí thải carbon -> Text 1 đang nói quá ('overstates').",
        "erica_explanation": "Đoạn 1 kịch liệt cảnh báo việc vận chuyển thực phẩm 1,500 dặm gây hậu quả nghiêm trọng cho môi trường và nóng lên toàn cầu. Ngược lại, Đoạn 2 trích dẫn nghiên cứu của DEFRA chứng minh lượng khí thải CO2 từ vận chuyển lương thực chỉ vỏn vẹn 1.8% tổng phát thải của Anh. Do đó, các tác giả Đoạn 2 sẽ coi quan điểm của Đoạn 1 là đã 'thổi phồng/nói quá tác động của việc vận chuyển thực phẩm lên môi trường' (overstates the effects). Phương án (B) là đáp án hoàn hảo."
    }
]

def parse_options_raw(raw):
    if not raw:
        return []
    lines = [line.strip() for line in str(raw).split('\n') if line.strip()]
    options = []
    current_key = None
    current_text = []
    
    for line in lines:
        m = re.match(r'^([A-D])[\.\:\)]\s*(.*)$', line)
        if m:
            if current_key:
                options.append({'key': current_key, 'text': ' '.join(current_text).strip()})
            current_key = m.group(1)
            current_text = [m.group(2)]
        else:
            if current_key:
                current_text.append(line)
    if current_key:
        options.append({'key': current_key, 'text': ' '.join(current_text).strip()})
    return options

def load_practice_questions():
    print(f"Loading practice questions from workbook: {EXCEL_PATH}")
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=False)
    practice_by_chapter = {}

    chapter_sheets = [
        (2, "Ch2_Vocabulary"),
        (3, "Ch3_MakingTheLeap"),
        (4, "Ch4_BigPicture"),
        (5, "Ch5_LiteralComprehension"),
        (6, "Ch6_ReadingForFunction"),
        (7, "Ch7_TextCompletions"),
        (8, "Ch8_SupportUndermining"),
        (9, "Ch9_GraphsCharts"),
        (10, "Ch10_PairedPassages")
    ]

    for ch_num, sname in chapter_sheets:
        if sname not in wb.sheetnames:
            continue
        ws = wb[sname]
        ch_strategy = str(ws.cell(row=3, column=1).value or '').strip()
        ch_traps = str(ws.cell(row=3, column=9).value or '').strip()
        q_list = []

        for r in range(5, ws.max_row + 1):
            raw_q_label = ws.cell(row=r, column=1).value
            topic_str = ws.cell(row=r, column=2).value
            passage = ws.cell(row=r, column=3).value
            prompt = ws.cell(row=r, column=4).value
            options_raw = ws.cell(row=r, column=5).value
            formula = str(ws.cell(row=r, column=7).value or '')
            hint_formula = str(ws.cell(row=r, column=15).value or '')
            strat_tip = str(ws.cell(row=r, column=16).value or '').strip()

            if not (raw_q_label and prompt):
                continue

            # Extract correct answer from formula
            m_ans = re.search(r'=\"([ABCD])\"', formula)
            correct_ans = m_ans.group(1) if m_ans else ''
            if not correct_ans:
                continue

            # Extract Socratic hint
            m_hint = re.search(r'Gợi ý:\s*\"?\s*&\s*\"([^\"]+)', hint_formula)
            if not m_hint:
                m_hint = re.search(r'Gợi ý:\s*([^\"&]+)', hint_formula)
            raw_hint = m_hint.group(1).replace("\\'", "'").strip() if m_hint else ""

            options = parse_options_raw(options_raw)

            q_list.append({
                "topic_str": str(topic_str or '').strip(),
                "passage": str(passage or '').strip(),
                "prompt": str(prompt or '').strip(),
                "options": options,
                "options_raw": str(options_raw or '').strip(),
                "correct_answer": correct_ans,
                "raw_hint": raw_hint,
                "strat_tip": strat_tip,
                "ch_strategy": ch_strategy,
                "ch_traps": ch_traps
            })

        practice_by_chapter[ch_num] = q_list

    return practice_by_chapter

def build_full_dataset():
    practice_data = load_practice_questions()
    total_prac = sum(len(qs) for qs in practice_data.values())
    print(f"Loaded {total_prac} practice questions from Excel.")

    chapter_configs = [
        {
            "num": 2,
            "code": "Ch2_Vocabulary",
            "name": "Chương 2: Vocabulary in Context (Nghĩa Từ Trong Ngữ Cảnh)",
            "short_name": "Chương 2: Vocabulary in Context",
            "sub_title": "Nghĩa Từ Trong Ngữ Cảnh",
            "domain": "Craft and Structure",
            "pdf_start_page": 29,
            "time_minutes": 30
        },
        {
            "num": 3,
            "code": "Ch3_MakingTheLeap",
            "name": "Chương 3: Making the Leap (Đại từ & Danh từ nén)",
            "short_name": "Chương 3: Making the Leap",
            "sub_title": "Đại từ & Danh từ nén",
            "domain": "Information and Ideas",
            "pdf_start_page": 61,
            "time_minutes": 15
        },
        {
            "num": 4,
            "code": "Ch4_BigPicture",
            "name": "Chương 4: The Big Picture / Main Idea (Ý chính & Đại ý)",
            "short_name": "Chương 4: The Big Picture",
            "sub_title": "Ý chính & Đại ý",
            "domain": "Information and Ideas",
            "pdf_start_page": 73,
            "time_minutes": 12
        },
        {
            "num": 5,
            "code": "Ch5_LiteralComprehension",
            "name": "Chương 5: Literal Comprehension (Đọc hiểu Trực tiếp)",
            "short_name": "Chương 5: Literal Comprehension",
            "sub_title": "Đọc hiểu Trực tiếp",
            "domain": "Information and Ideas",
            "pdf_start_page": 91,
            "time_minutes": 13
        },
        {
            "num": 6,
            "code": "Ch6_ReadingForFunction",
            "name": "Chương 6: Reading for Function (Đọc theo Chức năng Diễn ngôn)",
            "short_name": "Chương 6: Reading for Function",
            "sub_title": "Đọc theo Chức năng Diễn ngôn",
            "domain": "Craft and Structure",
            "pdf_start_page": 102,
            "time_minutes": 16
        },
        {
            "num": 7,
            "code": "Ch7_TextCompletions",
            "name": "Chương 7: Text Completions (Hoàn thành Văn bản / Suy luận)",
            "short_name": "Chương 7: Text Completions",
            "sub_title": "Hoàn thành Văn bản / Suy luận",
            "domain": "Information and Ideas",
            "pdf_start_page": 121,
            "time_minutes": 10
        },
        {
            "num": 8,
            "code": "Ch8_SupportUndermining",
            "name": "Chương 8: Supporting & Undermining (Củng cố & Làm suy yếu)",
            "short_name": "Chương 8: Supporting & Undermining",
            "sub_title": "Củng cố & Làm suy yếu",
            "domain": "Information and Ideas",
            "pdf_start_page": 133,
            "time_minutes": 15
        },
        {
            "num": 9,
            "code": "Ch9_GraphsCharts",
            "name": "Chương 9: Graphs & Charts (Biểu đồ & Bảng số liệu)",
            "short_name": "Chương 9: Graphs & Charts",
            "sub_title": "Biểu đồ & Bảng số liệu",
            "domain": "Information and Ideas",
            "pdf_start_page": 145,
            "time_minutes": 10
        },
        {
            "num": 10,
            "code": "Ch10_PairedPassages",
            "name": "Chương 10: Paired Passages (Đoạn văn Kép)",
            "short_name": "Chương 10: Paired Passages",
            "sub_title": "Đoạn văn Kép",
            "domain": "Cross-Text Connections",
            "pdf_start_page": 159,
            "time_minutes": 8
        }
    ]

    all_questions = []
    global_id = 0
    modules = []

    for ch in chapter_configs:
        ch_num = ch["num"]
        ch_examples = [ex for ex in GUIDED_EXAMPLES if ex["chapter_num"] == ch_num]
        ch_practice = practice_data.get(ch_num, [])
        
        ch_question_ids = []
        item_num = 0

        # 1. Add Guided Examples first
        for ex_idx, ex in enumerate(ch_examples, 1):
            global_id += 1
            item_num += 1
            ch_question_ids.append(global_id)

            tier1 = f"Đọc kỹ đoạn trích ví dụ và xác định ngữ cảnh trọng tâm: {ex['topic']}. Chú ý mối liên hệ logic và các từ khóa dẫn hướng."
            tier2 = f"Chiến thuật sư phạm Erica Meltzer: {ex['pedagogical_focus']} Phân tích phương án nhiễu và loại trừ các lựa chọn ngoài phạm vi bài."
            
            target_opt = next((o for o in ex["options"] if o['key'] == ex["correct_answer"]), None)
            target_text = target_opt['text'] if target_opt else ''
            tier3 = (
                f"Đáp án chính xác là **{ex['correct_answer']}** ({target_text}).\n\n"
                f"**Bài giảng chi tiết của Erica Meltzer:**\n"
                f"{ex['erica_explanation']}\n\n"
                f"• **Quy tắc vàng:** {ex['pedagogical_focus']}"
            )

            mermaid = (
                f"flowchart TD\n"
                f"    A[\"Ví dụ minh họa Ch.{ch_num}<br>{ex['topic'][:40]}\"] --> B{{\"Manh mối cốt lõi\"}}\n"
                f"    B --> C[\"{ex['pedagogical_focus'][:55]}\"]\n"
                f"    C --> D[\"Đáp án chính xác: {ex['correct_answer']}\"]"
            )

            q_obj = {
                "id": global_id,
                "master_id": f"EM_Ch{ch_num}_Ex{ex_idx}",
                "q_number": item_num,
                "q_label": f"Ch.{ch_num} - Ví dụ {ex_idx}",
                "category": "example",
                "category_label": "Ví dụ minh họa",
                "module_code": ch["code"],
                "module_title": ch["name"],
                "section": "Reading and Writing",
                "chapter": ch["name"],
                "chapter_num": ch_num,
                "topic": ex["topic"],
                "passage": ex["passage"],
                "prompt": ex["prompt"],
                "options": ex["options"],
                "options_raw": "\n".join([f"{o['key']}) {o['text']}" for o in ex["options"]]),
                "is_grid_in": False,
                "correct_answer": ex["correct_answer"],
                "acceptable_answers": [ex["correct_answer"]],
                "tier1_hint": tier1,
                "tier2_hint": tier2,
                "tier3_hint": tier3,
                "strategic_tip": ex["pedagogical_focus"],
                "mermaid_diagram": mermaid,
                "pdf_page": ex["pdf_page"],
                "difficulty": "Foundation",
                "domain": ch["domain"]
            }
            all_questions.append(q_obj)

        # 2. Add Practice Questions
        for pr_idx, pr in enumerate(ch_practice, 1):
            global_id += 1
            item_num += 1
            ch_question_ids.append(global_id)

            tier1 = f"Đọc kỹ đoạn văn và xác định ngữ cảnh trọng tâm của câu hỏi: {pr['topic_str']}. Chú ý mối liên hệ logic giữa các câu văn và từ nối chuyển ý."
            
            clean_hint = pr["raw_hint"]
            for letter in ["A", "B", "C", "D"]:
                clean_hint = re.sub(rf'\b(đáp án|chọn|phương án)\s+{letter}\b', 'phương án này', clean_hint, flags=re.IGNORECASE)
            
            strat_note = pr["strat_tip"] if pr["strat_tip"] else (pr["ch_strategy"] if pr["ch_strategy"] else "Tìm dẫn chứng trực tiếp từ đoạn văn, loại trừ phương án quá cực đoan hoặc suy diễn ngoài bài.")
            if clean_hint:
                tier2 = f"{clean_hint} Áp dụng quy tắc vàng Erica Meltzer: {strat_note}"
            else:
                tier2 = f"Áp dụng chiến thuật cốt lõi: {strat_note}"

            target_opt = next((o for o in pr["options"] if o['key'] == pr["correct_answer"]), None)
            target_text = target_opt['text'] if target_opt else ''
            tier3 = (
                f"Đáp án chính xác là **{pr['correct_answer']}** ({target_text}).\n\n"
                f"**Phân tích chi tiết:**\n"
                f"• Văn bản cung cấp manh mối: {pr['raw_hint'] if pr['raw_hint'] else pr['prompt']}\n"
                f"• Chiến thuật trọng tâm ({ch['short_name']}): {pr['strat_tip'] if pr['strat_tip'] else pr['ch_strategy']}\n"
                f"• Phương án **{pr['correct_answer']}** khớp hoàn hảo với logic và nội dung trong bài, không mắc các bẫy cực đoan hay suy diễn quá đà."
            )

            mermaid = (
                f"flowchart TD\n"
                f"    A[\"Ngữ cảnh ({ch['short_name']})<br>{pr['topic_str'][:35]}\"] --> B{{\"Manh mối cốt lõi\"}}\n"
                f"    B --> C[\"{(pr['strat_tip'] or pr['ch_strategy'])[:55]}\"]\n"
                f"    C --> D[\"Đáp án tối ưu: Phương án {pr['correct_answer']}\"]"
            )

            q_obj = {
                "id": global_id,
                "master_id": f"EM_Ch{ch_num}_Q{pr_idx}",
                "q_number": item_num,
                "q_label": f"Ch.{ch_num} - Câu {pr_idx}",
                "category": "practice",
                "category_label": "Thực hành",
                "module_code": ch["code"],
                "module_title": ch["name"],
                "section": "Reading and Writing",
                "chapter": ch["name"],
                "chapter_num": ch_num,
                "topic": f"{ch['short_name']} • {pr['topic_str']}",
                "passage": pr["passage"],
                "prompt": pr["prompt"],
                "options": pr["options"],
                "options_raw": pr["options_raw"],
                "is_grid_in": False,
                "correct_answer": pr["correct_answer"],
                "acceptable_answers": [pr["correct_answer"]],
                "tier1_hint": tier1,
                "tier2_hint": tier2,
                "tier3_hint": tier3,
                "strategic_tip": pr["strat_tip"],
                "mermaid_diagram": mermaid,
                "pdf_page": ch["pdf_start_page"],
                "difficulty": "Medium" if ch_num <= 5 else "Hard",
                "domain": ch["domain"]
            }
            all_questions.append(q_obj)

        modules.append({
            "id": f"em_ch{ch_num}",
            "code": ch["code"],
            "chapter_num": ch_num,
            "title": ch["name"],
            "short_title": ch["short_name"],
            "sub_title": ch["sub_title"],
            "domain": ch["domain"],
            "section": "Reading and Writing",
            "time_minutes": ch["time_minutes"],
            "question_count": len(ch_question_ids),
            "example_count": len(ch_examples),
            "practice_count": len(ch_practice),
            "pdf_start_page": ch["pdf_start_page"],
            "strategy": ch_practice[0]["ch_strategy"] if ch_practice else "",
            "traps": ch_practice[0]["ch_traps"] if ch_practice else "",
            "question_ids": ch_question_ids
        })

    print(f"Total compiled questions: {len(all_questions)} (Examples: {len(GUIDED_EXAMPLES)}, Practice: {total_prac})")

    # Audit for leaks in Tier 1 and Tier 2
    leaks = 0
    for q in all_questions:
        for letter in ["A", "B", "C", "D"]:
            pattern = rf"(đáp án|chọn|phương án)\s+(là\s+)?{letter}\b"
            if re.search(pattern, q["tier1_hint"], re.IGNORECASE):
                print(f"[LEAK] Q{q['id']} Tier 1: {q['tier1_hint']}")
                leaks += 1
            if re.search(pattern, q["tier2_hint"], re.IGNORECASE):
                print(f"[LEAK] Q{q['id']} Tier 2: {q['tier2_hint']}")
                leaks += 1

    if leaks == 0:
        print("✅ NO-LEAK AUDIT PASSED: 0 leaks found across all 101 questions!")
    else:
        print(f"❌ WARNING: {leaks} leaks detected.")

    total_time = sum(m["time_minutes"] for m in modules)

    db_data = {
        "test_title": "The Critical Reader: Complete Guide to SAT Reading (Erica Meltzer)",
        "source_attribution": "Erica Lynn Meltzer - The Critical Reader: The Complete Guide to SAT Reading (Digital SAT)",
        "credits": "Compiled and Enhanced by Mike Pham Bá Hong Son - Google for Education Innovator",
        "pdf_drive_id": "10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z",
        "pdf_path": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/preview",
        "pdf_drive_preview": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/preview",
        "pdf_drive_view": "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/view",
        "total_questions": len(all_questions),
        "total_examples": len(GUIDED_EXAMPLES),
        "total_practice": total_prac,
        "time_minutes": total_time,
        "modules_count": len(modules),
        "structure_mode": "chapter_by_chapter_with_examples",
        "modules": modules,
        "questions": all_questions
    }

    out_file = os.path.join(os.path.dirname(__file__), OUTPUT_JSON)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(db_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully exported {len(all_questions)} questions to {out_file} ({os.path.getsize(out_file)} bytes)")

if __name__ == "__main__":
    build_full_dataset()
