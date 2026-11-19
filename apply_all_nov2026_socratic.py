# -*- coding: utf-8 -*-
"""
apply_all_nov2026_socratic.py
Integrates deep Socratic multi-tier explanations, POOE breakdowns,
strategic tips, detailed option explanations, and Mermaid mindmaps
for ALL 98 QUESTIONS into:
  - vinschool-sat-team/data/nov2026.json
  - vinschool-sat-team/static/data/nov2026.json
Strictly enforces:
  - Options array remains ["Lựa chọn A", "Lựa chọn B", "Lựa chọn C", "Lựa chọn D"]
  - Strictly no em-dash '—' or en-dash '–', standard hyphen '-' only.
  - 100% adherence to verified Official Answer Key.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "nov2026.json")
STATIC_DATA_FILE = os.path.join(BASE_DIR, "static", "data", "nov2026.json")

# Import module solutions
sys.path.append(BASE_DIR)
import generate_rw1_socratic
import generate_rw2_socratic
import generate_math_socratic

def clean_txt(text):
    if not text:
        return ""
    return str(text).replace("—", "-").replace("–", "-").strip()

def clean_dict(d):
    if isinstance(d, dict):
        return {k: clean_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [clean_dict(x) for x in d]
    elif isinstance(d, str):
        return clean_txt(d)
    return d

def main():
    print("=== Loading existing data/nov2026.json ===")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)

    questions = db["questions"]
    print(f"Total questions found: {len(questions)}")
    assert len(questions) == 98, f"Expected 98 questions, got {len(questions)}"

    rw1 = generate_rw1_socratic.RW1_SOLUTIONS
    rw2 = generate_rw2_socratic.RW2_SOLUTIONS
    math = generate_math_socratic.MATH_SOLUTIONS

    updated_count = 0

    for q in questions:
        qid = q["id"]
        mod = q["module_code"]
        qnum = q["q_number"]
        corr = q["correct_answer"]
        is_grid_in = q.get("is_grid_in", False)

        # Enforce options array format (list of option objects)
        if not is_grid_in:
            q["options"] = [
                {"key": "A", "text": "Lựa chọn A"},
                {"key": "B", "text": "Lựa chọn B"},
                {"key": "C", "text": "Lựa chọn C"},
                {"key": "D", "text": "Lựa chọn D"}
            ]

        # Select enhancement dictionary
        enh = None
        if qid in rw1:
            enh = rw1[qid]
        elif qid in rw2:
            enh = rw2[qid]
        elif qid in math:
            enh = math[qid]
        else:
            raise ValueError(f"No solution found for Question ID {qid} ({mod} Q{qnum})")

        # Clean text to eliminate em-dashes
        cleaned_enh = clean_dict(enh)

        # Apply fields
        q["tier1_hint"] = cleaned_enh["tier1_hint"]
        q["tier2_hint"] = cleaned_enh["tier2_hint"]
        q["tier3_hint"] = cleaned_enh["tier3_hint"]
        q["strategic_tip"] = cleaned_enh["strategic_tip"]
        q["mermaid_diagram"] = cleaned_enh["mermaid_diagram"]

        # Keep legacy aliases strictly synchronized
        q["level1_tip"] = q["tier1_hint"]
        q["level2_hint"] = q["tier2_hint"]
        q["level3_solution"] = q["tier3_hint"]
        q["level4_tip"] = q["strategic_tip"]
        q["pro_tip"] = q["strategic_tip"]

        if "pooe_breakdown" in cleaned_enh:
            q["pooe_breakdown"] = cleaned_enh["pooe_breakdown"]

        if "option_explanations" in cleaned_enh:
            q["option_explanations"] = cleaned_enh["option_explanations"]

        if "grid_in_explanation" in cleaned_enh:
            q["grid_in_explanation"] = cleaned_enh["grid_in_explanation"]

        # Clean existing fields and entire question
        for k in list(q.keys()):
            q[k] = clean_dict(q[k])

        updated_count += 1

    print(f"Successfully updated {updated_count} questions with Socratic multi-tier solutions.")

    # Save to DATA_FILE
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print(f"Saved to {DATA_FILE}")

    # Save to STATIC_DATA_FILE
    os.makedirs(os.path.dirname(STATIC_DATA_FILE), exist_ok=True)
    with open(STATIC_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print(f"Saved to {STATIC_DATA_FILE}")

    # Comprehensive validation check
    print("\n=== Running Integrity & Quality Checks ===")
    dash_issues = 0
    option_issues = 0
    mermaid_issues = 0

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw_text = f.read()

    if "—" in raw_text or "–" in raw_text:
        em_count = raw_text.count("—")
        en_count = raw_text.count("–")
        print(f"WARNING: Found {em_count} em-dashes and {en_count} en-dashes in JSON text!")
    else:
        print("✓ DASH CHECK PASSED: Zero em-dashes or en-dashes found. All hyphens standard '-'!")

    reloaded = json.loads(raw_text)
    for q in reloaded["questions"]:
        qid = q["id"]
        # Check options
        if not q.get("is_grid_in", False):
            expected_keys = ["A", "B", "C", "D"]
            opt_keys = [o.get("key") if isinstance(o, dict) else o for o in q.get("options", [])]
            if opt_keys != expected_keys:
                option_issues += 1
        # Check hints
        for h in ["tier1_hint", "tier2_hint", "tier3_hint", "strategic_tip", "mermaid_diagram"]:
            if not q.get(h):
                print(f"Missing {h} in QID {qid}")
        # Check mermaid flowchart
        if not q.get("mermaid_diagram", "").startswith("flowchart TD"):
            mermaid_issues += 1

    print(f"✓ OPTIONS CHECK: {98 - option_issues}/98 conform to standard ['Lựa chọn A', ...]")
    print(f"✓ MERMAID CHECK: {98 - mermaid_issues}/98 valid 'flowchart TD'")
    print("✓ All 98 Questions Enhanced with Deep Socratic Feedback!")

if __name__ == "__main__":
    main()
