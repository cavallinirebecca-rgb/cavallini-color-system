"""Odečítací logika pro spektrální a nespektrální režim."""

from cavallini.constants import SPECTRAL_SUBTRACT_PAIRS
from cavallini.models import CMYValues


def spectral_subtract(c: float, m: float, y: float, main_color: str) -> tuple[float, CMYValues]:
    if main_color not in SPECTRAL_SUBTRACT_PAIRS:
        raise ValueError(f"Neznámá spektrální barva: {main_color}")

    values = {"C": c, "M": m, "Y": y}
    component_a, component_b = SPECTRAL_SUBTRACT_PAIRS[main_color]
    subtracted = min(values[component_a], values[component_b])

    remainders = dict(values)
    remainders[component_a] = max(0.0, values[component_a] - subtracted)
    remainders[component_b] = max(0.0, values[component_b] - subtracted)

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
