# Brasaland — Empresa del Proyecto Transversal

## AI Engineering · 4Geeks Academy

---

## Descripción general

**Brasaland** es una cadena de restaurantes de cocina a la brasa fundada en 2008 en Medellín, Colombia. Lo que empezó como un único local familiar se convirtió en una cadena de **14 restaurantes propios** que opera en Colombia y Estados Unidos (Florida). La empresa emplea a unas **115 personas** entre el personal de sala y cocina, los equipos de supervisión operativa y la sede corporativa en Medellín, con una oficina comercial en Miami. La facturación anual ronda los **6 millones de dólares**.

La marca se construye sobre tres pilares: calidad de producto consistente en todos los locales, una experiencia del cliente cálida y fiable, y velocidad de servicio. El reto es que mantener esos tres pilares en dos mercados tan distintos —Colombia y Florida— se hace cada vez más difícil sin tecnología adecuada. Los competidores ganan clientes con programas de fidelización digitales, visibilidad en tiempo real de sus operaciones y decisiones basadas en datos. Brasaland sigue gestionando la mayor parte de esto por instinto y hoja de cálculo.

La CEO, **Mariana Restrepo**, hija del fundador, ha creado un equipo interno llamado **Brasaland Digital** para liderar la transformación de la empresa. Conoce el negocio en profundidad y tiene una visión clara de hacia dónde quiere llevarlo. Solo necesita que el equipo técnico construya las herramientas que la lleven hasta allí. Tú eres parte de ese equipo.

---

## Mapa de departamentos y sus problemas reales

### 🍖 Operaciones de Restaurante

**Responsable:** Felipe Guerrero, Director de Operaciones
**Equipo:** 4 supervisores operativos + ~85 personas de sala y cocina repartidas en 14 locales

**Situación actual:**

- Cada local tiene un manager que gestiona el día a día: turnos del personal, apertura y cierre de caja, pedidos de materia prima al proveedor y control de mermas.
- No existe visibilidad centralizada. Felipe no sabe cuántos cubiertos se han servido hoy en el local del centro de Medellín ni si el de Miami está teniendo una semana floja.
- Los pedidos de materia prima se hacen por WhatsApp o llamada. Cada manager pide lo que cree que necesita. Resultado: sobrestock en unos locales y roturas de stock en otros.
- El control de mermas es manual e inconsistente. Los partes de turno se rellenan en papel o Excel.
- Operar en Colombia y Florida implica dos monedas (COP y USD), dos idiomas (español e inglés) y dos entornos regulatorios muy distintos — sin ningún sistema para gestionar ninguno de ellos.

**Necesidades de automatización e IA:**

- Dashboard de operaciones en tiempo real: ventas del día por local, cubiertos, ticket medio, comparativa vs. mismo día semana anterior — en ambas monedas.
- Sistema de pedidos de materia prima: basado en ventas históricas y stock disponible, el sistema genera el pedido sugerido automáticamente.
- Control de mermas digitalizado: el manager registra las mermas en una app, el sistema detecta anomalías y alerta a operaciones.
- Alertas operativas: si un local lleva dos horas sin ventas en horario de apertura, notificación automática a Felipe.
- Agente de soporte al manager: responde preguntas operativas frecuentes en español o inglés según el local.

---

### 🛒 Compras y Proveedores

**Responsable:** Lucía Fernández, Procurement Manager
**Equipo:** 3 personas

**Situación actual:**

- Brasaland trabaja con unos 20 proveedores entre Colombia y Florida: carnes, vegetales, salsas, bebidas, embalajes y productos de limpieza, con proveedores distintos en cada país.
- La negociación se hace por email y Excel. No hay sistema de gestión de contratos.
- Los precios de las materias primas clave fluctúan de forma distinta en cada mercado. Lucía se entera cuando llega la factura.
- No hay datos consolidados de compras a nivel de cadena. Colombia y Florida negocian de forma independiente.
- El proceso de aprobación de un nuevo proveedor es lento: formularios en papel, validaciones manuales, sin trazabilidad.

**Necesidades de automatización e IA:**

- Plataforma de gestión de proveedores: ficha de cada proveedor, contratos, historial de precios, evaluaciones de calidad — segmentada por país.
- Alertas de variación de precio: cuando sube un ingrediente clave en cualquiera de los dos mercados, notificación inmediata a Lucía y a la CEO.
- Consolidación de compras: visibilidad del volumen total por ingrediente a nivel de cadena, para identificar oportunidades de negociación centralizada.
- Proceso de homologación de proveedores automatizado: formulario digital → validación → aprobación → alta en sistema.
- Agente de análisis de compras: "¿cuánto hemos gastado en carne este trimestre en Florida comparado con Colombia?"

---

### 📱 Marketing, Marca y Experiencia Digital

**Responsable:** Camila Ospina, Marketing Manager
**Equipo:** 4 personas + apoyo freelance

**Situación actual:**

- La web de Brasaland es de 2019, no permite pedidos online y solo muestra el menú. Valoración de 2,8 en las tiendas de apps.
- El programa de fidelización ("Brasa Points") funciona con tarjetas físicas de sello. Se pierden, no generan datos y el 60% de los clientes no las usa.
- Las campañas se producen en Medellín y se adaptan manualmente al mercado de Florida, con frecuencia tarde.
- Las redes sociales se gestionan desde cada oficina con criterios distintos. La percepción de marca es inconsistente entre los dos países.
- No hay ningún dato sobre quiénes son los clientes de Brasaland.

**Necesidades de automatización e IA:**

- App de pedidos y fidelización digital: pedido online, pago, puntos digitales, historial de visitas — bilingüe (español/inglés).
- CRM de clientes: perfil unificado con historial de pedidos, frecuencia de visita, preferencias y puntos acumulados.
- Motor de personalización: sugerir productos u ofertas basadas en el historial del cliente.
- Dashboard de marketing: CAC, LTV, frecuencia media de visita, conversión de campañas, evolución de Brasa Points — por mercado.
- Pipeline de contenido asistido por IA: briefing → generación de copy adaptado a cada mercado e idioma → revisión → publicación.
- Automatización de comunicaciones: emails y push notifications segmentados por comportamiento e idioma.

---

### 🧑‍🤝‍🧑 Personas y Cultura

**Responsable:** Ashley Turner, People Manager (Miami)
**Equipo:** 3 personas

**Situación actual:**

- Gestionar 115 personas en 14 locales de dos países con legislaciones laborales muy distintas implica una gran carga administrativa.
- La mayoría de los procesos de RRHH funcionan por email y Excel. No hay ningún sistema de información de RRHH.
- El onboarding de personal nuevo —especialmente de cocina, con alta rotación— es manual.
- No hay visibilidad de indicadores clave: rotación por local, absentismo, tiempo medio de contratación.
- La legislación laboral de Colombia y EE.UU. difiere sustancialmente. Gestionarlas sin sistema es arriesgado.

**Necesidades de automatización e IA:**

- Portal interno de RRHH: solicitudes de vacaciones, consulta de contratos, gestión de ausencias — bilingüe.
- Flujo de onboarding automatizado: checklist, envío de documentos, seguimiento de pasos completados.
- Dashboard de KPIs de RRHH: headcount por local, rotación mensual, absentismo, tiempo de cobertura — por país.
- Agente interno de RRHH: responde preguntas del equipo sobre políticas, horarios y beneficios en español o inglés.

---

### 🎓 Formación y Estándares de Calidad

**Responsable:** Jake Morrison, Head of Training (Miami)
**Equipo:** 3 personas

**Situación actual:**

- Todos los locales deben seguir las mismas recetas, técnicas de preparación y estándares de presentación independientemente del país.
- Los materiales de formación viven en un Google Drive compartido que nadie sabe navegar bien.
- El personal nuevo recibe un manual impreso y dos días de shadowing. Después van solos.
- No hay ningún sistema para verificar que se cumplen los estándares entre visitas a los locales.
- Cuando cambia una receta o procedimiento, comunicar la actualización en dos idiomas a 14 locales lleva días y genera confusión.

**Necesidades de automatización e IA:**

- Plataforma de formación: catálogo con buscador de recetas, guías de técnica y estándares de calidad — en español e inglés.
- Manual de procedimientos digital: siempre actualizado, accesible desde cualquier dispositivo en cocina.
- Flujo de onboarding del personal nuevo: itinerario de aprendizaje estructurado con checkpoints.
- Sistema de actualización de estándares: cuando cambia una receta, todos los locales reciben la notificación inmediata en ambos idiomas.
- Agente de soporte de formación: el personal puede preguntar en español o inglés y obtener la respuesta oficial al momento.

---

### 💻 Tecnología

**Responsable:** Nicolás Park, CTO (Medellín)
**Equipo:** 4 personas (2 desarrolladores, 1 sysadmin, Nicolás)

**Situación actual:**

- La infraestructura tecnológica de Brasaland es mínima: web estática, app obsoleta, TPV distinto en cada país sin integración, y hojas de cálculo como sistemas de gestión.
- No hay API propia. No hay datos consolidados. No hay telemetría.
- Nicolás tiene el mandato de construir la plataforma digital desde casi cero, con equipo pequeño y presupuesto ajustado.
- Todo lo que se construya debe funcionar igual de bien en Colombia y en Florida.

**Necesidades de automatización e IA:**

- API central de Brasaland: endpoints para locales, menús, ventas, clientes, proveedores y personal.
- Telemetría: eventos de cada local capturados y procesados en tiempo real.
- Pipeline de datos: TPV → API → transformación → dashboards de operaciones, marketing y finanzas.
- Monitorización: uptime, errores, latencia, alertas automáticas al equipo.
- Agente de soporte técnico interno: responde preguntas del equipo sobre arquitectura, APIs y despliegue.

---

### 📊 Dirección y Reporting Ejecutivo

**Responsable:** Mariana Restrepo, CEO (Medellín)

**Situación actual:**

- Mariana gestiona una cadena de 14 locales en dos mercados muy distintos sin un cuadro de mando unificado. Decide basándose en llamadas, informes en PDF del martes y sensaciones del mercado.
- No puede responder en tiempo real: "¿cuánto hemos vendido esta semana en Florida?" o "¿qué local tiene el ticket medio más alto este mes?"
- Los inversores y socios piden presentaciones trimestrales que el equipo prepara manualmente durante una semana.

**Necesidades de automatización e IA:**

- Dashboard ejecutivo: ventas totales en USD y COP, desglose por país y local, comparativa vs. periodo anterior, top y bottom performers.
- Informe semanal automatizado: el agente consolida datos, redacta el informe en español y lo envía cada lunes a las 7h.
- Asistente ejecutivo de IA: Mariana puede preguntar en lenguaje natural y obtener respuestas con datos y contexto.
- Alertas estratégicas: si las ventas de un país caen más del 15% vs. la semana anterior, notificación inmediata a Mariana y Felipe.

---

## Resumen de necesidades por hito del curso

| Hito              | Departamento principal         | Entregable de negocio                                                                |
| ----------------- | ------------------------------ | ------------------------------------------------------------------------------------ |
| 0 — Prework       | Todos                          | Configuración del entorno, primeros prompts sobre Brasaland                          |
| 1 — Web           | Marketing                      | Web corporativa bilingüe renovada                                                    |
| 2 — Programación  | Finanzas / Operaciones         | Lógica de márgenes, scoring de locales, control de mermas                            |
| 3 — UI con IA     | Formación / Producto           | Interfaces generadas con IA para la plataforma de formación y el catálogo de fichas  |
| 4 — Next.js       | Marketing / Clientes           | App de fidelización o portal operativo para el personal                              |
| 5 — Backend       | Todos                          | API central de Brasaland: locales, menús, ventas, clientes                           |
| 6 — Telemetría    | Operaciones / Finanzas         | Pipeline de ventas por TPV y dashboard financiero en tiempo real                     |
| 7 — RAG y Memoria | Formación / CX                 | Base de conocimiento semántica de recetas, estándares y procedimientos               |
| 8 — Agentes       | Operaciones / RRHH / Formación | Agente de soporte al manager, agente de onboarding, asistente de formación           |
| 9 — Workflows     | Compras / Finanzas / Marketing | Automatizaciones n8n: pedidos de materia prima, cierre mensual, campañas segmentadas |
| 10 — Tiempo real  | Operaciones / Dirección        | Dashboard de ventas en vivo por local, alertas, informe ejecutivo automático         |

---

## Personajes recurrentes del proyecto

| Personaje            | Rol                              | Origen                     | Género | Estilo de comunicación                                                                                                  |
| -------------------- | -------------------------------- | -------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Mariana Restrepo** | CEO                              | Colombiana (Latinoamérica) | M      | Visionaria e impaciente. Mensajes de voz o mensajes cortos. Quiere resultados visibles rápido.                          |
| **Felipe Guerrero**  | Director de Operaciones          | Colombiano (Latinoamérica) | H      | Operativo y directo. Piensa en procesos físicos. Sus emails son listas de puntos sin adornos.                           |
| **Camila Ospina**    | Marketing Manager                | Colombiana (Latinoamérica) | M      | Creativa y orientada al cliente. Quiere que todo sea bonito y fácil de usar. Muy activa en Slack.                       |
| **Ashley Turner**    | People Manager                   | Estadounidense             | M      | Estructurada y orientada al cumplimiento normativo. Piensa en procesos y marcos legales. Emails claros y profesionales. |
| **Jake Morrison**    | Head of Training                 | Estadounidense             | H      | Perfeccionista con la consistencia. Desconfía de la tecnología hasta que la ve funcionar.                               |
| **Lucía Fernández**  | Procurement Manager              | Española                   | M      | Analítica y metódica. Habla en números y porcentajes. Muy precisa en sus requisitos.                                    |
| **Carlos Jiménez**   | Supervisor Senior de Operaciones | Español                    | H      | Experimentado, tranquilo bajo presión. Sus informes son minuciosos y bien estructurados.                                |
| **Nicolás Park**     | CTO                              | Otro (coreano-colombiano)  | H      | Pragmático y minimalista. Prefiere hacer poco y bien. Entrega specs en Notion con criterios de aceptación claros.       |

---

## Tono y uso en los proyectos

Brasaland debe aparecer en los enunciados como **el empleador del estudiante dentro del equipo Brasaland Digital**. Los proyectos llegan como:

- **Mensaje de voz transcrito de Mariana (CEO)** con una idea urgente y poco definida que el estudiante debe convertir en spec.
- **Notion de Nicolás (CTO)** con requisitos técnicos, criterios de aceptación y restricciones de stack.
- **Email de un responsable de área** (Felipe, Camila, Ashley, Jake, Lucía) describiendo su problema con detalle operativo.
- **Ticket asignado** por el tech lead.

El estudiante siempre sabe que lo que construye **va a ser usado mañana por los managers de 14 locales en Colombia y Florida** — no es un ejercicio desechable.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
_Uso exclusivo para la generación de proyectos del programa_
