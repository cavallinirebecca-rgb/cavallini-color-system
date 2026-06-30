"""Parser dat z aplikace LScolor."""

import re


def parse_lscolor_text(text: str) -> dict[str, float]:
    """
    Načte hodnoty z textu z LScolor.

    Očekává například:
    Lab: 35.65, 63.32, 38.78
    LCh: 35.65, 74.25, 31.48
    CMYK: 0%, 100%, 85%, 31%
    """

    result = {}

    lab_match = re.search(r"Lab:\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)", text)
    lch_match = re.search(r"LCh:\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)", text)
    cmyk_match = re.search(
        r"CMYK:\s*([\d.]+)%\s*,\s*([\d.]+)%\s*,\s*([\d.]+)%\s*,\s*([\d.]+)%",
        text,
    )

    if lab_match:
        result["lab_l"] = float(lab_match.group(1))

    if lch_match:
        result["lch_c"] = float(lch_match.group(2))

    if cmyk_match:
        result["c"] = float(cmyk_match.group(1))
        result["m"] = float(cmyk_match.group(2))
        result["y"] = float(cmyk_match.group(3))
        result["k"] = float(cmyk_match.group(4))

    return result