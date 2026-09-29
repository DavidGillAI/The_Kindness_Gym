# The Kindness Gym: Round 1 Funding Pitch Outline

Presentation target: approximately 6 minutes, including a short live POC demonstration.

## Slide 1: The Kindness Gym
Estimated time: 30 seconds

AI-assisted training for two everyday skills:

- Kindness towards yourself
- Kindness towards others

Round 1 scenario:

- Sector: Personal-development technology
- Company size: Small early-stage company
- Current stage: Research and working proof of concept

The central trust question is whether users can understand what the AI does and where its limitations lie.

## Slide 2: Everyday Kindness Can Be Difficult
Estimated time: 40 seconds

Chart: `kindness_survey_challenges_90.png`

Among the 90 survey respondents:

- 62.2% found self-kindness after mistakes challenging.
- 62.2% found setting boundaries without guilt challenging.
- 48.9% found maintaining positive habits challenging.

The findings support focusing on self-criticism, guilt, boundaries and habit support.

Limitation: This was a convenience sample recruited through an extended personal and social network.

## Slide 3: The Proposed Solution and Use Cases
Estimated time: 40 seconds

The Kindness Gym is a proposed personal-development app offering:

1. Personalised guidance for everyday kindness dilemmas
2. Practical exercises within an optional 21-day programme
3. Optional insights from a verified research library

Proposed supporting features include progress tracking and habit reminders.

The product is intended for personal development. It is not therapy or medical treatment.

## Slide 4: Comparable Products Show Some Adoption
Estimated time: 40 seconds

Chart: Comparable wellness-app Google Play download milestones

Comparable products include:

- Loving Kindness
- The Self-Compassion App
- BeKind
- Holly Health

These apps show consumer adoption within related categories.

Limitation: Google Play milestones do not show active users, paying customers, retention or demand for The Kindness Gym.

## Slide 5: Early User Interest and Concerns
Estimated time: 45 seconds

Charts:

- `kindness_survey_free_interest_90.png`
- `kindness_survey_ai_concerns_90_vertical.png`

Survey findings:

- 60% said they were somewhat or very likely to try a free version.
- Privacy and personal data concerned 60%.
- Inaccurate or inappropriate advice concerned 56.7%.

These are stated preferences from a non-representative sample. They do not demonstrate customer demand or actual adoption.

## Slide 6: Commercial Benchmarks
Estimated time: 35 seconds

Tableau charts:

- Download-to-paid conversion: freemium compared with a hard paywall
- Year 1 revenue per payer: AI compared with non-AI subscription apps

The benchmarks illustrate possible business-model trade-offs.

RevenueCat reports stronger early monetisation for AI apps alongside weaker retention. The figures cover subscription apps across many categories and do not forecast results for The Kindness Gym.

## Slide 7: Working Proof of Concept
Estimated time: 1 minute 20 seconds, including demonstration

Current n8n workflow:

User message → Chat Trigger → GPT-4o-mini → Kindness Gym response

The POC demonstrates the everyday coaching use case through:

- Acknowledgement of the situation
- A balanced perspective
- One practical exercise
- Optional research
- One reflection question

The workflow is a two-node proof of concept. It does not demonstrate the full app, 21-day programme, user accounts or production safeguards.

Demonstrate one representative scenario.

## Slide 8: Evaluation Exposed Reliability Problems
Estimated time: 1 minute

Five manually scored scenarios used five pass/fail criteria:

- Autonomy
- Accuracy
- Accountability
- Exercise relevance
- Research integrity

Result:

- 2 PASS
- 3 FAIL
- 40% overall pass rate

Show two cases:

- Customer misinformation: PASS
- Coffee for a colleague: FAIL

Main failures:

- Irrelevant research
- Malformed or inconsistent citations
- Unsupported reassurance

The test set is small and manually assessed. It does not establish general reliability or behaviour change.

## Slide 9: Pilot Architecture Must Make Evidence Controllable

Proposed, not yet implemented: interpret the situation, select relevant research from an approved library, insert the citation through a fixed workflow step, then generate and check the response.

Before testing with real users, review privacy, AI disclosure and safety reporting. Energy and carbon impact have not been measured.

## Slide 10: A Limited Six-Week Pilot

Ask: fund a focused six-week pilot with a preliminary upfront budget of €1,700–€4,500, excluding founder time.

Weeks 1–2: define the experience and safety rules.
Weeks 3–4: build the focused pilot.
Weeks 5–6: test, refine and launch to a small group.

Measure completion, repeat use, perceived usefulness, willingness to pay and performance on a broader safety test set.