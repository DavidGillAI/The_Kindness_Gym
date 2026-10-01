from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Form
from html import escape
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).parent / ".env")
client = OpenAI()
SYSTEM_PROMPT = (
    Path(__file__).parent / "system_prompt.txt"
).read_text(encoding="utf-8")
app = FastAPI(title="The Kindness Gym")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html>
    <html lang="en">
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>The Kindness Gym</title>
      <style>
        body { font-family: system-ui, sans-serif; max-width: 42rem;
               margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }
        textarea { box-sizing: border-box; width: 100%; min-height: 10rem;
                   padding: 0.75rem; font: inherit; }
        button { margin-top: 1rem; padding: 0.75rem 1rem; font: inherit; }
      </style>
    </head>
    <body>
      <h1>The Kindness Gym</h1>
      <p>Describe an everyday situation you're unsure how to handle.</p>
      <form action="/coach" method="post">
        <label for="dilemma">What's happening?</label>
        <textarea id="dilemma" name="dilemma" required></textarea>
        <button type="submit">Explore this dilemma</button>
      </form>
  
    </body>
    </html>
    """

@app.post("/coach", response_class=HTMLResponse)
def coach(dilemma: str = Form(...)):
    dilemma = dilemma.strip()

    if not dilemma:
        return HTMLResponse(
            'Please enter a situation. <a href="/">Go back</a>',
            status_code=400,
        )

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=SYSTEM_PROMPT,
        input=dilemma,
        max_output_tokens=600,
        store=False,
    )

    safe_dilemma = escape(dilemma)
    reply = response.output_text

    for heading in (
        "Acknowledgement:",
        "Perspective:",
        "Kindness exercise:",
        "Reflection:",
    ):
        reply = reply.replace("**" + heading + "**", "")
        reply = reply.replace(heading, "")

    safe_reply = escape(reply.strip())

    return f"""
    <!doctype html>
    <html lang="en">
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>The Kindness Gym</title>
      <style>
        body {{ font-family: system-ui, sans-serif; max-width: 42rem;
                margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }}
        .text {{ white-space: pre-wrap; }}
      </style>
    </head>
    <body>
      <h1>The Kindness Gym</h1>
      <h2>Your situation</h2>
      <p class="text">{safe_dilemma}</p>
      <h2>Your guidance</h2>
      <div class="text">{safe_reply}</div>
      <p><a href="/">Explore another situation</a></p>
    </body>
    </html>
    """