# Cavallini Color System
## Methodology v2.0 (Draft)

Tento dokument popisuje druhou generaci algoritmu Cavallini Color System.

Verze 2 rozšiřuje původní algoritmus o hodnocení charakteru barvy. Výsledná sezóna již není určena pouze podtónem, ale kombinací tří vlastností.

---

# Vstupní data

Kolorimetr poskytuje:

- CMYK
- CIE Lab
- CIE LCH

---

# Výpočet

## Krok 1

Určení dominantní barvy.

## Krok 2

Odečtení dominantní barvy (spektrální) nebo minima (nespektrální).

## Krok 3

Výpočet podtónu ze zbytkových hodnot.

Výsledkem je například:

- žlutá
- oranžová
- žluto-oranžová
- červeno-oranžová
- zelená
- modro-zelená
- modrá
- modro-fialová
...

Podtón je hlavním výsledkem algoritmu.

---

# Charakter barvy

Vedle podtónu se určuje také charakter barvy.

## Jas

Určuje se z hodnoty L (CIE Lab).

Výsledek:

- vysoký jas
- nízký jas

## Saturace

Určuje se z hodnoty C (CIE LCH).

Výsledek:

- vysoká saturace
- nízká saturace

---

# Charakteristika sezón

| Sezóna | Podtón | Jas | Saturace |
|--------|---------|------|-----------|
| Jaro | žlutá / oranžová | vysoký | nízká |
| Léto | modrá / zelená | nízký | nízká |
| Podzim | červená / oranžová | nízký | vysoká |
| Zima | modrá / fialová | vysoký | vysoká |

---

# Rozhodovací pravidlo

Každá sezóna je definována třemi vlastnostmi:

- podtón
- jas
- saturace

Barva je přiřazena k sezóně, pokud se shoduje alespoň ve dvou ze tří vlastností.

Pokud lze barvu přiřadit ke dvěma sezónám stejným počtem shodných vlastností, rozhodující je podtón.

Podtón má vždy nejvyšší prioritu.

# Budoucí rozšíření

V dalších verzích systému bude doplněno:

- automatické určení dominantní barvy,
- automatické určení jasu z L,
- automatické určení saturace z C,
- ukládání měření,
- přímé připojení kolorimetru LS170.