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
    .block-container { max-width: 1250px; padding-top: 4rem; }
    .hero { background: linear-gradient(120deg, #12212b, #0d6b72 65%, #3a8b7e); color: white; padding: 3rem; border-radius: 22px; }
    .hero h1 { color: white; font-size: 3rem; margin: 0; }
    .hero p { color: #d9f2eb; font-size: 1.15rem; max-width: 760px; }
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