# Evals and LLM-as-Judge: Production Quality Pipeline

A 90-minute course and hands-on build-along designed to help AI engineers move beyond "vibe checks" by building reliable evaluation suites and calculating objective judge metrics.

---

## 📌 Course Overview

- **Lesson 1: Framing Quality and Building Ground Truth**
  - Moving from intuition to discrete binary criteria (Pass=1, Fail=0).
  - Building a standardized dataset schema (`test_cases.json`).
- **Lesson 2: Constructing the LLM Judge & Metric Engine**
  - Designing structured JSON judge prompts using zero-shot chain-of-thought reasoning.
  - Computing True/False Positives, Precision, Recall, and $F_1$ scores against ground-truth baselines.

---

## 🛠️ Project Structure

```text
.
├── README.md           # Course overview and quickstart guide
├── writeup.md          # Design decisions and course limitations
├── requirements.txt    # Python environment requirements
├── course/             # Lesson markdown files
│   ├── lesson_1.md
│   └── lesson_2.md
├── build/              # Learner build-along scripts
│   ├── build_along_1/
│   │   └── dataset_builder.py
│   └── build_along_2/
│       └── evaluator.py
├── output/             # Generated execution outputs and benchmarks
│   ├── test_cases.json
│   ├── capstone_run.log
│   └── course_manifest.json
└── agent/              # Course orchestration agent scripts
    ├── build_course.py
    └── prompts.py
