import json
import os
import uuid

import pandas as pd
import streamlit as st


DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tpm_v2_onboarding_manual.json")
PHASES = ["Phase 1 (Days 1-30)", "Phase 2 (Days 31-60)", "Phase 3 (Days 61-90)"]
STATUSES = ["Not Started", "In Progress", "Completed", "Blocked"]
FOCUS_AREAS = ["IT / Admin", "Mandatory Training", "Stakeholder Management", "Delivery Ops", "Governance", "Proactive Value", "Risk Mgmt", "Process Optimization"]

st.set_page_config(page_title="PDO TPM Onboarding Hub | Foundations", page_icon="📦", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>
.block-container { max-width: 1500px; padding-top: 2rem; padding-bottom: 4rem; }
[data-testid="stMetric"] { background: linear-gradient(135deg, #fffaf2, #f8f0e5); border: 1px solid #eadbc5; padding: 1rem; border-radius: 12px; }
.hero { background: linear-gradient(120deg, #5a3a2e 0%, #9a6043 58%, #d58c62 100%); color: white; padding: 2rem 2.2rem; border-radius: 18px; margin-bottom: 1.5rem; }
.hero h1 { color: white; margin: 0; font-size: 2.4rem; }
.hero p { color: #fff0df; margin: .45rem 0 0; }
.stProgress > div > div > div > div { background-color: #d36f4c; }
</style>
""", unsafe_allow_html=True)


def make_task(phase, task, focus, priority, tpm_notes=""):
	return {"id": str(uuid.uuid4()), "phase": phase, "task": task, "focus": focus, "priority": priority, "status": "Not Started", "tpm_notes": tpm_notes, "manager_notes": ""}


DEFAULT_TASKS = [
	make_task(PHASES[0], "Verify system and environment access (GWCP, Jira, Aha!, Confluence, AWS).", "IT / Admin", "High"),
	make_task(PHASES[0], "Log into Guidewire Education Portal and enroll in Guidewire Certified Associate training.", "Mandatory Training", "High", "Required to understand InsuranceSuite configuration and Gosu basics."),
	make_task(PHASES[0], "Map key Pod Leads, Tech Leads, and Product Owners across PolicyCenter, ClaimCenter, and BillingCenter.", "Stakeholder Management", "High"),
	make_task(PHASES[0], "Deep-dive into SurePath methodology (Inception, Sprint 0, Development, Stabilization, Deployment).", "Delivery Ops", "High"),
	make_task(PHASES[0], "Audit current environments to ensure compliance with Guidewire's N-3 release policy.", "Governance", "High", "Are we within 3 releases of the current version to maintain support?"),
	make_task(PHASES[0], "Deliver an Early Quick Win, such as fixing a process document or streamlining a Jira board layout.", "Proactive Value", "Medium"),
	make_task(PHASES[1], "Take active ownership of the program risk log and cross-team escalation paths.", "Risk Mgmt", "High"),
	make_task(PHASES[1], "Drive weekly cross-pod dependency syncs for Cloud APIs, Event Webhooks, and Jutro digital frontends.", "Delivery Ops", "High"),
	make_task(PHASES[1], "Ensure teams execute SAST/DAST security scans and UAT sign-offs prior to release.", "Governance", "High"),
	make_task(PHASES[1], "Begin preparation for Guidewire Certified Ace specialization, if required by manager.", "Mandatory Training", "Medium", "Discuss specialized track, such as Integration or ClaimCenter, during 1:1."),
	make_task(PHASES[2], "Conduct pre-audit Cloud Assurance readiness reviews for upcoming major product releases.", "Governance", "High"),
	make_task(PHASES[2], "Identify 2-3 major workflow friction points in SurePath adoption and deploy streamlined solutions.", "Process Optimization", "High"),
	make_task(PHASES[2], "Deliver a comprehensive 90-day value and metrics presentation to senior leadership.", "Stakeholder Management", "High"),
]


def save_data(tasks):
	with open(DATA_FILE, "w", encoding="utf-8") as file:
		json.dump(tasks, file, indent=4)


def load_data():
	if not os.path.exists(DATA_FILE):
		save_data(DEFAULT_TASKS)
		return DEFAULT_TASKS
	try:
		with open(DATA_FILE, "r", encoding="utf-8") as file:
			return json.load(file)
	except (OSError, json.JSONDecodeError):
		return DEFAULT_TASKS


if "v2_tasks" not in st.session_state:
	st.session_state.v2_tasks = load_data()


def delete_task(task_id):
	st.session_state.v2_tasks = [task for task in st.session_state.v2_tasks if task["id"] != task_id]
	save_data(st.session_state.v2_tasks)
	st.toast("Task removed", icon="🗑️")


st.sidebar.markdown("## PDO / TPM Hub")
view = st.sidebar.radio("Workspace", ["Overview", "Onboarding Task List", "Manager Sync Hub"], label_visibility="collapsed")
st.sidebar.divider()
st.sidebar.caption("View controls")
phase_filter = st.sidebar.multiselect("Phase", PHASES, default=PHASES)
status_filter = st.sidebar.multiselect("Status", STATUSES, default=STATUSES)

tasks = st.session_state.v2_tasks
df = pd.DataFrame(tasks)
completed = sum(task["status"] == "Completed" for task in tasks)
completion_rate = completed / len(tasks) if tasks else 0
st.markdown("<div class='hero'><h1>PDO TPM Foundations</h1><p>A practical onboarding runway for access, certifications, operating context, delivery ownership, and early value.</p></div>", unsafe_allow_html=True)

if view == "Overview":
	st.subheader("Foundations command center")
	st.caption("Use this version as the focused 30-60-90 onboarding runway for the PDO team.")
	metric_cols = st.columns(5)
	metric_cols[0].metric("Total tasks", len(tasks))
	metric_cols[1].metric("Complete", f"{completion_rate:.0%}")
	metric_cols[2].metric("In progress", sum(task["status"] == "In Progress" for task in tasks))
	metric_cols[3].metric("Blocked", sum(task["status"] == "Blocked" for task in tasks))
	metric_cols[4].metric("High priority", sum(task["priority"] == "High" for task in tasks))
	st.progress(completion_rate, text=f"Onboarding progress · {completion_rate:.0%}")
	st.divider()
	phase_cols = st.columns(3)
	for column, phase in zip(phase_cols, PHASES):
		phase_tasks = [task for task in tasks if task["phase"] == phase]
		phase_done = sum(task["status"] == "Completed" for task in phase_tasks)
		phase_rate = phase_done / len(phase_tasks) if phase_tasks else 0
		with column:
			st.markdown(f"### {phase.split(' ')[1]}")
			st.progress(phase_rate, text=f"{phase_done}/{len(phase_tasks)} complete")
			st.caption(f"{sum(task['priority'] == 'High' for task in phase_tasks)} high priority · {len(phase_tasks)} total")
	st.subheader("Onboarding map")
	if not df.empty:
		st.dataframe(df[["phase", "task", "focus", "priority", "status"]], use_container_width=True, hide_index=True)

elif view == "Onboarding Task List":
	st.subheader("Onboarding task list")
	st.caption("Add new work, update progress, capture evidence, or remove tasks that do not apply.")
	with st.expander("＋ Add a new task or certification", expanded=False):
		with st.form("v2_add_task"):
			form_cols = st.columns([1, 2, 1, 1])
			new_phase = form_cols[0].selectbox("Phase", PHASES)
			new_task = form_cols[1].text_input("Task or milestone")
			new_focus = form_cols[2].selectbox("Focus", FOCUS_AREAS)
			new_priority = form_cols[3].selectbox("Priority", ["High", "Medium", "Low"])
			submitted = st.form_submit_button("Add task", type="primary")
			if submitted and new_task.strip():
				st.session_state.v2_tasks.append(make_task(new_phase, new_task.strip(), new_focus, new_priority))
				save_data(st.session_state.v2_tasks)
				st.success("Task added")
				st.rerun()
	filtered = [task for task in tasks if task["phase"] in phase_filter and task["status"] in status_filter]
	st.markdown(f"### {len(filtered)} tasks in view")
	for task in filtered:
		with st.expander(f"{task['task']}  ·  {task['status']}"):
			columns = st.columns([1.2, 1.2, 1.2, 1.2])
			new_status = columns[0].selectbox("Status", STATUSES, index=STATUSES.index(task["status"]), key=f"v2_status_{task['id']}")
			columns[1].write(f"**Focus**\n\n{task['focus']}")
			columns[2].write(f"**Priority**\n\n{task['priority']}")
			columns[3].write(f"**Phase**\n\n{task['phase']}")
			note_cols = st.columns(2)
			tpm_notes = note_cols[0].text_area("TPM evidence / progress notes", task.get("tpm_notes", ""), key=f"v2_tpm_{task['id']}")
			manager_notes = note_cols[1].text_area("Manager guidance", task.get("manager_notes", ""), key=f"v2_mgr_{task['id']}")
			action_cols = st.columns([8, 1])
			if action_cols[1].button("Delete", key=f"v2_delete_{task['id']}"):
				delete_task(task["id"])
				st.rerun()
			if new_status != task["status"] or tpm_notes != task.get("tpm_notes", "") or manager_notes != task.get("manager_notes", ""):
				task.update({"status": new_status, "tpm_notes": tpm_notes, "manager_notes": manager_notes})
				save_data(tasks)

elif view == "Manager Sync Hub":
	st.subheader("Manager sync hub")
	st.caption("Turn onboarding observations into focused conversations and next actions.")
	agenda, directives = st.columns(2)
	with agenda:
		st.text_area("Next 1:1 agenda", height=220, placeholder="Access blockers, certification progress, team context, and quick wins...")
	with directives:
		st.text_area("Manager directives and follow-ups", height=220, placeholder="Capture expectations, coaching, and next commitments...")
	st.divider()
	st.subheader("Export onboarding manual")
	export_columns = ["phase", "task", "focus", "priority", "status", "tpm_notes", "manager_notes"]
	st.download_button("Download onboarding manual as CSV", df[export_columns].to_csv(index=False).encode("utf-8"), "Guidewire_PDO_TPM_Onboarding_Manual.csv", "text/csv", type="primary")