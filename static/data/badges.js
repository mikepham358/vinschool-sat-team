window.BADGES_DEFINITIONS = [
  {
    "id": "trap_slayer",
    "category": "socratic",
    "category_name": "Socratic & Error Analysis",
    "title": "Trap Slayer",
    "icon": "🛡️",
    "description": "Proactively record test traps and root causes into your Socratic Error Log.",
    "quote": "A mistake is not a failure - it is the most valuable data point for exponential growth.",
    "criteria_type": "COUNT_ERROR_LOGS",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Apprentice",
        "target": 3,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Veteran",
        "target": 10,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Master",
        "target": 25,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Legend",
        "target": 50,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "trap_eliminator",
    "category": "socratic",
    "category_name": "Socratic & Error Analysis",
    "title": "Trap Eliminator",
    "icon": "🎯",
    "description": "Re-examine logged errors and elevate traps to 'Eliminated' status.",
    "quote": "An eliminated trap is guaranteed points preserved on official test day.",
    "criteria_type": "COUNT_RESOLVED_LOGS",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Initiate",
        "target": 2,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Tactician",
        "target": 8,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Strategist",
        "target": 20,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Grandmaster",
        "target": 40,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "socratic_inquirer",
    "category": "socratic",
    "category_name": "Socratic & Error Analysis",
    "title": "Socratic Thinker",
    "icon": "💡",
    "description": "Solve challenging questions correctly after consulting Tier 1 or Tier 2 Socratic hints.",
    "quote": "Hints are cognitive levers - self-directed reasoning is the key that unlocks mastery.",
    "criteria_type": "HINT_CORRECT_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Seeker",
        "target": 3,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Insightful",
        "target": 10,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Enlightened",
        "target": 25,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Philosopher",
        "target": 50,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "first_hit_sniper",
    "category": "mastery",
    "category_name": "SAT Mastery",
    "title": "First-Strike Sniper",
    "icon": "⚡",
    "description": "Answer correctly on the very first attempt without needing re-tries.",
    "quote": "Laser focus from the opening second separates 1500+ top scorers from the rest.",
    "criteria_type": "FIRST_TRY_CORRECT_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Sharpshooter",
        "target": 15,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Marksman",
        "target": 40,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Deadeye",
        "target": 80,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Apex Predator",
        "target": 150,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "desmos_wizard",
    "category": "mastery",
    "category_name": "SAT Mastery",
    "title": "Desmos Wizard",
    "icon": "📈",
    "description": "Harness the Desmos graphing calculator to rapidly solve complex SAT math problems.",
    "quote": "Transform cumbersome algebra into visual clarity in a matter of keystrokes.",
    "criteria_type": "DESMOS_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Cadet",
        "target": 5,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Graphing Adept",
        "target": 15,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Visual Prodigy",
        "target": 35,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Desmos Sorcerer",
        "target": 70,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "reading_analyst",
    "category": "mastery",
    "category_name": "SAT Mastery",
    "title": "Passage Analyst",
    "icon": "🔍",
    "description": "Conquer advanced Reading & Writing questions with high-yield textual analysis.",
    "quote": "Read between the lines - decode authorial intent and rhetorical architecture.",
    "criteria_type": "RW_CORRECT_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Discerning",
        "target": 15,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Perceptive",
        "target": 35,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Scholarly",
        "target": 70,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Literary Scholar",
        "target": 120,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "learning_streak",
    "category": "persistence",
    "category_name": "Persistence & AAR",
    "title": "Relentless Consistency",
    "icon": "🔥",
    "description": "Sustain deliberate practice across multiple study sessions.",
    "quote": "Daily disciplined consistency outlasts raw talent without routine every single time.",
    "criteria_type": "SESSION_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Kickstart",
        "target": 2,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Disciplined",
        "target": 5,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Iron Will",
        "target": 10,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Unstoppable",
        "target": 20,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "aar_discipline",
    "category": "persistence",
    "category_name": "Persistence & AAR",
    "title": "Metacognitive Master",
    "icon": "📝",
    "description": "Complete full 3-phase After Action Reviews: Anticipation, Action, and Reflection.",
    "quote": "Learning without reflection is blind; reflection after action produces genuine wisdom.",
    "criteria_type": "AAR_COMPLETED_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Reflective",
        "target": 1,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Synthesizer",
        "target": 3,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Practitioner",
        "target": 7,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Metacognitive Sage",
        "target": 15,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "target_achiever",
    "category": "persistence",
    "category_name": "Persistence & AAR",
    "title": "Goal Crusher",
    "icon": "👑",
    "description": "Attain high-yield accuracy aligned with committed target scores (1300+, 1400+, 1500+).",
    "quote": "You turned ambition into reality through deliberate grit and steadfast execution.",
    "criteria_type": "TARGET_ACHIEVED_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "1300+ Breakthrough",
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
        "name": "Valedictorian",
        "target": 8,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "lexical_hunter",
    "category": "tools",
    "category_name": "Vocabulary & Tools",
    "title": "Lexical Hunter",
    "icon": "📖",
    "description": "Curate academic SAT vocabulary with contextual definitions in your Socratic Notebook.",
    "quote": "A rich vocabulary is the ultimate passport to unlocking top-tier Reading & Writing scores.",
    "criteria_type": "VOCAB_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Word Seeker",
        "target": 5,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Etymologist",
        "target": 15,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Walking Lexicon",
        "target": 35,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Master of Words",
        "target": 70,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "dictionary_scholar",
    "category": "tools",
    "category_name": "Vocabulary & Tools",
    "title": "Cambridge Scholar",
    "icon": "🏛️",
    "description": "Leverage Cambridge Dictionary lookups to master nuanced definitions in real test contexts.",
    "quote": "True contextual grasp eliminates false-cognate and synonym traps with 100% precision.",
    "criteria_type": "DICT_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Inquisitive",
        "target": 5,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Deep Diver",
        "target": 15,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Lexicographer",
        "target": 35,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Cambridge Fellow",
        "target": 70,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  },
  {
    "id": "whiteboard_master",
    "category": "tools",
    "category_name": "Vocabulary & Tools",
    "title": "Scratchpad Architect",
    "icon": "✏️",
    "description": "Utilize the Socratic Scratchpad whiteboard to diagram, reason, and solve visually.",
    "quote": "Drawing a diagram is the first decisive step to simplifying any complex problem.",
    "criteria_type": "SCRATCHPAD_COUNT",
    "tiers": [
      {
        "level": 1,
        "tier": "bronze",
        "name": "Sketcher",
        "target": 3,
        "color": "#b45309",
        "bg": "#fef3c7"
      },
      {
        "level": 2,
        "tier": "silver",
        "name": "Visualizer",
        "target": 10,
        "color": "#475569",
        "bg": "#f1f5f9"
      },
      {
        "level": 3,
        "tier": "gold",
        "name": "Draftsman",
        "target": 25,
        "color": "#d97706",
        "bg": "#fffbeb"
      },
      {
        "level": 4,
        "tier": "diamond",
        "name": "Visual Architect",
        "target": 50,
        "color": "#0284c7",
        "bg": "#f0f9ff"
      }
    ]
  }
];
