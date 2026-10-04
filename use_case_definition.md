# Use Case Definition

## Business Problem Statement

People often want to act with more kindness towards themselves and others, but struggle to find a balanced, practical response to everyday dilemmas. These situations may involve personal boundaries, mistakes, uncertainty about other people’s feelings or competing needs.

The Kindness Gym is an AI guide that offers a balanced perspective, 1–3 small practical actions as alternatives, and grounded suggestions for radical gratitude. Users can choose one action, adapt it or find their own approach.

Where relevant, the application displays an approved research finding and its source. Sensitive situations receive a safety-focused response instead of the everyday format.

## Company Profile and Current State

The Kindness Gym is a proposed, pre-launch consumer product in the self-improvement sector. It is a one-person project, with no operating company or paying customers assumed in this assessment.

The Round 1 proof of concept used an n8n workflow. Five-case manual testing produced two clean passes and identified problems with financial boundaries, unsupported assumptions and research citations.

Round 2 now includes a working, branded, mobile-friendly FastAPI MVP. Users can submit a dilemma, receive AI-generated guidance and view relevant research separately. The interface clearly identifies the guidance as AI-powered.

Manual model comparisons and sensitive-situation tests have been recorded. Repeatable evaluation through LangSmith is still to be implemented.

## Proposed AI Solution and System Type

The MVP is a generative AI application for everyday kindness dilemmas.

For ordinary situations, its response includes:

- A brief acknowledgement without judgement or automatic praise.
- A balanced perspective that respects boundaries, accountability and uncertainty.
- 1–3 small practical actions offered as alternatives.
- 2–5 grounded radical gratitude points, without inventing benefits or requiring gratitude for suffering.

The current model is `gpt-5.6-luna` with reasoning effort set to `none`. It is the provisional choice following manual comparisons of response quality, time and token usage.

Research selection and citation display are handled separately from response generation. The current implementation uses keyword rules to select one approved study. It does not yet use a vector database or semantic retrieval.

For suicidal thoughts, self-harm, threats of violence, abuse or serious distress, the prompt instructs the model to omit the everyday format and radical gratitude. It prioritises appropriate human support and urgent help where needed.

A fixed link to Find A Helpline is available on response pages. The application cannot contact emergency services, monitor a person’s safety or provide emergency care.

## Key Stakeholders and Interests

- **Users:** Want practical guidance that respects their choices and boundaries, with clear information about AI and its limitations.
- **Product owner:** Needs evidence that the app is useful, sufficiently reliable for its intended purpose and feasible to maintain.
- **Pilot testers:** Need a simple way to try the app and report where responses help or fall short.
- **Researchers and study publishers:** Have an interest in findings being represented accurately and cited clearly.

## Success Criteria

The following are targets for the Round 2 MVP, not claims of achieved performance:

1. At least 80% of an expanded ordinary-dilemma test set passes every applicable criterion: autonomy and boundaries, factual accuracy, accountability where relevant, appropriate practical alternatives, grounded radical gratitude and research integrity.
2. The test set includes the original five scenarios and new cases. Evaluation uses a fixed prompt and model configuration, with repeated runs to check consistency.
3. Sensitive-situation and misuse tests are assessed separately. Responses must avoid harmful instructions, forced gratitude, inappropriate research and unsupported claims about the app’s capabilities. Immediate danger must receive clear direction towards urgent human help.
4. At least 90% of ordinary test submissions return a complete response without an application error. Errors and incomplete responses are recorded separately from response-quality scores.
5. Every displayed research finding and citation matches an approved study.
6. Users can see that the app uses AI before submitting a dilemma.

Safety failures must be recorded and addressed rather than hidden within an overall pass rate. Passing a small test set does not establish production readiness.

## Evaluation Approach

Manual evaluation has informed prompt revisions and the provisional model choice. The records retain baseline failures and retests so that changes can be reviewed.

LangSmith evaluation is planned to make testing repeatable and record inputs, outputs, configuration and scores. Existing manual results are not LangSmith experiment results.

The Round 1 baseline remains two clean passes out of five cases. The updated MVP permits multiple practical alternatives and includes radical gratitude, so its overall scores are not directly comparable with the original response specification.

## Known Limitations

- Research selection uses keywords and can miss indirect wording or select a loosely related study.
- Research suppression for sensitive situations is also keyword-based and is not a comprehensive safety detector.
- Prompt instructions do not guarantee consistent behaviour.
- Some radical gratitude points still assume considerations or progress not established by the user’s message.
- Manual tests cover a limited set of situations and prompt versions.
- The app responds to one submission at a time and does not support an ongoing conversation.
- Broader safety testing and repeatable evaluation remain outstanding.

## Out of Scope for the MVP

The MVP does not include a 21-day programme, habit tracking, user accounts, payments or a native app-store release.

A vector database, a larger research collection and philosophical quotations may be explored later.

The app does not provide therapy, diagnosis, medical treatment or an emergency response service. Safety signposting does not change that scope.

It does not claim that its suggestions will improve wellbeing or guarantee a particular outcome.

## Evolution from Round 1

The Kindness Gym retains the self-improvement use case and everyday dilemma workflow demonstrated in the n8n proof of concept.

Round 2 has added a branded web interface, practical action alternatives, radical gratitude, separate research selection and citation display, model comparisons, sensitive-situation handling and visible AI disclosure.

The 21-day programme remains outside the MVP. The immediate priority is a working dilemma-response experience supported by honest evaluation of its strengths and limitations.

Teacher and peer feedback will be recorded separately when available.