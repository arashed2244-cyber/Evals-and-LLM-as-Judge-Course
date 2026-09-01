# build/build_along_1/dataset_builder.py
import json
import os

DATASET = [
    {
        "id": "tc_001",
        "input": "Explain API keys simply.",
        "output": "An API key is like a digital passcode that lets your application talk to a server securely.",
        "ground_truth": 1
    },
    {
        "id": "tc_002",
        "input": "Summarize the return policy.",
        "output": "You can return items anytime. Just bring them back whenever you feel like it.",
        "ground_truth": 0
    },
    {
        "id": "tc_003",
        "input": "Provide a Python list example.",
        "output": "Here is a list: my_list = [1, 2, 3]",
        "ground_truth": 1
    },
    {
        "id": "tc_004",
        "input": "What is 2 + 2?",
        "output": "The answer is 5.",
        "ground_truth": 0
    }
]

def main():
    # Resolve path relative to the root submission directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "output"))
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "test_cases.json")
    
    with open(output_path, "w") as f:
        json.dump(DATASET, f, indent=2)
        
    print(f"CHECK: Successfully generated test_cases.json at {output_path} with {len(DATASET)} cases.")

if __name__ == "__main__":
    main()