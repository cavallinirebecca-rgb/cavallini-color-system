"""Mapování podtónu na sezónní typ."""

from typing import Optional

from cavallini.constants import SEASON_LABELS, UNDERTONE_SEASON
from cavallini.undertone import simplify_undertone


def get_season_from_undertone(undertone: Optional[str]) -> Optional[str]:
    """Vrátí sezónu podle vypočteného podtónu."""
    if undertone is None:
        return None

    season = UNDERTONE_SEASON.get(undertone)
    if season is not None:
        return season

    simplified = simplify_undertone(undertone)
    if simplified is not None:
        return UNDERTONE_SEASON.get(simplified)

    return None


def season_display_name(season: str) -> str:
    """Vrátí český název sezóny."""
    return SEASON_LABELS.get(season, season)
