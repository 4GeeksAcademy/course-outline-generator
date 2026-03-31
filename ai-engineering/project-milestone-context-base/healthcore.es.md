# HealthCore — Empresa del Proyecto Transversal

## AI Engineering · 4Geeks Academy

---

## Visión General

**HealthCore** es una empresa de servicios sanitarios ambulatorios fundada en 2011 en Austin, Texas. Opera una red de **12 clínicas ambulatorias** — 9 en Estados Unidos (Texas, Florida y Georgia) y 3 en el Reino Unido (Londres y Mánchester) — que ofrecen atención primaria, consultas con especialistas, gestión de enfermedades crónicas y programas de salud preventiva. La empresa cuenta con aproximadamente **200 empleados** entre personal clínico, operaciones, administración y una unidad tecnológica en crecimiento. La facturación anual ronda los **28 millones de dólares**.

La ventaja competitiva de HealthCore siempre ha sido la accesibilidad: citas el mismo día, horario ampliado y personal bilingüe en los mercados estadounidenses. Pero operar en dos países con marcos regulatorios sanitarios distintos — HIPAA en EE.UU., UK GDPR y estándares NHS en el Reino Unido — y gestionar datos de pacientes, flujos clínicos y procesos de seguros en 12 centros sin una plataforma unificada empieza a pasar factura. Las tasas de no-shows están subiendo, los errores de facturación son costosos, y los equipos clínicos dedican horas a tareas administrativas que no deberían tener que hacer.

La CEO, **Dra. Sandra Okonkwo**, médica reconvertida en directiva, fundó HealthCore tras años de frustración con la carga administrativa dentro de los grandes sistemas hospitalarios. Su pensamiento es profundamente clínico y se opone radicalmente a la tecnología por la tecnología — pero sabe que sin sistemas adecuados, la empresa no puede crecer. Ha creado una unidad interna llamada **HealthCore Digital** para construir la infraestructura que los equipos clínicos y operativos necesitan. Tú formas parte de ese equipo.

---

## Mapa de Departamentos y Sus Problemas Reales

### 🏥 Operaciones Clínicas

**Responsable:** Dr. Marcus Reid, Director de Operaciones Clínicas (Austin)
**Equipo:** ~120 profesionales clínicos (médicos, enfermeros practicantes, enfermeros, auxiliares médicos) distribuidos en 12 centros

**Situación actual:**

- Cada clínica opera de forma semi-independiente. La admisión de pacientes, la programación de citas y la documentación clínica siguen procesos locales distintos según cuándo se abrió cada centro y quién lo configuró.
- No existe un historial clínico electrónico (EHR) unificado entre los centros de EE.UU. y los del Reino Unido. Las clínicas estadounidenses usan un EHR heredado de 2014; las del Reino Unido utilizan un sistema diferente, y ninguno se integra con el otro.
- El personal clínico dedica una media de 35 minutos al día a documentación fuera del tiempo de atención al paciente: notas post-visita, cartas de derivación y resúmenes de resultados de laboratorio.
- La gestión de derivaciones es completamente manual: un auxiliar médico envía las cartas por fax y hace seguimiento por teléfono. Tiempo medio de resolución de una derivación: 11 días.
- Los pacientes con enfermedades crónicas (diabetes, hipertensión, asma) no tienen un programa de seguimiento estructurado entre visitas. Los reingresos evitables no se rastrean.

**Necesidades de automatización e IA:**

- API unificada de pacientes: un único endpoint para datos demográficos, historial de visitas, diagnósticos, prescripciones y resultados de laboratorio — accesible para el personal de EE.UU. y del Reino Unido.
- Asistente de documentación clínica: escucha la conversación entre paciente y médico (con consentimiento) y genera un borrador estructurado de nota SOAP para que el médico revise y firme.
- Flujo automatizado de derivaciones: derivación creada en el sistema → asignada al especialista → estado rastreado → paciente notificado — sin fax, sin seguimiento telefónico.
- Programa de seguimiento de pacientes crónicos: contactos automatizados (SMS o email) para pacientes con enfermedades crónicas entre visitas; las respuestas preocupantes se señalan al equipo asistencial.
- Dashboard de KPIs clínicos: pacientes atendidos por día, tiempo medio de espera, acumulación de documentación pendiente, tasa de resolución de derivaciones — por clínica y por país.

---

### 📋 Experiencia del Paciente y Acceso

**Responsable:** Priya Nair, Responsable de Experiencia del Paciente (Londres)
**Equipo:** 8 coordinadoras de pacientes + personal de recepción en los 12 centros

**Situación actual:**

- La reserva de citas está fragmentada: los pacientes en EE.UU. reservan por teléfono o a través de un portal exclusivo para ese mercado; los del Reino Unido llaman a la recepción. No existe un sistema de reservas online compartido entre mercados.
- La tasa de no-shows (ausencias sin aviso) es del 22% de media en la red, lo que supone una pérdida estimada de 800.000 dólares anuales en capacidad desaprovechada.
- Las encuestas de satisfacción de pacientes son en papel, se recogen al salir de la consulta y nunca se agregan ni se analizan.
- Cuando un paciente es derivado internamente de una clínica HealthCore a otra (por ejemplo, de atención primaria a una clínica de especialistas), el centro receptor no tiene acceso previo al historial del paciente hasta el día de la cita.
- Los pacientes con competencia limitada en inglés (principalmente hispanohablantes y lusohablantes en Florida) abandonan con frecuencia el seguimiento porque las comunicaciones les llegan solo en inglés.

**Necesidades de automatización e IA:**

- Plataforma unificada de reserva de citas: reservas online en los 12 centros, disponible en inglés y español, con disponibilidad en tiempo real y confirmación automática.
- Sistema de prevención de no-shows: secuencia automatizada de recordatorios (48h, 24h, 2h) por SMS y email, con enlace de reprogramación en un clic. Puntuación de riesgo inteligente para identificar citas con alta probabilidad de ausencia y hacer contacto proactivo.
- Pipeline de satisfacción del paciente: encuesta post-visita enviada automáticamente tras cada cita; respuestas agregadas en un dashboard semanal de NPS por centro y tipo de servicio.
- Traspaso interno de derivaciones: cuando un paciente es derivado entre clínicas HealthCore, el profesional receptor ve un resumen del historial relevante antes de la cita.
- Comunicación multilingüe con el paciente: todos los mensajes automatizados generados en el idioma preferido del paciente (inglés, español).

---

### 💰 Ciclo de Ingresos y Facturación

**Responsable:** Tom Callahan, Director de Ciclo de Ingresos (Austin)
**Equipo:** 6 personas (especialistas en facturación, codificadores, analistas de cuentas por cobrar)

**Situación actual:**

- La facturación en EE.UU. opera bajo el reembolso de seguros (seguro comercial + Medicare/Medicaid). La facturación en el Reino Unido es una combinación de pago privado y un pequeño contrato con el NHS. Los dos flujos de ingresos los gestionan equipos completamente separados sin informes compartidos.
- La tasa de denegación de reclamaciones es del 14% — muy por encima del benchmark del sector, que está entre el 5% y el 8%. La mayoría de las denegaciones se deben a errores de codificación y a autorizaciones previas ausentes, ambas situaciones prevenibles.
- El equipo de facturación revisa manualmente cada reclamación antes de enviarla. Con alrededor de 600 visitas semanales, esto genera un cuello de botella: el tiempo medio entre la visita y el envío de la reclamación es de 5 días.
- No existe ningún sistema que alerte sobre pacientes con cobertura de seguro caducada antes de su cita. La recepción suele descubrirlo en el momento del check-in.
- Los informes de ingresos mensuales por país los elabora Tom manualmente y le ocupan 2 días laborables completos.

**Necesidades de automatización e IA:**

- Motor de prevalidación de reclamaciones: antes de cada visita, el sistema verifica la elegibilidad del seguro, señala autorizaciones previas ausentes e identifica posibles problemas de codificación según el servicio programado.
- Pipeline automatizado de envío de reclamaciones: datos estructurados de la visita → sugerencia de código ICD/CPT → revisión del codificador → envío — reduciendo la revisión manual a la gestión de excepciones únicamente.
- Rastreador de gestión de denegaciones: las reclamaciones denegadas se enrutan automáticamente al especialista adecuado con el código de motivo, el plazo de reenvío previsto y una plantilla de apelación.
- Dashboard de ingresos: cobros por centro, tasa de denegación por pagador y tipo de servicio, antigüedad de cuentas por cobrar, reparto de ingresos EE.UU. vs. Reino Unido — actualizado diariamente.
- Agente de reporting financiero: "¿cuál es nuestra tasa neta de cobro para pacientes de Medicare en Texas este trimestre?" respondido desde los datos, no desde una hoja de cálculo.

> **Nota regulatoria:** Las reclamaciones en EE.UU. contienen Información de Salud Protegida (PHI) bajo HIPAA — cualquier pipeline que toque estos datos requiere un Acuerdo de Socio Comercial (BAA) firmado con todos los proveedores y un registro de auditoría completo. Los datos de facturación en el Reino Unido están sujetos a UK GDPR; se requiere un Acuerdo de Tratamiento de Datos (DPA) con cualquier procesador externo.

---

### 🧬 Cumplimiento Normativo y Gobernanza de Datos

**Responsable:** Claire Whitfield, Directora de Cumplimiento Normativo (Londres)
**Equipo:** 3 personas

**Situación actual:**

- HealthCore gestiona datos de pacientes bajo HIPAA en EE.UU. y UK GDPR en el Reino Unido. Las normas difieren en aspectos clave: HIPAA permite 60 días para notificar una brecha; UK GDPR exige notificación a la ICO en 72 horas. Los períodos de retención de datos, los derechos de acceso de los pacientes y los requisitos de acuerdos con proveedores son distintos en cada país.
- No existe un registro de auditoría automatizado de quién accedió a qué historial de paciente. Si se produce una posible brecha, la reconstrucción es manual y lleva días.
- La formación del personal en privacidad de datos es anual, se imparte mediante una presentación de PowerPoint y el seguimiento de completitud se lleva en una hoja de cálculo.
- Las políticas y procedimientos están almacenados en una carpeta compartida que no se ha auditado en 18 meses. Algunos documentos hacen referencia a regulaciones que desde entonces han sido actualizadas.
- La diligencia debida con proveedores — confirmar que los socios tecnológicos han firmado los BAA (EE.UU.) y los DPA (Reino Unido) — se rastrea manualmente en una hoja de cálculo que Claire gestiona en solitario.

**Necesidades de automatización e IA:**

- Sistema de registro de auditoría de accesos: cada evento de acceso a datos de pacientes (quién, qué historial, cuándo, desde qué centro) capturado y consultable, con detección automática de anomalías en patrones de acceso inusuales.
- Plataforma de formación en cumplimiento normativo: módulos de formación anual por rol con seguimiento de finalización mediante cuestionarios y generación automática de certificados.
- Sistema de gestión de políticas: biblioteca de políticas con búsqueda, control de versiones, alertas de fecha de revisión y notificaciones de cambios al personal relevante.
- Rastreador de cumplimiento de proveedores: estado de BAA/DPA por proveedor, fechas de renovación, nivel de riesgo — alerta automática cuando un acuerdo se acerca a su vencimiento.
- Asistente de cumplimiento normativo: responde preguntas del personal sobre qué está y qué no está permitido bajo HIPAA y UK GDPR en lenguaje claro, con referencias a la política correspondiente.

---

### 🧑‍💼 Personas y Fuerza Laboral

**Responsable:** Diane Foster, VP de Personas (Austin)
**Equipo:** 4 personas

**Situación actual:**

- Gestionar 200 empleados en 12 centros en dos países con marcos laborales distintos supone una carga administrativa constante y una complejidad legal permanente.
- La contratación es de alto volumen y urgente: los roles clínicos son difíciles de cubrir, el tiempo medio de contratación para un enfermero practicante es de 47 días, y las tasas de vacantes en centros de EE.UU. rondan el 11%.
- El proceso de incorporación es inconsistente según el centro. El personal clínico nuevo a menudo empieza sin haber completado la formación obligatoria en cumplimiento normativo, lo que genera riesgo regulatorio.
- No existe ningún sistema que registre las horas de formación médica continuada (CME) de médicos y enfermeros practicantes, que están obligados a acreditarlas para mantener su licencia.
- La rotación en los roles de recepción y administración es del 38% anual. Los datos de las entrevistas de salida existen en hilos de email y nunca se agregan.

**Necesidades de automatización e IA:**

- Rastreador del pipeline de contratación: vacantes abiertas, estado de los candidatos, fases de entrevista, tiempo de contratación por rol y centro — con alertas cuando una vacante supera los 30 días sin cubrir.
- Checklist de incorporación automatizada: para cada tipo de nuevo empleado (médico, enfermero, administrativo), una secuencia estructurada de tareas con recogida de documentación, provisión de accesos al sistema y seguimiento de finalización de formación obligatoria.
- Rastreador de CME y licencias: estado de la licencia de cada clínico, fecha de vencimiento, horas de CME registradas frente a las requeridas — recordatorio automático 90 y 30 días antes de los plazos.
- Dashboard de KPIs de personas: plantilla, tasa de vacantes, rotación, tiempo de contratación, absentismo — por centro y por país.
- Análisis de entrevistas de salida: entrevistas de salida digitales estructuradas con extracción automática de temas recurrentes y resumen mensual para Diane y la CEO.

---

### 💻 Tecnología

**Responsable:** James Osei, CTO (Austin)
**Equipo:** 6 personas (2 ingenieros, 1 ingeniero de datos, 1 DevOps, 1 QA, James)

**Situación actual:**

- El patrimonio tecnológico de HealthCore es un mosaico: un EHR estadounidense (heredado, sin API pública), un EHR del Reino Unido (proveedor distinto, API REST con documentación limitada), una plataforma de facturación en EE.UU., una hoja de cálculo de facturación en el Reino Unido, un sistema de programación telefónica en EE.UU. y una agenda manual en el Reino Unido.
- No existe una capa de datos centralizada. Cada sistema almacena sus propios datos y exporta CSVs a petición.
- El manejo de datos de pacientes en las integraciones está documentado de forma inconsistente. Algunas conexiones fueron construidas por consultores externos que ya no colaboran con la empresa, y no hay un mapa claro de qué datos fluyen por dónde — una responsabilidad de cumplimiento que Claire escala con regularidad.
- El despliegue de una nueva herramienta interna tarda entre 3 y 4 semanas debido a revisiones manuales de cumplimiento normativo que podrían estar al menos parcialmente automatizadas.
- James quiere construir una plataforma HealthCore unificada que sirva a ambos mercados, pero el 70% del tiempo del equipo se dedica a mantener los sistemas heredados.

**Necesidades de automatización e IA:**

- Plataforma de datos unificada: una capa de datos conforme con HIPAA y UK GDPR que ingiere eventos de todos los sistemas clínicos y operativos, los normaliza y los expone a través de una API interna única.
- Mapa de linaje de datos de pacientes: rastreo automatizado de dónde entran, por dónde se mueven y por dónde salen los datos de pacientes del sistema — consultable por el equipo de cumplimiento de Claire en cualquier momento.
- Pipeline de CI/CD con controles de cumplimiento: verificaciones automáticas de seguridad y cumplimiento integradas en el despliegue, reduciendo el tiempo de release sin incrementar el riesgo regulatorio.
- Dashboard de salud del sistema: disponibilidad, latencia de API, errores de integración — en todos los sistemas conectados y en ambos países.
- Agente de documentación técnica interna: responde preguntas del equipo de ingeniería sobre la arquitectura de la plataforma, los esquemas de datos y las especificaciones de integración a partir del código base y la documentación.

---

### 📊 Dirección Ejecutiva e Informes

**Responsable:** Dra. Sandra Okonkwo, CEO (Austin)
**Equipo directivo:** CTO, Director de Operaciones Clínicas, Responsable de Experiencia del Paciente, Director de Ciclo de Ingresos, Directora de Cumplimiento Normativo, VP de Personas

**Situación actual:**

- Sandra gestiona una red clínica de 12 centros en dos países sin una visión operativa unificada. Recibe informes semanales elaborados por cada responsable de departamento, con formatos distintos y a menudo contradictorios porque se nutren de sistemas fuente diferentes.
- No puede responder en tiempo real: "¿cuál es nuestra tasa de no-shows en toda la red esta semana?" o "¿qué clínica del Reino Unido tiene peores resultados en satisfacción del paciente?"
- Las presentaciones al consejo requieren una semana de consolidación de datos entre todo el equipo.
- Las decisiones estratégicas — como si abrir un 13º centro o qué línea de servicio expandir en el Reino Unido — se toman con datos incompletos y con retraso.

**Necesidades de automatización e IA:**

- Dashboard ejecutivo de operaciones: KPIs de toda la red en una sola vista — pacientes atendidos, ingresos cobrados, tasa de no-shows, puntuación de satisfacción, tasa de denegaciones, tasa de vacantes — actualizado diariamente y segmentado por país y por centro.
- Pack automatizado de informes para el consejo: el agente consolida datos de todos los departamentos, redacta el informe mensual del consejo y entrega un documento listo para revisión en el buzón de Sandra el primer día laborable de cada mes.
- Alertas estratégicas: si la tasa de no-shows de un centro supera el 25%, o si la tasa de denegación de facturación sube por encima del 10% en cualquier centro, notificación inmediata a Sandra y al responsable de departamento correspondiente.
- Asistente ejecutivo con IA: Sandra puede preguntar en lenguaje natural "¿cuáles son los tres centros de EE.UU. con peor cumplimiento del seguimiento de pacientes crónicos este trimestre?" y obtener una respuesta respaldada por datos con acciones recomendadas.

---

## Mapa de Milestones

| Milestone        | Departamento Principal                   | Entregable de Negocio                                                                         |
| ---------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------- |
| 0 — Prework      | Todos                                    | Configuración del entorno, primeros prompts e investigación sobre HealthCore                  |
| 1 — Web          | Experiencia del Paciente                 | Web corporativa bilingüe (EN/ES) orientada al paciente con información de servicios y centros |
| 2 — Programación | Ciclo de Ingresos / Operaciones Clínicas | Calculadora de tasa de denegaciones, estimador del coste de no-shows, lógica de CME           |
| 3 — UI con IA    | Cumplimiento / Formación                 | Interfaces generadas con IA para módulos de formación en cumplimiento y búsqueda de políticas |
| 4 — Next.js      | Experiencia del Paciente / Clínica       | Portal de reserva de citas para pacientes o dashboard clínico interno                        |
| 5 — Backend      | Todos                                    | API central de HealthCore: pacientes, citas, centros, personal, facturación                   |
| 6 — Telemetría   | Ciclo de Ingresos / Operaciones          | Pipeline de reclamaciones y dashboard de ingresos en tiempo real                             |
| 7 — RAG y Memoria| Clínica / Cumplimiento                   | Base de conocimiento semántica para políticas, procedimientos y protocolos clínicos           |
| 8 — Agentes      | Clínica / Experiencia del Paciente / Personas | Asistente de documentación, agente de derivaciones, agente de CME                      |
| 9 — Workflows    | Ciclo de Ingresos / Personas / Pac. Exp. | Automatizaciones n8n: recordatorios de no-shows, envío de reclamaciones, flujos de incorporación |
| 10 — Tiempo Real | Clínica / Dirección Ejecutiva            | Dashboard de KPIs en vivo, alertas de anomalías de cumplimiento, informe automático para el consejo |

---

## Personajes Recurrentes

| Personaje              | Rol                                  | Origen               | Género | Estilo de Comunicación                                                                                                                        |
| ---------------------- | ------------------------------------ | -------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dra. Sandra Okonkwo**| CEO                                  | Americana (nigeriana)| F      | Precisa y exigente. Piensa como clínica: basada en evidencia, con poca tolerancia a la ambigüedad. Envía emails estructurados con puntos numerados. |
| **Dr. Marcus Reid**    | Director de Operaciones Clínicas     | Americano            | M      | Protector del tiempo del personal clínico. Necesita ver el impacto en el paciente antes de aprobar cualquier sistema nuevo. Llama antes de escribir. |
| **Priya Nair**         | Responsable de Experiencia del Paciente | Británica (india) | F      | Empática y orientada a datos. Apasionada por la accesibilidad y la equidad en salud. Comunica de forma cálida pero precisa por Slack.         |
| **Tom Callahan**       | Director de Ciclo de Ingresos        | Americano            | M      | Los números son lo primero. Habla en porcentajes y cifras en dólares. Se impacienta con todo lo que no conecta directamente con los ingresos.  |
| **Claire Whitfield**   | Directora de Cumplimiento Normativo  | Británica            | F      | Metódica y adversa al riesgo. Cada petición recibe un "¿pero hemos revisado las implicaciones bajo HIPAA?" Hilos de email con listas detalladas de puntos. |
| **Diane Foster**       | VP de Personas                       | Americana            | F      | Primero las personas, operacionalmente eficaz. Equilibra empatía y proceso. Comparte documentos estructurados en Notion y valora la minuciosidad. |
| **James Osei**         | CTO                                  | Americano (ghanés)   | M      | Constructor. Pragmático y orientado a la arquitectura. Entrega tickets en Jira con criterios de aceptación claros y es directo sobre la deuda técnica. |

---

## Tono y Uso en los Proyectos

HealthCore debe aparecer en los enunciados de proyecto como **el empleador del estudiante dentro del equipo de HealthCore Digital**. Los proyectos llegan como:

- **Email de la Dra. Okonkwo (CEO)** con un problema de negocio claramente definido y urgencia implícita — raramente explica el porqué, espera que lo entiendas.
- **Ticket de Jira de James (CTO)** con requisitos técnicos, criterios de aceptación, restricciones de stack y notas sobre las limitaciones de los sistemas heredados.
- **Mensaje de Slack de Priya o Diane** describiendo un problema de experiencia de paciente o de empleado que necesita una solución técnica.
- **Memorándum formal de Claire (Cumplimiento)** con una preocupación regulatoria formulada como requisito de proyecto.

El estudiante siempre sabe que lo que construye **gestiona datos reales de pacientes, opera en un entorno regulado y será utilizado por personal clínico con cero tolerancia a las herramientas que hacen perder el tiempo**. No es un ejercicio descartable.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
_De uso exclusivo en la generación de proyectos del programa_
