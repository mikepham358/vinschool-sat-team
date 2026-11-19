/**
 * Digital SAT Bluebook App - Internationalization (i18n) Engine
 * Language versions: English (Default) & Vietnamese
 * Designed with Google & Lego UX Design Philosophy:
 * Minimalist, joyful, tactile, mirror-glazed, and crystal clear.
 */

window.I18N_TRANSLATIONS = {
  en: {
    // Brand & App Bar
    brand_title: "Digital SAT Practice Based on Learning Science",
    btn_aar: "AAR Report",
    btn_vocab_1000: "AceSAT: 1,000 Vocab",
    exam_picker_label: "🗓️ Active Exam:",
    lang_toggle_btn: "English",
    lang_toggle_alt: "VI",
    hero_eyebrow: "✨ DESIGNED FOR VINSCHOOL SAT TEAM",

    // Home Page Hero
    hero_tag: "AUTHENTIC DIGITAL SAT ECOSYSTEM",
    hero_desc: "Master every question with authentic test booklets, synchronized Google Drive PDF viewer, Desmos graphing calculator, Socratic 4-tier feedback, and reflective error logging.",
    btn_hero_drive_pdf: "📖 Open Test Booklet PDF (Google Drive)",
    btn_hero_launch_vocab: "📚 1,000 SAT Vocab Hub",
    btn_hero_vocab_flashcard: "⚡ Vocab Flashcards",

    // Symmetrical Anticipation (Goal & Challenge)
    hero_aar_anticipation_title: "1️⃣ Pre-Session Anticipation (AAR Cycle)",
    hero_aar_anticipation_desc: "Define your learning intentions and anticipate challenges before practicing to build strong metacognition.",
    home_aar_sync_badge: "💾 Auto-saved to AAR Report",
    goal_field_label: "Lesson Goal & Target Score *",
    goal_badge_label: "🎯 TARGET SCORE & GOAL",
    goal_placeholder: "e.g. Score ≥ 85% correct; master keyword trap detection & POOE elimination.",
    challenge_field_label: "Anticipated Challenge *",
    challenge_badge_label: "📓 ERROR LOG NOTEBOOK",
    challenge_btn_text: "Review Error Log",
    challenge_placeholder: "e.g. Long inference questions, pacing pressure, or complex Desmos graphing.",

    // Student Information Form
    student_form_title: "Student Information",
    student_form_desc: "Enter your details to track personal progress, error logging, and AAR reports.",
    secure_badge: "🔒 100% saved locally on personal device",
    label_student_name: "Student Full Name *",
    placeholder_student_name: "e.g. Mike Pham",
    label_student_email: "Student Email Address *",
    placeholder_student_email: "e.g. mikepham358@gmail.com",
    label_target_score: "Expected Target Score Level *",
    label_session_date: "Session # (Practice Date) *",
    label_sat_module: "Expected SAT Module *",
    label_iste_standard: "Applied ISTE Standard *",
    btn_start_practice: "Start SAT Practice Now 🚀",
    btn_view_guide: "📖 Rules & Guide",
    btn_home_review_errors: "📓 Review Socratic Error Log",
    error_badge_suffix: "errors",

    // Modules Section
    modules_section_tag: "EXAM STRUCTURE (4 MODULES)",
    modules_section_title: "Select a Module to Start Practicing",
    modules_section_desc: "You can practice each module independently or complete all 98 questions consecutively.",
    btn_enter_module: "Enter Module ➔",
    mod_rw1_title: "Reading & Writing: Module 1",
    mod_rw1_desc: "27 questions testing Words in Context, Text Structure, Inferences, and Standard English Conventions.",
    mod_rw2_title: "Reading & Writing: Module 2 (Harder)",
    mod_rw2_desc: "27 advanced questions with complex scientific passages, quantitative evidence, and cross-text synthesis.",
    mod_math1_title: "Math: Module 1",
    mod_math1_desc: "22 questions covering Linear Equations, Quadratics, Geometry, and Statistics with Desmos.",
    mod_math2_title: "Math: Module 2 (Advanced)",
    mod_math2_desc: "22 high-yield questions featuring non-linear modeling, coordinate geometry, and Grid-in SPR items.",
    time_rw: "⏱️ 32 Mins",
    time_math: "⏱️ 35 Mins",
    qs_count_27: "27 Questions",
    qs_count_22: "22 Questions",

    // Practice Header & Controls
    btn_home: "Home",
    timer_hide: "Hide",
    timer_show: "Show",
    session_counter_label: "questions",
    btn_reset: "Reset",
    btn_zen: "Zen",
    btn_dict: "Dictionary",
    btn_error_log: "Error Log",
    btn_badges: "Badges",
    btn_vocab_tool: "1,000 Vocab",
    btn_scratchpad: "Scratchpad",
    btn_calc: "Desmos",
    btn_ref: "Math Formulas",
    btn_aar_header: "AAR",
    student_badge_default: "Student",
    input_student_name_ph: "Enter student name...",
    btn_strike_title: "Eliminate Option",
    tablet_pdf_tab: "📄 Test PDF Booklet",
    tablet_content_tab: "📝 Questions & Answers",
    response_instruction_default: "Read the question in the PDF booklet on the left and select the correct answer below:",
    pdf_page_prefix: "📖 This question is on",
    page_label: "Page",

    // Question Practice View
    question_of: "Question {cur} of {total}",
    mark_review: "Mark for Review",
    eliminate_options: "Eliminate Options (Alt+X)",
    btn_check_answer: "Check Answer (Enter)",
    btn_back: "Back",
    btn_next: "Next",
    choice_prefix: "Choice",
    gridin_placeholder: "Enter numeric answer...",
    mermaid_trigger_title: "Visual Logic Mindmap (Mermaid)",
    mermaid_trigger_btn: "Logic mindmap",

    // 4-Tier Socratic Hints
    tier1_title: "💡 Tier 1: Context Clues & Orientation",
    tier2_title: "🔍 Tier 2: Structural Clues & POOE Elimination",
    tier3_title: "🎯 Tier 3: Core Rationale & Detailed Solution",
    tier4_title: "✨ Tier 4: Strategic Tip & Desmos Shortcut",
    tier1_locked: "🔒 Complete Attempt 1 to unlock Context Clues orientation.",
    tier2_locked: "🔒 Complete Attempt 2 to unlock Structural Clues & POOE elimination.",
    tier3_locked: "🔒 Unlocked after 3 attempts or upon answering correctly.",
    tier4_locked: "🔒 Complete this question to unlock strategic pro-tips and shortcuts.",
    exp_correct_badge: "✅ CORRECT ANSWER",
    exp_wrong_badge: "❌ WHY INCORRECT / ELIMINATED",

    // Modals & Notebooks
    modal_error_log_title: "SOCRATIC ERROR LOG & REFLECTION NOTEBOOK",
    modal_reflection_title: "MANDATORY ERROR REFLECTION - DID IT WORK YET?",
    modal_aar_title: "POST-SESSION AFTER ACTION REVIEW (AAR) REPORT",
    modal_desmos_title: "Desmos Graphing Calculator",
    modal_dict_title: "Cambridge Dictionary & SAT Vocab Lookup",
    modal_badges_title: "ACHIEVEMENTS & MICRO-CREDENTIALS",
    modal_scratchpad_title: "Scratchpad & Whiteboard",
    modal_reset_title: "Reset Test Progress?",
    modal_reset_desc: "This will clear all your answers and attempts for the current test. Your cumulative error logs and badges will be preserved.",
    btn_confirm_reset: "Yes, Reset Test",
    btn_cancel: "Cancel",
    btn_close: "Close"
  },

  vi: {
    // Brand & App Bar
    brand_title: "Hệ Thống Luyện Thi Digital SAT Dựa Trên Khoa Học Học Tập",
    btn_aar: "Báo Cáo AAR",
    btn_vocab_1000: "AceSAT: 1,000 Từ Vựng",
    exam_picker_label: "🗓️ Đề thi:",
    lang_toggle_btn: "Tiếng Việt",
    lang_toggle_alt: "EN",
    hero_eyebrow: "✨ DÀNH CHO ĐỘI NGŨ SAT VINSCHOOL",

    // Home Page Hero
    hero_tag: "HỆ THỐNG LUYỆN THI DIGITAL SAT REAL TEST",
    hero_desc: "Luyện tập với đề thi gốc, trình đọc PDF Google Drive đồng bộ, máy tính vẽ đồ thị Desmos, phản hồi 4 tầng Socratic và sổ thử sai phản tư.",
    btn_hero_drive_pdf: "📖 Mở File Đề PDF (Google Drive)",
    btn_hero_launch_vocab: "📚 Kho 1,000 Từ Vựng SAT",
    btn_hero_vocab_flashcard: "⚡ Thẻ Học Từ Vựng",

    // Symmetrical Anticipation (Goal & Challenge)
    hero_aar_anticipation_title: "1️⃣ Dự Đoán Trước Buổi Học (Anticipation - Chu Trình AAR)",
    hero_aar_anticipation_desc: "Xác định mục tiêu học tập và dự đoán thách thức trước khi làm bài để phát triển siêu nhận thức.",
    home_aar_sync_badge: "💾 Tự lưu vào Báo cáo AAR",
    goal_field_label: "Mục tiêu bài học & Điểm kỳ vọng *",
    goal_badge_label: "🎯 MỤC TIÊU BÀI HỌC & ĐIỂM KỲ VỌNG",
    goal_placeholder: "Ví dụ: Đạt ≥ 85% câu đúng; nắm chắc phương pháp bẫy từ khóa & loại đáp án sai.",
    challenge_field_label: "Thách thức dự kiến *",
    challenge_badge_label: "📓 XEM LẠI SỔ THỬ SAI",
    challenge_btn_text: "Xem lại Sổ thử sai",
    challenge_placeholder: "Ví dụ: Câu suy luận dài, áp lực thời gian hoặc thao tác đồ thị Desmos.",

    // Student Information Form
    student_form_title: "Thông Tin Học Sinh",
    student_form_desc: "Điền thông tin để lưu vết học tập, ghi chép sổ thử sai và báo cáo AAR.",
    secure_badge: "🔒 Lưu 100% trên thiết bị cá nhân",
    label_student_name: "Họ và tên học sinh *",
    placeholder_student_name: "Ví dụ: Nguyễn Văn An",
    label_student_email: "Địa chỉ Email học sinh *",
    placeholder_student_email: "Ví dụ: an.nguyen@vinschool.edu.vn",
    label_target_score: "Mục tiêu điểm số kỳ vọng *",
    label_session_date: "Buổi # (Ngày học) *",
    label_sat_module: "Mô-đun SAT dự kiến *",
    label_iste_standard: "Tiêu chuẩn ISTE áp dụng *",
    btn_start_practice: "Bắt Đầu Làm Bài Ngay 🚀",
    btn_view_guide: "📖 Quy Tắc & Hướng Dẫn",
    btn_home_review_errors: "📓 Xem Sổ Thử Sai Socratic",
    error_badge_suffix: "lỗi",

    // Modules Section
    modules_section_tag: "CẤU TRÚC ĐỀ THI (4 MODULES)",
    modules_section_title: "Chọn Module Để Bắt Đầu Luyện Tập",
    modules_section_desc: "Em có thể chọn luyện tập từng phần riêng biệt hoặc làm liên tục toàn bộ 98 câu.",
    btn_enter_module: "Vào Thi ➔",
    mod_rw1_title: "Đọc & Viết: Module 1",
    mod_rw1_desc: "27 câu hỏi trắc nghiệm kiểm tra từ vựng ngữ cảnh, cấu trúc văn bản, suy luận và ngữ pháp chuẩn.",
    mod_rw2_title: "Đọc & Viết: Module 2 (Phân Hóa)",
    mod_rw2_desc: "27 câu hỏi nâng cao với các đoạn văn khoa học phức tạp, biểu đồ dữ liệu và cặp văn bản đối chiếu.",
    mod_math1_title: "Toán: Module 1",
    mod_math1_desc: "22 câu hỏi đại số tuyến tính, phương trình bậc hai, hình học và thống kê kèm máy tính Desmos.",
    mod_math2_title: "Toán: Module 2 (Nâng Cao)",
    mod_math2_desc: "22 câu hỏi phân hóa đỉnh cao với hàm phi tuyến tính, hình học không gian và các câu điền số Grid-in.",
    time_rw: "⏱️ 32 Phút",
    time_math: "⏱️ 35 Phút",
    qs_count_27: "27 Câu",
    qs_count_22: "22 Câu",

    // Practice Header & Controls
    btn_home: "Trang chủ",
    timer_hide: "Ẩn",
    timer_show: "Hiện",
    session_counter_label: "câu",
    btn_reset: "Làm lại",
    btn_zen: "Zen",
    btn_dict: "Từ điển",
    btn_error_log: "Sổ thử sai",
    btn_badges: "Huy hiệu",
    btn_vocab_tool: "Kho 1,000 từ vựng",
    btn_scratchpad: "Bản nháp",
    btn_calc: "Desmos",
    btn_ref: "Công thức toán",
    btn_aar_header: "AAR",
    student_badge_default: "Học sinh",
    input_student_name_ph: "Nhập tên học sinh...",
    btn_strike_title: "Gạch bỏ phương án",
    tablet_pdf_tab: "📄 Đề Thi Gốc (PDF)",
    tablet_content_tab: "📝 Câu Hỏi & Trả Lời",
    response_instruction_default: "Đọc đề bài trên trang sách PDF bên trái và chọn đáp án đúng:",
    pdf_page_prefix: "📖 Câu này ở",
    page_label: "Trang",

    // Question Practice View
    question_of: "Câu {cur} trên {total}",
    mark_review: "Đánh dấu xem lại",
    eliminate_options: "Gạch bỏ phương án (Alt+X)",
    btn_check_answer: "Kiểm tra đáp án (Enter)",
    btn_back: "Câu trước",
    btn_next: "Câu tiếp",
    choice_prefix: "Lựa chọn",
    gridin_placeholder: "Nhập đáp án số...",
    mermaid_trigger_title: "Sơ đồ tư duy logic (Mermaid)",
    mermaid_trigger_btn: "Logic mindmap",

    // 4-Tier Socratic Hints
    tier1_title: "💡 Tầng 1: Định Hướng Bối Cảnh & Tư Duy Tổng Quan",
    tier2_title: "🔍 Tầng 2: Manh Mối Cấu Trúc & Phân Tích Loại Trừ (POOE)",
    tier3_title: "🎯 Tầng 3: Chốt Phương Pháp & Lời Giải Chi Tiết",
    tier4_title: "✨ Tầng 4: Chiến Thuật Độc Quyền & Mẹo Desmos",
    tier1_locked: "🔒 Thử sức Lần 1 để mở khóa gợi ý định hướng bối cảnh.",
    tier2_locked: "🔒 Thử sức Lần 2 để mở khóa manh mối cấu trúc & loại trừ phương án sai.",
    tier3_locked: "🔒 Mở khóa chốt phương pháp sau 3 lần thử hoặc khi làm đúng.",
    tier4_locked: "🔒 Hoàn thành câu hỏi để mở khóa phân tích chiến thuật & mẹo độc quyền.",
    exp_correct_badge: "✅ ĐÁP ÁN ĐÚNG",
    exp_wrong_badge: "❌ TẠI SAO SAI / BỊ LOẠI",

    // Modals & Notebooks
    modal_error_log_title: "SỔ TAY THỬ SAI & PHẢN TƯ SOCRATIC",
    modal_reflection_title: "GHI CHÉP THỬ - ĐƯỢC CHƯA? (BẮT BUỘC)",
    modal_aar_title: "BÁO CÁO PHẢN TƯ SAU BUỔI HỌC (CHU TRÌNH AAR)",
    modal_desmos_title: "Máy Tính Vẽ Đồ Thị Desmos",
    modal_dict_title: "Từ Điển Cambridge & Tra Cứu Từ Vựng SAT",
    modal_badges_title: "HỆ THỐNG HUY HIỆU & MICRO-CREDENTIALS",
    modal_scratchpad_title: "Bản Nháp & Bảng Vẽ Trực Quan",
    modal_reset_title: "Làm lại bài thi từ đầu?",
    modal_reset_desc: "Thao tác này sẽ đặt lại toàn bộ câu trả lời của đề thi hiện tại. Lịch sử nhật ký lỗi sai và huy hiệu vẫn được bảo lưu an toàn.",
    btn_confirm_reset: "Đồng Ý Làm Lại",
    btn_cancel: "Hủy bỏ",
    btn_close: "Đóng"
  }
};

/**
 * Get translation for key in current language (fallback to English)
 */
window.t = function(key, params) {
  const lang = (window.App && window.App.currentLang) ? window.App.currentLang : (localStorage.getItem("bluebook_lang") || "en");
  const dict = window.I18N_TRANSLATIONS[lang] || window.I18N_TRANSLATIONS["en"];
  let text = (dict && dict[key]) ? dict[key] : (window.I18N_TRANSLATIONS["en"][key] || key);

  if (params && typeof params === "object") {
    Object.keys(params).forEach(p => {
      text = text.replace(new RegExp(`\\{${p}\\}`, "g"), params[p]);
    });
  }
  return text;
};

/**
 * Apply language to all elements decorated with data-i18n attributes
 */
window.applyI18nToDOM = function(lang) {
  if (!lang) {
    lang = (window.App && window.App.currentLang) ? window.App.currentLang : (localStorage.getItem("bluebook_lang") || "en");
  }

  // Update HTML lang attribute
  document.documentElement.lang = lang;

  // Translate all [data-i18n]
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    const translated = window.t(key);
    if (translated && translated !== key) {
      el.textContent = translated;
    }
  });

  // Translate [data-i18n-html]
  document.querySelectorAll("[data-i18n-html]").forEach(el => {
    const key = el.getAttribute("data-i18n-html");
    const translated = window.t(key);
    if (translated && translated !== key) {
      el.innerHTML = translated;
    }
  });

  // Translate placeholders [data-i18n-placeholder]
  document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
    const key = el.getAttribute("data-i18n-placeholder");
    const translated = window.t(key);
    if (translated && translated !== key) {
      el.setAttribute("placeholder", translated);
    }
  });

  // Translate titles [data-i18n-title]
  document.querySelectorAll("[data-i18n-title]").forEach(el => {
    const key = el.getAttribute("data-i18n-title");
    const translated = window.t(key);
    if (translated && translated !== key) {
      el.setAttribute("title", translated);
    }
  });

  // Update Language Toggle Buttons display
  const isEn = (lang === "en");
  document.querySelectorAll(".btn-lang-toggle").forEach(btn => {
    const curLabel = btn.querySelector(".lang-cur");
    const altLabel = btn.querySelector(".lang-alt");
    if (curLabel) curLabel.textContent = isEn ? "EN" : "VI";
    if (altLabel) altLabel.textContent = isEn ? "VI" : "EN";
    btn.setAttribute("title", isEn ? "Switch to Vietnamese / Đổi sang Tiếng Việt" : "Switch to English / Đổi sang Tiếng Anh");
  });
};

/**
 * Toggle Language between English and Vietnamese
 */
window.toggleAppLanguage = function() {
  const current = (window.App && window.App.currentLang) ? window.App.currentLang : (localStorage.getItem("bluebook_lang") || "en");
  const nextLang = (current === "en") ? "vi" : "en";
  
  if (window.App) {
    window.App.currentLang = nextLang;
  }
  localStorage.setItem("bluebook_lang", nextLang);

  // Apply to DOM
  window.applyI18nToDOM(nextLang);

  // Trigger app-level re-renders
  const viewPractice = document.getElementById("view-practice");
  const isPracticeActive = viewPractice && !viewPractice.classList.contains("hidden");

  if (typeof window.renderModuleCards === "function") {
    window.renderModuleCards();
  }
  if (typeof window.syncAarAnticipationUI === "function") {
    window.syncAarAnticipationUI();
  }
  if (isPracticeActive && typeof window.renderCurrentQuestion === "function") {
    window.renderCurrentQuestion();
  }

  // Toast confirmation
  if (typeof window.showToast === "function") {
    window.showToast(nextLang === "en" ? "🌐 Switched language to English (Default)" : "🌐 Đã chuyển sang Tiếng Việt");
  }
};
