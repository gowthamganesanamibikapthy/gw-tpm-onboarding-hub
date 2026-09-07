import json
import os
import uuid

import pandas as pd
import streamlit as st


ROOT_DIR = os.path.dirname(__file__)
TASKS_FILE = os.path.join(ROOT_DIR, "tpm_pdo_unified_tasks.json")
LEGACY_TASKS_FILE = os.path.join(ROOT_DIR, "tpm_v1_master_manual.json")
MANAGER_FILE = os.path.join(ROOT_DIR, "tpm_manager_workspace.json")
PHASES = ["Phase 1 (Days 1-30)", "Phase 2 (Days 31-60)", "Phase 3 (Days 61-90)"]
STATUSES = ["Not Started", "In Progress", "Completed", "Blocked"]
REQUIREMENTS = ["Mandatory (Core)", "Recommended", "Optional / Stretch"]
FOCUS_AREAS = [
    "IT / Admin",
    "Mandatory Training",
    "Stakeholder Management",
    "Platform & Tech",
    "Delivery Ops",
    "Release Mgmt",
    "Governance",
    "Risk Mgmt",
    "Process Optimization",
    "Proactive Value",
    "Agile Ops",
    "Strategic Alignment",
]

st.set_page_config(
    page_title="Guidewire PDO TPM Executive Portal",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    :root { --navy: #070f1b; --panel: rgba(14, 29, 49, .72); --panel-strong: rgba(11, 25, 44, .94); --line: rgba(125, 211, 252, .18); --blue: #0284c7; --sky: #38bdf8; --text: #e7f0fb; --muted: #8ea5bd; }
    html, body, [data-testid="stAppViewContainer"] { background: radial-gradient(circle at 10% 0%, rgba(2, 132, 199, .16), transparent 32rem), radial-gradient(circle at 92% 10%, rgba(56, 189, 248, .08), transparent 28rem), var(--navy); color: var(--text); }
    [data-testid="stHeader"] { background: rgba(7, 15, 27, .72); }
    [data-testid="stSidebar"] { background: rgba(5, 13, 25, .92); border-right: 1px solid rgba(125, 211, 252, .12); }
    .block-container { max-width: 1500px; padding-top: 2rem; padding-bottom: 4rem; }
    h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; letter-spacing: -.02em; color: var(--text); }
    p, label, [data-testid="stMarkdownContainer"] { font-family: 'DM Sans', sans-serif; }
    .hero { background: linear-gradient(120deg, rgba(9, 24, 43, .97), rgba(2, 83, 138, .88) 68%, rgba(14, 116, 144, .82)); border: 1px solid rgba(125, 211, 252, .28); box-shadow: 0 22px 70px rgba(0,0,0,.3), inset 0 1px 0 rgba(255,255,255,.12); color: white; padding: 2.2rem 2.4rem; border-radius: 16px; margin-bottom: 1.5rem; }
    .hero h1 { color: white; margin: 0; font-size: 2.5rem; }
    .hero p { color: #c9eaff; margin: .45rem 0 0; max-width: 850px; }
    [data-testid="stMetric"], [data-testid="stAlert"] { background: var(--panel); border: 1px solid var(--line); box-shadow: inset 0 1px 0 rgba(255,255,255,.06), 0 16px 40px rgba(0,0,0,.18); border-radius: 14px; }
    [data-testid="stMetric"] { transition: transform .2s ease, border-color .2s ease; }
    [data-testid="stMetric"]:hover { transform: translateY(-3px); border-color: rgba(56, 189, 248, .5); }
    [data-testid="stExpander"] { background: rgba(10, 25, 43, .66); border: 1px solid var(--line); border-radius: 14px; box-shadow: inset 0 1px 0 rgba(255,255,255,.05); }
    [data-testid="stExpander"]:hover { border-color: rgba(56, 189, 248, .42); }
    input, textarea, [data-baseweb="select"] > div { background: rgba(7, 15, 27, .72) !important; color: var(--text) !important; border-color: rgba(125, 211, 252, .2) !important; border-radius: 9px !important; }
    [data-baseweb="popover"] > div, [role="listbox"] { background: #0b192c !important; color: var(--text) !important; }
    .stButton > button, .stDownloadButton > button { background: linear-gradient(135deg, #0284c7, #0369a1); color: white; border: 1px solid rgba(125, 211, 252, .42); border-radius: 10px; font-weight: 700; transition: transform .2s ease, box-shadow .2s ease; }
    .stButton > button:hover, .stDownloadButton > button:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(2, 132, 199, .3); }
    .stProgress > div > div > div > div { background: linear-gradient(90deg, #0284c7, #38bdf8); }
    [data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }
    hr { border-color: rgba(125, 211, 252, .14); }
    .status-dot { color: #38bdf8; font-size: 1.15rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


def make_task(phase, task, focus, priority, requirement, notes="", source="PDO Foundations"):
    return {
        "id": str(uuid.uuid4()),
        "phase": phase,
        "task": task,
        "focus": focus,
        "priority": priority,
        "mandatory": requirement,
        "status": "Not Started",
        "tpm_notes": notes,
        "manager_notes": "",
        "source": source,
    }


SUPPLEMENTAL_TASKS = [
    make_task(PHASES[0], "Verify system and environment access across GWCP, Jira, Aha!, Confluence, and AWS.", "IT / Admin", "High", "Mandatory (Core)"),
    make_task(PHASES[0], "Enroll in Guidewire Certified Associate training through the Guidewire Education Portal.", "Mandatory Training", "High", "Mandatory (Core)", "Build working context for InsuranceSuite configuration and Gosu basics."),
    make_task(PHASES[0], "Audit current environments against Guidewire's N-3 release policy.", "Governance", "High", "Mandatory (Core)"),
    make_task(PHASES[0], "Deliver an early quick win by improving a process document or Jira board layout.", "Proactive Value", "Medium", "Recommended"),
    make_task(PHASES[1], "Begin preparation for Guidewire Certified Ace specialization, if required by the manager.", "Mandatory Training", "Medium", "Recommended", "Discuss the Integration or ClaimCenter track during a 1:1."),
    make_task(PHASES[1], "Drive dependency syncs across Cloud APIs, Event Webhooks, and Jutro digital frontends.", "Delivery Ops", "High", "Mandatory (Core)"),
    make_task(PHASES[2], "Deliver a 90-day value and metrics presentation to senior leadership.", "Stakeholder Management", "High", "Mandatory (Core)"),
]


def save_json(path, value):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(value, file, indent=4)


def load_tasks():
    source_path = TASKS_FILE if os.path.exists(TASKS_FILE) else LEGACY_TASKS_FILE
    try:
        with open(source_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except (OSError, json.JSONDecodeError):
        tasks = []
    existing_names = {task.get("task") for task in tasks}
    for task in tasks:
        task.setdefault("mandatory", "Recommended")
        task.setdefault("tpm_notes", "")
        task.setdefault("manager_notes", "")
        task.setdefault("source", "Master Matrix")
    for task in SUPPLEMENTAL_TASKS:
        if task["task"] not in existing_names:
            tasks.append(task)
    save_json(TASKS_FILE, tasks)
    return tasks


def load_manager_workspace():
    default = {"agenda": "", "talking_points": "", "manager_items": [], "next_check_in": ""}
    if not os.path.exists(MANAGER_FILE):
        return default
    try:
        with open(MANAGER_FILE, "r", encoding="utf-8") as file:
            value = json.load(file)
        default.update(value)
    except (OSError, json.JSONDecodeError):
        pass
    return default


if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()
if "manager_workspace" not in st.session_state:
    st.session_state.manager_workspace = load_manager_workspace()


def persist_tasks():
    save_json(TASKS_FILE, st.session_state.tasks)


def persist_manager():
    save_json(MANAGER_FILE, st.session_state.manager_workspace)


def delete_task(task_id):
    st.session_state.tasks = [task for task in st.session_state.tasks if task["id"] != task_id]
    persist_tasks()
    st.toast("Task removed", icon="🗑️")


# Sidebar navigation and focused filters.
st.sidebar.markdown("## PDO / TPM Hub")
view = st.sidebar.radio("Workspace", ["Executive Overview", "Unified Task List", "Manager 1:1 Hub"], label_visibility="collapsed")
st.sidebar.divider()
st.sidebar.caption("Unified task filters")
phase_filter = st.sidebar.multiselect("Phase", PHASES, default=PHASES)
requirement_filter = st.sidebar.multiselect("Requirement", REQUIREMENTS, default=REQUIREMENTS)
status_filter = st.sidebar.multiselect("Status", STATUSES, default=STATUSES)

all_tasks = st.session_state.tasks
tasks_df = pd.DataFrame(all_tasks)
completed = sum(task["status"] == "Completed" for task in all_tasks)
mandatory_tasks = [task for task in all_tasks if task["mandatory"] == "Mandatory (Core)"]
completion_rate = completed / len(all_tasks) if all_tasks else 0
mandatory_rate = sum(task["status"] == "Completed" for task in mandatory_tasks) / len(mandatory_tasks) if mandatory_tasks else 0

st.markdown(
    "<div class='hero'><h1>Guidewire PDO TPM Executive Portal</h1><p>One operating view for onboarding, delivery governance, manager alignment, and measurable value across the first 90 days.</p></div>",
    unsafe_allow_html=True,
)

if view == "Executive Overview":
    st.subheader("Executive command center")
    st.caption("A single source of truth for the TPM and manager. Every task displays its name, status, and requirement level.")
    metrics = st.columns(5)
    metrics[0].metric("Unified objectives", len(all_tasks))
    metrics[1].metric("Overall complete", f"{completion_rate:.0%}")
    metrics[2].metric("Core complete", f"{mandatory_rate:.0%}")
    metrics[3].metric("In progress", sum(task["status"] == "In Progress" for task in all_tasks))
    metrics[4].metric("Blocked", sum(task["status"] == "Blocked" for task in all_tasks))
    st.progress(completion_rate, text=f"90-day onboarding progress · {completion_rate:.0%}")
    st.divider()
    phase_columns = st.columns(3)
    for column, phase in zip(phase_columns, PHASES):
        phase_tasks = [task for task in all_tasks if task["phase"] == phase]
        phase_done = sum(task["status"] == "Completed" for task in phase_tasks)
        phase_rate = phase_done / len(phase_tasks) if phase_tasks else 0
        with column:
            st.markdown(f"### {phase.split(' ')[1]}")
            st.progress(phase_rate, text=f"{phase_done}/{len(phase_tasks)} complete")
            st.caption(f"{sum(task['mandatory'] == 'Mandatory (Core)' for task in phase_tasks)} core objectives · {sum(task['status'] == 'Blocked' for task in phase_tasks)} blocked")
    st.subheader("Unified operating view")
    if not tasks_df.empty:
        view_columns = ["phase", "task", "status", "mandatory", "focus", "priority"]
        st.dataframe(tasks_df[view_columns], width="stretch", hide_index=True)

elif view == "Unified Task List":
    st.subheader("Unified task list")
    st.caption("The complete PDO onboarding runway. Use the filters, then open any row to update its status, requirement, evidence, or manager guidance.")
    with st.expander("＋ Add a task or requirement", expanded=False):
        with st.form("add_unified_task"):
            fields = st.columns([1, 2, 1, 1])
            new_phase = fields[0].selectbox("Phase", PHASES)
            new_task = fields[1].text_input("Task name")
            new_focus = fields[2].selectbox("Focus area", FOCUS_AREAS)
            new_priority = fields[3].selectbox("Priority", ["High", "Medium", "Low"])
            new_requirement = st.selectbox("Requirement level", REQUIREMENTS)
            submitted = st.form_submit_button("Add task", type="primary")
            if submitted and new_task.strip():
                st.session_state.tasks.append(make_task(new_phase, new_task.strip(), new_focus, new_priority, new_requirement, source="Custom"))
                persist_tasks()
                st.success("Task added to the unified list")
                st.rerun()

    filtered_tasks = [
        task for task in all_tasks
        if task["phase"] in phase_filter and task["mandatory"] in requirement_filter and task["status"] in status_filter
    ]
    st.markdown(f"### {len(filtered_tasks)} objectives in view")
    for task in filtered_tasks:
        requirement_marker = "●" if task["mandatory"] == "Mandatory (Core)" else "○"
        with st.expander(f"{requirement_marker} {task['task']}  ·  {task['status']}  ·  {task['mandatory']}"):
            columns = st.columns([1.2, 1.3, 1.3, 1.2])
            new_status = columns[0].selectbox("Status", STATUSES, index=STATUSES.index(task["status"]), key=f"status_{task['id']}")
            new_requirement = columns[1].selectbox("Requirement level", REQUIREMENTS, index=REQUIREMENTS.index(task["mandatory"]), key=f"requirement_{task['id']}")
            columns[2].write(f"**Focus**\n\n{task['focus']}")
            columns[3].write(f"**Priority**\n\n{task['priority']}")
            notes = st.columns(2)
            tpm_notes = notes[0].text_area("TPM evidence / progress notes", task.get("tpm_notes", ""), key=f"tpm_{task['id']}")
            manager_notes = notes[1].text_area("Manager guidance", task.get("manager_notes", ""), key=f"manager_{task['id']}")
            actions = st.columns([8, 1])
            if actions[1].button("Delete", key=f"delete_{task['id']}"):
                delete_task(task["id"])
                st.rerun()
            if new_status != task["status"] or new_requirement != task["mandatory"] or tpm_notes != task.get("tpm_notes", "") or manager_notes != task.get("manager_notes", ""):
                task.update({"status": new_status, "mandatory": new_requirement, "tpm_notes": tpm_notes, "manager_notes": manager_notes})
                persist_tasks()

elif view == "Manager 1:1 Hub":
    workspace = st.session_state.manager_workspace
    st.subheader("Manager 1:1 hub")
    st.caption("Draft the conversation, organize strategic talking points, and track every manager action item in one place.")
    meeting_info = st.columns([1, 2, 1])
    with meeting_info[0]:
        st.text_input("Next check-in", value=workspace["next_check_in"], key="next_check_in")
    if st.session_state.next_check_in != workspace["next_check_in"]:
        workspace["next_check_in"] = st.session_state.next_check_in
        persist_manager()
    st.divider()
    agenda_col, strategy_col = st.columns(2)
    with agenda_col:
        agenda = st.text_area("Meeting agenda", value=workspace["agenda"], height=240, placeholder="Decisions needed, risks to review, progress to celebrate...", key="manager_agenda")
        if agenda != workspace["agenda"]:
            workspace["agenda"] = agenda
            persist_manager()
    with strategy_col:
        talking_points = st.text_area("Strategic talking points", value=workspace["talking_points"], height=240, placeholder="Product development operations themes, dependencies, coaching topics, and asks...", key="manager_talking_points")
        if talking_points != workspace["talking_points"]:
            workspace["talking_points"] = talking_points
            persist_manager()
    st.divider()
    st.subheader("Manager action items")
    with st.form("add_manager_action"):
        item_fields = st.columns([2.5, 1, 1, 1])
        item_text = item_fields[0].text_input("Action item")
        item_owner = item_fields[1].text_input("Owner")
        item_due = item_fields[2].text_input("Due date")
        item_status = item_fields[3].selectbox("Status", STATUSES)
        add_item = st.form_submit_button("Add action item", type="primary")
        if add_item and item_text.strip():
            workspace["manager_items"].append({"id": str(uuid.uuid4()), "item": item_text.strip(), "owner": item_owner.strip(), "due": item_due.strip(), "status": item_status})
            persist_manager()
            st.rerun()
    if not workspace["manager_items"]:
        st.info("No manager action items yet. Add the next commitment above.")
    for item in workspace["manager_items"]:
        with st.expander(f"{item['item']}  ·  {item['status']}"):
            item_columns = st.columns([2.5, 1, 1, 1])
            updated_status = item_columns[0].selectbox("Action", STATUSES, index=STATUSES.index(item["status"]), key=f"item_status_{item['id']}")
            updated_owner = item_columns[1].text_input("Owner", value=item["owner"], key=f"item_owner_{item['id']}")
            updated_due = item_columns[2].text_input("Due date", value=item["due"], key=f"item_due_{item['id']}")
            if item_columns[3].button("Delete", key=f"item_delete_{item['id']}"):
                workspace["manager_items"] = [entry for entry in workspace["manager_items"] if entry["id"] != item["id"]]
                persist_manager()
                st.rerun()
            if updated_status != item["status"] or updated_owner != item["owner"] or updated_due != item["due"]:
                item.update({"status": updated_status, "owner": updated_owner, "due": updated_due})
                persist_manager()
    st.divider()
    export_columns = ["phase", "task", "status", "mandatory", "focus", "priority", "tpm_notes", "manager_notes"]
    export_col, action_col = st.columns([1, 3])
    with export_col:
        st.download_button("Export task list", tasks_df[export_columns].to_csv(index=False).encode("utf-8"), "Guidewire_PDO_TPM_Unified_Tasks.csv", "text/csv", type="primary")
    with action_col:
        st.caption("Task progress and manager workspace are saved locally in JSON and remain available across sessions.")
