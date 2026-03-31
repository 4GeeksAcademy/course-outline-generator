# HealthCore — Transversal Project Company

## AI Engineering · 4Geeks Academy

---

## General Overview

**HealthCore** is an outpatient healthcare services company founded in 2011 in Austin, Texas. It operates a network of **12 outpatient clinics** — 9 in the United States (Texas, Florida, and Georgia) and 3 in the United Kingdom (London and Manchester) — offering primary care, specialist consultations, chronic disease management, and preventive health programmes. The company employs approximately **200 people** across clinical staff, operations, administration, and a growing technology unit. Annual revenue sits around **28 million dollars**.

HealthCore's competitive edge has always been accessibility: same-day appointments, extended hours, and bilingual staff in US markets. But operating across two countries with different healthcare regulatory frameworks — HIPAA in the US, UK GDPR and NHS standards in the UK — and managing patient data, clinical workflows, and insurance processes across 12 locations without a unified platform is beginning to show its limits. No-show rates are rising, billing errors are costly, and clinical teams spend hours on administrative tasks they shouldn't have to do.

The CEO, **Dr. Sandra Okonkwo**, a physician turned operator, founded HealthCore after years of frustration with the administrative burden inside large hospital systems. She is deeply clinical in her thinking and diametrically opposed to technology for its own sake — but she knows that without proper systems, the company cannot scale. She has created an internal unit called **HealthCore Digital** to build the infrastructure that the clinical and operational teams need. You are part of that team.

---

## Department Map and Their Real Problems

### 🏥 Clinical Operations

**Manager:** Dr. Marcus Reid, Director of Clinical Operations (Austin)
**Team:** ~120 clinical staff (physicians, nurse practitioners, nurses, medical assistants) across 12 locations

**Current situation:**

- Each clinic operates semi-independently. Patient intake, appointment scheduling, and clinical documentation follow different local processes depending on when each location was opened and who set it up.
- There is no unified electronic health record (EHR) across US and UK locations. The US clinics use a legacy EHR from 2014; the UK clinics use a different system, and neither integrates with the other.
- Clinical staff spend an average of 35 minutes per day on documentation outside of patient-facing time: post-visit notes, referral letters, and lab result summaries.
- Referral management is entirely manual: a medical assistant faxes referral letters and follows up by phone. Average referral completion time: 11 days.
- Chronic disease patients (diabetes, hypertension, asthma) have no structured follow-up programme between visits. Readmissions that could be prevented are not tracked.

**Automation and AI needs:**

- Unified patient API: a single endpoint for patient demographics, visit history, diagnoses, prescriptions, and lab results — accessible to both US and UK staff.
- Clinical documentation assistant: listens to the patient-physician conversation (with consent) and generates a structured draft SOAP note for the physician to review and sign.
- Automated referral workflow: referral created in system → routed to specialist → status tracked → patient notified — no fax, no phone follow-up.
- Chronic care follow-up programme: automated check-ins (SMS or email) for patients with chronic conditions between visits; flags concerning responses to the care team.
- Clinical KPI dashboard: patients seen per day, average wait time, documentation backlog, referral completion rate — by clinic and country.

---

### 📋 Patient Experience and Access

**Manager:** Priya Nair, Head of Patient Experience (London)
**Team:** 8 patient coordinators + front desk staff across 12 locations

**Current situation:**

- Appointment booking is fragmented: US patients book via phone or a US-only portal; UK patients call the front desk. There is no shared online booking system across markets.
- No-show rates average 22% across the network, costing an estimated $800K annually in lost capacity.
- Patient satisfaction surveys are paper-based, collected at checkout, and never aggregated or analysed.
- When a patient is referred internally from one HealthCore clinic to another (e.g., from primary care to a specialist clinic), the receiving clinic has no prior visibility into the patient's history until the day of the appointment.
- Patients with limited English proficiency (primarily Spanish and Portuguese speakers in Florida) frequently disengage from follow-up because communications arrive only in English.

**Automation and AI needs:**

- Unified appointment booking platform: online booking across all 12 locations, available in English and Spanish, with real-time availability and automatic confirmation.
- No-show prevention system: automated reminder sequence (48h, 24h, 2h) via SMS and email, with a one-tap rescheduling link. Smart risk scoring to identify high no-show-probability appointments for proactive outreach.
- Patient satisfaction pipeline: post-visit survey sent automatically after each appointment; responses aggregated into a weekly NPS dashboard by location and service type.
- Internal referral handoff: when a patient is referred between HealthCore clinics, the receiving provider sees a pre-built summary of relevant history before the appointment.
- Multilingual patient communication: all automated patient messages generated in the patient's preferred language (English, Spanish).

---

### 💰 Revenue Cycle and Billing

**Manager:** Tom Callahan, Revenue Cycle Director (Austin)
**Team:** 6 people (billing specialists, coders, AR analysts)

**Current situation:**

- US billing operates under insurance reimbursement (commercial insurance + Medicare/Medicaid). UK billing is a mix of private pay and a small NHS contract. The two revenue streams are managed by entirely separate teams with no shared reporting.
- The billing denial rate is 14% — well above the industry benchmark of 5–8%. Most denials are due to coding errors and missing prior authorisations, both of which are preventable.
- The billing team manually reviews every claim before submission. With around 600 visits per week, this creates a bottleneck: average time from visit to claim submission is 5 days.
- There is no system that flags patients with lapsed insurance coverage before their appointment. The front desk often discovers the issue at check-in.
- Monthly revenue reports for each country are compiled manually by Tom and take 2 full working days to produce.

**Automation and AI needs:**

- Claim pre-validation engine: before each visit, the system checks insurance eligibility, flags missing prior authorisations, and identifies likely coding issues based on the scheduled service.
- Automated claims submission pipeline: structured visit data → ICD/CPT code suggestion → coder review → submission — reducing manual review to exception handling only.
- Denial management tracker: denied claims automatically routed to the right specialist with reason code, expected resubmission deadline, and appeal template.
- Revenue dashboard: collections by location, denial rate by payer and service type, AR aging, US vs. UK revenue split — updated daily.
- Finance reporting agent: "what is our net collection rate for Medicare patients in Texas this quarter?" answered from the data, not from a spreadsheet.

> **Regulatory note:** US claims involve Protected Health Information (PHI) under HIPAA — any pipeline touching claim data requires a signed Business Associate Agreement (BAA) with all vendors and a full access audit trail. UK billing data falls under UK GDPR; a Data Processing Agreement (DPA) is required with any third-party processor.

---

### 🧬 Compliance and Data Governance

**Manager:** Claire Whitfield, Chief Compliance Officer (London)
**Team:** 3 people

**Current situation:**

- HealthCore handles patient data under HIPAA in the US and UK GDPR in the UK. The rules differ in key ways: HIPAA breach notification allows 60 days; UK GDPR requires notification to the ICO within 72 hours. Data retention periods, patient access rights, and vendor agreement requirements are all different.
- There is no automated audit trail for who accessed which patient records. If a potential breach occurs, reconstruction is manual and takes days.
- Staff data privacy training is annual, delivered by a PowerPoint, and completion is tracked in a spreadsheet.
- Policies and procedures are stored in a shared drive that has not been audited in 18 months. Some documents reference regulations that have since been updated.
- Vendor due diligence — confirming that technology partners have signed BAAs (US) and DPAs (UK) — is tracked manually in a spreadsheet that Claire owns alone.

**Automation and AI needs:**

- Access audit log system: every patient data access event (who, what record, when, from which location) captured and queryable, with automatic anomaly detection for unusual access patterns.
- Compliance training platform: role-based annual training modules with quiz completion tracking and automatic certificate generation.
- Policy management system: searchable policy library with version control, review due-date alerts, and change notifications to relevant staff.
- Vendor compliance tracker: BAA/DPA status per vendor, renewal dates, risk level — automatic alert when an agreement approaches expiry.
- Compliance assistant: answers staff questions about what is and isn't permissible under HIPAA and UK GDPR in plain language, with references to the relevant policy.

---

### 🧑‍💼 People and Workforce

**Manager:** Diane Foster, VP of People (Austin)
**Team:** 4 people

**Current situation:**

- Managing 200 employees across 12 locations in two countries with different employment law frameworks adds constant administrative overhead and legal complexity.
- Recruitment is high-volume and urgent: clinical roles are hard to fill, average time-to-hire for a nurse practitioner is 47 days, and vacancy rates in US locations average 11%.
- Onboarding is inconsistent across locations. New clinical staff often start without completing mandatory compliance training, which creates regulatory risk.
- There is no system tracking continuing medical education (CME) hours for physicians and nurse practitioners, who are required to log them to maintain licensure.
- Turnover in front desk and administrative roles is 38% annually. Exit interview data exists in email threads and is never aggregated.

**Automation and AI needs:**

- Recruitment pipeline tracker: open roles, candidate status, interview stages, time-to-hire by role and location — with alerts when a vacancy exceeds 30 days unfilled.
- Automated onboarding checklist: for each new hire role type (physician, nurse, admin), a structured task sequence with document collection, system access provisioning, and mandatory training completion tracking.
- CME and licensure tracker: each clinician's licence status, expiry date, CME hours logged vs. required — automatic reminder 90 and 30 days before deadlines.
- People KPI dashboard: headcount, vacancy rate, turnover, time-to-hire, absenteeism — by location and country.
- Exit interview analysis: structured digital exit interviews with automated theme extraction and monthly summary to Diane and the CEO.

---

### 💻 Technology

**Manager:** James Osei, CTO (Austin)
**Team:** 6 people (2 engineers, 1 data engineer, 1 DevOps, 1 QA, James)

**Current situation:**

- HealthCore's tech estate is a patchwork: a US EHR (legacy, no public API), a UK EHR (different vendor, REST API with limited documentation), a US billing platform, a UK billing spreadsheet, a phone-based scheduling system in the US, and a manual diary in the UK.
- There is no centralised data layer. Each system holds its own data and exports CSVs on request.
- Patient data handling across integrations is inconsistently documented. Some connectors were built by contractors no longer engaged, and there is no clear map of what data flows where — a compliance liability Claire escalates regularly.
- Deploying a new internal tool takes 3–4 weeks due to manual compliance review gates that could be partially automated.
- James wants to build a unified HealthCore platform serving both markets, but 70% of the team's time goes to maintaining legacy systems.

**Automation and AI needs:**

- Unified data platform: a HIPAA and UK GDPR-compliant data layer that ingests events from all clinical and operational systems, normalises them, and exposes them via a single internal API.
- Patient data lineage map: automated tracking of where patient data enters, moves through, and exits the system — queryable by Claire's compliance team at any time.
- CI/CD pipeline with compliance gates: automated security and compliance checks baked into deployment, reducing release time without increasing regulatory risk.
- System health dashboard: uptime, API latency, integration errors — across all connected systems, both countries.
- Internal technical documentation agent: answers engineering questions about the platform architecture, data schemas, and integration specs from the codebase and documentation.

---

### 📊 Executive Direction and Reporting

**Manager:** Dr. Sandra Okonkwo, CEO (Austin)
**Leadership team:** CTO, Director of Clinical Operations, Head of Patient Experience, Revenue Cycle Director, Chief Compliance Officer, VP of People

**Current situation:**

- Sandra manages a 12-location clinical network across two countries without a unified operational view. She receives weekly reports assembled by each department head, formatted differently, and often contradictory because they pull from different source systems.
- She cannot answer in real time: "what is our network-wide no-show rate this week?" or "which UK clinic is underperforming on patient satisfaction?"
- Board presentations require a week of data consolidation across the team.
- Strategic decisions — such as whether to open a 13th location or which service line to expand in the UK — are made with incomplete, delayed data.

**Automation and AI needs:**

- Executive operations dashboard: network-wide KPIs in a single view — patients seen, revenue collected, no-show rate, satisfaction score, denial rate, vacancy rate — updated daily and segmented by country and location.
- Automated board reporting pack: the agent consolidates data from all departments, drafts the monthly board report, and delivers a review-ready document to Sandra's inbox by the first working day of each month.
- Strategic alerts: if a location's no-show rate exceeds 25%, or if the billing denial rate rises above 10% in any location, immediate notification to Sandra and the relevant department head.
- AI executive assistant: Sandra can ask in natural language "which three US locations have the worst chronic care follow-up compliance this quarter?" and get a data-backed answer with recommended actions.

---

## Milestone Map

| Milestone        | Primary Department                     | Business Deliverable                                                                    |
| ---------------- | -------------------------------------- | --------------------------------------------------------------------------------------- |
| 0 — Prework      | All                                    | Environment setup, first prompts and research about HealthCore                          |
| 1 — Web          | Patient Experience                     | Renewed bilingual (EN/ES) patient-facing website with service and location information  |
| 2 — Programming  | Revenue Cycle / Clinical Operations    | Billing denial rate calculator, no-show cost estimator, CME hours tracker logic         |
| 3 — AI-driven UI | Compliance / Training                  | AI-generated interfaces for compliance training modules and policy search               |
| 4 — Next.js      | Patient Experience / Clinical          | Patient appointment booking portal or internal clinical dashboard                       |
| 5 — Backend      | All                                    | HealthCore central API: patients, appointments, locations, staff, billing               |
| 6 — Telemetry    | Revenue Cycle / Operations             | Claims pipeline and real-time revenue dashboard                                         |
| 7 — RAG & Memory | Clinical / Compliance                  | Semantic knowledge base for policies, procedures, and clinical protocols                |
| 8 — Agents       | Clinical / Patient Experience / People | Documentation assistant, referral agent, CME tracker agent                              |
| 9 — Workflows    | Revenue Cycle / People / Patient Exp.  | n8n automations: no-show reminders, claim submissions, onboarding flows                 |
| 10 — Real-time   | Clinical / Executive                   | Live network KPI dashboard, compliance anomaly alerts, automated board report           |

---

## Recurring Characters

| Character              | Role                            | Origin              | Gender | Communication Style                                                                                                                       |
| ---------------------- | ------------------------------- | ------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Dr. Sandra Okonkwo** | CEO                             | American (Nigerian) | F      | Precise and demanding. Thinks like a clinician: evidence-based, low tolerance for vagueness. Sends structured emails with numbered points. |
| **Dr. Marcus Reid**    | Director of Clinical Operations | American            | M      | Protective of clinical staff time. Needs to see the patient impact before approving any new system. Calls before emailing.                |
| **Priya Nair**         | Head of Patient Experience      | British (Indian)    | F      | Empathetic and data-informed. Passionate about accessibility and health equity. Communicates warmly but precisely on Slack.                |
| **Tom Callahan**       | Revenue Cycle Director          | American            | M      | Numbers-first. Talks in percentages and dollar values. Gets impatient with anything that doesn't connect to revenue.                      |
| **Claire Whitfield**   | Chief Compliance Officer        | British             | F      | Methodical and risk-averse. Every request gets a "but have we checked the HIPAA implications?" Email chains with detailed bullet points.  |
| **Diane Foster**       | VP of People                    | American            | F      | People-first, operationally sharp. Balanced between empathy and process. Shares structured Notion docs and appreciates thoroughness.      |
| **James Osei**         | CTO                             | American (Ghanaian) | M      | Builder. Pragmatic and architecture-minded. Delivers Jira tickets with clear acceptance criteria and is direct about technical debt.      |

---

## Tone and Usage in Projects

HealthCore should appear in project statements as **the student's employer within the HealthCore Digital team**. Projects arrive as:

- **Email from Dr. Okonkwo (CEO)** with a clearly stated business problem and implicit urgency — she rarely explains why, she expects you to understand it.
- **Jira ticket from James (CTO)** with technical requirements, acceptance criteria, stack constraints, and notes about legacy system limitations.
- **Slack message from Priya or Diane** describing a patient or staff experience problem that needs a technical solution.
- **Formal memo from Claire (Compliance)** with a regulatory concern framed as a project requirement.

The student always knows that what they build **handles real patient data, operates in a regulated environment, and will be used by clinical staff who have zero tolerance for tools that waste their time**. It is not a throwaway exercise.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_For exclusive use in programme project generation_
