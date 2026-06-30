"""Detekce a zjednodušení podtónu z hodnot CMY."""

from typing import Optional

from cavallini.constants import BALANCE_THRESHOLD, EPSILON, SIMPLIFY_UNDERTONE


def simplify_undertone(undertone: Optional[str]) -> Optional[str]:
    if undertone is None:
        return None
    return SIMPLIFY_UNDERTONE.get(undertone, undertone)


def detect_undertone(c: float, m: float, y: float) -> Optional[str]:
    """Určí podtón z hodnot C, M, Y podle pravidel."""
    has_c = c > EPSILON
    has_m = m > EPSILON
    has_y = y > EPSILON
    active_count = sum((has_c, has_m, has_y))

    if active_count == 0:
        return None

    if active_count == 1:
        if has_c:
            return "modrá"
        if has_m:
            return "červená"
        return "žlutá"

    if active_count == 2:
        return _detect_pair_undertone(has_c, has_m, has_y, c, m, y)

    components = [("C", c), ("M", m), ("Y", y)]
    components.sort(key=lambda item: item[1], reverse=True)
    top = {name for name, _ in components[:2]}

    return _detect_pair_undertone(
        "C" in top,
        "M" in top,
        "Y" in top,
        c,
        m,
        y,
    )


def _is_balanced_pair(first: float, second: float) -> bool:
    """Vrátí True, pokud se dvě hodnoty liší nejvýše o 20 %."""
    higher = max(first, second)
    if higher <= EPSILON:
        return True
    return abs(first - second) / higher <= BALANCE_THRESHOLD


def _detect_pair_undertone(
    has_c: bool,
    has_m: bool,
    has_y: bool,
    c: float,
    m: float,
    y: float,
) -> Optional[str]:
    if has_c and has_m and not has_y:
        if _is_balanced_pair(c, m):
            return "zelená"
        return "modro-zelená" if c > m else "červeno-zelená"

    if has_m and has_y and not has_c:
        if _is_balanced_pair(m, y):
            return "oranžová"
        return "červeno-oranžová" if m > y else "žluto-oranžová"

    if has_c and has_y and not has_m:
        if _is_balanced_pair(c, y):
            return "fialová"
        return "modro-fialová" if c > y else "žluto-fialová"

    components = [("C", c), ("M", m), ("Y", y)]
    components.sort(key=lambda item: item[1], reverse=True)
    top = {name for name, _ in components[:2]}

    return _detect_pair_undertone(
        "C" in top,
        "M" in top,
        "Y" in top,
        c,
        m,
        y,
    )
