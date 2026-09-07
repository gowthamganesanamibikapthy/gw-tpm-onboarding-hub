#Main Hub / Version Selector
import streamlit as st

st.set_page_config(
    page_title="Guidewire PDO TPM Onboarding Hub",
    page_icon="🔀",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    :root { --navy: #070f1b; --panel: rgba(14, 29, 49, .72); --line: rgba(125, 211, 252, .18); --blue: #0284c7; --sky: #38bdf8; --text: #e7f0fb; --muted: #8ea5bd; }
    html, body, [data-testid="stAppViewContainer"] { background: radial-gradient(circle at 12% 0%, rgba(2, 132, 199, .16), transparent 32rem), radial-gradient(circle at 90% 12%, rgba(56, 189, 248, .08), transparent 28rem), var(--navy); color: var(--text); }
    [data-testid="stHeader"] { background: rgba(7, 15, 27, .72); }
    .block-container { max-width: 1250px; padding-top: 4rem; padding-bottom: 4rem; }
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; letter-spacing: -.02em; color: var(--text); }
    p, label, [data-testid="stMarkdownContainer"] { font-family: 'DM Sans', sans-serif; }
    .hero { background: linear-gradient(120deg, rgba(9, 24, 43, .96), rgba(2, 83, 138, .85) 68%, rgba(14, 116, 144, .82)); border: 1px solid rgba(125, 211, 252, .28); box-shadow: 0 22px 70px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.12); color: white; padding: 3rem; border-radius: 18px; }
    .hero h1 { color: white; font-size: 3rem; margin: 0; }
    .hero p { color: #c9eaff; font-size: 1.15rem; max-width: 760px; }
    [data-testid="stMetric"], [data-testid="stAlert"] { background: var(--panel); border: 1px solid var(--line); box-shadow: inset 0 1px 0 rgba(255,255,255,.06), 0 16px 40px rgba(0,0,0,.18); border-radius: 14px; }
    [data-testid="stMetric"] { transition: transform .2s ease, border-color .2s ease; }
    [data-testid="stMetric"]:hover { transform: translateY(-3px); border-color: rgba(56, 189, 248, .5); }
    [data-testid="stSidebar"] { background: rgba(5, 13, 25, .9); border-right: 1px solid rgba(125, 211, 252, .12); }
    .stButton > button { background: linear-gradient(135deg, #0284c7, #0369a1); color: white; border: 1px solid rgba(125, 211, 252, .42); border-radius: 10px; font-weight: 700; transition: transform .2s ease, box-shadow .2s ease; }
    .stButton > button:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(2, 132, 199, .3); }
    </style>
    <div class="hero">
        <h1>Guidewire PDO TPM Onboarding</h1>
        <p>A practical portal for building context, tracking delivery ownership, capturing manager guidance, and showing value across the first 90 days.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Choose your working view")
st.caption("Both versions support progress tracking, custom tasks, notes, filters, deletion, and CSV export.")
left, right = st.columns(2)
with left:
    st.markdown("### 🚀 Version 1 · Master matrix")
    st.write("29 detailed PDO objectives with mandatory, recommended, and stretch requirements across delivery, governance, risk, and leadership.")
with right:
    st.markdown("### 📦 Version 2 · Foundations runway")
    st.write("14 focused onboarding tasks covering access, certifications, SurePath, quick wins, release readiness, and early leadership impact.")
st.info("Use the page navigation in the sidebar to open a workspace.")