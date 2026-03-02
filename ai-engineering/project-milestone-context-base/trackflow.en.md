# TrackFlow — Transversal Project Company

## AI Engineering · 4Geeks Academy

---

## General Overview

**TrackFlow** is a last-mile delivery and warehouse management company founded in 2009 in Monterrey, Mexico. It operates in two markets — **Mexico and Spain (Zaragoza)** — and offers three services: warehouse management for e-commerce brands that sell in both countries, last-mile delivery (the final leg from warehouse to end customer), and reverse logistics (returns and product reconditioning). The company has approximately **130 employees** and generates around **9 million euros in annual revenue**.

Its clients are mid-sized fashion, electronics, and cosmetics brands that sell online and outsource their entire logistics operation to TrackFlow. The company grew steadily during the e-commerce boom, but that growth left an uneven technical foundation: the Monterrey and Zaragoza operations use different tools, data doesn't flow between the two countries, and the leadership team makes decisions based on information that arrives late and incomplete. Margins are under pressure because competitors are automating what TrackFlow still does by hand.

The CEO, **Daniel Espinoza**, has created an internal unit called **TrackFlow Tech** to lead the company's digital transformation. You are part of that unit.

---

## Department Map and Their Real Problems

### 🚚 Warehouse Operations

**Manager:** Ana Whitfield, Head of Warehouse Operations
**Team:** ~70 warehouse operatives + 2 warehouse managers (one per country)

**Current situation:**

- The warehouse in Monterrey and the warehouse in Zaragoza each use a different warehouse management system (WMS). One is commercial software; the other is an advanced spreadsheet.
- Real-time inventory visibility doesn't exist at a global level. To know how many units of a given product are available across both countries, someone has to call both warehouses.
- Inbound orders arrive by email in different formats depending on the client. An operative transcribes them into the local system manually.
- Picking is done with printed paper lists.
- Inventory discrepancies are frequent and detected late.

**Automation and AI needs:**

- Unified inventory API: an endpoint that returns the real-time stock of any SKU in either warehouse.
- Order ingestion pipeline: email → AI parser → validation → insertion into system.
- Warehouse operations dashboard: pending orders, processed orders, inventory discrepancies, productivity per warehouse.
- Low stock alerts: when a SKU drops below the minimum threshold, automatic notification to the client and the procurement team.
- Inventory audit system: detect discrepancy patterns and predict where they are most likely to occur next.

---

### 📦 Last Mile and Carrier Management

**Manager:** Carlos Vega, Head of Carrier Operations
**Team:** 6 logistics coordinators

**Current situation:**

- TrackFlow works with 8 carriers: Estafeta, FedEx, and DHL in Mexico; MRW, SEUR, and DHL in Spain, plus two local carriers.
- Carrier assignment for each shipment is done manually by the coordinator based on experience.
- Package tracking is inconsistent: each carrier has its own portal. When clients ask where their parcel is, the team has to check multiple systems.
- Incidents (lost parcel, failed delivery, wrong address) arrive by email with no ticket management system.
- There is no historical data on carrier performance: on-time delivery rate, incidents per route, average cost per kg.

**Automation and AI needs:**

- Carrier selection engine: given the destination, weight, product type, and urgency, the system automatically recommends the optimal carrier.
- Unified tracking: a single endpoint that aggregates parcel status from any carrier and exposes it to the client.
- Public tracking portal: a URL where the recipient can check the real-time status of their order.
- Carrier performance dashboard: success rate per carrier, average delivery time, cost per route, incidents.
- Incident management agent: when an incident arrives, the agent classifies it, opens a ticket, and proposes the corrective action.

---

### 🔄 Reverse Logistics

**Manager:** Sofía Ramos, Returns Manager
**Team:** 5 people

**Current situation:**

- Returns represent between 18% and 25% of volume depending on the client and country. Managing them well is critical to profitability.
- Current process: the end customer requests a return → Sofía's team reviews manually → approves or rejects → coordinates collection with a carrier → product arrives at warehouse → an operative inspects and classifies it.
- There are no automatic approval criteria: everything goes through human review.
- The inspection of returned products is subjective and inconsistent between operatives.
- There is no visibility into which products are returned most frequently or why.

**Automation and AI needs:**

- Automatic returns approval engine: configurable rules per client that resolve 70% of cases without human intervention.
- Automated collection flow: approval → return label generation → instructions to the customer → scheduling with carrier.
- Assisted inspection system: the operative photographs the returned product → AI classifies its condition.
- Returns dashboard: volume by country, most frequent reason, reconditioning rate, cost per return.
- Pattern analysis: identify products or routes with abnormal return rates and alert the commercial team.

---

### 📞 Customer Experience

**Manager:** Valentina Cruz, CX Manager
**Team:** 15 agents distributed between Monterrey and Zaragoza

**Current situation:**

- TrackFlow serves two types of customer: the brands (B2B) that contract their services, and the end consumers (B2C) who receive the parcels.
- The 15 agents handle both through email, WhatsApp, and phone, with no unified ticketing system.
- 80% of queries ("where is my parcel?", "I want to make a return", "there is an error in my order") could be answered automatically.
- There is no knowledge base. Answers are inconsistent between agents.
- Coverage outside office hours is zero: tickets pile up overnight.

**Automation and AI needs:**

- First-line CX agent: bilingual chatbot (Spanish + English) that automatically resolves tracking queries, return status, and frequent questions.
- Semantic knowledge base: return policies, SLAs per country, incident procedures — indexed for RAG.
- Unified ticketing system: all channels in one place with automatic prioritisation.
- Real-time CX dashboard: open tickets, average response time, CSAT, backlog per agent and per country.
- Sentiment analysis: detect frustrated customers before they escalate and assign them to a senior agent automatically.

---

### 🤝 Commercial and Client Relations

**Manager:** Miguel Torres, Commercial Director
**Team:** 8 people (4 account managers, 4 business development)

**Current situation:**

- TrackFlow's clients are mid-sized brands that sign annual contracts. Renewal is the main commercial event of the year.
- Account managers track their accounts in personal spreadsheets and email threads. There is no CRM.
- Client reporting is manual: each month, an account manager compiles data from different systems to send each client a PDF report.
- There is no visibility into which clients are at risk of not renewing or which have grown their volume enough to justify upselling.

**Automation and AI needs:**

- CRM integration: unified client profile with contract history, shipment volume, incidents, and renewal date.
- Automated client report: the agent consolidates the month's shipment data for each client and generates the PDF automatically.
- Client health dashboard: volume trend, incident rate, renewal risk score, upsell opportunities.
- Renewal alert system: 90 and 30 days before contract expiry, automatic notification to the account manager with a client summary.
- Commercial agent: given a prospect's profile and sector, suggests the most relevant service and pricing structure.

---

### 💻 Technology

**Manager:** Andrés Kim, CTO (Zaragoza)
**Team:** 7 people (3 developers, 2 data engineers, 1 sysadmin, Andrés)

**Current situation:**

- TrackFlow's tech architecture is the result of years of unplanned growth: two different WMS systems, a corporate ERP from the early 2010s, point-to-point integrations built with undocumented Python scripts, and databases in two different cloud providers.
- There is no centralised telemetry. When an endpoint fails in Monterrey, the Zaragoza team finds out via WhatsApp.
- Deployment of a new feature takes one to two weeks. There is no CI/CD.
- Andrés wants to build a unified platform, but the team is 100% busy putting out fires.

**Automation and AI needs:**

- Centralised telemetry: logs, metrics, and events from all systems and both countries in one place.
- Data pipeline: capture operational events → transform → aggregate → feed all company dashboards.
- Real-time monitoring: uptime, endpoint latency, 5xx errors, automatic alerts to the team.
- Technical documentation agent: generates and keeps endpoint documentation up to date from the codebase.
- Ops automation: backups, log rotation, health checks, incident notifications with context.

---

### 📊 Executive Direction and Reporting

**Manager:** Daniel Espinoza, CEO (Monterrey)
**Leadership team:** CTO, Commercial Director, Head of Warehouse Operations, CX Manager

**Current situation:**

- Daniel receives a consolidated report every Monday that his directors prepare on Sunday evening by combining data from different systems. The process consumes 3 to 4 hours per director.
- The report arrives at 10am Monday. By then, some data is already two days old.
- There is no unified view of the business by country.
- Strategic decisions are made with partial data.

**Automation and AI needs:**

- Global executive dashboard: KPIs from both operations in real time — shipment volume, on-time delivery rate, operational cost, returns, customer satisfaction.
- Automatically generated weekly executive report: the agent consolidates data from both countries, drafts the report, and sends it every Monday at 7am.
- Country comparisons: Daniel can explore "how did Q3 go in Mexico vs. Spain" without calling anyone.
- Strategic alerts: if the delivery SLA falls below 90% in either country, immediate notification to Daniel and Ana.
- AI executive assistant: Daniel can ask in natural language "which carrier has the most incidents in Monterrey this month?" and get a data-backed answer.

---

## Milestone Map

| Milestone        | Primary Department     | Business Deliverable                                                     |
| ---------------- | ---------------------- | ------------------------------------------------------------------------ |
| 0 — Prework      | All                    | Environment setup, first prompts about TrackFlow                         |
| 1 — Web          | Commercial / CX        | TrackFlow corporate website and public tracking portal                   |
| 2 — Programming  | Warehouse / Last Mile  | Carrier scoring logic, rate calculation, inventory management            |
| 3 — AI-driven UI | Returns / CX           | AI-generated interfaces for returns and customer portals                 |
| 4 — Next.js      | Commercial / Warehouse | B2B client portal or warehouse operations dashboard                      |
| 5 — Backend      | All                    | Unified TrackFlow API: shipments, inventory, returns, carriers           |
| 6 — Telemetry    | Technology / Direction | Data pipeline and global executive dashboard                             |
| 7 — RAG & Memory | CX / Operations        | Semantic knowledge base; search over policies and procedures by country  |
| 8 — Agents       | CX / Returns / HR      | 24/7 support agent, returns agent, onboarding agent                      |
| 9 — Workflows    | Commercial / Warehouse | n8n automations: client reporting, stock alerts, weekly executive report |
| 10 — Real-time   | Last Mile / Direction  | Live parcel tracking, real-time operations dashboard, push alerts        |

---

## Recurring Characters

| Character           | Role                          | Origin                      | Gender | Communication Style                                                                                           |
| ------------------- | ----------------------------- | --------------------------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| **Daniel Espinoza** | CEO                           | Mexican (Latin)             | M      | Direct and data-driven. Always asks "how much does it cost?" and "when will it be done?" Not very technical.  |
| **Sofía Ramos**     | Returns Manager               | Mexican (Latin)             | F      | Organised, high tolerance for ambiguity. Wants clear rules and controlled exceptions.                         |
| **Valentina Cruz**  | CX Manager                    | Latin American (Venezuelan) | F      | Empathetic and demanding. Always thinks from the end customer's perspective. Bilingual (Spanish/English).     |
| **Ashley Morris**   | Head of Commercial Operations | American                    | F      | Structured and metrics-driven. Clear, concise emails. Wants dashboards she can share with clients directly.   |
| **Brian Calloway**  | Senior Data Analyst           | American                    | M      | Analytical and precise. Speaks in percentages and trends. Loves a well-structured dataset.                    |
| **Andrés Kim**      | CTO                           | Other (Korean-Mexican)      | M      | Meticulous and systematic. Detailed technical specs. Obsessed with scalability and observability.             |
| **Carlos Vega**     | Head of Carrier Operations    | Spanish                     | M      | Knows the carriers better than anyone. Very detail-oriented in integration requirements.                      |
| **Ana Whitfield**   | Head of Warehouse Operations  | Spanish                     | F      | Pragmatic and operational. Thinks in physical processes. Distrustful of technology until she sees it working. |

---

## Tone and Usage in Projects

TrackFlow appears in project statements as **the student's employer within the TrackFlow Tech unit**. Projects arrive as:

- **Email from Daniel (CEO)** with an urgent business need and a tight deadline.
- **Technical spec from Andrés (CTO)** with architecture requirements and acceptance criteria.
- **Request from a department head** (Ana, Carlos, Sofía, Valentina) describing their operational problem.
- **Ticket from the project management system** (Linear or Jira) assigned by the tech lead.

The student always knows that what they build **goes to production at TrackFlow** and that warehouse operatives and account managers in Monterrey and Zaragoza will be using it tomorrow.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
_For exclusive use in programme project generation_
