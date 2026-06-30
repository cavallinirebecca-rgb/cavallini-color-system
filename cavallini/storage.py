"""Ukládání měření Cavallini Color System."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from cavallini.models import AnalysisResult


DATA_DIR = Path("data")
MEASUREMENTS_FILE = DATA_DIR / "measurements.csv"


def ensure_storage() -> None:
    DATA_DIR.mkdir(exist_ok=True)

    if not MEASUREMENTS_FILE.exists():
        with MEASUREMENTS_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "datetime",
                "name",
                "mode",
                "main_color",
                "c",
                "m",
                "y",
                "k",
                "lab_l",
                "lch_c",
                "subtracted",
                "remainder_c",
                "remainder_m",
                "remainder_y",
                "undertone",
                "simplified_undertone",
                "brightness",
                "saturation",
                "season",
                "decision_reason",
            ])


def save_measurement(result: AnalysisResult, name: str = "") -> None:
    ensure_storage()

    with MEASUREMENTS_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            name,
            result.mode,
            result.main_color or "",
            result.c,
            result.m,
            result.y,
            result.k,
            result.lab_l,
            result.lch_c,
            result.subtracted,
            result.remainder_c,
            result.remainder_m,
            result.remainder_y,
            result.undertone or "",
            result.simplified_undertone or "",
            result.brightness or "",
            result.saturation or "",
            result.season or "",
            result.decision_reason or "",
        ])


def read_measurements() -> list[dict[str, str]]:
    ensure_storage()

    with MEASUREMENTS_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def get_measurements_file_path() -> Path:
    ensure_storage()
    return MEASUREMENTS_FILE