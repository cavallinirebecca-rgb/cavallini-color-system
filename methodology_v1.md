# Cavallini Color System — Methodology

This document describes the seasonal color analysis algorithm used by the Cavallini Color System application. The system is designed for **colorimeter-based measurement** (CMYK input). It does not provide styling recommendations — only a calculated undertone and a seasonal classification derived from that undertone.

---

## 1. Overview

The analysis proceeds in four steps:

1. **Input** — CMYK values (C, M, Y, K) on a scale of 0–100, plus an analysis mode.
2. **Subtraction** — Remainder values of C, M, and Y are computed according to the selected mode.
3. **Undertone** — The primary result: a named undertone derived from the remainders.
4. **Season** — A secondary interpretation: which seasonal type the undertone *usually corresponds to* (“Obvykle se řadí mezi”).

The value **K (black)** is recorded and used for color visualization only. It does not participate in undertone or season calculation.

---

## 2. Inputs

| Input | Range | Description |
|-------|-------|-------------|
| C | 0–100 | Cyan |
| M | 0–100 | Magenta |
| Y | 0–100 | Yellow |
| K | 0–100 | Black |
| Mode | Spektrální / Nespektrální | Analysis mode |
| Hlavní barva | modrá, červená, žlutá, zelená, oranžová, fialová | Required in spectral mode only |

---

## 3. Analysis modes

### 3.1 Nespektrální (non-spectral)

Used when the measured color is not treated as a specific spectral hue.

1. Find the minimum of C, M, and Y:
   ```
   subtracted = min(C, M, Y)
   ```
2. Subtract this value from all three components:
   ```
   C' = C − subtracted
   M' = M − subtracted
   Y' = Y − subtracted
   ```
3. Determine the undertone from `(C', M', Y')`.

This removes the neutral grey component shared equally across all three channels. The remainders reveal the undertone.

### 3.2 Spektrální (spectral)

Used when the operator identifies the dominant spectral direction of the measured color. The user selects **Hlavní barva** (main color). Subtraction is applied only to the CMY pair associated with that color; the third component is left unchanged.

For each main color, two components are used. The minimum of those two is subtracted from **both**; the third component is not modified.

| Hlavní barva | Components used | Third unchanged |
|--------------|-----------------|-----------------|
| modrá | C, Y | M |
| červená | M, Y | C |
| žlutá | C, M | Y |
| zelená | C, Y | M |
| oranžová | M, Y | C |
| fialová | C, M | Y |

General formula for spectral subtraction:

```
subtracted = min(value_a, value_b)
a' = a − subtracted
b' = b − subtracted
c' = c          (third component, unchanged)
```

**Example — modrá, C=90, M=20, Y=70:**

```
subtracted = min(90, 70) = 70
C' = 20,  M' = 20,  Y' = 0
```

Undertone from C' + M' → **zelená** (balanced pair; see Section 4).

---

## 4. Undertone determination

Undertone is calculated from the remainder values `(C', M', Y')`. A component is **active** if its value is greater than zero (threshold: 1×10⁻⁶).

### 4.1 Single active component

| Active component | Undertone |
|------------------|-----------|
| C only | modrá |
| M only | červená |
| Y only | žlutá |

### 4.2 Two active components

When exactly two of C', M', Y' are active, the undertone depends on which pair is active and whether the two values are **balanced**.

**Balance rule:** Two values are balanced if their relative difference is **20% or less**:

```
|a − b| / max(a, b) ≤ 0.20
```

If balanced, use the neutral compound undertone:

| Pair | Balanced undertone |
|------|--------------------|
| C + M | zelená |
| M + Y | oranžová |
| C + Y | fialová |

If **not** balanced (difference > 20%), use the directional undertone:

| Pair | Condition | Undertone |
|------|-----------|-----------|
| M + Y | Y > M | žluto-oranžová |
| M + Y | M > Y | červeno-oranžová |
| C + M | C > M | modro-zelená |
| C + M | M > C | červeno-zelená |
| C + Y | C > Y | modro-fialová |
| C + Y | Y > C | žluto-fialová |

**Examples:**

| C' | M' | Y' | Calculation | Undertone |
|----|----|----|-------------|-----------|
| 20 | 20 | 0 | \|20−20\|/20 = 0% | zelená |
| 20 | 17 | 0 | \|20−17\|/20 = 15% | zelená |
| 20 | 15 | 0 | \|20−15\|/20 = 25%, C > M | modro-zelená |
| 0 | 30 | 25 | \|30−25\|/30 ≈ 17% | oranžová |
| 0 | 30 | 20 | \|30−20\|/30 ≈ 33%, M > Y | červeno-oranžová |

### 4.3 Three active components

When all three remainders are active, only the **two highest** values are considered. The pair rules from Section 4.2 are then applied to that pair (using the full C', M', Y' values for balance and direction checks).

### 4.4 No active component

If all remainders are zero, no undertone can be determined. Season classification is not possible.

### 4.5 Simplified undertone (internal)

Mixed undertones can be mapped to a simplified base name. This is used as a fallback for season lookup when a mixed name is not explicitly listed:

| Mixed undertone | Simplified |
|-----------------|------------|
| žluto-oranžová | oranžová |
| červeno-oranžová | oranžová |
| modro-zelená | zelená |
| červeno-zelená | zelená |
| modro-fialová | fialová |
| žluto-fialová | fialová |

The **primary displayed result** is always the full calculated undertone name, not the simplified form.

---

## 5. Season interpretation

Season is derived **from the calculated undertone only**. It is presented in the application as **“Obvykle se řadí mezi”** — an indicative classification, not a styling recommendation.

| Undertone | Season |
|-----------|--------|
| žlutá | JARO |
| oranžová | JARO |
| žluto-oranžová | JARO |
| červená | PODZIM |
| červeno-oranžová | PODZIM |
| modrá | ZIMA |
| fialová | ZIMA |
| modro-fialová | ZIMA |
| červeno-fialová | ZIMA |
| zelená | LÉTO |
| modro-zelená | LÉTO |
| žluto-zelená | LÉTO |

If the calculated undertone is not found in this table, the simplified undertone is tried as a fallback (e.g. červeno-zelená → zelená → LÉTO).

---

## 6. Complete workflow

```
┌─────────────────┐
│  CMYK input     │
│  + mode         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     Spektrální: subtract min of
│  Subtraction    │     selected color pair; leave
│                 │     third component unchanged
│                 │     ─────────────────────────
│                 │     Nespektrální: subtract
│                 │     min(C,M,Y) from all three
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Remainders     │
│  C', M', Y'     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Undertone      │  ← primary result
│  (named)        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Season         │  ← secondary: Obvykle se řadí mezi
│  JARO/LÉTO/     │
│  PODZIM/ZIMA    │
└─────────────────┘
```

---

## 7. Worked examples

### Example A — Non-spectral

**Input:** C=50, M=20, Y=5, K=0, mode=Nespektrální

```
subtracted = min(50, 20, 5) = 5
C' = 45,  M' = 15,  Y' = 0
```

Active: C only → undertone **modrá** → season **ZIMA**.

---

### Example B — Spectral (modrá)

**Input:** C=90, M=20, Y=70, K=0, mode=Spektrální, hlavní barva=modrá

```
subtracted = min(90, 70) = 70
C' = 20,  M' = 20,  Y' = 0
```

C + M active, \|20−20\|/20 = 0% → balanced → undertone **zelená** → season **LÉTO**.

---

### Example C — Spectral (červená)

**Input:** C=10, M=40, Y=25, K=0, mode=Spektrální, hlavní barva=červená

```
subtracted = min(40, 25) = 25
C' = 10,  M' = 15,  Y' = 0
```

C + M active, \|10−15\|/15 ≈ 33%, M > C → undertone **červeno-zelená** → simplified **zelená** → season **LÉTO**.

---

## 8. Implementation reference

```
cavallini color system/
├── app.py                      # Streamlit entry point
├── requirements.txt
├── methodology.md
└── cavallini/
    ├── __init__.py             # Public API exports
    ├── constants.py            # Modes, color names, mapping tables
    ├── models.py               # AnalysisResult, CMYValues dataclasses
    ├── subtraction.py          # Spectral and non-spectral subtraction
    ├── undertone.py            # Undertone detection and simplification
    ├── season.py               # Season mapping from undertone
    ├── analysis.py             # analyze() orchestration
    ├── color_utils.py          # CMYK → hex conversion
    └── ui/
        ├── theme.py            # CSS and app branding
        └── components.py       # Streamlit UI components
```

Core functions:

- `analyze()` — runs the full pipeline and returns an `AnalysisResult`
- `spectral_subtract()` / `non_spectral_subtract()` — compute CMY remainders
- `detect_undertone()` — names the undertone from remainder CMY values
- `_is_balanced_pair()` — applies the 20% balance rule
- `get_season_from_undertone()` — maps undertone to seasonal type

---

## 9. Output fields

The `analyze()` function returns an `AnalysisResult` dataclass:

| Field | Description |
|-------|-------------|
| `c`, `m`, `y`, `k` | Original input values |
| `mode` | Spektrální or Nespektrální |
| `main_color` | Selected spectral color (spectral mode only) |
| `subtracted` | Value removed during subtraction |
| `remainders` | `CMYValues` dataclass with post-subtraction C, M, Y |
| `undertone` | **Primary result** — calculated undertone name |
| `simplified_undertone` | Simplified name (internal / fallback) |
| `season` | JARO, LÉTO, PODZIM, or ZIMA |

---

## 10. Limitations

- The algorithm operates on CMY remainders; K affects visual preview only.
- Spectral mode requires the operator to select the correct main color for the measurement context.
- Season is an interpretation of undertone, not a pair-based or multi-factor classification.
- Undertones not listed in the season table (and without a valid simplified fallback) cannot be assigned a season.
