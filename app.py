#Main Hub / Version Selector
import streamlit as st

st.set_page_config(
    page_title="Guidewire TPM Multi-Version Hub",
    page_icon="🔀",
    layout="wide",
)

st.title("🔀 Guidewire TPM Application Hub")
st.markdown("""
Welcome to the multi-version hub. You are running **two concurrent versions** of the application on the same platform:
- **Version 1 (Latest):** Full master task dashboard, complete 29-task list with mandatory requirement tags, CRUD management, and JSON storage.
- **Version 2 (Previous):** Your earlier core baseline version.

Use the navigation pane on the **left sidebar** to switch seamlessly between versions!
""")

st.info("👈 Select a version from the sidebar menu to launch it.")