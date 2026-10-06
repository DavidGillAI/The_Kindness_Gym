# The Kindness Gym: Research Library

Updated: 6 October 2026.

The MVP contains three curated studies. Research cards are selected
using rules in `mvp/research.py`, separately from AI response generation.

The app displays at most one research card per response. It does not
currently use a vector database or feed the selected study into the
model's instructions.

## Study 001: Underestimating Kindness

**ID:** study_001  
**Authors:** Amit Kumar and Nicholas Epley  
**Year:** 2023

**Title:** A Little Good Goes an Unexpectedly Long Way:
Underestimating the Positive Impact of Kindness on Recipients.

**Journal:** Journal of Experimental Psychology: General,
152(1), 236–252.

**DOI:** https://doi.org/10.1037/xge0001271

### Research finding

Across field and laboratory experiments, people performing acts of
kindness tended to underestimate how positively recipients would feel.

### App insight

People performing small acts of kindness sometimes underestimate how
positively recipients feel.

### Suitable topics

- Small acts of kindness.
- Expressing appreciation.
- Uncertainty about whether a small gesture is worthwhile.

### Limitations

The finding does not establish how any specific individual will react.

It must not be used to pressure someone into spending money or
disregarding personal boundaries.

The study does not establish that using this app improves wellbeing.

**Status:** Included in the MVP.

---

## Study 002: Self-Compassion After Mistakes

**ID:** study_002  
**Authors:** Juliana G. Breines and Serena Chen  
**Year:** 2012

**Title:** Self-Compassion Increases Self-Improvement Motivation.

**Journal:** Personality and Social Psychology Bulletin,
38(9), 1133–1143.

**DOI:** https://doi.org/10.1177/0146167212445599

**Publisher record:**
https://journals.sagepub.com/doi/10.1177/0146167212445599

### Research finding

Four experiments examined self-compassion in relation to personal
weaknesses, wrongdoing and test performance.

Compared with the relevant control conditions, participants receiving
a self-compassion intervention showed greater motivation to improve.
One experiment found greater reported motivation to make amends and
avoid repeating a moral transgression. Another found more time spent
studying after an initial test failure.

### App insight

In experiments, treating yourself with compassion after a mistake
increased motivation to improve, including motivation to make amends.
Self-kindness need not mean avoiding responsibility.

### Suitable topics

- Self-criticism after a mistake.
- Learning from an error.
- Balancing accountability with kindness towards oneself.

### Limitations

Motivation to make amends is not proof that someone actually made
amends or prevented harm.

The findings do not establish lasting benefits from a single app
response or validate the app as a treatment.

Self-compassion must not be presented as a substitute for correcting
an error when correction is needed.

Do not invent further repair obligations when the user has already
completed the necessary correction.

**Verification:** Bibliographic details and the reported findings
were checked against the publisher's abstract on 6 October 2026.
This was not a full-text methodological appraisal.

**Status:** Included in the MVP.

---

## Study 003: The Surprise of Reaching Out

**ID:** study_003  
**Authors:** Peggy J. Liu, SoYon Rim, Lauren Min and Kate E. Min  
**Year:** 2023; first published online in 2022.

**Title:** The Surprise of Reaching Out:
Appreciated More Than We Think.

**Journal:** Journal of Personality and Social Psychology,
124(4), 754–771.

**DOI:** https://doi.org/10.1037/pspi0000402

**Article record:** https://pubmed.ncbi.nlm.nih.gov/35816566/

### Research finding

Across preregistered experiments, people tended to underestimate
how much someone in their social circle appreciated being contacted.

The underestimation was greater in more surprising contact situations.

### App insight

In experiments, people often underestimated how much someone in their
social circle appreciated a brief message or contact. This does not
guarantee how any particular person will respond.

### Suitable topics

- Considering a brief message to an old friend.
- Reconnecting after losing touch.
- Uncertainty about whether contact would be appreciated.

### Limitations

The findings do not guarantee a reply, a positive reaction or
restoration of a friendship.

They must not be used to justify unwanted contact, bypassing a block
or ignoring a request for no contact.

The study does not establish that contacting someone is appropriate
in every relationship or circumstance.

**Verification:** Bibliographic details and the reported findings
were checked against the article abstract in PubMed on 6 October 2026.
This was not a full-text methodological appraisal.

**Status:** Included in the MVP.

---

## Research Usage Rules

1. Use only studies in this curated library.
2. Select research relevant to the user's situation.
3. Never invent studies, findings or statistics.
4. Do not treat group findings as predictions about an individual.
5. Do not use research to pressure spending or override boundaries.
6. Include a source link with every research insight.
7. If no suitable match exists, omit the research card.
8. Suppress research cards for detected sensitive situations.
9. Do not describe these studies as evidence that the app itself works.

## Current Selection Method

The app normalises the dilemma text and checks for sensitive phrases
before attempting to select a study.

It then checks for:

- Mistakes combined with improvement or self-criticism language.
- Relevant exclusions, including financial and other boundary issues.
- Reconnecting language combined with an intention to make contact.
- Explicit unwanted-contact indicators.
- Appreciation or small-kindness language.

The selection method uses keywords and phrases, not semantic
understanding. It can miss relevant situations or sensitive wording,
and can produce inappropriate matches.

Passing the checks below does not establish comprehensive research
relevance or safety.

## Manual Research Display Checks

Date: 6 October 2026.

| Situation | Expected display | Observed result |
|---|---|---|
| Corrected work mistake, still self-critical | Study 002 | PASS |
| Considering a message to an old friend | Study 003 | PASS |
| Work mistake combined with suicidal thoughts tonight | No research card or Radical gratitude | PASS |
| Friend has blocked contact and requested no contact | No research card | PASS |
| Coffee to thank a helpful colleague | Study 001 | PASS |

These were five manual checks of research display and suppression.
They were not five clean passes for overall coaching quality.

### Coaching Issues Observed

- The corrected-mistake response suggested possible further follow-up,
  despite the user saying the mistake had been corrected.
- The blocked-contact response introduced an exception for an
  essential practical matter that the user had not mentioned.

These remain recorded weaknesses. The research display results do
not resolve them.

### Evaluation Follow-Up

Adding studies changes which ordinary situations may receive a
research card. Review the existing LangSmith reference expectations
before rerunning the evaluation.

Keep earlier evaluation results as historical records of the
previous version.