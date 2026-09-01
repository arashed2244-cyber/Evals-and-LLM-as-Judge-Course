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
├── README.md
├── course/
│   ├── lesson_1.md
│   └── lesson_2.md
├── build/
│   ├── build_along_1
|   |   └──dataset_builder.py
│   └── build_along_2
|       └──evaluator.py
└── build-along/
    ├── output/
    |   ├──test_cases.json
    |   └──capstone_run.log
    ├── agent/
    |   ├──build_course.py
    |   └──prompts.py
    └── writeup.md
