STUDY_001 = {
    "id": "study_001",
    "insight": (
        "People performing small acts of kindness sometimes "
        "underestimate how positively recipients feel."
    ),
    "url": "https://doi.org/10.1037/xge0001271",
}


def select_research(dilemma: str) -> dict | None:
    text = dilemma.casefold().replace("’", "'")
    text = text.replace("‑", "-").replace("–", "-")
    text = " ".join(text.split())

    sensitive_situation = any(
        phrase in text
        for phrase in (
            "suicid", "self-harm", "self harm",
            "end my life", "ending my life",
            "kill myself", "hurt myself", "harm myself",
            "take my own life", "taking my own life",
            "don't want to live", "do not want to live",
            "want to die", "better off without me",
            "hopeless", "can't stay safe", "cannot stay safe",
            "kill someone", "kill him", "kill her", "kill them",
            "hurt someone", "hurt him", "hurt her", "hurt them",
            "harm someone", "harm him", "harm her", "harm them",
            "violen", "weapon", "abus",
        )
    )

    if sensitive_situation:
        return None

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