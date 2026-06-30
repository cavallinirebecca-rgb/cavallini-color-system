def classify_brightness(l_value: float) -> str:
    """
    Určí jas z hodnoty L v CIE Lab.
    L je v rozsahu 0–100.
    """

    if l_value >= 60:
        return "vysoký"
    return "nízký"