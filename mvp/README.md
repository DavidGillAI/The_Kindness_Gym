# The Kindness Gym MVP

## Purpose

A small web app that helps users think through everyday dilemmas and practise kindness towards themselves and others.

This is an early MVP for Round 2. It is not a validated or production-ready product.

## Current features

- Branded interface with a layout tested on a laptop and phone.
- A form for describing an everyday dilemma.
- AI guidance displayed in separate paragraphs without section headings.
- An optional research card with a source link.
- A loading message while guidance is generated.
- Error handling that preserves the user's input.

## How it works

FastAPI serves the interface and sends the situation to OpenAI using `gpt-4o-mini`.

The system prompt asks for an acknowledgement, a balanced perspective, exactly one practical exercise and one reflection question.

Research selection and citation display are handled separately from the model. The current research library contains one approved study. A keyword filter decides whether to show it.

## Run locally

From the repository root, with dependencies installed and `OPENAI_API_KEY` saved in `mvp/.env`:

```powershell
.\mvp\.venv\Scripts\python.exe -m uvicorn mvp.main:app --port 8001
```

Open http://127.0.0.1:8001/.

The `.env` file and virtual environment are excluded from Git.

## Checks completed

- Submitted a dilemma and received AI guidance.
- Checked paragraph formatting without response section headings.
- Checked that the coffee-for-colleague scenario displays the research card.
- Checked that a financial-boundary scenario omits the research card.
- Submitted the coffee scenario from a Pixel 8 Pro over home Wi-Fi.
- Confirmed the source link opens the correct APA study page.

These are manual development checks, not a controlled evaluation or proof of reliability.

## Known limitations

- The model can still give overly broad reassurance or redirect a user's idea unnecessarily.
- Prompt instructions do not guarantee exactly one exercise or respect for every boundary.
- The keyword research filter can miss relevant situations or select unsuitable ones.
- The model's guidance is not automatically checked for unsupported claims or invented research.
- Error handling has been added but has not yet been systematically tested.
- There is no authentication or rate limiting.
- Local Wi-Fi testing uses HTTP, so traffic between devices is not encrypted.

## Next steps

- Run a fixed evaluation set and record the results.
- Test error handling.
- Expand the approved research library.
- Evaluate better research selection and compare model performance.
- Prepare privacy and security controls before public deployment.

## Positioning

The Kindness Gym supports personal development. It is not therapy or medical advice.