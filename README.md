# Guidewire PDO TPM Onboarding Hub

A Streamlit executive portal for onboarding Technical Program Managers into Guidewire Product Development Operations (PDO).

The application combines 30-60-90 day onboarding objectives, delivery operations, governance, stakeholder alignment, manager 1:1 preparation, follow-up commitments, and post-call communications reporting in one workspace.

## Features

- Executive onboarding dashboard with overall, phase, and core-objective progress
- Unified task list covering the complete PDO TPM onboarding runway
- Collapsed task rows with expandable editable details
- Editable task name, description, status, requirement level, focus area, priority, TPM evidence, and manager guidance
- Search and filters for phase, status, and requirement level
- Add and remove custom onboarding tasks
- Manager 1:1 workspace with:
  - Meeting agenda
  - Strategic talking points
  - Follow-up commitments
  - Owners, due dates, and statuses
  - Post-call discussion reports
  - Decisions, risks, support needs, and next communications
  - Downloadable TXT and CSV communications extracts
- Dark Guidewire-inspired glassmorphism interface with midnight navy and cobalt accents

## Run Locally

Requirements:

- Python 3.10+
- Streamlit
- pandas

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Start the application:

```powershell
python -m streamlit run app.py
```

Open the local URL shown by Streamlit, normally:

```text
http://localhost:8501
```

## Streamlit Community Cloud

Deploy from the GitHub repository using:

- Repository: `gowthamganesanamibikapthy/gw-tpm-onboarding-hub`
- Branch: `main`
- Main file: `app.py`
- Dependencies: `requirements.txt`

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
├── tpm_pdo_unified_tasks.json
└── tpm_v1_master_manual.json
```

The application uses `app.py` as the single entrypoint. Task progress and manager workspace content are stored in local JSON files. For production use with multiple users, replace local JSON persistence with a shared database or managed storage service.

## Data Notes

- `tpm_pdo_unified_tasks.json` contains the unified onboarding task snapshot.
- `tpm_v1_master_manual.json` is retained as the original master data source.
- `tpm_manager_workspace.json` is created locally when manager notes, follow-ups, or call reports are saved.
- Streamlit Community Cloud storage is not a durable shared database, so persistent multi-user production data should use external storage.

## Repository Description

Guidewire PDO Technical Program Manager onboarding portal with 30-60-90 day task tracking, editable onboarding objectives, manager 1:1 planning, follow-up commitments, post-call reports, and executive progress dashboards.
