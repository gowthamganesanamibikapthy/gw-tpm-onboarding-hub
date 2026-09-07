# The newest 29-task CRUD manual
import json
import os
import pandas as pd
import streamlit as st
import uuid

# Use a distinct data file for Version 1 to prevent state conflicts
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tpm_v1_master_manual.json")

st.set_page_config(
    page_title="PDO TPM Onboarding Hub | Master",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    :root { --teal: #0d6b72; --coral: #e87561; }
    .block-container { max-width: 1500px; padding-top: 2rem; padding-bottom: 4rem; }
    [data-testid="stMetric"] { background: linear-gradient(135deg, #f7fbfa, #edf5f2); border: 1px solid #d8e7e1; padding: 1rem; border-radius: 12px; }
    .hero { background: linear-gradient(120deg, #12212b 0%, #0d6b72 60%, #3a8b7e 100%); color: white; padding: 2rem 2.2rem; border-radius: 18px; margin-bottom: 1.5rem; }
    .hero h1 { color: white; margin: 0; font-size: 2.4rem; }
    .hero p { color: #d9f2eb; margin: .45rem 0 0; }
    .stProgress > div > div > div > div { background-color: var(--coral); }
    </style>
    """,
    unsafe_allow_html=True,
)

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

STATUSES = ["Not Started", "In Progress", "Completed", "Blocked"]
PHASES = ["Phase 1 (Days 1-30)", "Phase 2 (Days 31-60)", "Phase 3 (Days 61-90)"]
FOCUS_AREAS = ["Platform & Tech", "Stakeholder Management", "Delivery Ops", "Release Mgmt", "Governance", "Risk Mgmt", "Agile Ops", "Strategic Alignment"]
REQUIREMENTS = ["Mandatory (Core)", "Recommended", "Optional / Stretch"]

def delete_task(task_id):
    st.session_state.v1_tasks = [task for task in st.session_state.v1_tasks if task["id"] != task_id]
    save_data(st.session_state.v1_tasks)
    st.toast("Task removed", icon="🗑️")

st.sidebar.markdown("## PDO / TPM Hub")
view = st.sidebar.radio("Workspace", ["Overview", "Master Task Matrix", "Manager Sync Hub"], label_visibility="collapsed")
st.sidebar.divider()
st.sidebar.caption("View controls")
phase_filter = st.sidebar.multiselect("Phase", PHASES, default=PHASES)
requirement_filter = st.sidebar.multiselect("Requirement", REQUIREMENTS, default=REQUIREMENTS)
status_filter = st.sidebar.multiselect("Status", STATUSES, default=STATUSES)

tasks = st.session_state.v1_tasks
df = pd.DataFrame(tasks)
completed = sum(task["status"] == "Completed" for task in tasks)
mandatory = [task for task in tasks if task["mandatory"] == "Mandatory (Core)"]
mandatory_done = sum(task["status"] == "Completed" for task in mandatory)
completion_rate = completed / len(tasks) if tasks else 0

st.markdown("<div class='hero'><h1>Guidewire PDO TPM Onboarding</h1><p>Master operating rhythm for product development operations, delivery governance, and technical program leadership.</p></div>", unsafe_allow_html=True)

if view == "Overview":
    st.subheader("Your 30-60-90 day command center")
    st.caption("A shared working view for the TPM and manager. Progress is saved to the local workspace.")
    metric_cols = st.columns(5)
    metric_cols[0].metric("Total objectives", len(tasks))
    metric_cols[1].metric("Overall complete", f"{completion_rate:.0%}")
    metric_cols[2].metric("Core complete", f"{mandatory_done}/{len(mandatory)}")
    metric_cols[3].metric("In progress", sum(task["status"] == "In Progress" for task in tasks))
    metric_cols[4].metric("Blocked", sum(task["status"] == "Blocked" for task in tasks))
    st.progress(completion_rate, text=f"Overall onboarding progress · {completion_rate:.0%}")
    st.divider()
    phase_cols = st.columns(3)
    for column, phase in zip(phase_cols, PHASES):
        phase_tasks = [task for task in tasks if task["phase"] == phase]
        phase_done = sum(task["status"] == "Completed" for task in phase_tasks)
        phase_rate = phase_done / len(phase_tasks) if phase_tasks else 0
        with column:
            st.markdown(f"### {phase.split(' ')[1]}")
            st.progress(phase_rate, text=f"{phase_done}/{len(phase_tasks)} complete")
            st.caption(f"{sum(task['status'] == 'Blocked' for task in phase_tasks)} blocked · {sum(task['mandatory'] == 'Mandatory (Core)' for task in phase_tasks)} core objectives")
    st.subheader("Priority lens")
    if not df.empty:
        st.dataframe(df[["phase", "task", "focus", "priority", "mandatory", "status"]], use_container_width=True, hide_index=True)

elif view == "Master Task Matrix":
    st.subheader("Master task matrix")
    st.caption("Filter, update, add, or remove any objective. Every edit is persisted immediately.")
    with st.expander("＋ Add a new objective", expanded=False):
        with st.form("v1_add_task"):
            form_cols = st.columns([1, 2, 1, 1])
            new_phase = form_cols[0].selectbox("Phase", PHASES)
            new_task = form_cols[1].text_input("Objective")
            new_focus = form_cols[2].selectbox("Focus", FOCUS_AREAS)
            new_priority = form_cols[3].selectbox("Priority", ["High", "Medium", "Low"])
            new_requirement = st.selectbox("Requirement", REQUIREMENTS)
            submitted = st.form_submit_button("Add objective", type="primary")
            if submitted and new_task.strip():
                st.session_state.v1_tasks.append({"id": str(uuid.uuid4()), "phase": new_phase, "task": new_task.strip(), "focus": new_focus, "priority": new_priority, "mandatory": new_requirement, "status": "Not Started", "tpm_notes": "", "manager_notes": ""})
                save_data(st.session_state.v1_tasks)
                st.success("Objective added")
                st.rerun()

    filtered = [task for task in tasks if task["phase"] in phase_filter and task["mandatory"] in requirement_filter and task["status"] in status_filter]
    st.markdown(f"### {len(filtered)} objectives in view")
    for task in filtered:
        marker = "●" if task["mandatory"] == "Mandatory (Core)" else "○"
        with st.expander(f"{marker} {task['task']}  ·  {task['status']}"):
            columns = st.columns([1.2, 1.2, 1.2, 1.2])
            new_status = columns[0].selectbox("Status", STATUSES, index=STATUSES.index(task["status"]), key=f"v1_status_{task['id']}")
            new_requirement = columns[1].selectbox("Requirement", REQUIREMENTS, index=REQUIREMENTS.index(task["mandatory"]), key=f"v1_req_{task['id']}")
            columns[2].write(f"**Focus**\n\n{task['focus']}")
            columns[3].write(f"**Priority**\n\n{task['priority']}")
            note_cols = st.columns(2)
            tpm_notes = note_cols[0].text_area("TPM evidence / progress notes", task.get("tpm_notes", ""), key=f"v1_tpm_{task['id']}")
            manager_notes = note_cols[1].text_area("Manager guidance", task.get("manager_notes", ""), key=f"v1_mgr_{task['id']}")
            action_cols = st.columns([8, 1])
            if action_cols[1].button("Delete", key=f"v1_delete_{task['id']}"):
                delete_task(task["id"])
                st.rerun()
            if new_status != task["status"] or new_requirement != task["mandatory"] or tpm_notes != task.get("tpm_notes", "") or manager_notes != task.get("manager_notes", ""):
                task.update({"status": new_status, "mandatory": new_requirement, "tpm_notes": tpm_notes, "manager_notes": manager_notes})
                save_data(tasks)

elif view == "Manager Sync Hub":
    st.subheader("Manager sync hub")
    st.caption("Prepare the conversation, capture decisions, and keep the next action visible.")
    agenda, directives = st.columns(2)
    with agenda:
        st.text_area("Next 1:1 agenda", height=220, placeholder="Risks, dependencies, decisions, and support needed...")
    with directives:
        st.text_area("Manager directives and follow-ups", height=220, placeholder="Capture expectations, coaching, and next commitments...")
    st.divider()
    st.subheader("Export working manual")
    export_columns = ["phase", "task", "focus", "mandatory", "priority", "status", "tpm_notes", "manager_notes"]
    st.download_button("Download master manual as CSV", df[export_columns].to_csv(index=False).encode("utf-8"), "Guidewire_PDO_TPM_Master_Manual.csv", "text/csv", type="primary")