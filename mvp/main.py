import re
from html import escape
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from openai import APIError, OpenAI
from time import perf_counter

from mvp.research import select_research


BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")
client = OpenAI(timeout=30.0, max_retries=0)
SYSTEM_PROMPT = (BASE_DIR / "system_prompt.txt").read_text(
    encoding="utf-8"
)

app = FastAPI(title="The Kindness Gym")
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)


def page(content: str) -> str:
    return f"""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>The Kindness Gym</title>
      <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
      <main class="page">
        <a href="/" aria-label="The Kindness Gym home">
          <img class="brand" src="/static/logo.png"
               alt="The Kindness Gym">
        </a>
        {content}
        <footer class="small">
          AI guidance for everyday kindness.
          Personal development, not therapy or medical advice.
        </footer>
      </main>
    </body>
    </html>
    """


def dilemma_form(dilemma: str = "", error: str = "") -> str:
    error_html = (
        f'<p role="alert">{escape(error)}</p>' if error else ""
    )

    return f"""
      <header class="hero">
        <h1>Small steps. More kindness.</h1>
        <p>AI-powered guidance.<br>
        <p>A little space to think through an everyday dilemma.</p>
      </header>

      <section class="card">
        {error_html}
        <form action="/coach" method="post" id="dilemma-form">
          <label for="dilemma">What's on your mind?</label>
          <textarea id="dilemma" name="dilemma" required
                    maxlength="4000"
                    aria-describedby="input-note"
                    placeholder="Describe what's happening and what you're unsure about."
          >{escape(dilemma)}</textarea>
          <p id="input-note" class="small">
            Leave out names and details that could identify someone.
          </p>
          <button type="submit" id="submit-button">
            Explore this dilemma
          </button>
          <p id="loading-message" class="small"
             role="status" hidden>
            Taking a moment to think this through…
          </p>
        </form>
      </section>

      <script>
        const form = document.getElementById("dilemma-form");
        const button = document.getElementById("submit-button");
        const message = document.getElementById("loading-message");

        form.addEventListener("submit", function () {{
          button.disabled = true;
          button.textContent = "Thinking…";
          message.hidden = false;
        }});

        window.addEventListener("pageshow", function () {{
          button.disabled = false;
          button.textContent = "Explore this dilemma";
          message.hidden = true;
        }});
      </script>
    """


def guidance_html(reply: str) -> str:
    headings = (
        "Acknowledgement:",
        "Perspective:",
        "Kindness exercise:",
        "Radical gratitude:",
    )

    for heading in headings:
        reply = reply.replace("**" + heading + "**", heading)

    parts = []
    paragraph = []
    bullets = []
    section = None

    def flush_paragraph():
        if paragraph:
            text = " ".join(paragraph)
            parts.append(f"<p>{escape(text)}</p>")
            paragraph.clear()

    def flush_bullets():
        if bullets:
            items = "".join(
                f"<li>{escape(text)}</li>" for text in bullets
            )
            parts.append(f"<ul>{items}</ul>")
            bullets.clear()

    for line in reply.splitlines():
        text = re.sub(r"^#{1,6}\s*", "", line.strip())

        if text in headings:
            flush_paragraph()
            flush_bullets()
            section = text

            if section == "Radical gratitude:":
                parts.append("<h2>Radical gratitude</h2>")

            continue

        if not text:
            flush_paragraph()
            continue

        is_bullet = bool(re.match(r"^[-*•]\s+", text))

        if section in ("Acknowledgement:", "Perspective:"):
            flush_bullets()

            if is_bullet:
                text = re.sub(r"^[-*•]\s+", "", text)

            paragraph.append(text)

        elif is_bullet:
            flush_paragraph()
            bullets.append(re.sub(r"^[-*•]\s+", "", text))

        else:
            flush_bullets()
            paragraph.append(text)

    flush_paragraph()
    flush_bullets()

    return "".join(parts)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def home():
    return page(dilemma_form())


@app.post("/coach", response_class=HTMLResponse)
def coach(dilemma: str = Form(...)):
    dilemma = dilemma.strip()

    if not dilemma or len(dilemma) > 4000:
        return HTMLResponse(
            page(dilemma_form(
                dilemma,
                "Please enter a situation using 1–4,000 characters.",
            )),
            status_code=400,
        )
    started = perf_counter()
    try:
        response = client.responses.create(
            # model="gpt-4o-mini",
            model="gpt-5.6-luna",
            # model="gpt-5.6-sol",
            reasoning={"effort": "none"},
            instructions=SYSTEM_PROMPT,
            input=dilemma,
            max_output_tokens=3000,
            store=False,
        )
    except APIError:
        return HTMLResponse(
            page(dilemma_form(
                dilemma,
                "We couldn't put together a response just now. "
                "Your situation is still here, so you can try again.",
            )),
            status_code=502,
        )
    elapsed = perf_counter() - started

    print(
        f"METRICS model={response.model} "
        f"seconds={elapsed:.2f} status={response.status}",
        flush=True,
    )

    if response.usage:
        print(
        f"REASONING requested=none returned={response.reasoning}",
        flush=True,
    )
        print(
            "TOKEN_USAGE " + response.usage.model_dump_json(),
            flush=True,
        )
    if not response.output_text.strip():
        return HTMLResponse(
            page(dilemma_form(
                dilemma,
                "No response came back this time. Please try again.",
            )),
            status_code=502,
        )

    research = select_research(dilemma)
    research_html = ""

    if research:
        research_html = f"""
          <aside class="card research">
            <h2>Did you know?</h2>
            <p>{escape(research["insight"])}</p>
            <a href="{escape(research["url"], quote=True)}"
               target="_blank" rel="noopener noreferrer">
              Read the study ↗
            </a>
          </aside>
        """

    content = f"""
      <header class="hero">
        <h1>A moment for kindness.</h1>
        <p>AI-powered guidance.<br>
Take what helps, and choose what feels right for you.</p>
      </header>

      <section class="card">
        <h2>Your situation</h2>
        <p class="situation">{escape(dilemma)}</p>
      </section>

      <section class="card guidance">
        <h2>TKG’s perspective</h2>

        {guidance_html(response.output_text)}
    <p class="support-link">
       Need someone to talk to?
        <a href="https://findahelpline.com/"
           target="_blank" rel="noopener noreferrer">
          Find support in your country
        </a>
        </section>
    </p>

      {research_html}
<div class="response-actions">
        <br></br>
  <a class="button" href="/">Explore another situation</a>
  <p>
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSdm-tMulOPi0rw3CGlQLSgsmFpl9-BliaeHqdbV1_PvUhbqdg/viewform"
       target="_blank" rel="noopener noreferrer">
      Share feedback or suggest a feature ↗
    </a>
  </p>
</div>
</p>
            <p class="support-link">
       
      </p>
    """

    return page(content)