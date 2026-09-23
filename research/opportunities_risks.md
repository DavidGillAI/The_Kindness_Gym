# The Kindness Gym: Opportunity and Risk Mapping

## 1. Market Opportunities

### Opportunity 1: Existing Market Activity
Our Health & Fitness app research demonstrates activity in the broader digital wellness market.

Limitation: Broad market activity does not establish demand for kindness training specifically.

### Opportunity 2: Comparable Product Adoption
Google Play data identifies four comparable apps with published download milestones ranging from 5,000+ to 50,000+.

This provides evidence that consumers have downloaded products offering kindness, compassion and wellbeing exercises.

Limitation: Download thresholds do not establish active users, revenue or willingness to pay.

### Opportunity 3: AI-Personalised Kindness Training
The Kindness Gym proposes personalised exercises addressing both self-kindness and kindness towards others.

The working n8n POC demonstrates the ability to generate context-sensitive exercises.

Limitation: We have not established that consumers prefer this approach or would pay for it.

### Opportunity 4: Evidence-Based Differentiation
A curated research library could provide relevant scientific context alongside practical exercises.

Initial testing demonstrated research inclusion and omission, but also exposed citation and relevance failures.

Opportunity: Improve reliability through controlled research retrieval and deterministic citation formatting.

### Risk 1: Incorrect or Misapplied Research

**Risk:** The AI may include research that is only loosely related to the user's situation, or present a correct study in a misleading context.

**Evidence from POC testing:** The research relevance gate failed repeatedly in the homelessness and tipping scenarios, and citation formatting was inconsistent.

**Impact:** Users could receive misleading reassurance or lose trust in the product.

**Mitigation:** Separate research retrieval and citation formatting from the free-text coaching response. Use only a curated, verified research library and omit research when relevance is uncertain.

**Current status:** Unresolved in the POC.

### Risk 2: Sensitive Personal Information

**Risk:** Users may describe emotionally sensitive situations, relationships, finances or other personal circumstances when asking for kindness guidance.

**Impact:** Poor handling of this data could create privacy concerns, reduce trust and increase GDPR obligations.

**Mitigation:** Minimise data collection, avoid requiring real names, clearly explain what is processed, limit retention and design the product so users do not need to provide unnecessary personal details.

**Current status:** The POC uses synthetic or test scenarios only. A production privacy design has not yet been implemented.

### Risk 3: Over-Reliance on AI Guidance

**Risk:** Users may begin treating the app as an authority on personal decisions rather than as a reflective self-development tool.

**Impact:** This could reduce user autonomy and create inappropriate dependence on AI-generated guidance.

**Mitigation:** Frame outputs as optional exercises and perspectives, not instructions. Preserve user choice, avoid definitive advice, and clearly state that the product is not therapy or medical advice.

**Current status:** Partly addressed through the current system prompt, but not yet tested at scale.

### Risk 4: Inconsistent AI Responses

**Risk:** The same input may produce different outputs, even when the system prompt and model settings are unchanged.

**Evidence from POC testing:** Repeated tests of the homelessness and tipping scenarios produced recurring research relevance failures and inconsistent citation formatting.

**Impact:** Inconsistent behaviour could make the product feel unreliable and reduce user trust.

**Mitigation:** Move critical logic out of the free-text prompt where possible. Use deterministic workflow steps for research selection, formatting and validation, then evaluate repeated runs against fixed criteria.

**Current status:** Demonstrated in POC testing and not yet resolved.

### Risk 5: Unproven Effectiveness and Market Demand

**Risk:** The Kindness Gym has not yet demonstrated that users will complete the 21-day programme, change their behaviour, or pay for the product.

**Evidence:** Current evidence shows activity in the broader wellness market and adoption of comparable apps, but does not establish demand for this specific product.

**Impact:** Investment could be made before product-market fit or behavioural effectiveness is established.

**Mitigation:** Use the Round 1 survey as exploratory validation, then run a small pilot measuring sign-up, completion, repeat use, perceived usefulness and willingness to pay.

**Current status:** Unvalidated. An exploratory survey of 90 respondents has been completed, but actual adoption, willingness to pay and behaviour change remain untested.

### Risk 6: Harmful or Inappropriate Guidance

**Risk:** The AI may generate advice that is poorly suited to the user's situation, especially when context is incomplete.

**Impact:** A response could encourage guilt, self-sacrifice, avoidance of accountability or other unhelpful behaviour.

**Mitigation:** Use explicit prompt safeguards, test against difficult scenarios, introduce output validation, and escalate or refuse where the situation falls outside the app's intended scope.

**Current status:** Partly addressed through prompt refinement and manual evaluation, but broader safety testing is still required.