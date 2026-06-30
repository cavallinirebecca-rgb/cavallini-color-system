"""Datové modely pro výsledky analýzy."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CMYValues:
    c: float
    m: float
    y: float

    def as_tuple(self) -> tuple[float, float, float]:
        return self.c, self.m, self.y


@dataclass(frozen=True)
class AnalysisResult:
    c: float
    m: float
    y: float
    k: float

    lab_l: Optional[float]
    lch_c: Optional[float]

    mode: str
    main_color: Optional[str]
    subtracted: float
    remainders: CMYValues

    undertone: Optional[str]
    simplified_undertone: Optional[str]

    brightness: Optional[str]
    saturation: Optional[str]

    season: Optional[str]
    decision_reason: Optional[str]

    @property
    def remainder_c(self) -> float:
        return self.remainders.c

    @property
    def remainder_m(self) -> float:
        return self.remainders.m

    @property
    def remainder_y(self) -> float:
        return self.remainders.y
