/**
 * =========================================================================
 * VINSCHOOL SAT TEAM - REAL-TIME TELEMETRY & GOOGLE SHEETS TRACKER
 * Target Google Sheet: Vinschool SAT Team - Live Telemetry
 * Doc ID: 1ETvQI-xd8HUJlpI4xEO_SV8o2mjqkDckPFMKLhynquE
 * Sheet URL: https://docs.google.com/spreadsheets/d/1ETvQI-xd8HUJlpI4xEO_SV8o2mjqkDckPFMKLhynquE/edit
 * Tác giả: Thầy Mike Pham & Antigravity AI
 * =========================================================================
 */
(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.SATTracker = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {

  const DEFAULT_TELEMETRY_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbx9XhNqKw2Hf4qrtdQkBFB9hFlyyZoaySrSTPX_Y1DkN-Mr1EA_CvMPl7lXZw-tUkfr/exec";
  const STORAGE_KEY_WEBHOOK = "vinschool_sat_telemetry_webhook_url";
  const STORAGE_KEY_SESSION = "vinschool_sat_telemetry_session_id";
  const TARGET_SHEET_ID = "1ETvQI-xd8HUJlpI4xEO_SV8o2mjqkDckPFMKLhynquE";
  const TARGET_SHEET_URL = "https://docs.google.com/spreadsheets/d/1ETvQI-xd8HUJlpI4xEO_SV8o2mjqkDckPFMKLhynquE/edit?gid=473216962#gid=473216962";

  // Generate or retrieve persistent Session ID for this tab session
  function getSessionId() {
    let sid = null;
    try {
      sid = sessionStorage.getItem(STORAGE_KEY_SESSION);
      if (!sid) {
        sid = "SAT_" + Date.now().toString(36).toUpperCase() + "_" + Math.random().toString(36).substring(2, 6).toUpperCase();
        sessionStorage.setItem(STORAGE_KEY_SESSION, sid);
      }
    } catch (e) {
      sid = "SAT_SESSION";
    }
    return sid;
  }

  function getWebhookUrl() {
    try {
      return localStorage.getItem(STORAGE_KEY_WEBHOOK) || DEFAULT_TELEMETRY_WEBHOOK_URL;
    } catch (e) {
      return DEFAULT_TELEMETRY_WEBHOOK_URL;
    }
  }

  function setWebhookUrl(url) {
    try {
      if (url && typeof url === "string") {
        localStorage.setItem(STORAGE_KEY_WEBHOOK, url.trim());
      } else {
        localStorage.removeItem(STORAGE_KEY_WEBHOOK);
      }
    } catch (e) {}
  }

  function getDeviceInfo() {
    try {
      const ua = navigator.userAgent || "";
      let os = "Desktop";
      if (/iPad|iPhone|iPod/.test(ua)) os = "iOS";
      else if (/Android/.test(ua)) os = "Android";
      else if (/Macintosh|Mac OS X/.test(ua)) os = "macOS";
      else if (/Windows NT/.test(ua)) os = "Windows";

      let browser = "Browser";
      if (/Chrome|CriOS/.test(ua) && !/Edg/.test(ua)) browser = "Chrome";
      else if (/Safari/.test(ua) && !/Chrome/.test(ua)) browser = "Safari";
      else if (/Firefox/.test(ua)) browser = "Firefox";
      else if (/Edg/.test(ua)) browser = "Edge";

      return `${os} • ${browser}`;
    } catch (e) {
      return "Web Client";
    }
  }

  // Per-Question Stopwatch Engine
  const questionTimers = {};
  let currentActiveQuestionId = null;

  function startQuestionTimer(qid) {
    if (!qid) return;
    currentActiveQuestionId = String(qid);
    if (!questionTimers[currentActiveQuestionId]) {
      questionTimers[currentActiveQuestionId] = {
        start: Date.now(),
        lastAttempt: Date.now()
      };
    } else {
      questionTimers[currentActiveQuestionId].lastAttempt = Date.now();
    }
  }

  function getQuestionDuration(qid) {
    const id = String(qid || currentActiveQuestionId || "");
    if (!id || !questionTimers[id]) return 0;
    const now = Date.now();
    const elapsed = Math.max(1, Math.round((now - (questionTimers[id].lastAttempt || questionTimers[id].start)) / 1000));
    questionTimers[id].lastAttempt = now;
    return elapsed;
  }

  /**
   * Main telemetry track function
   * Non-blocking, failsafe, sends via sendBeacon or fetch(no-cors)
   * 100% silent background tracking for all users
   */
  function track(eventType, details = {}, extra = {}) {
    const webhookUrl = getWebhookUrl();
    const app = window.App || {};
    const studentState = app.studentState || {};
    const q = extra.question || app.currentQuestion || {};

    let durationSeconds = 0;
    if (typeof extra.duration === "number" && extra.duration > 0) {
      durationSeconds = Math.round(extra.duration);
    } else if (eventType === "ANSWER_CHECK") {
      durationSeconds = getQuestionDuration(q.id);
      if (!durationSeconds && app.currentQuestionStartTime) {
        durationSeconds = Math.max(1, Math.round((Date.now() - app.currentQuestionStartTime) / 1000));
      }
    }

    const payload = {
      sheet_id: TARGET_SHEET_ID,
      session_id: getSessionId(),
      timestamp: new Date().toISOString(),
      student_name: studentState.student_name || (window.DOM && window.DOM.homeInputName ? window.DOM.homeInputName.value.trim() : "") || (window.App && window.App.studentState ? window.App.studentState.student_name : "") || "Khách (Chưa nhập tên)",
      student_email: studentState.student_email || (window.DOM && window.DOM.homeInputEmail ? window.DOM.homeInputEmail.value.trim() : "") || (window.App && window.App.studentState ? window.App.studentState.student_email : "") || "Chưa có email",
      target_score: studentState.student_target || (window.App && window.App.studentState ? window.App.studentState.student_target : "") || "",
      test_id: app.activeTestId || "oct-2026",
      module: q.module || q.module_code || app.activeModuleCode || "",
      question_number: q.q_label || (q.id ? `Câu ${q.q_number || q.id}` : ""),
      event_type: eventType,
      result: extra.result || "",
      details: typeof details === "object" ? JSON.stringify(details) : String(details),
      duration_seconds: durationSeconds,
      device: getDeviceInfo()
    };

    if (!webhookUrl) return false;

    try {
      const blob = new Blob([JSON.stringify(payload)], { type: "text/plain;charset=UTF-8" });
      if (navigator.sendBeacon) {
        return navigator.sendBeacon(webhookUrl, blob);
      } else {
        fetch(webhookUrl, {
          method: "POST",
          mode: "no-cors",
          body: blob
        }).catch(() => {});
        return true;
      }
    } catch (err) {
      return false;
    }
  }

  /**
   * Test connection ping to verify Google Apps Script Webhook
   */
  async function testPing(customUrl) {
    const url = customUrl || getWebhookUrl();
    if (!url) {
      return { success: false, message: "Chưa cấu hình URL Webhook Google Apps Script!" };
    }

    const payload = {
      sheet_id: TARGET_SHEET_ID,
      session_id: getSessionId(),
      timestamp: new Date().toISOString(),
      student_name: "Thầy Mike Pham (Admin Test)",
      student_email: "mikepham358@gmail.com",
      target_score: "1600 (Mastery)",
      test_id: "system-test",
      module: "Live-Check",
      question_number: "Ping #1",
      event_type: "SYSTEM_PING",
      result: "CONNECTED ✅",
      details: JSON.stringify({ message: "Test telemetry ping to Google Sheet successfully verified!" }),
      duration_seconds: 0,
      device: getDeviceInfo()
    };

    try {
      const blob = new Blob([JSON.stringify(payload)], { type: "text/plain;charset=UTF-8" });
      if (navigator.sendBeacon) {
        navigator.sendBeacon(url, blob);
      } else {
        await fetch(url, {
          method: "POST",
          mode: "no-cors",
          body: blob
        });
      }
      return {
        success: true,
        message: "✅ Đã gửi tín hiệu Test thành công! Vui lòng kiểm tra dòng mới nhất trên Google Sheet."
      };
    } catch (e) {
      return {
        success: false,
        message: "❌ Không thể kết nối tới Webhook: " + (e.message || String(e))
      };
    }
  }

  // Auto-track initial page view
  if (typeof window !== "undefined") {
    window.addEventListener("DOMContentLoaded", () => {
      setTimeout(() => {
        track("PAGE_VIEW", {
          href: window.location.href,
          referrer: document.referrer || "Direct",
          screen_width: window.innerWidth,
          screen_height: window.innerHeight
        });
      }, 500);
    });
  }

  return {
    track: track,
    testPing: testPing,
    getWebhookUrl: getWebhookUrl,
    setWebhookUrl: setWebhookUrl,
    getSessionId: getSessionId,
    startQuestionTimer: startQuestionTimer,
    getQuestionDuration: getQuestionDuration,
    TARGET_SHEET_ID: TARGET_SHEET_ID,
    TARGET_SHEET_URL: TARGET_SHEET_URL
  };
}));
