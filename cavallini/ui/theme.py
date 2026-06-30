"""Vzhled a styly aplikace."""

APP_TITLE = "Cavallini Color System"
APP_SUBTITLE = "Sezónní analýza barev"

GOLD_PRIMARY = "#C9A227"
GOLD_DARK = "#9A7B1A"
GOLD_LIGHT = "#F5E6B8"
TEXT_PRIMARY = "#1A1A1A"
TEXT_MUTED = "#666666"
BORDER = "#E8E0C8"

CUSTOM_CSS = f"""
<style>
    .stApp {{
        background-color: #FFFFFF;
    }}
    .block-container {{
        padding-top: 2rem;
        max-width: 820px;
    }}
    h1 {{
        color: {TEXT_PRIMARY};
        font-weight: 600;
        letter-spacing: -0.02em;
    }}
    .subtitle {{
        color: {TEXT_MUTED};
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }}
    div[data-testid="stRadio"] label {{
        font-weight: 500;
    }}
    .stNumberInput label, .stSelectbox label {{
        color: {TEXT_PRIMARY};
    }}
    hr {{
        border-color: {BORDER};
        margin: 1.5rem 0;
    }}
    div[data-testid="stFormSubmitButton"] button,
    .stButton > button {{
        background-color: {GOLD_PRIMARY};
        color: white;
        border: none;
        border-radius: 6px;
    }}
    div[data-testid="stFormSubmitButton"] button:hover,
    .stButton > button:hover {{
        background-color: {GOLD_DARK};
        color: white;
        border: none;
    }}
    .result-box {{
        background: #FAFAF8;
        border: 1px solid {BORDER};
        border-left: 4px solid {GOLD_PRIMARY};
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }}
    .result-label {{
        color: {TEXT_MUTED};
        font-size: 0.85rem;
        margin-bottom: 0.15rem;
    }}
    .result-value {{
        color: {TEXT_PRIMARY};
        font-size: 1.05rem;
        font-weight: 600;
    }}
    .season-banner {{
        background: linear-gradient(135deg, {GOLD_LIGHT} 0%, #FFFFFF 100%);
        border: 1px solid {BORDER};
        border-radius: 10px;
        padding: 1rem 1.25rem;
        text-align: center;
        margin: 1rem 0;
    }}
    .season-name {{
        color: {GOLD_DARK};
        font-size: 1.5rem;
        font-weight: 700;
        letter-spacing: 0.08em;
    }}
    .undertone-banner {{
        background: #FFFFFF;
        border: 2px solid {GOLD_PRIMARY};
        border-radius: 10px;
        padding: 1.25rem;
        text-align: center;
        margin: 1rem 0;
    }}
    .undertone-name {{
        color: {TEXT_PRIMARY};
        font-size: 2rem;
        font-weight: 700;
    }}
    .color-swatch {{
        width: 100%;
        height: 90px;
        border-radius: 8px;
        border: 1px solid {BORDER};
        margin-top: 0.5rem;
    }}
    .swatch-caption {{
        color: {TEXT_MUTED};
        font-size: 0.8rem;
        text-align: center;
        margin-top: 0.35rem;
    }}
</style>
"""
