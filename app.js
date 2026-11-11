/**
 * Digital SAT Practice Based on Learning Science
 * Designed by Mike Pham Bá Hong Son - Google for Education Innovator
 * 100% Client-Side LocalStorage Isolation for Independent Student Practice
 * Multi-Exam Architecture with Dynamic Switching & Drive Sync
 */

const GLOBAL_PROFILE_KEY = "bluebook_global_student_profile_v1";
const GLOBAL_AAR_STORAGE_KEY = "bluebook_global_aar_tracker_v1";
const GLOBAL_AAR_DRAFT_KEY = "bluebook_global_aar_draft_v1";
const GLOBAL_SESSION_TRACKER_KEY = "bluebook_global_session_tracker_v1";
const LEGACY_STORAGE_KEY = "bluebook_oct2026_student_state_v1";
const AAR_TEACHER_RECIPIENTS = "v.sonpbh1@vinschool.edu.vn,mikepham@baoan.ai.vn";

const TESTS_MANIFEST_DEFAULT = [
  {
    id: "oct-2026",
    code: "oct2026",
    title: "Digital SAT Practice Test — October 2026 (INT-B)",
    short_title: "Tháng 10/2026 (INT-B)",
    badge: "Mới nhất",
    date: "2026-10",
    dataFile: "data/oct2026.json",
    pdfDriveId: "1Qiu34_dltehpEVmfHvOivjAvf8Zkd77b",
    pdfPreviewUrl: "https://drive.google.com/file/d/1Qiu34_dltehpEVmfHvOivjAvf8Zkd77b/preview",
    pdfViewUrl: "https://drive.google.com/file/d/1Qiu34_dltehpEVmfHvOivjAvf8Zkd77b/view?usp=drive_link",
    poster: "poster.png",
    total_questions: 98,
    storageKey: "bluebook_oct2026_student_state_v1",
    description: "Đề thi Real Test Digital SAT quốc tế tháng 10/2026 kèm giải thích chi tiết 4 tầng Socratic."
  },
  {
    id: "sep-2026",
    code: "sep2026",
    title: "Digital SAT Practice Test — September 2026 (INT-A)",
    short_title: "Tháng 09/2026 (INT-A)",
    badge: "Chính thức",
    date: "2026-09",
    dataFile: "data/sep2026.json",
    pdfDriveId: "1dt6Up_Tz-B_h48JVLeIPF8vMwWWPxVSL",
    pdfPreviewUrl: "https://drive.google.com/file/d/1dt6Up_Tz-B_h48JVLeIPF8vMwWWPxVSL/preview",
    pdfViewUrl: "https://drive.google.com/file/d/1dt6Up_Tz-B_h48JVLeIPF8vMwWWPxVSL/view",
    poster: "poster_sep.png",
    total_questions: 98,
    storageKey: "bluebook_sep2026_student_state_v1",
    description: "Đề thi Real Test Digital SAT quốc tế tháng 09/2026 kèm giải thích chi tiết 4 tầng Socratic."
  },
  {
    id: "erica-reading",
    code: "ericareading",
    title: "The Critical Reader: Complete Guide to SAT Reading (Erica Meltzer)",
    short_title: "Erica Meltzer Reading",
    badge: "9 Chương Chuyên Sâu",
    date: "2026-Reading",
    dataFile: "data/erica_reading.json",
    pdfDriveId: "10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z",
    pdfPreviewUrl: "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/preview",
    pdfViewUrl: "https://drive.google.com/file/d/10d5oocFy5VfhLfP1ZB88xAGRe-5TFl7Z/view",
    poster: "poster.png",
    total_questions: 101,
    time_minutes: 129,
    modules_count: 9,
    storageKey: "bluebook_erica_reading_student_state_v1",
    description: "Bộ câu hỏi toàn diện 9 chương sách The Critical Reader: The Complete Guide to SAT Reading (Erica Meltzer) gồm 101 câu (27 ví dụ minh họa kèm bài giảng + 74 câu thực hành) phân tách chi tiết theo từng chương kèm chiến thuật cốt lõi, bẫy SAT và gợi ý Socratic đa tầng."
  },
  {
    id: "panda-math",
    code: "pandamath",
    title: "The College Panda: SAT Math Advanced Guide & Workbook (Nielson Phu)",
    short_title: "College Panda Math",
    badge: "27 Chương Chuyên Sâu",
    date: "2026-Math",
    dataFile: "data/panda_math.json",
    pdfDriveId: "1z4CC7X-L3e3XZr04uc7RgMZBK5lYs8Gb",
    pdfPreviewUrl: "https://drive.google.com/file/d/1z4CC7X-L3e3XZr04uc7RgMZBK5lYs8Gb/preview",
    pdfViewUrl: "https://drive.google.com/file/d/1z4CC7X-L3e3XZr04uc7RgMZBK5lYs8Gb/view?usp=drive_open",
    poster: "poster.png",
    total_questions: 330,
    time_minutes: 360,
    modules_count: 27,
    storageKey: "bluebook_panda_math_student_state_v1",
    description: "Bộ 330 câu hỏi luyện tập chuyên sâu 27 chương sách The College Panda SAT Math (Nielson Phu) kèm chiến thuật cốt lõi, công thức then chốt, bẫy SAT và gợi ý Socratic đa tầng."
  },
  {
    id: "erica-writing",
    code: "ericawriting",
    title: "The Ultimate Guide to SAT Grammar (Erica Meltzer - 6th Edition)",
    short_title: "Erica Meltzer Writing",
    badge: "17 Chuyên Đề Grammar",
    date: "2026-Writing",
    dataFile: "data/erica_writing.json",
    pdfDriveId: "1RRTBIfpSDD6AyaPJNmfK54fyoXmvNu-s",
    pdfPreviewUrl: "https://drive.google.com/file/d/1RRTBIfpSDD6AyaPJNmfK54fyoXmvNu-s/preview",
    pdfViewUrl: "https://drive.google.com/file/d/1RRTBIfpSDD6AyaPJNmfK54fyoXmvNu-s/view",
    poster: "poster.png",
    total_questions: 334,
    time_minutes: 352,
    modules_count: 17,
    storageKey: "bluebook_erica_writing_student_state_v1",
    description: "Bộ câu hỏi toàn diện sách The Ultimate Guide to SAT Grammar 6th Edition (Erica Meltzer) gồm 334 câu (62 ví dụ minh họa + 272 bài tập thực hành, Practice Sets 1–5, Cumulative Reviews & Parts of Speech) kèm gợi ý Socratic 4 tầng và Answer Key chính xác từ sách gốc."
  }
];

// Determine initial test ID from URL params or local preference
function detectInitialTestId() {
  try {
    const urlParams = new URLSearchParams(window.location.search);
    const paramTest = urlParams.get("test");
    if (paramTest) {
      const clean = paramTest.toLowerCase().replace(/[^a-z0-9]/g, "");
      if (clean.includes("panda") || clean.includes("nielson") || clean.includes("math")) return "panda-math";
      if (clean.includes("writing") || clean.includes("grammar")) return "erica-writing";
      if (clean.includes("erica") || clean.includes("reading")) return "erica-reading";
      if (clean.includes("sep")) return "sep-2026";
      if (clean.includes("oct")) return "oct-2026";
      return paramTest;
    }
    const hash = window.location.hash || "";
    if (hash.includes("panda") || hash.includes("nielson") || hash.includes("math")) return "panda-math";
    if (hash.includes("writing") || hash.includes("grammar")) return "erica-writing";
    if (hash.includes("erica") || hash.includes("reading")) return "erica-reading";
    if (hash.includes("sep")) return "sep-2026";
    if (hash.includes("oct")) return "oct-2026";

    const saved = localStorage.getItem("bluebook_selected_test_id");
    if (saved) return saved;
  } catch (e) {}
  return "oct-2026";
}

// Application State
const App = {
  testsManifest: (window.TESTS_MANIFEST && window.TESTS_MANIFEST.length) ? window.TESTS_MANIFEST : TESTS_MANIFEST_DEFAULT,
  activeTestId: detectInitialTestId(),
  activeTest: null,
  db: null,
  activeModuleCode: "RW_Module1",
  questions: [],
  currentIndex: 0,
  currentQuestion: null,
  selectedChoice: null,
  eliminatorMode: false,
  timerInterval: null,
  timerRunning: false, // Default paused until student starts practice
  manualPause: false,  // Student clicked pause button manually
  timerHidden: false,
  pdfViewerMode: "drive", // Standard Google Drive viewer
  notebookFilterStatus: "all",
  notebookSearchQuery: "",
  editingLogId: null,
  feedbacks: [],
  currentFeedbackContext: null,
  lastMailtoUrl: null,
  lastReportText: "",
  sessionStartedAt: new Date().toISOString(),
  sessionPracticedIds: new Set(),
  globalSessionItems: {},
  aarScope: "session",
  aarLogs: [],
  lastAarReportAt: null,
  aarDraft: {
    session_label: "",
    sat_module: "",
    sat_module_custom: "",
    sat_module_user_set: false,
    iste_standard: "",
    iste_user_set: false,
    goal: "",
    challenge: "",
    updated_at: null
  },

  // Student Personal State (Loaded from localStorage)
  studentState: {
    student_name: "",
    student_email: "",
    student_target: "1400+",
    active_module: "RW_Module1",
    active_q_index: 0,
    attempts: {}, // [qid]: { attempts: [], status: "unanswered", efficiency: 0.0, marked: false, eliminated: [] }
    error_logs: [],
    timer_seconds: {
      "RW_Module1": 32 * 60,
      "RW_Module2": 32 * 60,
      "Math_Module1": 35 * 60,
      "Math_Module2": 35 * 60,
      "ALL": 134 * 60
    }
  }
};

function getActiveTestMeta() {
  const match = (App.testsManifest || []).find(t => t.id === App.activeTestId || t.code === App.activeTestId);
  return match || App.testsManifest[0] || TESTS_MANIFEST_DEFAULT[0];
}

function getStorageKeyForTest(testId) {
  const meta = (App.testsManifest || []).find(t => t.id === testId || t.code === testId);
  if (meta && meta.storageKey) return meta.storageKey;
  return `bluebook_${testId}_student_state_v1`;
}

// DOM Cache
const DOM = {
  // Views
  viewHome: document.getElementById("view-home"),
  viewPractice: document.getElementById("view-practice"),

  // Multi-Exam Switcher Elements
  selectActiveExam: document.getElementById("select-active-exam"),
  selectPracticeExam: document.getElementById("select-practice-exam"),
  homeBrandBadge: document.getElementById("home-brand-badge"),
  heroMainTitle: document.getElementById("hero-main-title"),
  heroTitleGradient: document.getElementById("hero-title-gradient"),
  heroMainDesc: document.getElementById("hero-main-desc"),
  heroPosterImg: document.getElementById("hero-poster-img"),
  btnHeroDrivePdf: document.getElementById("btn-hero-drive-pdf"),
  examsGrid: document.getElementById("exams-grid"),
  practiceTestBadge: document.getElementById("practice-test-badge"),
  modulesSectionTag: document.getElementById("modules-section-tag"),
  modulesSectionTitle: document.getElementById("modules-section-title"),
  modulesSectionDesc: document.getElementById("modules-section-desc"),
  modulesGrid: document.getElementById("modules-grid"),
  pageModRw1: document.getElementById("page-mod-rw1"),
  pageModRw2: document.getElementById("page-mod-rw2"),
  pageModMath1: document.getElementById("page-mod-math1"),
  pageModMath2: document.getElementById("page-mod-math2"),

  // Home Page Elements
  btnHeroEnterTest: document.getElementById("btn-hero-enter-test"),
  homeUserChip: document.getElementById("home-user-chip"),
  homeStudentNameChip: document.getElementById("home-student-name-chip"),
  homeInputName: document.getElementById("home-input-name"),
  homeInputEmail: document.getElementById("home-input-email"),
  targetChipsContainer: document.getElementById("target-chips-container"),
  homeAarSyncBadge: document.getElementById("home-aar-sync-badge"),
  homeAarSession: document.getElementById("home-aar-session"),
  homeAarSatModule: document.getElementById("home-aar-sat-module"),
  homeAarSatModuleCustom: document.getElementById("home-aar-sat-module-custom"),
  homeAarIste: document.getElementById("home-aar-iste"),
  homeAarIsteHint: document.getElementById("home-aar-iste-hint"),
  homeGoalTargetPill: document.getElementById("home-goal-target-pill"),
  homeAarGoal: document.getElementById("home-aar-goal"),
  homeAarChallenge: document.getElementById("home-aar-challenge"),
  btnHomeStartPractice: document.getElementById("btn-home-start-practice"),
  btnHomeViewGuide: document.getElementById("btn-home-view-guide"),

  // Practice Header
  btnHome: document.getElementById("btn-home"),
  selectModule: document.getElementById("select-active-module"),
  timerDisplay: document.getElementById("timer-display"),
  btnTimerToggleView: document.getElementById("btn-timer-toggle-view"),
  btnTimerPause: document.getElementById("btn-timer-pause"),
  btnOpenCalc: document.getElementById("btn-open-calc"),
  btnOpenRef: document.getElementById("btn-open-ref"),
  btnToggleScratchpad: document.getElementById("btn-toggle-scratchpad"),
  btnOpenErrorLog: document.getElementById("btn-open-error-log"),
  badgeErrorCount: document.getElementById("badge-error-count"),
  btnOpenVocab: document.getElementById("btn-open-vocab"),
  btnOpenStrategies: document.getElementById("btn-open-strategies"),
  btnExportExcel: document.getElementById("btn-export-excel"),
  headerSessionCounter: document.getElementById("header-session-counter"),
  headerSessionCountVal: document.getElementById("header-session-count-val"),
  btnResetTest: document.getElementById("btn-reset-test"),
  btnOpenAar: document.getElementById("btn-open-aar"),
  btnHomeOpenAar: document.getElementById("btn-home-open-aar"),
  headerStudentBadge: document.getElementById("header-student-badge"),
  headerStudentName: document.getElementById("header-student-name"),
  btnEditStudent: document.getElementById("btn-edit-student"),

  // Zen Mode & Tablet Controls (Trụ cột 4 & 5)
  btnToggleZen: document.getElementById("btn-toggle-zen"),
  zenFloatingPill: document.getElementById("zen-floating-pill"),
  zenTimerDisplay: document.getElementById("zen-timer-display"),
  zenBtnCalc: document.getElementById("zen-btn-calc"),
  btnExitZen: document.getElementById("btn-exit-zen"),
  tabletPaneToggle: document.getElementById("tablet-pane-toggle"),
  btnTabPanePdf: document.getElementById("btn-tab-pane-pdf"),
  btnTabPaneContent: document.getElementById("btn-tab-pane-content"),
  btnTabletToQuestion: document.getElementById("btn-tablet-to-question"),

  // Split & PDF
  splitContainer: document.getElementById("split-container"),
  panePdf: document.getElementById("pane-pdf"),
  splitDivider: document.getElementById("split-divider"),
  pdfFrame: document.getElementById("pdf-frame"),
  pdfPageBadge: document.getElementById("pdf-page-badge"),
  pdfSyncPageNum: document.getElementById("pdf-sync-page-num"),
  btnPdfExternal: document.getElementById("btn-pdf-external"),

  // Question Top & Actions
  questionTopBar: document.getElementById("question-top-bar"),
  responseInstruction: document.getElementById("response-instruction"),
  qActionRow: document.getElementById("q-action-row"),
  qNumberLabel: document.getElementById("q-number-label"),
  qTopicBadge: document.getElementById("q-topic-badge"),
  qDomainBadge: document.getElementById("q-domain-badge"),
  chkMarkReview: document.getElementById("chk-mark-review"),
  markReviewLabel: document.querySelector(".mark-review-label"),
  btnToggleEliminator: document.getElementById("btn-toggle-eliminator"),
  btnQMermaid: document.getElementById("btn-q-mermaid"),

  // Excerpt
  excerptHeader: document.getElementById("excerpt-header"),
  excerptBody: document.getElementById("excerpt-body"),
  excerptToggleIcon: document.getElementById("excerpt-toggle-icon"),
  excerptPassage: document.getElementById("excerpt-passage"),
  excerptPrompt: document.getElementById("excerpt-prompt"),

  // Response Areas
  mcqResponseArea: document.getElementById("mcq-response-area"),
  questionStemBox: document.getElementById("question-stem-box"),
  questionStemText: document.getElementById("question-stem-text"),
  optionsContainer: document.getElementById("options-container"),
  gridinResponseArea: document.getElementById("gridin-response-area"),
  gridinInput: document.getElementById("gridin-input"),

  // Attempts & Feedback
  slotL1: document.getElementById("slot-l1"),
  slotL2: document.getElementById("slot-l2"),
  slotL3: document.getElementById("slot-l3"),
  effVal: document.getElementById("eff-val"),
  btnCheckAnswer: document.getElementById("btn-check-answer"),
  statusAlert: document.getElementById("status-alert"),
  alertIcon: document.getElementById("alert-icon"),
  alertText: document.getElementById("alert-text"),

  // Hints
  hintCard1: document.getElementById("hint-card-1"),
  hintHead1: document.getElementById("hint-head-1"),
  hintContent1: document.getElementById("hint-content-1"),
  hintText1: document.getElementById("hint-text-1"),

  hintCard2: document.getElementById("hint-card-2"),
  hintHead2: document.getElementById("hint-head-2"),
  hintContent2: document.getElementById("hint-content-2"),
  hintText2: document.getElementById("hint-text-2"),

  hintCard3: document.getElementById("hint-card-3"),
  hintHead3: document.getElementById("hint-head-3"),
  hintContent3: document.getElementById("hint-content-3"),
  hintText3: document.getElementById("hint-text-3"),

  hintCard4: document.getElementById("hint-card-4"),
  hintHead4: document.getElementById("hint-head-4"),
  hintContent4: document.getElementById("hint-content-4"),
  hintText4: document.getElementById("hint-text-4"),

  // Visual Thinking Diagram (Mermaid Pop-up Modal)
  modalMermaid: document.getElementById("modal-mermaid"),
  mermaidModalCard: document.getElementById("mermaid-modal-card"),
  mermaidModalTitle: document.getElementById("mermaid-modal-title"),
  mermaidModalSubtitle: document.getElementById("mermaid-modal-subtitle"),
  mermaidTriggerBanner: document.getElementById("mermaid-trigger-banner"),
  btnOpenMermaidModal: document.getElementById("btn-open-mermaid-modal"),
  btnCloseMermaid: document.getElementById("btn-close-mermaid"),
  mermaidViewport: document.getElementById("mermaid-viewport"),
  mermaidCanvas: document.getElementById("mermaid-canvas"),
  mermaidViewer: document.getElementById("mermaid-viewer"),
  btnMmZoomIn: document.getElementById("btn-mm-zoom-in"),
  btnMmZoomOut: document.getElementById("btn-mm-zoom-out"),
  btnMmZoomReset: document.getElementById("btn-mm-zoom-reset"),
  mmZoomLevel: document.getElementById("mm-zoom-level"),

  // Footer Dock
  inputStudentName: document.getElementById("input-student-name"),
  btnOpenNavigator: document.getElementById("btn-open-navigator"),
  navCurrentLabel: document.getElementById("nav-current-label"),
  navTotalLabel: document.getElementById("nav-total-label"),
  btnNavBack: document.getElementById("btn-nav-back"),
  btnNavNext: document.getElementById("btn-nav-next"),

  // Navigator Modal
  navigatorOverlay: document.getElementById("navigator-modal-overlay"),
  btnCloseNavigator: document.getElementById("btn-close-navigator"),
  navModalModuleTitle: document.getElementById("nav-modal-module-title"),
  navTilesGrid: document.getElementById("nav-tiles-grid"),

  // Modals
  modalCalculator: document.getElementById("modal-calculator"),
  calcModalHeader: document.getElementById("calc-modal-header"),
  btnCloseCalculator: document.getElementById("btn-close-calculator"),
  modalReference: document.getElementById("modal-reference"),
  btnCloseReference: document.getElementById("btn-close-reference"),
  modalAceSATVocab: document.getElementById("modal-acesat-vocab"),
  btnCloseAceSATVocab: document.getElementById("btn-close-acesat-vocab"),

  // Socratic Error & Vocabulary Notebook
  modalErrorLog: document.getElementById("modal-error-log"),
  btnCloseErrorLog: document.getElementById("btn-close-error-log"),
  btnAddNewError: document.getElementById("btn-add-new-error"),
  errorLogList: document.getElementById("error-log-list"),
  inputFilterErrSearch: document.getElementById("input-filter-err-search"),
  btnClearErrSearch: document.getElementById("btn-clear-err-search"),
  badgeNotebookCount: document.getElementById("badge-notebook-count"),
  notebookFilterChips: document.getElementById("notebook-filter-chips"),
  countChipAll: document.getElementById("count-chip-all"),
  countChipPending: document.getElementById("count-chip-pending"),
  countChipTracking: document.getElementById("count-chip-tracking"),
  countChipResolved: document.getElementById("count-chip-resolved"),
  notebookAddPanel: document.getElementById("notebook-add-panel"),
  addPanelQBadge: document.getElementById("add-panel-q-badge"),
  selectNewTrap: document.getElementById("select-new-trap"),
  selectNewStatus: document.getElementById("select-new-status"),
  inputNewDetail: document.getElementById("input-new-detail"),
  inputNewNotes: document.getElementById("input-new-notes"),
  inputNewVocab: document.getElementById("input-new-vocab"),
  btnSaveNewError: document.getElementById("btn-save-new-error"),
  btnCancelAddError: document.getElementById("btn-cancel-add-error"),

  modalStrategies: document.getElementById("modal-strategies"),
  btnCloseStrategies: document.getElementById("btn-close-strategies"),
  strategiesContent: document.getElementById("strategies-content"),

  // Scratchpad & Whiteboard
  scratchpadDrawer: document.getElementById("scratchpad-drawer"),
  scratchpadHeader: document.getElementById("scratchpad-header"),
  scratchpadBody: document.getElementById("scratchpad-body"),
  scratchpadCanvas: document.getElementById("scratchpad-canvas"),
  scratchpadTextLayer: document.getElementById("scratchpad-text-layer"),
  btnScratchToolPen: document.getElementById("btn-scratch-tool-pen"),
  btnScratchToolText: document.getElementById("btn-scratch-tool-text"),
  btnScratchAddTextbox: document.getElementById("btn-scratch-add-textbox"),
  btnScratchClear: document.getElementById("btn-scratch-clear"),
  btnScratchClose: document.getElementById("btn-scratch-close"),
  colorButtons: document.querySelectorAll(".color-btn"),

  // Guide / Onboarding Modal
  modalOnboarding: document.getElementById("modal-onboarding"),
  btnCloseOnboarding: document.getElementById("btn-close-onboarding"),
  btnGuideDismiss: document.getElementById("btn-guide-dismiss"),
  obPreviewName: document.getElementById("ob-preview-name"),
  obPreviewEmail: document.getElementById("ob-preview-email"),
  btnObStart: document.getElementById("btn-ob-start"),

  // Mandatory Reflection Modal
  modalMandatoryReflection: document.getElementById("modal-mandatory-reflection"),
  reflQLabel: document.getElementById("refl-q-label"),
  reflQTopic: document.getElementById("refl-q-topic"),
  reflQModule: document.getElementById("refl-q-module"),
  reflCorrectAns: document.getElementById("refl-correct-ans"),
  reflWrongPicks: document.getElementById("refl-wrong-picks"),
  reflHintBox: document.getElementById("refl-hint-box"),
  selectReflTrap: document.getElementById("select-refl-trap"),
  inputReflDetail: document.getElementById("input-refl-detail"),
  inputReflNotes: document.getElementById("input-refl-notes"),
  inputReflVocab: document.getElementById("input-refl-vocab"),
  btnSaveReflAndReview: document.getElementById("btn-save-refl-and-review"),
  btnSaveMandatoryReflection: document.getElementById("btn-save-mandatory-reflection"),

  // Success Modal
  modalSubmitSuccess: document.getElementById("modal-submit-success"),
  successModalTitle: document.getElementById("success-modal-title"),
  successStatusText: document.getElementById("success-status-text"),
  successFilename: document.getElementById("success-filename"),
  successRecipientText: document.getElementById("success-recipient-text"),
  btnRelaunchMail: document.getElementById("btn-relaunch-mail"),
  btnCopyMailBody: document.getElementById("btn-copy-mail-body"),
  btnDownloadSubmittedFile: document.getElementById("btn-download-submitted-file"),
  btnCloseSuccess: document.getElementById("btn-close-success"),

  // AAR / ARR Cycle Modal
  modalAarReport: document.getElementById("modal-aar-report"),
  btnCloseAar: document.getElementById("btn-close-aar"),
  tabBtnAarForm: document.getElementById("tab-btn-aar-form"),
  tabBtnAarHistory: document.getElementById("tab-btn-aar-history"),
  aarHistoryCount: document.getElementById("aar-history-count"),
  aarTabPanelForm: document.getElementById("aar-tab-panel-form"),
  aarTabPanelHistory: document.getElementById("aar-tab-panel-history"),
  aarInputStudentName: document.getElementById("aar-input-student-name"),
  aarInputStudentEmail: document.getElementById("aar-input-student-email"),
  aarPerfHeadline: document.getElementById("aar-perf-headline"),
  aarPerfSub: document.getElementById("aar-perf-sub"),
  aarScopePills: document.getElementById("aar-scope-pills"),
  aarStatCorrect: document.getElementById("aar-stat-correct"),
  aarStatPct: document.getElementById("aar-stat-pct"),
  aarStatL1: document.getElementById("aar-stat-l1"),
  aarStatL23: document.getElementById("aar-stat-l23"),
  aarStatMissed: document.getElementById("aar-stat-missed"),
  aarInputSessionLabel: document.getElementById("aar-input-session-label"),
  aarInputDate: document.getElementById("aar-input-date"),
  aarSelectSatModule: document.getElementById("aar-select-sat-module"),
  aarInputSatModuleCustom: document.getElementById("aar-input-sat-module-custom"),
  aarSelectIste: document.getElementById("aar-select-iste"),
  aarIsteHint: document.getElementById("aar-iste-hint"),
  aarInputGoal: document.getElementById("aar-input-goal"),
  aarInputChallenge: document.getElementById("aar-input-challenge"),
  aarTargetScorePill: document.getElementById("aar-target-score-pill"),
  aarInputTools: document.getElementById("aar-input-tools"),
  aarSelectMastery: document.getElementById("aar-select-mastery"),
  aarInputEvidence: document.getElementById("aar-input-evidence"),
  btnAarPullErrors: document.getElementById("btn-aar-pull-errors"),
  aarInputGap: document.getElementById("aar-input-gap"),
  aarInputFeedforward: document.getElementById("aar-input-feedforward"),
  aarSelectEmotion: document.getElementById("aar-select-emotion"),
  aarSelectStatus: document.getElementById("aar-select-status"),
  aarPreviewCcEmail: document.getElementById("aar-preview-cc-email"),
  btnAarSubmitSend: document.getElementById("btn-aar-submit-send"),
  aarSubmitBtnText: document.getElementById("aar-submit-btn-text"),
  aarSubmitSpinner: document.getElementById("aar-submit-spinner"),
  btnAarDownloadOnly: document.getElementById("btn-aar-download-only"),
  btnAarCancel: document.getElementById("btn-aar-cancel"),
  aarHistorySummary: document.getElementById("aar-history-summary"),
  btnAarExportAllHistory: document.getElementById("btn-aar-export-all-history"),
  aarHistoryList: document.getElementById("aar-history-list"),

  // Reset Confirmation Modal
  modalResetConfirm: document.getElementById("modal-reset-confirm"),
  chkResetAnswers: document.getElementById("chk-reset-answers"),
  chkResetSessionCounter: document.getElementById("chk-reset-session-counter"),
  chkResetTimer: document.getElementById("chk-reset-timer"),
  chkResetErrors: document.getElementById("chk-reset-errors"),
  btnConfirmDoReset: document.getElementById("btn-confirm-do-reset"),
  btnCancelReset: document.getElementById("btn-cancel-reset"),

  // Smart Feedback
  btnFloatingFeedback: document.getElementById("btn-floating-feedback"),
  btnQFeedback: document.getElementById("btn-q-feedback"),
  modalFeedback: document.getElementById("modal-feedback"),
  btnCloseFeedback: document.getElementById("btn-close-feedback"),
  tabBtnFbNew: document.getElementById("tab-btn-fb-new"),
  tabBtnFbHistory: document.getElementById("tab-btn-fb-history"),
  fbTabContentNew: document.getElementById("fb-tab-content-new"),
  fbTabContentHistory: document.getElementById("fb-tab-content-history"),
  fbHistoryCount: document.getElementById("fb-history-count"),
  fbDetectedContext: document.getElementById("fb-detected-context"),
  btnToggleCustomContext: document.getElementById("btn-toggle-custom-context"),
  groupCustomContext: document.getElementById("group-custom-context"),
  selectFbCustomModule: document.getElementById("select-fb-custom-module"),
  formSubmitFeedback: document.getElementById("form-submit-feedback"),
  selectFbCategory: document.getElementById("select-fb-category"),
  selectFbPriority: document.getElementById("select-fb-priority"),
  inputFbContent: document.getElementById("input-fb-content"),
  inputFbName: document.getElementById("input-fb-name"),
  inputFbEmail: document.getElementById("input-fb-email"),
  btnSubmitFeedback: document.getElementById("btn-submit-feedback"),
  fbSuccessBanner: document.getElementById("fb-success-banner"),
  fbSuccessMsg: document.getElementById("fb-success-msg"),
  btnSendAnotherFb: document.getElementById("btn-send-another-fb"),
  fbHistoryList: document.getElementById("fb-history-list")
};

// ================= LOCALSTORAGE MANAGER (MULTI-TEST & GLOBAL PROFILE) =================
function loadLocalState() {
  try {
    // 1. Load Global Student Profile (Shared across tests)
    let globalProfile = null;
    const rawProfile = localStorage.getItem(GLOBAL_PROFILE_KEY);
    if (rawProfile) {
      globalProfile = JSON.parse(rawProfile);
    } else {
      // Legacy fallback
      const legacyRaw = localStorage.getItem(LEGACY_STORAGE_KEY);
      if (legacyRaw) {
        const parsed = JSON.parse(legacyRaw);
        globalProfile = {
          student_name: parsed.student_name || "",
          student_email: parsed.student_email || "",
          student_target: parsed.student_target || "1400+",
          selected_test_id: "oct-2026"
        };
        localStorage.setItem(GLOBAL_PROFILE_KEY, JSON.stringify(globalProfile));
      }
    }

    if (globalProfile) {
      App.studentState.student_name = globalProfile.student_name || "";
      App.studentState.student_email = globalProfile.student_email || "";
      App.studentState.student_target = globalProfile.student_target || "1400+";
    }

    // 2. Load Scoped Test Progress
    const testKey = getStorageKeyForTest(App.activeTestId);
    let testRaw = localStorage.getItem(testKey);

    // Fallback for oct-2026 to legacy key
    if (!testRaw && (App.activeTestId === "oct-2026" || App.activeTestId === "oct2026")) {
      testRaw = localStorage.getItem(LEGACY_STORAGE_KEY);
    }

    if (testRaw) {
      const parsedTest = JSON.parse(testRaw);
      App.studentState.attempts = parsedTest.attempts || {};
      App.studentState.active_module = parsedTest.active_module || "RW_Module1";
      App.studentState.active_q_index = parsedTest.active_q_index || 0;
      App.activeModuleCode = App.studentState.active_module;

      // Purge any legacy default/seeded error logs
      if (parsedTest.error_logs) {
        App.studentState.error_logs = parsedTest.error_logs.filter(e => e && e.id && !e.id.startsWith("err_oct_"));
      } else {
        App.studentState.error_logs = [];
      }

      if (parsedTest.timer_seconds) {
        App.studentState.timer_seconds = parsedTest.timer_seconds;
      } else {
        App.studentState.timer_seconds = {
          "RW_Module1": 32 * 60,
          "RW_Module2": 32 * 60,
          "Math_Module1": 35 * 60,
          "Math_Module2": 35 * 60,
          "ALL": 134 * 60
        };
      }
    } else {
      App.studentState.attempts = {};
      App.studentState.error_logs = [];
      App.studentState.timer_seconds = {
        "RW_Module1": 32 * 60,
        "RW_Module2": 32 * 60,
        "Math_Module1": 35 * 60,
        "Math_Module2": 35 * 60,
        "ALL": 134 * 60
      };
    }
  } catch (e) {
    console.warn("Could not load from localStorage:", e);
    App.studentState.attempts = {};
    App.studentState.error_logs = [];
  }

  // Restore student profile UI
  if (App.studentState.student_name) {
    if (DOM.homeInputName) DOM.homeInputName.value = App.studentState.student_name;
    if (DOM.headerStudentName) DOM.headerStudentName.textContent = App.studentState.student_name;
  }
  if (App.studentState.student_email && DOM.homeInputEmail) {
    DOM.homeInputEmail.value = App.studentState.student_email;
  }

  loadGlobalAARState();
  loadGlobalSessionTracker();
}

function saveLocalState() {
  try {
    // 1. Save Global Student Profile
    const profile = {
      student_name: App.studentState.student_name || "",
      student_email: App.studentState.student_email || "",
      student_target: App.studentState.student_target || "1400+",
      selected_test_id: App.activeTestId
    };
    localStorage.setItem(GLOBAL_PROFILE_KEY, JSON.stringify(profile));
    localStorage.setItem("bluebook_selected_test_id", App.activeTestId);

    // 2. Save Test-Specific State
    const testState = {
      active_module: App.activeModuleCode || "RW_Module1",
      active_q_index: App.currentIndex || 0,
      attempts: App.studentState.attempts || {},
      error_logs: App.studentState.error_logs || [],
      timer_seconds: App.studentState.timer_seconds || {}
    };
    const testKey = getStorageKeyForTest(App.activeTestId);
    localStorage.setItem(testKey, JSON.stringify(testState));

    // Backward compatibility mirror for oct-2026
    if (App.activeTestId === "oct-2026" || App.activeTestId === "oct2026") {
      localStorage.setItem(LEGACY_STORAGE_KEY, JSON.stringify(App.studentState));
    }
  } catch (e) {
    console.warn("Could not save to localStorage:", e);
  }
}

// ================= VIEW CONTROLLER (GOOGLE UX LANDING & PRACTICE) =================
function showView(viewName) {
  if (viewName === "home") {
    document.body.classList.remove("in-practice");
    document.body.classList.remove("zen-mode");
    if (DOM.zenFloatingPill) DOM.zenFloatingPill.classList.add("hidden");
    if (DOM.viewHome) {
      DOM.viewHome.classList.remove("hidden");
      DOM.viewHome.style.display = "flex";
    }
    if (DOM.viewPractice) {
      DOM.viewPractice.classList.add("hidden");
      DOM.viewPractice.style.display = "none";
    }
    pauseTimer();
    syncHomeProfile();
    updateModuleCardStats();
    if (DOM.viewHome) DOM.viewHome.scrollTo({ top: 0, behavior: "smooth" });
    window.scrollTo({ top: 0, behavior: "smooth" });
  } else {
    document.body.classList.add("in-practice");
    const savedZen = localStorage.getItem("bluebook_zen_mode");
    if (savedZen === "active") {
      toggleZenMode(true);
    }
    if (DOM.viewHome) {
      DOM.viewHome.classList.add("hidden");
      DOM.viewHome.style.display = "none";
    }
    if (DOM.viewPractice) {
      DOM.viewPractice.classList.remove("hidden");
      DOM.viewPractice.style.display = "flex";
    }
    if (DOM.modalOnboarding) {
      DOM.modalOnboarding.classList.add("hidden");
      DOM.modalOnboarding.style.display = "none";
    }
    resumeTimer();
    renderCurrentQuestion();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
}

function syncHomeProfile() {
  const name = App.studentState.student_name || "";
  const email = App.studentState.student_email || "";
  const target = App.studentState.student_target || "1400+";

  if (DOM.homeInputName) DOM.homeInputName.value = name;
  if (DOM.homeInputEmail) DOM.homeInputEmail.value = email;

  if (DOM.homeStudentNameChip) {
    if (name) {
      DOM.homeStudentNameChip.textContent = name;
      if (DOM.homeUserChip) DOM.homeUserChip.title = `Học sinh: ${name} (${email || "Chưa có email"})`;
    } else {
      DOM.homeStudentNameChip.textContent = "Chưa đăng ký";
      if (DOM.homeUserChip) DOM.homeUserChip.title = "Học sinh đang tham gia";
    }
  }

  if (DOM.targetChipsContainer) {
    const chips = DOM.targetChipsContainer.querySelectorAll(".target-chip");
    chips.forEach(chip => {
      if (chip.getAttribute("data-val") === target) {
        chip.classList.add("active");
      } else {
        chip.classList.remove("active");
      }
    });
  }

  if (typeof syncAarAnticipationUI === "function") {
    syncAarAnticipationUI();
  }
}

function updateModuleCardStats() {
  renderModuleCards();
}

function renderModuleCards() {
  if (!DOM.modulesGrid || !App.db || !App.db.questions) return;

  const isErica = App.activeTestId === "erica-reading";
  const isEricaWriting = App.activeTestId === "erica-writing";
  const isPanda = App.activeTestId === "panda-math";
  const isChapterBased = isErica || isEricaWriting || isPanda;

  if (isChapterBased) {
    if (isErica) {
      if (DOM.modulesSectionTag) DOM.modulesSectionTag.textContent = "9 CHƯƠNG CHIẾN THUẬT ERICA MELTZER";
      if (DOM.modulesSectionTitle) DOM.modulesSectionTitle.textContent = "Luyện Tập Từng Chương Sách The Critical Reader";
      if (DOM.modulesSectionDesc) DOM.modulesSectionDesc.textContent = "Em có thể chọn luyện tập từng chuyên đề riêng biệt theo phương pháp của Erica Meltzer hoặc làm toàn bộ 101 câu (27 ví dụ minh họa kèm bài giảng + 74 bài tập thực hành).";
    } else if (isEricaWriting) {
      if (DOM.modulesSectionTag) DOM.modulesSectionTag.textContent = "17 CHUYÊN ĐỀ GRAMMAR ERICA MELTZER (6TH ED.)";
      if (DOM.modulesSectionTitle) DOM.modulesSectionTitle.textContent = "Luyện Tập Toàn Diện SAT Grammar & Writing";
      if (DOM.modulesSectionDesc) DOM.modulesSectionDesc.textContent = "Em có thể chọn từng chuyên đề từ Chương 1–12, Parts of Speech, Cumulative Reviews hay 5 Practice Sets (tổng 334 câu: 62 ví dụ minh họa + 272 câu thực hành) kèm Answer Key chuẩn sách gốc.";
    } else {
      if (DOM.modulesSectionTag) DOM.modulesSectionTag.textContent = "27 CHƯƠNG CHUYÊN SÂU THE COLLEGE PANDA";
      if (DOM.modulesSectionTitle) DOM.modulesSectionTitle.textContent = "Luyện Tập Từng Chuyên Đề SAT Math (Nielson Phu)";
      if (DOM.modulesSectionDesc) DOM.modulesSectionDesc.textContent = "Em có thể chọn luyện tập từng chuyên đề riêng biệt theo phương pháp của Nielson Phu hoặc làm toàn bộ 330 câu hỏi SAT Math kèm máy tính Desmos, công thức chuẩn và Sổ thử sai.";
    }
    DOM.modulesGrid.classList.add("grid-chapters");

    DOM.modulesGrid.innerHTML = "";
    (App.db.modules || []).forEach(m => {
      const modQuestions = App.db.questions.filter(q => q.module_code === m.code);
      const total = modQuestions.length;
      const exCount = modQuestions.filter(q => q.category === "example").length;
      const prCount = modQuestions.filter(q => q.category === "practice").length;
      let answeredCount = 0;
      let correctCount = 0;

      modQuestions.forEach(q => {
        const att = App.studentState.attempts[q.id];
        if (att && att.status && att.status !== "unanswered") {
          answeredCount++;
          if (att.status === "correct" || (typeof att.status === "string" && att.status.startsWith("mastered"))) correctCount++;
        }
      });

      const card = document.createElement("div");
      card.className = "module-card";
      card.dataset.module = m.code;

      const titleClean = (m.short_title || m.title || "").replace(/^Chương \d+:\s*/, "");
      const headingText = m.card_heading || (m.chapter_num ? `Chương ${m.chapter_num}: ${titleClean}` : titleClean);
      const btnText = m.btn_label || (m.chapter_num ? `Luyện Tập Chương ${m.chapter_num} ➔` : `Luyện Tập ${titleClean} ➔`);
      const pageLabel = isEricaWriting && m.book_start_page ? m.book_start_page : (m.pdf_start_page || 1);
      const stratSnippet = m.strategy ? m.strategy.replace(/^[•\s]+/, "").slice(0, 95) + "..." : (isPanda ? "Công thức và chiến thuật toán SAT then chốt" : (isEricaWriting ? "Quy tắc ngữ pháp và dấu câu SAT trọng tâm" : "Chiến thuật đọc hiểu cốt lõi"));
      const countDetail = exCount > 0 
        ? `${total} Câu (${exCount} ví dụ + ${prCount} thực hành)`
        : `${total} Câu`;

      const pillClass = (m.section === "Math" || isPanda) ? "mod-math" : "mod-rw";
      const domainLabel = m.domain || (isPanda ? "Math" : (isEricaWriting ? "Writing & Grammar" : "Reading"));

      card.innerHTML = `
        <div class="mod-card-header">
          <span class="mod-pill ${pillClass}">${domainLabel}</span>
          <span class="mod-time">⏱️ ${m.time_minutes || 15} Phút</span>
        </div>
        <h3>${headingText}</h3>
        <p>${m.sub_title ? `<strong>${m.sub_title}</strong>: ` : ""}${stratSnippet}</p>
        <div class="mod-meta">
          <span>📖 Trang ${pageLabel}</span>
          <span class="mod-stat ${answeredCount > 0 ? "in-progress" : ""}">
            ${answeredCount > 0 ? `<strong>${answeredCount}/${total}</strong> đã làm (${correctCount} đúng)` : countDetail}
          </span>
        </div>
        <button type="button" class="btn-module-jump" data-module="${m.code}">${btnText}</button>
      `;

      card.addEventListener("click", () => {
        startPracticeFromHome(m.code);
      });

      DOM.modulesGrid.appendChild(card);
    });
  } else {
    // Standard 4 SAT Modules
    if (DOM.modulesSectionTag) DOM.modulesSectionTag.textContent = "CẤU TRÚC ĐỀ THI (4 MODULES)";
    if (DOM.modulesSectionTitle) DOM.modulesSectionTitle.textContent = "Chọn Module Để Bắt Đầu Luyện Tập";
    if (DOM.modulesSectionDesc) DOM.modulesSectionDesc.textContent = "Em có thể chọn luyện tập từng phần riêng biệt hoặc làm liên tục toàn bộ 98 câu.";
    DOM.modulesGrid.classList.remove("grid-chapters");

    const satDefs = [
      { code: "RW_Module1", title: "Module 1: Đọc & Viết Chuẩn", pill: "Reading & Writing", pillClass: "mod-rw", time: "⏱️ 32 Phút", desc: "27 câu hỏi trắc nghiệm kiểm tra từ vựng ngữ cảnh, cấu trúc văn bản, suy luận và ngữ pháp chuẩn.", defaultPage: "📖 Trang 3 – 14", total: 27 },
      { code: "RW_Module2", title: "Module 2: Đọc & Viết Phân Hóa", pill: "Reading & Writing", pillClass: "mod-rw", time: "⏱️ 32 Phút", desc: "27 câu hỏi nâng cao với các đoạn văn khoa học phức tạp, biểu đồ dữ liệu và cặp văn bản đối chiếu.", defaultPage: "📖 Trang 16 – 25", total: 27 },
      { code: "Math_Module1", title: "Module 1: Toán Chuẩn", pill: "Math", pillClass: "mod-math", time: "⏱️ 35 Phút", desc: "22 câu hỏi đại số tuyến tính, phương trình bậc hai, hình học và thống kê kèm máy tính Desmos.", defaultPage: "📖 Trang 29 – 35", total: 22 },
      { code: "Math_Module2", title: "Module 2: Toán Nâng Cao", pill: "Math", pillClass: "mod-math", time: "⏱️ 35 Phút", desc: "22 câu hỏi phân hóa đỉnh cao với hàm phi tuyến tính, hình học không gian và các câu điền số Grid-in.", defaultPage: "📖 Trang 38 – 44", total: 22 }
    ];

    DOM.modulesGrid.innerHTML = "";
    satDefs.forEach(def => {
      const modQuestions = App.db.questions.filter(q => q.module_code === def.code);
      const total = modQuestions.length || def.total;
      let answeredCount = 0;
      let correctCount = 0;

      modQuestions.forEach(q => {
        const att = App.studentState.attempts[q.id];
        if (att && att.status && att.status !== "unanswered") {
          answeredCount++;
          if (att.status === "correct" || (typeof att.status === "string" && att.status.startsWith("mastered"))) correctCount++;
        }
      });

      let pageText = def.defaultPage;
      if (App.db.modules) {
        const mObj = App.db.modules.find(m => m.code === def.code);
        if (mObj) {
          const mIdx = App.db.modules.indexOf(mObj);
          const nextM = App.db.modules[mIdx + 1];
          const endP = nextM ? (nextM.pdf_start_page - 1) : (mObj.pdf_start_page + (def.code.startsWith("RW") ? 12 : 6));
          pageText = `📖 Trang ${mObj.pdf_start_page} – ${endP}`;
        }
      }

      const card = document.createElement("div");
      card.className = "module-card";
      card.dataset.module = def.code;
      card.innerHTML = `
        <div class="mod-card-header">
          <span class="mod-pill ${def.pillClass}">${def.pill}</span>
          <span class="mod-time">${def.time}</span>
        </div>
        <h3>${def.title}</h3>
        <p>${def.desc}</p>
        <div class="mod-meta">
          <span>${pageText}</span>
          <span class="mod-stat ${answeredCount > 0 ? "in-progress" : ""}">
            ${answeredCount > 0 ? `<strong>${answeredCount}/${total}</strong> đã làm (${correctCount} đúng)` : `${total} Câu`}
          </span>
        </div>
        <button type="button" class="btn-module-jump" data-module="${def.code}">Vào Thi ${def.title.split(":")[0]} ➔</button>
      `;

      card.addEventListener("click", () => {
        startPracticeFromHome(def.code);
      });

      DOM.modulesGrid.appendChild(card);
    });
  }
}

function flagHomeFieldError(el, message) {
  if (el) {
    el.focus();
    const wrap = el.parentElement;
    if (wrap) {
      wrap.classList.add("input-error");
      setTimeout(() => wrap.classList.remove("input-error"), 2000);
    }
    if (typeof el.scrollIntoView === "function") {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }
  alert(message);
}

function startPracticeFromHome(targetModule) {
  let name = (DOM.homeInputName ? DOM.homeInputName.value.trim() : "") || App.studentState.student_name;
  let email = (DOM.homeInputEmail ? DOM.homeInputEmail.value.trim() : "") || App.studentState.student_email;

  if (App.db && App.db.questions) {
    const qInMod = targetModule === "ALL" ? App.db.questions : App.db.questions.filter(q => q.module_code === targetModule);
    if (qInMod.length === 0) {
      targetModule = (App.db.modules && App.db.modules.length > 0) ? App.db.modules[0].code : "RW_Module1";
    }
  }

  if (!name || !email) {
    const missingEl = (!DOM.homeInputName || !DOM.homeInputName.value.trim()) ? DOM.homeInputName : DOM.homeInputEmail;
    flagHomeFieldError(missingEl, "Vui lòng điền đầy đủ Họ và tên cùng Địa chỉ email của em để bắt đầu bài làm!");
    return;
  }

  // Validate & auto-save Stage 1 Anticipation (ARR) before entering practice
  if (DOM.homeAarGoal && DOM.homeAarChallenge) {
    const draftGoal = DOM.homeAarGoal.value.trim();
    const draftChallenge = DOM.homeAarChallenge.value.trim();
    const draftMod = DOM.homeAarSatModule ? DOM.homeAarSatModule.value : "";
    const draftModCustom = DOM.homeAarSatModuleCustom ? DOM.homeAarSatModuleCustom.value.trim() : "";

    if (draftMod === "Khác (Tự nhập...)" && !draftModCustom) {
      flagHomeFieldError(DOM.homeAarSatModuleCustom, "Vui lòng nhập tên Mô-đun SAT / chủ đề em dự kiến luyện tập!");
      return;
    }
    if (!draftGoal) {
      flagHomeFieldError(DOM.homeAarGoal, "Vui lòng điền Mục tiêu bài học & Điểm kỳ vọng (phần Dự đoán trước buổi học - ARR) trước khi bắt đầu làm bài!");
      return;
    }
    if (!draftChallenge) {
      flagHomeFieldError(DOM.homeAarChallenge, "Vui lòng điền Thách thức dự kiến (phần Dự đoán trước buổi học - ARR) trước khi bắt đầu làm bài!");
      return;
    }
  }

  App.studentState.student_name = name;
  App.studentState.student_email = email;

  if (DOM.targetChipsContainer) {
    const activeChip = DOM.targetChipsContainer.querySelector(".target-chip.active");
    if (activeChip) {
      App.studentState.student_target = activeChip.getAttribute("data-val");
    }
  }

  saveLocalState();

  if (DOM.headerStudentName) DOM.headerStudentName.textContent = name;
  if (DOM.inputStudentName) DOM.inputStudentName.value = name;

  if (targetModule && targetModule !== App.activeModuleCode) {
    App.activeModuleCode = targetModule;
    App.studentState.active_module = targetModule;
    saveLocalState();
    if (DOM.selectModule) DOM.selectModule.value = targetModule;
    setupModuleQuestions();
    startModuleTimer();
  }

  if (typeof captureHomeAarDraftFromInputs === "function") {
    captureHomeAarDraftFromInputs();
  }

  showView("practice");
}

// ================= INITIALIZATION =================
document.addEventListener("DOMContentLoaded", async () => {
  if (window.mermaid) {
    try {
      mermaid.initialize({
        startOnLoad: false,
        theme: 'neutral',
        securityLevel: 'loose',
        fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        flowchart: {
          useMaxWidth: true,
          htmlLabels: true,
          curve: 'basis'
        }
      });
    } catch (e) {
      console.warn("Mermaid init error:", e);
    }
  }

  loadLocalState();
  loadFeedbacksList();
  initSplitResizer();
  initDraggableDesmos();
  initScratchpad();
  initTabletSupport();
  initZenMode();
  initOnboarding();
  initHomeAarSelects();
  setupEventListeners();

  await fetchDatabase();
  setupModuleQuestions();
  startModuleTimer();
  updateModuleCardStats();
  syncHomeProfile();
  showView("home");
});

// ================= MULTI-EXAM CONTROLLER & DATA LOADER =================
async function fetchDatabase(targetTestId = null) {
  try {
    if (targetTestId) {
      App.activeTestId = targetTestId;
    }
    App.activeTest = getActiveTestMeta();

    let data = null;
    const targetFile = App.activeTest.dataFile || "database.json";

    // 1. Try local dataFile (e.g. data/sep2026.json, data/oct2026.json)
    try {
      const res = await fetch(targetFile);
      if (res.ok) data = await res.json();
    } catch (err) {}

    // 2. Try static/data path if running in some subpaths
    if (!data) {
      try {
        const res = await fetch(`data/${App.activeTest.code}.json`);
        if (res.ok) data = await res.json();
      } catch (err) {}
    }

    // 3. Fallback to /api/data?test= if running via Python server
    if (!data) {
      try {
        const res = await fetch(`/api/data?test=${App.activeTest.code}`);
        if (res.ok) data = await res.json();
      } catch (err) {}
    }

    // 4. Ultimate fallback to root database.json
    if (!data) {
      try {
        const res = await fetch("database.json");
        if (res.ok) data = await res.json();
      } catch (err) {}
    }

    if (data) {
      App.db = data;
    }

    if (!App.studentState.error_logs) {
      App.studentState.error_logs = [];
    }

    // Update UI Elements with active test info
    updateActiveTestUI();
    renderExamSelectors();
    updateErrorBadge();
  } catch (e) {
    console.error("Failed to load test database:", e);
  }
}

function updateActiveTestUI() {
  if (!App.activeTest) App.activeTest = getActiveTestMeta();
  const test = App.activeTest;

  // Document Title
  document.title = `Bluebook Digital SAT — ${test.short_title}`;

  // Nav brand badge
  if (DOM.homeBrandBadge) {
    DOM.homeBrandBadge.textContent = `${test.short_title} • ${test.badge || "Real Test"}`;
  }

  // Hero section titles
  if (DOM.heroMainTitle && DOM.heroTitleGradient) {
    DOM.heroTitleGradient.textContent = `Real Test ${test.short_title}`;
  }
  if (DOM.heroMainDesc && test.description) {
    DOM.heroMainDesc.textContent = test.description;
  }

  // Hero poster & Drive buttons
  if (DOM.heroPosterImg && test.poster) {
    DOM.heroPosterImg.src = test.poster;
  }
  if (DOM.btnHeroDrivePdf && test.pdfViewUrl) {
    DOM.btnHeroDrivePdf.href = test.pdfViewUrl;
  }

  // Practice View header badge & PDF iframe
  if (DOM.practiceTestBadge) {
    DOM.practiceTestBadge.textContent = test.short_title;
  }
  if (DOM.pdfFrame && test.pdfPreviewUrl) {
    // Only update iframe src if changed to avoid unnecessary reloads
    if (!DOM.pdfFrame.src || !DOM.pdfFrame.src.includes(test.pdfDriveId)) {
      DOM.pdfFrame.src = test.pdfPreviewUrl;
    }
  }

  // Update Module Page Ranges dynamically from App.db.modules
  if (App.db && App.db.modules) {
    const mRw1 = App.db.modules.find(m => m.code === "RW_Module1");
    const mRw2 = App.db.modules.find(m => m.code === "RW_Module2");
    const mM1 = App.db.modules.find(m => m.code === "Math_Module1");
    const mM2 = App.db.modules.find(m => m.code === "Math_Module2");

    if (mRw1 && DOM.pageModRw1) {
      const endP = mRw2 ? (mRw2.pdf_start_page - 1) : (mRw1.pdf_start_page + 12);
      DOM.pageModRw1.textContent = `📖 Trang ${mRw1.pdf_start_page} – ${endP}`;
    }
    if (mRw2 && DOM.pageModRw2) {
      const endP = mM1 ? (mM1.pdf_start_page - 1) : (mRw2.pdf_start_page + 12);
      DOM.pageModRw2.textContent = `📖 Trang ${mRw2.pdf_start_page} – ${endP}`;
    }
    if (DOM.pageModMath1) {
      if (mM1) {
        const endP = mM2 ? (mM2.pdf_start_page - 1) : (mM1.pdf_start_page + 6);
        DOM.pageModMath1.textContent = `📖 Trang ${mM1.pdf_start_page} – ${endP}`;
      } else {
        DOM.pageModMath1.textContent = `📖 Không áp dụng (Reading)`;
      }
    }
    if (DOM.pageModMath2) {
      if (mM2) {
        const endP = mM2.pdf_start_page + 6;
        DOM.pageModMath2.textContent = `📖 Trang ${mM2.pdf_start_page} – ${endP}`;
      } else {
        DOM.pageModMath2.textContent = `📖 Không áp dụng (Reading)`;
      }
    }

    // Dynamic Module selector dropdown
    if (DOM.selectModule && App.db.modules.length > 0) {
      const prevMod = App.activeModuleCode;
      DOM.selectModule.innerHTML = "";
      App.db.modules.forEach(m => {
        const opt = document.createElement("option");
        opt.value = m.code;
        const modQs = (App.db.questions || []).filter(q => q.module_code === m.code);
        const count = modQs.length;
        const exCount = modQs.filter(q => q.category === "example").length;
        const prCount = modQs.filter(q => q.category === "practice").length;
        if (exCount > 0) {
          opt.textContent = `${m.title || m.code} (${count} câu: ${exCount} ví dụ + ${prCount} thực hành)`;
        } else {
          opt.textContent = `${m.title || m.code} (${count} Qs)`;
        }
        DOM.selectModule.appendChild(opt);
      });
      const totalCount = (App.db.questions || []).length;
      const optAll = document.createElement("option");
      optAll.value = "ALL";
      if (App.activeTestId === "erica-reading") {
        optAll.textContent = `Toàn bộ 9 chương: Tất cả ${totalCount} câu (${App.db.total_examples || 27} ví dụ + ${App.db.total_practice || 74} thực hành)`;
      } else if (App.activeTestId === "erica-writing") {
        optAll.textContent = `Toàn bộ 17 chuyên đề: Tất cả ${totalCount} câu (${App.db.total_examples || 62} ví dụ + ${App.db.total_practice || 272} thực hành)`;
      } else if (App.activeTestId === "panda-math") {
        optAll.textContent = `Toàn bộ 27 chương: Tất cả ${totalCount} câu hỏi SAT Math (College Panda)`;
      } else {
        optAll.textContent = `Toàn bộ đề: Tất cả ${totalCount} câu`;
      }
      DOM.selectModule.appendChild(optAll);

      const hasPrev = Array.from(DOM.selectModule.options).some(o => o.value === prevMod);
      if (hasPrev) {
        DOM.selectModule.value = prevMod;
      } else {
        DOM.selectModule.value = App.db.modules[0].code;
        App.activeModuleCode = DOM.selectModule.value;
      }
    }
  }

  renderModuleCards();
}

function renderExamSelectors() {
  const manifest = App.testsManifest || [];

  // 1. Populate Nav dropdown
  if (DOM.selectActiveExam) {
    DOM.selectActiveExam.innerHTML = "";
    manifest.forEach(test => {
      const opt = document.createElement("option");
      opt.value = test.id;
      opt.textContent = `${test.short_title} (${test.badge || "Chính thức"})`;
      if (test.id === App.activeTestId || test.code === App.activeTestId) {
        opt.selected = true;
      }
      DOM.selectActiveExam.appendChild(opt);
    });
  }

  // 2. Populate Practice Header dropdown
  if (DOM.selectPracticeExam) {
    DOM.selectPracticeExam.innerHTML = "";
    manifest.forEach(test => {
      const opt = document.createElement("option");
      opt.value = test.id;
      opt.textContent = `🗓️ ${test.short_title}`;
      if (test.id === App.activeTestId || test.code === App.activeTestId) {
        opt.selected = true;
      }
      DOM.selectPracticeExam.appendChild(opt);
    });
  }

  // 3. Render Exam Hub Cards in Home
  if (DOM.examsGrid) {
    DOM.examsGrid.innerHTML = "";
    manifest.forEach(test => {
      const isActive = (test.id === App.activeTestId || test.code === App.activeTestId);

      // Calculate progress from localStorage for this test
      let answeredCount = 0;
      let totalCount = test.total_questions || 98;
      try {
        const testKey = getStorageKeyForTest(test.id);
        let raw = localStorage.getItem(testKey);
        if (!raw && (test.id === "oct-2026" || test.code === "oct2026")) {
          raw = localStorage.getItem(LEGACY_STORAGE_KEY);
        }
        if (raw) {
          const parsed = JSON.parse(raw);
          if (parsed && parsed.attempts) {
            Object.values(parsed.attempts).forEach(a => {
              if (a && a.status && a.status !== "unanswered") answeredCount++;
            });
          }
        }
      } catch (e) {}

      const pct = Math.round((answeredCount / totalCount) * 100);

      const card = document.createElement("div");
      card.className = `exam-card ${isActive ? "active" : ""}`;
      card.dataset.testId = test.id;
      card.innerHTML = `
        <div class="exam-card-header">
          <span class="exam-badge-tag">${test.badge || "Official Test"}</span>
          ${isActive ? '<span class="exam-active-indicator">● Đang luyện tập</span>' : ""}
        </div>
        <h3 class="exam-card-title">${test.title}</h3>
        <p class="exam-card-desc">${test.description}</p>
        <div class="exam-card-meta">
          <span>📅 ${test.date || "2026"}</span>
          <span>•</span>
          <span>📝 ${test.total_questions || 98} Câu Hỏi (${test.modules_count ? test.modules_count + " Chương / Modules" : (test.id.includes("reading") ? "9 Chương" : "4 Modules")})</span>
          <span>•</span>
          <span>⏱️ ${test.time_minutes ? test.time_minutes + " Phút" : "134 Phút"}</span>
        </div>
        <div class="exam-progress-bar-wrap">
          <div class="exam-progress-label">
            <span>Tiến độ cá nhân:</span>
            <strong>${answeredCount}/${totalCount} câu (${pct}%)</strong>
          </div>
          <div class="exam-progress-bar">
            <div class="exam-progress-fill" style="width: ${pct}%"></div>
          </div>
        </div>
        <button type="button" class="btn-select-exam">
          ${isActive ? "✓ Đang Chọn Đề Này" : "Chọn Đề Này Để Luyện Tập ➔"}
        </button>
      `;

      card.addEventListener("click", () => {
        if (!isActive) switchTest(test.id);
      });

      DOM.examsGrid.appendChild(card);
    });
  }
}

async function switchTest(targetTestId) {
  if (targetTestId === App.activeTestId) return;

  // Save current test state before switching
  saveLocalState();
  pauseTimer();

  App.activeTestId = targetTestId;
  App.activeTest = getActiveTestMeta();

  // Save preference
  localStorage.setItem("bluebook_selected_test_id", targetTestId);

  // Update browser URL query param without page reload
  try {
    const url = new URL(window.location.href);
    url.searchParams.set("test", App.activeTest.code || App.activeTest.id);
    window.history.replaceState({}, "", url.toString());
  } catch (e) {}

  // Load new test state and database
  loadLocalState();
  await fetchDatabase(targetTestId);

  // Validate activeModuleCode for newly loaded test
  if (App.db && App.db.modules) {
    const isValid = App.db.modules.some(m => m.code === App.activeModuleCode) || App.activeModuleCode === "ALL";
    if (!isValid) {
      App.activeModuleCode = App.db.modules[0].code;
    }
  }

  setupModuleQuestions();
  updateModuleCardStats();
  if (typeof syncAarAnticipationUI === "function") {
    syncAarAnticipationUI();
  }

  // If in practice view, re-render question immediately
  if (document.body.classList.contains("in-practice")) {
    renderCurrentQuestion();
    startModuleTimer();
  }
}

function setupModuleQuestions() {
  if (!App.db) return;

  const mod = App.activeModuleCode;
  if (mod === "ALL") {
    App.questions = App.db.questions;
  } else {
    App.questions = App.db.questions.filter(q => q.module_code === mod);
  }

  App.currentIndex = 0;
  DOM.navTotalLabel.textContent = App.questions.length;
  DOM.selectModule.value = mod;

  renderCurrentQuestion();
}

// ================= TIMER CONTROLS & AUTO-PAUSE LOGIC =================
function pauseTimer() {
  App.timerRunning = false;
  if (DOM.btnTimerPause) {
    DOM.btnTimerPause.textContent = "▶️";
    DOM.btnTimerPause.title = "Tiếp tục tính giờ";
  }
  if (DOM.timerDisplay) {
    DOM.timerDisplay.classList.add("timer-paused");
  }
  if (DOM.zenTimerDisplay) {
    DOM.zenTimerDisplay.classList.add("timer-paused");
  }
}

function resumeTimer() {
  if (App.manualPause) return; // Respect student's manual pause
  App.timerRunning = true;
  if (DOM.btnTimerPause) {
    DOM.btnTimerPause.textContent = "⏸️";
    DOM.btnTimerPause.title = "Tạm dừng";
  }
  if (DOM.timerDisplay) {
    DOM.timerDisplay.classList.remove("timer-paused");
  }
  if (DOM.zenTimerDisplay) {
    DOM.zenTimerDisplay.classList.remove("timer-paused");
  }
}

function shouldTimerRun() {
  if (App.manualPause) return false;

  // 1. Must be in practice view
  if (!DOM.viewPractice || DOM.viewPractice.classList.contains("hidden")) return false;

  // 2. Modals that suspend active practice (error notes, review, calculators, strategies, etc.)
  if (DOM.modalMandatoryReflection && !DOM.modalMandatoryReflection.classList.contains("hidden")) return false;
  if (DOM.modalErrorLog && !DOM.modalErrorLog.classList.contains("hidden")) return false;
  if (DOM.navigatorOverlay && !DOM.navigatorOverlay.classList.contains("hidden")) return false;
  if (DOM.modalCalculator && !DOM.modalCalculator.classList.contains("hidden")) return false;
  if (DOM.modalReference && !DOM.modalReference.classList.contains("hidden")) return false;
  if (DOM.modalStrategies && !DOM.modalStrategies.classList.contains("hidden")) return false;
  if (DOM.modalAarReport && !DOM.modalAarReport.classList.contains("hidden")) return false;
  if (DOM.modalSubmitSuccess && !DOM.modalSubmitSuccess.classList.contains("hidden")) return false;
  if (DOM.modalFeedback && !DOM.modalFeedback.classList.contains("hidden")) return false;
  if (DOM.modalAceSATVocab && !DOM.modalAceSATVocab.classList.contains("hidden")) return false;

  // 3. Question status check:
  // If the current question is already completed or just evaluated for review, pause the timer!
  const currentQ = App.currentQuestion || (App.questions ? App.questions[App.currentIndex] : null);
  if (!currentQ) return false;

  const qState = App.studentState.attempts[currentQ.id];
  if (qState) {
    const isFinished = (qState.status && (qState.status.startsWith("mastered") || qState.status === "missed"));
    if (isFinished) return false;
    if (qState.justChecked) return false;
  }

  return true;
}

function syncTimerState() {
  if (shouldTimerRun()) {
    resumeTimer();
  } else {
    pauseTimer();
  }
}

window.pauseTimer = pauseTimer;
window.resumeTimer = resumeTimer;
window.syncTimerState = syncTimerState;

// ================= TIMER =================
function startModuleTimer() {
  clearInterval(App.timerInterval);
  
  if (!App.studentState.timer_seconds[App.activeModuleCode]) {
    const activeModObj = (App.db && App.db.modules) ? App.db.modules.find(m => m.code === App.activeModuleCode) : null;
    let mins = 32;
    if (activeModObj && activeModObj.time_minutes) {
      mins = activeModObj.time_minutes;
    } else if (App.activeModuleCode === "ALL") {
      mins = (App.db && App.db.time_minutes) ? App.db.time_minutes : (App.activeTestId === "erica-writing" ? 352 : (App.activeTestId === "erica-reading" ? 96 : 134));
    }
    App.studentState.timer_seconds[App.activeModuleCode] = mins * 60;
  }

  const updateDisplay = () => {
    let secs = App.studentState.timer_seconds[App.activeModuleCode] || 0;
    const mins = Math.floor(secs / 60);
    const remSecs = secs % 60;
    const timeStr = `${String(mins).padStart(2, "0")}:${String(remSecs).padStart(2, "0")}`;
    if (DOM.timerDisplay) DOM.timerDisplay.textContent = timeStr;
    if (DOM.zenTimerDisplay) DOM.zenTimerDisplay.textContent = timeStr;
  };

  updateDisplay();

  App.timerInterval = setInterval(() => {
    if (App.timerRunning) {
      if (App.studentState.timer_seconds[App.activeModuleCode] > 0) {
        App.studentState.timer_seconds[App.activeModuleCode]--;
        updateDisplay();
        // Save timer state periodically
        if (App.studentState.timer_seconds[App.activeModuleCode] % 5 === 0) {
          saveLocalState();
        }
      } else {
        if (DOM.timerDisplay) DOM.timerDisplay.textContent = "00:00";
        if (DOM.zenTimerDisplay) DOM.zenTimerDisplay.textContent = "00:00";
        pauseTimer();
      }
    }
  }, 1000);
}

// ================= QUESTION RENDERING =================
function renderCurrentQuestion() {
  const q = App.questions[App.currentIndex];
  if (!q) return;

  App.currentQuestion = q;
  App.selectedChoice = null;

  // Retrieve student's personal state for this question from localStorage
  const qState = App.studentState.attempts[q.id] || {
    attempts: [],
    status: "unanswered",
    efficiency: 0.0,
    marked: false,
    eliminated: []
  };

  // Question Number & Navigation Labels
  if (DOM.qNumberLabel) {
    if ((App.activeTestId === "erica-reading" || App.activeTestId === "ericareading" || App.activeTestId === "erica-writing" || App.activeTestId === "ericawriting" || App.activeTestId === "panda-math" || App.activeTestId === "pandamath") && q.q_label) {
      const bookPg = q.book_page || (q.pdf_page ? q.pdf_page - 1 : null);
      const bookStr = bookPg ? ` • Sách trang ${bookPg}` : "";
      DOM.qNumberLabel.innerHTML = `<strong>${escapeHtml(q.q_label)}</strong> <span style="opacity:0.75; font-weight:normal; margin-left:8px;">(Mục ${App.currentIndex + 1}/${App.questions.length}${bookStr})</span>`;
    } else {
      DOM.qNumberLabel.textContent = `Question ${App.currentIndex + 1} of ${App.questions.length}`;
    }
  }
  if (DOM.navCurrentLabel) DOM.navCurrentLabel.textContent = App.currentIndex + 1;
  if (DOM.qTopicBadge) {
    if (q.category === "example") {
      DOM.qTopicBadge.innerHTML = `<span class="pill-badge pill-example">💡 Ví dụ minh họa</span> ${escapeHtml(q.topic || "")}`;
    } else if (q.category === "practice") {
      DOM.qTopicBadge.innerHTML = `<span class="pill-badge pill-practice">✍️ Luyện tập</span> ${escapeHtml(q.topic || "")}`;
    } else {
      DOM.qTopicBadge.textContent = q.topic || "";
    }
    DOM.qTopicBadge.title = `Chủ đề: ${q.topic || ""}`;
  }
  if (DOM.qDomainBadge) {
    let extra = "";
    if (q.calc_mode) {
      extra = q.is_calculator ? " • 🧮 Calculator Allowed" : " • ✏️ No Calculator";
    }
    DOM.qDomainBadge.textContent = (q.domain || q.section || "") + extra;
    DOM.qDomainBadge.title = `Phần thi: ${q.domain || q.section || ""} (${q.calc_mode || ""})`;
  }

  // Response instruction label
  if (DOM.responseInstruction) {
    const isEricaWriting = (App.activeTestId === "erica-writing" || App.activeTestId === "ericawriting");
    const bookPg = q.book_page || (q.pdf_page ? q.pdf_page - 2 : null);
    const labelMeta = isEricaWriting && q.q_label
      ? ` — <span style="color:#1e40af; font-weight:700;">${escapeHtml(q.q_label)}</span>${bookPg ? ` <span style="opacity:0.78;">(Sách tr. ${bookPg})</span>` : ""}`
      : "";
    if (App.activeTestId === "panda-math") {
      DOM.responseInstruction.innerHTML = '<strong>🐼 THE COLLEGE PANDA SAT MATH</strong> — Đọc đề bài và tính toán cẩn thận để chọn đáp án đúng:';
    } else if (q.category === "example") {
      DOM.responseInstruction.innerHTML = `<strong>💡 VÍ DỤ MINH HỌA (WORKED EXAMPLE)</strong>${labelMeta} — Đọc ví dụ trên trang sách PDF bên trái và cùng phân tích phương pháp của Erica Meltzer:`;
    } else if (q.category === "practice") {
      DOM.responseInstruction.innerHTML = `<strong>✍️ BÀI TẬP THỰC HÀNH</strong>${labelMeta} — Đọc đề bài trên trang sách PDF bên trái và chọn đáp án đúng:`;
    } else {
      DOM.responseInstruction.textContent = 'Đọc đề bài trên trang sách PDF bên trái và chọn đáp án đúng:';
    }
  }

  // Question Stem Box (for Math problems and questions with explicit text)
  if (DOM.questionStemBox && DOM.questionStemText) {
    const qStem = q.prompt || q.question || "";
    if (App.activeTestId === "panda-math" && qStem.trim()) {
      DOM.questionStemText.innerHTML = escapeHtml(qStem);
      DOM.questionStemBox.classList.remove("hidden");
    } else {
      DOM.questionStemBox.classList.add("hidden");
    }
  }

  // Mark for review
  DOM.chkMarkReview.checked = !!qState.marked;
  DOM.markReviewLabel.classList.toggle("marked", !!qState.marked);

  // PDF Page Sync
  if (DOM.pdfSyncPageNum) DOM.pdfSyncPageNum.textContent = q.pdf_page;
  if (DOM.inputPdfPage) DOM.inputPdfPage.value = q.pdf_page;
  if (App.pdfViewerMode === "local") {
    navigatePdf(q.pdf_page);
  }

  // Excerpt Accordion (optional)
  if (DOM.excerptPassage) DOM.excerptPassage.textContent = q.passage || "Xem văn bản trên trang đề thi PDF bên trái.";
  if (DOM.excerptPrompt) DOM.excerptPrompt.textContent = q.prompt || "";

  // Render Response Mode: Multiple-Choice or Grid-in
  const isFinished = (qState.status && (qState.status.startsWith("mastered") || qState.status === "missed")) || !!qState.reviewAllHints;

  // Question Header Instruction & Mark for Review visibility (Hidden after trial & error is completed)
  if (DOM.questionTopBar) {
    DOM.questionTopBar.classList.toggle("hidden", isFinished);
  }
  if (DOM.qActionRow) {
    DOM.qActionRow.classList.toggle("hidden", isFinished);
  }

  if (q.is_grid_in) {
    DOM.mcqResponseArea.classList.add("hidden");
    DOM.gridinResponseArea.classList.remove("hidden");
    DOM.gridinInput.value = (qState.attempts && qState.attempts.length > 0) ? qState.attempts[qState.attempts.length - 1] : "";
    DOM.gridinInput.disabled = isFinished;
    renderGridInSolution(q, qState, isFinished);
  } else {
    DOM.gridinResponseArea.classList.add("hidden");
    DOM.mcqResponseArea.classList.remove("hidden");
    renderOptions(q, qState, isFinished);
  }

  // Attempt tracker & Slots
  renderAttemptSlots(q, qState);

  // Progressive Hints
  renderHints(q, qState);

  // Visual Thinking Diagram (Mermaid) - Revealed when trial & error is finished
  renderMermaidDiagram(q, isFinished);

  // Math typesetting
  if (window.renderMathInElement) {
    window.renderMathInElement(document.getElementById("pane-content"), {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\(', right: '\\)', display: false},
        {left: '\\[', right: '\\]', display: true}
      ],
      throwOnError: false
    });
  }

  // Disable check button until selected
  DOM.btnCheckAnswer.disabled = true;

  // Auto-sync timer based on practice vs review mode
  syncTimerState();
}

function renderGridInSolution(q, qState, isFinished) {
  let solBox = document.getElementById("gridin-solution-box");
  if (!solBox) {
    solBox = document.createElement("div");
    solBox.id = "gridin-solution-box";
    DOM.gridinResponseArea.appendChild(solBox);
  }
  if (!isFinished) {
    solBox.className = "hidden";
    solBox.innerHTML = "";
    return;
  }
  solBox.className = "gridin-solution-card";
  const trapErrors = q.grid_in_explanation?.trap_errors || "Cẩn thận kiểm tra các bẫy đổi đơn vị, làm tròn số thập phân, hoặc điều kiện bài toán.";
  const steps = q.solution_steps || q.pooe_breakdown || "Xem lời giải chi tiết và các bước biến đổi trên bảng gợi ý.";
  
  solBox.innerHTML = `
    <div class="gridin-badge-line">
      <span class="gridin-correct-tag"><span class="badge-icon">✅</span> ĐÁP ÁN ĐÚNG CHUẨN: <strong>${escapeHtml(q.correct_answer)}</strong></span>
    </div>
    <div class="gridin-section">
      <div class="gridin-sec-header">💡 CÁCH GIẢI CHI TIẾT & BƯỚC TÍNH:</div>
      <div class="gridin-sec-body">${escapeHtml(steps)}</div>
    </div>
    <div class="gridin-section gridin-trap">
      <div class="gridin-sec-header trap-header">⚠️ TẠI SAO CÁC KẾT QUẢ KHÁC BỊ SAI / LỖI BẪY:</div>
      <div class="gridin-sec-body">${escapeHtml(trapErrors)}</div>
    </div>
  `;
}

function renderOptions(q, qState, isFinished) {
  DOM.optionsContainer.innerHTML = "";
  if (isFinished === undefined) {
    isFinished = (qState.status && (qState.status.startsWith("mastered") || qState.status === "missed")) || !!qState.reviewAllHints;
  }
  const eliminated = qState.eliminated || [];

  const defaultKeys = ["A", "B", "C", "D"];
  const opts = (q.options && q.options.length > 0)
    ? q.options
    : defaultKeys.map(k => ({ key: k, text: `Lựa chọn ${k}` }));

  opts.forEach(opt => {
    const row = document.createElement("div");
    row.className = "option-row";
    row.dataset.key = opt.key;

    if (eliminated.includes(opt.key)) {
      row.classList.add("eliminated");
    }

    const isCorrect = (opt.key === q.correct_answer);

    if (isFinished) {
      if (isCorrect) {
        row.classList.add("correct");
      } else if (qState.attempts && qState.attempts.includes(opt.key)) {
        row.classList.add("wrong");
      }
    } else if (qState.attempts && qState.attempts.includes(opt.key)) {
      row.classList.add("wrong");
    }

    const isEliminated = eliminated.includes(opt.key);
    const optText = (opt.text && opt.text.trim() && opt.text !== opt.key && opt.text !== `Lựa chọn ${opt.key}`)
      ? opt.text
      : `Lựa chọn ${opt.key}`;

    row.innerHTML = `
      <div class="option-header-row">
        <div class="option-bubble">${opt.key}</div>
        <div class="option-text-wrap font-medium">${escapeHtml(optText)}</div>
        ${!isFinished ? `<button type="button" class="btn-strike-option ${isEliminated ? 'is-eliminated' : ''}" title="${isEliminated ? 'Khôi phục phương án ' + opt.key : 'Gạch bỏ phương án ' + opt.key + ' (Eliminate)'}">⨉</button>` : ''}
      </div>
    `;

    // Render explanation for every option (why right / why wrong) when finished
    if (isFinished && q.option_explanations && q.option_explanations[opt.key]) {
      const expText = q.option_explanations[opt.key];
      const expDiv = document.createElement("div");
      expDiv.className = `option-explanation-card ${isCorrect ? 'exp-correct' : 'exp-wrong'}`;
      
      const badgeLabel = isCorrect ? "✅ ĐÁP ÁN ĐÚNG" : "❌ TẠI SAO SAI / BỊ LOẠI";
      
      expDiv.innerHTML = `
        <div class="exp-badge-line">
          <span class="exp-badge-tag ${isCorrect ? 'tag-correct' : 'tag-wrong'}">${badgeLabel}</span>
        </div>
        <div class="exp-text-content">${escapeHtml(expText)}</div>
      `;
      row.appendChild(expDiv);
    }

    // Click option to select
    row.addEventListener("click", (e) => {
      if (e.target.classList.contains("btn-strike-option")) return;
      if (isFinished) return;
      if (row.classList.contains("eliminated")) return;

      if (qState.justChecked) {
        qState.justChecked = false;
        saveLocalState();
        syncTimerState();
      }

      document.querySelectorAll(".option-row").forEach(r => r.classList.remove("selected"));
      row.classList.add("selected");
      App.selectedChoice = opt.key;
      DOM.btnCheckAnswer.disabled = false;
    });

    // Eliminator strike action (Directly integrated on options A, B, C, D)
    const btnStrike = row.querySelector(".btn-strike-option");
    if (btnStrike) {
      btnStrike.addEventListener("click", (e) => {
        e.stopPropagation();
        row.classList.toggle("eliminated");
        const nowEliminated = row.classList.contains("eliminated");
        btnStrike.classList.toggle("is-eliminated", nowEliminated);
        btnStrike.title = nowEliminated ? `Khôi phục phương án ${opt.key}` : `Gạch bỏ phương án ${opt.key} (Eliminate)`;

        if (nowEliminated) {
          if (row.classList.contains("selected")) {
            row.classList.remove("selected");
            App.selectedChoice = null;
            DOM.btnCheckAnswer.disabled = true;
          }
          if (!qState.eliminated) qState.eliminated = [];
          if (!qState.eliminated.includes(opt.key)) qState.eliminated.push(opt.key);
        } else {
          qState.eliminated = (qState.eliminated || []).filter(k => k !== opt.key);
        }
        App.studentState.attempts[q.id] = qState;
        saveLocalState();
      });
    }

    DOM.optionsContainer.appendChild(row);
  });
}

function renderAttemptSlots(q, qState) {
  const attempts = qState.attempts || [];
  const status = qState.status || "unanswered";
  const eff = qState.efficiency || 0;

  const setSlot = (slotEl, idx) => {
    const textEl = slotEl.querySelector(".slot-text");
    if (attempts.length > idx) {
      textEl.textContent = attempts[idx];
      if (status.startsWith("mastered") && idx === attempts.length - 1) {
        textEl.className = "slot-text correct";
      } else {
        textEl.className = "slot-text wrong";
      }
    } else {
      textEl.textContent = "-";
      textEl.className = "slot-text";
    }
  };

  setSlot(DOM.slotL1, 0);
  setSlot(DOM.slotL2, 1);
  setSlot(DOM.slotL3, 2);

  DOM.effVal.textContent = `${Math.round(eff * 100)}%`;

  // Status Alert
  if (status === "mastered_l1") {
    showAlert(true, "🎉 Chính xác! Em đã làm đúng ngay Lần 1 (Hiệu suất 100%).");
  } else if (status === "mastered_l2") {
    showAlert(true, "✅ Rất tốt! Em đã làm đúng ở Lần 2 (Hiệu suất 66.7%).");
  } else if (status === "mastered_l3") {
    showAlert(true, "✅ Đúng ở Lần 3 (Hiệu suất 33.3%). Xem lại gợi ý để nắm chắc kiến thức.");
  } else if (status === "missed") {
    showAlert(false, `❌ Chưa chính xác sau 3 lần. Đáp án đúng là [${q.correct_answer}]. Hãy ghi lại vào Sổ thử sai.`);
  } else if (status.startsWith("retry")) {
    const left = 3 - attempts.length;
    showAlert(false, `⚠️ Chưa chính xác. Em còn ${left} lần thử. Đã mở gợi ý bên dưới!`);
  } else {
    DOM.statusAlert.className = "status-alert hidden";
  }
}

function showAlert(isSuccess, text) {
  DOM.statusAlert.className = `status-alert ${isSuccess ? "success" : "wrong"}`;
  DOM.alertIcon.textContent = isSuccess ? "✅" : "❌";
  DOM.alertText.textContent = text;
}

function renderHints(q, qState) {
  const attempts = qState.attempts || [];
  const isFinished = (qState.status.startsWith("mastered") || qState.status === "missed") || !!qState.reviewAllHints;

  // Tier 1: Định hướng bối cảnh & Tư duy tổng quan (Mở sau Lần 1 hoặc khi hoàn thành)
  if (attempts.length >= 1 || isFinished) {
    DOM.hintText1.innerHTML = formatMarkdownHints(q.tier1_hint || q.level1_tip || "Xác định từ khóa trọng tâm và logic ngữ cảnh của câu hỏi.");
    DOM.hintContent1.classList.remove("collapsed");
    DOM.hintCard1.classList.add("unlocked");
  } else {
    DOM.hintText1.textContent = "🔒 Thử sức Lần 1 để mở khóa gợi ý định hướng bối cảnh.";
    DOM.hintContent1.classList.add("collapsed");
    DOM.hintCard1.classList.remove("unlocked");
  }

  // Tier 2: Manh mối cấu trúc & Phân tích loại trừ (Mở sau Lần 2 hoặc khi hoàn thành)
  if (attempts.length >= 2 || isFinished) {
    DOM.hintText2.innerHTML = formatMarkdownHints(q.tier2_hint || q.level2_hint || "Áp dụng phương pháp loại trừ và phân tích cấu trúc đối chiếu.");
    DOM.hintContent2.classList.remove("collapsed");
    DOM.hintCard2.classList.add("unlocked");
  } else {
    DOM.hintText2.textContent = "🔒 Thử sức Lần 2 để mở khóa manh mối cấu trúc & loại trừ phương án sai.";
    DOM.hintContent2.classList.add("collapsed");
    DOM.hintCard2.classList.remove("unlocked");
  }

  // Tier 3: Chốt phương pháp & Lời giải chi tiết (Mở sau Lần 3 hoặc khi hoàn thành)
  if (attempts.length >= 3 || isFinished) {
    let sol = q.tier3_hint || q.level3_solution || "Chốt phương pháp: So sánh trực tiếp với giả thiết cốt lõi trong đề.";
    if (isFinished) {
      sol = `<strong>Đáp án đúng: <span class="correct-highlight">[${q.correct_answer}]</span></strong><br><br>${formatMarkdownHints(sol)}`;
    } else {
      sol = formatMarkdownHints(sol);
    }
    DOM.hintText3.innerHTML = sol;
    DOM.hintContent3.classList.remove("collapsed");
    DOM.hintCard3.classList.add("unlocked");
  } else {
    DOM.hintText3.textContent = "🔒 Mở khóa chốt phương pháp sau 3 lần thử hoặc khi làm đúng.";
    DOM.hintContent3.classList.add("collapsed");
    DOM.hintCard3.classList.remove("unlocked");
  }

  // Tier 4: Strategic Tip & Công thức chuẩn College Board / Princeton Review (Mở khi làm đúng hoặc hoàn thành)
  if (DOM.hintCard4) {
    if (isFinished) {
      let content = "";
      if (q.princeton_strategy) {
        content += `<p style="margin-bottom: 8px;"><strong>🎯 Chiến thuật Princeton Review:</strong> ${escapeHtml(q.princeton_strategy)}</p>`;
      }
      if (q.target_clue) {
        content += `<p style="margin-bottom: 8px;"><strong>🔍 Phân tích Manh mối & Target:</strong> ${escapeHtml(q.target_clue)}</p>`;
      }
      if (q.pro_tip) {
        content += `<p style="margin-bottom: 8px;"><strong>💡 Mẹo độc quyền Pro-Tip:</strong> ${escapeHtml(q.pro_tip)}</p>`;
      }
      if (!content) {
        content = `<strong>✨ Chiến thuật College Board:</strong><br>${escapeHtml(q.strategic_tip || "Nắm vững quy tắc và công thức toán / ngữ pháp cốt lõi.")}`;
      }
      DOM.hintText4.innerHTML = content;
      DOM.hintContent4.classList.remove("collapsed");
      DOM.hintCard4.classList.add("unlocked");
    } else {
      DOM.hintText4.textContent = "🔒 Hoàn thành câu hỏi để mở khóa phân tích chiến thuật & mẹo độc quyền Princeton Review.";
      DOM.hintContent4.classList.add("collapsed");
      DOM.hintCard4.classList.remove("unlocked");
    }
  }
}

// ================= MERMAID POP-UP MODAL & PAN-ZOOM CONTROLLER =================
const MermaidPanZoom = {
  baseW: 800,
  baseH: 600,
  panX: 0,
  panY: 0,
  scale: 1,
  fitScale: 1,
  minScale: 0.1,
  maxScale: 6.0,
  isDragging: false,
  isPinching: false,
  activePointers: new Map(),
  dragStart: { x: 0, y: 0 },
  panStart: { x: 0, y: 0 },
  initialPinchDist: 0,
  initialPinchMid: { x: 0, y: 0 },
  initialPinchScale: 1,
  initialPinchPan: { x: 0, y: 0 },
  transitionTimer: null,
  isInitialized: false,

  init() {
    if (this.isInitialized || !DOM.mermaidViewport || !DOM.mermaidCanvas) return;
    this.isInitialized = true;

    // Mouse wheel zooming centered at mouse pointer
    DOM.mermaidViewport.addEventListener("wheel", (e) => {
      e.preventDefault();
      const rect = DOM.mermaidViewport.getBoundingClientRect();
      const focusX = e.clientX - rect.left;
      const focusY = e.clientY - rect.top;
      const factor = e.deltaY < 0 ? 1.15 : (1 / 1.15);
      this.zoomBy(factor, focusX, focusY, false);
    }, { passive: false });

    // Pointer events (unifies Mouse drag and Touch pinch/pan on all devices)
    DOM.mermaidViewport.addEventListener("pointerdown", (e) => {
      try {
        DOM.mermaidViewport.setPointerCapture(e.pointerId);
      } catch (_) {}
      this.onPointerDown(e);
    });

    DOM.mermaidViewport.addEventListener("pointermove", (e) => {
      this.onPointerMove(e);
    });

    const pointerEnd = (e) => {
      try {
        if (DOM.mermaidViewport.hasPointerCapture(e.pointerId)) {
          DOM.mermaidViewport.releasePointerCapture(e.pointerId);
        }
      } catch (_) {}
      this.onPointerUp(e);
    };

    DOM.mermaidViewport.addEventListener("pointerup", pointerEnd);
    DOM.mermaidViewport.addEventListener("pointercancel", pointerEnd);

    // Safari iOS gesture prevention to avoid bouncing the whole page
    DOM.mermaidViewport.addEventListener("gesturestart", (e) => e.preventDefault());
    DOM.mermaidViewport.addEventListener("gesturechange", (e) => e.preventDefault());
    DOM.mermaidViewport.addEventListener("gestureend", (e) => e.preventDefault());

    // Double-click to toggle fit vs zoom in
    DOM.mermaidViewport.addEventListener("dblclick", (e) => {
      e.preventDefault();
      const rect = DOM.mermaidViewport.getBoundingClientRect();
      const focusX = e.clientX - rect.left;
      const focusY = e.clientY - rect.top;
      if (Math.abs(this.scale - this.fitScale) / (this.fitScale || 1) < 0.15) {
        this.zoomTo(this.fitScale * 1.8, focusX, focusY, true);
      } else {
        this.fitToView(true);
      }
    });

    // Toolbar controls
    if (DOM.btnMmZoomIn) {
      DOM.btnMmZoomIn.addEventListener("click", (e) => {
        e.stopPropagation();
        const rect = DOM.mermaidViewport.getBoundingClientRect();
        this.zoomBy(1.25, rect.width / 2, rect.height / 2, true);
      });
    }

    if (DOM.btnMmZoomOut) {
      DOM.btnMmZoomOut.addEventListener("click", (e) => {
        e.stopPropagation();
        const rect = DOM.mermaidViewport.getBoundingClientRect();
        this.zoomBy(1 / 1.25, rect.width / 2, rect.height / 2, true);
      });
    }

    if (DOM.btnMmZoomReset) {
      DOM.btnMmZoomReset.addEventListener("click", (e) => {
        e.stopPropagation();
        this.fitToView(true);
      });
    }

    // Auto re-fit on window resize if modal is visible
    window.addEventListener("resize", () => {
      if (DOM.modalMermaid && !DOM.modalMermaid.classList.contains("hidden")) {
        this.fitToView(false);
      }
    });
  },

  initDiagram(baseW, baseH) {
    this.baseW = Math.max(100, baseW || 800);
    this.baseH = Math.max(100, baseH || 600);
    this.activePointers.clear();
    this.isDragging = false;
    this.isPinching = false;
    if (DOM.mermaidViewport) {
      DOM.mermaidViewport.classList.remove("is-dragging");
    }
    // Delay 1 frame to ensure DOM layout / modal visibility is ready
    requestAnimationFrame(() => {
      this.fitToView(false);
    });
  },

  fitToView(smooth = false) {
    if (!DOM.mermaidViewport || !DOM.mermaidCanvas) return;
    const vpW = DOM.mermaidViewport.clientWidth || 800;
    const vpH = DOM.mermaidViewport.clientHeight || 500;

    // 48px padding (24px each side) for comfortable breathing room
    const padding = 48;
    const availW = Math.max(100, vpW - padding);
    const availH = Math.max(100, vpH - padding);

    const scaleX = availW / this.baseW;
    const scaleY = availH / this.baseH;

    // Diagram fits 100% visible on screen; cap at 1.25x so tiny diagrams aren't blown up
    this.fitScale = Math.min(scaleX, scaleY, 1.25);
    this.scale = this.fitScale;

    // Set zoom boundaries
    this.minScale = Math.max(0.1, this.fitScale * 0.35);
    this.maxScale = Math.max(4.0, this.fitScale * 5.0);

    // Center in viewport
    const renderedW = this.baseW * this.scale;
    const renderedH = this.baseH * this.scale;
    this.panX = (vpW - renderedW) / 2;
    this.panY = (vpH - renderedH) / 2;

    this.applyTransform(smooth);
  },

  zoomBy(factor, focusX, focusY, smooth = false) {
    this.zoomTo(this.scale * factor, focusX, focusY, smooth);
  },

  zoomTo(targetScale, focusX, focusY, smooth = false) {
    const clampedScale = Math.max(this.minScale, Math.min(this.maxScale, targetScale));
    if (Math.abs(clampedScale - this.scale) < 0.0001) return;

    const r = clampedScale / this.scale;
    this.panX = focusX - (focusX - this.panX) * r;
    this.panY = focusY - (focusY - this.panY) * r;
    this.scale = clampedScale;

    this.applyTransform(smooth);
  },

  applyTransform(smooth = false) {
    if (!DOM.mermaidCanvas) return;
    if (smooth) {
      DOM.mermaidCanvas.classList.add("smooth-transition");
      clearTimeout(this.transitionTimer);
      this.transitionTimer = setTimeout(() => {
        if (DOM.mermaidCanvas) {
          DOM.mermaidCanvas.classList.remove("smooth-transition");
        }
      }, 260);
    } else {
      DOM.mermaidCanvas.classList.remove("smooth-transition");
    }

    DOM.mermaidCanvas.style.transform = `translate3d(${this.panX.toFixed(2)}px, ${this.panY.toFixed(2)}px, 0) scale(${this.scale.toFixed(4)})`;
    this.updateZoomDisplay();
  },

  updateZoomDisplay() {
    if (!DOM.mmZoomLevel) return;
    const pct = Math.round((this.scale / (this.fitScale || 1)) * 100);
    DOM.mmZoomLevel.textContent = `${pct}%`;
  },

  onPointerDown(e) {
    this.activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (this.activePointers.size === 1) {
      this.isDragging = true;
      this.dragStart = { x: e.clientX, y: e.clientY };
      this.panStart = { x: this.panX, y: this.panY };
      if (DOM.mermaidViewport) DOM.mermaidViewport.classList.add("is-dragging");
    } else if (this.activePointers.size === 2) {
      this.isDragging = false;
      this.isPinching = true;
      const pts = Array.from(this.activePointers.values());
      this.initialPinchDist = Math.hypot(pts[1].x - pts[0].x, pts[1].y - pts[0].y);
      const rect = DOM.mermaidViewport.getBoundingClientRect();
      this.initialPinchMid = {
        x: (pts[0].x + pts[1].x) / 2 - rect.left,
        y: (pts[0].y + pts[1].y) / 2 - rect.top
      };
      this.initialPinchScale = this.scale;
      this.initialPinchPan = { x: this.panX, y: this.panY };
    }
  },

  onPointerMove(e) {
    if (!this.activePointers.has(e.pointerId)) return;
    this.activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY });

    if (this.isPinching && this.activePointers.size === 2) {
      const pts = Array.from(this.activePointers.values());
      const currentDist = Math.hypot(pts[1].x - pts[0].x, pts[1].y - pts[0].y);
      const rect = DOM.mermaidViewport.getBoundingClientRect();
      const currentMid = {
        x: (pts[0].x + pts[1].x) / 2 - rect.left,
        y: (pts[0].y + pts[1].y) / 2 - rect.top
      };

      if (this.initialPinchDist > 5) {
        const pinchFactor = currentDist / this.initialPinchDist;
        let targetScale = this.initialPinchScale * pinchFactor;
        targetScale = Math.max(this.minScale, Math.min(this.maxScale, targetScale));
        const r = targetScale / this.initialPinchScale;
        this.scale = targetScale;
        this.panX = this.initialPinchMid.x - (this.initialPinchMid.x - this.initialPinchPan.x) * r + (currentMid.x - this.initialPinchMid.x);
        this.panY = this.initialPinchMid.y - (this.initialPinchMid.y - this.initialPinchPan.y) * r + (currentMid.y - this.initialPinchMid.y);
        this.applyTransform(false);
      }
    } else if (this.isDragging && this.activePointers.size === 1) {
      const dx = e.clientX - this.dragStart.x;
      const dy = e.clientY - this.dragStart.y;
      this.panX = this.panStart.x + dx;
      this.panY = this.panStart.y + dy;
      this.applyTransform(false);
    }
  },

  onPointerUp(e) {
    this.activePointers.delete(e.pointerId);
    if (this.activePointers.size === 0) {
      this.isDragging = false;
      this.isPinching = false;
      if (DOM.mermaidViewport) DOM.mermaidViewport.classList.remove("is-dragging");
    } else if (this.activePointers.size === 1) {
      this.isPinching = false;
      this.isDragging = true;
      const rem = Array.from(this.activePointers.values())[0];
      this.dragStart = { x: rem.x, y: rem.y };
      this.panStart = { x: this.panX, y: this.panY };
    }
  }
};

async function openMermaidModal() {
  const q = App.currentQuestion;
  if (!q || !q.mermaid_diagram || !q.mermaid_diagram.trim()) return;

  pauseTimer();

  const qIndex = App.currentIndex + 1;
  const modTitle = DOM.selectModule ? DOM.selectModule.options[DOM.selectModule.selectedIndex].text.split("(")[0].trim() : App.activeModuleCode;

  if (DOM.mermaidModalTitle) {
    DOM.mermaidModalTitle.textContent = `${modTitle} • Câu ${qIndex}: ${q.topic || 'Sơ đồ tư duy logic'}`;
  }

  if (DOM.modalMermaid) {
    DOM.modalMermaid.classList.remove("hidden");
  }

  MermaidPanZoom.init();
  await renderMermaidDiagramContent(q);
}

function closeMermaidModal() {
  if (DOM.modalMermaid) {
    DOM.modalMermaid.classList.add("hidden");
  }
}

async function renderMermaidDiagramContent(q) {
  if (!DOM.mermaidViewer) return;
  const rawCode = q.mermaid_diagram.trim();
  const targetQId = q.id;
  const renderId = `mermaid-svg-modal-${q.id || App.currentIndex}-${Date.now()}`;

  if (window.mermaid) {
    try {
      const { svg } = await mermaid.render(renderId, rawCode);
      if (App.currentQuestion && App.currentQuestion.id === targetQId) {
        DOM.mermaidViewer.innerHTML = svg;
        prepareMermaidSvg();
      }
    } catch (err) {
      console.warn("Mermaid render error for Q" + q.id, err);
      if (App.currentQuestion && App.currentQuestion.id === targetQId) {
        DOM.mermaidViewer.innerHTML = `<pre class="mermaid-raw-fallback">${escapeHtml(rawCode)}</pre>`;
        MermaidPanZoom.initDiagram(700, 400);
      }
    }
  } else {
    DOM.mermaidViewer.innerHTML = `<pre class="mermaid-raw-fallback">${escapeHtml(rawCode)}</pre>`;
    MermaidPanZoom.initDiagram(700, 400);
  }
}

function prepareMermaidSvg() {
  if (!DOM.mermaidViewer) return;
  const svgEl = DOM.mermaidViewer.querySelector("svg");
  if (!svgEl) return;

  // Extract base natural dimensions
  let baseW = 0;
  let baseH = 0;

  const vb = svgEl.getAttribute("viewBox");
  if (vb) {
    const parts = vb.trim().split(/[\s,]+/).map(Number);
    if (parts.length === 4 && parts[2] > 0 && parts[3] > 0) {
      baseW = parts[2];
      baseH = parts[3];
    }
  }

  if (!baseW || !baseH) {
    try {
      const bbox = svgEl.getBBox();
      if (bbox && bbox.width > 0 && bbox.height > 0) {
        baseW = bbox.width + (bbox.x > 0 ? bbox.x * 2 : 20);
        baseH = bbox.height + (bbox.y > 0 ? bbox.y * 2 : 20);
      }
    } catch (_) {}
  }

  if (!baseW || !baseH) {
    baseW = parseFloat(svgEl.getAttribute("width")) || svgEl.clientWidth || 900;
    baseH = parseFloat(svgEl.getAttribute("height")) || svgEl.clientHeight || 600;
  }

  // Ensure viewBox is properly defined so SVG scales cleanly
  if (!svgEl.getAttribute("viewBox") && baseW > 0 && baseH > 0) {
    svgEl.setAttribute("viewBox", `0 0 ${baseW} ${baseH}`);
  }

  // Set explicit base dimensions on SVG and remove inline max-width
  svgEl.removeAttribute("width");
  svgEl.removeAttribute("height");
  svgEl.style.width = `${baseW}px`;
  svgEl.style.height = `${baseH}px`;
  svgEl.style.maxWidth = "none";
  svgEl.style.maxHeight = "none";
  svgEl.style.display = "block";

  MermaidPanZoom.initDiagram(baseW, baseH);
}

function renderMermaidDiagram(q, isFinished) {
  const hasMermaid = isFinished && q.mermaid_diagram && q.mermaid_diagram.trim().length > 0;

  if (DOM.btnQMermaid) {
    DOM.btnQMermaid.classList.toggle("hidden", !hasMermaid);
  }

  if (DOM.mermaidTriggerBanner) {
    DOM.mermaidTriggerBanner.classList.toggle("hidden", !hasMermaid);
  }

  // If modal is currently open and user changed questions, sync or close
  if (DOM.modalMermaid && !DOM.modalMermaid.classList.contains("hidden")) {
    if (hasMermaid) {
      openMermaidModal();
    } else {
      closeMermaidModal();
    }
  }
}

// ================= SUBMIT / CHECK ANSWER (100% LOCALSTORAGE) =================
function checkAnswer() {
  const q = App.currentQuestion;
  if (!q) return;

  let choice = App.selectedChoice;
  if (q.is_grid_in) {
    choice = DOM.gridinInput.value.trim();
  }

  if (!choice) return;

  const qState = App.studentState.attempts[q.id] || {
    attempts: [],
    status: "unanswered",
    efficiency: 0.0,
    marked: false,
    eliminated: []
  };

  qState.attempts = qState.attempts || [];
  qState.attempts.push(choice);
  qState.last_practiced_at = new Date().toISOString();
  if (!App.sessionPracticedIds) App.sessionPracticedIds = new Set();
  App.sessionPracticedIds.add(`${App.activeTestId}::${q.id}`);
  const attemptCount = qState.attempts.length;

  // Evaluation: match string or float for grid-in
  let isCorrect = false;
  if (q.is_grid_in) {
    const cleanUser = choice.replace(/\s+/g, '');
    const cleanAns = q.correct_answer.replace(/\s+/g, '');
    isCorrect = (cleanUser === cleanAns);
    if (!isCorrect) {
      try {
        const uVal = evalFraction(cleanUser);
        const aVal = evalFraction(cleanAns);
        if (uVal !== null && aVal !== null && Math.abs(uVal - aVal) < 0.0001) {
          isCorrect = true;
        }
      } catch (e) {}
    }
  } else {
    isCorrect = (choice.toUpperCase() === q.correct_answer.toUpperCase());
  }

  // Scoring & Error Tracking
  if (isCorrect) {
    if (attemptCount === 1) {
      qState.status = "mastered_l1";
      qState.efficiency = 1.0;
    } else if (attemptCount === 2) {
      qState.status = "mastered_l2";
      qState.efficiency = 0.667;
    } else {
      qState.status = "mastered_l3";
      qState.efficiency = 0.333;
    }

    // Did the student make any mistake prior to getting it right?
    if (qState.had_mistake || attemptCount > 1) {
      if (!qState.error_logged) {
        qState.needs_error_log = true;
      }
    }
  } else {
    qState.had_mistake = true;
    if (attemptCount >= 3) {
      qState.status = "missed";
      qState.efficiency = 0.0;
      if (!qState.error_logged) {
        qState.needs_error_log = true;
      }
    } else {
      qState.status = `retry_l${attemptCount + 1}`;
      qState.efficiency = 0.0;
    }
  }

  // Save to Student's LocalStorage & Cross-Test Session Tracker
  App.studentState.attempts[q.id] = qState;
  saveLocalState();
  recordQuestionInGlobalSession(q, qState);

  // Pause timer so student can review explanations, hints, or record reflection without penalty
  pauseTimer();

  // Re-render UI
  renderCurrentQuestion();

  // If question is completed (correct or 3 attempts) and has unlogged mistake, show mandatory reflection modal!
  if ((isCorrect || attemptCount >= 3) && qState.needs_error_log && !qState.error_logged) {
    setTimeout(() => {
      openMandatoryReflectionModal(q, qState);
    }, 400);
  }
}

function evalFraction(str) {
  if (str.includes('/')) {
    const parts = str.split('/');
    if (parts.length === 2) {
      const num = parseFloat(parts[0]);
      const den = parseFloat(parts[1]);
      if (den !== 0) return num / den;
    }
  }
  const val = parseFloat(str);
  return isNaN(val) ? null : val;
}

// ================= BLUEBOOK QUESTION NAVIGATOR POPUP =================
function renderNavigatorTiles() {
  DOM.navTilesGrid.innerHTML = "";
  DOM.navModalModuleTitle.textContent = `${DOM.selectModule.options[DOM.selectModule.selectedIndex].text}`;

  App.questions.forEach((q, idx) => {
    const qState = App.studentState.attempts[q.id] || { status: "unanswered", attempts: [], marked: false };
    const tile = document.createElement("div");
    tile.className = "nav-tile";
    if (q.category === "example") {
      tile.classList.add("nav-tile-example");
    }
    tile.textContent = idx + 1;
    const tileBookPg = q.book_page || (q.pdf_page ? q.pdf_page - 1 : null);
    const tileBookStr = tileBookPg ? ` • Sách trang ${tileBookPg}` : "";
    tile.title = `${q.q_label || `Câu ${idx + 1}`}${tileBookStr}`;

    if (idx === App.currentIndex) tile.classList.add("current");
    if (qState.attempts && qState.attempts.length > 0) tile.classList.add("answered");
    if (qState.marked) tile.classList.add("marked");

    tile.addEventListener("click", () => {
      if (idx !== App.currentIndex && !checkCanNavigate()) return;
      if (idx !== App.currentIndex) {
        App.currentIndex = idx;
        renderCurrentQuestion();
      }
      DOM.navigatorOverlay.classList.add("hidden");
    });

    DOM.navTilesGrid.appendChild(tile);
  });
}

// ================= PDF NAVIGATION (GOOGLE DRIVE OFFICIAL) =================
function navigatePdf(page, zoom = null) {
  const maxPage = App.activeTestId === "panda-math" ? 317 : (App.activeTestId === "erica-writing" ? 218 : (App.activeTestId === "erica-reading" ? 175 : 44));
  const p = Math.max(1, Math.min(maxPage, parseInt(page) || 1));
  if (DOM.pdfSyncPageNum) DOM.pdfSyncPageNum.textContent = p;
}

function formatMarkdownHints(str) {
  if (!str) return "";
  return str
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, '<br>');
}

// ================= ERROR LOG & NOTEBOOK UTILS =================
function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function formatVocabHtml(vocabText) {
  if (!vocabText) return "";
  const lines = vocabText.split(/[\n;]+/).map(s => s.trim()).filter(Boolean);
  if (lines.length > 1) {
    return `<div style="display: flex; flex-direction: column; gap: 4px; margin-top: 4px;">` +
      lines.map(line => {
        const parts = line.split(/[:=–-]/);
        if (parts.length >= 2) {
          const word = parts[0].trim();
          const def = parts.slice(1).join("=").trim();
          return `<div><span class="vocab-tag-highlight">${escapeHtml(word)}</span>: ${escapeHtml(def)}</div>`;
        }
        return `<div>• ${escapeHtml(line)}</div>`;
      }).join("") + `</div>`;
  }
  return `<span>${escapeHtml(vocabText)}</span>`;
}

function updateErrorBadge() {
  const unres = (App.studentState.error_logs || []).filter(l => l.status !== "Đã triệt tiêu").length;
  if (DOM.badgeErrorCount) DOM.badgeErrorCount.textContent = unres;
}

function renderErrorLogs() {
  const list = App.studentState.error_logs || [];
  const total = list.length;
  const pending = list.filter(l => l.status === "Chưa xử lý").length;
  const tracking = list.filter(l => l.status === "Đang theo dõi").length;
  const resolved = list.filter(l => l.status === "Đã triệt tiêu").length;
  const vocabCount = list.filter(l => l.vocabulary && l.vocabulary.trim()).length;

  if (DOM.countChipAll) DOM.countChipAll.textContent = total;
  if (DOM.countChipPending) DOM.countChipPending.textContent = pending;
  if (DOM.countChipTracking) DOM.countChipTracking.textContent = tracking;
  if (DOM.countChipResolved) DOM.countChipResolved.textContent = resolved;
  if (DOM.badgeNotebookCount) {
    DOM.badgeNotebookCount.textContent = `${total} ghi chép • ${vocabCount} từ mới`;
  }

  DOM.errorLogList.innerHTML = "";

  const qLower = (App.notebookSearchQuery || "").toLowerCase();
  const filtered = list.filter(item => {
    const matchStatus = (App.notebookFilterStatus === "all" || item.status === App.notebookFilterStatus);
    if (!matchStatus) return false;
    if (!qLower) return true;
    const searchTarget = [
      item.q_label,
      item.question_id,
      item.module,
      item.skill,
      item.root_cause,
      item.trap_detail,
      item.student_notes,
      item.vocabulary
    ].filter(Boolean).join(" ").toLowerCase();
    return searchTarget.includes(qLower);
  });

  if (filtered.length === 0) {
    DOM.errorLogList.innerHTML = `
      <div style="text-align: center; padding: 36px 16px; color: #5f6368;">
        <div style="font-size: 32px; margin-bottom: 8px;">📭</div>
        <div style="font-weight: 600; font-size: 14px; color: #202124;">Không tìm thấy ghi chép nào</div>
        <div style="font-size: 12.5px; margin-top: 4px;">
          ${qLower ? `Không có kết quả khớp với từ khóa "${escapeHtml(qLower)}".` : `Em chưa có ghi chép thử sai hoặc từ vựng nào trong mục này.`}
        </div>
      </div>
    `;
    return;
  }

  filtered.forEach(item => {
    if (App.editingLogId === item.id) {
      // INLINE EDIT FORM (Google Material 3)
      const editCard = document.createElement("div");
      editCard.className = "g-inline-edit";
      editCard.innerHTML = `
        <div style="font-size: 13px; font-weight: 700; color: #1a73e8; margin-bottom: 10px;">
          ✏️ Đang chỉnh sửa: ${escapeHtml(item.module || "SAT")} • Câu ${escapeHtml(item.q_label || item.question_id || "")}
        </div>
        <div class="inline-edit-grid">
          <div>
            <label>Tình trạng xử lý:</label>
            <select class="g-select edit-status">
              <option value="Chưa xử lý" ${item.status === "Chưa xử lý" ? "selected" : ""}>⏳ Chưa xử lý</option>
              <option value="Đang theo dõi" ${item.status === "Đang theo dõi" ? "selected" : ""}>🔄 Đang theo dõi</option>
              <option value="Đã triệt tiêu" ${item.status === "Đã triệt tiêu" ? "selected" : ""}>✅ Đã triệt tiêu</option>
            </select>
          </div>
          <div>
            <label>Nhóm bẫy SAT:</label>
            <select class="g-select edit-trap">
              <option value="Bẫy từ vựng & Nghĩa trong ngữ cảnh (Context Clues)" ${item.root_cause?.includes("từ vựng") ? "selected" : ""}>📖 Bẫy từ vựng & Nghĩa trong ngữ cảnh (Context Clues)</option>
              <option value="Bẫy đảo cực & Từ tuyệt đối (Extreme Words: always, never, only...)" ${item.root_cause?.includes("đảo cực") ? "selected" : ""}>⚠️ Bẫy đảo cực & Từ tuyệt đối (Extreme Words: always, never, only...)</option>
              <option value="Bẫy tương phản giả & Cụm nối (However, Although, But...)" ${item.root_cause?.includes("tương phản") ? "selected" : ""}>⚡ Bẫy tương phản giả & Cụm nối (However, Although, But...)</option>
              <option value="Bẫy suy diễn quá xa / Lạc đề (Out of Scope / Assumption)" ${item.root_cause?.includes("suy diễn") ? "selected" : ""}>🔍 Bẫy suy diễn quá xa / Lạc đề (Out of Scope / Assumption)</option>
              <option value="Bẫy đọc lướt sót từ khóa quan trọng (Careless Reading)" ${item.root_cause?.includes("đọc lướt") ? "selected" : ""}>👀 Bẫy đọc lướt sót từ khóa quan trọng (Careless Reading)</option>
              <option value="Bẫy đại số / Đổi dấu / Chuyển vế nhầm (Algebra / Sign Trap)" ${item.root_cause?.includes("đại số") ? "selected" : ""}>🧮 Bẫy đại số / Đổi dấu / Chuyển vế nhầm (Algebra / Sign Trap)</option>
              <option value="Bẫy đọc nhầm câu hỏi (Đề hỏi y nhưng giải ra x)" ${item.root_cause?.includes("nhầm câu hỏi") ? "selected" : ""}>🎯 Bẫy đọc nhầm câu hỏi (Đề hỏi y nhưng giải ra x)</option>
              <option value="Bẫy làm tròn số / Phân số / Đơn vị đo (Fractions / Units)" ${item.root_cause?.includes("làm tròn") ? "selected" : ""}>📏 Bẫy làm tròn số / Phân số / Đơn vị đo (Fractions / Units)</option>
              <option value="Chưa nắm chắc công thức / lý thuyết cốt lõi" ${item.root_cause?.includes("công thức") ? "selected" : ""}>📚 Chưa nắm chắc công thức / lý thuyết cốt lõi</option>
              <option value="Khác" ${item.root_cause === "Khác" ? "selected" : ""}>💡 Bẫy khác...</option>
            </select>
          </div>
          <div class="full-width">
            <label>Phân tích nguyên nhân thử sai & Bài học rút ra:</label>
            <textarea class="g-textarea edit-detail" rows="2">${escapeHtml(item.trap_detail || "")}</textarea>
          </div>
          <div class="full-width">
            <label>📝 Ghi chú tư duy cá nhân (Mẹo nhớ nhanh):</label>
            <textarea class="g-textarea edit-notes" rows="2" placeholder="Ví dụ: Quy tắc gạch chân từ khóa, cách giải nhanh...">${escapeHtml(item.student_notes || "")}</textarea>
          </div>
          <div class="full-width">
            <label>📖 Từ mới & Thuật ngữ tiếng Anh:</label>
            <textarea class="g-textarea edit-vocab" rows="2" placeholder="Ví dụ: repudiate = bác bỏ; ephemeral = ngắn ngủi...">${escapeHtml(item.vocabulary || "")}</textarea>
          </div>
        </div>
        <div class="inline-edit-actions">
          <button class="btn-subtle btn-cancel-edit">✕ Hủy</button>
          <button class="btn-primary-g btn-save-edit">💾 Lưu thay đổi</button>
        </div>
      `;

      editCard.querySelector(".btn-cancel-edit").addEventListener("click", () => {
        App.editingLogId = null;
        renderErrorLogs();
      });

      editCard.querySelector(".btn-save-edit").addEventListener("click", () => {
        const newDetail = editCard.querySelector(".edit-detail").value.trim();
        if (!newDetail) {
          alert("Vui lòng không để trống phần phân tích thử sai!");
          return;
        }
        item.status = editCard.querySelector(".edit-status").value;
        item.root_cause = editCard.querySelector(".edit-trap").value;
        item.trap_detail = newDetail;
        item.student_notes = editCard.querySelector(".edit-notes").value.trim();
        item.vocabulary = editCard.querySelector(".edit-vocab").value.trim();

        saveLocalState();
        App.editingLogId = null;
        updateErrorBadge();
        renderErrorLogs();
      });

      DOM.errorLogList.appendChild(editCard);
      return;
    }

    // READ CARD (Material 3 Minimalist)
    const card = document.createElement("div");
    card.className = "g-notebook-card";

    let statusClass = "status-tracking";
    let statusText = "🔄 Đang theo dõi";
    if (item.status === "Chưa xử lý") {
      statusClass = "status-pending";
      statusText = "⏳ Chưa xử lý";
    } else if (item.status === "Đã triệt tiêu") {
      statusClass = "status-resolved";
      statusText = "✅ Đã triệt tiêu";
    }

    const notesHtml = item.student_notes ? `
      <div class="card-notes-box">
        <strong>📝 Ghi chú tư duy:</strong> ${escapeHtml(item.student_notes)}
      </div>
    ` : "";

    const vocabHtml = item.vocabulary ? `
      <div class="card-vocab-box">
        <strong>📖 Từ mới / Thuật ngữ:</strong>
        ${formatVocabHtml(item.vocabulary)}
      </div>
    ` : "";

    const quickToggleBtn = (item.status === "Đã triệt tiêu") ?
      `<button class="btn-quick-toggle-status" title="Chuyển về trạng thái đang theo dõi">🔄 Đưa về theo dõi</button>` :
      `<button class="btn-quick-toggle-status" title="Đánh dấu em đã nắm vững kiến thức này">✅ Đã triệt tiêu</button>`;

    card.innerHTML = `
      <div class="card-top-row">
        <div class="card-top-left">
          <span class="card-q-tag">📘 ${escapeHtml(item.module || "SAT")} • Câu ${escapeHtml(item.q_label || item.question_id || "")}</span>
          <span class="card-status-badge ${statusClass}">${statusText}</span>
        </div>
        <div class="card-top-right">
          <button class="btn-card-action btn-edit-card" title="Chỉnh sửa ghi chép này">✏️ Sửa</button>
          <button class="btn-card-action btn-del-card" title="Xóa ghi chép này">✕</button>
        </div>
      </div>

      <div class="card-trap-content">
        <span class="card-trap-tag">${escapeHtml(item.root_cause || "Bẫy SAT")}</span>
        <span>${escapeHtml(item.trap_detail || "")}</span>
      </div>

      ${notesHtml}
      ${vocabHtml}

      <div class="card-footer">
        <span>🕒 ${escapeHtml(item.date || "Ghi chép")} ${item.skill ? `• ${escapeHtml(item.skill)}` : ""}</span>
        <div>${quickToggleBtn}</div>
      </div>
    `;

    // Edit button
    card.querySelector(".btn-edit-card").addEventListener("click", () => {
      App.editingLogId = item.id;
      renderErrorLogs();
    });

    // Delete button
    card.querySelector(".btn-del-card").addEventListener("click", () => {
      if (confirm(`Em có chắc chắn muốn xóa ghi chép thử sai câu ${item.q_label || item.question_id} này không?`)) {
        App.studentState.error_logs = App.studentState.error_logs.filter(x => x.id !== item.id);
        saveLocalState();
        updateErrorBadge();
        renderErrorLogs();
      }
    });

    // Quick status toggle
    const toggleBtn = card.querySelector(".btn-quick-toggle-status");
    if (toggleBtn) {
      toggleBtn.addEventListener("click", () => {
        item.status = (item.status === "Đã triệt tiêu") ? "Đang theo dõi" : "Đã triệt tiêu";
        saveLocalState();
        updateErrorBadge();
        renderErrorLogs();
      });
    }

    DOM.errorLogList.appendChild(card);
  });
}

function renderStrategiesModal() {
  if (!App.db || !App.db.strategies) return;
  DOM.strategiesContent.innerHTML = "";

  App.db.strategies.forEach(s => {
    const box = document.createElement("div");
    box.style.cssText = "background: var(--bb-bg-surface-elevated); border: 1px solid var(--bb-border); border-radius: 8px; padding: 16px; margin-bottom: 14px;";
    box.innerHTML = `
      <h4 style="color: #0369a1; font-size: 15px; font-weight: 800; margin-bottom: 6px;">${s.domain} (${s.category})</h4>
      <div style="font-size: 13px; line-height: 1.6; margin-bottom: 8px;"><strong>📚 Chiến thuật cốt lõi:</strong><br>${s.core_rules.replace(/\n/g, '<br>')}</div>
      <div style="font-size: 13px; line-height: 1.6; background: #fffbeb; border-left: 3px solid #d97706; padding: 8px 12px; border-radius: 4px;"><strong>⚠️ Bẫy SAT thường gặp:</strong><br>${s.traps.replace(/\n/g, '<br>')}</div>
    `;
    DOM.strategiesContent.appendChild(box);
  });
}

// ================= PRACTICE GUIDE MODAL =================
function initOnboarding() {
  const hasProfile = App.studentState.student_name && App.studentState.student_email;
  // Landing page contains profile form, keep guide modal hidden initially
  if (DOM.modalOnboarding) {
    DOM.modalOnboarding.classList.add("hidden");
    DOM.modalOnboarding.style.display = "none";
  }

  if (hasProfile) {
    if (DOM.headerStudentName) DOM.headerStudentName.textContent = App.studentState.student_name;
    if (DOM.inputStudentName) DOM.inputStudentName.value = App.studentState.student_name;
    if (DOM.homeStudentNameChip) DOM.homeStudentNameChip.textContent = App.studentState.student_name;
  }

  // Start Practice from Guide Modal
  if (DOM.btnObStart) {
    DOM.btnObStart.addEventListener("click", () => {
      if (DOM.modalOnboarding) {
        DOM.modalOnboarding.classList.add("hidden");
        DOM.modalOnboarding.style.display = "none";
      }
      startPracticeFromHome();
    });
  }

  // Dismiss Guide Modal
  if (DOM.btnGuideDismiss) {
    DOM.btnGuideDismiss.addEventListener("click", () => {
      if (DOM.modalOnboarding) {
        DOM.modalOnboarding.classList.add("hidden");
        DOM.modalOnboarding.style.display = "none";
      }
    });
  }

  // Close Guide Modal (X button)
  if (DOM.btnCloseOnboarding) {
    DOM.btnCloseOnboarding.addEventListener("click", () => {
      if (DOM.modalOnboarding) {
        DOM.modalOnboarding.classList.add("hidden");
        DOM.modalOnboarding.style.display = "none";
      }
    });
  }

  // Backdrop click closes Guide Modal
  if (DOM.modalOnboarding) {
    DOM.modalOnboarding.addEventListener("click", (e) => {
      if (e.target === DOM.modalOnboarding) {
        DOM.modalOnboarding.classList.add("hidden");
        DOM.modalOnboarding.style.display = "none";
      }
    });
  }

  // Edit Profile from Practice Header
  if (DOM.headerStudentBadge) {
    DOM.headerStudentBadge.addEventListener("click", () => {
      const current = App.studentState.student_name || "";
      const updated = prompt("Chỉnh sửa Họ và tên thí sinh:", current);
      if (updated && updated.trim()) {
        App.studentState.student_name = updated.trim();
        saveLocalState();
        syncHomeProfile();
        if (DOM.headerStudentName) DOM.headerStudentName.textContent = updated.trim();
      }
    });
  }
}

function handleHomeClick() {
  showView("home");
}

function handleResetConfirm() {
  // 1. Reset answers & attempts
  App.studentState.attempts = {};

  // 2. Reset timer if checked
  if (DOM.chkResetTimer && DOM.chkResetTimer.checked) {
    App.studentState.timer_seconds = {
      "RW_Module1": 32 * 60,
      "RW_Module2": 32 * 60,
      "Math_Module1": 35 * 60,
      "Math_Module2": 35 * 60,
      "ALL": 134 * 60
    };
  }

  // 3. Reset error logs if checked
  if (DOM.chkResetErrors && DOM.chkResetErrors.checked) {
    App.studentState.error_logs = [];
  }

  // 3b. Reset cross-test session counter if checked
  if (DOM.chkResetSessionCounter && DOM.chkResetSessionCounter.checked) {
    App.globalSessionItems = {};
    if (App.sessionPracticedIds) App.sessionPracticedIds.clear();
  } else if (App.globalSessionItems) {
    const prefix = `${App.activeTestId}::`;
    Object.keys(App.globalSessionItems).forEach(k => {
      if (k.startsWith(prefix)) delete App.globalSessionItems[k];
    });
  }
  saveGlobalSessionTracker();

  // 4. Reset navigation to Question 1 of active first module
  const firstModCode = (App.db && Array.isArray(App.db.modules) && App.db.modules[0]) ? App.db.modules[0].code : "RW_Module1";
  App.activeModuleCode = firstModCode;
  if (DOM.selectModule) DOM.selectModule.value = firstModCode;
  App.currentIndex = 0;
  App.studentState.active_module = firstModCode;
  App.studentState.active_q_index = 0;

  // 5. Persist and Re-render
  saveLocalState();
  setupModuleQuestions();
  startModuleTimer();
  updateErrorBadge();
  renderCurrentQuestion();

  DOM.modalResetConfirm.classList.add("hidden");
  alert("✨ Đã đặt lại bài thi thành công! Chúc em luyện tập thật tốt!");
}

// ================= TEST SUMMARY CALCULATION =================
function calculateTestSummary() {
  const allQs = (App.db && App.db.questions) ? App.db.questions : [];
  const total = allQs.length || 98;
  const attempts = App.studentState.attempts || {};

  let answered = 0;
  let l1Correct = 0;
  let l2Correct = 0;
  let l3Correct = 0;
  let earnedWeight = 0;

  allQs.forEach(q => {
    const st = attempts[q.id];
    if (st && st.attempts && st.attempts.length > 0) {
      answered++;
      const eff = parseFloat(st.efficiency) || 0;
      earnedWeight += eff;
      if (eff >= 0.99) l1Correct++;
      else if (eff >= 0.60) l2Correct++;
      else if (eff >= 0.30) l3Correct++;
    }
  });

  const scorePct = total > 0 ? Math.round((earnedWeight / total) * 100) : 0;
  const unanswered = Math.max(0, total - answered);

  return {
    total,
    answered,
    unanswered,
    l1Correct,
    l2Correct,
    l3Correct,
    scorePct,
    timeSpent: "Hoàn tất các Module"
  };
}

// ================= MANDATORY ERROR REFLECTION =================
function checkCanNavigate() {
  const currentQ = App.currentQuestion;
  if (!currentQ) return true;
  const qState = App.studentState.attempts[currentQ.id];
  if (qState && qState.needs_error_log && !qState.error_logged) {
    alert("⚠️ Em cần hoàn thành ghi chép sổ thử sai cho câu này trước khi chuyển sang câu tiếp theo!");
    openMandatoryReflectionModal(currentQ, qState);
    return false;
  }
  return true;
}

function openMandatoryReflectionModal(q, qState) {
  // Always pause timer during error notebook reflection
  pauseTimer();

  if (!q) q = App.currentQuestion;
  if (!qState) qState = App.studentState.attempts[q.id];
  if (!q || !qState) return;

  DOM.reflQLabel.textContent = `Câu ${q.q_label}`;
  DOM.reflQTopic.textContent = q.topic;
  DOM.reflQModule.textContent = q.module_title;
  DOM.reflCorrectAns.textContent = q.correct_answer;

  const wrongs = (qState.attempts || []).filter(a => a.toUpperCase() !== q.correct_answer.toUpperCase());
  DOM.reflWrongPicks.textContent = wrongs.length > 0
    ? wrongs.map((w, idx) => `Lần ${idx + 1}: [${w}]`).join("  •  ")
    : "Có lần thử trước đó chưa chính xác";

  const hint1 = q.tier1_hint || q.level1_tip || "Đọc kỹ từ khóa, ngữ cảnh và xác định bẫy SAT.";
  const hint2 = q.tier2_hint || q.level2_hint || "";
  DOM.reflHintBox.innerHTML = `<strong>💡 Gợi ý Tầng 1:</strong> ${hint1}${hint2 ? `<br><strong style="margin-top: 6px; display: inline-block;">🔍 Manh mối Tầng 2:</strong> ${hint2}` : ""}`;

  DOM.selectReflTrap.value = "";
  DOM.inputReflDetail.value = "";
  if (DOM.inputReflNotes) DOM.inputReflNotes.value = "";
  if (DOM.inputReflVocab) DOM.inputReflVocab.value = "";

  DOM.modalMandatoryReflection.classList.remove("hidden");
}

function saveMandatoryReflection(advanceToNext = true) {
  const q = App.currentQuestion;
  if (!q) return;
  const qState = App.studentState.attempts[q.id];
  if (!qState) return;

  const trap = DOM.selectReflTrap.value;
  const detail = DOM.inputReflDetail.value.trim();
  const notes = DOM.inputReflNotes ? DOM.inputReflNotes.value.trim() : "";
  const vocab = DOM.inputReflVocab ? DOM.inputReflVocab.value.trim() : "";

  if (!trap) {
    alert("Vui lòng chọn nhóm bẫy SAT em đã gặp phải!");
    DOM.selectReflTrap.focus();
    return;
  }

  if (!detail || detail.length < 5) {
    alert("Vui lòng nhập phân tích nguyên nhân thử sai và bài học rút ra (tối thiểu 5 ký tự)!");
    DOM.inputReflDetail.focus();
    return;
  }

  const newLog = {
    id: `err_${q.id}_${Date.now()}`,
    question_id: q.id,
    q_label: q.q_label,
    module: q.module_title,
    skill: q.topic,
    date: new Date().toLocaleDateString("vi-VN"),
    wrong_attempts: (qState.attempts || []).filter(a => a.toUpperCase() !== q.correct_answer.toUpperCase()),
    correct_answer: q.correct_answer,
    root_cause: trap,
    trap_detail: detail,
    student_notes: notes,
    vocabulary: vocab,
    socratic_analysis: q.level1_tip || "",
    status: "Đang theo dõi"
  };

  if (!App.studentState.error_logs) App.studentState.error_logs = [];
  App.studentState.error_logs.unshift(newLog);

  qState.error_logged = true;
  qState.needs_error_log = false;
  qState.reviewAllHints = true;
  App.studentState.attempts[q.id] = qState;

  saveLocalState();
  updateErrorBadge();
  renderErrorLogs();

  DOM.modalMandatoryReflection.classList.add("hidden");

  if (advanceToNext) {
    // Show a brief success alert & auto advance
    alert("✅ Ghi chép sổ thử sai thành công! Em đã mở khóa và có thể tiếp tục làm câu tiếp theo.");
    if (App.currentIndex < App.questions.length - 1) {
      App.currentIndex++;
      renderCurrentQuestion();
    } else {
      renderCurrentQuestion();
      syncTimerState();
    }
  } else {
    // Stay on current question with all hints unlocked and expanded
    renderCurrentQuestion();

    if (DOM.hintContent1) DOM.hintContent1.classList.remove("collapsed");
    if (DOM.hintContent2) DOM.hintContent2.classList.remove("collapsed");
    if (DOM.hintContent3) DOM.hintContent3.classList.remove("collapsed");
    if (DOM.hintContent4) DOM.hintContent4.classList.remove("collapsed");

    pauseTimer();

    const hintSec = document.getElementById("hint-card-1") || DOM.hintsContainer;
    if (hintSec) {
      hintSec.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }

    alert("💡 Đã lưu vào Sổ Thử Sai! Tất cả các tầng gợi ý & chiến thuật của câu này đã được mở khóa hoàn toàn để em nghiên cứu kỹ lưỡng.");
  }
}

// ================= CONSOLIDATED PRACTICE EXCEL EXPORT (MULTI-SOURCE + MULTI-TIER + NOTEBOOK) =================
function cleanTextForExcel(raw, maxLen = 30000) {
  if (raw === null || raw === undefined) return "";
  let s = String(raw);
  s = s
    .replace(/<\s*br\s*\/?>/gi, "\n")
    .replace(/<\/\s*(p|div|li|h[1-6]|tr)\s*>/gi, "\n")
    .replace(/<li[^>]*>/gi, "• ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/gi, " ")
    .replace(/&amp;/gi, "&")
    .replace(/&lt;/gi, "<")
    .replace(/&gt;/gi, ">")
    .replace(/&quot;/gi, '"')
    .replace(/&#0?39;/gi, "'")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n[ \t]+/g, "\n")
    .replace(/[ \t]{2,}/g, " ")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
  if (s.length > maxLen) {
    s = s.slice(0, maxLen - 3) + "...";
  }
  return s;
}

function formatExcelDateTime(val) {
  if (!val) return "";
  try {
    const d = new Date(val);
    if (!isNaN(d.getTime())) {
      return d.toLocaleString("vi-VN");
    }
  } catch (e) {}
  return String(val);
}

function buildQuestionTierFeedbacks(q) {
  if (!q) return { tier1: "", tier2: "", tier3: "", tier4: "" };
  const tier1 = cleanTextForExcel(q.tier1_hint || q.level1_tip || "");
  const tier2 = cleanTextForExcel(q.tier2_hint || q.level2_hint || "");

  const t3Parts = [];
  const baseT3 = cleanTextForExcel(q.tier3_hint || q.level3_solution || "");
  if (baseT3) t3Parts.push(baseT3);
  const solSteps = cleanTextForExcel(q.solution_steps || "");
  if (solSteps && (!baseT3 || !baseT3.includes(solSteps.slice(0, 40)))) {
    t3Parts.push(`Các bước giải:\n${solSteps}`);
  }
  const pooe = cleanTextForExcel(q.pooe_breakdown || "");
  if (pooe && (!baseT3 || !baseT3.includes(pooe.slice(0, 40)))) {
    t3Parts.push(`Phân tích loại trừ (POOE):\n${pooe}`);
  }
  const gridExp = cleanTextForExcel(q.grid_in_explanation || "");
  if (gridExp && (!baseT3 || !baseT3.includes(gridExp.slice(0, 40)))) {
    t3Parts.push(`Hướng dẫn điền số (Grid-In):\n${gridExp}`);
  }
  const tier3 = cleanTextForExcel(t3Parts.join("\n\n"));

  const t4Parts = [];
  if (q.princeton_strategy) t4Parts.push(`Chiến thuật Princeton Review: ${cleanTextForExcel(q.princeton_strategy)}`);
  if (q.target_clue) t4Parts.push(`Phân tích manh mối & Target: ${cleanTextForExcel(q.target_clue)}`);
  if (q.pro_tip) t4Parts.push(`Mẹo độc quyền Pro-Tip: ${cleanTextForExcel(q.pro_tip)}`);
  const stratTip = cleanTextForExcel(q.strategic_tip || "");
  if (stratTip) t4Parts.push(t4Parts.length > 0 ? `Chiến thuật / Công thức cốt lõi: ${stratTip}` : stratTip);
  const tier4 = cleanTextForExcel(t4Parts.join("\n\n"));

  return { tier1, tier2, tier3, tier4 };
}

function formatQuestionPromptForExcel(q) {
  if (!q) return "";
  const parts = [];
  const passage = cleanTextForExcel(q.passage || "", 12000);
  const prompt = cleanTextForExcel(q.prompt || "", 4000);
  if (passage) parts.push(`[Ngữ liệu]: ${passage}`);
  if (prompt) parts.push(`[Câu hỏi]: ${prompt}`);
  if (q.is_grid_in) {
    parts.push("[Hình thức]: Tự luận điền đáp án (Grid-in)");
  } else if (Array.isArray(q.options) && q.options.length > 0) {
    const optStr = q.options.map(o => `${o.key}) ${cleanTextForExcel(o.text || "", 1000)}`).join(" | ");
    if (optStr) parts.push(`[Phương án]: ${optStr}`);
  } else if (q.options_raw) {
    parts.push(`[Phương án]: ${cleanTextForExcel(q.options_raw, 4000)}`);
  }
  return cleanTextForExcel(parts.join("\n"), 20000);
}

function parseSocraticVocabEntries(vocabText) {
  if (!vocabText) return [];
  const lines = String(vocabText).split(/[\n;]+/).map(s => s.trim()).filter(Boolean);
  return lines.map(line => {
    const m = line.match(/^(.*?)\s*(?:[:=–—]|\s+-\s+)\s*(.+)$/);
    if (m && m[1].trim() && m[2].trim()) {
      return { term: m[1].trim(), meaning: m[2].trim() };
    }
    return { term: line, meaning: "" };
  });
}

function getExportStatusMeta(qState) {
  const status = (qState && qState.status) ? String(qState.status) : "";
  const eff = parseFloat(qState && qState.efficiency) || 0;
  const isL1 = eff >= 0.99 || status === "mastered_l1";
  const isL2 = !isL1 && (eff >= 0.6 || status === "mastered_l2");
  const isL3 = !isL1 && !isL2 && (eff >= 0.3 || status === "mastered_l3");
  const isCorrect = isL1 || isL2 || isL3;

  let statusLabel = "Đang thử lại (Chưa hoàn thành)";
  if (isL1) statusLabel = "Đúng Lần 1 (L1 - 100%)";
  else if (isL2) statusLabel = "Đúng Lần 2 (L2 - 66.7%)";
  else if (isL3) statusLabel = "Đúng Lần 3 (L3 - 33.3%)";
  else if (status === "missed" || ((qState && Array.isArray(qState.attempts) ? qState.attempts.length : 0) >= 3 && !isCorrect)) {
    statusLabel = "Sai cả 3 lần (0%)";
  }

  return { isCorrect, isL1, isL2, isL3, eff, effPct: Math.round(eff * 100), statusLabel };
}

function getSavedStateForTestId(meta) {
  const canonicalId = meta.id;
  const activeCanonical = (getActiveTestMeta() || {}).id || App.activeTestId;
  if (canonicalId === activeCanonical || canonicalId === App.activeTestId || meta.code === App.activeTestId) {
    return App.studentState || { attempts: {}, error_logs: [] };
  }

  const keysToTry = [getStorageKeyForTest(meta.id)];
  if (meta.code && meta.code !== meta.id) keysToTry.push(`bluebook_${meta.code}_student_state_v1`);
  if (meta.id === "oct-2026") keysToTry.push(LEGACY_STORAGE_KEY);

  for (const key of keysToTry) {
    try {
      const raw = localStorage.getItem(key);
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed && typeof parsed === "object") {
          return {
            student_name: parsed.student_name || "",
            student_email: parsed.student_email || "",
            student_target: parsed.student_target || "1400+",
            attempts: parsed.attempts || {},
            error_logs: Array.isArray(parsed.error_logs)
              ? parsed.error_logs.filter(e => e && e.id && !String(e.id).startsWith("err_oct_"))
              : []
          };
        }
      }
    } catch (e) {}
  }
  return { attempts: {}, error_logs: [] };
}

async function ensureTestDbLoadedForExport(meta) {
  if (!App.dbCacheByTestId) App.dbCacheByTestId = {};
  const activeCanonical = (getActiveTestMeta() || {}).id || App.activeTestId;
  if ((meta.id === activeCanonical || meta.id === App.activeTestId || meta.code === App.activeTestId) && App.db) {
    App.dbCacheByTestId[meta.id] = App.db;
    return App.db;
  }
  if (App.dbCacheByTestId[meta.id]) return App.dbCacheByTestId[meta.id];
  if (meta.dataFile) {
    try {
      const res = await fetch(meta.dataFile);
      if (res.ok) {
        const db = await res.json();
        App.dbCacheByTestId[meta.id] = db;
        return db;
      }
    } catch (e) {
      console.warn("Could not hydrate dataset for export:", meta.dataFile, e);
    }
  }
  return null;
}

async function collectConsolidatedExportData(studentName) {
  const manifest = (App.testsManifest && App.testsManifest.length) ? App.testsManifest : TESTS_MANIFEST_DEFAULT;
  const sessionItemsAll = Object.values(App.globalSessionItems || {});

  const practicedRows = [];
  const errorLogs = [];
  const vocabEntries = [];
  const byTestStats = [];
  const byModuleMap = {};
  const seenErrorKeys = new Set();

  let totalPracticed = 0;
  let totalCorrect = 0;
  let totalL1 = 0;
  let totalL2 = 0;
  let totalL3 = 0;
  let totalEarnedWeight = 0;

  for (const meta of manifest) {
    const state = getSavedStateForTestId(meta);
    const attemptsMap = state.attempts || {};
    const testErrors = Array.isArray(state.error_logs) ? state.error_logs : [];
    const matchingSessionItems = sessionItemsAll.filter(it => it && (it.test_id === meta.id || it.test_id === meta.code));

    const practicedQids = Object.keys(attemptsMap).filter(qid => {
      const st = attemptsMap[qid];
      return st && Array.isArray(st.attempts) && st.attempts.length > 0;
    });

    if (practicedQids.length === 0 && testErrors.length === 0 && matchingSessionItems.length === 0) {
      continue;
    }

    const db = await ensureTestDbLoadedForExport(meta);
    const allQs = (db && Array.isArray(db.questions)) ? db.questions : [];
    const qById = new Map();
    allQs.forEach(q => qById.set(String(q.id), q));

    // Build lookup from error logs by question_id so practiced questions link to Socratic reflections
    const errByQid = {};
    testErrors.forEach(err => {
      const qKey = String(err.question_id || "");
      if (!errByQid[qKey]) errByQid[qKey] = [];
      errByQid[qKey].push(err);
    });

    const testShort = meta.short_title || (db && db.test_title) || meta.title || meta.id;
    const testStat = {
      test_id: meta.id,
      test_short: testShort,
      test_title: meta.title || testShort,
      bank_total: allQs.length || meta.total_questions || 0,
      practiced: 0,
      correct: 0,
      unfinished_or_missed: 0,
      l1: 0,
      l2: 0,
      l3: 0,
      earned_weight: 0,
      accuracy_pct: 0,
      weighted_pct: 0,
      error_log_count: testErrors.length
    };

    // Order practiced questions cleanly by canonical question order first, then any extras
    const orderedIds = [];
    const pushedIds = new Set();
    allQs.forEach(q => {
      const idStr = String(q.id);
      const st = attemptsMap[q.id] || attemptsMap[idStr];
      if (st && Array.isArray(st.attempts) && st.attempts.length > 0) {
        orderedIds.push(idStr);
        pushedIds.add(idStr);
      }
    });
    practicedQids.forEach(idStr => {
      if (!pushedIds.has(idStr)) {
        orderedIds.push(idStr);
        pushedIds.add(idStr);
      }
    });

    orderedIds.forEach(idStr => {
      const q = qById.get(idStr);
      const st = attemptsMap[idStr] || (q ? attemptsMap[q.id] : null);
      if (!st || !Array.isArray(st.attempts) || st.attempts.length === 0) return;

      const sMeta = getExportStatusMeta(st);
      totalPracticed++;
      if (sMeta.isCorrect) totalCorrect++;
      if (sMeta.isL1) totalL1++;
      else if (sMeta.isL2) totalL2++;
      else if (sMeta.isL3) totalL3++;
      totalEarnedWeight += sMeta.eff;

      testStat.practiced++;
      if (sMeta.isCorrect) testStat.correct++;
      else testStat.unfinished_or_missed++;
      if (sMeta.isL1) testStat.l1++;
      else if (sMeta.isL2) testStat.l2++;
      else if (sMeta.isL3) testStat.l3++;
      testStat.earned_weight += sMeta.eff;

      const modTitle = (q && (q.module_title || q.chapter || q.module_code)) || "SAT";
      const modKey = `${meta.id}::${modTitle}`;
      if (!byModuleMap[modKey]) {
        byModuleMap[modKey] = {
          test_short: testShort,
          module_title: modTitle,
          practiced: 0,
          correct: 0,
          l1: 0,
          l2: 0,
          l3: 0,
          earned_weight: 0
        };
      }
      const mStat = byModuleMap[modKey];
      mStat.practiced++;
      if (sMeta.isCorrect) mStat.correct++;
      if (sMeta.isL1) mStat.l1++;
      else if (sMeta.isL2) mStat.l2++;
      else if (sMeta.isL3) mStat.l3++;
      mStat.earned_weight += sMeta.eff;

      const tiers = buildQuestionTierFeedbacks(q);
      const matchingErrs = errByQid[idStr] || [];
      const errSummary = matchingErrs.map(e => {
        const head = e.root_cause ? `[${e.root_cause}]` : "[Sổ thử sai]";
        const body = cleanTextForExcel(e.trap_detail || "");
        const note = e.student_notes ? ` | Ghi chú: ${cleanTextForExcel(e.student_notes)}` : "";
        return `${head} ${body}${note}`;
      }).join("\n");

      const pageParts = [];
      if (q && q.pdf_page) pageParts.push(`PDF tr.${q.pdf_page}`);
      if (q && q.book_page) pageParts.push(`Sách tr.${q.book_page}`);

      const topicParts = [];
      if (q && q.topic) topicParts.push(q.topic);
      if (q && q.domain && !String(q.topic || "").includes(q.domain)) topicParts.push(q.domain);
      if (q && q.calc_mode) topicParts.push(q.calc_mode);

      practicedRows.push({
        stt: practicedRows.length + 1,
        test_id: meta.id,
        test_short: testShort,
        module_title: modTitle,
        q_label: (q && q.q_label) || `Q${idStr}`,
        topic: topicParts.join(" • "),
        page_label: pageParts.join(" / "),
        difficulty: (q && q.difficulty) || "",
        question_content: formatQuestionPromptForExcel(q),
        attempt_1: st.attempts[0] !== undefined ? String(st.attempts[0]) : "",
        attempt_2: st.attempts[1] !== undefined ? String(st.attempts[1]) : "",
        attempt_3: st.attempts[2] !== undefined ? String(st.attempts[2]) : "",
        correct_answer: (q && q.correct_answer) ? String(q.correct_answer) : "",
        status_label: sMeta.statusLabel,
        efficiency_pct: sMeta.effPct,
        tier1_feedback: tiers.tier1,
        tier2_feedback: tiers.tier2,
        tier3_feedback: tiers.tier3,
        tier4_feedback: tiers.tier4,
        error_note_summary: errSummary,
        practiced_at: formatExcelDateTime(st.last_practiced_at)
      });
    });

    if (testStat.practiced > 0) {
      testStat.accuracy_pct = Math.round((testStat.correct / testStat.practiced) * 100);
      testStat.weighted_pct = Math.round((testStat.earned_weight / testStat.practiced) * 100);
      byTestStats.push(testStat);
    }

    // Collect Error Notebook & Socratic Vocabulary rows for this test
    testErrors.forEach(err => {
      const uniq = `${meta.id}::${err.id || `${err.question_id}_${err.date}`}`;
      if (seenErrorKeys.has(uniq)) return;
      seenErrorKeys.add(uniq);

      const q = qById.get(String(err.question_id || ""));
      const wrongsText = Array.isArray(err.wrong_attempts)
        ? err.wrong_attempts.join(", ")
        : (err.wrong_attempts ? String(err.wrong_attempts) : "");
      const vocabRaw = cleanTextForExcel(err.vocabulary || "");
      const socraticRef = cleanTextForExcel(
        err.socratic_analysis || (q && (q.tier1_hint || q.level1_tip)) || ""
      );

      const row = {
        stt: errorLogs.length + 1,
        test_short: testShort,
        q_label: String(err.q_label || (q && q.q_label) || (err.question_id ? `Q${err.question_id}` : "Ghi chép")),
        module: cleanTextForExcel(err.module || (q && (q.module_title || q.chapter)) || "SAT"),
        skill: cleanTextForExcel(err.skill || (q && q.topic) || ""),
        wrong_attempts: wrongsText,
        correct_answer: String(err.correct_answer || (q && q.correct_answer) || ""),
        root_cause: cleanTextForExcel(err.root_cause || "Bẫy SAT"),
        trap_detail: cleanTextForExcel(err.trap_detail || ""),
        student_notes: cleanTextForExcel(err.student_notes || ""),
        vocabulary: vocabRaw,
        socratic_analysis: socraticRef,
        status: cleanTextForExcel(err.status || "Đang theo dõi"),
        date: String(err.date || new Date().toLocaleDateString("vi-VN"))
      };
      errorLogs.push(row);

      if (vocabRaw) {
        const parsedTerms = parseSocraticVocabEntries(vocabRaw);
        parsedTerms.forEach(vt => {
          vocabEntries.push({
            stt: vocabEntries.length + 1,
            test_short: testShort,
            q_label: row.q_label,
            module_skill: [row.module, row.skill].filter(Boolean).join(" • "),
            term: vt.term,
            meaning: vt.meaning,
            context_note: [row.root_cause, row.student_notes].filter(Boolean).join(" | "),
            date: row.date
          });
        });
      }
    });
  }

  const byModuleStats = Object.values(byModuleMap).map(m => ({
    test_short: m.test_short,
    module_title: m.module_title,
    practiced: m.practiced,
    correct: m.correct,
    unfinished_or_missed: Math.max(0, m.practiced - m.correct),
    l1: m.l1,
    l2: m.l2,
    l3: m.l3,
    accuracy_pct: m.practiced > 0 ? Math.round((m.correct / m.practiced) * 100) : 0,
    weighted_pct: m.practiced > 0 ? Math.round((m.earned_weight / m.practiced) * 100) : 0
  }));

  const accuracyPct = totalPracticed > 0 ? Math.round((totalCorrect / totalPracticed) * 100) : 0;
  const weightedPct = totalPracticed > 0 ? Math.round((totalEarnedWeight / totalPracticed) * 100) : 0;

  // Session counter (cross-test ARR session metrics) for transparency
  const sessionPracticed = sessionItemsAll.length;
  const sessionCorrect = sessionItemsAll.filter(it => it && it.is_correct).length;
  const sessionAccuracyPct = sessionPracticed > 0 ? Math.round((sessionCorrect / sessionPracticed) * 100) : 0;

  const sourcesSummary = byTestStats.length > 0
    ? byTestStats.map(s => `${s.test_short} (${s.correct}/${s.practiced})`).join(" + ")
    : ((getActiveTestMeta() || {}).short_title || "Digital SAT");

  return {
    generated_at: new Date().toLocaleString("vi-VN"),
    generated_date_iso: new Date().toISOString().slice(0, 10),
    student: {
      name: studentName,
      email: (App.studentState && App.studentState.student_email) || "Chưa cung cấp",
      target: (App.studentState && App.studentState.student_target) || "1400+",
      sources_summary: sourcesSummary
    },
    overall: {
      total_practiced: totalPracticed,
      total_correct: totalCorrect,
      total_unfinished_or_missed: Math.max(0, totalPracticed - totalCorrect),
      l1_correct: totalL1,
      l2_correct: totalL2,
      l3_correct: totalL3,
      accuracy_pct: accuracyPct,
      weighted_pct: weightedPct,
      error_logs_count: errorLogs.length,
      vocab_notes_count: errorLogs.filter(e => e.vocabulary && e.vocabulary.trim()).length,
      vocab_terms_count: vocabEntries.length,
      session_practiced: sessionPracticed,
      session_correct: sessionCorrect,
      session_accuracy_pct: sessionAccuracyPct
    },
    by_test: byTestStats,
    by_module: byModuleStats,
    practiced_questions: practicedRows,
    error_logs: errorLogs,
    vocab_entries: vocabEntries
  };
}

function buildConsolidatedWorkbookAoa(exportData) {
  const st = exportData.student || {};
  const ov = exportData.overall || {};

  // ---- Sheet 1: Hieu_Suat_Lam_Bai ----
  const perfAoa = [
    ["BÁO CÁO TỔNG HỢP THỰC HÀNH DIGITAL SAT BLUEBOOK (SOCRATIC)"],
    ["Thông tin học sinh & Hiệu suất làm bài • Phản hồi đa tầng • Sổ tay Thử sai & Từ vựng Socratic"],
    [],
    ["1. THÔNG TIN HỌC SINH & PHIÊN XUẤT BÁO CÁO"],
    ["Họ và tên học sinh", st.name || "Hoc_Sinh"],
    ["Email học sinh", st.email || "Chưa cung cấp"],
    ["Mục tiêu điểm SAT", st.target || "1400+"],
    ["Nguồn tài liệu / Bộ đề đã thực hành", st.sources_summary || "Chưa có dữ liệu"],
    ["Thời gian xuất báo cáo", exportData.generated_at || new Date().toLocaleString("vi-VN")],
    ["Giáo viên hướng dẫn", "Mike Pham Bá Hong Son • mikepham358@gmail.com"],
    [],
    ["2. HIỆU SUẤT LÀM BÀI TỔNG HỢP"],
    ["Chỉ số hiệu suất", "Giá trị", "Diễn giải / Ghi chú"],
    ["Tổng số câu đã thực hành", ov.total_practiced || 0, "Tổng số câu đã có ít nhất 1 lần chọn đáp án xuyên suốt các bộ đề"],
    ["Số câu hoàn thành đúng", ov.total_correct || 0, "Trả lời chính xác ở Lần 1, Lần 2 hoặc Lần 3"],
    ["Chưa hoàn thành / Sai cả 3 lần", ov.total_unfinished_or_missed || 0, "Cần ôn lại gợi ý đa tầng và ghi chú Sổ thử sai"],
    ["Tỷ lệ chính xác (Đúng / Đã làm)", `${ov.accuracy_pct || 0}%`, "Tỷ lệ số câu hoàn thành đúng trên tổng số câu đã thực hành"],
    ["Hiệu suất Socratic (Có trọng số)", `${ov.weighted_pct || 0}%`, "Trọng số Socratic: Đúng Lần 1 = 100%, Lần 2 = 66.7%, Lần 3 = 33.3%"],
    ["Đúng ngay Lần 1 (L1 - 100%)", ov.l1_correct || 0, "Làm đúng độc lập không cần mở gợi ý"],
    ["Đúng ở Lần 2 (L2 - 66.7%)", ov.l2_correct || 0, "Điều chỉnh đúng sau Phản hồi Tầng 1"],
    ["Đúng ở Lần 3 (L3 - 33.3%)", ov.l3_correct || 0, "Hoàn thành sau Phản hồi Tầng 2"],
    ["Tổng ghi chép Sổ tay Thử sai Socratic", ov.error_logs_count || 0, "Số thẻ phân tích bẫy SAT & bài học đã lưu"],
    ["Số mục Từ vựng Socratic đã ghi", ov.vocab_terms_count || 0, `${ov.vocab_notes_count || 0} thẻ ghi chép có từ mới / thuật ngữ`],
    ["Phiên học hiện tại (Bộ đếm ARR)", `${ov.session_correct || 0}/${ov.session_practiced || 0} câu (${ov.session_accuracy_pct || 0}%)`, "Thống kê xuyên suốt phiên học hiện tại (khi chuyển đổi giữa các bộ đề)"]
  ];

  perfAoa.push([]);
  perfAoa.push(["3. HIỆU SUẤT THEO TỪNG NGUỒN TÀI LIỆU / BỘ ĐỀ"]);
  perfAoa.push([
    "Nguồn tài liệu / Bộ đề", "Đã thực hành", "Số câu đúng", "Chưa đúng / Chờ xử lý",
    "L1 (100%)", "L2 (66.7%)", "L3 (33.3%)", "Tỷ lệ đúng (%)", "Hiệu suất Socratic (%)"
  ]);
  const byTest = exportData.by_test || [];
  if (byTest.length === 0) {
    perfAoa.push(["Chưa có câu hỏi nào được thực hành", 0, 0, 0, 0, 0, 0, "0%", "0%"]);
  } else {
    byTest.forEach(t => {
      perfAoa.push([
        t.test_short,
        t.practiced,
        t.correct,
        t.unfinished_or_missed,
        t.l1,
        t.l2,
        t.l3,
        `${t.accuracy_pct}%`,
        `${t.weighted_pct}%`
      ]);
    });
    perfAoa.push([
      "TỔNG CỘNG TẤT CẢ BỘ ĐỀ",
      ov.total_practiced || 0,
      ov.total_correct || 0,
      ov.total_unfinished_or_missed || 0,
      ov.l1_correct || 0,
      ov.l2_correct || 0,
      ov.l3_correct || 0,
      `${ov.accuracy_pct || 0}%`,
      `${ov.weighted_pct || 0}%`
    ]);
  }

  perfAoa.push([]);
  perfAoa.push(["4. CHI TIẾT HIỆU SUẤT THEO MODULE / CHƯƠNG / CHUYÊN ĐỀ"]);
  perfAoa.push([
    "Nguồn tài liệu", "Module / Chương / Chuyên đề", "Đã thực hành", "Số câu đúng",
    "Chưa đúng", "L1", "L2", "L3", "Tỷ lệ đúng (%)"
  ]);
  const byMod = exportData.by_module || [];
  if (byMod.length === 0) {
    perfAoa.push(["Chưa có dữ liệu module / chương", "", 0, 0, 0, 0, 0, 0, "0%"]);
  } else {
    byMod.forEach(m => {
      perfAoa.push([
        m.test_short,
        m.module_title,
        m.practiced,
        m.correct,
        m.unfinished_or_missed,
        m.l1,
        m.l2,
        m.l3,
        `${m.accuracy_pct}%`
      ]);
    });
  }

  // ---- Sheet 2: Cau_Hoi_Da_Thuc_Hanh ----
  const qHeaders = [
    "STT",
    "Nguồn tài liệu / Bộ đề",
    "Module / Chương",
    "Mã câu",
    "Chủ đề / Kỹ năng",
    "Trang (PDF / Sách)",
    "Độ khó",
    "Nội dung câu hỏi & Phương án",
    "Lần thử 1",
    "Lần thử 2",
    "Lần thử 3",
    "Đáp án đúng",
    "Kết quả & Mức đạt",
    "Hiệu suất (%)",
    "Phản hồi Tầng 1 (Định hướng tư duy)",
    "Phản hồi Tầng 2 (Manh mối cấu trúc & Loại trừ)",
    "Phản hồi Tầng 3 (Chốt phương pháp & Lời giải chi tiết)",
    "Phản hồi Tầng 4 (Chiến thuật & Công thức cốt lõi)",
    "Ghi chú Sổ thử sai Socratic (nếu có)",
    "Thời gian thực hành"
  ];
  const qAoa = [
    [`DANH SÁCH CÂU HỎI ĐÃ THỰC HÀNH & PHẢN HỒI ĐA TẦNG — ${(st.name || "HỌC SINH").toUpperCase()}`],
    qHeaders
  ];
  const pQuestions = exportData.practiced_questions || [];
  if (pQuestions.length === 0) {
    qAoa.push([
      1, "", "", "", "", "", "",
      "Chưa có câu hỏi nào được thực hành. Hãy chọn đáp án trong bài luyện tập để hệ thống lưu lại câu hỏi và phản hồi đa tầng.",
      "", "", "", "", "", "", "", "", "", "", "", ""
    ]);
  } else {
    pQuestions.forEach(q => {
      qAoa.push([
        q.stt,
        q.test_short,
        q.module_title,
        q.q_label,
        q.topic,
        q.page_label,
        q.difficulty,
        q.question_content,
        q.attempt_1,
        q.attempt_2,
        q.attempt_3,
        q.correct_answer,
        q.status_label,
        `${q.efficiency_pct}%`,
        q.tier1_feedback,
        q.tier2_feedback,
        q.tier3_feedback,
        q.tier4_feedback,
        q.error_note_summary,
        q.practiced_at
      ]);
    });
  }

  // ---- Sheet 3: So_Tay_Thu_Sai_Socratic ----
  const errHeaders = [
    "STT",
    "Nguồn tài liệu / Bộ đề",
    "Mã câu",
    "Module / Chương",
    "Chủ đề / Kỹ năng",
    "Các lần chọn sai",
    "Đáp án đúng",
    "Nhóm bẫy SAT / Nguyên nhân gốc",
    "Phân tích nguyên nhân thử sai & Bài học rút ra",
    "Ghi chú tư duy cá nhân",
    "Từ mới & Thuật ngữ Socratic đã ghi",
    "Gợi ý Socratic tham chiếu (Tầng 1)",
    "Tình trạng xử lý",
    "Ngày ghi chép"
  ];
  const errAoa = [
    [`SỔ TAY THỬ SAI SOCRATIC & BÀI HỌC PHẢN TƯ — ${(st.name || "HỌC SINH").toUpperCase()}`],
    errHeaders
  ];
  const eLogs = exportData.error_logs || [];
  if (eLogs.length === 0) {
    errAoa.push([
      1, "", "", "", "", "", "", "",
      "Chưa có ghi chép nào trong Sổ tay Thử sai Socratic.",
      "", "", "", "", ""
    ]);
  } else {
    eLogs.forEach(e => {
      errAoa.push([
        e.stt,
        e.test_short,
        e.q_label,
        e.module,
        e.skill,
        e.wrong_attempts,
        e.correct_answer,
        e.root_cause,
        e.trap_detail,
        e.student_notes,
        e.vocabulary,
        e.socratic_analysis,
        e.status,
        e.date
      ]);
    });
  }

  // ---- Sheet 4: Tu_Vung_Socratic ----
  const vocabHeaders = [
    "STT",
    "Nguồn tài liệu / Bộ đề",
    "Mã câu liên quan",
    "Module / Chủ đề",
    "Từ mới / Thuật ngữ Socratic",
    "Nghĩa / Giải thích học sinh đã ghi",
    "Ngữ cảnh bẫy SAT & Ghi chú liên quan",
    "Ngày ghi chép"
  ];
  const vocabAoa = [
    [`TỪ VỰNG & THUẬT NGỮ SOCRATIC ĐÃ GHI CHÉP — ${(st.name || "HỌC SINH").toUpperCase()}`],
    vocabHeaders
  ];
  const vEntries = exportData.vocab_entries || [];
  if (vEntries.length === 0) {
    vocabAoa.push([
      1, "", "", "",
      "Chưa có từ vựng / thuật ngữ nào được ghi chép trong Sổ tay Socratic.",
      "", "", ""
    ]);
  } else {
    vEntries.forEach(v => {
      vocabAoa.push([
        v.stt,
        v.test_short,
        v.q_label,
        v.module_skill,
        v.term,
        v.meaning,
        v.context_note,
        v.date
      ]);
    });
  }

  return { perfAoa, qAoa, errAoa, vocabAoa };
}

// ================= CLIENT-SIDE CONSOLIDATED EXCEL GENERATOR =================
async function generateClientExcelBlob(studentName, exportData) {
  if (typeof XLSX === "undefined") return null;

  try {
    const data = exportData || await collectConsolidatedExportData(studentName);
    const { perfAoa, qAoa, errAoa, vocabAoa } = buildConsolidatedWorkbookAoa(data);

    const wb = XLSX.utils.book_new();

    const wsPerf = XLSX.utils.aoa_to_sheet(perfAoa);
    wsPerf["!cols"] = [
      { wch: 36 }, { wch: 34 }, { wch: 48 }, { wch: 20 },
      { wch: 12 }, { wch: 12 }, { wch: 12 }, { wch: 16 }, { wch: 20 }
    ];
    wsPerf["!merges"] = [
      { s: { r: 0, c: 0 }, e: { r: 0, c: 8 } },
      { s: { r: 1, c: 0 }, e: { r: 1, c: 8 } }
    ];
    XLSX.utils.book_append_sheet(wb, wsPerf, "Hieu_Suat_Lam_Bai");

    const wsQ = XLSX.utils.aoa_to_sheet(qAoa);
    wsQ["!cols"] = [
      { wch: 6 }, { wch: 24 }, { wch: 30 }, { wch: 14 }, { wch: 28 },
      { wch: 18 }, { wch: 12 }, { wch: 52 }, { wch: 10 }, { wch: 10 },
      { wch: 10 }, { wch: 12 }, { wch: 22 }, { wch: 13 }, { wch: 44 },
      { wch: 46 }, { wch: 54 }, { wch: 48 }, { wch: 40 }, { wch: 20 }
    ];
    wsQ["!merges"] = [{ s: { r: 0, c: 0 }, e: { r: 0, c: 19 } }];
    XLSX.utils.book_append_sheet(wb, wsQ, "Cau_Hoi_Da_Thuc_Hanh");

    const wsErr = XLSX.utils.aoa_to_sheet(errAoa);
    wsErr["!cols"] = [
      { wch: 6 }, { wch: 24 }, { wch: 14 }, { wch: 28 }, { wch: 26 },
      { wch: 16 }, { wch: 12 }, { wch: 32 }, { wch: 46 }, { wch: 36 },
      { wch: 36 }, { wch: 40 }, { wch: 18 }, { wch: 14 }
    ];
    wsErr["!merges"] = [{ s: { r: 0, c: 0 }, e: { r: 0, c: 13 } }];
    XLSX.utils.book_append_sheet(wb, wsErr, "So_Tay_Thu_Sai_Socratic");

    const wsVocab = XLSX.utils.aoa_to_sheet(vocabAoa);
    wsVocab["!cols"] = [
      { wch: 6 }, { wch: 24 }, { wch: 16 }, { wch: 30 },
      { wch: 28 }, { wch: 44 }, { wch: 42 }, { wch: 14 }
    ];
    wsVocab["!merges"] = [{ s: { r: 0, c: 0 }, e: { r: 0, c: 7 } }];
    XLSX.utils.book_append_sheet(wb, wsVocab, "Tu_Vung_Socratic");

    const wbout = XLSX.write(wb, { bookType: "xlsx", type: "array" });
    return new Blob([wbout], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
  } catch (e) {
    console.error("Client Excel generation failed:", e);
    return null;
  }
}

// ================= EXPORT CONSOLIDATED EXCEL =================
async function exportExcelPersonalized() {
  const resolvedName = (
    (App.studentState && App.studentState.student_name ? String(App.studentState.student_name).trim() : "") ||
    (DOM.inputStudentName ? DOM.inputStudentName.value.trim() : "") ||
    (DOM.homeInputName ? DOM.homeInputName.value.trim() : "") ||
    prompt("Nhập họ và tên của em để xuất file Excel tổng hợp:") ||
    "Hoc_Sinh"
  ).trim() || "Hoc_Sinh";

  App.studentState.student_name = resolvedName;
  if (DOM.inputStudentName) DOM.inputStudentName.value = resolvedName;
  if (DOM.homeInputName) DOM.homeInputName.value = resolvedName;
  if (DOM.headerStudentName) DOM.headerStudentName.textContent = resolvedName;
  saveLocalState();

  const btn = DOM.btnExportExcel;
  const textSpan = btn ? btn.querySelector(".tool-text") : null;
  const origLabel = textSpan ? textSpan.textContent : "";
  if (btn) btn.disabled = true;
  if (textSpan) textSpan.textContent = "Đang xuất...";

  try {
    const exportData = await collectConsolidatedExportData(resolvedName);
    const safeFileStudent = resolvedName.replace(/[^a-zA-Z0-9\u00C0-\u1EF9_-]+/g, "_").replace(/^_+|_+$/g, "") || "Hoc_Sinh";
    const dateStamp = (exportData.generated_date_iso || new Date().toISOString().slice(0, 10)).replace(/-/g, "");
    const downloadFilename = `SAT_Tong_Hop_Thuc_Hanh_${safeFileStudent}_${dateStamp}.xlsx`;

    const payload = {
      student_name: resolvedName,
      student_email: (App.studentState && App.studentState.student_email) || "",
      student_target: (App.studentState && App.studentState.student_target) || "1400+",
      attempts: App.studentState.attempts || {},
      error_logs: App.studentState.error_logs || [],
      export_data: exportData
    };

    let downloaded = false;
    try {
      const res = await fetch("/api/export-excel", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        const blob = await res.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = downloadFilename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        setTimeout(() => window.URL.revokeObjectURL(url), 1000);
        downloaded = true;
      }
    } catch (e) {}

    // Fallback to client-side SheetJS generation (for GitHub Pages static hosting)
    if (!downloaded) {
      const blob = await generateClientExcelBlob(resolvedName, exportData);
      if (blob) {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = downloadFilename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        setTimeout(() => window.URL.revokeObjectURL(url), 1000);
      } else {
        alert("Không thể tạo file Excel tổng hợp. Vui lòng tải lại trang.");
      }
    }
  } finally {
    if (btn) btn.disabled = false;
    if (textSpan && origLabel) textSpan.textContent = origLabel;
  }
}

// ================= SCRATCHPAD CANVAS & WHITEBOARD (TOUCH + TEXTBOX + DRAGGABLE) =================
function initScratchpad() {
  const drawer = DOM.scratchpadDrawer;
  const header = DOM.scratchpadHeader || drawer.querySelector(".scratchpad-header");
  const body = DOM.scratchpadBody || document.getElementById("scratchpad-body");
  const canvas = DOM.scratchpadCanvas;
  const textLayer = DOM.scratchpadTextLayer || document.getElementById("scratchpad-text-layer");
  if (!drawer || !canvas) return;

  const ctx = canvas.getContext("2d");
  let drawing = false;
  let currentColor = "#0f172a";
  let currentTool = "pen"; // "pen" | "text"

  // 1. Generic Touch & Mouse Dragging Helper
  function makeDraggable(element, dragHandle, boundaryContainer = null) {
    if (!element || !dragHandle) return;
    let isDragging = false;
    let startX = 0, startY = 0;
    let initialLeft = 0, initialTop = 0;

    function getPointerPos(e) {
      const touch = (e.touches && e.touches[0]) ? e.touches[0] : (e.changedTouches ? e.changedTouches[0] : e);
      return { x: touch.clientX, y: touch.clientY };
    }

    function onStart(e) {
      if (e.target.closest("button") || e.target.closest("input") || e.target.closest("textarea")) {
        return;
      }
      isDragging = true;
      element.classList.add("is-dragging");
      element.style.zIndex = "1002";

      const pointer = getPointerPos(e);
      startX = pointer.x;
      startY = pointer.y;

      const rect = element.getBoundingClientRect();
      if (boundaryContainer) {
        const bRect = boundaryContainer.getBoundingClientRect();
        initialLeft = rect.left - bRect.left;
        initialTop = rect.top - bRect.top;
      } else {
        initialLeft = rect.left;
        initialTop = rect.top;
        element.style.right = "auto";
        element.style.bottom = "auto";
        element.style.margin = "0";
      }

      element.style.left = `${initialLeft}px`;
      element.style.top = `${initialTop}px`;

      document.addEventListener("mousemove", onMove, { passive: false });
      document.addEventListener("mouseup", onEnd);
      document.addEventListener("touchmove", onMove, { passive: false });
      document.addEventListener("touchend", onEnd);
      document.addEventListener("touchcancel", onEnd);

      if (e.cancelable) e.preventDefault();
    }

    function onMove(e) {
      if (!isDragging) return;
      if (e.cancelable) e.preventDefault();

      const pointer = getPointerPos(e);
      const dx = pointer.x - startX;
      const dy = pointer.y - startY;

      let newLeft = initialLeft + dx;
      let newTop = initialTop + dy;

      if (boundaryContainer) {
        const bRect = boundaryContainer.getBoundingClientRect();
        const eRect = element.getBoundingClientRect();
        newLeft = Math.max(0, Math.min(newLeft, bRect.width - eRect.width));
        newTop = Math.max(0, Math.min(newTop, bRect.height - eRect.height));
      } else {
        const eRect = element.getBoundingClientRect();
        newLeft = Math.max(5, Math.min(newLeft, window.innerWidth - eRect.width - 5));
        newTop = Math.max(5, Math.min(newTop, window.innerHeight - eRect.height - 5));
      }

      element.style.left = `${newLeft}px`;
      element.style.top = `${newTop}px`;
    }

    function onEnd() {
      if (isDragging) {
        isDragging = false;
        element.classList.remove("is-dragging");
        document.removeEventListener("mousemove", onMove);
        document.removeEventListener("mouseup", onEnd);
        document.removeEventListener("touchmove", onMove);
        document.removeEventListener("touchend", onEnd);
        document.removeEventListener("touchcancel", onEnd);
      }
    }

    dragHandle.addEventListener("mousedown", onStart);
    dragHandle.addEventListener("touchstart", onStart, { passive: false });
  }

  // Make scratchpad drawer draggable across window
  if (header) {
    makeDraggable(drawer, header, null);
  }

  // Elevate scratchpad above other modals on click
  drawer.addEventListener("mousedown", () => {
    drawer.style.zIndex = "1002";
  });
  drawer.addEventListener("touchstart", () => {
    drawer.style.zIndex = "1002";
  }, { passive: true });

  // 2. Canvas Resizing with drawing preservation
  function resizeCanvas() {
    const parent = body || drawer;
    const w = parent.clientWidth;
    const h = parent.clientHeight;
    if (!w || !h) return;

    let backupCanvas = null;
    if (canvas.width > 0 && canvas.height > 0) {
      backupCanvas = document.createElement("canvas");
      backupCanvas.width = canvas.width;
      backupCanvas.height = canvas.height;
      const bCtx = backupCanvas.getContext("2d");
      bCtx.drawImage(canvas, 0, 0);
    }

    canvas.width = w;
    canvas.height = h;

    if (backupCanvas) {
      ctx.drawImage(backupCanvas, 0, 0, backupCanvas.width, backupCanvas.height, 0, 0, w, h);
    }
  }

  window.addEventListener("resize", resizeCanvas);
  setTimeout(resizeCanvas, 200);

  // 3. Coordinate Transformation (Mouse, Touch, iPad Apple Pencil)
  function getCanvasCoords(e) {
    const rect = canvas.getBoundingClientRect();
    let clientX = e.clientX;
    let clientY = e.clientY;

    if (e.touches && e.touches.length > 0) {
      clientX = e.touches[0].clientX;
      clientY = e.touches[0].clientY;
    } else if (e.changedTouches && e.changedTouches.length > 0) {
      clientX = e.changedTouches[0].clientX;
      clientY = e.changedTouches[0].clientY;
    }

    const scaleX = canvas.width / (rect.width || 1);
    const scaleY = canvas.height / (rect.height || 1);
    return {
      x: (clientX - rect.left) * scaleX,
      y: (clientY - rect.top) * scaleY
    };
  }

  // 4. Drawing Actions
  function startDraw(e) {
    if (currentTool !== "pen") return;
    drawing = true;
    const pos = getCanvasCoords(e);
    ctx.beginPath();
    ctx.moveTo(pos.x, pos.y);
    if (e.cancelable) e.preventDefault();
  }

  function doDraw(e) {
    if (!drawing || currentTool !== "pen") return;
    const pos = getCanvasCoords(e);
    ctx.strokeStyle = currentColor;
    ctx.lineWidth = 2.5;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.lineTo(pos.x, pos.y);
    ctx.stroke();
    if (e.cancelable) e.preventDefault();
  }

  function stopDraw() {
    if (drawing) {
      drawing = false;
      ctx.closePath();
    }
  }

  // Mouse Listeners
  canvas.addEventListener("mousedown", startDraw);
  window.addEventListener("mousemove", (e) => {
    if (drawing) doDraw(e);
  });
  window.addEventListener("mouseup", stopDraw);

  // Touch Listeners (iPad & Mobile with passive: false)
  canvas.addEventListener("touchstart", startDraw, { passive: false });
  canvas.addEventListener("touchmove", doDraw, { passive: false });
  canvas.addEventListener("touchend", stopDraw);
  canvas.addEventListener("touchcancel", stopDraw);

  // 5. Textbox Feature Implementation
  function createTextbox(x = null, y = null, initialText = "") {
    if (!textLayer || !body) return;
    const bRect = body.getBoundingClientRect();

    const posX = (x !== null && x !== undefined) ? x : Math.max(15, bRect.width / 2 - 110);
    const posY = (y !== null && y !== undefined) ? y : Math.max(15, bRect.height / 2 - 60);

    const box = document.createElement("div");
    box.className = "scratch-textbox active";
    box.style.borderColor = currentColor;
    box.style.left = `${Math.max(8, Math.min(posX, bRect.width - 210))}px`;
    box.style.top = `${Math.max(8, Math.min(posY, bRect.height - 110))}px`;

    box.innerHTML = `
      <div class="scratch-textbox-header" style="border-top: 3px solid ${currentColor};">
        <span class="scratch-tb-drag">⋮⋮ Ô gõ nháp</span>
        <button type="button" class="scratch-tb-del" title="Xóa ô này">✕</button>
      </div>
      <textarea class="scratch-tb-input" placeholder="Nhập văn bản nháp / công thức...">${initialText}</textarea>
    `;

    // Delete Button
    const btnDel = box.querySelector(".scratch-tb-del");
    btnDel.addEventListener("click", (e) => {
      e.stopPropagation();
      box.remove();
    });

    // Make textbox draggable inside scratchpad body
    const tbHeader = box.querySelector(".scratch-textbox-header");
    makeDraggable(box, tbHeader, body);

    // Textarea focus management
    const textarea = box.querySelector(".scratch-tb-input");
    textarea.addEventListener("focus", () => {
      document.querySelectorAll(".scratch-textbox").forEach(b => b.classList.remove("active"));
      box.classList.add("active");
    });

    textLayer.appendChild(box);
    setTimeout(() => textarea.focus(), 60);
    return box;
  }

  // Click on canvas while in Textbox mode to place a textbox
  function onCanvasTapForText(e) {
    if (currentTool !== "text") return;
    // Don't trigger if clicked on an existing textbox
    if (e.target.closest(".scratch-textbox")) return;

    const bRect = body.getBoundingClientRect();
    let clientX = e.clientX;
    let clientY = e.clientY;
    if (e.changedTouches && e.changedTouches.length > 0) {
      clientX = e.changedTouches[0].clientX;
      clientY = e.changedTouches[0].clientY;
    }
    const x = clientX - bRect.left - 20;
    const y = clientY - bRect.top - 15;
    createTextbox(x, y);
  }

  canvas.addEventListener("click", onCanvasTapForText);

  // 6. Tool Mode Switcher Controls
  if (DOM.btnScratchToolPen) {
    DOM.btnScratchToolPen.addEventListener("click", () => {
      currentTool = "pen";
      DOM.btnScratchToolPen.classList.add("active");
      if (DOM.btnScratchToolText) DOM.btnScratchToolText.classList.remove("active");
      if (body) body.classList.remove("text-mode");
    });
  }

  if (DOM.btnScratchToolText) {
    DOM.btnScratchToolText.addEventListener("click", () => {
      currentTool = "text";
      DOM.btnScratchToolText.classList.add("active");
      if (DOM.btnScratchToolPen) DOM.btnScratchToolPen.classList.remove("active");
      if (body) body.classList.add("text-mode");
    });
  }

  if (DOM.btnScratchAddTextbox) {
    DOM.btnScratchAddTextbox.addEventListener("click", () => {
      createTextbox();
    });
  }

  // 7. Color Buttons
  DOM.colorButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      DOM.colorButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentColor = btn.dataset.color;

      // Update active textbox color accent
      const activeTb = document.querySelector(".scratch-textbox.active");
      if (activeTb) {
        activeTb.style.borderColor = currentColor;
        const tbHdr = activeTb.querySelector(".scratch-textbox-header");
        if (tbHdr) tbHdr.style.borderTop = `3px solid ${currentColor}`;
      }
    });
  });

  // 8. Clear & Close Actions
  if (DOM.btnScratchClear) {
    DOM.btnScratchClear.addEventListener("click", () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (textLayer) {
        textLayer.innerHTML = "";
      }
    });
  }

  if (DOM.btnScratchClose) {
    DOM.btnScratchClose.addEventListener("click", () => {
      drawer.classList.add("hidden");
    });
  }

  if (DOM.btnToggleScratchpad) {
    DOM.btnToggleScratchpad.addEventListener("click", () => {
      drawer.classList.toggle("hidden");
      if (!drawer.classList.contains("hidden")) {
        drawer.style.zIndex = "1002";
        setTimeout(resizeCanvas, 50);
      }
    });
  }
}

// ================= SPLIT RESIZER & THEME (TOUCH + MOUSE OPTIMIZED) =================
function initSplitResizer() {
  const savedWidth = localStorage.getItem("bluebook_split_width") || "50%";
  if (DOM.panePdf && window.innerWidth > 900) {
    DOM.panePdf.style.width = savedWidth;
  }

  let isDragging = false;

  function onDragStart(e) {
    // Only drag on desktop/tablet landscape (not tablet portrait single-pane mode)
    if (window.innerWidth <= 900 || (window.innerWidth <= 1024 && window.innerHeight > window.innerWidth)) {
      return;
    }
    isDragging = true;
    if (DOM.splitDivider) DOM.splitDivider.classList.add("dragging");
    document.body.classList.add("resizing-split");
    if (e.cancelable) e.preventDefault();
  }

  function onDragMove(e) {
    if (!isDragging) return;
    if (e.cancelable) e.preventDefault();

    const clientX = (e.touches && e.touches[0]) ? e.touches[0].clientX : e.clientX;
    const containerRect = DOM.splitContainer.getBoundingClientRect();
    const newWidth = clientX - containerRect.left;
    const totalWidth = containerRect.width;

    if (newWidth >= 280 && newWidth <= totalWidth - 320) {
      const pct = (newWidth / totalWidth * 100).toFixed(1) + "%";
      DOM.panePdf.style.width = pct;
      localStorage.setItem("bluebook_split_width", pct);
    }
  }

  function onDragEnd() {
    if (isDragging) {
      isDragging = false;
      if (DOM.splitDivider) DOM.splitDivider.classList.remove("dragging");
      document.body.classList.remove("resizing-split");
    }
  }

  if (DOM.splitDivider) {
    DOM.splitDivider.addEventListener("mousedown", onDragStart);
    DOM.splitDivider.addEventListener("touchstart", onDragStart, { passive: false });
  }

  window.addEventListener("mousemove", onDragMove);
  window.addEventListener("touchmove", onDragMove, { passive: false });

  window.addEventListener("mouseup", onDragEnd);
  window.addEventListener("touchend", onDragEnd);
  window.addEventListener("touchcancel", onDragEnd);
}

// ================= TRỤ CỘT 4: TABLET & IPAD TOUCH CONTROLS =================
function setTabletPane(paneType) {
  if (paneType === "pdf") {
    document.body.classList.add("tablet-show-pdf");
    document.body.classList.remove("tablet-show-content");
    if (DOM.btnTabPanePdf) DOM.btnTabPanePdf.classList.add("active");
    if (DOM.btnTabPaneContent) DOM.btnTabPaneContent.classList.remove("active");
  } else {
    document.body.classList.add("tablet-show-content");
    document.body.classList.remove("tablet-show-pdf");
    if (DOM.btnTabPaneContent) DOM.btnTabPaneContent.classList.add("active");
    if (DOM.btnTabPanePdf) DOM.btnTabPanePdf.classList.remove("active");
  }
}

function initTabletSupport() {
  setTabletPane("content");

  if (DOM.btnTabPanePdf) {
    DOM.btnTabPanePdf.addEventListener("click", () => setTabletPane("pdf"));
  }
  if (DOM.btnTabPaneContent) {
    DOM.btnTabPaneContent.addEventListener("click", () => setTabletPane("content"));
  }
  if (DOM.btnTabletToQuestion) {
    DOM.btnTabletToQuestion.addEventListener("click", () => setTabletPane("content"));
  }

  // When tapping the PDF sync page badge in content view, jump to PDF if on tablet portrait
  if (DOM.pdfPageBadge) {
    DOM.pdfPageBadge.addEventListener("click", () => {
      if (window.innerWidth <= 900 || (window.innerWidth <= 1024 && window.innerHeight > window.innerWidth)) {
        setTabletPane("pdf");
      }
    });
  }
}

// ================= TRỤ CỘT 5: ZEN FOCUS MODE CONTROLS =================
function toggleZenMode(forcedState) {
  const isZen = (typeof forcedState === "boolean") ? forcedState : !document.body.classList.contains("zen-mode");
  document.body.classList.toggle("zen-mode", isZen);
  if (DOM.btnToggleZen) {
    DOM.btnToggleZen.classList.toggle("active", isZen);
  }
  if (DOM.zenFloatingPill) {
    DOM.zenFloatingPill.classList.toggle("hidden", !isZen);
  }
  localStorage.setItem("bluebook_zen_mode", isZen ? "active" : "inactive");
}

function initZenMode() {
  const savedZen = localStorage.getItem("bluebook_zen_mode");
  if (savedZen === "active" && document.body.classList.contains("in-practice")) {
    toggleZenMode(true);
  }

  if (DOM.btnToggleZen) {
    DOM.btnToggleZen.addEventListener("click", () => toggleZenMode());
  }
  if (DOM.btnExitZen) {
    DOM.btnExitZen.addEventListener("click", () => toggleZenMode(false));
  }
  if (DOM.zenBtnCalc && DOM.btnOpenCalc) {
    DOM.zenBtnCalc.addEventListener("click", () => DOM.btnOpenCalc.click());
  }
}

// ================= DRAGGABLE DESMOS CALCULATOR =================
function initDraggableDesmos() {
  const modal = DOM.modalCalculator;
  const header = DOM.calcModalHeader || document.getElementById("calc-modal-header");
  if (!modal || !header) return;

  let isDragging = false;
  let startX = 0;
  let startY = 0;
  let initialLeft = 0;
  let initialTop = 0;
  const iframe = modal.querySelector("iframe");

  // Keep modal elevated above other floating elements when clicked
  modal.addEventListener("mousedown", () => {
    modal.style.zIndex = "1000";
  });

  function onPointerDown(e) {
    // Ignore clicks on close button or interactive elements
    if (e.target.closest("#btn-close-calculator") || e.target.closest("button") || e.target.closest("a")) {
      return;
    }

    isDragging = true;
    modal.classList.add("is-dragging");
    modal.style.zIndex = "1000";

    // Disable iframe pointer events during drag so mousemove events are not swallowed
    if (iframe) {
      iframe.style.pointerEvents = "none";
    }

    const clientX = (e.touches && e.touches[0]) ? e.touches[0].clientX : e.clientX;
    const clientY = (e.touches && e.touches[0]) ? e.touches[0].clientY : e.clientY;

    startX = clientX;
    startY = clientY;

    const rect = modal.getBoundingClientRect();
    initialLeft = rect.left;
    initialTop = rect.top;

    // Convert fixed right-anchored positioning to explicit top/left coordinates
    modal.style.right = "auto";
    modal.style.bottom = "auto";
    modal.style.left = `${initialLeft}px`;
    modal.style.top = `${initialTop}px`;
    modal.style.margin = "0";

    document.addEventListener("mousemove", onPointerMove, { passive: false });
    document.addEventListener("mouseup", onPointerUp);
    document.addEventListener("touchmove", onPointerMove, { passive: false });
    document.addEventListener("touchend", onPointerUp);
    document.addEventListener("touchcancel", onPointerUp);

    e.preventDefault();
  }

  function onPointerMove(e) {
    if (!isDragging) return;

    if (e.cancelable) {
      e.preventDefault();
    }

    const clientX = (e.touches && e.touches[0]) ? e.touches[0].clientX : e.clientX;
    const clientY = (e.touches && e.touches[0]) ? e.touches[0].clientY : e.clientY;

    const deltaX = clientX - startX;
    const deltaY = clientY - startY;

    let newLeft = initialLeft + deltaX;
    let newTop = initialTop + deltaY;

    // Viewport constraints: allow flexible movement anywhere on screen,
    // while keeping at least 80px of width and the 44px header visible
    const modalWidth = modal.offsetWidth;
    const winWidth = window.innerWidth;
    const winHeight = window.innerHeight;

    const minLeft = -(modalWidth - 80);
    const maxLeft = winWidth - 80;
    const minTop = 0;
    const maxTop = winHeight - 44;

    newLeft = Math.max(minLeft, Math.min(newLeft, maxLeft));
    newTop = Math.max(minTop, Math.min(newTop, maxTop));

    modal.style.left = `${newLeft}px`;
    modal.style.top = `${newTop}px`;
  }

  function onPointerUp() {
    if (!isDragging) return;
    isDragging = false;
    modal.classList.remove("is-dragging");

    if (iframe) {
      iframe.style.pointerEvents = "auto";
    }

    document.removeEventListener("mousemove", onPointerMove);
    document.removeEventListener("mouseup", onPointerUp);
    document.removeEventListener("touchmove", onPointerMove);
    document.removeEventListener("touchend", onPointerUp);
    document.removeEventListener("touchcancel", onPointerUp);
  }

  header.addEventListener("mousedown", onPointerDown);
  header.addEventListener("touchstart", onPointerDown, { passive: false });

  // Double click header to reset back to default top-right position
  header.addEventListener("dblclick", (e) => {
    if (e.target.closest("button")) return;
    modal.style.left = "auto";
    modal.style.top = "80px";
    modal.style.right = "40px";
  });
}

// ================= SMART FEEDBACK & GITHUB LOG SYSTEM =================
async function loadFeedbacksList() {
  try {
    const res = await fetch("/api/feedbacks");
    if (res.ok) {
      App.feedbacks = await res.json();
    } else {
      throw new Error("fallback to static");
    }
  } catch (e) {
    try {
      const resStatic = await fetch("feedback.json?t=" + Date.now());
      if (resStatic.ok) {
        App.feedbacks = await resStatic.json();
      }
    } catch (e2) {}
  }

  // Also merge any offline feedbacks stored in localStorage
  try {
    const localFbs = JSON.parse(localStorage.getItem("sat_feedback_local_queue") || "[]");
    if (Array.isArray(localFbs) && localFbs.length > 0) {
      if (!App.feedbacks) App.feedbacks = [];
      const existingIds = new Set(App.feedbacks.map(x => x.id));
      for (const item of localFbs) {
        if (!existingIds.has(item.id)) {
          App.feedbacks.unshift(item);
        }
      }
    }
  } catch (e3) {}

  updateFeedbackBadge();
}

function updateFeedbackBadge() {
  if (DOM.fbHistoryCount) {
    DOM.fbHistoryCount.textContent = App.feedbacks ? App.feedbacks.length : 0;
  }
}

function openFeedbackModal(prefilledContext) {
  pauseTimer();

  // Detect current context
  let contextLabel = "Trang chủ / Hệ thống chung";
  const isPractice = DOM.viewPractice && !DOM.viewPractice.classList.contains("hidden");

  if (prefilledContext) {
    contextLabel = prefilledContext;
  } else if (isPractice && App.currentQuestion) {
    const q = App.currentQuestion;
    const qIndex = App.currentIndex + 1;
    const modTitle = DOM.selectModule ? DOM.selectModule.options[DOM.selectModule.selectedIndex].text.split("(")[0].trim() : App.activeModuleCode;
    contextLabel = `${modTitle} • Câu ${qIndex} (Mã #${q.id}) ${q.pdf_page ? `• Trang ${q.pdf_page}` : ""}`;
  }

  App.currentFeedbackContext = contextLabel;

  if (DOM.fbDetectedContext) {
    DOM.fbDetectedContext.textContent = contextLabel;
  }

  // Pre-fill user details if available
  if (DOM.inputFbName && !DOM.inputFbName.value) {
    DOM.inputFbName.value = App.studentState.student_name || "";
  }
  if (DOM.inputFbEmail && !DOM.inputFbEmail.value) {
    DOM.inputFbEmail.value = App.studentState.student_email || "";
  }

  // Pre-select category based on context
  if (DOM.selectFbCategory) {
    if (isPractice) {
      DOM.selectFbCategory.value = "🎯 Báo lỗi câu hỏi / Đáp án";
    } else {
      DOM.selectFbCategory.value = "📝 Góp ý chung & Đánh giá";
    }
  }

  // Reset form state & success banner
  if (DOM.formSubmitFeedback) {
    DOM.formSubmitFeedback.classList.remove("hidden");
    DOM.formSubmitFeedback.reset();
    if (DOM.inputFbName) DOM.inputFbName.value = App.studentState.student_name || "";
    if (DOM.inputFbEmail) DOM.inputFbEmail.value = App.studentState.student_email || "";
    if (DOM.selectFbCategory) DOM.selectFbCategory.value = isPractice ? "🎯 Báo lỗi câu hỏi / Đáp án" : "📝 Góp ý chung & Đánh giá";
  }

  if (DOM.fbSuccessBanner) DOM.fbSuccessBanner.classList.add("hidden");
  if (DOM.groupCustomContext) DOM.groupCustomContext.classList.add("hidden");

  // Show Tab 1 by default
  switchFeedbackTab("new");

  if (DOM.modalFeedback) {
    DOM.modalFeedback.classList.remove("hidden");
  }

  loadFeedbacksList();
}

function closeFeedbackModal() {
  if (DOM.modalFeedback) {
    DOM.modalFeedback.classList.add("hidden");
  }
  syncTimerState();
}

function switchFeedbackTab(tabName) {
  if (tabName === "new") {
    if (DOM.tabBtnFbNew) DOM.tabBtnFbNew.classList.add("active");
    if (DOM.tabBtnFbHistory) DOM.tabBtnFbHistory.classList.remove("active");
    if (DOM.fbTabContentNew) DOM.fbTabContentNew.classList.remove("hidden");
    if (DOM.fbTabContentHistory) DOM.fbTabContentHistory.classList.add("hidden");
  } else {
    if (DOM.tabBtnFbNew) DOM.tabBtnFbNew.classList.remove("active");
    if (DOM.tabBtnFbHistory) DOM.tabBtnFbHistory.classList.add("active");
    if (DOM.fbTabContentNew) DOM.fbTabContentNew.classList.add("hidden");
    if (DOM.fbTabContentHistory) DOM.fbTabContentHistory.classList.remove("hidden");
    renderFeedbackHistoryList();
  }
}

function renderFeedbackHistoryList() {
  if (!DOM.fbHistoryList) return;
  const list = App.feedbacks || [];

  if (list.length === 0) {
    DOM.fbHistoryList.innerHTML = `
      <div style="text-align: center; padding: 32px 16px; color: #64748b;">
        <div style="font-size: 32px; margin-bottom: 8px;">📭</div>
        <div style="font-weight: 600;">Chưa có phản hồi nào được ghi nhận</div>
        <div style="font-size: 12.5px; margin-top: 4px;">Em có thể là người đầu tiên gửi đóng góp ý kiến qua tab bên cạnh!</div>
      </div>
    `;
    return;
  }

  // Render in reverse chronological order (newest first)
  const sorted = [...list].reverse();
  DOM.fbHistoryList.innerHTML = sorted.map((item, idx) => {
    const isResolved = item.status && (item.status.includes("Đã") || item.status.includes("giải quyết") || item.status.includes("triệt tiêu"));
    const statusClass = isResolved ? "fb-status-resolved" : "fb-status-open";
    
    return `
      <div class="fb-card-item">
        <div class="fb-card-top">
          <div class="fb-card-meta">
            <span class="fb-card-id">${escapeHtml(item.id || `FB-${idx+1}`)}</span>
            <span class="fb-card-cat">${escapeHtml(item.category || "Góp ý")}</span>
            <span class="fb-card-date">${escapeHtml(item.date_str || "")}</span>
          </div>
          <span class="fb-card-status ${statusClass}">${escapeHtml(item.status || "Đang xử lý")}</span>
        </div>
        <div class="fb-card-context">📍 ${escapeHtml(item.context_label || item.question_label || "Toàn hệ thống")}</div>
        <div class="fb-card-content">${escapeHtml(item.content || "")}</div>
        <div class="fb-card-footer">
          <span>Người gửi: <strong>${escapeHtml(item.student_name || "Học sinh")}</strong> ${item.student_email ? `(${escapeHtml(item.student_email)})` : ""}</span>
          <span>Ưu tiên: <strong>${escapeHtml(item.priority || "Bình thường")}</strong></span>
        </div>
      </div>
    `;
  }).join("");
}

async function handleFeedbackSubmit(e) {
  e.preventDefault();
  const content = DOM.inputFbContent ? DOM.inputFbContent.value.trim() : "";
  if (!content) {
    alert("Vui lòng nhập nội dung chi tiết phản hồi của em!");
    return;
  }

  const studentName = (DOM.inputFbName ? DOM.inputFbName.value.trim() : "") || App.studentState.student_name || "Ẩn danh";
  const studentEmail = (DOM.inputFbEmail ? DOM.inputFbEmail.value.trim() : "") || App.studentState.student_email || "";
  const category = DOM.selectFbCategory ? DOM.selectFbCategory.value : "🎯 Báo lỗi câu hỏi / Đáp án";
  const priority = DOM.selectFbPriority ? DOM.selectFbPriority.value : "🟢 Bình thường";

  let contextLabel = App.currentFeedbackContext || "Hệ thống chung";
  if (DOM.groupCustomContext && !DOM.groupCustomContext.classList.contains("hidden")) {
    const customMod = DOM.selectFbCustomModule.value;
    if (customMod !== "CURRENT") {
      contextLabel = DOM.selectFbCustomModule.options[DOM.selectFbCustomModule.selectedIndex].text;
    }
  }

  const payload = {
    student_name: studentName,
    student_email: studentEmail,
    category: category,
    priority: priority,
    context_label: contextLabel,
    content: content
  };

  if (DOM.btnSubmitFeedback) {
    DOM.btnSubmitFeedback.disabled = true;
    DOM.btnSubmitFeedback.innerHTML = `<span>⏳ Đang ghi nhận & đồng bộ lên GitHub...</span>`;
  }

  let serverSuccess = false;
  let serverResponse = null;

  try {
    const res = await fetch("/api/feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      serverResponse = await res.json();
      if (serverResponse.success) {
        serverSuccess = true;
      }
    }
  } catch (err) {
    // Expected on static hosting like GitHub Pages
  }

  if (serverSuccess && serverResponse && serverResponse.item) {
    if (!App.feedbacks) App.feedbacks = [];
    App.feedbacks.push(serverResponse.item);
    updateFeedbackBadge();
    showFeedbackSuccess(serverResponse.item.id, true, payload);
  } else {
    // Client-side fallback for GitHub Pages
    const now = new Date();
    const localId = `FB-${now.getFullYear()}${(now.getMonth()+1).toString().padStart(2, '0')}${now.getDate().toString().padStart(2, '0')}-${Date.now().toString().slice(-3)}`;
    const localItem = {
      id: localId,
      timestamp: now.toISOString(),
      date_str: `${now.getDate().toString().padStart(2, '0')}/${(now.getMonth()+1).toString().padStart(2, '0')}/${now.getFullYear()} ${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`,
      student_name: studentName,
      student_email: studentEmail,
      category: category,
      priority: priority,
      context_label: contextLabel,
      content: content,
      status: "⏳ Đã ghi nhận (Local Queue)"
    };

    try {
      const localQueue = JSON.parse(localStorage.getItem("sat_feedback_local_queue") || "[]");
      localQueue.push(localItem);
      localStorage.setItem("sat_feedback_local_queue", JSON.stringify(localQueue));
    } catch (e) {}

    if (!App.feedbacks) App.feedbacks = [];
    App.feedbacks.push(localItem);
    updateFeedbackBadge();
    showFeedbackSuccess(localId, false, payload);
  }

  if (DOM.btnSubmitFeedback) {
    DOM.btnSubmitFeedback.disabled = false;
    DOM.btnSubmitFeedback.innerHTML = `<span>🚀 Gửi Phản Hồi & Đồng Bộ Lên GitHub</span>`;
  }
}

function showFeedbackSuccess(fbId, isServerSynced, rawPayload) {
  if (DOM.formSubmitFeedback) DOM.formSubmitFeedback.classList.add("hidden");
  if (DOM.fbSuccessBanner) {
    DOM.fbSuccessBanner.classList.remove("hidden");
    if (DOM.fbSuccessMsg) {
      const teacherEmail = "mikepham358@gmail.com";
      const mailSubject = encodeURIComponent(`[SAT Bluebook Feedback - ${fbId}] ${rawPayload.category} - ${rawPayload.context_label}`);
      const mailBody = encodeURIComponent(
`Kính gửi Thầy Mike Pham Bá Hong Son,

Em gửi phản hồi / báo lỗi từ ứng dụng luyện thi Digital SAT Bluebook:

- Mã phản hồi: ${fbId}
- Học sinh gửi: ${rawPayload.student_name} (${rawPayload.student_email || "Chưa cung cấp"})
- Phân loại: ${rawPayload.category}
- Mức độ ưu tiên: ${rawPayload.priority}
- Vị trí / Ngữ cảnh: ${rawPayload.context_label}
- Thời gian: ${new Date().toLocaleString("vi-VN")}

--------------------------------------------------
NỘI DUNG PHẢN HỒI / BÁO LỖI:
${rawPayload.content}
--------------------------------------------------

Em cảm ơn Thầy!`
      );
      const mailtoUrl = `mailto:${teacherEmail}?subject=${mailSubject}&body=${mailBody}`;

      const ghIssueTitle = encodeURIComponent(`[Feedback ${rawPayload.category}] ${rawPayload.context_label}`);
      const ghIssueBody = encodeURIComponent(
`### 💬 Phản hồi từ học sinh Vinschool SAT Team\n\n` +
`- **Mã phản hồi:** \`${fbId}\`\n` +
`- **Người gửi:** ${rawPayload.student_name} (${rawPayload.student_email || "Chưa cung cấp"})\n` +
`- **Phân loại:** ${rawPayload.category}\n` +
`- **Mức độ:** ${rawPayload.priority}\n` +
`- **Vị trí / Ngữ cảnh:** ${rawPayload.context_label}\n` +
`- **Thời gian:** ${new Date().toLocaleString("vi-VN")}\n\n` +
`---\n### 📝 Nội dung phản hồi:\n${rawPayload.content}\n\n` +
`*(Gửi từ Digital SAT Bluebook Practice App)*\n\ncc: @mikepham358`
      );
      const ghIssueUrl = `https://github.com/mikepham358/vinschool-sat-team/issues/new?title=${ghIssueTitle}&body=${ghIssueBody}&assignees=mikepham358&labels=student-feedback`;

      // On GitHub Pages: auto open GitHub Issue tab so user doesn't miss posting to GitHub
      if (!isServerSynced) {
        try {
          window.open(ghIssueUrl, "_blank");
        } catch (errOpen) {}
      }

      DOM.fbSuccessMsg.innerHTML = `
        <div style="font-size: 14px; line-height: 1.6; color: #1e293b;">
          🎉 Phản hồi mã <strong>${escapeHtml(fbId)}</strong> đã được ghi nhận thành công!<br>
          ${isServerSynced ? "Dữ liệu đã tự động commit & push lên kho lưu trữ GitHub (<code>FEEDBACK_LOG.md</code>)." : "Dữ liệu đã được chuẩn bị đầy đủ sẵn sàng đồng bộ lên GitHub."}
        </div>
        ${!isServerSynced ? `
        <div style="margin-top: 14px; padding: 12px 14px; background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: 10px; font-size: 13.5px; color: #1e40af;">
          🚀 <strong>Hệ thống đã tự động mở trang tạo Issue trên GitHub cho em!</strong><br>
          Em chỉ cần kiểm tra nội dung và nhấn nút xanh <strong>"Submit new issue"</strong> trên GitHub để phản hồi tự động cập nhật vào <code>FEEDBACK_LOG.md</code> và gửi email thông báo cho Thầy Mike.
        </div>
        ` : ""}
        <div style="margin-top: 14px; padding: 12px 14px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; font-size: 13px; color: #475569;">
          📬 <strong>Kênh liên hệ trực tiếp:</strong> Em cũng có thể gửi email thẳng tới <strong>${teacherEmail}</strong> qua nút bấm bên dưới:
        </div>
        <div style="margin-top: 14px; display: flex; flex-wrap: wrap; gap: 10px;">
          <a href="${mailtoUrl}" style="display: inline-flex; align-items: center; gap: 6px; padding: 9px 18px; background: #ea4335; color: #ffffff; text-decoration: none; border-radius: 20px; font-weight: 700; font-size: 13px; box-shadow: 0 2px 6px rgba(234, 67, 53, 0.25);">
            📧 Gửi Email Trực Tiếp Cho Thầy (mikepham358@gmail.com) ↗
          </a>
          <a href="${ghIssueUrl}" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 6px; padding: 9px 18px; background: #0969da; color: #ffffff; text-decoration: none; border-radius: 20px; font-weight: 700; font-size: 13px; box-shadow: 0 2px 6px rgba(9, 105, 218, 0.25);">
            🐙 Mở Lại Trang GitHub Issue (Gán Thầy @mikepham358) ↗
          </a>
        </div>
      `;
    }
  }
}

// ================= EVENT LISTENERS =================
function setupEventListeners() {
  // Module Change
  DOM.selectModule.addEventListener("change", (e) => {
    if (!checkCanNavigate()) {
      DOM.selectModule.value = App.activeModuleCode;
      return;
    }
    App.activeModuleCode = e.target.value;
    App.studentState.active_module = e.target.value;
    saveLocalState();
    setupModuleQuestions();
    startModuleTimer();
  });

  // Student Name input
  DOM.inputStudentName.addEventListener("input", (e) => {
    App.studentState.student_name = e.target.value;
    saveLocalState();
  });

  // Mark for review toggle
  DOM.chkMarkReview.addEventListener("change", (e) => {
    const q = App.currentQuestion;
    if (!q) return;
    const qState = App.studentState.attempts[q.id] || { attempts: [], status: "unanswered", efficiency: 0.0 };
    qState.marked = e.target.checked;
    App.studentState.attempts[q.id] = qState;
    saveLocalState();
    DOM.markReviewLabel.classList.toggle("marked", e.target.checked);
  });

  // Eliminator mode toggle [ABC] (Optional top toggle fallback)
  if (DOM.btnToggleEliminator) {
    DOM.btnToggleEliminator.addEventListener("click", () => {
      App.eliminatorMode = !App.eliminatorMode;
      DOM.btnToggleEliminator.classList.toggle("active", App.eliminatorMode);
      document.body.classList.toggle("eliminator-mode-active", App.eliminatorMode);
    });
  }

  // Check Answer
  DOM.btnCheckAnswer.addEventListener("click", checkAnswer);

  // Grid-in input change
  DOM.gridinInput.addEventListener("input", () => {
    DOM.btnCheckAnswer.disabled = (DOM.gridinInput.value.trim() === "");
    const q = App.currentQuestion;
    if (q) {
      const qState = App.studentState.attempts[q.id];
      if (qState && qState.justChecked) {
        qState.justChecked = false;
        saveLocalState();
        syncTimerState();
      }
    }
  });
  DOM.gridinInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !DOM.btnCheckAnswer.disabled) {
      checkAnswer();
    }
  });

  // Navigation Dock
  DOM.btnNavBack.addEventListener("click", () => {
    if (!checkCanNavigate()) return;
    if (App.currentIndex > 0) {
      App.currentIndex--;
      renderCurrentQuestion();
    }
  });

  DOM.btnNavNext.addEventListener("click", () => {
    if (!checkCanNavigate()) return;
    if (App.currentIndex < App.questions.length - 1) {
      App.currentIndex++;
      renderCurrentQuestion();
    }
  });

  // Question Navigator Modal
  DOM.btnOpenNavigator.addEventListener("click", () => {
    pauseTimer();
    renderNavigatorTiles();
    DOM.navigatorOverlay.classList.remove("hidden");
  });
  DOM.btnCloseNavigator.addEventListener("click", () => {
    DOM.navigatorOverlay.classList.add("hidden");
    syncTimerState();
  });
  DOM.navigatorOverlay.addEventListener("click", (e) => {
    if (e.target === DOM.navigatorOverlay) {
      DOM.navigatorOverlay.classList.add("hidden");
      syncTimerState();
    }
  });

  // Timer Controls
  DOM.btnTimerToggleView.addEventListener("click", () => {
    App.timerHidden = !App.timerHidden;
    DOM.timerDisplay.classList.toggle("hidden-time", App.timerHidden);
    DOM.btnTimerToggleView.textContent = App.timerHidden ? "Show" : "Hide";
  });

  DOM.btnTimerPause.addEventListener("click", () => {
    if (App.timerRunning) {
      App.manualPause = true;
      pauseTimer();
    } else {
      App.manualPause = false;
      resumeTimer();
    }
  });

  // Modals
  DOM.btnOpenCalc.addEventListener("click", () => {
    const isHidden = DOM.modalCalculator.classList.contains("hidden");
    DOM.modalCalculator.classList.toggle("hidden");
    if (isHidden) {
      DOM.modalCalculator.style.zIndex = "1000";
      // Ensure calculator is positioned nicely within viewport
      const rect = DOM.modalCalculator.getBoundingClientRect();
      if (rect.right < 80 || rect.left > window.innerWidth - 80 || rect.top > window.innerHeight - 44) {
        DOM.modalCalculator.style.left = "auto";
        DOM.modalCalculator.style.top = "80px";
        DOM.modalCalculator.style.right = "40px";
      }
    }
    syncTimerState();
  });
  DOM.btnCloseCalculator.addEventListener("click", () => {
    DOM.modalCalculator.classList.add("hidden");
    syncTimerState();
  });

  DOM.btnOpenRef.addEventListener("click", () => {
    pauseTimer();
    DOM.modalReference.classList.remove("hidden");
  });
  DOM.btnCloseReference.addEventListener("click", () => {
    DOM.modalReference.classList.add("hidden");
    syncTimerState();
  });

  DOM.btnOpenErrorLog.addEventListener("click", () => {
    pauseTimer();
    App.editingLogId = null;
    if (DOM.notebookAddPanel) DOM.notebookAddPanel.classList.add("hidden");
    renderErrorLogs();
    DOM.modalErrorLog.classList.remove("hidden");
  });
  DOM.btnCloseErrorLog.addEventListener("click", () => {
    DOM.modalErrorLog.classList.add("hidden");
    syncTimerState();
  });

  if (DOM.btnOpenVocab) {
    DOM.btnOpenVocab.addEventListener("click", () => {
      pauseTimer();
      if (window.openAceSATVocabModal) window.openAceSATVocabModal("practice");
    });
  }

  const btnHomeOpenVocab = document.getElementById("btn-home-open-vocab");
  if (btnHomeOpenVocab) {
    btnHomeOpenVocab.addEventListener("click", () => {
      if (window.openAceSATVocabModal) {
        window.openAceSATVocabModal("practice");
      } else {
        const modal = document.getElementById("modal-acesat-vocab");
        if (modal) modal.classList.remove("hidden");
      }
    });
  }

  // Notebook Add Entry Panel
  if (DOM.btnAddNewError) {
    DOM.btnAddNewError.addEventListener("click", () => {
      if (!DOM.notebookAddPanel) return;
      const isHidden = DOM.notebookAddPanel.classList.contains("hidden");
      if (isHidden) {
        DOM.notebookAddPanel.classList.remove("hidden");
        const q = App.currentQuestion;
        if (DOM.addPanelQBadge) {
          DOM.addPanelQBadge.textContent = q ? `Câu ${q.q_label} (${q.topic})` : "Ghi chép tự do";
        }
        if (DOM.inputNewDetail) DOM.inputNewDetail.focus();
      } else {
        DOM.notebookAddPanel.classList.add("hidden");
      }
    });
  }

  if (DOM.btnCancelAddError) {
    DOM.btnCancelAddError.addEventListener("click", () => {
      if (DOM.notebookAddPanel) DOM.notebookAddPanel.classList.add("hidden");
    });
  }

  if (DOM.btnSaveNewError) {
    DOM.btnSaveNewError.addEventListener("click", () => {
      const q = App.currentQuestion;
      const detail = DOM.inputNewDetail ? DOM.inputNewDetail.value.trim() : "";
      if (!detail) {
        alert("Vui lòng nhập phân tích nguyên nhân thử sai hoặc bài học rút ra!");
        if (DOM.inputNewDetail) DOM.inputNewDetail.focus();
        return;
      }
      const newEntry = {
        id: `err_man_${Date.now()}`,
        question_id: q ? q.id : "custom",
        q_label: q ? q.q_label : "Ghi chép",
        module: q ? q.module_title : "SAT",
        skill: q ? q.topic : "Luyện thi",
        date: new Date().toLocaleDateString("vi-VN"),
        wrong_attempts: [],
        correct_answer: q ? q.correct_answer : "",
        root_cause: DOM.selectNewTrap ? DOM.selectNewTrap.value : "Bẫy SAT Trap",
        trap_detail: detail,
        student_notes: DOM.inputNewNotes ? DOM.inputNewNotes.value.trim() : "",
        vocabulary: DOM.inputNewVocab ? DOM.inputNewVocab.value.trim() : "",
        socratic_analysis: q ? (q.level1_tip || "") : "",
        status: DOM.selectNewStatus ? DOM.selectNewStatus.value : "Đang theo dõi"
      };

      if (!App.studentState.error_logs) App.studentState.error_logs = [];
      App.studentState.error_logs.unshift(newEntry);

      // Clear add form
      if (DOM.inputNewDetail) DOM.inputNewDetail.value = "";
      if (DOM.inputNewNotes) DOM.inputNewNotes.value = "";
      if (DOM.inputNewVocab) DOM.inputNewVocab.value = "";
      if (DOM.notebookAddPanel) DOM.notebookAddPanel.classList.add("hidden");

      saveLocalState();
      updateErrorBadge();
      renderErrorLogs();
    });
  }

  // Notebook Search Input
  if (DOM.inputFilterErrSearch) {
    DOM.inputFilterErrSearch.addEventListener("input", (e) => {
      App.notebookSearchQuery = e.target.value.trim();
      if (DOM.btnClearErrSearch) {
        DOM.btnClearErrSearch.classList.toggle("hidden", !App.notebookSearchQuery);
      }
      renderErrorLogs();
    });
  }

  if (DOM.btnClearErrSearch) {
    DOM.btnClearErrSearch.addEventListener("click", () => {
      if (DOM.inputFilterErrSearch) DOM.inputFilterErrSearch.value = "";
      App.notebookSearchQuery = "";
      DOM.btnClearErrSearch.classList.add("hidden");
      renderErrorLogs();
    });
  }

  // Notebook Filter Chips
  if (DOM.notebookFilterChips) {
    DOM.notebookFilterChips.querySelectorAll(".filter-chip").forEach(chip => {
      chip.addEventListener("click", () => {
        DOM.notebookFilterChips.querySelectorAll(".filter-chip").forEach(c => c.classList.remove("active"));
        chip.classList.add("active");
        App.notebookFilterStatus = chip.dataset.status || "all";
        renderErrorLogs();
      });
    });
  }

  if (DOM.btnOpenStrategies) {
    DOM.btnOpenStrategies.addEventListener("click", () => {
      pauseTimer();
      renderStrategiesModal();
      DOM.modalStrategies.classList.remove("hidden");
    });
  }
  if (DOM.btnCloseStrategies) {
    DOM.btnCloseStrategies.addEventListener("click", () => {
      DOM.modalStrategies.classList.add("hidden");
      syncTimerState();
    });
  }

  // Home Button
  if (DOM.btnHome) {
    DOM.btnHome.addEventListener("click", handleHomeClick);
  }

  // Reset Test Controls
  if (DOM.btnResetTest) {
    DOM.btnResetTest.addEventListener("click", () => DOM.modalResetConfirm.classList.remove("hidden"));
  }
  if (DOM.btnCancelReset) {
    DOM.btnCancelReset.addEventListener("click", () => DOM.modalResetConfirm.classList.add("hidden"));
  }
  if (DOM.btnConfirmDoReset) {
    DOM.btnConfirmDoReset.addEventListener("click", handleResetConfirm);
  }

  // Export Excel
  if (DOM.btnExportExcel) {
    DOM.btnExportExcel.addEventListener("click", exportExcelPersonalized);
  }

  // Session Counter -> Open ARR Report
  if (DOM.headerSessionCounter) {
    DOM.headerSessionCounter.addEventListener("click", openAARModal);
  }

  // ARR / AAR Report Controls
  if (DOM.btnOpenAar) DOM.btnOpenAar.addEventListener("click", openAARModal);
  if (DOM.btnHomeOpenAar) DOM.btnHomeOpenAar.addEventListener("click", openAARModal);
  if (DOM.btnCloseAar) DOM.btnCloseAar.addEventListener("click", closeAARModal);
  if (DOM.btnAarCancel) DOM.btnAarCancel.addEventListener("click", closeAARModal);
  if (DOM.modalAarReport) {
    DOM.modalAarReport.addEventListener("click", (e) => {
      if (e.target === DOM.modalAarReport) closeAARModal();
    });
  }
  if (DOM.tabBtnAarForm) DOM.tabBtnAarForm.addEventListener("click", () => switchAARTab("form"));
  if (DOM.tabBtnAarHistory) DOM.tabBtnAarHistory.addEventListener("click", () => switchAARTab("history"));
  if (DOM.aarScopePills) {
    DOM.aarScopePills.querySelectorAll(".aar-scope-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        App.aarScope = btn.getAttribute("data-scope") || "session";
        refreshAARPerformanceUI(true);
      });
    });
  }
  if (DOM.aarSelectSatModule) {
    DOM.aarSelectSatModule.addEventListener("change", () => {
      toggleAarCustomModuleInput(true);
      captureModalAarDraftFromInputs({ markModuleUserSet: true });
    });
  }
  if (DOM.aarInputSatModuleCustom) {
    DOM.aarInputSatModuleCustom.addEventListener("input", () => captureModalAarDraftFromInputs({ markModuleUserSet: true }));
  }
  if (DOM.aarInputSessionLabel) {
    DOM.aarInputSessionLabel.addEventListener("input", () => captureModalAarDraftFromInputs());
  }
  if (DOM.aarSelectIste) {
    DOM.aarSelectIste.addEventListener("change", () => {
      updateAARIsteHint();
      captureModalAarDraftFromInputs({ markIsteUserSet: true });
    });
  }
  if (DOM.aarInputGoal) {
    DOM.aarInputGoal.addEventListener("input", () => captureModalAarDraftFromInputs());
  }
  if (DOM.aarInputChallenge) {
    DOM.aarInputChallenge.addEventListener("input", () => captureModalAarDraftFromInputs());
  }
  if (DOM.aarInputStudentName) {
    DOM.aarInputStudentName.addEventListener("input", () => {
      const val = DOM.aarInputStudentName.value.trim();
      App.studentState.student_name = val;
      if (DOM.homeInputName) DOM.homeInputName.value = val;
      if (DOM.homeStudentNameChip) DOM.homeStudentNameChip.textContent = val || "Chưa đăng ký";
      if (DOM.headerStudentName) DOM.headerStudentName.textContent = val || "Học sinh";
      saveLocalState();
    });
  }
  if (DOM.aarInputStudentEmail) {
    DOM.aarInputStudentEmail.addEventListener("input", () => {
      const val = DOM.aarInputStudentEmail.value.trim();
      App.studentState.student_email = val;
      if (DOM.homeInputEmail) DOM.homeInputEmail.value = val;
      if (DOM.aarPreviewCcEmail) {
        DOM.aarPreviewCcEmail.textContent = val || "Chưa nhập email học sinh";
      }
      saveLocalState();
    });
  }
  if (DOM.btnAarPullErrors) {
    DOM.btnAarPullErrors.addEventListener("click", pullErrorsIntoAARGap);
  }
  if (DOM.btnAarSubmitSend) {
    DOM.btnAarSubmitSend.addEventListener("click", submitAARReport);
  }
  if (DOM.btnAarDownloadOnly) {
    DOM.btnAarDownloadOnly.addEventListener("click", downloadAARExcelOnly);
  }
  if (DOM.btnAarExportAllHistory) {
    DOM.btnAarExportAllHistory.addEventListener("click", exportAllAARHistoryExcel);
  }

  // Success Modal Controls
  DOM.btnCloseSuccess.addEventListener("click", () => DOM.modalSubmitSuccess.classList.add("hidden"));
  if (DOM.btnRelaunchMail) {
    DOM.btnRelaunchMail.addEventListener("click", () => {
      if (App.lastMailtoUrl) window.location.href = App.lastMailtoUrl;
    });
  }
  if (DOM.btnCopyMailBody) {
    DOM.btnCopyMailBody.addEventListener("click", async () => {
      const textToCopy = App.lastReportText || "";
      if (!textToCopy) return;
      try {
        await navigator.clipboard.writeText(textToCopy);
        const orig = DOM.btnCopyMailBody.textContent;
        DOM.btnCopyMailBody.textContent = "✅ Đã Copy Nội Dung!";
        setTimeout(() => { DOM.btnCopyMailBody.textContent = orig; }, 2000);
      } catch (err) {
        const ta = document.createElement("textarea");
        ta.value = textToCopy;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        ta.remove();
      }
    });
  }

  // Mandatory Error Reflection Modal Controls
  if (DOM.btnSaveReflAndReview) {
    DOM.btnSaveReflAndReview.addEventListener("click", () => saveMandatoryReflection(false));
  }
  if (DOM.btnSaveMandatoryReflection) {
    DOM.btnSaveMandatoryReflection.addEventListener("click", () => saveMandatoryReflection(true));
  }

  // PDF External Drive Opener
  if (DOM.btnPdfExternal) {
    DOM.btnPdfExternal.addEventListener("click", () => {
      const url = (App.activeTest && App.activeTest.pdfViewUrl) || (App.db && App.db.pdf_drive_view) || "https://drive.google.com";
      window.open(url, '_blank');
    });
  }

  // Multi-Exam Selectors Listeners
  if (DOM.selectActiveExam) {
    DOM.selectActiveExam.addEventListener("change", (e) => {
      switchTest(e.target.value);
    });
  }
  if (DOM.selectPracticeExam) {
    DOM.selectPracticeExam.addEventListener("change", (e) => {
      switchTest(e.target.value);
    });
  }

  // Excerpt Accordion (optional)
  if (DOM.excerptHeader) {
    DOM.excerptHeader.addEventListener("click", () => {
      if (DOM.excerptBody) DOM.excerptBody.classList.toggle("collapsed");
      if (DOM.excerptToggleIcon && DOM.excerptBody) {
        DOM.excerptToggleIcon.textContent = DOM.excerptBody.classList.contains("collapsed") ? "▼" : "▲";
      }
    });
  }

  // Hints Accordion
  DOM.hintHead1.addEventListener("click", () => DOM.hintContent1.classList.toggle("collapsed"));
  DOM.hintHead2.addEventListener("click", () => DOM.hintContent2.classList.toggle("collapsed"));
  DOM.hintHead3.addEventListener("click", () => DOM.hintContent3.classList.toggle("collapsed"));
  if (DOM.hintHead4) DOM.hintHead4.addEventListener("click", () => DOM.hintContent4.classList.toggle("collapsed"));

  // --- Google Material UX Home Page Listeners ---
  if (DOM.btnHeroEnterTest) {
    DOM.btnHeroEnterTest.addEventListener("click", () => startPracticeFromHome());
  }
  if (DOM.btnHomeStartPractice) {
    DOM.btnHomeStartPractice.addEventListener("click", () => startPracticeFromHome());
  }
  if (DOM.homeUserChip) {
    DOM.homeUserChip.addEventListener("click", () => {
      if (DOM.homeInputName) DOM.homeInputName.focus();
    });
  }

  // Target score chips selection
  if (DOM.targetChipsContainer) {
    DOM.targetChipsContainer.addEventListener("click", (e) => {
      const chip = e.target.closest(".target-chip");
      if (!chip) return;
      DOM.targetChipsContainer.querySelectorAll(".target-chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      App.studentState.student_target = chip.getAttribute("data-val");
      saveLocalState();
      syncAarTargetPills();
    });
  }

  // Home Form inputs real-time sync
  if (DOM.homeInputName) {
    DOM.homeInputName.addEventListener("input", (e) => {
      const val = e.target.value.trim();
      App.studentState.student_name = val;
      if (DOM.homeStudentNameChip) {
        DOM.homeStudentNameChip.textContent = val || "Chưa đăng ký";
      }
      if (DOM.headerStudentName) {
        DOM.headerStudentName.textContent = val || "Học sinh";
      }
      if (DOM.aarInputStudentName) {
        DOM.aarInputStudentName.value = val;
      }
      saveLocalState();
    });
  }
  if (DOM.homeInputEmail) {
    DOM.homeInputEmail.addEventListener("input", (e) => {
      const val = e.target.value.trim();
      App.studentState.student_email = val;
      if (DOM.aarInputStudentEmail) DOM.aarInputStudentEmail.value = val;
      if (DOM.aarPreviewCcEmail) DOM.aarPreviewCcEmail.textContent = val || "Chưa nhập email học sinh";
      saveLocalState();
    });
  }

  // Integrated Home Anticipation (Stage 1 AAR) real-time two-way sync
  if (DOM.homeAarSession) {
    DOM.homeAarSession.addEventListener("input", () => captureHomeAarDraftFromInputs());
  }
  if (DOM.homeAarSatModule) {
    DOM.homeAarSatModule.addEventListener("change", () => {
      toggleCustomModuleField(DOM.homeAarSatModule, DOM.homeAarSatModuleCustom, true);
      captureHomeAarDraftFromInputs({ markModuleUserSet: true });
    });
  }
  if (DOM.homeAarSatModuleCustom) {
    DOM.homeAarSatModuleCustom.addEventListener("input", () => captureHomeAarDraftFromInputs({ markModuleUserSet: true }));
  }
  if (DOM.homeAarIste) {
    DOM.homeAarIste.addEventListener("change", () => {
      updateIsteHintFor(DOM.homeAarIste, DOM.homeAarIsteHint);
      captureHomeAarDraftFromInputs({ markIsteUserSet: true });
    });
  }
  if (DOM.homeAarGoal) {
    DOM.homeAarGoal.addEventListener("input", () => captureHomeAarDraftFromInputs());
  }
  if (DOM.homeAarChallenge) {
    DOM.homeAarChallenge.addEventListener("input", () => captureHomeAarDraftFromInputs());
  }

  // View Guide button
  if (DOM.btnHomeViewGuide) {
    DOM.btnHomeViewGuide.addEventListener("click", () => {
      const name = App.studentState.student_name || (DOM.homeInputName ? DOM.homeInputName.value.trim() : "") || "Học sinh";
      const email = App.studentState.student_email || (DOM.homeInputEmail ? DOM.homeInputEmail.value.trim() : "") || "Chưa có email";
      if (DOM.obPreviewName) DOM.obPreviewName.textContent = name;
      if (DOM.obPreviewEmail) DOM.obPreviewEmail.textContent = email;
      if (DOM.modalOnboarding) {
        DOM.modalOnboarding.classList.remove("hidden");
        DOM.modalOnboarding.style.display = "flex";
      }
    });
  }

  // 4 Module Cards & Jump Buttons
  document.querySelectorAll(".module-card").forEach(card => {
    card.addEventListener("click", (e) => {
      const modCode = card.getAttribute("data-module");
      if (modCode) {
        startPracticeFromHome(modCode);
      }
    });
  });

  // Keyboard Shortcuts
  window.addEventListener("keydown", (e) => {
    if (DOM.modalMermaid && !DOM.modalMermaid.classList.contains("hidden")) {
      if (e.key === "Escape") {
        closeMermaidModal();
        e.preventDefault();
        return;
      }
      if (e.key === "+" || e.key === "=") {
        if (DOM.btnMmZoomIn) DOM.btnMmZoomIn.click();
        e.preventDefault();
        return;
      }
      if (e.key === "-" || e.key === "_") {
        if (DOM.btnMmZoomOut) DOM.btnMmZoomOut.click();
        e.preventDefault();
        return;
      }
      if (e.key === "0" || e.key.toLowerCase() === "r") {
        if (DOM.btnMmZoomReset) DOM.btnMmZoomReset.click();
        e.preventDefault();
        return;
      }
      return;
    }
    if (["INPUT", "TEXTAREA", "SELECT"].includes(e.target.tagName)) return;

    const key = e.key.toUpperCase();
    if (key === "Z" && !e.ctrlKey && !e.metaKey && !e.altKey) {
      if (document.body.classList.contains("in-practice")) {
        toggleZenMode();
        e.preventDefault();
        return;
      }
    }
    if (["A", "B", "C", "D"].includes(key) || ["1", "2", "3", "4"].includes(key)) {
      const optKey = ["1", "2", "3", "4"].includes(key) ? ["A", "B", "C", "D"][parseInt(key) - 1] : key;
      const row = document.querySelector(`.option-row[data-key="${optKey}"]`);
      if (row && !row.classList.contains("eliminated")) {
        row.click();
      }
    } else if (e.key === "Enter") {
      if (!DOM.btnCheckAnswer.disabled) {
        checkAnswer();
      }
    } else if (e.key === "[" || e.key === "ArrowLeft") {
      DOM.btnNavBack.click();
    } else if (e.key === "]" || e.key === "ArrowRight") {
      DOM.btnNavNext.click();
    }
  });

  // Smart Feedback Controls
  if (DOM.btnFloatingFeedback) {
    DOM.btnFloatingFeedback.addEventListener("click", () => openFeedbackModal());
  }
  if (DOM.btnQFeedback) {
    DOM.btnQFeedback.addEventListener("click", () => openFeedbackModal());
  }
  if (DOM.btnCloseFeedback) {
    DOM.btnCloseFeedback.addEventListener("click", closeFeedbackModal);
  }
  if (DOM.modalFeedback) {
    DOM.modalFeedback.addEventListener("click", (e) => {
      if (e.target === DOM.modalFeedback) closeFeedbackModal();
    });
  }
  if (DOM.tabBtnFbNew) {
    DOM.tabBtnFbNew.addEventListener("click", () => switchFeedbackTab("new"));
  }
  if (DOM.tabBtnFbHistory) {
    DOM.tabBtnFbHistory.addEventListener("click", () => switchFeedbackTab("history"));
  }
  if (DOM.btnToggleCustomContext) {
    DOM.btnToggleCustomContext.addEventListener("click", () => {
      if (DOM.groupCustomContext) {
        DOM.groupCustomContext.classList.toggle("hidden");
      }
    });
  }
  if (DOM.btnSendAnotherFb) {
    DOM.btnSendAnotherFb.addEventListener("click", () => {
      if (DOM.fbSuccessBanner) DOM.fbSuccessBanner.classList.add("hidden");
      if (DOM.formSubmitFeedback) {
        DOM.formSubmitFeedback.classList.remove("hidden");
        DOM.formSubmitFeedback.reset();
        if (DOM.inputFbName) DOM.inputFbName.value = App.studentState.student_name || "";
        if (DOM.inputFbEmail) DOM.inputFbEmail.value = App.studentState.student_email || "";
      }
    });
  }
  if (DOM.formSubmitFeedback) {
    DOM.formSubmitFeedback.addEventListener("submit", handleFeedbackSubmit);
  }

  // Mermaid Mindmap Pop-up Modal triggers
  if (DOM.btnQMermaid) {
    DOM.btnQMermaid.addEventListener("click", openMermaidModal);
  }
  if (DOM.btnOpenMermaidModal) {
    DOM.btnOpenMermaidModal.addEventListener("click", openMermaidModal);
  }
  if (DOM.btnCloseMermaid) {
    DOM.btnCloseMermaid.addEventListener("click", closeMermaidModal);
  }
  if (DOM.modalMermaid) {
    DOM.modalMermaid.addEventListener("click", (e) => {
      if (e.target === DOM.modalMermaid) closeMermaidModal();
    });
  }
  MermaidPanZoom.init();
}

// ================= ARR / AAR CYCLE REPORT SYSTEM =================
const ISTE_STANDARDS_LOOKUP = {
  "Empowered Learner": {
    concept: "Đặt mục tiêu cá nhân, sử dụng công nghệ để đạt mục tiêu và tự đánh giá quá trình học.",
    satApp: "Tự theo dõi tiến độ điểm số SAT, chủ động luyện đề Bluebook/Khan Academy và phân bổ thời gian theo điểm yếu."
  },
  "Digital Citizen": {
    concept: "Sử dụng công nghệ an toàn, hợp pháp, có trách nhiệm và giữ kỷ luật tập trung số.",
    satApp: "Quản lý thời gian dùng thiết bị, tránh xao nhãng khi làm test online và tôn trọng bản quyền tài liệu SAT."
  },
  "Knowledge Constructor": {
    concept: "Thu thập, phân tích và tổng hợp thông tin từ nhiều nguồn để tạo ra tri thức có ý nghĩa.",
    satApp: "Tổng hợp quy tắc Writing, phân tích cấu trúc bài Reading và xây dựng kho từ vựng SAT (Vocabulary Bank) theo ngữ cảnh."
  },
  "Innovative Designer": {
    concept: "Sử dụng quy trình thiết kế để giải quyết vấn đề và tinh chỉnh giải pháp cá nhân.",
    satApp: "Thử nghiệm chiến thuật làm bài và tự thiết kế hệ thống phân loại lỗi sai (Sổ thử sai / Error Log) hiệu quả."
  },
  "Computational Thinker": {
    concept: "Phân tích bài toán, nhận diện mẫu hình và sử dụng thuật toán/công cụ để giải quyết vấn đề.",
    satApp: "Sử dụng thành thạo Desmos giải nhanh SAT Math, nhận diện bẫy lặp lại và bóc tách bài toán nhiều bước."
  },
  "Creative Communicator": {
    concept: "Bày tỏ tư tưởng, lập luận rõ ràng qua nhiều phương tiện kỹ thuật số.",
    satApp: "Diễn giải lại cách giải câu SAT Math khó hoặc lập luận chứng cứ (Evidence-Based) khi phân tích bài Reading."
  },
  "Global Collaborator": {
    concept: "Kết nối với cộng đồng người học rộng lớn để trao đổi chiến thuật và học hỏi lẫn nhau.",
    satApp: "Thảo luận câu hỏi khó trong nhóm học SAT và chia sẻ kinh nghiệm luyện đề với thầy cô & bạn học."
  }
};

function createEmptyAarDraft() {
  return {
    session_label: "",
    sat_module: "",
    sat_module_custom: "",
    sat_module_user_set: false,
    iste_standard: "",
    iste_user_set: false,
    goal: "",
    challenge: "",
    updated_at: null
  };
}

function formatTargetScoreLabel(targetVal) {
  const val = String(targetVal || "1400+").trim();
  if (val === "1300+") return "🎯 1300+";
  if (val === "1500+") return "🎯 1500+ Ivy League";
  if (val === "1400+") return "🎯 1400+ Top 50";
  return `🎯 ${val}`;
}

function getDefaultIsteForModule(modChoice) {
  if (!DOM.aarSelectIste) return "";
  const opts = Array.from(DOM.aarSelectIste.options);
  const low = String(modChoice || "").trim().toLowerCase();
  if (/^(math|toán)\b|\b(math|desmos|algebra|geometry|trig)\b/.test(low)) {
    const m = opts.find(o => o.value.includes("Computational Thinker"));
    if (m) return m.value;
  } else if (/^(reading|writing)\b|\b(reading|writing|grammar|vocab|rhetoric)\b/.test(low)) {
    const rw = opts.find(o => o.value.includes("Knowledge Constructor"));
    if (rw) return rw.value;
  }
  return opts[0] ? opts[0].value : "";
}

function populateMirroredSelect(sourceSel, targetSel) {
  if (!sourceSel || !targetSel) return;
  targetSel.innerHTML = "";
  Array.from(sourceSel.options).forEach(opt => {
    const clone = document.createElement("option");
    clone.value = opt.value;
    clone.textContent = opt.textContent;
    targetSel.appendChild(clone);
  });
}

function initHomeAarSelects() {
  populateMirroredSelect(DOM.aarSelectSatModule, DOM.homeAarSatModule);
  populateMirroredSelect(DOM.aarSelectIste, DOM.homeAarIste);
  syncAarAnticipationUI();
}

function toggleCustomModuleField(selectEl, customEl, shouldFocus = false) {
  if (!selectEl || !customEl) return;
  const isCustom = selectEl.value === "Khác (Tự nhập...)";
  customEl.classList.toggle("hidden", !isCustom);
  if (isCustom && shouldFocus) {
    customEl.focus();
  }
}

function loadGlobalAARState() {
  try {
    const raw = localStorage.getItem(GLOBAL_AAR_STORAGE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      App.aarLogs = Array.isArray(parsed.logs) ? parsed.logs : [];
      App.lastAarReportAt = parsed.last_report_at || null;
    } else {
      App.aarLogs = [];
      App.lastAarReportAt = null;
    }
  } catch (e) {
    App.aarLogs = [];
    App.lastAarReportAt = null;
  }

  try {
    const rawDraft = localStorage.getItem(GLOBAL_AAR_DRAFT_KEY);
    if (rawDraft) {
      const parsedDraft = JSON.parse(rawDraft);
      App.aarDraft = Object.assign(createEmptyAarDraft(), parsedDraft || {});
    } else {
      App.aarDraft = createEmptyAarDraft();
    }
  } catch (e) {
    App.aarDraft = createEmptyAarDraft();
  }

  updateAARHistoryBadge();
}

function saveGlobalAARState() {
  try {
    const data = {
      logs: App.aarLogs || [],
      last_report_at: App.lastAarReportAt || null
    };
    localStorage.setItem(GLOBAL_AAR_STORAGE_KEY, JSON.stringify(data));
  } catch (e) {
    console.warn("Could not save global AAR state:", e);
  }
  updateAARHistoryBadge();
}

function saveGlobalAARDraft() {
  try {
    App.aarDraft = Object.assign(createEmptyAarDraft(), App.aarDraft || {}, {
      updated_at: new Date().toISOString()
    });
    localStorage.setItem(GLOBAL_AAR_DRAFT_KEY, JSON.stringify(App.aarDraft));
  } catch (e) {
    console.warn("Could not save global AAR draft:", e);
  }
  updateHomeAarSyncBadge();
}

function syncAarTargetPills() {
  const label = formatTargetScoreLabel((App.studentState && App.studentState.student_target) || "1400+");
  if (DOM.homeGoalTargetPill) DOM.homeGoalTargetPill.textContent = label;
  if (DOM.aarTargetScorePill) DOM.aarTargetScorePill.textContent = `Mục tiêu SAT: ${label}`;
}

function updateHomeAarSyncBadge() {
  if (!DOM.homeAarSyncBadge) return;
  const d = App.aarDraft || {};
  const isReady = Boolean(String(d.goal || "").trim() && String(d.challenge || "").trim());
  DOM.homeAarSyncBadge.classList.toggle("ready", isReady);
  DOM.homeAarSyncBadge.textContent = isReady ? "✓ Đã đồng bộ sẵn vào ARR" : "💾 Tự lưu vào Báo cáo ARR";
}

function getEffectiveModuleForIste(satModule, customModule) {
  if (satModule === "Khác (Tự nhập...)") {
    const customTrim = String(customModule || "").trim();
    return customTrim || detectDefaultAarModule();
  }
  return satModule;
}

function resolveAnticipationState() {
  const d = Object.assign(createEmptyAarDraft(), App.aarDraft || {});
  const nextIdx = (App.aarLogs ? App.aarLogs.length : 0) + 1;
  const sessionLabel = d.session_label && d.session_label.trim() ? d.session_label : `Buổi ${nextIdx}`;
  const satModule = (d.sat_module_user_set && d.sat_module) ? d.sat_module : detectDefaultAarModule();
  const effectiveModForIste = getEffectiveModuleForIste(satModule, d.sat_module_custom);
  const isteStandard = (d.iste_user_set && d.iste_standard)
    ? d.iste_standard
    : (getDefaultIsteForModule(effectiveModForIste) || d.iste_standard);
  return {
    session_label: sessionLabel,
    sat_module: satModule,
    sat_module_custom: d.sat_module_custom || "",
    iste_standard: isteStandard,
    goal: d.goal || "",
    challenge: d.challenge || ""
  };
}

function applyAnticipationFieldsToElements(resolved, targets) {
  targets.forEach(({ sessionEl, modEl, modCustomEl, isteEl, hintEl, goalEl, challengeEl }) => {
    if (sessionEl && document.activeElement !== sessionEl) sessionEl.value = resolved.session_label;
    if (modEl && modEl.options.length > 0 && document.activeElement !== modEl) {
      modEl.value = resolved.sat_module;
    }
    if (modCustomEl) {
      if (document.activeElement !== modCustomEl) modCustomEl.value = resolved.sat_module_custom;
      toggleCustomModuleField(modEl, modCustomEl, false);
    }
    if (isteEl && isteEl.options.length > 0 && resolved.iste_standard && document.activeElement !== isteEl) {
      isteEl.value = resolved.iste_standard;
    }
    updateIsteHintFor(isteEl, hintEl);
    if (goalEl && document.activeElement !== goalEl) goalEl.value = resolved.goal;
    if (challengeEl && document.activeElement !== challengeEl) challengeEl.value = resolved.challenge;
  });
}

function syncAarAnticipationUI() {
  const resolved = resolveAnticipationState();
  applyAnticipationFieldsToElements(resolved, [
    {
      sessionEl: DOM.homeAarSession,
      modEl: DOM.homeAarSatModule,
      modCustomEl: DOM.homeAarSatModuleCustom,
      isteEl: DOM.homeAarIste,
      hintEl: DOM.homeAarIsteHint,
      goalEl: DOM.homeAarGoal,
      challengeEl: DOM.homeAarChallenge
    },
    {
      sessionEl: DOM.aarInputSessionLabel,
      modEl: DOM.aarSelectSatModule,
      modCustomEl: DOM.aarInputSatModuleCustom,
      isteEl: DOM.aarSelectIste,
      hintEl: DOM.aarIsteHint,
      goalEl: DOM.aarInputGoal,
      challengeEl: DOM.aarInputChallenge
    }
  ]);
  syncAarTargetPills();
  updateHomeAarSyncBadge();
}

function captureDraftFromSource(source, { markModuleUserSet = false, markIsteUserSet = false } = {}) {
  const prev = Object.assign(createEmptyAarDraft(), App.aarDraft || {});
  const modVal = source.modEl ? source.modEl.value : prev.sat_module;
  const userSetMod = markModuleUserSet || prev.sat_module_user_set;
  const userSetIste = markIsteUserSet || prev.iste_user_set;

  App.aarDraft = {
    session_label: source.sessionEl ? source.sessionEl.value.trim() : prev.session_label,
    sat_module: modVal,
    sat_module_custom: source.modCustomEl ? source.modCustomEl.value.trim() : prev.sat_module_custom,
    sat_module_user_set: userSetMod,
    iste_standard: source.isteEl ? source.isteEl.value : prev.iste_standard,
    iste_user_set: userSetIste,
    goal: source.goalEl ? source.goalEl.value : prev.goal,
    challenge: source.challengeEl ? source.challengeEl.value : prev.challenge
  };

  if (markModuleUserSet && !userSetIste && source.isteEl) {
    const autoIste = getDefaultIsteForModule(
      getEffectiveModuleForIste(modVal, App.aarDraft.sat_module_custom)
    );
    if (autoIste) App.aarDraft.iste_standard = autoIste;
  }

  saveGlobalAARDraft();
  syncAarAnticipationUI();
}

function captureHomeAarDraftFromInputs(opts = {}) {
  captureDraftFromSource({
    sessionEl: DOM.homeAarSession,
    modEl: DOM.homeAarSatModule,
    modCustomEl: DOM.homeAarSatModuleCustom,
    isteEl: DOM.homeAarIste,
    goalEl: DOM.homeAarGoal,
    challengeEl: DOM.homeAarChallenge
  }, opts);
}

function captureModalAarDraftFromInputs(opts = {}) {
  captureDraftFromSource({
    sessionEl: DOM.aarInputSessionLabel,
    modEl: DOM.aarSelectSatModule,
    modCustomEl: DOM.aarInputSatModuleCustom,
    isteEl: DOM.aarSelectIste,
    goalEl: DOM.aarInputGoal,
    challengeEl: DOM.aarInputChallenge
  }, opts);
}

// ================= CROSS-TEST SESSION TRACKER & COUNTER =================
function loadGlobalSessionTracker() {
  try {
    const raw = localStorage.getItem(GLOBAL_SESSION_TRACKER_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      App.globalSessionItems = (parsed && parsed.items && typeof parsed.items === "object") ? parsed.items : {};
    } else {
      App.globalSessionItems = {};
    }
  } catch (e) {
    App.globalSessionItems = {};
  }
  updateGlobalSessionCounterUI();
}

function saveGlobalSessionTracker() {
  try {
    const payload = {
      updated_at: new Date().toISOString(),
      items: App.globalSessionItems || {}
    };
    localStorage.setItem(GLOBAL_SESSION_TRACKER_KEY, JSON.stringify(payload));
  } catch (e) {
    console.warn("Could not save cross-test session tracker:", e);
  }
  updateGlobalSessionCounterUI();
}

function recordQuestionInGlobalSession(q, qState) {
  if (!q || !qState) return;
  if (!App.globalSessionItems || typeof App.globalSessionItems !== "object") {
    App.globalSessionItems = {};
  }
  const testId = App.activeTestId || "oct-2026";
  const testShort = (App.activeTest && App.activeTest.short_title) || (App.db && App.db.test_title) || testId;
  const eff = parseFloat(qState.efficiency) || 0;
  const isCorrect = (qState.status === "mastered_l1" || qState.status === "mastered_l2" || qState.status === "mastered_l3" || eff > 0);
  const modCode = String(q.module_code || App.activeModuleCode || "");
  const modTitle = String(q.module_title || "");
  const isMath = modCode.toLowerCase().includes("math") || modTitle.toLowerCase().includes("math") || testId.toLowerCase().includes("math");
  const key = `${testId}::${q.id}`;

  App.globalSessionItems[key] = {
    key,
    test_id: testId,
    test_short: testShort,
    qid: q.id,
    q_label: q.q_label || `Q${q.id}`,
    module_code: modCode,
    module_title: modTitle,
    is_math: isMath,
    is_correct: isCorrect,
    l1_correct: eff >= 0.99 || qState.status === "mastered_l1",
    l2_correct: (eff >= 0.6 && eff < 0.99) || qState.status === "mastered_l2",
    l3_correct: (eff >= 0.3 && eff < 0.6) || qState.status === "mastered_l3",
    efficiency: eff,
    status: qState.status || "unanswered",
    practiced_at: qState.last_practiced_at || new Date().toISOString()
  };

  saveGlobalSessionTracker();
}

function updateGlobalSessionCounterUI() {
  const items = Object.values(App.globalSessionItems || {});
  const total = items.length;
  const correct = items.filter(it => it && it.is_correct).length;
  if (DOM.headerSessionCountVal) {
    DOM.headerSessionCountVal.textContent = String(total);
  }
  if (DOM.headerSessionCounter) {
    const pct = total > 0 ? Math.round((correct / total) * 100) : 0;
    DOM.headerSessionCounter.title = total > 0
      ? `Đã thực hành ${total} câu xuyên suốt buổi học (Đúng: ${correct}/${total} - ${pct}%) • Bấm để mở ARR Report`
      : "Tổng số câu đã thực hành trong buổi học (xuyên suốt khi đổi đề) — Bấm để mở ARR Report";
  }
}

function getAllSessionErrorLogs(practicedMapByTest) {
  const collected = [];
  const seen = new Set();
  const testIds = Object.keys(practicedMapByTest || {});
  testIds.forEach(tId => {
    const qSet = practicedMapByTest[tId];
    let logs = [];
    if (tId === App.activeTestId) {
      logs = App.studentState.error_logs || [];
    } else {
      try {
        const raw = localStorage.getItem(getStorageKeyForTest(tId));
        if (raw) {
          const parsed = JSON.parse(raw);
          logs = Array.isArray(parsed.error_logs) ? parsed.error_logs : [];
        }
      } catch (e) {}
    }
    const meta = (App.testsManifest || []).find(t => t.id === tId || t.code === tId);
    const tShort = meta ? meta.short_title : tId;
    logs.forEach(err => {
      const qidStr = String(err.question_id || "");
      if (qSet.has(qidStr)) {
        const uniq = `${tId}::${err.id || qidStr}`;
        if (!seen.has(uniq)) {
          seen.add(uniq);
          collected.push(Object.assign({}, err, { _test_short: tShort }));
        }
      }
    });
  });
  return collected;
}

function toggleAarCustomModuleInput(shouldFocus = true) {
  toggleCustomModuleField(DOM.aarSelectSatModule, DOM.aarInputSatModuleCustom, shouldFocus);
}

function updateAARHistoryBadge() {
  if (DOM.aarHistoryCount) {
    DOM.aarHistoryCount.textContent = String((App.aarLogs || []).length);
  }
}

function detectDefaultAarModule() {
  const sessionItems = Object.values(App.globalSessionItems || {});
  if (sessionItems.length > 0) {
    const distinctTests = new Set(sessionItems.map(it => it.test_id).filter(Boolean));
    const hasMathItem = sessionItems.some(it => it.is_math);
    const hasRwItem = sessionItems.some(it => !it.is_math);
    if (distinctTests.size >= 2 || (hasMathItem && hasRwItem)) {
      return "Mix (Nhiều mô-đun / Tài liệu kết hợp)";
    }
  }

  const testId = (App.activeTestId || "").toLowerCase();
  const modCode = (App.activeModuleCode || "").toLowerCase();
  const activeModMeta = (App.db && Array.isArray(App.db.modules))
    ? App.db.modules.find(m => m.code === App.activeModuleCode)
    : null;
  const modTitle = activeModMeta ? String(activeModMeta.title || "").toLowerCase() : "";

  if (testId.includes("panda") || testId.includes("math") || modCode.includes("math") || modTitle.includes("math")) {
    if (modTitle.includes("geometry") || modTitle.includes("trig") || modTitle.includes("triangle") || modTitle.includes("circle")) {
      return "Math: Geometry & Trig";
    }
    if (modTitle.includes("probability") || modTitle.includes("stat") || modTitle.includes("percent") || modTitle.includes("ratio") || modTitle.includes("rate")) {
      return "Math: Problem-Solving";
    }
    if (modTitle.includes("quadratic") || modTitle.includes("exponent") || modTitle.includes("function") || modTitle.includes("polynomial") || modTitle.includes("complex")) {
      return "Math: Advanced Math";
    }
    return "Math: Algebra";
  }

  if (testId.includes("writing") || testId.includes("grammar")) {
    if (modTitle.includes("transition") || modTitle.includes("student notes") || modCode.startsWith("ch1") || modCode.startsWith("ch2")) {
      return "Writing: Expression of Ideas";
    }
    return "Writing: Standard English";
  }
  if (testId.includes("erica") || modCode.startsWith("rw_") || modTitle.includes("reading")) {
    if (modTitle.includes("vocabulary") || modTitle.includes("words in context") || modTitle.includes("purpose") || modTitle.includes("structure") || modTitle.includes("rhetoric") || modTitle.includes("tone")) {
      return "Reading: Craft & Structure";
    }
    return "Reading: Information & Ideas";
  }

  if (modCode === "all") {
    return "Digital SAT Full-test";
  }
  return "Digital SAT Full-test";
}

function calculateAARSessionSummary(scope = "session") {
  const allQs = (App.db && Array.isArray(App.db.questions)) ? App.db.questions : [];
  const attempts = App.studentState.attempts || {};
  const lastAarAt = App.lastAarReportAt;
  const activeTestShort = (App.activeTest && App.activeTest.short_title) || (App.db && App.db.test_title) || "Digital SAT";

  let practicedCount = 0;
  let correctCount = 0;
  let l1Correct = 0;
  let l2Correct = 0;
  let l3Correct = 0;
  let earnedWeight = 0;
  let hasMath = false;
  let scopedErrors = [];
  let sourceSummary = activeTestShort;
  let isMixedSources = false;

  if (scope === "session") {
    // Merge persistent cross-test globalSessionItems with any active-test items practiced since last AAR report
    const combinedMap = Object.assign({}, App.globalSessionItems || {});
    allQs.forEach(q => {
      const st = attempts[q.id];
      if (!st || !Array.isArray(st.attempts) || st.attempts.length === 0) return;
      const key = `${App.activeTestId}::${q.id}`;
      const inCurrentMem = App.sessionPracticedIds && App.sessionPracticedIds.has(key);
      const isFreshTime = st.last_practiced_at && (!lastAarAt || st.last_practiced_at > lastAarAt);
      if ((inCurrentMem || isFreshTime) && !combinedMap[key]) {
        const eff = parseFloat(st.efficiency) || 0;
        const modCode = String(q.module_code || "");
        combinedMap[key] = {
          key,
          test_id: App.activeTestId,
          test_short: activeTestShort,
          qid: q.id,
          q_label: q.q_label || `Q${q.id}`,
          module_code: modCode,
          is_math: modCode.toLowerCase().includes("math") || (App.activeTestId || "").includes("math"),
          is_correct: (st.status === "mastered_l1" || st.status === "mastered_l2" || st.status === "mastered_l3" || eff > 0),
          l1_correct: eff >= 0.99 || st.status === "mastered_l1",
          l2_correct: (eff >= 0.6 && eff < 0.99) || st.status === "mastered_l2",
          l3_correct: (eff >= 0.3 && eff < 0.6) || st.status === "mastered_l3",
          efficiency: eff
        };
      }
    });

    const items = Object.values(combinedMap);
    const bySource = {};
    const practicedMapByTest = {};

    items.forEach(it => {
      practicedCount++;
      if (it.is_correct) correctCount++;
      if (it.l1_correct) l1Correct++;
      else if (it.l2_correct) l2Correct++;
      else if (it.l3_correct) l3Correct++;
      earnedWeight += parseFloat(it.efficiency) || 0;
      if (it.is_math) hasMath = true;

      const sName = it.test_short || it.test_id || activeTestShort;
      if (!bySource[sName]) bySource[sName] = { total: 0, correct: 0 };
      bySource[sName].total++;
      if (it.is_correct) bySource[sName].correct++;

      const tId = it.test_id || App.activeTestId;
      if (!practicedMapByTest[tId]) practicedMapByTest[tId] = new Set();
      practicedMapByTest[tId].add(String(it.qid));
    });

    const sourceNames = Object.keys(bySource);
    isMixedSources = sourceNames.length > 1;
    if (sourceNames.length > 0) {
      sourceSummary = sourceNames.map(n => `${n} (${bySource[n].correct}/${bySource[n].total})`).join(" + ");
    }
    scopedErrors = getAllSessionErrorLogs(practicedMapByTest);
  } else {
    const isMathModule = (q) => String(q.module_code || "").toLowerCase().includes("math") || (App.activeTestId || "").includes("math");
    const targetQs = (scope === "module")
      ? ((App.questions && App.questions.length) ? App.questions : allQs)
      : allQs;
    const practicedIds = new Set();

    targetQs.forEach(q => {
      const st = attempts[q.id];
      if (st && Array.isArray(st.attempts) && st.attempts.length > 0) {
        practicedCount++;
        practicedIds.add(String(q.id));
        if (isMathModule(q)) hasMath = true;
        const eff = parseFloat(st.efficiency) || 0;
        const isMastered = (st.status === "mastered_l1" || st.status === "mastered_l2" || st.status === "mastered_l3" || eff > 0);
        if (isMastered) correctCount++;
        earnedWeight += eff;
        if (eff >= 0.99 || st.status === "mastered_l1") l1Correct++;
        else if (eff >= 0.6 || st.status === "mastered_l2") l2Correct++;
        else if (eff >= 0.3 || st.status === "mastered_l3") l3Correct++;
      }
    });
    scopedErrors = (App.studentState.error_logs || []).filter(e => practicedIds.has(String(e.question_id || "")));
  }

  const missedOrRetry = Math.max(0, practicedCount - correctCount);
  const accuracyPct = practicedCount > 0 ? Math.round((correctCount / practicedCount) * 100) : 0;
  const weightedPct = practicedCount > 0 ? Math.round((earnedWeight / practicedCount) * 100) : 0;

  return {
    scope,
    practicedCount,
    correctCount,
    l1Correct,
    l2Correct,
    l3Correct,
    l23Correct: l2Correct + l3Correct,
    missedOrRetry,
    accuracyPct,
    weightedPct,
    hasMath,
    scopedErrors,
    testShort: sourceSummary,
    activeTestShort,
    isMixedSources,
    totalInTest: allQs.length
  };
}

function updateIsteHintFor(selectEl, hintEl) {
  if (!selectEl || !hintEl) return;
  const raw = selectEl.value || "";
  const shortKey = raw.split("(")[0].trim();
  const info = ISTE_STANDARDS_LOOKUP[shortKey];
  if (info) {
    hintEl.innerHTML = `<strong>Khái niệm:</strong> ${escapeHtmlSafe(info.concept)}<br><strong>Ứng dụng SAT:</strong> ${escapeHtmlSafe(info.satApp)}`;
  } else {
    hintEl.textContent = "";
  }
}

function updateAARIsteHint() {
  updateIsteHintFor(DOM.aarSelectIste, DOM.aarIsteHint);
}

function escapeHtmlSafe(str) {
  return String(str || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function refreshAARPerformanceUI(updateFormFields = false) {
  const s = calculateAARSessionSummary(App.aarScope || "session");
  App.currentAarSummary = s;

  if (DOM.aarScopePills) {
    DOM.aarScopePills.querySelectorAll(".aar-scope-btn").forEach(btn => {
      btn.classList.toggle("active", btn.getAttribute("data-scope") === s.scope);
    });
  }

  const scopeDescMap = {
    session: s.isMixedSources ? "Xuyên suốt nhiều đề/sách trong buổi học" : "Phiên thực hành hiện tại",
    module: `Module/Chương: ${DOM.selectModule ? (DOM.selectModule.options[DOM.selectModule.selectedIndex]?.text || App.activeModuleCode) : App.activeModuleCode}`,
    all: `Toàn bộ câu đã làm trong ${s.activeTestShort}`
  };

  if (DOM.aarPerfHeadline) {
    DOM.aarPerfHeadline.textContent = `Đúng ${s.correctCount} / ${s.practicedCount} câu thực hành (${s.accuracyPct}%)`;
  }
  if (DOM.aarPerfSub) {
    DOM.aarPerfSub.textContent = `${s.testShort} • ${scopeDescMap[s.scope] || ""} • Hiệu suất trọng số Socratic: ${s.weightedPct}%`;
  }
  if (DOM.aarStatCorrect) DOM.aarStatCorrect.textContent = `${s.correctCount} / ${s.practicedCount}`;
  if (DOM.aarStatPct) DOM.aarStatPct.textContent = `${s.accuracyPct}%`;
  if (DOM.aarStatL1) DOM.aarStatL1.textContent = String(s.l1Correct);
  if (DOM.aarStatL23) DOM.aarStatL23.textContent = String(s.l23Correct);
  if (DOM.aarStatMissed) DOM.aarStatMissed.textContent = String(s.missedOrRetry);

  if (updateFormFields) {
    if (DOM.aarInputEvidence) {
      if (s.practicedCount > 0) {
        DOM.aarInputEvidence.value = `Đúng ${s.correctCount}/${s.practicedCount} câu thực hành (${s.accuracyPct}%) — Đúng Lần 1: ${s.l1Correct}, Lần 2: ${s.l2Correct}, Lần 3: ${s.l3Correct}, Chưa đúng/Đang thử: ${s.missedOrRetry}. Nguồn: ${s.testShort}.`;
      } else {
        DOM.aarInputEvidence.value = `Đã hoàn thành buổi học trên ${s.activeTestShort} (0 câu chấm điểm tự động; chuyển phạm vi hoặc ghi bổ sung minh chứng tại đây).`;
      }
    }
  }
}

function pullErrorsIntoAARGap() {
  const s = App.currentAarSummary || calculateAARSessionSummary(App.aarScope || "session");
  const allErrors = (s.scopedErrors && s.scopedErrors.length > 0)
    ? s.scopedErrors
    : (App.studentState.error_logs || []);

  if (!allErrors || allErrors.length === 0) {
    alert("Chưa có lỗi sai nào được ghi trong Sổ thử sai. Em có thể tự nhập nhận xét khoảng cách học tập ở ô này.");
    return;
  }

  const lines = allErrors.slice(0, 6).map(e => {
    const src = e._test_short ? `[${e._test_short}] ` : "";
    const qLbl = e.q_label || `Q${e.question_id || ""}`;
    const cause = e.root_cause || "Bẫy SAT";
    const detail = e.trap_detail ? `: ${e.trap_detail}` : "";
    return `• ${src}${qLbl} [${cause}]${detail}`;
  });
  if (DOM.aarInputGap) {
    DOM.aarInputGap.value = lines.join("\n");
  }
}

function getTodayIsoLocal() {
  const now = new Date();
  const y = now.getFullYear();
  const m = String(now.getMonth() + 1).padStart(2, "0");
  const d = String(now.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
}

function formatDateViFromIso(isoDate) {
  if (!isoDate || !isoDate.includes("-")) return new Date().toLocaleDateString("vi-VN");
  const parts = isoDate.split("-");
  if (parts.length !== 3) return isoDate;
  return `${parts[2]}/${parts[1]}/${parts[0]}`;
}

function switchAARTab(tabName) {
  const isHistory = tabName === "history";
  if (DOM.tabBtnAarForm) DOM.tabBtnAarForm.classList.toggle("active", !isHistory);
  if (DOM.tabBtnAarHistory) DOM.tabBtnAarHistory.classList.toggle("active", isHistory);
  if (DOM.aarTabPanelForm) DOM.aarTabPanelForm.classList.toggle("hidden", isHistory);
  if (DOM.aarTabPanelHistory) DOM.aarTabPanelHistory.classList.toggle("hidden", !isHistory);
  if (isHistory) renderAARHistoryList();
}

function closeAARModal() {
  if (DOM.modalAarReport) DOM.modalAarReport.classList.add("hidden");
  syncTimerState();
}

function openAARModal() {
  pauseTimer();
  loadGlobalAARState();
  loadGlobalSessionTracker();

  const name = App.studentState.student_name || (DOM.homeInputName ? DOM.homeInputName.value.trim() : "") || "";
  const email = App.studentState.student_email || (DOM.homeInputEmail ? DOM.homeInputEmail.value.trim() : "") || "";
  if (DOM.aarInputStudentName) DOM.aarInputStudentName.value = name;
  if (DOM.aarInputStudentEmail) DOM.aarInputStudentEmail.value = email;
  if (DOM.aarPreviewCcEmail) DOM.aarPreviewCcEmail.textContent = email || "Chưa nhập email học sinh";

  // Prefer persistent cross-test session; only fall back to active module/all if 0 practiced in session
  let initialScope = "session";
  const sessionStats = calculateAARSessionSummary("session");
  if (sessionStats.practicedCount === 0) {
    const modStats = calculateAARSessionSummary("module");
    if (modStats.practicedCount > 0) {
      initialScope = "module";
    } else {
      const allStats = calculateAARSessionSummary("all");
      if (allStats.practicedCount > 0) initialScope = "all";
    }
  }
  App.aarScope = initialScope;

  if (DOM.aarInputDate) DOM.aarInputDate.value = getTodayIsoLocal();

  // Restore saved pre-session Anticipation values (Session #, Module, ISTE, Goal, Challenge) & SAT Target
  syncAarAnticipationUI();

  refreshAARPerformanceUI(true);

  switchAARTab("form");
  if (DOM.modalAarReport) DOM.modalAarReport.classList.remove("hidden");
}

function collectAARFormEntry(requireCompleteFields = true) {
  const studentName = DOM.aarInputStudentName ? DOM.aarInputStudentName.value.trim() : "";
  const studentEmail = DOM.aarInputStudentEmail ? DOM.aarInputStudentEmail.value.trim() : "";
  if (requireCompleteFields) {
    if (!studentName) {
      alert("Vui lòng nhập Họ và tên học sinh trước khi gửi báo cáo ARR!");
      if (DOM.aarInputStudentName) DOM.aarInputStudentName.focus();
      return null;
    }
    if (!studentEmail || !studentEmail.includes("@")) {
      alert("Vui lòng nhập Email học sinh hợp lệ để hệ thống CC bản sao cho em!");
      if (DOM.aarInputStudentEmail) DOM.aarInputStudentEmail.focus();
      return null;
    }
  }

  if (studentName) App.studentState.student_name = studentName;
  if (studentEmail) App.studentState.student_email = studentEmail;
  saveLocalState();
  syncHomeProfile();
  if (DOM.headerStudentName && studentName) DOM.headerStudentName.textContent = studentName;

  let satModuleVal = (DOM.aarSelectSatModule && DOM.aarSelectSatModule.value) || "Digital SAT Full-test";
  if (satModuleVal === "Khác (Tự nhập...)") {
    const customMod = DOM.aarInputSatModuleCustom ? DOM.aarInputSatModuleCustom.value.trim() : "";
    if (requireCompleteFields && !customMod) {
      alert("Vui lòng nhập tên Mô-đun SAT / chủ đề em đã học ở ô Khác!");
      if (DOM.aarInputSatModuleCustom) DOM.aarInputSatModuleCustom.focus();
      return null;
    }
    satModuleVal = customMod || "Khác";
  }

  const s = calculateAARSessionSummary(App.aarScope || "session");
  const dateIso = (DOM.aarInputDate && DOM.aarInputDate.value) ? DOM.aarInputDate.value : getTodayIsoLocal();

  const rawGoal = (DOM.aarInputGoal && DOM.aarInputGoal.value.trim()) || "";
  const targetLabel = formatTargetScoreLabel((App.studentState && App.studentState.student_target) || "1400+");
  const hasTargetHint = /1[345]00\+|Mục tiêu SAT/i.test(rawGoal);
  const fullGoal = rawGoal
    ? (hasTargetHint ? rawGoal : `${rawGoal} (Mục tiêu SAT: ${targetLabel.replace(/^🎯\s*/, "")})`)
    : "";

  const entry = {
    id: `AAR-${Date.now()}`,
    created_at: new Date().toISOString(),
    student_name: studentName || "Hoc_Sinh",
    student_email: studentEmail,
    student_target: targetLabel,
    test_id: s.isMixedSources ? "mix" : App.activeTestId,
    test_title: s.testShort,
    scope: s.scope,
    correct_count: s.correctCount,
    practiced_count: s.practicedCount,
    accuracy_pct: s.accuracyPct,
    weighted_pct: s.weightedPct,
    l1_correct: s.l1Correct,
    l2_correct: s.l2Correct,
    l3_correct: s.l3Correct,
    missed_count: s.missedOrRetry,
    error_log_count: (s.scopedErrors || []).length,
    session_label: (DOM.aarInputSessionLabel && DOM.aarInputSessionLabel.value.trim()) || `Buổi ${(App.aarLogs || []).length + 1}`,
    date_iso: dateIso,
    date_display: formatDateViFromIso(dateIso),
    sat_module: satModuleVal,
    iste_standard: (DOM.aarSelectIste && DOM.aarSelectIste.value) || "Empowered Learner \n(Học sinh Chủ động)",
    goal: fullGoal,
    challenge: (DOM.aarInputChallenge && DOM.aarInputChallenge.value.trim()) || "",
    tools: (DOM.aarInputTools && DOM.aarInputTools.value.trim()) || "",
    evidence: (DOM.aarInputEvidence && DOM.aarInputEvidence.value.trim()) || `Đúng ${s.correctCount}/${s.practicedCount} câu thực hành (${s.accuracyPct}%)`,
    mastery: (DOM.aarSelectMastery && DOM.aarSelectMastery.value) || "",
    gap: (DOM.aarInputGap && DOM.aarInputGap.value.trim()) || "",
    feedforward: (DOM.aarInputFeedforward && DOM.aarInputFeedforward.value.trim()) || "",
    emotion: (DOM.aarSelectEmotion && DOM.aarSelectEmotion.value) || "",
    status: (DOM.aarSelectStatus && DOM.aarSelectStatus.value) || ""
  };

  if (requireCompleteFields) {
    const requiredChecks = [
      { val: entry.goal, el: DOM.aarInputGoal, label: "Mục tiêu bài học & Điểm kỳ vọng" },
      { val: entry.challenge, el: DOM.aarInputChallenge, label: "Thách thức dự kiến" },
      { val: entry.tools, el: DOM.aarInputTools, label: "Công cụ & Kỹ thuật áp dụng" },
      { val: entry.mastery, el: DOM.aarSelectMastery, label: "Mức độ làm chủ" },
      { val: entry.gap, el: DOM.aarInputGap, label: "Khoảng cách (Gap) & Nguyên nhân thử sai" },
      { val: entry.feedforward, el: DOM.aarInputFeedforward, label: "Bài học chuyển hóa cho buổi sau (Feed-forward)" }
    ];
    const missing = requiredChecks.find(c => !c.val);
    if (missing) {
      alert(`Vui lòng điền/chọn đầy đủ mục "${missing.label}" để hoàn thiện chu trình AAR nhé!`);
      if (missing.el) missing.el.focus();
      return null;
    }
  }

  return entry;
}

async function generateAARExcelBlob(logsArray, studentName, studentEmail) {
  if (typeof XLSX === "undefined") return null;
  const rows = Array.isArray(logsArray) ? logsArray : [];
  const safeStudent = studentName || "Học sinh";
  const latest = rows[rows.length - 1] || null;

  try {
    let wb = null;
    try {
      const res = await fetch("aar_template.xlsx");
      if (res.ok) {
        const ab = await res.arrayBuffer();
        wb = XLSX.read(ab, { type: "array", cellStyles: true });
      }
    } catch (e) {
      console.warn("Could not fetch aar_template.xlsx:", e);
    }

    if (wb && wb.Sheets && wb.Sheets["AAR Journal"]) {
      const ws = wb.Sheets["AAR Journal"];

      ws["B1"] = Object.assign({}, ws["B1"] || {}, {
        t: "s",
        v: `HỆ THỐNG THU THẬP & PHẢN TƯ SAU MỖI BUỔI HỌC - CHU TRÌNH AAR (${safeStudent}${studentEmail ? " - " + studentEmail : ""})`
      });
      if (latest) {
        ws["B6"] = {
          t: "s",
          v: `Học sinh: ${safeStudent} (${studentEmail || "N/A"}) | Hiệu suất buổi gần nhất (${latest.session_label}): Đúng ${latest.correct_count}/${latest.practiced_count} câu thực hành (${latest.accuracy_pct}%)`
        };
      }

      const cols = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"];
      for (let r = 10; r <= 100; r++) {
        cols.forEach(col => { delete ws[`${col}${r}`]; });
      }

      rows.forEach((entry, idx) => {
        const r = 10 + idx;
        if (r > 100) return;
        ws[`B${r}`] = { t: "s", v: String(entry.session_label || `Buổi ${idx + 1}`) };
        ws[`C${r}`] = { t: "s", v: String(entry.date_display || "") };
        ws[`D${r}`] = { t: "s", v: String(entry.sat_module || "") };
        ws[`E${r}`] = { t: "s", v: String(entry.iste_standard || "") };
        ws[`F${r}`] = { t: "s", v: String(entry.goal || "") };
        ws[`G${r}`] = { t: "s", v: String(entry.challenge || "") };
        ws[`H${r}`] = { t: "s", v: String(entry.tools || "") };
        ws[`I${r}`] = { t: "s", v: String(entry.evidence || "") };
        ws[`J${r}`] = { t: "s", v: String(entry.mastery || "") };
        ws[`K${r}`] = { t: "s", v: String(entry.gap || "") };
        ws[`L${r}`] = { t: "s", v: String(entry.feedforward || "") };
        ws[`M${r}`] = { t: "s", v: String(entry.emotion || "") };
        ws[`N${r}`] = { t: "s", v: String(entry.status || "") };
      });

      const totalSessions = rows.length;
      const completedCount = rows.filter(x => x.status === "Hoàn thành").length;
      const rate = totalSessions > 0 ? completedCount / totalSessions : 0;
      const rating = rate >= 0.8
        ? "Xuất sắc (Kỷ luật cao)"
        : (rate >= 0.5 ? "Đang duy trì tốt" : (rate > 0 ? "Cần tăng cường phản tư" : "Chưa bắt đầu"));

      ws["B3"] = Object.assign({}, ws["B3"] || {}, { t: "n", v: totalSessions, f: (ws["B3"] && ws["B3"].f) || "COUNTA(B10:B100)" });
      ws["E3"] = Object.assign({}, ws["E3"] || {}, { t: "n", v: completedCount, f: (ws["E3"] && ws["E3"].f) || 'COUNTIF(N10:N100, "Hoàn thành")' });
      ws["H3"] = Object.assign({}, ws["H3"] || {}, { t: "n", v: rate, f: (ws["H3"] && ws["H3"].f) || "IFERROR(E3/B3, 0)" });
      ws["K3"] = Object.assign({}, ws["K3"] || {}, { t: "s", v: rating, f: (ws["K3"] && ws["K3"].f) || 'IF(H3>=80%, "Xuất sắc (Kỷ luật cao)", IF(H3>=50%, "Đang duy trì tốt", IF(H3>0, "Cần tăng cường phản tư", "Chưa bắt đầu")))' });
      ws["M4"] = Object.assign({}, ws["M4"] || {}, { t: "s", v: `${Math.round(rate * 100)}% Hoàn tất`, f: (ws["M4"] && ws["M4"].f) || 'TEXT(H3, "0%") & " Hoàn tất"' });

      const wbout = XLSX.write(wb, { bookType: "xlsx", type: "array" });
      return new Blob([wbout], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
    }

    const fbWb = XLSX.utils.book_new();
    const headerRow = [
      "Buổi #", "Ngày học", "Mô-đun SAT", "Tiêu chuẩn ISTE áp dụng",
      "Mục tiêu bài học & Điểm kỳ vọng", "Thách thức dự kiến", "Công cụ & Kỹ thuật áp dụng",
      "Kết quả Thực tế & Minh chứng", "Mức độ làm chủ",
      "Khoảng cách (Gap) & Nguyên nhân thử sai", "Bài học chuyển hóa cho buổi sau (Feed-forward)",
      "Cảm xúc & Mức độ tập trung", "Trạng thái AAR"
    ];
    const aoa = [
      [`BÁO CÁO CHU TRÌNH AAR - HỌC SINH: ${safeStudent} (${studentEmail || "N/A"})`],
      headerRow,
      ...rows.map(entry => [
        entry.session_label, entry.date_display, entry.sat_module, entry.iste_standard,
        entry.goal, entry.challenge, entry.tools, entry.evidence, entry.mastery,
        entry.gap, entry.feedforward, entry.emotion, entry.status
      ])
    ];
    XLSX.utils.book_append_sheet(fbWb, XLSX.utils.aoa_to_sheet(aoa), "AAR Journal");
    const wbout = XLSX.write(fbWb, { bookType: "xlsx", type: "array" });
    return new Blob([wbout], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
  } catch (err) {
    console.error("Failed generating AAR Excel:", err);
    return null;
  }
}

function buildAAREmailPayload(entry, filename) {
  const perfStr = `Đúng ${entry.correct_count} / ${entry.practiced_count} câu thực hành (${entry.accuracy_pct}%)`;
  const subject = `[SAT ARR Report] ${entry.student_name} - ${entry.session_label} (${entry.sat_module}) - ${entry.correct_count}/${entry.practiced_count} câu đúng (${entry.accuracy_pct}%)`;
  const bodyText = `Kính gửi thầy Mike Phạm,

Em xin gửi Báo cáo Phản tư Sau Buổi học (Chu trình AAR - OECD Learning Compass 2030):

[THÔNG TIN BUỔI HỌC & HIỆU SUẤT THỰC HÀNH]
- Học sinh: ${entry.student_name} (${entry.student_email})
- ${entry.session_label} | Ngày học: ${entry.date_display} | Nguồn: ${entry.test_title}
- Mô-đun SAT: ${entry.sat_module}
- HIỆU SUẤT TRONG BUỔI HỌC: ${perfStr}
- Chi tiết: Đúng Lần 1: ${entry.l1_correct} | Lần 2: ${entry.l2_correct} | Lần 3: ${entry.l3_correct} | Chưa đúng: ${entry.missed_count} | Sổ thử sai: ${entry.error_log_count}

[1. DỰ ĐOÁN (ANTICIPATION)]
- Mục tiêu điểm số SAT: ${entry.student_target || formatTargetScoreLabel((App.studentState && App.studentState.student_target) || "1400+")}
- Tiêu chuẩn ISTE: ${String(entry.iste_standard || "").replace(/\s*\n\s*/g, " ")}
- Mục tiêu & Điểm kỳ vọng: ${entry.goal}
- Thách thức dự kiến: ${entry.challenge}

[2. HÀNH ĐỘNG (ACTION)]
- Công cụ & Kỹ thuật: ${entry.tools || "(Chưa nhập)"}
- Kết quả Thực tế & Minh chứng: ${entry.evidence}
- Mức độ làm chủ: ${entry.mastery || "(Chưa chọn)"}

[3. PHẢN TƯ (REFLECTION) & ĐÁNH GIÁ]
- Khoảng cách (Gap) & Nguyên nhân thử sai: ${entry.gap}
- Bài học chuyển hóa (Feed-forward): ${entry.feedforward}
- Cảm xúc & Tập trung: ${entry.emotion || "(Chưa chọn)"} | Trạng thái AAR: ${entry.status || "(Chưa chọn)"}

(File Excel AAR Tracker: ${filename} đã được tải về thiết bị để đính kèm cùng email này).

Trân trọng,
${entry.student_name}`;

  return { subject, bodyText };
}

function triggerBlobDownload(blobUrl, filename) {
  if (!blobUrl) return;
  const a = document.createElement("a");
  a.href = blobUrl;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
}

async function submitAARReport() {
  const entry = collectAARFormEntry(true);
  if (!entry) return;

  if (DOM.btnAarSubmitSend) DOM.btnAarSubmitSend.disabled = true;
  if (DOM.aarSubmitSpinner) DOM.aarSubmitSpinner.classList.remove("hidden");
  if (DOM.aarSubmitBtnText) DOM.aarSubmitBtnText.textContent = "Đang tạo Excel AAR & mở Email...";

  try {
    // 1. Persist entry & reset cross-test session tracker for the next study session
    App.aarLogs = [...(App.aarLogs || []), entry];
    App.lastAarReportAt = entry.created_at;
    if (App.sessionPracticedIds) App.sessionPracticedIds.clear();
    App.globalSessionItems = {};
    saveGlobalAARState();
    saveGlobalSessionTracker();

    const safeName = entry.student_name.replace(/\s+/g, "_").replace(/[^a-zA-Z0-9_\-À-ỹ]/g, "") || "Hoc_Sinh";
    const defaultFilename = `AAR_Cycle_Tracker_${safeName}_${entry.date_iso}.xlsx`;

    // 2. Optional local server dispatch (if running server.py)
    let serverData = null;
    try {
      const res = await fetch("/api/submit-aar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          student_name: entry.student_name,
          student_email: entry.student_email,
          entry,
          logs: App.aarLogs
        })
      });
      if (res.ok) serverData = await res.json();
    } catch (err) {}

    const filename = (serverData && serverData.filename) ? serverData.filename : defaultFilename;
    let fileBlobUrl = (serverData && serverData.download_url) ? serverData.download_url : null;
    if (!fileBlobUrl) {
      const clientBlob = await generateAARExcelBlob(App.aarLogs, entry.student_name, entry.student_email);
      if (clientBlob) fileBlobUrl = window.URL.createObjectURL(clientBlob);
    }

    // 3. Build Mailto link (To both teacher emails, CC student)
    const { subject, bodyText } = buildAAREmailPayload(entry, filename);
    const mailtoUrl = `mailto:${AAR_TEACHER_RECIPIENTS}?cc=${encodeURIComponent(entry.student_email)}&subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(bodyText)}`;
    App.lastMailtoUrl = mailtoUrl;
    App.lastReportText = bodyText;

    // 4. Download Excel & launch Mail client
    if (fileBlobUrl) triggerBlobDownload(fileBlobUrl, filename);
    setTimeout(() => {
      window.location.href = mailtoUrl;
    }, 550);

    // 5. Reset session inputs for the next AAR cycle & switch to Success Modal
    App.aarDraft = createEmptyAarDraft();
    saveGlobalAARDraft();
    if (DOM.aarInputGoal) DOM.aarInputGoal.value = "";
    if (DOM.aarInputChallenge) DOM.aarInputChallenge.value = "";
    if (DOM.aarInputTools) DOM.aarInputTools.value = "";
    if (DOM.aarSelectMastery) DOM.aarSelectMastery.value = "";
    if (DOM.aarInputGap) DOM.aarInputGap.value = "";
    if (DOM.aarInputFeedforward) DOM.aarInputFeedforward.value = "";
    if (DOM.aarSelectEmotion) DOM.aarSelectEmotion.value = "";
    if (DOM.aarSelectStatus) DOM.aarSelectStatus.value = "";
    syncAarAnticipationUI();

    closeAARModal();
    if (DOM.successModalTitle) DOM.successModalTitle.textContent = "Đã Tạo Báo Cáo ARR & Mở Email!";
    if (DOM.successStatusText) {
      DOM.successStatusText.textContent = `Hiệu suất buổi học (${entry.correct_count}/${entry.practiced_count} câu đúng - ${entry.accuracy_pct}%) và nội dung chu trình AAR đã được điền sẵn trong Email.`;
    }
    if (DOM.successRecipientText) {
      DOM.successRecipientText.innerHTML = `Bấm <strong>Gửi (Send)</strong> tới <code>v.sonpbh1@vinschool.edu.vn</code> &amp; <code>mikepham@baoan.ai.vn</code> (CC: <code>${escapeHtmlSafe(entry.student_email)}</code>) để hoàn tất!`;
    }
    if (DOM.successFilename) DOM.successFilename.textContent = filename;
    if (fileBlobUrl && DOM.btnDownloadSubmittedFile) {
      DOM.btnDownloadSubmittedFile.href = fileBlobUrl;
      DOM.btnDownloadSubmittedFile.setAttribute("download", filename);
    }
    if (DOM.modalSubmitSuccess) DOM.modalSubmitSuccess.classList.remove("hidden");
  } finally {
    if (DOM.btnAarSubmitSend) DOM.btnAarSubmitSend.disabled = false;
    if (DOM.aarSubmitSpinner) DOM.aarSubmitSpinner.classList.add("hidden");
    if (DOM.aarSubmitBtnText) DOM.aarSubmitBtnText.textContent = "📤 Lưu AAR, Tải Excel & Gửi Email ARR";
  }
}

async function downloadAARExcelOnly() {
  const entry = collectAARFormEntry(false);
  if (!entry) return;
  const exportRows = [...(App.aarLogs || []), entry];
  const safeName = entry.student_name.replace(/\s+/g, "_").replace(/[^a-zA-Z0-9_\-À-ỹ]/g, "") || "Hoc_Sinh";
  const filename = `AAR_Cycle_Tracker_${safeName}_${entry.date_iso}.xlsx`;
  const blob = await generateAARExcelBlob(exportRows, entry.student_name, entry.student_email);
  if (blob) {
    const url = window.URL.createObjectURL(blob);
    triggerBlobDownload(url, filename);
  }
}

async function exportAllAARHistoryExcel() {
  const logs = App.aarLogs || [];
  if (logs.length === 0) {
    alert("Chưa có nhật ký AAR nào được lưu trên thiết bị.");
    return;
  }
  const latest = logs[logs.length - 1];
  const name = App.studentState.student_name || latest.student_name || "Hoc_Sinh";
  const email = App.studentState.student_email || latest.student_email || "";
  const safeName = name.replace(/\s+/g, "_").replace(/[^a-zA-Z0-9_\-À-ỹ]/g, "") || "Hoc_Sinh";
  const blob = await generateAARExcelBlob(logs, name, email);
  if (blob) {
    const url = window.URL.createObjectURL(blob);
    triggerBlobDownload(url, `AAR_Cycle_Tracker_${safeName}_TongHop.xlsx`);
  }
}

function renderAARHistoryList() {
  const logs = App.aarLogs || [];
  if (DOM.aarHistorySummary) {
    if (logs.length === 0) {
      DOM.aarHistorySummary.textContent = "Chưa có buổi học AAR nào được lưu trên thiết bị này.";
    } else {
      const done = logs.filter(x => x.status === "Hoàn thành").length;
      const pct = Math.round((done / logs.length) * 100);
      DOM.aarHistorySummary.textContent = `Đã ghi nhận ${logs.length} buổi học • Hoàn thành chu trình AAR: ${done}/${logs.length} (${pct}%)`;
    }
  }
  if (!DOM.aarHistoryList) return;
  if (logs.length === 0) {
    DOM.aarHistoryList.innerHTML = `<div style="text-align:center;padding:24px;color:#64748b;font-size:13px;">Hãy hoàn thiện báo cáo ARR đầu tiên ở tab <strong>Báo Cáo Buổi Học Mới</strong> nhé!</div>`;
    return;
  }

  DOM.aarHistoryList.innerHTML = [...logs].reverse().map(item => `
    <div class="aar-history-card">
      <div class="aar-history-card-top">
        <div>
          <strong>${escapeHtmlSafe(item.session_label)}</strong> • ${escapeHtmlSafe(item.date_display)} • <span style="color:#1e3a8a;font-weight:700;">${escapeHtmlSafe(item.sat_module)}</span>
        </div>
        <span class="aar-history-badge">${escapeHtmlSafe(item.status || "Chưa chọn trạng thái")} • Đúng ${item.correct_count}/${item.practiced_count} (${item.accuracy_pct}%)</span>
      </div>
      <div class="aar-history-meta">
        <div><strong>Minh chứng:</strong> ${escapeHtmlSafe(item.evidence)}</div>
        <div><strong>Gap:</strong> ${escapeHtmlSafe(item.gap)}</div>
        <div><strong>Feed-forward:</strong> ${escapeHtmlSafe(item.feedforward)}</div>
      </div>
    </div>
  `).join("");
}
