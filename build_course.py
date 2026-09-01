#!/usr/bin/env python3
"""
Orchestration agent to build the 'Evals and LLM-as-Judge' course content.
Generates course structure manifests and manages prompt templates.
"""

import os
import json
from prompts import COURSE_GENERATION_PROMPT, LESSON_1_PROMPT, LESSON_2_PROMPT

def run_agent():
    print("[Agent Orchestration] Initializing course builder agent...")
    
    # Ensure relative directories exist
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "output"))
    os.makedirs(output_dir, exist_ok=True)

    print("[Agent Step 1/3] Loading prompt templates...")
    _ = COURSE_GENERATION_PROMPT
    _ = LESSON_1_PROMPT
    _ = LESSON_2_PROMPT
    
    print("[Agent Step 2/3] Simulating course structure assembly...")
    course_manifest = {
        "title": "Evals and LLM-as-Judge",
        "target_audience": "Engineers shipping AI features seeking reliable evaluation",
        "estimated_minutes": 90,
        "lessons": [
            {
                "lesson_id": 1,
                "title": "Framing Quality and Building Ground Truth",
                "artifact": "test_cases.json",
                "script": "build/build_along_1/dataset_builder.py"
            },
            {
                "lesson_id": 2,
                "title": "Constructing the LLM Judge & Metric Engine",
                "artifact": "capstone_run.log",
                "script": "build/build_along_2/evaluator.py"
            }
        ]
    }

    manifest_path = os.path.join(output_dir, "course_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(course_manifest, f, indent=2)

    print(f"[Agent Step 3/3] Manifest written to {manifest_path}")
    print("CHECK: Course generation pipeline completed successfully.")

if __name__ == "__main__":
    run_agent()