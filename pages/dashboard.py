
"""Edumind Ai dashboard: real SQLite statistics and local AI status."""
from __future__ import annotations

from datetime import datetime

import streamlit as st

from components.context import get_repo, get_settings, get_status, navigate
from components.metrics import fmt_percent, metric_row, status_pill
from components.styles import esc


def _when(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts).astimezone().strftime("%d %b, %H:%M")
    except (ValueError, TypeError):
        return str(ts)


def _continue_cards(repo) -> None:
    """Preserve unfinished quizzes and unsaved drafts."""
    session = repo.load_active_session()
    quiz = repo.get_quiz(session["quiz_id"]) if session else None

    if quiz is not None:
        question_ids = {q.id for q in quiz.questions}
        done = sum(
            1 for answer_id in session.get("answers", {})
            if answer_id in question_ids
        )

        with st.container(border=True):
            left, right = st.columns([4, 1])
            left.markdown("**Continue where you left off**")
            left.caption(
                f"{esc(quiz.title)} · {done} of {len(quiz.questions)} questions answered"
            )

            if right.button(
                "Resume quiz",
                key="dash_resume",
                type="primary",
                use_container_width=True,
            ):
                st.session_state["resume_quiz"] = True
                navigate("Take a Quiz")

    draft = repo.load_draft()

    if draft:
        draft_quiz = draft.get("quiz") or {}
        title = esc(draft_quiz.get("title", "Untitled"))
        count = len(draft_quiz.get("questions", []))

        with st.container(border=True):
            left, right = st.columns([4, 1])
            left.markdown("**Your saved draft is waiting**")
            left.caption(f"{title} · {count} question(s) ready for review")

            if right.button(
                "Open draft",
                key="dash_draft",
                use_container_width=True,
            ):
                navigate("Generate Quiz")


def _onboarding(repo, status, stats) -> None:
    if (
        stats["quizzes"]
        or stats["attempts"]
        or repo.load_setting("onboarding_done")
    ):
        return

    with st.container(border=True):
        st.markdown("### Let's get you started")
        st.caption("Complete these three steps to begin creating AI-powered quizzes.")

        steps = [
            (
                status.connected,
                "Connect Ollama",
                "Open Ollama or run ollama serve.",
            ),
            (
                status.model_installed,
                "Install an AI model",
                "Check the Settings page for the installation command.",
            ),
            (
                False,
                "Create your first quiz",
                "Paste your notes or upload a study document.",
            ),
        ]

        for index, (done, title, hint) in enumerate(steps, 1):
            mark = "&#10003;" if done else str(index)
            css_class = "done" if done else "todo"

            st.markdown(
                f'<div class="qf-step {css_class}" '
                f'style="margin:.35rem 0;border-radius:12px">'
                f'<span>{mark}</span>'
                f'<b>{esc(title)}</b>&nbsp;'
                f'<span style="background:none;width:auto" '
                f'class="qf-muted">· {esc(hint)}</span></div>',
                unsafe_allow_html=True,
            )

        col1, col2, _ = st.columns([1.3, 1.3, 3])

        if col1.button("Open Settings", key="onb_settings"):
            navigate("Settings")

        if col2.button("Hide guide", key="onb_hide"):
            repo.set_setting("onboarding_done", True)
            st.rerun()


def _welcome_section() -> None:
    st.markdown(
        """
        <div class="em-dashboard-hero">
            <div class="em-hero-topline">
                <span class="em-hero-label">YOUR PERSONAL LEARNING SPACE</span>
                <span class="em-hero-indicator">
                    <span></span> AI POWERED
                </span>
            </div>
            <h1>Learn smarter.<br>Grow faster.</h1>
            <p>
                Turn your study material into interactive quizzes,
                practise at your own pace and understand your progress
                with Edumind Ai.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 3])

    if col1.button(
        "✦  Generate a quiz",
        key="dashboard_generate",
        type="primary",
        use_container_width=True,
    ):
        navigate("Generate Quiz")

    col2.caption("Create a quiz from your notes, PDF, DOCX or TXT documents.")


def _recent_activity(repo) -> None:
    st.markdown("### Recent activity")
    st.caption("A quick look at what you've been working on.")

    items = repo.recent_activity(8)

    if not items:
        st.markdown(
            """
            <div class="em-empty-state">
                <div class="em-empty-icon">◷</div>
                <b>No activity yet</b>
                <p>Your recent quizzes and learning activity will appear here.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    rows = ""

    for activity in items:
        message = esc(activity.get("message", "Activity"))
        timestamp = esc(_when(activity.get("ts", "")))

        rows += (
            '<div class="em-activity-row">'
            '<div class="em-activity-dot"></div>'
            f'<div class="em-activity-message">{message}</div>'
            f'<div class="em-activity-time">{timestamp}</div>'
            '</div>'
        )

    st.markdown(
        f'<div class="em-activity-card">{rows}</div>',
        unsafe_allow_html=True,
    )


def _ai_panel(status, settings) -> None:
    st.markdown(
        """
        <div class="em-ai-card">
            <div class="em-ai-icon">✦</div>
            <div class="em-ai-label">MEET YOUR AI STUDY ASSISTANT</div>
            <h3>Your learning, powered by AI.</h3>
            <p>
                Generate multiple-choice questions from your own study
                material using a local AI model. Your documents stay
                on your computer.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    with st.container(border=True):
        st.markdown("**Your AI engine**")
        st.markdown(status_pill(status), unsafe_allow_html=True)

        st.caption(f"Model endpoint: {esc(settings.base_url)}")

        if status.connected and status.model_installed:
            st.success("Your AI engine is ready.")
        elif not status.connected:
            st.warning(status.error or "Ollama is not running.")
        else:
            st.warning(status.error or "The selected model is not installed.")

        if st.button("Manage AI settings", key="dash_ai_settings",
                     use_container_width=True):
            navigate("Settings")


def render() -> None:
    repo = get_repo()
    settings = get_settings()
    status = get_status()
    stats = repo.dashboard_stats()

    _welcome_section()

    _continue_cards(repo)
    _onboarding(repo, status, stats)

    st.markdown("### Your learning overview")
    st.caption("Your actual progress, calculated from your saved quiz data.")

    metric_row(
        [
            (
                "Questions generated",
                str(stats["questions_generated"]),
                f'{stats["questions_in_bank"]} currently saved',
            ),
            (
                "Quizzes taken",
                str(stats["attempts"]),
                f'{stats["quizzes"]} quiz sets saved',
            ),
            (
                "Average score",
                fmt_percent(stats["avg_percent"]),
                "Across all attempts" if stats["attempts"] else "No attempts yet",
            ),
            (
                "Best score",
                fmt_percent(stats["best_percent"]),
                "Personal best" if stats["attempts"] else "No attempts yet",
            ),
        ]
    )

    st.write("")

    left, right = st.columns([3, 2], gap="large")

    with left:
        _recent_activity(repo)

    with right:
        _ai_panel(status, settings)
