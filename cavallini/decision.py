SEASON_RULES = {
    "JARO": {
        "undertones": ["žlutá", "oranžová", "žluto-oranžová"],
        "brightness": "vysoký",
        "saturation": "nízká",
    },
    "LÉTO": {
        "undertones": ["modrá", "zelená", "modro-zelená", "žluto-zelená"],
        "brightness": "nízký",
        "saturation": "nízká",
    },
    "PODZIM": {
        "undertones": ["červená", "oranžová", "červeno-oranžová"],
        "brightness": "nízký",
        "saturation": "vysoká",
    },
    "ZIMA": {
        "undertones": ["modrá", "fialová", "modro-fialová", "červeno-fialová"],
        "brightness": "vysoký",
        "saturation": "vysoká",
    },
}


def decide_season(undertone: str, brightness: str, saturation: str) -> dict:
    """
    Rozhodovací pravidlo:
    - sezóna musí sedět alespoň ve 2 ze 3 vlastností
    - při remíze rozhoduje shoda s podtónem
    """

    results = []

    for season, rules in SEASON_RULES.items():
        score = 0
        undertone_match = undertone in rules["undertones"]

        if undertone_match:
            score += 1

        if brightness == rules["brightness"]:
            score += 1

        if saturation == rules["saturation"]:
            score += 1

        results.append({
            "season": season,
            "score": score,
            "undertone_match": undertone_match,
        })

    valid_results = [r for r in results if r["score"] >= 2]

    if not valid_results:
        return {
            "season": "NEURČENO",
            "reason": "Žádná sezóna nemá shodu alespoň ve 2 vlastnostech.",
            "details": results,
        }

    best_score = max(r["score"] for r in valid_results)
    best_results = [r for r in valid_results if r["score"] == best_score]

    if len(best_results) > 1:
        undertone_priority = [r for r in best_results if r["undertone_match"]]
        if undertone_priority:
            best = undertone_priority[0]
        else:
            best = best_results[0]
    else:
        best = best_results[0]

    return {
        "season": best["season"],
        "reason": "Výsledek odpovídá pravidlu 2 ze 3 vlastností.",
        "details": results,
    }