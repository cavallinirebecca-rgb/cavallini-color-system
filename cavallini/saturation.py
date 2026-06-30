def classify_saturation(chroma_value: float) -> str:
    """
    Určí saturaci z hodnoty C v CIE LCH.
    C = chroma / sytost barvy.
    """

    if chroma_value >= 35:
        return "vysoká"
    return "nízká"