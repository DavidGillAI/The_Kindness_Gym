# Round 2 POC Evaluation

Date: 1 October 2026
Model: gpt-4o-mini
Method: Manual review of five everyday dilemmas.

## Workflow

Chat Trigger → Research selection → OpenAI → Merge → Format Response

Research selection uses keyword rules and one approved study.
The formatter inserts the selected finding and source URL.
It checks heading order and blocks model-generated citation URLs.

These checks do not validate the meaning or quality of the advice.

## Results

| Scenario | Observed behaviour | Assessment |
|---|---|---|
| Coffee for a colleague | Suggested one thank-you message. Approved research inserted before reflection. | Provisional pass |
| €5 and guilt about giving | Respected financial limits. Suggested a smile with a greeting. No research included. | Provisional pass |
| Incorrect customer information | Encouraged contacting the customer to correct the information. No research included. | Provisional pass |
| Exhausted friend | Suggested declining, catching up later and providing snacks. No research included. | Fail: multiple suggestions and an added obligation |
| €0.20 tip | Acknowledged uncertainty about the waiter’s feelings. Suggested returning to the café to express thanks. No research included. | Needs revision: unnecessary return visit and weak handling of uncertainty |

## What Improved

- Research selection and citation formatting are handled outside the model.
- The approved study appeared in the coffee case.
- Research was omitted in the other four cases.
- The final reply appeared directly in the chat.
- A formatting issue caused by bold headings was corrected.

## Remaining Issues

- The model still sometimes suggests multiple actions.
- Boundary advice can introduce new obligations.
- Research relevance depends on narrow keyword rules.
- The formatter cannot detect every unsupported claim or repeated research idea.
- The chat displays the source as a clickable link; exact line formatting still needs checking.

## Limitations

This was a development test, with prompt changes made during testing.
The results are provisional and are not a controlled comparison with Round 1.
Five responses do not establish reliability or production readiness.

## Next Step

Freeze the prompt and workflow, then rerun all five cases using
the same evaluation criteria. Save the full responses alongside the scores.