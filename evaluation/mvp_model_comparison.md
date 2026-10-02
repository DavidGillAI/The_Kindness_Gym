# MVP Model Comparison

## Baseline: gpt-4o-mini

Date: 2 October 2026.
Five manual cases, one response per case, with the same unchanged prompt.
This is a preliminary comparison, not a reliability estimate.

| Case | Main finding |
|---|---|
| Exhausted friend | Suggested future help and a catch-up despite the rest boundary. |
| Coffee for colleague | Introduced unmentioned spending concerns and broad positive claims. Research card appeared. |
| Financial guilt | Suggested giving the €5 despite the stated limit. Research correctly omitted. |
| Customer misinformation | Included correction, but offered private reflection as an alternative that leaves the error unresolved. |
| Tipping uncertainty | Assumed good service and suggested a compensatory gift. |

All five responses need revision on at least one criterion.

Current requirements: 1–3 alternative actions, 2–5 grounded gratitude points, British English, respect for boundaries, accountability and uncertainty.

Next: test another model using identical inputs and the unchanged prompt.

## Comparison: gpt-5.6-sol

Reasoning effort: none.
Same prompt and five inputs as the baseline, one response per case.

| Case | Main finding |
|---|---|
| Exhausted friend | Respected rest without compensatory commitments. Breathing option prepares a reply but does not resolve the request itself. |
| Coffee for colleague | Supported the coffee idea without predicting a reaction. Two options overlapped; gratitude introduced unmentioned pressure. |
| Financial guilt | No spending or compensation suggested. Assumed a request had been made. Research omitted. |
| Customer misinformation | Supported proportionate correction through workplace procedures. One gratitude point slightly overstated what noticing the error established. |
| Tipping uncertainty | Distinguished facts from assumptions without extra spending. Optional explanation may give the incident unnecessary weight. |

Sol showed better boundary handling and accountability in this small comparison. Grounding and option quality still need improvement.

Speed and token costs were not measured. Repeat tests and broader cases are needed before choosing the production model.