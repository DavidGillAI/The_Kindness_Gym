# Kindness Gym n8n Proof of Concept

## Purpose

This proof of concept demonstrates how The Kindness Gym can respond to everyday dilemmas with short, personalised kindness guidance.

The current workflow is intentionally small and is designed to test the AI interaction rather than represent the full product.

## Current Workflow

The n8n workflow contains two main nodes:

1. Chat Trigger
2. OpenAI "Message a model" node

The chat message is passed directly to the model for response generation.

## Model

The current POC uses:

`gpt-4o-mini`

This model was selected for a lightweight and inexpensive proof of concept.

## Current Response Design

The system prompt instructs the AI to provide:

- A brief acknowledgement
- A balanced perspective
- Exactly one practical kindness exercise
- An optional research-based "Did you know?" section
- One reflection question

The prompt also includes safeguards around:

- Personal boundaries
- Financial pressure
- Accountability and repair
- Uncertainty about other people's feelings
- Avoiding unsupported reassurance
- Avoiding therapy or medical positioning

## Research Feature

The POC currently includes one approved research study directly inside the system prompt.

Research should only appear when it is directly relevant to the user's situation.

This is a temporary POC implementation. A production system should separate research retrieval and citation handling from free-text response generation.

## Current Evaluation Result

The latest five-case evaluation produced:

- 2 PASS
- 3 FAIL

Overall pass rate: 40%

The strongest areas were:

- Respecting personal and financial boundaries
- Accountability in the work-mistake scenario
- Generally relevant kindness exercises

The main failures were:

- Research being included when it was not directly relevant
- Inconsistent citation formatting
- Occasional unsupported reassurance

## Main Technical Learning

Prompt instructions alone are not sufficiently reliable for research selection and citation formatting.

A stronger architecture would separate:

1. User-situation interpretation
2. Research retrieval
3. Citation formatting
4. AI coaching response generation

## Current Status

The workflow is suitable as a Round 1 proof of concept.

It is not production-ready and should not be presented as a validated product.