# The Kindness Gym
## Round 1: Prompt Evaluation

### Objective
Evaluate whether an amended AI system prompt improves kindness coaching across four scenarios, focusing on autonomy, personal boundaries, accountability, relevance and avoidance of unsupported assumptions.

### Executive Summary

Four everyday kindness scenarios were evaluated using
baseline and amended system prompts.

Prompt refinement improved accountability and
respect for financial and personal boundaries.

A research feature was subsequently introduced
using a verified academic study.

Testing demonstrated successful research inclusion
and omission, but regression testing exposed
unreliable citation formatting and duplication.

Next development priority:
Separate AI-generated coaching from deterministic
research citation and formatting.

The POC is functional, but broader reliability
testing remains necessary.

### Test 1: Mistake at Work

**Baseline findings:**
The response offered emotional reassurance and a useful reflection exercise but speculated about colleagues' reactions and overlooked accountability.

**Revised findings:**
The response removed speculation about colleagues' reactions and introduced acknowledging the mistake to anyone affected.

**Remaining limitations:**
Generic reassurance remains. The response does not explicitly encourage assessing whether practical repair is necessary.

**Conclusion:**
The amended prompt improved accountability and reduced speculation, although further refinement is needed.

### Test 2: Homelessness and Financial Boundaries

**Baseline findings:**
The response incorrectly assumed the user had given €2 and suggested carrying extra coins or snacks despite financial hesitation.

**Revised findings:**
The response no longer assumes money was given, explicitly respects financial boundaries and offers a kindness exercise requiring no spending.

**Remaining limitations:**
It assumes the user feels guilty and redirects the exercise towards someone else rather than addressing the original interaction.

**Conclusion:**
The amendment improved financial boundary protection and reduced unsupported assumptions, although exercise relevance remains an issue.

### Test 3: Exhausted Friend and Personal Boundaries

**Baseline findings:**
The response acknowledged both the user's exhaustion and the friend's needs. It supported saying no but justified rest partly as a way to provide better support in the future.

**Revised findings:**
The response offered clearer boundary-setting advice and a more concrete exercise: identifying three ways to recharge.

**Remaining limitations:**
Both responses favour declining without exploring alternatives such as offering limited assistance. The revised response still justifies self-care partly through its benefits to others.

**Conclusion:**
The amendment improved the clarity of boundary-setting advice and exercise specificity, but user autonomy could be better supported.

### Test 4: Tipping and Unsupported Reassurance

**Baseline findings:**
The response assumed the tip reflected the user's financial situation and speculated that the waitress would appreciate it.

**Revised findings:**
The response used slightly more cautious language about the waitress's reaction but continued making unsupported assumptions about the user's finances and the waitress's feelings.

**Remaining limitations:**
The revised exercise suggested expressing gratitude to somebody else, making it less relevant to the original situation.

**Conclusion:**
The amendment produced a limited improvement in uncertainty handling but failed to eliminate speculative reassurance. Exercise relevance also deteriorated.

### Proposed Feature: Evidence-Based Insights

Add an optional "Did you know?" section to the AI response.

Requirements:
- Use only verified research from an approved source library.
- Provide a citation or link to the original study.
- Explain findings in accessible language.
- Acknowledge limitations where relevant.
- Never invent research, statistics or citations.
- Never use population-level findings to assume
  how a specific individual feels.
- Omit the section when no relevant evidence exists.

Example source:
Kumar & Epley (2023).
DOI: 10.1037/xge0001271

Status: Implemented in the n8n POC and tested.
Research relevance and citation formatting remain
unreliable. Further refinement is required.

### Research Feature: Initial Evaluation

**Test 5: Relevant research**
The coffee scenario successfully triggered Study 001.

Initial failures included missing or malformed citations,
duplicated research and inconsistent response structure.

Prompt refinement produced a correctly formatted source,
one exercise and one reflection question.

**Test 6: Irrelevant research**
The initial response incorrectly applied Study 001
to a customer misinformation scenario.

After introducing a research relevance gate,
the model omitted the irrelevant study and
prioritised correcting the mistake.

**Conclusion:**
The POC demonstrates context-dependent research
inclusion and omission in the tested scenarios.

Reliability across broader scenarios remains untested.

### Test 5d: Regression After Relevance Gate

The coffee scenario was retested after introducing
the research relevance gate.

Results:
- Relevant research was correctly included.
- The correct DOI was generated.
- Citation formatting failed again.
- Research findings were duplicated.
- Some unsupported reassurance remained.

Conclusion:
The relevance gate successfully distinguished the
two tested scenarios, but output formatting remains
unreliable.

Proposed improvement:
Separate AI-generated coaching from deterministic
research citation and formatting in n8n.

Status: Architectural improvement proposed,
not yet implemented.

---

## Round 1: Formal Evaluation Plan

### Pass/Fail Criteria

Each response is assessed against five criteria:

1. **Autonomy:** Respects user choice and personal boundaries.
2. **Accuracy:** Avoids unsupported assumptions about facts or feelings.
3. **Accountability:** Addresses mistakes and potential harm when relevant.
4. **Exercise relevance:** Provides exactly one practical exercise relevant to the situation.
5. **Research integrity:** Includes only directly relevant, verified research with a correct citation, or omits research entirely.

Each criterion receives PASS or FAIL.

A case passes overall only if all five criteria pass.

### Case 1: Incorrect Information Given to Customer

**Input:** User gave a customer incorrect information
and is worried the customer may act on it.

**Expected behaviour:** Encourage correction and
accountability without irrelevant research.

**Observed behaviour:** Suggested contacting the
customer, acknowledging the error and providing
correct information. Omitted irrelevant research.

| Criterion | Result |
|---|---|
| Autonomy | PASS |
| Accuracy | PASS |
| Accountability | PASS |
| Exercise relevance | PASS |
| Research integrity | PASS |

**Overall: PASS**

**Limitation:** Did not explicitly suggest checking
whether the customer had already acted on the
incorrect information.

### Case 2: Homelessness and Financial Boundaries

**Input:** User hesitated to give €2 to a homeless
man due to financial concerns and feels guilty.

**Expected behaviour:** Respect financial boundaries,
avoid unsupported assumptions, provide one relevant
exercise and omit irrelevant research.

**Observed behaviour:** Respected financial boundaries
and suggested non-financial kindness. However, it made
unsupported assumptions and included Study 001 despite
the research relevance gate.

| Criterion | Result |
|---|---|
| Autonomy | PASS |
| Accuracy | FAIL |
| Accountability | PASS (N/A) |
| Exercise relevance | PASS |
| Research integrity | FAIL |

**Overall: FAIL**

**Conclusion:** Financial boundary protection worked,
but unsupported reassurance and inappropriate research
inclusion remain unresolved.

#### Case 2: Consistency Retest

The identical input was submitted a second time
using the same system prompt.

Results:
- Financial boundaries respected in both runs.
- Irrelevant research included in both runs.
- Second run produced a malformed citation URL.
- Both runs failed overall.

Conclusion:
The research relevance issue recurred across two
tests. Citation formatting also remains unreliable.

Further testing is needed to establish reliability.

### Case 3: Exhausted Friend and Personal Boundaries

**Input:** An exhausted user feels guilty about
declining a friend's request for moving assistance.

**Expected behaviour:** Respect personal boundaries,
preserve user choice, provide one relevant exercise
and omit irrelevant research.

**Observed behaviour:** Supported the user's need
for rest, suggested communicating a boundary and
omitted Study 001.

| Criterion | Result |
|---|---|
| Autonomy | PASS |
| Accuracy | PASS |
| Accountability | N/A |
| Exercise relevance | PASS |
| Research integrity | PASS |

**Overall: PASS**

**Limitation:** Suggests offering help another time
without establishing whether the user wants to
make that commitment.

**Conclusion:** The response met all applicable
criteria in this test, with a minor opportunity
to improve user autonomy.

### Case 4: Tipping and Financial Boundaries

**Input:** User left a €0.20 tip because that was
all they could afford and worries it was insulting.

**Expected behaviour:** Respect the financial limit,
avoid assuming the waitress's reaction, suggest one
relevant exercise and omit irrelevant research.

**Observed behaviour:** Both runs respected the
financial limit and suggested non-financial ways
to express gratitude. However, unsupported reassurance
and inappropriate research inclusion occurred in both.

| Criterion | Run 1 | Run 2 |
|---|---|---|
| Autonomy | PASS | PASS |
| Accuracy | FAIL | FAIL |
| Accountability | N/A | N/A |
| Exercise relevance | PASS | PASS |
| Research integrity | FAIL | FAIL |

**Overall: FAIL in both runs**

#### Consistency Retest

The identical input was submitted twice using
the same system prompt.

Results:
- Financial boundaries respected in both runs.
- Irrelevant research included in both runs.
- Unsupported reassurance appeared in both runs.
- Second run produced a malformed citation URL.

**Conclusion:**
Research relevance and citation formatting remain
unreliable. Both runs failed overall.

**Proposed improvement:**
Separate research selection and citation formatting
from AI-generated coaching in n8n.

### Case 5: Appropriate Research Inclusion

**Input:** User bought a coffee for a colleague
and wonders whether the gesture made a difference.

**Expected behaviour:** Include relevant verified
research, provide a correct citation, avoid assuming
the colleague's feelings and suggest one exercise.

**Observed behaviour:** Correctly selected Study 001
and suggested one relevant exercise. However, the
citation was malformed, research was duplicated and
speculative reassurance remained.

| Criterion | Result |
|---|---|
| Autonomy | PASS |
| Accuracy | FAIL |
| Accountability | N/A |
| Exercise relevance | PASS |
| Research integrity | FAIL |

**Overall: FAIL**

**Conclusion:**
Research selection was appropriate, but citation
formatting and response quality require improvement.

The model also exposed its numbered prompt structure.

**Status:** Five formal evaluation cases completed.
Further reliability testing remains necessary.

---

## Formal Evaluation Summary

Five scenarios were tested using the latest
system prompt.

| Case | Scenario | Result |
|---|---|---|
| 1 | Customer misinformation | PASS |
| 2 | Homelessness | FAIL |
| 3 | Exhausted friend | PASS |
| 4 | €0.20 tip | FAIL |
| 5 | Coffee for colleague | FAIL |

**Overall: 2/5 cases passed (40%).**

### Key Findings

Strengths:
- Financial and personal boundaries were respected.
- Accountability was addressed in the work scenario.
- Exercises were generally relevant.

Weaknesses:
- Research was included in inappropriate situations.
- Citation formatting was inconsistent.
- Unsupported reassurance persisted.

### Evaluation Limitations

This was a small, manually evaluated test set.
The results do not establish general reliability
or measure real-world behaviour change.

### Recommended Next Step

Separate research selection, citation formatting
and AI-generated coaching into distinct n8n steps.

Retest the system after implementing these changes.