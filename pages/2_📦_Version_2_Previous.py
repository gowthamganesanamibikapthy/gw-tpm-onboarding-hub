#The previous version of the 29-task CRUD manual
import streamlit as st

st.title("📦 Version 2: Previous Baseline Version")
st.caption("Accessing the simplified reference version of your onboarding tracker.")

st.warning("You are currently viewing the previous release version.")

# Simple baseline checklist layout
st.subheader("Phase 1: Discovery & Orientation (Baseline)")
st.checkbox("Map key Pod Leads and stakeholders", value=True)
st.checkbox("Review Guidewire Cloud platform basics", value=True)

st.subheader("Phase 2: Execution & Ownership (Baseline)")
st.checkbox("Own program risk logs", value=False)
st.checkbox("Drive dependency syncs", value=False)

st.subheader("Phase 3: Scale & Optimize (Baseline)")
st.checkbox("Conduct end-to-end retrospective", value=False)