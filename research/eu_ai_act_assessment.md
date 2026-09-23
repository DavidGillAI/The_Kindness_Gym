# The Kindness Gym: Preliminary EU AI Act Assessment

Assessment date: 23 September 2026
Status: Preliminary assessment for Ironhack Round 1

## 1. Intended Purpose and Preliminary Classification

### Intended Purpose

The Kindness Gym is a proposed AI-assisted
personal-development application designed to help
adults practise kindness towards themselves and others.

Its proposed features include:
- A structured 21-day kindness programme.
- Personalised AI guidance for everyday situations.
- Short, voluntary kindness exercises.
- Optional, research-based educational insights.

The application is intended to support reflection,
learning and personal choice.

It is not intended to:
- Diagnose or treat medical or mental-health conditions.
- Replace professional therapy or medical advice.
- Make decisions about employment, education,
  creditworthiness or access to essential services.
- Evaluate or rank individuals based on their behaviour.

### Preliminary EU AI Act Classification

The proposed application meets the general concept
of an AI system because it uses a machine-learning
model to generate contextual recommendations
and educational content.

Based on its currently defined intended purpose,
The Kindness Gym does not appear to fall within
the high-risk use cases listed in Annex III.

However, it directly interacts with users through
an AI-generated conversational interface.
Consequently, the transparency requirements
of Article 50 are relevant.

### Preliminary Conclusion

For the currently proposed functionality,
The Kindness Gym is provisionally assessed
as a non-high-risk AI system subject to
applicable transparency requirements.

This classification is preliminary and must
be reviewed if the product's purpose, users
or functionality changes.

This document is a student project assessment,
not a formal legal compliance certification.

## 2. Transparency Requirements

### Relevant Legislation

EU AI Act, Article 50.

### Application to The Kindness Gym

The proposed application allows users to interact
directly with an AI system.

Users should be clearly informed that the guidance
and personalised exercises are AI-generated.

This disclosure should appear before or at the
beginning of their first interaction.

### Proposed Implementation

The pilot should include:

- A clear AI disclosure during onboarding.
- A persistent label identifying AI-generated guidance.
- An accessible explanation of the AI's intended purpose.
- A clear distinction between AI-generated coaching
  and information drawn from verified research.

### Proposed User Disclosure

"The Kindness Gym uses artificial intelligence to
generate personalised kindness exercises and
perspectives.

You are interacting with an AI system, not a human
coach or therapist.

AI responses may be inaccurate or inappropriate
for your particular circumstances. You remain
responsible for deciding which suggestions,
if any, to follow."

### Additional Considerations

The proposed pilot will generate conversational text.

Before deployment, the project must assess which
additional Article 50 requirements apply to the
specific system and its outputs, including any
applicable machine-readable marking obligations.

The application should also make its limitations
understandable without requiring users to read
lengthy legal documentation.

### Current Status

The existing n8n POC identifies itself as an AI
personal-development guide in its system prompt.

A dedicated user-facing transparency notice has
not yet been implemented or tested.

Status: Planned for the pilot.

## 3. AI Literacy and Operational Safeguards

### Relevant Legislation

EU AI Act, Article 4.

### Application to The Kindness Gym

The project must take appropriate measures to
support the AI literacy of people developing,
operating and maintaining the application.

Training and procedures should reflect their
responsibilities and the risks associated with
personalised AI-generated guidance.

### Proposed Measures

Before the pilot, the project should establish:

- Basic understanding of how the AI system works,
  including its capabilities and limitations.
- Awareness of hallucinations, unsupported
  reassurance and inconsistent responses.
- Procedures for identifying and reviewing
  potentially harmful or misleading outputs.
- Clear boundaries between personal-development
  guidance and professional mental-health advice.
- Appropriate human review of evaluation failures
  and significant safety concerns.
- Documentation of testing, identified problems
  and corrective actions.

### Operational Safeguards

The proposed pilot should:

- Use predefined evaluation criteria and
  representative test scenarios.
- Maintain a curated, verified research library.
- Separate research selection and citation
  formatting from free-text response generation.
- Allow users to disregard AI-generated suggestions.
- Avoid presenting AI responses as professional
  therapeutic or medical advice.
- Provide a mechanism for users to report
  inaccurate or inappropriate guidance.

These safeguards are proposed design and
operational measures. They are not all separate
legal requirements under Article 4.

### Current Status

The POC has been manually evaluated using
five representative scenarios.

Two passed all applicable criteria and three
failed, primarily because of research relevance,
citation formatting and unsupported reassurance.

This evaluation provides preliminary evidence
of system limitations but does not establish
compliance or overall reliability.

Formal operational procedures and documented
AI literacy measures have not yet been implemented.

Status: Partially addressed; further work
required before a public pilot.

## 4. Prohibited AI Practices

### Relevant Legislation

EU AI Act, Article 5(1)(a), (b) and (c).

### Application to The Kindness Gym

The application is designed to encourage voluntary
kindness exercises and personal reflection.

Users may describe emotionally sensitive situations,
including guilt, insecurity, personal relationships
and financial difficulties.

The system must not exploit those circumstances
to manipulate users into harmful decisions.

Article 5 prohibits specified forms of harmful
manipulation, exploitation of vulnerabilities
and social scoring.

Not every persuasive suggestion or personalised
exercise constitutes a prohibited AI practice.

### Proposed Safeguards

The application should:

- Avoid guilt-based persuasion or emotional manipulation.
- Never pressure users to donate money, purchase
  subscriptions or disregard personal boundaries.
- Present exercises as voluntary suggestions.
- Avoid exploiting vulnerabilities related to age,
  disability or social and economic circumstances.
- Avoid encouraging users to become emotionally
  dependent on the AI.
- Avoid assigning social scores or ranking users
  according to their perceived kindness.
- Allow users to decline exercises without punishment
  or manipulative messaging.

### Practical Example

A user expresses guilt about not giving money
to someone experiencing homelessness.

The AI should acknowledge the situation, respect
the user's financial boundaries and offer a
voluntary exercise.

It should not use the user's guilt to pressure
them into spending money.

### Preliminary Assessment

The currently defined product does not appear
to involve the prohibited practices identified
above.

However, personalised behavioural guidance
creates foreseeable risks that require testing
and appropriate safeguards.

The assessment must be revisited if future
features introduce behavioural scoring,
aggressive engagement mechanisms or
personalised commercial persuasion.

### Current Status

The existing POC includes prompt instructions
against financial pressure and unsupported
assumptions.

Manual testing has demonstrated some successful
boundary-respecting responses, but the system
has not undergone comprehensive safety testing.

Status: Partially addressed; further evaluation
required before public deployment.

## 5. Preliminary Conclusion and Action Plan

### Preliminary Conclusion

Based on its currently proposed purpose and features,
The Kindness Gym does not appear to fall within the
EU AI Act's high-risk categories.

The application is intended to provide voluntary
personal-development exercises, not regulated
decision-making or medical treatment.

However, the project must address applicable
transparency requirements, AI literacy measures
and prohibitions on harmful AI practices.

This preliminary classification does not establish
legal compliance.

### Actions Before Public Deployment

1. Implement a clear user-facing AI disclosure.
2. Document appropriate AI literacy measures for
   anyone developing or operating the system.
3. Improve testing for misleading, manipulative
   or otherwise harmful responses.
4. Implement controlled research retrieval and
   reliable citation formatting.
5. Establish a mechanism for reporting and
   reviewing problematic responses.
6. Reassess the classification if the intended
   purpose or functionality changes.
7. Review the final implementation against
   the applicable legislation before launch.

### Current Compliance Status

- Preliminary classification: Completed.
- User-facing AI disclosure: Not implemented.
- AI literacy documentation: Not implemented.
- Initial response evaluation: Completed.
- Comprehensive safety testing: Not completed.
- Production safeguards: Not implemented.
- GDPR assessment: Preliminary assessment completed; implementation          requirements remain unresolved.

### Overall Status

Preliminary academic assessment completed.

Further implementation, testing and legal review
would be necessary before public deployment.

The existing n8n proof of concept must not be
presented as a legally certified or production-ready
application.