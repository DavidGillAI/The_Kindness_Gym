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

## Measured Sol run: 3 October 2026

Model: gpt-5.6-sol. Reasoning: none.
Same prompt and five inputs. One response per case.
Times measure the API call, not the full browser experience.

| Case | Seconds | Input tokens | Output tokens |
|---|---:|---:|---:|
| Exhausted friend | 6.37 | 595 | 270 |
| Coffee for colleague | 5.09 | 601 | 286 |
| Financial guilt | 5.41 | 605 | 285 |
| Customer misinformation | 5.60 | 601 | 293 |
| Tipping uncertainty | 5.86 | 605 | 305 |

Mean API time: 5.67 seconds.
Total input tokens: 3,007.
Total output tokens: 1,439.
No cache reads, cache writes or reasoning tokens were reported.

Boundary handling and accountability remained stronger than the
gpt-4o-mini baseline. Minor assumptions, overlapping options and
gratitude points that resemble affirmations remain concerns.

## Measured Luna run: 3 October 2026

Model: gpt-5.6-luna. Reasoning: none.
Same prompt, five inputs and 600-token limit as Sol.
One response per case.

| Case | Seconds | Input tokens | Output tokens |
|---|---:|---:|---:|
| Exhausted friend | 5.17 | 595 | 278 |
| Coffee for colleague | 4.51 | 601 | 254 |
| Financial guilt | 4.34 | 605 | 298 |
| Customer misinformation | 4.25 | 601 | 303 |
| Tipping uncertainty | 4.83 | 605 | 286 |

Mean API time: 4.62 seconds.
Total input tokens: 3,007.
Total output tokens: 1,419.
No cache reads, cache writes or reasoning tokens were reported.

Luna respected the main financial and rest boundaries, supported
correction of misinformation and acknowledged uncertainty.

Remaining weaknesses included assumptions about guilt and requests,
overlapping gratitude points, and treating confirmed misinformation
as potentially incorrect.

In this run, Luna was approximately 18% faster than Sol on average.
The cases were familiar development examples, with one measured
response per model per case. These results do not establish general
reliability or a consistent speed advantage.

Next: calculate estimated costs and test unfamiliar situations
before deciding which model to keep.

## Luna with low reasoning: 3 October 2026

Model: gpt-5.6-luna.
Reasoning requested and returned: low.
Output allowance: 3,000 tokens. Prompt and inputs unchanged.

| Case | Seconds | Input tokens | Output tokens | Reasoning tokens |
|---|---:|---:|---:|---:|
| Exhausted friend | 5.49 | 595 | 278 | 0 |
| Coffee for colleague | 5.22 | 601 | 270 | 0 |
| Financial guilt | 5.05 | 605 | 281 | 0 |
| Customer misinformation | 5.55 | 601 | 346 | 38 |
| Tipping uncertainty | 5.03 | 605 | 298 | 0 |

Mean API time: 5.27 seconds.
Total input tokens: 3,007.
Total output tokens: 1,473, including 38 reasoning tokens.

An earlier exhausted-friend call took 5.52 seconds. It was used
for diagnostics and is excluded from this table.

No clear quality improvement was observed over Luna without
reasoning. Remaining issues included dependent action options,
unsupported assumptions and weak gratitude points.

The tipping response invented the explanation that the user
only had a small amount available.

Both reasoning effort and the output allowance changed, so this
compares configurations rather than isolating reasoning alone.
The sample is too small for firm conclusions.

Provisional next candidate: Luna with reasoning set to none,
subject to sensitive-case and misuse testing.

### GPT-5.6-luna: high reasoning, targeted checks

Same prompt and inputs, with a 3,000-token output allowance.

| Case | Seconds | Input tokens | Output tokens | Reasoning tokens |
|---|---:|---:|---:|---:|
| Customer misinformation | 9.94 | 601 | 818 | 516 |
| Tipping uncertainty | 9.27 | 605 | 663 | 361 |

Output token totals include reasoning tokens. Both responses completed.

High effort recognised the confirmed customer error and avoided
inventing a financial explanation in the tipping case. Remaining
issues included suggestions presented as consecutive steps and
gratitude points assuming progress or benefits not established
by the user's message.

These two checks showed some improvement, with approximately
double the response time of the corresponding no-reasoning runs.
They do not establish broader reliability.

Provisional candidate: GPT-5.6-luna with reasoning effort "none",
subject to sensitive-situation and misuse testing.