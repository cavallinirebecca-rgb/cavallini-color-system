"""Konstanty a mapovací tabulky pro Cavallini Color System."""

from typing import Final

MODE_SPECTRAL: Final = "Spektrální"
MODE_NON_SPECTRAL: Final = "Nespektrální"
MODES: Final = [MODE_SPECTRAL, MODE_NON_SPECTRAL]

MAIN_COLORS: Final = [
    "modrá",
    "červená",
    "žlutá",
    "zelená",
    "oranžová",
    "fialová",
]

SPECTRAL_SUBTRACT_PAIRS: Final[dict[str, tuple[str, str]]] = {
    "modrá": ("C", "Y"),
    "červená": ("M", "Y"),
    "žlutá": ("C", "M"),
    "zelená": ("C", "Y"),
    "oranžová": ("M", "Y"),
    "fialová": ("C", "M"),
}

SIMPLIFY_UNDERTONE: Final[dict[str, str]] = {
    "žluto-oranžová": "oranžová",
    "červeno-oranžová": "oranžová",
    "modro-zelená": "zelená",
    "červeno-zelená": "zelená",
    "modro-fialová": "fialová",
    "žluto-fialová": "fialová",
}

UNDERTONE_SEASON: Final[dict[str, str]] = {
    "žlutá": "JARO",
    "oranžová": "JARO",
    "žluto-oranžová": "JARO",
    "červená": "PODZIM",
    "červeno-oranžová": "PODZIM",
    "modrá": "ZIMA",
    "fialová": "ZIMA",
    "modro-fialová": "ZIMA",
    "červeno-fialová": "ZIMA",
    "zelená": "LÉTO",
    "modro-zelená": "LÉTO",
    "žluto-zelená": "LÉTO",
}

SEASONS: Final = ["JARO", "LÉTO", "PODZIM", "ZIMA"]

SEASON_LABELS: Final[dict[str, str]] = {
    "JARO": "Jaro",
    "LÉTO": "Léto",
    "PODZIM": "Podzim",
    "ZIMA": "Zima",
}

EPSILON: Final = 1e-6
BALANCE_THRESHOLD: Final = 0.20
