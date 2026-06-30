"""Odečítací logika pro spektrální a nespektrální režim."""

from cavallini.models import CMYValues


SPECTRAL_COMPONENTS = {
    "modrá": ("C",),
    "červená": ("M",),
    "žlutá": ("Y",),
    "zelená": ("C", "Y"),
    "oranžová": ("M", "Y"),
    "fialová": ("M", "C"),
}


def spectral_subtract(c: float, m: float, y: float, main_color: str) -> tuple[float, CMYValues]:
    if main_color not in SPECTRAL_COMPONENTS:
        raise ValueError(f"Neznámá spektrální barva: {main_color}")

    values = {"C": c, "M": m, "Y": y}
    components = SPECTRAL_COMPONENTS[main_color]

    if len(components) == 1:
        subtracted = values[components[0]]
    else:
        subtracted = min(values[component] for component in components)

    remainders = dict(values)

    for component in components:
        remainders[component] = max(0.0, values[component] - subtracted)

    return subtracted, CMYValues(
        c=remainders["C"],
        m=remainders["M"],
        y=remainders["Y"],
    )


def non_spectral_subtract(c: float, m: float, y: float) -> tuple[float, CMYValues]:
    subtracted = min(c, m, y)

    return subtracted, CMYValues(
        c=c - subtracted,
        m=m - subtracted,
        y=y - subtracted,
    )