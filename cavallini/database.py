"""Napojení na Supabase databázi."""

import streamlit as st
from supabase import create_client

from cavallini.models import AnalysisResult


DEVICE_SN = "170005114"


def get_supabase_client():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)


def save_measurement_to_supabase(
    result: AnalysisResult,
    operator: str = "",
    customer_name: str = "",
) -> None:
    supabase = get_supabase_client()

    data = {
        "operator": operator,
        "customer_name": customer_name,
        "mode": result.mode,
        "main_color": result.main_color,
        "c": result.c,
        "m": result.m,
        "y": result.y,
        "k": result.k,
        "lab_l": result.lab_l,
        "lch_c": result.lch_c,
        "undertone": result.undertone,
        "simplified_undertone": result.simplified_undertone,
        "brightness": result.brightness,
        "saturation": result.saturation,
        "season": result.season,
        "decision_reason": result.decision_reason,
        "device_sn": DEVICE_SN,
    }

    supabase.table("measurements").insert(data).execute()


def get_last_measurements(limit: int = 20):
    supabase = get_supabase_client()

    response = (
        supabase.table("measurements")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )

    return response.data