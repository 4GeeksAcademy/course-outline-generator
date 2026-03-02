# Nexova — Transversal Project Company

## AI Engineering · 4Geeks Academy

---

## General Overview

**Nexova** is a human resources consulting and talent acquisition firm founded in 2011, headquartered in Santiago, Chile, with a commercial office in Buenos Aires, Argentina. It has **120 employees** and operates across three business lines: executive and mid-management headhunting, customer support team outsourcing for technology companies, and corporate training in soft skills and leadership. The company generates approximately **8 million dollars in annual revenue**.

Its clients are primarily mid-sized companies in the technology, retail, and financial services sectors that outsource part of their talent management. Nexova has operated successfully for years, but is now feeling competitive pressure from new automated recruiting platforms that are beginning to take market share.

The CEO, **Laura Mendoza**, has bet on AI as a competitive advantage and has assembled an AI Engineering team to lead that transformation. You are part of that team.

---

## Department Map and Their Real Problems

### 🌐 Marketing and Communications

**Manager:** Carmen Ruiz, Head of Marketing
**Team:** 5 people

**Current situation:**

- They manage Nexova's digital presence: corporate website, LinkedIn, monthly newsletter, and blog.
- The website was built in 2019 and hasn't been meaningfully updated. It's slow, not accessible, and doesn't reflect the company's current positioning.
- Content is produced manually: writers draft blog posts, designers create social media graphics, and an external freelancer handles SEO.
- They don't measure the real impact of their content: they know how many visits they get but not where visitors come from or what converts.

**Automation and AI needs:**

- Full redesign of the corporate website: accessible, SEO/GEO optimised, with schema.org markup.
- AI-assisted content pipeline: briefing → draft → review → publish.
- Marketing metrics dashboard: visits, traffic sources, contact form conversion rate.
- Automated newsletter delivery segmented by client type.

---

### 💼 Sales and Business Development

**Manager:** Marcos Ibáñez, Sales Director
**Team:** 18 people (6 account managers, 12 SDRs)

**Current situation:**

- SDRs prospect manually on LinkedIn, export lists to Excel, and follow up by email with no automation.
- They have a CRM (HubSpot) but only 40% of the team updates it consistently.
- The sales cycle runs between 3 and 8 weeks. Many deals are lost due to lack of follow-up.
- There is no visibility into which clients are most likely to close or what the real state of the pipeline is.

**Automation and AI needs:**

- CRM integration with an agent that drafts personalised follow-up emails.
- Sales pipeline dashboard: deals by stage, monthly forecast, team activity.
- Prospecting sequence automation: first contact → follow-up 1 → follow-up 2 → close or discard.
- Alert system for deals with no activity in more than X days.
- AI agent that, given a prospect's profile, suggests the most appropriate proposal angle.

---

### 🧑‍🤝‍🧑 Human Resources (Internal)

**Manager:** Patricia Solís, HR Manager
**Team:** 4 people

**Current situation:**

- Holiday requests, absences, and HR queries are managed by email and spreadsheets.
- New employee onboarding is manual: Patricia sends a PDF with instructions and follows up via Slack.
- Performance reviews happen twice a year through Google Forms that nobody reviews systematically.
- There is no visibility into key indicators: turnover, absenteeism, average internal hiring time.

**Automation and AI needs:**

- Internal HR portal: holiday requests, payslip access, absence management.
- Automated onboarding flow: progressive checklist, material assignment, step completion validation.
- HR KPI dashboard: headcount, monthly turnover, average time to fill internal vacancies.
- Internal HR agent that answers frequent team questions about policies, benefits, and procedures.

---

### 🔍 Talent Selection Operations (core business)

**Manager:** Javier Almeida, Operations Manager
**Team:** 40 selection consultants

**Current situation:**

- Consultants receive job briefings by email and enter them manually into their proprietary ATS, which is old and slow.
- CV screening is manual: each consultant reads between 30 and 80 CVs per search.
- Candidate communication is done by individual email, with no automated templates.
- There is no system to know the real-time status of each candidate. Clients call to ask.
- Matching between candidate and vacancy is done by consultant intuition and experience.

**Automation and AI needs:**

- AI-assisted selection pipeline: CV intake → data extraction → automatic scoring → ranking.
- RAG system over the candidate database: "find profiles with B2B sales experience and C1 English level."
- Candidate portal: real-time process status, uploaded documents, scheduled interviews.
- Communication agent: automatic status emails (shortlisted, rejected, interview scheduled).
- Selection operations dashboard: active vacancies, candidates per stage, average time to fill.

---

### 🎓 Corporate Training

**Manager:** Elena Vargas, Learning & Development Manager
**Team:** 12 people

**Current situation:**

- The training catalogue lives in a PDF updated quarterly.
- Enrolments are handled through a Google Form managed manually in a spreadsheet.
- Tracking of who completed which training doesn't exist beyond Excel attendance lists.
- Personalisation is zero: every client receives the same catalogue proposal.

**Automation and AI needs:**

- Training catalogue platform: search, filtering by area or level, online enrolment.
- Recommendation system: given a client's profile and objectives, suggest the most relevant programmes.
- Learner portal: my enrolments, progress, certificates.
- Training advisory agent: chatbot that takes the client's needs and proposes a training plan.
- L&D dashboard: enrolments by programme, completion rate, NPS per course.

---

### 📞 Customer Support (outsourced service)

**Manager:** Roberto Díaz, Customer Support Lead
**Team:** 30 agents providing support to Nexova's outsourcing clients

**Current situation:**

- The 30 agents handle incidents from Nexova's clients (tech, retail, and finance companies) by phone, email, and web chat, using a legacy helpdesk.
- There is no centralised knowledge base: each agent resolves issues based on experience and a shared Word document on Drive.
- Average resolution time is 48 hours for non-urgent tickets. The committed SLA is 24 hours.
- Supervisors have no real-time visibility into workload per agent or the state of the backlog.

**Automation and AI needs:**

- First-line support agent: chatbot that resolves 40% of queries without human intervention, using RAG over the knowledge base.
- Centralised knowledge base with semantic search.
- Real-time support dashboard: open tickets, average response time, backlog per agent, SLA at risk.
- Automatic escalation system: if a ticket goes unattended for more than X hours, reassign and notify the supervisor.
- Ticket sentiment analysis: identify dissatisfied clients before they escalate.

---

### 💻 Technology and Infrastructure

**Manager:** Sergio Molina, CTO
**Team:** 6 people (2 developers, 2 sysadmins, 1 QA, Sergio)

**Current situation:**

- The technology stack is a patchwork of disconnected tools: HubSpot, legacy Zendesk, Google Workspace, a home-built ATS from the 2010s, and multiple spreadsheets acting as management systems.
- There is no telemetry or centralised logging. When something fails, the team finds out through users.
- Deployments are manual. There is no CI/CD.
- Sergio wants to build a unified platform but doesn't have enough team capacity.

**Automation and AI needs:**

- Centralised telemetry: error logs, system events, automatic alerts.
- Data pipeline: capture events from all applications → transform → aggregate → feed dashboards.
- Monitoring system: uptime, endpoint latency, real-time 5xx errors.
- Internal engineering agent: answers questions about system architecture by querying technical documentation (RAG over docs).
- Automation of repetitive ops tasks: backups, log rotation, incident notifications.

---

### 📊 Executive Direction and Reporting

**Manager:** Laura Mendoza, CEO + leadership team

**Current situation:**

- Laura receives a weekly PDF report prepared manually by each department head. Preparation takes between 4 and 8 hours per manager.
- There is no unified view of the business. To know how many selection processes are active, Laura calls Javier. To know if the sales team is on track, she calls Marcos.
- Strategic decisions are made with data that is a week old, not real-time.

**Automation and AI needs:**

- Unified executive dashboard: KPIs from all areas in one place, updated in real time.
- Automatically generated executive report: the agent consolidates data, drafts the report, and sends it every Monday at 8am.
- Strategic alerts: if any KPI falls below a threshold, notify leadership immediately.
- AI executive assistant: Laura can ask in natural language "how did last month's selection performance compare to the previous one?" and get a data-backed answer.

---

## Milestone Map

| Milestone        | Primary Department     | Business Deliverable                                              |
| ---------------- | ---------------------- | ----------------------------------------------------------------- |
| 0 — Prework      | All                    | Environment setup, first prompts about Nexova                     |
| 1 — Web          | Marketing              | Nexova's corporate website                                        |
| 2 — Programming  | Operations / HR        | CV scoring logic, basic KPI calculation                           |
| 3 — AI-driven UI | Training / Candidates  | AI-generated interfaces for internal portals                      |
| 4 — Next.js      | Selection / Sales      | Interactive frontend for the ATS or sales portal                  |
| 5 — Backend      | All                    | Nexova API: endpoints for candidates, vacancies, clients          |
| 6 — Telemetry    | Technology / Direction | Data pipeline and executive dashboard                             |
| 7 — RAG & Memory | Support / Selection    | Semantic knowledge base; candidate search                         |
| 8 — Agents       | Support / HR / Sales   | First-line agents: support, onboarding, prospecting               |
| 9 — Workflows    | Operations / Marketing | n8n automations: selection pipeline, newsletter, executive report |
| 10 — Real-time   | Support / Direction    | Live support dashboard, push notifications, event streaming       |

---

## Recurring Characters

| Character          | Role                  | Origin                    | Gender | Communication Style                                                                          |
| ------------------ | --------------------- | ------------------------- | ------ | -------------------------------------------------------------------------------------------- |
| **Laura Mendoza**  | CEO                   | Chilean (Latin)           | F      | Direct, results-oriented. Communicates by email with high-level ideas. Not very technical.   |
| **Javier Almeida** | Operations Manager    | Chilean (Latin)           | M      | Pragmatic. Describes problems with a lot of operational detail. Low patience for technology. |
| **Elena Vargas**   | L&D Manager           | Argentine (Latin)         | F      | Creative, detail-oriented. Wants learners to have the best possible experience.              |
| **Megan Clarke**   | Head of Sales         | American                  | F      | Impatient, numbers-driven. Wants fast results and clear dashboards. Short, direct messages.  |
| **Tom Reeves**     | Senior Sales Analyst  | American                  | M      | Methodical and data-literate. Always wants the underlying numbers, not the summary.          |
| **Sergio Molina**  | CTO                   | Spanish                   | M      | Technical, meticulous. Delivers detailed specs. Values scalability and security.             |
| **Carmen Ruiz**    | Head of Marketing     | Spanish                   | F      | Brand and experience-focused. Knows what she wants visually but not how to build it.         |
| **Roberto Díaz**   | Customer Support Lead | Other (Dominican-Chilean) | M      | Under constant pressure. Needs real-time visibility and tools his team will actually adopt.  |

---

## Tone and Usage in Projects

Nexova should appear in project statements as **the student's client or employer**, never as an academic example. Projects are always framed from one of these angles:

- **Email from a manager** with a specific request and a deadline.
- **Spec from Sergio (CTO)** with detailed technical requirements.
- **Kickoff meeting** in which the team receives the transversal project brief.
- **Jira or Notion ticket** assigned by the tech lead.

The student always knows that what they build **goes to production at Nexova** — it is not a throwaway exercise.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_For exclusive use in programme project generation_
