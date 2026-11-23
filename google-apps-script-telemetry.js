/**
 * =========================================================================
 * VINSCHOOL SAT TEAM - REAL-TIME TELEMETRY & LIVE TRACKER
 * Target Google Sheet: Vinschool SAT Team - Live Telemetry
 * Doc ID: 1ETvQI-xd8HUJlpI4xEO_SV8o2mjqkDckPFMKLhynquE
 * Tác giả: Thầy Mike Pham & Antigravity AI
 * =========================================================================
 * 
 * HƯỚNG DẪN KÍCH HOẠT (CHỈ CẦN LÀM 1 LẦN DUY NHẤT):
 * 1. Mở file Google Sheet:
 *    https://docs.google.com/spreadsheets/d/1ETvQI-xd8HUJlpI4xEO_SV8o2mjqkDckPFMKLhynquE/edit
 * 2. Vào menu: Tiện ích mở rộng (Extensions) -> Apps Script.
 * 3. Xóa toàn bộ nội dung trong Code.gs, dán toàn bộ đoạn mã này vào.
 * 4. Bấm biểu tượng 💾 Lưu (Ctrl + S hoặc Cmd + S).
 * 5. Bấm nút "Triển khai" (Deploy) màu xanh ở góc trên bên phải -> "Quản lý bản triển khai mới" (New deployment).
 * 6. Chọn loại (bánh răng): "Ứng dụng web" (Web app).
 *    - Mô tả: Vinschool SAT Live Telemetry v1
 *    - Thực thi dưới dạng (Execute as): "Tôi" (My account - mikepham358@gmail.com)
 *    - Ai có quyền truy cập (Who has access): "Bất kỳ ai" (Anyone) -> RẤT QUAN TRỌNG ĐỂ GITHUB PAGES GỬI ĐƯỢC DỮ LIỆU
 * 7. Bấm "Triển khai", cấp quyền truy cập tài khoản Google.
 * 8. Sao chép "URL Ứng dụng web" (dạng https://script.google.com/macros/s/AKfycb.../exec)
 *    và dán vào cài đặt Telemetry trên Web App.
 */

var SHEET_NAME = "Live_Telemetry";

function setupSheetHeaders(sheet) {
  if (sheet.getLastRow() === 0) {
    var headers = [
      "Thời Gian (VN)",
      "Mã Phiên (Session ID)",
      "Họ Và Tên Học Sinh",
      "Email Học Sinh",
      "Mục Tiêu Điểm",
      "Bộ Đề (Test ID)",
      "Module",
      "Câu Số",
      "Loại Tương Tác (Event)",
      "Kết Quả / Trạng Thái",
      "Chi Tiết Hành Động (Details)",
      "Thời Gian Làm (Giây)",
      "Thiết Bị / Trình Duyệt"
    ];
    sheet.appendRow(headers);
    
    // Format Header Row
    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#1a73e8"); // Google Blue
    headerRange.setFontColor("#ffffff");
    headerRange.setFontWeight("bold");
    headerRange.setHorizontalAlignment("center");
    headerRange.setFontSize(10.5);
    
    // Freeze Top Row
    sheet.setFrozenRows(1);
    
    // Auto column widths
    sheet.setColumnWidth(1, 160); // Timestamp
    sheet.setColumnWidth(2, 160); // Session ID
    sheet.setColumnWidth(3, 180); // Student Name
    sheet.setColumnWidth(4, 210); // Email
    sheet.setColumnWidth(5, 120); // Target
    sheet.setColumnWidth(6, 150); // Test ID
    sheet.setColumnWidth(7, 130); // Module
    sheet.setColumnWidth(8, 100); // Question #
    sheet.setColumnWidth(9, 160); // Event Type
    sheet.setColumnWidth(10, 160); // Result
    sheet.setColumnWidth(11, 350); // Details
    sheet.setColumnWidth(12, 130); // Duration
    sheet.setColumnWidth(13, 160); // Device
  }
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  // Khóa 10s để đảm bảo an toàn đồng thời khi nhiều học sinh nộp bài cùng 1 tích tắc
  try {
    lock.waitLock(10000);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Server busy, lock timeout" }))
      .setMimeType(ContentService.MimeType.JSON);
  }

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
    }
    setupSheetHeaders(sheet);

    var data = {};
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (jsonErr) {
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    // Định dạng thời gian theo múi giờ Việt Nam (UTC+7)
    var timestampStr = Utilities.formatDate(new Date(), "Asia/Ho_Chi_Minh", "yyyy-MM-dd HH:mm:ss");

    var detailsStr = "";
    if (typeof data.details === "object") {
      detailsStr = JSON.stringify(data.details);
    } else if (data.details !== undefined && data.details !== null) {
      detailsStr = String(data.details);
    }

    var resultStr = data.result || "";
    if (!resultStr && data.event_type === "ANSWER_CHECK") {
      if (data.details && typeof data.details === "object") {
        var isCorr = data.details.correct;
        var att = data.details.attempt_num || 1;
        resultStr = isCorr ? ("ĐÚNG (Lần " + att + ")") : ("CHƯA ĐÚNG (Lần " + att + ")");
      }
    }

    var rowData = [
      timestampStr,
      data.session_id || "ANON",
      data.student_name || "Ẩn danh",
      data.student_email || "",
      data.target_score || "",
      data.test_id || "",
      data.module || "",
      data.question_number || "",
      data.event_type || "INTERACTION",
      resultStr,
      detailsStr,
      data.duration_seconds || 0,
      data.device || ""
    ];

    sheet.appendRow(rowData);
    var newRow = sheet.getLastRow();

    // Định dạng màu nhẹ cho cột Kết Quả để Thầy dễ nhìn
    if (resultStr.indexOf("ĐÚNG") !== -1 && resultStr.indexOf("CHƯA ĐÚNG") === -1) {
      sheet.getRange(newRow, 10).setBackground("#e6f4ea").setFontColor("#137333").setFontWeight("bold");
    } else if (resultStr.indexOf("CHƯA ĐÚNG") !== -1) {
      sheet.getRange(newRow, 10).setBackground("#fce8e6").setFontColor("#c5221f").setFontWeight("bold");
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      row: newRow,
      timestamp: timestampStr
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);

  } finally {
    lock.releaseLock();
  }
}

function doGet(e) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  var count = sheet ? Math.max(0, sheet.getLastRow() - 1) : 0;
  return ContentService.createTextOutput("✅ Vinschool SAT Live Telemetry is ACTIVE! Total recorded events: " + count);
}
