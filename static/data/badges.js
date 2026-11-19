window.BADGES_DEFINITIONS = [
  {
    "id": "trap_slayer",
    "category": "socratic",
    "category_name": "Socratic & Thử Sai",
    "title": "Dũng Sĩ Thử Sai",
    "icon": "🛡️",
    "description": "Chủ động ghi chép bẫy đề thi và phân tích nguyên nhân vào Sổ Thử Sai",
    "quote": "Sai lầm không phải là thất bại - nó là dữ liệu quý giá nhất để em tiến bộ vượt bậc.",
    "criteria_type": "COUNT_ERROR_LOGS",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Tập Sự",
        "target": 3,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Thiện Chiến",
        "target": 10,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Bậc Thầy",
        "target": 25,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Huyền Thoại",
        "target": 50,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "trap_eliminator",
    "category": "socratic",
    "category_name": "Socratic & Thử Sai",
    "title": "Sát Thủ Triệt Tiêu",
    "icon": "🎯",
    "description": "Nghiên cứu lại câu hỏi và chuyển trạng thái bẫy thành Đã Triệt Tiêu",
    "quote": "Một cái bẫy đã triệt tiêu là một điểm số chắc chắn được bảo toàn trong phòng thi thật.",
    "criteria_type": "COUNT_RESOLVED_LOGS",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Tập Sự",
        "target": 2,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Thiện Chiến",
        "target": 8,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Bậc Thầy",
        "target": 20,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Huyền Thoại",
        "target": 40,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "socratic_inquirer",
    "category": "socratic",
    "category_name": "Socratic & Thử Sai",
    "title": "Tự Lực Cánh Sinh",
    "icon": "💡",
    "description": "Giải đúng câu hỏi sau khi đọc gợi ý Socratic tầng 1 hoặc tầng 2",
    "quote": "Gợi ý là đòn bẩy tư duy - trí tuệ tự thân là chiếc chìa khóa mở cánh cửa tri thức.",
    "criteria_type": "HINT_CORRECT_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Khởi Đầu",
        "target": 3,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Sâu Sắc",
        "target": 10,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Khai Sáng",
        "target": 25,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Đại Triết Gia",
        "target": 50,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "first_hit_sniper",
    "category": "mastery",
    "category_name": "Kỹ Năng SAT",
    "title": "Xạ Thủ Vòng 1",
    "icon": "⚡",
    "description": "Bắn tỉa chính xác ngay ở lần làm đầu tiên (Attempt 1) không cần thử lại",
    "quote": "Tập trung cao độ từ giây đầu tiên tạo nên sự khác biệt của những thủ khoa 1500+.",
    "criteria_type": "FIRST_TRY_CORRECT_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Chuẩn Xác",
        "target": 15,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Cao Thủ",
        "target": 40,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Thiện Xạ",
        "target": 80,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Bách Phát Bách Trúng",
        "target": 150,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "desmos_wizard",
    "category": "mastery",
    "category_name": "Kỹ Năng SAT",
    "title": "Phù Thủy Desmos",
    "icon": "📈",
    "description": "Khai thác công cụ đồ thị Desmos để giải quyết các bài toán SAT nhanh chóng",
    "quote": "Biến đại số phức tạp thành đồ thị trực quan chỉ trong vài giây thao tác.",
    "criteria_type": "DESMOS_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Làm Quen",
        "target": 5,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Thành Thạo",
        "target": 15,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Bậc Thầy",
        "target": 35,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Phù Thủy Đồ Thị",
        "target": 70,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "reading_analyst",
    "category": "mastery",
    "category_name": "Kỹ Năng SAT",
    "title": "Bậc Thầy Đọc Hiểu",
    "icon": "🔍",
    "description": "Chinh phục chính xác các câu hỏi Reading & Writing khó",
    "quote": "Đọc sâu giữa các dòng chữ - thấu suốt dụng ý của tác giả và cấu trúc lập luận.",
    "criteria_type": "RW_CORRECT_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Tinh Tường",
        "target": 15,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Sắc Bén",
        "target": 35,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Uyên Bác",
        "target": 70,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Học Giả Đọc Hiểu",
        "target": 120,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "learning_streak",
    "category": "persistence",
    "category_name": "Kỷ Luật & AAR",
    "title": "Chiến Hạm Bền Bỉ",
    "icon": "🔥",
    "description": "Duy trì rèn luyện qua nhiều buổi học khác nhau trên hệ thống",
    "quote": "Sự kiên trì đều đặn mỗi ngày đánh bại mọi tài năng thiên bẩm nhưng thiếu kỷ luật.",
    "criteria_type": "SESSION_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Khởi Động",
        "target": 2,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Kỷ Luật",
        "target": 5,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Ý Chí Thép",
        "target": 10,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Huyền Thoại Bất Bại",
        "target": 20,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "aar_discipline",
    "category": "persistence",
    "category_name": "Kỷ Luật & AAR",
    "title": "Kỷ Luật Chu Trình AAR",
    "icon": "📝",
    "description": "Hoàn tất chu trình AAR 3 giai đoạn: Dự đoán - Thực chiến - Phản tư đúc kết",
    "quote": "Học mà không phản tư thì mù quáng; phản tư sâu sắc sau hành động mới sinh ra trí tuệ.",
    "criteria_type": "AAR_COMPLETED_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Ghi Nhận",
        "target": 1,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Đúc Kết",
        "target": 3,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Chuyên Gia",
        "target": 7,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Đại Sư Siêu Nhận Thức",
        "target": 15,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "target_achiever",
    "category": "persistence",
    "category_name": "Kỷ Luật & AAR",
    "title": "Chinh Phục Mục Tiêu",
    "icon": "👑",
    "description": "Đạt tỷ lệ làm bài xuất sắc phù hợp với mục tiêu điểm số kỳ vọng đã cam kết",
    "quote": "Em đã biến cam kết ban đầu thành hiện thực bằng chính ý chí và nỗ lực của mình!",
    "criteria_type": "TARGET_ACHIEVED_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "1300+ Đột Phá",
        "target": 1,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "1400+ Top 50",
        "target": 2,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "1500+ Ivy League",
        "target": 4,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Thủ Khoa Đỉnh Cao",
        "target": 8,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "lexical_hunter",
    "category": "tools",
    "category_name": "Từ Vựng & Công Cụ",
    "title": "Thợ Săn Từ Vựng",
    "icon": "📖",
    "description": "Lưu trữ từ vựng SAT học thuật kèm định nghĩa và ngữ cảnh vào Sổ Thử Sai",
    "quote": "Vốn từ vựng phong phú là chìa khóa mở toang cánh cửa Reading & Writing điểm cao.",
    "criteria_type": "VOCAB_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Nhập Môn",
        "target": 5,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Uyên Thâm",
        "target": 15,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Từ Điển Sống",
        "target": 35,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Đại Sư Ngôn Ngữ",
        "target": 70,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "dictionary_scholar",
    "category": "tools",
    "category_name": "Từ Vựng & Công Cụ",
    "title": "Học Giả Cambridge",
    "icon": "🏛️",
    "description": "Sử dụng từ điển Cambridge tra cứu nghĩa gốc và ngữ cảnh trong lúc luyện đề",
    "quote": "Hiểu đúng nghĩa gốc trong văn cảnh giúp loại trừ 100% bẫy đồng nghĩa giả mạo.",
    "criteria_type": "DICT_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Hiếu Học",
        "target": 5,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Đào Sâu",
        "target": 15,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Học Giả",
        "target": 35,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Viện Sĩ Ngôn Ngữ",
        "target": 70,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "whiteboard_master",
    "category": "tools",
    "category_name": "Từ Vựng & Công Cụ",
    "title": "Bậc Thầy Nháp Socratic",
    "icon": "✏️",
    "description": "Sử dụng bảng vẽ nháp tay Scratchpad để phân tích và lập luận tư duy",
    "quote": "Đặt bút vẽ sơ đồ là bước đầu tiên để trực quan hóa và làm chủ bài toán phức tạp.",
    "criteria_type": "SCRATCHPAD_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Phác Thảo",
        "target": 3,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Sơ Đồ Hóa",
        "target": 10,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Đại Sư Nháp",
        "target": 25,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Bậc Thầy Trực Quan",
        "target": 50,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  }
];
