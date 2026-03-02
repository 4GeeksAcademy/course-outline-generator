# Brasaland — Transversal Project Company

## AI Engineering · 4Geeks Academy

---

## General Overview

**Brasaland** is a grilled food restaurant chain founded in 2008 in Medellín, Colombia. What began as a single family-run location has grown into a chain of **14 company-owned restaurants** operating in Colombia and the United States (Florida). The company employs approximately **115 people** between kitchen and floor staff, operations management, and the corporate team headquartered in Medellín, with a commercial office in Miami. Annual revenue sits around **6 million dollars**.

The brand is built on three pillars: consistent product quality across every location, a warm and reliable customer experience, and speed of service. The challenge is that maintaining those three pillars across two very different markets — Colombia and Florida — is increasingly difficult without proper technology. Competitors are winning customers with digital loyalty programmes, real-time operations dashboards, and data-driven decision-making. Brasaland is still managing most of this by instinct and spreadsheet.

The CEO, **Mariana Restrepo**, daughter of the founder, has created an internal team called **Brasaland Digital** to lead the company's transformation. She knows the business in depth and has a clear vision of where she wants to take it — she just needs the technical team to build the tools that get her there. You are part of that team.

---

## Department Map and Their Real Problems

### 🍖 Restaurant Operations

**Manager:** Felipe Guerrero, Operations Director
**Team:** 4 operations supervisors + ~85 kitchen and floor staff across 14 locations

**Current situation:**

- Each location has a manager who handles daily operations: staff scheduling, cash opening and closing, ingredient orders from suppliers, and waste tracking.
- There is no centralised visibility into what is happening at each location. Felipe doesn't know how many covers were served today at the Medellín downtown location or whether the Miami one is having a slow week.
- Ingredient orders are placed by WhatsApp or phone call. Each manager orders what they think they need. The result: overstock in some locations, stockouts in others.
- Waste tracking (product lost to expiry, cooking errors, or theft) is manual and inconsistent.
- Shift reports are filled out on paper or Excel and sent to HR week by week.
- Operating in Colombia and Florida means dealing with two currencies (COP and USD), two languages (Spanish and English), and two very different regulatory environments — all without a system to manage either.

**Automation and AI needs:**

- Real-time operations dashboard: daily sales per location, covers served, average ticket, comparison vs. same day last week — displayed in both currencies.
- Ingredient ordering system: based on historical sales and available stock, the system generates the suggested order for the supplier automatically.
- Digitised waste tracking: the manager logs waste in an app, the system detects anomalies and alerts the operations team.
- Operations alerts: if a location has no registered sales for two hours during opening hours, automatic notification to Felipe.
- Manager support agent: answers frequent operational questions in Spanish or English depending on the location.

---

### 🛒 Procurement and Suppliers

**Manager:** Lucía Fernández, Procurement Manager
**Team:** 3 people

**Current situation:**

- Brasaland works with around 20 suppliers between Colombia and Florida: meat, vegetables, sauces, beverages, packaging, and cleaning products, with different suppliers in each country.
- Price and terms negotiation happens by email and Excel. There is no contract management system.
- The prices of key raw materials — especially meat — fluctuate significantly and differently in each market. Lucía finds out about price changes when the invoice arrives.
- There is no consolidated data on purchasing across the chain. Colombia and Florida negotiate independently.
- The process to approve a new supplier is slow: paper forms, manual validations, no traceability.

**Automation and AI needs:**

- Supplier management platform: profile for each supplier, active contracts, price history, quality ratings — segmented by country.
- Price variation alerts: when the price of a key ingredient rises above a threshold in either market, immediate notification to Lucía and the CEO.
- Purchasing consolidation: visibility of total volume by ingredient across the chain, to identify central negotiation opportunities.
- Automated supplier approval process: digital form → validation → approval → system registration.
- Procurement analysis agent: "how much did we spend on beef this quarter in Florida compared to Colombia?"

---

### 📱 Marketing, Brand and Digital Experience

**Manager:** Camila Ospina, Marketing Manager
**Team:** 4 people + freelance support

**Current situation:**

- The Brasaland website exists but is from 2019, doesn't allow online orders, and only shows the menu. Its app store rating is 2.8.
- The loyalty programme ("Brasa Points") runs on physical stamp cards. Cards get lost, generate no data, and 60% of customers don't use them.
- Marketing campaigns are produced in Medellín and adapted for the Florida market manually and often late.
- Social media is managed from each office with different criteria. Brand perception is inconsistent between Colombia and the US.
- There is no data about who Brasaland's customers actually are: no age, visit frequency, or preferences.

**Automation and AI needs:**

- Digital loyalty and ordering app: online ordering, payment, digital point accumulation, visit history — bilingual (Spanish/English).
- Customer CRM: unified customer profile with order history, visit frequency, preferences, and accumulated points.
- Personalisation engine: based on customer history, suggest products or launch personalised offers.
- Marketing dashboard: CAC, LTV, average visit frequency, campaign conversion, Brasa Points evolution — by market.
- AI-assisted content pipeline: campaign briefing → copy generation adapted to each market and language → review → publish.
- Communication automation: emails and push notifications segmented by customer behaviour and language.

---

### 🧑‍🤝‍🧑 People and Culture

**Manager:** Ashley Turner, People Manager (Miami)
**Team:** 3 people

**Current situation:**

- Managing 115 people across 14 locations in two countries with very different labour laws involves significant administrative overhead.
- Most HR processes run by email and Excel. There is no HR information system.
- Onboarding a new team member — especially kitchen staff, who turn over frequently — is manual.
- There is no visibility into key indicators: turnover by location, absenteeism, average time to hire for operational roles.
- Colombian and US labour regulations differ substantially. Managing both without a system is error-prone and legally risky.

**Automation and AI needs:**

- Internal HR portal: holiday requests, contract consultation, absence management — bilingual.
- Automated onboarding flow for new hires: checklist, document delivery, step completion tracking.
- HR KPI dashboard: headcount per location, monthly turnover, absenteeism rate, average time to fill vacancies — by country.
- Internal HR agent: answers frequent questions from team members about policies, schedules, and benefits in Spanish or English.

---

### 🎓 Training and Quality Standards

**Manager:** Jake Morrison, Head of Training (Miami)
**Team:** 3 people

**Current situation:**

- Every location must follow the same recipes, preparation techniques, and presentation standards regardless of country.
- Training materials are stored in a shared Google Drive that nobody can navigate easily.
- New staff receive a printed manual and a 2-day shadowing period. After that, they're on their own.
- There is no system to verify that standards are being met between visits to each location.
- When a recipe or procedure changes, communicating the update to all 14 locations in two languages takes days and often creates confusion.

**Automation and AI needs:**

- Training platform: searchable catalogue of recipes, technique guides, and quality standards — available in Spanish and English.
- Digital procedure manual: always up to date, accessible from any device in the kitchen.
- New staff onboarding flow: structured learning path with confirmation checkpoints.
- Standards update system: when a recipe changes, all locations are notified immediately with the updated version in both languages.
- Training support agent: staff can ask "how is the house sauce prepared?" in Spanish or English and get the official answer immediately.

---

### 💻 Technology

**Manager:** Nicolás Park, CTO (Medellín)
**Team:** 4 people (2 developers, 1 sysadmin, Nicolás)

**Current situation:**

- Brasaland's technology stack is minimal: a static corporate website, the outdated app, a different POS terminal in each country with no integration between them, and spreadsheets acting as management systems.
- There is no internal API. No consolidated data. No telemetry.
- Nicolás has the mandate to build Brasaland's digital platform from near-zero, with a small team and a tight budget.
- Everything built must be modular, work equally well in Colombia and Florida, and be maintainable by a small team.

**Automation and AI needs:**

- Brasaland central API: endpoints for locations, menus, sales, customers, suppliers, and staff.
- Telemetry: events from each location captured and processed in real time.
- Data pipeline: POS → API → transformation → operations, marketing, and finance dashboards.
- Platform monitoring: uptime, errors, latency, automatic alerts to the team.
- Internal technical support agent: answers team questions about the architecture, APIs, and deployment procedures.

---

### 📊 Executive Direction and Reporting

**Manager:** Mariana Restrepo, CEO (Medellín)

**Current situation:**

- Mariana manages a 14-location chain across two very different markets without a unified dashboard. Her decisions are based on calls with the operations team, PDF reports that arrive on Tuesday, and gut feeling.
- She cannot answer in real time: "how much did we sell this week in Florida?" or "which location has the highest average ticket this month?"
- Investors and partners ask for quarterly presentations that the team spends a week preparing manually.

**Automation and AI needs:**

- Executive dashboard: total chain sales in USD and COP, breakdown by country and location, comparison vs. previous period, top and bottom performers of the week.
- Automated weekly report: the agent consolidates data, drafts the executive report, and sends it every Monday at 7am.
- AI executive assistant: Mariana can ask in natural language "which are the three locations with the worst sales trend this month?" and get a data-backed answer.
- Strategic alerts: if sales in a country drop more than 15% vs. the previous week, immediate notification to Mariana and Felipe.

---

## Milestone Map

| Milestone        | Primary Department                | Business Deliverable                                                           |
| ---------------- | --------------------------------- | ------------------------------------------------------------------------------ |
| 0 — Prework      | All                               | Environment setup, first prompts about Brasaland                               |
| 1 — Web          | Marketing                         | Renewed bilingual corporate website                                            |
| 2 — Programming  | Finance / Operations              | Margin calculation logic, location scoring, waste control                      |
| 3 — AI-driven UI | Training / Product                | AI-generated interfaces for the training platform and recipe catalogue         |
| 4 — Next.js      | Marketing / Customers             | Customer loyalty app or staff-facing operations portal                         |
| 5 — Backend      | All                               | Brasaland central API: locations, menus, sales, customers                      |
| 6 — Telemetry    | Operations / Finance              | POS sales pipeline and real-time financial dashboard                           |
| 7 — RAG & Memory | Training / CX                     | Semantic knowledge base for recipes, standards, and procedures                 |
| 8 — Agents       | Operations / HR / Training        | Manager support agent, onboarding agent, training assistant                    |
| 9 — Workflows    | Procurement / Finance / Marketing | n8n automations: ingredient orders, monthly close, segmented campaigns         |
| 10 — Real-time   | Operations / Direction            | Live sales dashboard per location, incident alerts, automatic executive report |

---

## Recurring Characters

| Character            | Role                         | Origin                   | Gender | Communication Style                                                                                                   |
| -------------------- | ---------------------------- | ------------------------ | ------ | --------------------------------------------------------------------------------------------------------------------- |
| **Mariana Restrepo** | CEO                          | Colombian (Latin)        | F      | Visionary and impatient. Voice notes or short messages. Wants visible results fast.                                   |
| **Felipe Guerrero**  | Operations Director          | Colombian (Latin)        | M      | Operational and direct. Thinks in physical processes. Bullet-point emails, no frills.                                 |
| **Camila Ospina**    | Marketing Manager            | Colombian (Latin)        | F      | Creative and customer-focused. Wants everything to look good and be easy to use. Very active on Slack.                |
| **Ashley Turner**    | People Manager               | American                 | F      | Structured and compliance-aware. Thinks in processes and legal frameworks. Clear, professional emails.                |
| **Jake Morrison**    | Head of Training             | American                 | M      | Perfectionist about consistency. Hands-on. Distrustful of technology until he sees it working.                        |
| **Lucía Fernández**  | Procurement Manager          | Spanish                  | F      | Analytical and methodical. Speaks in numbers and percentages. Very precise in her requirements.                       |
| **Carlos Jiménez**   | Senior Operations Supervisor | Spanish                  | M      | Experienced, calm under pressure. Thorough and well-structured in his reports.                                        |
| **Nicolás Park**     | CTO                          | Other (Korean-Colombian) | M      | Pragmatic and minimal. Prefers doing less but doing it well. Delivers specs in Notion with clear acceptance criteria. |

---

## Tone and Usage in Projects

Brasaland should appear in project statements as **the student's employer within the Brasaland Digital team**. Projects arrive as:

- **Voice note transcript from Mariana (CEO)** with an urgent, loosely defined idea that the student must turn into a spec.
- **Notion doc from Nicolás (CTO)** with technical requirements, acceptance criteria, and stack restrictions.
- **Email from a department head** (Felipe, Camila, Ashley, Jake, Lucía) describing their problem with operational detail.
- **Task ticket** assigned by the tech lead.

The student always knows that what they build **will be used tomorrow by the managers of 14 locations across Colombia and Florida** — it is not a throwaway exercise.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_For exclusive use in programme project generation_
