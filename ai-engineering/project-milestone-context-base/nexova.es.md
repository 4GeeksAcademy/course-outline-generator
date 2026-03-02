# Nexova — Empresa del Proyecto Transversal

## AI Engineering · 4Geeks Academy

---

## Descripción general

**Nexova** es una empresa de consultoría de recursos humanos y selección de talento fundada en 2011, con sede en Santiago de Chile y una oficina comercial en Buenos Aires, Argentina. Cuenta con **120 empleados** y opera en tres líneas de negocio: headhunting para perfiles de mandos medios y directivos, outsourcing de equipos de soporte al cliente para empresas tecnológicas, y formación corporativa en habilidades blandas y liderazgo. Factura aproximadamente **8 millones de dólares anuales**.

Sus clientes son principalmente medianas empresas del sector tecnológico, retail y servicios financieros que externalizan parte de su gestión de talento. Nexova lleva años funcionando bien, pero siente la presión competitiva de nuevas plataformas de recruiting automatizadas que empiezan a quitarle cuota de mercado.

La CEO, **Laura Mendoza**, ha apostado por la IA como ventaja competitiva y ha formado un equipo de AI Engineering para liderar esa transformación. Tú eres parte de ese equipo.

---

## Mapa de departamentos y sus problemas reales

### 🌐 Marketing y Comunicación

**Responsable:** Carmen Ruiz, Head of Marketing
**Equipo:** 5 personas

**Situación actual:**

- Gestionan la presencia digital de Nexova: web corporativa, LinkedIn, newsletter mensual y blog.
- La web fue diseñada en 2019 y no se ha actualizado en profundidad. Es lenta, no es accesible y no refleja la imagen actual de la empresa.
- Producen contenido de forma manual: redactores escriben artículos del blog, diseñadores crean posts para redes sociales y un externo gestiona el SEO.
- No miden el impacto real del contenido: saben cuántas visitas reciben pero no de dónde vienen ni qué convierte.

**Necesidades de automatización e IA:**

- Rediseño completo del sitio web corporativo: accesible, optimizado para SEO/GEO y con schema.org.
- Pipeline de generación de contenido asistido por IA: briefing → borrador → revisión → publicación.
- Dashboard de métricas de marketing: visitas, fuentes de tráfico, tasa de conversión de formularios de contacto.
- Automatización del envío de newsletter segmentada por tipo de cliente.

---

### 💼 Ventas y Desarrollo de Negocio

**Responsable:** Megan Clarke, Head of Sales
**Equipo:** 18 personas (6 account managers, 12 SDRs)

**Situación actual:**

- Los SDRs prospectan manualmente en LinkedIn, exportan listas a Excel y hacen seguimiento por correo sin automatización.
- Tienen un CRM (HubSpot) pero solo el 40% del equipo lo actualiza de forma consistente.
- El ciclo de ventas dura entre 3 y 8 semanas. Muchos deals se pierden por falta de seguimiento.
- No hay visibilidad de qué clientes tienen mayor probabilidad de cerrar ni cuál es el estado real del pipeline.

**Necesidades de automatización e IA:**

- Integración del CRM con un agente que genere borradores de emails de seguimiento personalizados.
- Dashboard de pipeline de ventas: deals por etapa, forecast del mes, actividad del equipo.
- Automatización de secuencias de prospección: primer contacto → seguimiento 1 → seguimiento 2 → cierre o descarte.
- Sistema de alertas para deals sin actividad en más de X días.
- Agente de IA que, dado el perfil de un prospecto, sugiera el enfoque de propuesta más adecuado.

---

### 🧑‍🤝‍🧑 Recursos Humanos (interno)

**Responsable:** Patricia Solís, HR Manager
**Equipo:** 4 personas

**Situación actual:**

- Gestión de vacaciones, ausencias y solicitudes de RRHH por correo y hojas de cálculo.
- El onboarding de nuevos empleados es manual: Patricia envía un PDF con instrucciones y hace seguimiento por Slack.
- Las evaluaciones de desempeño se realizan dos veces al año en formularios de Google que nadie revisa de forma sistemática.
- No hay visibilidad de indicadores clave: rotación, absentismo, tiempo medio de contratación interna.

**Necesidades de automatización e IA:**

- Portal interno de RRHH: solicitudes de vacaciones, consulta de nóminas, gestión de ausencias.
- Flujo de onboarding automatizado: checklist progresivo, asignación de materiales, validación de pasos completados.
- Dashboard de KPIs de RRHH: headcount, rotación mensual, tiempo medio de cobertura de vacantes internas.
- Agente de RRHH interno que responda preguntas frecuentes del equipo sobre políticas, beneficios y procedimientos.

---

### 🔍 Operaciones de Selección (core business)

**Responsable:** Javier Almeida, Operations Manager
**Equipo:** 40 consultores de selección

**Situación actual:**

- Los consultores reciben briefings de vacantes por correo y los introducen manualmente en su ATS propietario, que es antiguo y lento.
- El proceso de criba de CVs es manual: cada consultor lee entre 30 y 80 CVs por proceso.
- La comunicación con candidatos se hace por correo individual, sin plantillas automatizadas.
- No existe un sistema para saber en qué estado está cada candidato en tiempo real. Los clientes llaman para preguntar.
- El matching entre candidato y vacante se hace por intuición y experiencia del consultor.

**Necesidades de automatización e IA:**

- Pipeline de selección asistido por IA: ingesta de CV → extracción de datos → scoring automático → ranking.
- Sistema RAG sobre la base de datos de candidatos: "busca perfiles con experiencia en ventas B2B y nivel de inglés C1".
- Portal de candidatos: estado del proceso en tiempo real, documentos subidos, entrevistas agendadas.
- Agente de comunicación: envío automático de emails de estado.
- Dashboard de operaciones de selección: vacantes activas, candidatos por etapa, tiempo medio de cobertura.

---

### 🎓 Formación Corporativa

**Responsable:** Elena Vargas, Learning & Development Manager
**Equipo:** 12 personas

**Situación actual:**

- El catálogo de formación vive en un PDF actualizado trimestralmente.
- Las inscripciones se hacen por formulario de Google y se gestionan manualmente en una hoja de cálculo.
- El seguimiento de quién completó qué formación es inexistente más allá de listas de asistencia en Excel.
- La personalización es nula: todos los clientes reciben la misma propuesta de catálogo.

**Necesidades de automatización e IA:**

- Plataforma de catálogo de formación: búsqueda, filtrado por área o nivel, inscripción en línea.
- Sistema de recomendación: dado el perfil del cliente y sus objetivos, sugerir los programas más relevantes.
- Portal del alumno: mis inscripciones, progreso, certificados.
- Agente de asesoramiento formativo: chatbot que propone un plan de formación a partir de las necesidades del cliente.
- Dashboard de L&D: inscripciones por programa, tasa de completitud, NPS de cada curso.

---

### 📞 Soporte al Cliente (servicio externalizado)

**Responsable:** Roberto Díaz, Customer Support Lead
**Equipo:** 30 agentes

**Situación actual:**

- Los 30 agentes atienden incidencias de los clientes de Nexova por teléfono, email y chat web, usando un helpdesk antiguo.
- No hay base de conocimiento centralizada: cada agente resuelve basándose en su experiencia y un documento de Word compartido.
- El tiempo medio de resolución es de 48 horas para tickets no urgentes. El SLA comprometido es de 24 horas.
- Los supervisores no tienen visibilidad en tiempo real de la carga de trabajo ni del estado del backlog.

**Necesidades de automatización e IA:**

- Agente de soporte de primera línea: chatbot que resuelve el 40% de las consultas sin intervención humana usando RAG.
- Base de conocimiento centralizada con búsqueda semántica.
- Dashboard de soporte en tiempo real: tickets abiertos, tiempo medio de respuesta, backlog por agente, SLA en riesgo.
- Sistema de escalado automático: si un ticket lleva más de X horas sin respuesta, reasignarlo y notificar al supervisor.
- Análisis de sentimiento de tickets: identificar clientes insatisfechos antes de que escalen.

---

### 💻 Tecnología e Infraestructura

**Responsable:** Sergio Molina, CTO
**Equipo:** 6 personas (2 desarrolladores, 2 sysadmins, 1 QA, Sergio)

**Situación actual:**

- La infraestructura tecnológica es un patchwork de herramientas desconectadas: HubSpot, Zendesk legacy, Google Workspace, un ATS propio de los años 2010 y múltiples hojas de cálculo.
- No existe telemetría ni logging centralizado. Cuando algo falla, el equipo se entera por los usuarios.
- Los despliegues son manuales. No hay CI/CD.
- Sergio quiere construir una plataforma unificada pero no tiene equipo suficiente.

**Necesidades de automatización e IA:**

- Telemetría centralizada: logs de errores, eventos del sistema, alertas automáticas.
- Pipeline de datos: capturar eventos de todas las aplicaciones → transformar → agregar → alimentar dashboards.
- Sistema de monitorización: uptime, latencia de endpoints, errores 5xx en tiempo real.
- Agente de ingeniería interna: responde preguntas sobre la arquitectura consultando documentación técnica (RAG sobre docs).
- Automatización de tareas repetitivas de ops: backups, rotación de logs, notificaciones de incidencias.

---

### 📊 Dirección y Reporting Ejecutivo

**Responsable:** Laura Mendoza, CEO + equipo directivo

**Situación actual:**

- Laura recibe un informe semanal en PDF preparado manualmente por los responsables de cada área. El proceso toma entre 4 y 8 horas del tiempo de cada manager.
- No hay una vista unificada del estado del negocio. Para saber cuántos procesos de selección están activos, Laura llama a Javier. Para saber si ventas va bien, llama a Megan.
- Las decisiones estratégicas se toman con datos de la semana anterior, no en tiempo real.

**Necesidades de automatización e IA:**

- Dashboard ejecutivo unificado: KPIs de todas las áreas en un solo lugar, actualizado en tiempo real.
- Informe ejecutivo generado automáticamente: el agente consolida los datos, redacta el informe y lo envía cada lunes a las 8h.
- Alertas estratégicas: si algún KPI cae por debajo de un umbral, notificar a la dirección de inmediato.
- Asistente ejecutivo de IA: Laura puede preguntar en lenguaje natural y obtener respuestas con datos.

---

## Resumen de necesidades por hito del curso

| Hito              | Departamento principal  | Entregable de negocio                                                      |
| ----------------- | ----------------------- | -------------------------------------------------------------------------- |
| 0 — Prework       | Todos                   | Configuración del entorno, primeros prompts sobre Nexova                   |
| 1 — Web           | Marketing               | Web corporativa de Nexova                                                  |
| 2 — Programación  | Operaciones / RRHH      | Lógica de scoring de CVs, cálculo de KPIs básicos                          |
| 3 — UI con IA     | Formación / Candidatos  | Interfaces generadas con IA para portales internos                         |
| 4 — Next.js       | Selección / Ventas      | Frontend interactivo del ATS o el portal de ventas                         |
| 5 — Backend       | Todos                   | API de Nexova: endpoints para candidatos, vacantes, clientes               |
| 6 — Telemetría    | Tecnología / Dirección  | Pipeline de datos y dashboard ejecutivo                                    |
| 7 — RAG y Memoria | Soporte / Selección     | Base de conocimiento semántica; búsqueda de candidatos                     |
| 8 — Agentes       | Soporte / RRHH / Ventas | Agentes de primera línea: soporte, onboarding, prospección                 |
| 9 — Workflows     | Operaciones / Marketing | Automatizaciones n8n: pipeline de selección, newsletter, informe ejecutivo |
| 10 — Tiempo real  | Soporte / Dirección     | Dashboard de soporte en vivo, notificaciones push, streaming de eventos    |

---

## Personajes recurrentes del proyecto

| Personaje          | Rol                   | Origen                    | Género | Estilo de comunicación                                                                                        |
| ------------------ | --------------------- | ------------------------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| **Laura Mendoza**  | CEO                   | Chilena (Latinoamérica)   | M      | Directa, orientada a resultados. Comunica por email con ideas de alto nivel. Poco técnica.                    |
| **Javier Almeida** | Operations Manager    | Chileno (Latinoamérica)   | H      | Pragmático. Describe los problemas con mucho detalle operativo. Poco paciente con la tecnología.              |
| **Elena Vargas**   | L&D Manager           | Argentina (Latinoamérica) | M      | Creativa, detallista. Quiere que los alumnos tengan la mejor experiencia posible.                             |
| **Megan Clarke**   | Head of Sales         | Estadounidense            | M      | Impaciente, orientada a números. Quiere resultados rápidos y dashboards claros. Mensajes cortos y directos.   |
| **Tom Reeves**     | Senior Sales Analyst  | Estadounidense            | H      | Metódico y con cultura de datos. Siempre quiere los números de fondo, no el resumen.                          |
| **Sergio Molina**  | CTO                   | Español                   | H      | Técnico, meticuloso. Entrega specs detalladas. Valora la escalabilidad y la seguridad.                        |
| **Carmen Ruiz**    | Head of Marketing     | Española                  | M      | Orientada a marca y experiencia. Sabe lo que quiere visualmente pero no cómo construirlo.                     |
| **Roberto Díaz**   | Customer Support Lead | Otro (dominicano-chileno) | H      | Bajo presión constante. Necesita visibilidad en tiempo real y herramientas que su equipo adopte sin fricción. |

---

## Tono y uso en los proyectos

Nexova debe aparecer en los enunciados como **el cliente o el empleador** del estudiante, nunca como un ejemplo académico. Los proyectos se enmarcan siempre desde uno de estos ángulos:

- **Email de un directivo** con una solicitud concreta y un plazo.
- **Spec de Sergio (CTO)** con requisitos técnicos detallados.
- **Reunión de kickoff** en la que el equipo recibe el encargo del proyecto transversal.
- **Ticket de Jira o Notion** asignado por el tech lead.

El estudiante siempre sabe que lo que construye **va a producción en Nexova**, no es un ejercicio desechable.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
_Uso exclusivo para la generación de proyectos del programa_
