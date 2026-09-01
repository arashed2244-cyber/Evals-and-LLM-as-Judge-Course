# build/build_along_2/evaluator.py
import json
import os

# Cached judge responses for deterministic offline replay
MOCK_JUDGE_RESPONSES = {
    "tc_001": {"reasoning": "Clear explanation without jargon.", "passed": 1},
    "tc_002": {"reasoning": "Inaccurate policy summary provided.", "passed": 0},
    "tc_003": {"reasoning": "Valid python list syntax.", "passed": 1},
    "tc_004": {"reasoning": "Incorrect calculation.", "passed": 1}  # Intentional FP for metric testing
}

def evaluate_case(case_id):
    return MOCK_JUDGE_RESPONSES.get(case_id, {"reasoning": "Unknown", "passed": 0})["passed"]

def calculate_metrics(tp, fp, fn):
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    return precision, recall, f1

def main():
    dataset_path = os.path.join("..", "..", "output", "test_cases.json")
    
    if not os.path.exists(dataset_path):
        print(f"ERROR: Could not find {dataset_path}. Did you run Lesson 1 first?")
        return

    with open(dataset_path, "r") as f:
        cases = json.load(f)

    tp, fp, fn, tn = 0, 0, 0, 0

    print("--- RUNNING EVALUATION SUITE ---")
    for case in cases:
        predicted = evaluate_case(case["id"])
        actual = case["ground_truth"]

        if predicted == 1 and actual == 1:
            tp += 1
            status = "TP"
        elif predicted == 1 and actual == 0:
            fp += 1
            status = "FP"
        elif predicted == 0 and actual == 1:
            fn += 1
            status = "FN"
        else:
            tn += 1
            status = "TN"

        print(f"Case {case['id']}: Predicted={predicted}, Actual={actual} [{status}]")

    precision, recall, f1 = calculate_metrics(tp, fp, fn)

    print("\n--- GRADER METRICS ---")
    print(f"True Positives:  {tp}")
    print(f"False Positives: {fp}")
    print(f"False Negatives: {fn}")
    print(f"True Negatives:  {tn}")
    print(f"Precision:       {precision:.2f}")
    print(f"Recall:          {recall:.2f}")
    print(f"F1 Score:        {f1:.2f}")
    print("CHECK: Evaluation pipeline executed successfully.")

if __name__ == "__main__":
    main()