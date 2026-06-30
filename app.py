"""Cavallini Color System — Streamlit aplikace."""

import streamlit as st

from cavallini import analyze
from cavallini.database import (
    get_last_measurements,
    save_measurement_to_supabase,
)
from cavallini.ui.components import (
    apply_theme,
    render_cmyk_inputs,
    render_header,
    render_mode_inputs,
    render_results,
)
from cavallini.ui.theme import APP_TITLE


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🎨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

apply_theme()
render_header()

# ==========================
# VSTUPNÍ HODNOTY
# ==========================

c, m, y, k, lab_l, lch_c = render_cmyk_inputs()
mode, spectral_color = render_mode_inputs()

# ==========================
# ANALÝZA
# ==========================

if st.button("Analyzovat", type="primary"):
    try:
        st.session_state["analysis"] = analyze(
            c=c,
            m=m,
            y=y,
            k=k,
            mode=mode,
            spectral_color=spectral_color,
            lab_l=lab_l,
            lch_c=lch_c,
        )
    except ValueError as error:
        st.error(str(error))

# ==========================
# VÝSLEDKY
# ==========================

if "analysis" in st.session_state:

    render_results(st.session_state["analysis"])

    st.markdown("---")
    st.subheader("Uložení měření")

    operator = st.text_input(
        "Kdo měřil",
        value="Rebecca",
    )

    customer_name = st.text_input(
        "Jméno klienta / vzorku",
        value="",
    )

    if st.button("💾 Uložit do databáze"):
        try:
            save_measurement_to_supabase(
                st.session_state["analysis"],
                operator=operator,
                customer_name=customer_name,
            )

            st.success("✅ Měření bylo úspěšně uloženo do databáze.")

        except Exception as error:
            st.error(f"❌ Chyba při ukládání: {error}")

# ==========================
# HISTORIE
# ==========================

st.markdown("---")

if st.checkbox("📋 Zobrazit historii měření"):

    try:
        history = get_last_measurements()

        if history:

            visible_history = [
                {
                    "Datum": item.get("created_at", ""),
                    "Operátor": item.get("operator", ""),
                    "Klient": item.get("customer_name", ""),
                    "Režim": item.get("mode", ""),
                    "Hlavní barva": item.get("main_color", ""),
                    "Podtón": item.get("undertone", ""),
                    "Jas": item.get("brightness", ""),
                    "Saturace": item.get("saturation", ""),
                    "Sezóna": item.get("season", ""),
                }
                for item in history
            ]

            st.dataframe(
                visible_history,
                use_container_width=True,
                hide_index=True,
            )

        else:
            st.info("Databáze zatím neobsahuje žádná měření.")

    except Exception as error:
        st.error(f"Nelze načíst historii: {error}")