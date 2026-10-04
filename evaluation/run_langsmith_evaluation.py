import re
import sys
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from time import perf_counter

from dotenv import load_dotenv
from fastapi.testclient import TestClient
from langsmith import Client

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / "mvp" / ".env")

from mvp.main import app

DATASET_NAME = "TKG MVP evaluation v1"


class ReadableText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {"p", "h2", "li", "br"}:
            self.parts.append("\n")
        if tag == "li":
            self.parts.append("- ")

    def handle_endtag(self, tag):
        if tag in {"p", "h2", "li"}:
            self.parts.append("\n")

    def handle_data(self, data):
        self.parts.append(data)

    def text(self):
        lines = [
            line.strip()
            for line in "".join(self.parts).splitlines()
            if line.strip()
        ]
        return "\n".join(lines)


def test_app(inputs: dict) -> dict:
    started = perf_counter()

    with TestClient(app) as web:
        response = web.post(
            "/coach",
            data={"dilemma": inputs["dilemma"]},
        )

    html = response.text
    guidance = re.search(
        r'<section class="card guidance">(.*?)</section>',
        html,
        flags=re.DOTALL,
    )

    reader = ReadableText()
    reader.feed(guidance.group(1) if guidance else html)

    return {
        "response": reader.text(),
        "http_status": response.status_code,
        "seconds": round(perf_counter() - started, 2),
        "guidance_present": guidance is not None,
        "research_present": '<aside class="card research">' in html,
        "gratitude_present": (
            "<h2>Radical gratitude</h2>" in html
            or "<h2>Radical gratitude:</h2>" in html
        ),
        "page_html": html,
    }


def request_succeeded(outputs: dict) -> bool:
    return (
        outputs["http_status"] == 200
        and outputs["guidance_present"]
        and bool(outputs["response"].strip())
    )


def research_display_matches(
    outputs: dict, reference_outputs: dict
) -> bool:
    return (
        request_succeeded(outputs)
        and outputs["research_present"]
        == reference_outputs["research_expected"]
    )


def gratitude_display_matches(
    outputs: dict, reference_outputs: dict
) -> bool:
    return (
        request_succeeded(outputs)
        and outputs["gratitude_present"]
        == reference_outputs["gratitude_expected"]
    )


def main():
    fingerprints = {
        filename: sha256(
            (ROOT / "mvp" / filename).read_bytes()
        ).hexdigest()
        for filename in (
            "main.py",
            "system_prompt.txt",
            "research.py",
        )
    }

    Client().evaluate(
        test_app,
        data=DATASET_NAME,
        evaluators=[
            request_succeeded,
            research_display_matches,
            gratitude_display_matches,
        ],
        experiment_prefix="TKG-MVP-first-evaluation",
        description=(
            "Ten fictional cases through the actual FastAPI app. "
            "Automatic display checks; response quality needs human review."
        ),
        metadata={"file_fingerprints": fingerprints},
        max_concurrency=1,
    )


if __name__ == "__main__":
    main()