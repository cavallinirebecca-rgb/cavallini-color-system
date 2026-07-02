"""Orchestrace sezónní analýzy barev."""

from typing import Optional

from cavallini.brightness import classify_brightness
from cavallini.constants import MODE_NON_SPECTRAL, MODE_SPECTRAL
from cavallini.decision import decide_season
from cavallini.models import AnalysisResult
from cavallini.season import get_season_from_undertone
from cavallini.saturation import classify_saturation
from cavallini.subtraction import non_spectral_subtract, spectral_subtract
from cavallini.undertone import detect_undertone, simplify_undertone


NEUTRAL_CHROMA_THRESHOLD = 5


def analyze(
    c: float,
    m: float,
    y: float,
    k: float,
    mode: str,
    spectral_color: Optional[str] = None,
    lab_l: Optional[float] = None,
    lch_c: Optional[float] = None,
) -> AnalysisResult:
    """Provede sezónní analýzu barev."""

    main_color: Optional[str] = None

    if mode == MODE_SPECTRAL:
        if not spectral_color:
            raise ValueError("Spektrální režim vyžaduje výběr hlavní barvy.")
        subtracted, remainders = spectral_subtract(c, m, y, spectral_color)
        main_color = spectral_color
    elif mode == MODE_NON_SPECTRAL:
        subtracted, remainders = non_spectral_subtract(c, m, y)
    else:
        raise ValueError(f"Neznámý režim: {mode}")

    brightness = classify_brightness(lab_l) if lab_l is not None else None
    saturation = classify_saturation(lch_c) if lch_c is not None else None

    if lch_c is not None and lch_c < NEUTRAL_CHROMA_THRESHOLD:
        undertone = "neutrální"
        simplified_undertone = "neutrální"
        season = "NEURČENO"
        decision_reason = (
            "Barva má velmi nízkou chromatičnost, proto je vyhodnocena jako neutrální."
        )
    else:
        undertone = detect_undertone(remainders.c, remainders.m, remainders.y)
        simplified_undertone = simplify_undertone(undertone)

        if brightness is not None and saturation is not None and undertone is not None:
            decision = decide_season(undertone, brightness, saturation)
            season = decision["season"]
            decision_reason = decision["reason"]
        else:
            season = get_season_from_undertone(undertone)
            decision_reason = (
                "Sezóna je určena pouze podle podtónu, protože chybí Lab L nebo LCH C."
            )

    return AnalysisResult(
        c=c,
        m=m,
        y=y,
        k=k,
        lab_l=lab_l,
        lch_c=lch_c,
        mode=mode,
        main_color=main_color,
        subtracted=subtracted,
        remainders=remainders,
        undertone=undertone,
        simplified_undertone=simplified_undertone,
        brightness=brightness,
        saturation=saturation,
        season=season,
        decision_reason=decision_reason,
    )