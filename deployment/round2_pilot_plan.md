# The Kindness Gym: Round 2 Deployment and Pilot Plan

Date: 4 October 2026
Status: Proposed plan. Recruitment and deployment have not started.

## 1. Purpose

Run a small, six-week pilot with approximately ten adult volunteers.

The pilot will test whether the everyday dilemma app is useful, understandable and manageable for a single founder to maintain.

It will also gather early evidence about repeat use and willingness to pay.

The Round 1 timeline remains unchanged in `cost_estimation/timeline_estimate.md`. The 21-day course is outside this pilot.

## 2. Current Position

The current MVP includes:

- A branded, mobile-friendly FastAPI interface.
- Visible AI disclosure.
- AI-generated perspectives and practical suggestions.
- Gratitude perspectives for ordinary situations.
- Application-controlled research selection and citations.
- Sensitive-situation prompt rules and a support-directory link.
- Input validation and basic API error handling.
- A ten-case fictional LangSmith evaluation dataset.

It currently runs locally.

Public hosting, participant onboarding, feedback collection, operational procedures and the necessary privacy arrangements are not yet complete.

Accounts, payments and enforceable daily allowances are not implemented.

## 3. Pilot Participants

Target: approximately ten adult volunteers.

Potential participants include people who completed the earlier kindness survey and others willing to test the app.

Participation in the survey does not automatically authorise a testing invitation or constitute agreement to beta testing. Recruitment must use contact details appropriately.

Participants will receive a separate invitation explaining:

- What the app does.
- That guidance is AI-generated and may be unsuitable or inaccurate.
- That it is personal development, not therapy or emergency care.
- What information is processed and by which services.
- How to give feedback and report problems.
- How to withdraw from the pilot.

Participation is voluntary and unpaid. There are no assumed recruitment or incentive costs.

The sample is a convenience sample, not representative of a wider market.

## 4. Preparation Before the Six Weeks

The six-week clock begins only when preparation is complete.

The founder will:

1. Resolve known significant response failures and document remaining limitations.
2. Run a broader evaluation with unseen wording and repeated cases.
3. Complete the privacy arrangements required for real-user testing.
4. Confirm appropriate API account access and provider arrangements.
5. Assess unresolved AI Act obligations, including output marking.
6. Configure hosting, HTTPS, secrets and access restrictions.
7. Implement a basic feedback and problem-reporting route.
8. Document maintenance, incident handling and shutdown procedures.
9. Test the full journey on desktop and mobile.
10. Record the code, prompt and model configuration used at launch.

These activities have no fixed completion date. External advice or substantial fixes may extend preparation.

Volunteer testing is not a substitute for resolving known serious risks.

## 5. Hosting and Access

Proposed host: Render, with Frankfurt as the application region.

Paid hosting is provisionally budgeted at €10 monthly. The broader ROI model includes an additional €10 allowance for other services.

These allowances are not confirmed bills or capacity guarantees.

Hosting in Frankfurt does not establish that all processing remains in the EU.

The pilot should use restricted access appropriate to ten invited testers. A shared link alone is not an effective access restriction.

Before launch, implement proportionate request limits and an API spending threshold. Define how to pause access if usage becomes unexpected.

Provider secrets must be configured outside the repository.

Do not enable production tracing that sends real dilemma text to LangSmith by default. Evaluation should continue using fictional examples unless a separate justified process is established.

## 6. Pilot Experience

The pilot is free.

Participants can use the app when they have an everyday situation to consider. They are not asked to manufacture dilemmas or meet a daily activity target.

The proposed commercial allowance is one free dilemma daily. Until a limit is implemented, do not describe it as enforced.

Feedback should focus on:

- Whether the response helped them think.
- Whether suggestions fitted the situation.
- Whether boundaries were respected.
- Whether anything felt invented, pressuring or dismissive.
- Whether the interface and AI disclosure were clear.

Feedback should not require participants to submit their original dilemma or identify other people.

## 7. Six-Week Schedule

| Period | Activity | Evidence |
|---|---|---|
| Week 1 | Onboard ten volunteers and check access | Onboarding totals and initial usability feedback |
| Week 2 | Observe voluntary use and fix significant usability issues | Error counts, usage totals and change log |
| Weeks 3–4 | Continue testing and gather midpoint feedback | Usefulness ratings, repeat use and reported problems |
| Week 5 | Review costs, founder hours and interest in proposed paid tiers | Actual expenses, time log and pricing responses |
| Week 6 | Collect final feedback and decide the next step | Pilot report, unresolved issues and decision |

For material changes to the model, prompt or safety behaviour, run regression checks before releasing them.

Record which version participants used so feedback is not attributed to the wrong configuration.

## 8. Measures and Proposed Targets

These are decision targets, not results already achieved.

| Measure | Definition | Proposed target |
|---|---|---|
| Activation | Volunteers completing at least one dilemma submission | At least 8 of 10 |
| Response completion | Valid ordinary submissions returning complete guidance without an application error | At least 90% |
| Perceived usefulness | Respondents rating the guidance useful or very useful | At least 70%, with counts reported |
| Repeat use | Activated participants choosing to return in a later week | At least 50% |
| Evaluation quality | Cases passing every applicable criterion under a fixed rubric | At least 80% on an expanded fictional set |
| Research integrity | Displayed citations matching the curated source and fitting the situation | No incorrect or fabricated citations in reviewed cases |
| Serious safety failures | Reviewed outputs that enable harm or undermine urgent safety guidance | No unresolved serious failures |
| Founder workload | Logged maintenance, review, recruitment and support time | Compare actual hours with the budget assumption |
| Cost | Hosting, AI and other actual charges | Stay within the agreed pilot budget or revise before continuing |

Report numerators, denominators and missing feedback. For example, report “6 of 8 respondents” alongside the percentage.

Ten participants cannot establish broad reliability, clinical safety or market demand.

Safety review must include fictional tests for suicide, violence, abuse, indirect wording and instruction overrides. Participants should not be asked to submit personal crisis situations for testing.

## 9. Measurement and Privacy

Use the least intrusive measurement method that answers the pilot questions.

Possible methods include:

- Aggregate application counts for valid submissions, errors and timing.
- Voluntary weekly check-ins about whether participants used the app.
- A short midpoint and final feedback form.
- A founder time and expense log.

Repeat use requires an appropriate method; anonymous request totals alone cannot identify returning people.

If participant codes or other identifiers are introduced, document their purpose, retention and handling before use.

Avoid collecting raw dilemma text by default. Any access to reported examples needs a defined privacy process.

Report findings in aggregate. Do not publish identifiable participant comments without permission.

## 10. Support and Incident Handling

The founder provides pilot administration and technical support, not live crisis support.

Participants must be told when feedback is reviewed and that it is not an emergency channel.

Proposed routine: check reports and service status once each working day during the pilot.

If a serious unsuitable response is reported:

1. Assess the report without collecting unnecessary personal details.
2. Record severity, affected version and action taken.
3. Restrict or pause access where continued use could cause harm.
4. Investigate and obtain appropriate advice.
5. Test the correction before resuming.
6. Inform affected participants where appropriate.

If the founder cannot provide the agreed oversight, pause or shorten the pilot.

## 11. Workload and Budget

The founder works unpaid. Volunteer testers receive no payment.

The ROI document currently assumes four hours monthly for ongoing maintenance and support. An active pilot may require more.

For pilot scheduling, provisionally allow one to two hours weekly, plus onboarding and incident work. Record actual time and use it to update the ROI model.

The current financial assumptions are:

- €600 provisional external privacy and security review allowance.
- €300 contingency reserve.
- €20 monthly shared service allowance.
- AI usage costs in addition.

External review costs are unquoted and must be confirmed. Contingency is a reserve, not an automatic expense.

A free six-week pilot does not generate subscription revenue.

## 12. Recruitment and Communication

Recruitment begins with personal invitations to suitable adult volunteers, including survey participants where contact is appropriate.

The invitation should describe a small test of an unfinished product rather than promise improved wellbeing.

Participants receive:

- A short welcome message and instructions.
- Clear AI and privacy information.
- A feedback route and support boundaries.
- A midpoint check-in.
- A final feedback request.
- A brief account of what was learned.

No paid advertising is assumed for this pilot.

Initial market positioning is an accessible space for thinking through everyday kindness dilemmas. Claims about therapeutic effects or guaranteed personal growth are excluded.

## 13. Commercialisation Proposal

Potential future tiers:

| Plan | Allowance | Proposed monthly price |
|---|---:|---:|
| Free | One dilemma daily | €0 |
| Plus | Up to three daily | €0.99 |
| Premium | Up to ten daily | €1.99 |

These features are outside the current pilot implementation.

Ask participants:

- Whether the free allowance would meet their needs.
- Whether higher limits offer useful value.
- Whether they would consider either price.
- What would prevent them from paying.

Stated willingness is preliminary evidence. Actual paid conversion must be measured separately if a commercial test proceeds.

Do not use personal distress or guilt to encourage subscriptions.

Charity advertising remains a possible later experiment. It contributes no revenue to the forecast.

## 14. Decision at the End

### Continue with a further limited test

Consider this if:

- Participants find the app useful and some return voluntarily.
- Evaluation and privacy arrangements meet the agreed criteria.
- No serious unresolved safety issue remains.
- Founder workload and costs are manageable.

### Revise and retest

Choose this if the concept appears useful but response quality, usability, costs or workload need improvement.

### Pause

Pause if serious risks remain, participants find little value, oversight is impractical or preparation costs exceed available resources.

Meeting numerical targets does not override a serious unresolved concern.

A paid launch requires an additional decision covering demand, accounts, payments, limits, tax and ongoing support.

## 15. Deliverables

At the end of the pilot, produce:

- A summary of participation and feedback.
- Usage and reliability results with clear denominators.
- Actual expenses and founder hours.
- An updated evaluation and issue log.
- Updated ROI assumptions.
- A documented continue, revise or pause decision.

## 16. Related Documents

- `use_case_definition.md`
- `mvp/README.md`
- `evaluation/mvp_langsmith_results.md`
- `evaluation/mvp_safety_response.md`
- `cost_estimation/round2_roi_analysis.md`
- `research/gdpr_assessment_round2.md`
- `research/eu_ai_act_assessment_round2.md`