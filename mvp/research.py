STUDY_001 = {
    "id": "study_001",
    "insight": (
        "People performing small acts of kindness sometimes "
        "underestimate how positively recipients feel."
    ),
    "url": "https://doi.org/10.1037/xge0001271",
}

STUDY_002 = {
    "id": "study_002",
    "insight": (
        "In experiments, treating yourself with compassion after "
        "a mistake increased motivation to improve, including "
        "motivation to make amends. Self-kindness need not mean "
        "avoiding responsibility."
    ),
    "url": "https://doi.org/10.1177/0146167212445599",
}

STUDY_003 = {
    "id": "study_003",
    "insight": (
        "In experiments, people often underestimated how much "
        "someone in their social circle appreciated a brief "
        "message or contact. This does not guarantee how any "
        "particular person will respond."
    ),
    "url": "https://doi.org/10.1037/pspi0000402",
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

    mistake_context = any(
        phrase in text
        for phrase in (
            "mistake", "made an error", "got something wrong",
            "incorrect information", "wrong information",
            "failed a test", "failed an exam",
        )
    )

    improvement_or_self_criticism = any(
        phrase in text
        for phrase in (
            "learn", "improv", "repair", "make amends",
            "apolog", "guilt", "ashamed", "shame",
            "beating myself up", "hard on myself",
            "self-crit", "forgive myself",
        )
    )

    if mistake_context and improvement_or_self_criticism:
        return dict(STUDY_002)

    boundary_or_other_issue = any(
        word in text
        for word in (
            "€", "afford", "homeless", "tip", "guilt", "money",
            "mistake", "apolog", "misinform", "exhaust",
        )
    )

    if boundary_or_other_issue:
        return None

    reconnecting_context = any(
        phrase in text
        for phrase in (
            "old friend", "lost touch", "haven't spoken",
            "haven't talked", "not spoken for",
            "not talked for", "reconnect",
        )
    )

    contact_context = any(
        phrase in text
        for phrase in (
            "message", "text", "call", "contact",
            "reach out", "reaching out", "get in touch",
        )
    )

    unwanted_contact = any(
        phrase in text
        for phrase in (
            "blocked", "no contact", "leave them alone",
            "leave me alone", "asked me not to",
            "doesn't want contact", "does not want contact",
            "ex-partner", "ex partner", "ex-boyfriend",
            "ex-girlfriend", "restraining order",
        )
    )

    if unwanted_contact:
        return None

    if reconnecting_context and contact_context:
        return dict(STUDY_003)

    kindness_context = (
        any(word in text for word in ("thank", "compliment", "appreciat"))
        or (
            "coffee" in text
            and any(word in text for word in ("colleague", "coworker"))
        )
    )

    if kindness_context:
        return dict(STUDY_001)

    return None