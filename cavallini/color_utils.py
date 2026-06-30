"""Pomocné funkce pro práci s barvami."""


def cmyk_to_hex(c: float, m: float, y: float, k: float) -> str:
    """Převede CMYK (0–100) na hex barvu."""
    c_norm = max(0.0, min(100.0, c)) / 100.0
    m_norm = max(0.0, min(100.0, m)) / 100.0
    y_norm = max(0.0, min(100.0, y)) / 100.0
    k_norm = max(0.0, min(100.0, k)) / 100.0

    r = int(round(255 * (1 - c_norm) * (1 - k_norm)))
    g = int(round(255 * (1 - m_norm) * (1 - k_norm)))
    b = int(round(255 * (1 - y_norm) * (1 - k_norm)))

    return f"#{r:02X}{g:02X}{b:02X}"
