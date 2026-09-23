# The Kindness Gym: Preliminary Green AI Assessment

Assessment date: 23 September 2026
Status: Preliminary Ironhack Round 1 assessment

## 1. Environmental Impact and Project Scope

### Purpose

Identify the main environmental considerations
associated with The Kindness Gym and propose
practical measures to reduce unnecessary
computational resource use.

### Current Architecture

The existing proof of concept uses:

- n8n for workflow automation.
- OpenAI's gpt-4o-mini for response generation.
- A system prompt containing one approved study.
- A simple two-node workflow.

The current POC does not use a vector database,
multiple AI agents or repeated research API calls.

### Environmental Considerations

Potential sources of environmental impact include:

- Electricity consumed during AI inference.
- Energy used by workflow automation and hosting.
- Data storage and network activity.
- Manufacturing and operation of computing hardware.

The Green Software Foundation's Software Carbon
Intensity framework provides a methodology for
assessing operational and embodied emissions.

### Current Measurement Limitations

The project has not measured:

- Electricity consumed per AI interaction.
- Carbon emissions per generated response.
- Energy used by the hosting environment.
- Embodied emissions attributable to the POC.

API token usage alone is insufficient to
establish actual energy consumption or emissions.

Consequently, the project cannot currently
report a verified carbon footprint.

### Preliminary Conclusion

The environmental assessment will focus on
avoiding unnecessary computation, measuring
resource usage where practical and documenting
the limitations of available data.

Environmental improvements should be evaluated
alongside response quality, reliability and safety.

A smaller model should not automatically be
described as environmentally sustainable
without supporting measurements.

## 2. Computational Efficiency

### Current POC

The existing n8n workflow uses a relatively simple
architecture:

- One chat trigger.
- One OpenAI model node.
- The gpt-4o-mini model.
- A concise response target of approximately
  100–150 words.

The POC does not currently use multiple AI agents,
a vector database or additional research API calls.

This limits architectural complexity, but actual
energy consumption has not been measured.

### Proposed Pilot Improvements

The pilot should investigate the following measures:

1. Continue testing smaller models before considering
   more computationally expensive alternatives.

2. Minimise unnecessary model calls and repeated
   processing of the same information.

3. Keep prompts and generated responses concise
   without sacrificing accuracy, safety or usefulness.

4. Select relevant research through controlled
   retrieval rather than repeatedly asking an AI
   model to generate citations.

5. Use deterministic processing for tasks that
   do not require AI, such as citation formatting.

6. Collect token usage, response times and API
   costs to establish operational benchmarks.

### Quality Versus Efficiency

A smaller model is not automatically the appropriate
choice for every task.

Model selection must consider response quality,
research accuracy, user safety and resource use.

The pilot should compare these factors using
the same evaluation scenarios.

### Measurement Limitations

Token counts, latency and API costs can help
identify inefficient behaviour, but they are
not direct measurements of electricity use
or greenhouse-gas emissions.

Any environmental claims would require
additional measurements or defensible estimates.

### Current Status

Simple single-model architecture: Implemented.

Concise response instructions: Implemented.

Automated usage and efficiency monitoring:
Not implemented.

Comparative model efficiency testing:
Not completed.

Verified energy or carbon measurements:
Not available.

## 3. Measurement Plan and Preliminary Conclusion

### Proposed Measurement Plan

During the pilot, record the following metrics:

| Metric | Purpose |
|---|---|
| Input tokens | Measure prompt size |
| Output tokens | Measure generated response length |
| Total tokens per interaction | Track overall model usage |
| Response time | Identify slow or inefficient requests |
| API cost per interaction | Estimate operating costs |
| Evaluation pass rate | Monitor response quality and safety |
| Model calls per interaction | Identify unnecessary processing |

### Proposed Evaluation

Test a consistent set of representative scenarios
using the selected model and workflow.

Compare resource usage alongside the existing
evaluation criteria.

Investigate whether changes to prompts, model
selection or workflow architecture reduce resource
consumption without compromising response quality.

### Environmental Measurement Limitations

These operational metrics are indirect indicators.

They cannot establish actual electricity consumption,
carbon emissions or the environmental impact of
the underlying data centres.

Any future carbon estimate should disclose
its methodology, assumptions and uncertainty.

### Preliminary Conclusion

The Kindness Gym currently uses a simple,
single-model proof of concept.

Its environmental impact has not been measured.

The proposed pilot will prioritise efficient
processing, monitor resource usage and avoid
unnecessary AI requests.

The project should not claim to be carbon-neutral,
sustainable or environmentally friendly without
appropriate supporting evidence.

### Actions Before Public Deployment

1. Implement token, latency and API-cost logging.
2. Establish baseline measurements.
3. Compare model and workflow configurations.
4. Investigate avoidable computation.
5. Reassess environmental impact as usage grows.

### Current Status

Preliminary Green AI assessment completed.

Operational measurement and environmental
verification remain outstanding.