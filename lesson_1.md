# Lesson 1: Framing Quality and Building Ground Truth

## Section 1: Why Your Intuition Fails at Scale
When launching an AI feature, your first reaction is to test inputs manually. You try five prompts, read the responses, and if they look good, you push to production. This "vibe check" approach works for version 0.1, but breaks down immediately as your feature evolves.

When you update your system prompt or switch model versions, outputs change subtly across edge cases. Without automated evaluation, you cannot tell if a prompt change fixed a bug or secretly regressed performance across 20% of your user base. Relying on intuition scale-locks your product: you become afraid to modify prompts because you have no objective measure of quality.

```xml
<svg viewBox="0 0 600 140" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)" style="background:#f8fafc; border-radius:8px; padding:10px;">
  <rect x="20" y="45" width="140" height="50" rx="6" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>
  <text x="90" y="75" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e293b">Manual Vibe Check</text>
  
  <path d="M 160 70 L 220 70" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>
  
  <rect x="230" y="45" width="140" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="300" y="75" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#92400e">Prompt Update</text>
  
  <path d="M 370 70 L 430 70" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>
  
  <rect x="440" y="45" width="140" height="50" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="510" y="68" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#991b1b">Silent Regression</text>
  <text x="510" y="83" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#7f1d1d">(Undetected in Prod)</text>
  
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#94a3b8"/>
    </marker>
  </defs>
</svg>