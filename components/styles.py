
"""Edumind Ai - Global application styling."""
from __future__ import annotations

import html
import re

import streamlit as st


CSS = """
<style>
:root {
    color-scheme: dark;
    --qf-bg: #0b1020;
    --qf-surface: #121a30;
    --qf-surface-2: #18223d;
    --qf-border: #26324f;
    --qf-text: #e6e9f2;
    --qf-muted: #9aa6c4;
    --qf-accent: #818cf8;
    --qf-accent-2: #6366f1;
    --qf-ok: #34d399;
    --qf-warn: #fbbf24;
    --qf-bad: #f87171;
    --qf-radius: 16px;
}

html, body,
[data-testid="stAppViewContainer"],
.stApp {
    font-family: Inter, "Segoe UI", system-ui, -apple-system,
    Roboto, "Helvetica Neue", Arial, sans-serif;
    color: var(--qf-text);
}

.stApp {
    background:
        radial-gradient(1000px 500px at 90% -10%,
        rgba(99,102,241,.12), transparent 60%),
        var(--qf-bg);
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: transparent;
}

.block-container {
    max-width: 1350px;
    padding-top: 2rem;
    padding-bottom: 3.5rem;
}

h1, h2, h3, h4, h5, h6 {
    color: var(--qf-text) !important;
    letter-spacing: -.025em;
}

p, li, label, span, small {
    color: inherit;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #0d1529;
    border-right: 1px solid #26324f;
}

[data-testid="stSidebar"] > div:first-child {
    background: #0d1529;
}

[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #e6e9f2;
}

.em-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: .3rem 0 2rem;
    padding: 0 .3rem;
}

.em-brand-logo {
    width: 43px;
    height: 43px;
    border-radius: 13px;
    display: grid;
    place-items: center;
    background: linear-gradient(135deg, #6366f1, #818cf8);
    color: white;
    font-size: 23px;
    font-weight: 800;
    box-shadow: 0 5px 18px rgba(99,102,241,.25);
}

.em-brand-name {
    font-size: 19px;
    font-weight: 750;
    color: #ffffff;
    letter-spacing: -.5px;
}

.em-brand-name span {
    color: #a5b4fc;
}

.em-brand-caption,
.em-nav-heading,
.em-status-heading {
    color: #8493b2;
    font-size: 10px;
    font-weight: 750;
    letter-spacing: 1.5px;
}

.em-brand-caption {
    margin-top: 3px;
}

.em-nav-heading,
.em-status-heading {
    padding: 0 .6rem;
    margin-bottom: .7rem;
}

[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 7px;
}

[data-testid="stSidebar"] [role="radiogroup"] label {
    width: 100%;
    padding: .65rem .8rem;
    border: 1px solid transparent;
    border-radius: 11px;
    cursor: pointer;
    transition: all .2s ease;
}

[data-testid="stSidebar"] [role="radiogroup"] label p {
    color: #b8c4dc;
    font-size: 13px;
    font-weight: 550;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: #1c2947;
}

[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: #263b65;
    border-color: #405f9c;
}

[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {
    color: #ffffff;
    font-weight: 700;
}

[data-testid="stSidebar"] [data-testid="stRadioOption"] > div > div:first-child {
    display: none;
}

.em-sidebar-bottom {
    margin-top: 2.5rem;
}

.em-sidebar-divider {
    height: 1px;
    background: #293653;
    margin: 1rem 0 1.3rem;
}

.em-engine-card {
    background: #1a2845;
    border: 1px solid #2d4168;
    border-radius: 12px;
    padding: 12px;
}

.em-engine-caption {
    color: #9aaac6;
    font-size: 11px;
    margin-top: 9px;
}

.em-sidebar-footer {
    color: #8292af;
    font-size: 10px;
    margin: 1.2rem .2rem;
    display: flex;
    align-items: center;
    gap: 7px;
}

.em-footer-dot {
    width: 7px;
    height: 7px;
    background: #34d399;
    border-radius: 50%;
    display: inline-block;
}

/* CARDS */

.qf-card,
.qf-metric,
.em-activity-card {
    background: var(--qf-surface);
    border: 1px solid var(--qf-border);
    border-radius: var(--qf-radius);
    padding: 1.1rem 1.25rem;
    margin-bottom: .9rem;
    box-shadow: 0 3px 15px rgba(0,0,0,.16);
}

.qf-card h4 {
    margin: 0 0 .35rem;
    font-size: 1rem;
}

.qf-muted {
    color: var(--qf-muted) !important;
    font-size: .88rem;
}

.qf-hero,
.em-dashboard-hero {
    background:
        radial-gradient(circle at 90% 15%,
        rgba(129,140,248,.16), transparent 35%),
        linear-gradient(120deg, #182440, #151d35 65%, #121a30);
    border: 1px solid #344466;
    border-radius: 18px;
    padding: 1.6rem 1.7rem;
    margin-bottom: 1.2rem;
}

.qf-hero h1,
.em-dashboard-hero h1 {
    color: #f1f5ff !important;
    margin: 0 0 .5rem;
}

.qf-hero p,
.em-dashboard-hero p {
    color: #aab7d2 !important;
    margin: 0;
    max-width: 60ch;
    line-height: 1.8;
}

.qf-metric {
    padding: 1rem 1.15rem;
    height: 100%;
}

.qf-metric .l {
    color: var(--qf-muted);
    font-size: .78rem;
    text-transform: uppercase;
    letter-spacing: .07em;
}

.qf-metric .v {
    font-size: 1.95rem;
    font-weight: 750;
    margin-top: .2rem;
    color: #f1f5ff;
    line-height: 1.15;
}

.qf-metric .s {
    color: var(--qf-muted);
    font-size: .8rem;
    margin-top: .15rem;
}

/* BADGES */

.qf-badge {
    display: inline-block;
    padding: .12rem .6rem;
    border-radius: 999px;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .03em;
    border: 1px solid;
}

.qf-easy {
    color: #6ee7b7;
    border-color: rgba(52,211,153,.5);
    background: rgba(52,211,153,.10);
}

.qf-medium {
    color: #fcd34d;
    border-color: rgba(251,191,36,.5);
    background: rgba(251,191,36,.10);
}

.qf-hard {
    color: #fca5a5;
    border-color: rgba(248,113,113,.5);
    background: rgba(248,113,113,.10);
}

.qf-topic {
    color: #c4b5fd;
    border-color: rgba(129,140,248,.45);
    background: rgba(129,140,248,.10);
}

.qf-pill {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    padding: .3rem .8rem;
    border-radius: 999px;
    font-weight: 650;
    font-size: .82rem;
    border: 1px solid;
}

.qf-pill i {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
}

.qf-pill.on {
    color: #6ee7b7;
    border-color: rgba(52,211,153,.5);
    background: rgba(52,211,153,.09);
}

.qf-pill.on i {
    background: #34d399;
    box-shadow: 0 0 8px #34d399;
}

.qf-pill.off {
    color: #fca5a5;
    border-color: rgba(248,113,113,.5);
    background: rgba(248,113,113,.09);
}

.qf-pill.off i {
    background: #f87171;
}

.qf-pill.warn {
    color: #fcd34d;
    border-color: rgba(251,191,36,.5);
    background: rgba(251,191,36,.09);
}

.qf-pill.warn i {
    background: #fbbf24;
}

/* QUESTION CARDS */

.qf-qhead {
    display: flex;
    gap: .5rem;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: .55rem;
}

.qf-qnum {
    font-weight: 800;
    color: var(--qf-accent);
}

.qf-qtext {
    font-size: 1.08rem;
    font-weight: 600;
    line-height: 1.5;
    margin: .1rem 0 .7rem;
    color: var(--qf-text);
}

.qf-opt {
    display: flex;
    gap: .7rem;
    padding: .55rem .8rem;
    border: 1px solid var(--qf-border);
    border-radius: 10px;
    margin: .3rem 0;
    background: var(--qf-surface-2);
    color: var(--qf-text);
}

.qf-opt b {
    min-width: 1.4rem;
    color: var(--qf-accent);
}

.qf-opt.correct {
    border-color: rgba(52,211,153,.7);
    background: rgba(52,211,153,.10);
}

.qf-opt.correct b {
    color: #34d399;
}

.qf-opt.wrong {
    border-color: rgba(248,113,113,.7);
    background: rgba(248,113,113,.10);
}

.qf-opt.wrong b {
    color: #f87171;
}

.qf-expl {
    border-left: 3px solid var(--qf-accent-2);
    padding: .35rem .8rem;
    margin: .7rem 0 .2rem;
    color: #c7d2fe;
    background: rgba(99,102,241,.10);
    border-radius: 0 8px 8px 0;
    font-size: .93rem;
}

.qf-src {
    border-left: 3px solid #64748b;
    padding: .3rem .8rem;
    margin-top: .5rem;
    color: var(--qf-muted);
    font-size: .85rem;
    font-style: italic;
}

.qf-activity {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    padding: .55rem 0;
    border-bottom: 1px solid var(--qf-border);
    font-size: .92rem;
}

/* BUTTONS AND INPUTS */

.stButton > button,
.stDownloadButton > button {
    border-radius: 11px;
    font-weight: 650;
    border: 1px solid var(--qf-border);
    background: #18223d;
    color: #e6e9f2;
    transition: transform .12s, border-color .15s, box-shadow .15s;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border-color: var(--qf-accent);
    color: #ffffff;
    transform: translateY(-1px);
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1, #818cf8);
    border: none;
    color: #fff;
    box-shadow: 0 6px 18px rgba(99,102,241,.25);
}

.stButton > button:disabled,
.stButton > button[kind="primary"]:disabled {
    opacity: .45;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
    background: var(--qf-surface-2);
    color: var(--qf-muted);
    border: 1px solid var(--qf-border);
}

.stButton > button:focus-visible,
.stDownloadButton > button:focus-visible,
input:focus-visible,
textarea:focus-visible {
    outline: 2px solid var(--qf-accent) !important;
    outline-offset: 2px;
}

[data-baseweb="input"] > div,
[data-baseweb="textarea"] > div,
[data-baseweb="select"] > div {
    background: #121a30 !important;
    border-color: #34415f !important;
    border-radius: 10px !important;
}

[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
[data-baseweb="select"] input {
    color: #e6e9f2 !important;
    -webkit-text-fill-color: #e6e9f2 !important;
}

[data-baseweb="select"] span {
    color: #e6e9f2 !important;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: var(--qf-radius);
    border-color: var(--qf-border);
    background: var(--qf-surface);
}

[data-testid="stTabs"] button {
    font-weight: 650;
    color: var(--qf-muted);
}

[data-testid="stTabs"] button[aria-selected="true"] {
    color: #a5b4fc;
}

/* QUIZ OPTION BUTTONS */

[class*="st-key-qopts"] .stButton > button {
    justify-content: flex-start;
    text-align: left;
    padding: .75rem 1rem;
    border-radius: 12px;
    background: var(--qf-surface-2);
    color: var(--qf-text);
    font-weight: 550;
    min-height: 3rem;
}

[class*="st-key-qopts"] .stButton > button:hover {
    border-color: var(--qf-accent);
    background: rgba(129,140,248,.12);
    transform: translateX(3px);
}

[class*="st-key-qopts"] .stButton > button[kind="primary"] {
    background: rgba(129,140,248,.16);
    border: 1px solid var(--qf-accent);
    box-shadow: none;
}

[class*="st-key-qopts"] .stButton > button > div,
[class*="st-key-qopts"] .stButton > button [data-testid="stMarkdownContainer"] {
    width: 100%;
    justify-content: flex-start;
    text-align: left;
}

[class*="st-key-qopts"] .stButton > button p {
    text-align: left;
    width: 100%;
}

/* ANIMATIONS */

@keyframes qf-pop {
    0% { transform: scale(.96); opacity: .4; }
    55% { transform: scale(1.035); }
    100% { transform: scale(1); opacity: 1; }
}

@keyframes qf-glow {
    0% { box-shadow: 0 0 0 0 rgba(52,211,153,.65); }
    100% { box-shadow: 0 0 0 16px rgba(52,211,153,0); }
}

@keyframes qf-shake {
    0%, 100% { transform: translateX(0); }
    20% { transform: translateX(-7px); }
    40% { transform: translateX(7px); }
    60% { transform: translateX(-5px); }
    80% { transform: translateX(4px); }
}

@keyframes qf-slide {
    from { transform: translateY(10px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

@keyframes qf-icon {
    0% { transform: scale(0) rotate(-45deg); }
    70% { transform: scale(1.35) rotate(8deg); }
    100% { transform: scale(1) rotate(0); }
}

.qf-anim .qf-opt.correct {
    animation: qf-pop .5s ease-out, qf-glow 1.1s ease-out .1s;
}

.qf-anim .qf-opt.wrong {
    animation: qf-shake .5s ease-in-out;
}

.qf-anim .qf-expl {
    animation: qf-slide .5s ease-out .35s both;
}

.qf-verdict {
    display: flex;
    align-items: center;
    gap: .7rem;
    padding: .75rem 1rem;
    border-radius: 12px;
    margin: .8rem 0 .2rem;
    font-weight: 650;
    animation: qf-slide .4s ease-out .15s both;
}

.qf-verdict .qf-ico {
    width: 1.9rem;
    height: 1.9rem;
    border-radius: 50%;
    display: grid;
    place-items: center;
    font-size: 1.05rem;
    color: #ffffff;
    animation: qf-icon .55s cubic-bezier(.2,.9,.3,1.3) .2s both;
}

.qf-verdict.ok {
    background: rgba(52,211,153,.12);
    border: 1px solid rgba(52,211,153,.55);
    color: #6ee7b7;
}

.qf-verdict.ok .qf-ico {
    background: #059669;
}

.qf-verdict.bad {
    background: rgba(248,113,113,.12);
    border: 1px solid rgba(248,113,113,.55);
    color: #fca5a5;
}

.qf-verdict.bad .qf-ico {
    background: #dc2626;
}

/* GENERATION STEPS */

.qf-steps {
    display: flex;
    gap: .5rem;
    margin: .2rem 0 1rem;
    flex-wrap: wrap;
}

.qf-step {
    display: flex;
    align-items: center;
    gap: .5rem;
    padding: .35rem .8rem .35rem .4rem;
    border-radius: 999px;
    font-size: .85rem;
    font-weight: 650;
    border: 1px solid var(--qf-border);
    color: var(--qf-muted);
    background: var(--qf-surface);
}

.qf-step span {
    width: 1.35rem;
    height: 1.35rem;
    border-radius: 50%;
    display: grid;
    place-items: center;
    font-size: .72rem;
    background: var(--qf-surface-2);
}

.qf-step.active {
    color: var(--qf-text);
    border-color: var(--qf-accent);
}

.qf-step.active span {
    background: var(--qf-accent-2);
    color: #fff;
}

.qf-step.done {
    color: #6ee7b7;
    border-color: rgba(52,211,153,.4);
}

.qf-step.done span {
    background: rgba(52,211,153,.15);
    color: #6ee7b7;
}

.qf-live {
    animation: qf-slide .45s ease-out both;
}

/* DASHBOARD */

.em-dashboard-hero {
    position: relative;
    overflow: hidden;
    padding: 2.2rem;
    margin-bottom: 1.2rem;
    border-radius: 20px;
}

.em-hero-topline {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
}

.em-hero-label {
    color: #a5b4fc;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.em-hero-indicator {
    color: #c7d2fe;
    font-size: 10px;
    font-weight: 750;
    letter-spacing: 1px;
    background: rgba(30,41,72,.8);
    padding: 7px 11px;
    border-radius: 30px;
}

.em-hero-indicator span {
    display: inline-block;
    width: 7px;
    height: 7px;
    margin-right: 5px;
    border-radius: 50%;
    background: #34d399;
}

.em-dashboard-hero h1 {
    font-size: clamp(2rem, 4vw, 2.8rem);
    line-height: 1.12;
    letter-spacing: -1.5px;
    margin: 1.4rem 0 .8rem;
}

.em-dashboard-hero p {
    max-width: 570px;
    font-size: .95rem;
}

.em-activity-card {
    padding: .5rem 1rem;
}

.em-activity-row {
    display: flex;
    align-items: center;
    gap: 11px;
    padding: .9rem .1rem;
    border-bottom: 1px solid var(--qf-border);
}

.em-activity-row:last-child {
    border-bottom: none;
}

.em-activity-dot {
    flex-shrink: 0;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #818cf8;
    box-shadow: 0 0 0 4px rgba(129,140,248,.15);
}

.em-activity-message {
    flex: 1;
    min-width: 0;
    color: #d1d9eb;
    font-size: .85rem;
    overflow-wrap: anywhere;
}

.em-activity-time {
    flex-shrink: 0;
    color: #9aa6c4;
    font-size: .72rem;
}

.em-empty-state {
    text-align: center;
    background: var(--qf-surface);
    border: 1px dashed var(--qf-border);
    border-radius: 15px;
    padding: 2rem 1rem;
}

.em-empty-icon {
    font-size: 1.8rem;
    color: #a5b4fc;
    margin-bottom: .5rem;
}

.em-empty-state b {
    display: block;
    color: var(--qf-text);
}

.em-empty-state p {
    color: var(--qf-muted);
    font-size: .83rem;
    margin: .4rem 0 0;
}

/* AI ASSISTANT */

.em-ai-card {
    padding: 1.35rem;
    border-radius: 16px;
    border: 1px solid #344466;
    background: linear-gradient(145deg, #182440, #121a30);
}

.em-ai-icon {
    display: grid;
    place-items: center;
    width: 38px;
    height: 38px;
    border-radius: 12px;
    background: #29365e;
    color: #a5b4fc;
    font-size: 21px;
    margin-bottom: 1rem;
}

.em-ai-label {
    color: #a5b4fc;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1.1px;
}

.em-ai-card h3 {
    color: #e6e9f2 !important;
    font-size: 1.25rem;
    margin: .6rem 0;
}

.em-ai-card p {
    color: #aab7d2;
    font-size: .84rem;
    line-height: 1.7;
    margin: 0;
}

/* GENERAL STREAMLIT DARK CONTROLS */

[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label,
[data-testid="stSelectbox"] label,
[data-testid="stMultiSelect"] label,
[data-testid="stNumberInput"] label,
[data-testid="stSlider"] label,
[data-testid="stCheckbox"] label,
[data-testid="stRadio"] label,
[data-testid="stToggle"] label,
[data-testid="stDateInput"] label,
[data-testid="stFileUploader"] label {
    color: #dce4f5 !important;
}

[data-testid="stCaptionContainer"],
.stCaption {
    color: var(--qf-muted) !important;
}

[data-testid="stAlert"] {
    border-radius: 12px;
}

[data-testid="stExpander"] {
    background: var(--qf-surface);
    border: 1px solid var(--qf-border);
    border-radius: 12px;
}

[data-testid="stExpander"] summary {
    color: var(--qf-text);
}

hr {
    border-color: var(--qf-border);
}

/* RESPONSIVE */

@media (max-width: 900px) {
    .block-container {
        padding: 1.2rem 1rem 3rem;
    }

    .qf-hero h1 {
        font-size: 1.5rem;
    }

    .qf-metric .v {
        font-size: 1.55rem;
    }
}

@media (max-width: 700px) {
    .em-dashboard-hero {
        padding: 1.4rem;
    }

    .em-activity-row {
        flex-wrap: wrap;
    }

    .em-activity-time {
        margin-left: 19px;
    }
}

/* HIDE STREAMLIT TOP TOOLBAR */

[data-testid="stToolbar"],
[data-testid="stHeader"],
#MainMenu,
.stDeployButton,
[data-testid="stDecoration"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation: none !important;
        transition: none !important;
    }
}
</style>
"""


def is_light() -> bool:
    """Always use the original dark application theme."""
    return False


def inject_css() -> None:
    """Inject the application-wide dark CSS."""
    st.markdown(CSS, unsafe_allow_html=True)


def esc(text: object) -> str:
    """HTML-escape untrusted text before rendering custom HTML."""
    return html.escape(str(text), quote=True)


_MD_SPECIAL = re.compile(r"([\\`*_{}\[\]()#+\-.!|<>~$:&])")


def md_escape(text: str) -> str:
    """Escape Markdown syntax in untrusted labels."""
    return _MD_SPECIAL.sub(r"\\\1", str(text))


def badge(difficulty: str) -> str:
    """Generate a difficulty badge."""
    cls = {
        "Easy": "qf-easy",
        "Medium": "qf-medium",
        "Hard": "qf-hard",
    }.get(difficulty, "qf-medium")

    return (
        f'<span class="qf-badge {cls}">'
        f'{esc(difficulty)}'
        f'</span>'
    )
