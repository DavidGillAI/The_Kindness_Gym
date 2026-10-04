import json
from pathlib import Path

from dotenv import load_dotenv
from langsmith import Client

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / "mvp" / ".env")

DATASET_NAME = "TKG MVP evaluation v1"


def main():
    cases = json.loads(
        (ROOT / "evaluation" / "mvp_test_cases.json").read_text(
            encoding="utf-8"
        )
    )
    client = Client()

    if client.has_dataset(dataset_name=DATASET_NAME):
        dataset = client.read_dataset(dataset_name=DATASET_NAME)
    else:
        dataset = client.create_dataset(
            dataset_name=DATASET_NAME,
            description=(
                "Ten fictional Kindness Gym cases: everyday dilemmas, "
                "sensitive situations, safeguard override and research "
                "suppression. Expected behaviour requires human review."
            ),
        )

    existing_ids = {
        (example.metadata or {}).get("case_id")
        for example in client.list_examples(dataset_id=dataset.id)
    }

    added = 0

    for case in cases:
        if case["id"] in existing_ids:
            continue

        client.create_example(
            dataset_id=dataset.id,
            inputs=case["inputs"],
            outputs=case["outputs"],
            metadata={
                "case_id": case["id"],
                "category": case["outputs"]["category"],
                "fictional": True,
            },
        )
        existing_ids.add(case["id"])
        added += 1

    print(f"Dataset: {DATASET_NAME}")
    print(f"Examples added: {added}")
    print(f"Cases present: {sum(c['id'] in existing_ids for c in cases)}")


if __name__ == "__main__":
    main()