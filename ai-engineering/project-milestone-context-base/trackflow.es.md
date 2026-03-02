# TrackFlow — Empresa del Proyecto Transversal

## AI Engineering · 4Geeks Academy

---

## Descripción general

**TrackFlow** es una empresa de logística de última milla y gestión de almacenes fundada en 2009 en Monterrey, México. Opera en dos mercados — **México y España (Zaragoza)** — y ofrece tres servicios: gestión de almacenes para marcas de e-commerce que venden en ambos países, transporte de última milla (la última vuelta desde el almacén al cliente final) y logística inversa (devoluciones y reacondicionamiento de producto). Cuenta con unos **130 empleados** y factura alrededor de **9 millones de euros anuales**.

Sus clientes son marcas de moda, electrónica y cosmética de tamaño medio que venden online y externalizan en TrackFlow toda su operación logística. La empresa creció de forma constante durante el auge del e-commerce, pero ese crecimiento dejó una base tecnológica desigual: las operaciones de Monterrey y Zaragoza usan herramientas distintas, los datos no fluyen entre los dos países y el equipo directivo toma decisiones con información que llega tarde e incompleta. Los márgenes están bajo presión porque los competidores están automatizando lo que TrackFlow aún hace a mano.

El CEO, **Daniel Espinoza**, ha creado una unidad interna llamada **TrackFlow Tech** para liderar la transformación digital de la empresa. Tú formas parte de esa unidad.

---

## Mapa de departamentos y sus problemas reales

### 🚚 Operaciones de Almacén

**Responsable:** Ana Whitfield, Head of Warehouse Operations
**Equipo:** ~70 operarios de almacén + 2 managers de almacén (uno por país)

**Situación actual:**

- El almacén de Monterrey y el de Zaragoza usan sistemas de gestión de almacén (WMS) distintos. Uno es software comercial; el otro es una hoja de cálculo avanzada.
- El inventario en tiempo real no existe a nivel global. Para saber cuántas unidades de un producto hay disponibles en los dos países, alguien tiene que llamar a los dos almacenes.
- Las órdenes de entrada llegan por email en formatos distintos según el cliente. Un operario las transcribe al sistema local manualmente.
- El picking se hace con listas impresas en papel. Las discrepancias de inventario son frecuentes y se detectan tarde.

**Necesidades de automatización e IA:**

- API unificada de inventario: un endpoint que devuelva el stock en tiempo real de cualquier SKU en cualquiera de los dos almacenes.
- Pipeline de ingesta de órdenes: email → parser con IA → validación → inserción en sistema.
- Dashboard de operaciones de almacén: órdenes pendientes, órdenes procesadas, discrepancias de inventario, productividad por almacén.
- Alertas de stock bajo: cuando un SKU baja del umbral mínimo, notificación automática al cliente y al equipo de compras.
- Sistema de auditoría de inventario: detectar patrones de discrepancia y predecir dónde es más probable que ocurran.

---

### 📦 Última Milla y Gestión de Transportistas

**Responsable:** Carlos Vega, Head of Carrier Operations
**Equipo:** 6 coordinadores logísticos

**Situación actual:**

- TrackFlow trabaja con 8 transportistas: Estafeta, FedEx y DHL en México; MRW, SEUR y DHL en España, más dos carriers locales.
- La asignación de transportista para cada envío se hace manualmente por experiencia del coordinador.
- El tracking de los paquetes es inconsistente: cada transportista tiene su propio portal. El equipo tiene que consultar varios sistemas para responder al cliente.
- Las incidencias llegan por email sin ningún sistema de gestión de tickets.
- No hay datos históricos sobre el rendimiento de cada transportista.

**Necesidades de automatización e IA:**

- Motor de selección de transportista: dado el destino, el peso, el tipo de producto y la urgencia, el sistema recomienda automáticamente el carrier óptimo.
- Tracking unificado: un solo endpoint que agrega el estado del paquete desde cualquier transportista.
- Portal de tracking para el cliente final: URL pública donde el destinatario consulta el estado de su pedido en tiempo real.
- Dashboard de rendimiento de carriers: tasa de éxito, tiempo medio de entrega, coste por ruta, incidencias.
- Agente de gestión de incidencias: cuando llega una incidencia, el agente la clasifica, abre un ticket y propone la acción correctiva.

---

### 🔄 Logística Inversa

**Responsable:** Sofía Ramos, Returns Manager
**Equipo:** 5 personas

**Situación actual:**

- Las devoluciones representan entre el 18% y el 25% del volumen según el cliente y el país.
- Proceso actual: el cliente final solicita la devolución → el equipo de Sofía revisa manualmente → aprueba o rechaza → coordina la recogida → el producto llega al almacén → un operario lo inspecciona y clasifica.
- No hay criterios automáticos de aprobación: todo pasa por revisión humana.
- La inspección del producto devuelto es subjetiva e inconsistente entre operarios.
- No hay visibilidad de qué productos se devuelven más ni por qué.

**Necesidades de automatización e IA:**

- Motor de aprobación automática: reglas configurables por cliente que resuelven el 70% de los casos sin intervención humana.
- Flujo automatizado de recogida: aprobación → generación de etiqueta → instrucciones al cliente → scheduling con transportista.
- Sistema de inspección asistida: el operario fotografía el producto devuelto → la IA clasifica su estado.
- Dashboard de devoluciones: volumen por país, motivo más frecuente, tasa de reacondicionamiento, coste por devolución.
- Análisis de patrones: identificar productos o rutas con tasas de devolución anómalas y alertar al equipo comercial.

---

### 📞 Atención al Cliente

**Responsable:** Valentina Cruz, CX Manager
**Equipo:** 15 agentes distribuidos entre Monterrey y Zaragoza

**Situación actual:**

- TrackFlow tiene dos tipos de clientes: las marcas (B2B) y los consumidores finales (B2C).
- Los 15 agentes atienden ambos tipos a través de email, WhatsApp y teléfono, sin ticketing unificado.
- El 80% de las consultas ("¿dónde está mi paquete?", "quiero hacer una devolución", "hay un error en mi pedido") podrían responderse automáticamente.
- No hay base de conocimiento. Las respuestas son inconsistentes. La cobertura fuera del horario de oficina es nula.

**Necesidades de automatización e IA:**

- Agente de CX de primera línea: chatbot bilingüe (español + inglés) que resuelve automáticamente tracking, estado de devoluciones y preguntas frecuentes.
- Base de conocimiento semántica: políticas de devolución, SLAs por país, procedimientos de incidencias — indexada para RAG.
- Sistema de ticketing unificado: todos los canales en un solo lugar con priorización automática.
- Dashboard de CX en tiempo real: tickets abiertos, tiempo medio de respuesta, CSAT, backlog por agente y por país.
- Análisis de sentimiento: detectar clientes frustrados antes de que escalen y asignarlos a un agente senior.

---

### 🤝 Comercial y Relación con Clientes

**Responsable:** Miguel Torres, Director Comercial
**Equipo:** 8 personas (4 account managers, 4 business development)

**Situación actual:**

- Los clientes de TrackFlow son marcas de tamaño medio con contratos anuales. La renovación es el principal evento comercial del año.
- Los account managers hacen el seguimiento en hojas de cálculo personales e hilos de email. No hay CRM.
- El reporting al cliente es manual: cada mes, un account manager consolida datos para enviar un informe en PDF.
- No hay visibilidad de qué clientes tienen riesgo de no renovar ni cuáles justifican un upsell.

**Necesidades de automatización e IA:**

- Integración con CRM: perfil unificado de cada cliente con historial de contratos, volumen de envíos, incidencias y fecha de renovación.
- Informe automático al cliente: el agente consolida los datos del mes y genera el PDF automáticamente.
- Dashboard de salud del cliente: tendencia de volumen, tasa de incidencias, puntuación de riesgo de renovación, oportunidades de upsell.
- Sistema de alertas de renovación: 90 y 30 días antes del vencimiento, notificación automática al account manager.
- Agente comercial: dado el perfil de un prospecto y su sector, sugiere el servicio y la estructura de precios más adecuados.

---

### 💻 Tecnología

**Responsable:** Andrés Kim, CTO (Zaragoza)
**Equipo:** 7 personas (3 desarrolladores, 2 data engineers, 1 sysadmin, Andrés)

**Situación actual:**

- La arquitectura tecnológica de TrackFlow es el resultado de años de crecimiento no planificado: dos WMS distintos, un ERP de principios de los 2010, integraciones punto a punto con scripts Python sin documentar y bases de datos en dos proveedores cloud distintos.
- No hay telemetría centralizada. Cuando falla un endpoint en Monterrey, el equipo de Zaragoza se entera por WhatsApp.
- El tiempo de despliegue de una nueva feature es de una a dos semanas. No hay CI/CD.

**Necesidades de automatización e IA:**

- Telemetría centralizada: logs, métricas y eventos de todos los sistemas y los dos países en un solo lugar.
- Pipeline de datos: capturar eventos operativos → transformar → agregar → alimentar todos los dashboards de la empresa.
- Monitorización en tiempo real: uptime, latencia de endpoints, errores 5xx, alertas automáticas al equipo.
- Agente de documentación técnica: genera y mantiene actualizada la documentación de los endpoints.
- Automatización de ops: backups, rotación de logs, health checks, notificaciones de incidencias con contexto.

---

### 📊 Dirección y Reporting Ejecutivo

**Responsable:** Daniel Espinoza, CEO (Monterrey)

**Situación actual:**

- Daniel recibe cada lunes un informe consolidado que sus directores preparan juntando datos de distintos sistemas. El proceso consume entre 3 y 4 horas por director.
- El informe llega a las 10h del lunes con datos ya envejecidos. No hay vista unificada por país.
- Las decisiones estratégicas se toman con datos parciales.

**Necesidades de automatización e IA:**

- Dashboard ejecutivo global: KPIs de las dos operaciones en tiempo real — volumen de envíos, tasa de entrega a tiempo, coste operativo, devoluciones, satisfacción del cliente.
- Informe ejecutivo semanal generado automáticamente: el agente consolida los datos y lo envía cada lunes a las 7h.
- Comparativas por país y periodo: Daniel puede explorar "cómo fue el Q3 en México vs. España" sin llamar a nadie.
- Alertas estratégicas: si el SLA de entrega cae por debajo del 90% en alguno de los dos países, notificación inmediata a Daniel y a Ana.
- Asistente ejecutivo de IA: Daniel puede preguntar en lenguaje natural y obtener respuestas con datos del sistema.

---

## Resumen de necesidades por hito del curso

| Hito              | Departamento principal   | Entregable de negocio                                                           |
| ----------------- | ------------------------ | ------------------------------------------------------------------------------- |
| 0 — Prework       | Todos                    | Configuración del entorno, primeros prompts sobre TrackFlow                     |
| 1 — Web           | Comercial / CX           | Web corporativa de TrackFlow y portal público de tracking                       |
| 2 — Programación  | Almacén / Última milla   | Lógica de scoring de carriers, cálculo de tarifas, gestión de inventario        |
| 3 — UI con IA     | Devoluciones / CX        | Interfaces generadas con IA para portales de devoluciones y cliente             |
| 4 — Next.js       | Comercial / Almacén      | Portal B2B de clientes o dashboard de operaciones de almacén                    |
| 5 — Backend       | Todos                    | API unificada de TrackFlow: envíos, inventario, devoluciones, carriers          |
| 6 — Telemetría    | Tecnología / Dirección   | Pipeline de datos y dashboard ejecutivo global                                  |
| 7 — RAG y Memoria | CX / Operaciones         | Base de conocimiento semántica; búsqueda de políticas y procedimientos por país |
| 8 — Agentes       | CX / Devoluciones / RRHH | Agente de soporte 24/7, agente de devoluciones, agente de onboarding            |
| 9 — Workflows     | Comercial / Almacén      | Automatizaciones n8n: informes a clientes, alertas de stock, informe ejecutivo  |
| 10 — Tiempo real  | Última milla / Dirección | Tracking en vivo de paquetes, dashboard operativo en tiempo real, alertas push  |

---

## Personajes recurrentes del proyecto

| Personaje           | Rol                           | Origen                       | Género | Estilo de comunicación                                                                                             |
| ------------------- | ----------------------------- | ---------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------ |
| **Daniel Espinoza** | CEO                           | Mexicano (Latinoamérica)     | H      | Directo y orientado a datos. Pregunta siempre "¿cuánto cuesta?" y "¿cuándo lo tenemos?" Poco técnico.              |
| **Sofía Ramos**     | Returns Manager               | Mexicana (Latinoamérica)     | M      | Organizada, con alta tolerancia a la ambigüedad. Quiere reglas claras y excepciones controladas.                   |
| **Valentina Cruz**  | CX Manager                    | Latinoamericana (venezolana) | M      | Empática y exigente. Piensa siempre desde la experiencia del cliente final. Bilingüe (español/inglés).             |
| **Ashley Morris**   | Head of Commercial Operations | Estadounidense               | M      | Estructurada y orientada a métricas. Emails claros y concisos. Quiere dashboards que pueda mostrar a los clientes. |
| **Brian Calloway**  | Senior Data Analyst           | Estadounidense               | H      | Analítico y preciso. Habla en porcentajes y tendencias. Le encanta un dataset bien estructurado.                   |
| **Andrés Kim**      | CTO                           | Otro (coreano-mexicano)      | H      | Meticuloso y sistemático. Specs técnicas detalladas. Obsesionado con la escalabilidad y la observabilidad.         |
| **Carlos Vega**     | Head of Carrier Operations    | Español                      | H      | Conoce los transportistas mejor que nadie. Muy detallista en los requisitos de integración.                        |
| **Ana Whitfield**   | Head of Warehouse Operations  | Española                     | M      | Pragmática y operativa. Piensa en procesos físicos. Desconfía de la tecnología hasta que la ve funcionar.          |

---

## Tono y uso en los proyectos

TrackFlow aparece en los enunciados siempre como **el empleador del estudiante dentro de la unidad TrackFlow Tech**. Los proyectos llegan como:

- **Email de Daniel (CEO)** con una necesidad de negocio urgente y un plazo ajustado.
- **Spec técnica de Andrés (CTO)** con requisitos de arquitectura y criterios de aceptación.
- **Solicitud de un responsable de área** (Ana, Carlos, Sofía, Valentina) describiendo su problema operativo.
- **Ticket del sistema de gestión de proyectos** (Linear o Jira) asignado por el tech lead.

El estudiante siempre sabe que lo que construye **va a producción en TrackFlow** y que los operarios de Monterrey y Zaragoza van a usarlo mañana.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
_Uso exclusivo para la generación de proyectos del programa_
