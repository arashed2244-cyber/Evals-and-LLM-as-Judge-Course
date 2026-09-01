"""
Prompt templates used by the course generation agent.
"""

COURSE_GENERATION_PROMPT = """
You are an expert AI Curriculum Engineer. Design a 90-minute course on "Evals and LLM-as-Judge" for engineers whose AI features are regressing in production.

Course Constraints:
- Text only (no video/audio).
- Exactly 2 lessons.
- Up to 5 sections per lesson (300-500 words per section).
- 1 to 3 checkpoints per lesson.
- 1 build-along script per lesson.
- Lessons must compound: Lesson 1 creates test data, Lesson 2 builds the judge/metrics engine.

Structure your response around these core breaking points:
1. Synthetic ground truth trap.
2. Binary vs. continuous scoring ambiguity.
3. Prompt drift in evaluators.
"""

LESSON_1_PROMPT = """
Generate Lesson 1: Framing Quality and Building Ground Truth.
Focus on translating intuition into discrete binary criteria (Pass=1, Fail=0) and creating test_cases.json.
Include Python code for dataset_builder.py as the build-along.
"""

LESSON_2_PROMPT = """
Generate Lesson 2: Constructing the LLM Judge & Metric Engine.
Focus on structured JSON outputs, zero-shot chain-of-thought, and calculating Precision, Recall, and F1.
Include Python code for evaluator.py as the build-along capstone.
"""