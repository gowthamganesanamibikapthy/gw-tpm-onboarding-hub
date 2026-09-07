# The newest 29-task CRUD manual
import json
import os
import pandas as pd
import streamlit as st
import uuid

# Use a distinct data file for Version 1 to prevent state conflicts
DATA_FILE = "tpm_v1_master_manual.json"

st.title("🚀 Version 1: Latest Master Task Matrix (29 Items + Mandatory Tags)")
st.caption("Includes full CRUD management, filtering by mandatory core items, and manager sync hub.")

# Master Dataset Definition (29 Tasks)
MASTER_TASKS = [
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Map key Pod Leads, Tech Leads, and Product Owners across PolicyCenter, ClaimCenter, and BillingCenter.",
        "focus": "Stakeholder Management",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Schedule 15-minute intro calls with primary cross-functional partners and engineering leads.",
        "focus": "Stakeholder Management",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Complete foundational training on Guidewire Cloud Platform (GWCP) multi-tenant architecture and SaaS operations.",
        "focus": "Platform & Tech",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Deep-dive into SurePath methodology phases (Inception, Sprint 0, Development, Stabilization, Deployment).",
        "focus": "Delivery Ops",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Review Integration Gateway, Cloud APIs, REST endpoints, and event webhook architecture.",
        "focus": "Platform & Tech",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Audit current backlog hygiene, sprint board conventions, and story estimation practices in Jira/Aha!.",
        "focus": "Delivery Ops",
        "priority": "Medium",
        "mandatory": "Recommended",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Attend and observe active team Agile ceremonies (Standups, Grooming, Sprint Planning, Retros).",
        "focus": "Agile Ops",
        "priority": "Medium",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Examine current CI/CD pipelines, lower environment promotion pathways, and cutover protocols.",
        "focus": "Release Mgmt",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Map out cross-functional dependencies between core Guidewire product pods and third-party integrations.",
        "focus": "Delivery Ops",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 1 (Days 1-30)",
        "task": "Shadow ongoing Cloud Assurance Assessments and release governance review gates.",
        "focus": "Governance",
        "priority": "Medium",
        "mandatory": "Recommended",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Take active ownership of the program risk log, issue tracking, and cross-team escalation paths.",
        "focus": "Risk Mgmt",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Drive weekly cross-pod dependency syncs to align feature delivery schedules.",
        "focus": "Delivery Ops",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Establish baseline dashboards for team velocity, cycle time, and release quality.",
        "focus": "Delivery Ops",
        "priority": "Medium",
        "mandatory": "Recommended",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Ensure teams execute SAST/DAST security scans, automated tests, and UAT sign-offs prior to release.",
        "focus": "Governance",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Coordinate delivery timelines with third-party vendors (e.g., payment gateways, fraud detection webhooks).",
        "focus": "Platform & Tech",
        "priority": "Medium",
        "mandatory": "Recommended",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Track and coordinate environment allocation across Dev, Integration, UAT, and Pre-Prod.",
        "focus": "Release Mgmt",
        "priority": "Medium",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Facilitate weekly program status reviews with Product Management and Engineering leadership.",
        "focus": "Stakeholder Management",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Lead your first release cutover or Program Increment (PI) planning cycle independently.",
        "focus": "Release Mgmt",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Clarify precise operational boundaries between TPMs, Product Owners, and Tech Leads.",
        "focus": "Governance",
        "priority": "High",
        "mandatory": "Recommended",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 2 (Days 31-60)",
        "task": "Standardize and document technical escalation procedures for critical production or release blockers.",
        "focus": "Governance",
        "priority": "Medium",
        "mandatory": "Recommended",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Conduct an end-to-end program retrospective on recent release cycles to extract key learnings.",
        "focus": "Delivery Ops",
        "priority": "Medium",
        "mandatory": "Recommended",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Identify 2-3 major workflow friction points in SurePath adoption and deploy streamlined solutions.",
        "focus": "Delivery Ops",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Standardize release management checklists and change governance templates across all pods.",
        "focus": "Release Mgmt",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Partner with Product and Engineering execs to finalize the upcoming quarter's roadmap priorities.",
        "focus": "Stakeholder Management",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Evaluate opportunities to integrate AI-assisted automation into claims triage or program reporting.",
        "focus": "Platform & Tech",
        "priority": "Low",
        "mandatory": "Optional / Stretch",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Conduct pre-audit Cloud Assurance readiness reviews for upcoming major product releases.",
        "focus": "Governance",
        "priority": "Medium",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Formalize a quarterly cross-team dependency matrix and automated risk heat map.",
        "focus": "Risk Mgmt",
        "priority": "Medium",
        "mandatory": "Recommended",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Prepare and deliver a comprehensive 90-day value delivery presentation to leadership.",
        "focus": "Stakeholder Management",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
    {
        "id": str(uuid.uuid4()),
        "phase": "Phase 3 (Days 61-90)",
        "task": "Review first-quarter achievements with your manager and establish long-term career impact goals.",
        "focus": "Strategic Alignment",
        "priority": "High",
        "mandatory": "Mandatory (Core)",
        "status": "Not Started",
        "tpm_notes": "",
        "manager_notes": "",
    },
]

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump(MASTER_TASKS, f, indent=4)
        return MASTER_TASKS
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return MASTER_TASKS

def save_data(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

if "v1_tasks" not in st.session_state:
    st.session_state.v1_tasks = load_data()

# Quick View / Filters
st.subheader("📋 Master Task Matrix")
for t in st.session_state.v1_tasks:
    badge = "🔴" if t["mandatory"] == "Mandatory (Core)" else "🟡"
    with st.expander(f"{badge} [{t['status']}] {t['task']} ({t['phase']})"):
        new_status = st.selectbox("Status", ["Not Started", "In Progress", "Completed", "Blocked"], index=["Not Started", "In Progress", "Completed", "Blocked"].index(t["status"]), key=f"v1_status_{t['id']}")
        if new_status != t["status"]:
            t["status"] = new_status
            save_data(st.session_state.v1_tasks)
            st.rerun()