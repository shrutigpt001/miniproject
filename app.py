
"""
Edumind Ai - AI-Powered MCQ Learning Platform
Powered by local Ollama models.
Run with: streamlit run app.py
"""
from __future__ import annotations

import streamlit as st

st.set_page_config(
    page_title="Edumind Ai | Smart Learning Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

from components.sidebar import render_sidebar
from components.styles import inject_css
from pages import (
    about,
    analytics,
    dashboard,
    generate_quiz,
    question_bank,
    settings,
    take_quiz
)

PAGES = {
    "Dashboard": dashboard.render,
    "Generate Quiz": generate_quiz.render,
    "My Question Bank": question_bank.render,
    "Take a Quiz": take_quiz.render,
    "Analytics": analytics.render,
    "Settings": settings.render,
    "About Project": about.render,
}


def main() -> None:
    inject_css()

    page = render_sidebar()

    try:
        page_function = PAGES.get(page, dashboard.render)
        page_function()

    except Exception as exc:
        st.error("Something went wrong while loading this page.")
        with st.expander("Technical details"):
            st.exception(exc)


if __name__ == "__main__":
    main()
