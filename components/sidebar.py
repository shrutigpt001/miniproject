
"""Edumind Ai sidebar: branding, navigation and live model status."""
from __future__ import annotations

import streamlit as st

from components.context import NAV_PAGES, get_status
from components.metrics import status_pill


ICONS = {
    "Dashboard": "⌂",
    "Generate Quiz": "✦",
    "My Question Bank": "▤",
    "Take a Quiz": "▷",
    "Analytics": "◷",
    "Settings": "⚙",
    "About Project": "ⓘ",
}


def render_sidebar() -> str:
    if "_nav_request" in st.session_state:
        st.session_state["nav"] = st.session_state.pop("_nav_request")

    st.session_state.setdefault("nav", NAV_PAGES[0])

    with st.sidebar:
        st.markdown(
            """
            <div class="em-brand">
                <div class="em-brand-logo">E</div>
                <div class="em-brand-text">
                    <div class="em-brand-name">Edumind <span>Ai</span></div>
                    <div class="em-brand-caption">YOUR AI LEARNING SPACE</div>
                </div>
            </div>
            <div class="em-nav-heading">WORKSPACE</div>
            """,
            unsafe_allow_html=True,
        )

        page = st.radio(
            "Navigation",
            NAV_PAGES,
            key="nav",
            format_func=lambda p: f"{ICONS.get(p, '•')}   {p}",
            label_visibility="collapsed",
        )

        st.markdown(
            '<div class="em-sidebar-bottom">'
            '<div class="em-sidebar-divider"></div>'
            '<div class="em-status-heading">AI ENGINE STATUS</div>',
            unsafe_allow_html=True,
        )

        status = get_status()

        st.markdown(
            f"""
            <div class="em-engine-card">
                {status_pill(status)}
                <div class="em-engine-caption">
                    Powered by your local Ollama engine
                </div>
            </div>
            <div class="em-sidebar-footer">
                <span class="em-footer-dot"></span>
                Private · Runs on your device
            </div>
            """,
            unsafe_allow_html=True,
        )

    return page
