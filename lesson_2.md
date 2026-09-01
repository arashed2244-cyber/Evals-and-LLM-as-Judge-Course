# Lesson 2: Constructing the LLM Judge & Metric Engine

## Section 1: The LLM-as-a-Judge Pattern
An LLM judge replaces manual human verification by using an LLM to classify whether feature outputs pass or fail your binary assertions. Instead of returning raw prose, the judge evaluates the feature output against a strict evaluation rubric and produces a structured verdict.

Using an LLM as a judge requires enforcing structured JSON output. If a judge returns freeform text, parsing binary results programmatically becomes fragile. Requiring a JSON payload with explicit fields guarantees that your evaluation pipeline can consume grades deterministically.

---

## Section 2: Prompt Engineering for Evaluation
LLM judges suffer from position bias, verbosity bias, and output instability. To maximize judge reliability, structure evaluation prompts with a zero-shot chain-of-thought requirement: require the judge to state its reasoning *before* outputting the final binary decision (`1` or `0`).

```xml
<svg viewBox="0 0 620 140" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)" style="background:#f8fafc; border-radius:8px; padding:10px;">
  <rect x="20" y="45" width="130" height="50" rx="6" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>
  <text x="85" y="68" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b">Test Case Input</text>
  <text x="85" y="83" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#475569">&amp; Feature Output</text>
  
  <path d="M 150 70 L 190 70" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow2)"/>
  
  <rect x="200" y="45" width="140" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="270" y="68" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e40af">LLM Judge Prompt</text>
  <text x="270" y="83" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#1e3a8a">(Reasoning First)</text>
  
  <path d="M 340 70 L 380 70" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow2)"/>
  
  <rect x="390" y="45" width="210" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="495" y="68" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#14532d">Structured JSON Result</text>
  <text x="495" y="83" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#166534">{"reasoning": "...", "passed": 1}</text>
  
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#94a3b8"/>
    </marker>
  </defs>
</svg>