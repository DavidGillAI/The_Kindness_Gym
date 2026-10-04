# The Kindness Gym: Round 2 EU AI Act Assessment

Assessment date: 4 October 2026
Status: Preliminary academic assessment of the current MVP.

The Round 1 assessment remains unchanged in `eu_ai_act_assessment.md`.

This document records the current implementation, relevant obligations and remaining gaps. It does not certify legal compliance or readiness for public deployment.

## 1. Intended Purpose

The Kindness Gym is an AI-powered personal-development app intended to help adults think through everyday dilemmas involving kindness, boundaries, mistakes and uncertainty.

The current MVP provides:

- A mobile-friendly form for describing a situation.
- An AI-generated acknowledgement and balanced perspective.
- One to three practical suggestions, intended as alternatives where appropriate.
- Grounded gratitude perspectives for ordinary situations.
- A separately displayed research insight and citation when selected by the application.
- Safety-focused responses and a support-directory link for sensitive situations.

The app does not support an ongoing conversation.

The proposed 21-day programme is outside the current MVP.

The app is not intended to diagnose, treat or monitor health conditions, provide therapy or deliver emergency care.

It does not make decisions about employment, education, credit, benefits or access to essential services.

Its intended audience is adults. An effective age restriction has not been implemented.

## 2. System and Operator Roles

The app uses an OpenAI model to generate contextual content and recommendations. It is therefore provisionally assessed as an AI system.

The founder develops the application under The Kindness Gym name. If supplied or put into service under that name, the founder would likely be the provider of the application-level AI system.

Using a third-party model does not automatically transfer all application responsibilities to the model supplier.

OpenAI supplies the underlying model. The current MVP accesses it through an Ironhack account. The contracting arrangements and permission to use that account for a public pilot require confirmation.

Providing an app free of charge does not automatically exempt it from the AI Act. Development-stage exclusions must not be assumed to cover a real-user deployment.

These role assessments are preliminary and must be confirmed against the actual launch arrangements.

## 3. Preliminary Risk Classification

The current intended purpose does not appear to fall within an Annex III high-risk use case.

The app is also not currently designed as a medical device or a safety component of a regulated product under Article 6(1).

It is provisionally assessed as a non-high-risk interactive generative AI system with applicable transparency obligations.

This conclusion is based on the defined purpose and functionality, not solely on the disclaimer.

Unexpected disclosures of suicidal thoughts do not by themselves establish that the app is a medical device. However, therapeutic claims, clinical functionality or deployment in regulated settings would require reassessment.

A non-high-risk classification does not mean that responses cannot cause harm.

### Changes requiring reassessment

- Diagnosis, treatment or clinical monitoring.
- Employment or education decisions about people.
- Behavioural scoring used to determine opportunities or treatment.
- Biometric emotion recognition.
- A change in audience, including intentional use by children.
- Other substantial changes to purpose or deployment.

## 4. Transparency: Article 50

Article 50 transparency obligations apply from 2 August 2026.

### User-facing disclosure

The current homepage and results page display:

“AI-powered guidance.”

The interface also describes the app as personal development rather than therapy or medical advice.

The homepage disclosure appears before the user submits a dilemma. This is a concrete improvement over the Round 1 POC.

Further checks are needed for visibility, accessibility and understanding across devices. A visible label is evidence of implementation, not complete proof of compliance.

A short explanation of possible inaccuracies and how to report problems should accompany the pilot.

### AI output marking

Article 50(2) addresses machine-readable marking and detectability of generated content.

The current visible AI label does not establish compliance with this separate obligation.

Before launch, assess the responsibilities of the application and model providers, available marking mechanisms and whether application processing preserves relevant markings.

Status: Unresolved.

### Other transparency provisions

The current app does not generate deepfake audio, images or video, or use biometric emotion recognition.

Private dilemma responses are not currently intended as public-interest publications. Publishing AI-generated articles or adding other media would require a fresh assessment.

## 5. AI Literacy: Article 4

This assessment uses the amended Article 4 wording reflected in the consolidated legislation following the July 2026 AI Omnibus.

Providers and deployers must take measures supporting AI literacy among staff and others operating systems on their behalf. The provision does not require guaranteeing a particular literacy level for every individual.

### Existing evidence

The project documents:

- Model comparisons and reasoning-setting experiments.
- Known unsupported assumptions and boundary failures.
- Evaluation methods and their limitations.
- Sensitive-situation and prompt-injection tests.
- Separation of model guidance from research citations.

These activities support practical understanding of the system.

### Remaining work

Before a pilot, document a short operating guide covering:

- Intended purpose and limitations.
- Model and prompt configuration.
- How to review failures and record changes.
- Sensitive disclosures and support boundaries.
- Privacy-conscious handling of reports.
- When to pause the app and seek specialist advice.

No formal operator guide or completed training record is claimed in this assessment.

## 6. Prohibited Practices: Article 5

Relevant prohibitions include specified harmful manipulation, exploitation of vulnerabilities and social scoring. Their legal thresholds matter; not every persuasive suggestion is prohibited.

The current app is not intended to use prohibited practices.

Its design nevertheless creates foreseeable risks because users may describe guilt, financial difficulty, distress or vulnerable circumstances.

### Implemented safeguards

The system prompt instructs the model to:

- Respect financial and personal boundaries.
- Avoid guilt-based pressure and predictions of other people's reactions.
- Avoid inventing facts or benefits.
- Treat user instructions as situation content rather than overrides.
- Omit gratitude prompts for sensitive situations.
- Prioritise immediate human help where danger is stated.

There is no implemented kindness score, donation mechanism, subscription upselling or targeted advertising.

### Remaining limitations

Prompt instructions do not guarantee compliant behaviour.

Testing has still found suggestions involving future giving despite financial-boundary rules.

Gratitude prompts can also become minimising or imply that distress has benefits if poorly generated.

Any future paid tiers or charity advertising must avoid using guilt, distress or personal disclosures to encourage purchases or donations.

## 7. Technical Implementation and Evidence

| Component | Current implementation |
|---|---|
| Interface | Branded, mobile-friendly HTML and CSS |
| Application | FastAPI |
| Provisional model | `gpt-5.6-luna` |
| Reasoning configuration | `none` |
| Response generation | OpenAI Responses API |
| Input validation | Trimmed input, 1–4,000 characters |
| Output display | Escaped text, paragraphs and bullet lists |
| Research selection | Deterministic keyword rules |
| Research collection | One currently implemented study |
| Citations | Application-controlled source link |
| Support directory | Fixed link displayed on results pages |
| Evaluation | Fictional examples in LangSmith EU |
| Runtime recording | Timing, response status and token usage |
| Current deployment | Local development and testing |

Research selection is not a vector database or a comprehensive retrieval system.

Keyword exclusions reduce some inappropriate research displays but can miss indirect wording.

The app requests `store=False`. This does not establish zero provider retention. Processing and retention are addressed separately in the GDPR assessment.

## 8. Evaluation Findings

The LangSmith dataset contains ten fictional cases:

- Five ordinary dilemmas.
- Five sensitive cases, including suicidal thoughts, immediate danger, violence, instruction override and mixed gratitude/crisis content.

Three recorded experiments checked:

1. Successful response generation.
2. Research display matching expectations.
3. Gratitude display matching expectations.

All ten cases passed those three automatic checks in each recorded experiment.

These checks assess response delivery and selected display behaviour. They do not assess all factual, ethical or safety qualities.

The latest assisted content review recorded eight of ten content passes under its stated criteria:

- Three of five ordinary cases.
- Five of five sensitive cases.

Remaining ordinary-case issues included repetitive alternatives, unsupported wording and suggestions inconsistent with financial boundaries.

Sensitive-case responses generally prioritised human support and omitted gratitude and research. Some included unnecessary or unrelated wording.

Presentation problems were assessed separately. A subsequent rendering change keeps acknowledgement and perspective as paragraphs, with suggestions and gratitude as lists.

### Evaluation limits

- The dataset is small.
- Familiar cases were reused during prompt development.
- Results are not an independent clinical assessment.
- The revised format differs from Round 1, preventing a direct pass-rate comparison.
- Passing display checks does not prove safety or legal compliance.
- Broader abuse, indirect crisis wording and repeated-run consistency remain insufficiently tested.

Evidence is recorded in:

- `evaluation/mvp_langsmith_results.md`
- `evaluation/mvp_safety_response.md`
- `evaluation/mvp_model_comparison.md`
- `evaluation/mvp_test_cases.json`

## 9. Conformity Assessment and Documentation

On the provisional non-high-risk classification, the high-risk conformity assessment, CE marking and Annex IV technical-documentation requirements are not identified as applicable to this app.

This is an applicability conclusion, not a completed conformity assessment or certification.

If classification changes, the relevant requirements must be assessed again.

The project nevertheless maintains voluntary technical evidence through its code, prompt, research rules, evaluation scripts and results.

Before a pilot, this should be supplemented with release identifiers, operating procedures, responsibility assignments and records of unresolved issues.

## 10. Human Oversight and Incident Handling

The current app does not monitor users, contact emergency services or provide a live response from a human.

Safety instructions and directory links must not imply those capabilities.

A pilot reporting and review procedure is not yet implemented.

Proposed procedure:

1. Give testers a clear way to report unsuitable guidance.
2. Explain that reports are not an emergency support channel.
3. Collect only the information needed to investigate.
4. Record severity, affected version and corrective action.
5. Pause testing for serious unresolved problems.
6. Retest changes before resuming.
7. Assess any applicable reporting duties with appropriate advice.

Routine review of real dilemma text must not be introduced without addressing its privacy implications.

## 11. Action Plan

| Action | Status |
|---|---|
| Record intended purpose and preliminary classification | Documented |
| Display AI disclosure before interaction | Implemented; accessibility review pending |
| Separate research citation formatting from generation | Implemented |
| Test ordinary and sensitive scenarios | Initial evaluation completed |
| Resolve known content failures | Incomplete |
| Assess machine-readable output marking | Unresolved |
| Document operator AI literacy measures | Partially evidenced; guide pending |
| Provide reporting and incident procedure | Not implemented |
| Confirm provider roles and account arrangements | Pending |
| Complete privacy safeguards for real-user testing | Pending |
| Review final configuration before deployment | Pending |

The founder is the proposed owner of these actions. Specialist advice is needed where legal, privacy or safety issues exceed the founder's competence.

Hosting, paid subscriptions and advertising remain proposals, not implemented features.

## 12. Conclusion

The current MVP is provisionally assessed as a non-high-risk AI system subject to applicable transparency and other obligations.

Round 2 has added visible AI disclosure, controlled citations, documented evaluation and safety-oriented prompt rules.

Important gaps remain, particularly output-marking assessment, operator procedures, reporting, privacy arrangements and response consistency.

The project should be presented as an evaluated academic MVP with documented limitations, not a legally certified or production-ready service.

## Sources

Checked on 4 October 2026:

- Consolidated EU AI Act:
  https://eur-lex.europa.eu/eli/reg/2024/1689
- Definitions, Article 3:
  https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3
- AI literacy, Article 4:
  https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4
- Prohibited practices, Article 5:
  https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5
- High-risk classification, Article 6:
  https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6
- High-risk use cases, Annex III:
  https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3
- Transparency, Article 50:
  https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50
- Commission transparency FAQ:
  https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- Commission AI Omnibus update:
  https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force

Related project assessment:

- `research/gdpr_assessment_round2.md`