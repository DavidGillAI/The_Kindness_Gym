STUDY_001 = {
    "id": "study_001",
    "insight": (
        "People performing small acts of kindness sometimes "
        "underestimate how positively recipients feel."
    ),
    "url": "https://doi.org/10.1037/xge0001271",
}


def select_research(dilemma: str) -> dict | None:
    text = dilemma.lower()

    possible_match = (
        any(word in text for word in ("thank", "compliment", "appreciat"))
        or (
            "coffee" in text
            and any(word in text for word in ("colleague", "coworker"))
        )
    )

    boundary_or_other_issue = any(
        word in text
        for word in (
            "€", "afford", "homeless", "tip", "guilt", "money",
            "mistake", "apolog", "misinform", "exhaust",
        )
    )

    if possible_match and not boundary_or_other_issue:
        return dict(STUDY_001)

    return None