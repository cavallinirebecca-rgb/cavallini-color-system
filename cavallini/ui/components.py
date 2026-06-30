"""Streamlit UI komponenty."""

import streamlit as st

from cavallini.color_utils import cmyk_to_hex
from cavallini.constants import MAIN_COLORS, MODE_SPECTRAL, MODES
from cavallini.models import AnalysisResult
from cavallini.season import season_display_name
from cavallini.ui.theme import APP_SUBTITLE, APP_TITLE, CUSTOM_CSS


def render_header() -> None:
    st.title(APP_TITLE)
    st.markdown(f'<p class="subtitle">{APP_SUBTITLE}</p>', unsafe_allow_html=True)
    st.markdown("---")


def render_cmyk_inputs() -> tuple[float, float, float, float, float, float]:
    st.subheader("Hodnoty CMYK")
    col_c, col_m, col_y, col_k = st.columns(4)

    with col_c:
        c = st.number_input("C", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    with col_m:
        m = st.number_input("M", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    with col_y:
        y = st.number_input("Y", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    with col_k:
        k = st.number_input("K", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

    st.subheader("CIE hodnoty")
    col_l, col_chroma = st.columns(2)

    with col_l:
        lab_l = st.number_input("Lab L", min_value=0.0, max_value=100.0, value=50.0, step=0.1)

    with col_chroma:
        lch_c = st.number_input("LCH Chroma", min_value=0.0, max_value=150.0, value=35.0, step=0.1)

    return c, m, y, k, lab_l, lch_c


def render_mode_inputs() -> tuple[str, str | None]:
    st.markdown("---")
    st.subheader("Režim analýzy")

    mode = st.radio(
        "Režim",
        options=MODES,
        horizontal=True,
        label_visibility="collapsed",
    )

    spectral_color = None
    if mode == MODE_SPECTRAL:
        spectral_color = st.selectbox(
            "Hlavní barva",
            options=MAIN_COLORS,
            index=0,
        )

    st.markdown("---")
    return mode, spectral_color


def _result_box(label: str, value: str) -> str:
    return (
        f'<div class="result-box">'
        f'<div class="result-label">{label}</div>'
        f'<div class="result-value">{value}</div>'
        f"</div>"
    )


def _color_swatch(hex_color: str, caption: str) -> str:
    return f"""
    <div>
        <div class="color-swatch" style="background-color: {hex_color};"></div>
        <div class="swatch-caption">{caption}</div>
    </div>
    """


def render_results(result: AnalysisResult) -> None:
    measured_hex = cmyk_to_hex(result.c, result.m, result.y, result.k)
    undertone_hex = cmyk_to_hex(
        result.remainder_c,
        result.remainder_m,
        result.remainder_y,
        result.k,
    )

    undertone_text = result.undertone or "—"

    st.subheader("Výsledky analýzy")

    if result.undertone:
        st.markdown(
            f'<div class="undertone-banner">'
            f'<div class="result-label">Vypočtený podtón</div>'
            f'<div class="undertone-name">{undertone_text}</div>'
            f"</div>",
            unsafe_allow_html=True,
        )
    else:
        st.warning("Podtón se nepodařilo určit.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            _result_box(
                "Původní CMYK",
                f"C={result.c:.1f} · M={result.m:.1f} · "
                f"Y={result.y:.1f} · K={result.k:.1f}",
            ),
            unsafe_allow_html=True,
        )
        st.markdown(_result_box("Režim", result.mode), unsafe_allow_html=True)

        if result.mode == MODE_SPECTRAL and result.main_color:
            st.markdown(
                _result_box("Zvolená hlavní barva", result.main_color),
                unsafe_allow_html=True,
            )

    with col2:
        st.markdown(
            _result_box("Odečtená hodnota", f"{result.subtracted:.1f}"),
            unsafe_allow_html=True,
        )
        st.markdown(
            _result_box(
                "Zbytkové C, M, Y",
                f"C={result.remainder_c:.1f} · M={result.remainder_m:.1f} · "
                f"Y={result.remainder_y:.1f}",
            ),
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("Charakter barvy")

    char_col1, char_col2, char_col3 = st.columns(3)

    with char_col1:
        st.markdown(
            _result_box("Lab L / jas", f"{result.lab_l:.1f} → {result.brightness}"),
            unsafe_allow_html=True,
        )

    with char_col2:
        st.markdown(
            _result_box("LCH C / saturace", f"{result.lch_c:.1f} → {result.saturation}"),
            unsafe_allow_html=True,
        )

    with char_col3:
        st.markdown(
            _result_box("Rozhodnutí", result.decision_reason or "—"),
            unsafe_allow_html=True,
        )

    if result.season:
        season_label = season_display_name(result.season)
        st.markdown(
            f'<div class="season-banner">'
            f'<div class="result-label">Obvykle se řadí mezi</div>'
            f'<div class="season-name">{result.season}</div>'
            f'<div class="result-label">{season_label}</div>'
            f"</div>",
            unsafe_allow_html=True,
        )
    elif result.undertone:
        st.warning("Sezónu se nepodařilo určit pro vypočtený podtón.")

    st.subheader("Náhled barev")
    preview_col1, preview_col2 = st.columns(2)

    with preview_col1:
        st.markdown(_color_swatch(measured_hex, "Naměřená barva"), unsafe_allow_html=True)

    with preview_col2:
        st.markdown(_color_swatch(undertone_hex, "Vizualizace podtónu"), unsafe_allow_html=True)


def apply_theme() -> None:
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)