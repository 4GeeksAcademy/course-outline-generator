---
name: syllabus-context-reader
description: >
  Official syllabus source: the planning CSV (e.g. New Syllabus AI Engineer -
  Planificación del programa.csv). NOT syllabus.md — that file is a derived export
  and may be out of date. Reads the CSV and extracts full pedagogical context for
  a course day: skill, content, how-to-think, best practices, patterns,
  anti-patterns, limitations, and prior_skills.

  Use this skill whenever a request involves creating, reviewing, or adapting
  course content (lessons, exercises, projects, assessments, quizzes, README
  files, rubrics, slides, or any educational material) for the AI Engineer or
  AI Native Full Stack programs. Trigger on phrases like "para el día N",
  "semana X día Y", "hito N", "basado en el syllabus", "en el contexto del
  curso", "qué saben los estudiantes hasta el día X", or any request that
  implies alignment with a specific point in the course timeline.
---

# Syllabus Context Reader

Extrae el contexto pedagógico completo de un día del curso desde el CSV de
planificación del programa **AI Engineer** (o **AI Native Full Stack**).

---

## 0. Fuente oficial del syllabus

| Archivo                                                         | Rol                                                                                |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **`New Syllabus AI Engineer - Planificación del programa.csv`** | **Fuente oficial** — semana, día, skill, teoría, proyecto, thinking framework      |
| **`syllabus.md`**                                               | Export derivado (Excel/conversor) — **no usar como fuente** para alinear contenido |
| **GitHub raw URL de `syllabus.md`**                             | Igual que arriba — evitar                                                          |

Si `syllabus.md` y el CSV **no coinciden**, gana el **CSV** (vía `parse_syllabus.py`).

**AI Engineer (ruta canónica en este repo):**

`course-outline-generator/ai-engineering/New Syllabus AI Engineer - Planificación del programa.csv`

---

## 1. Cuándo usar esta skill

- Crear o revisar **contenido de clase** (teoría, ejercicios, proyectos).
- Generar **READMEs** de proyectos o hitos.
- Diseñar **rúbricas** o **criterios de evaluación**.
- Producir **quizzes**, **checklists** o **material de apoyo**.
- Verificar que el contenido sea coherente con **lo que el estudiante ya sabe**.
- Consumida por `module-guidelines-generator` para crear lineamientos (estudiantes + profesor) alineados al día del syllabus.

> Regla de oro: nunca referenciar contenido de días futuros. El parser
> entrega `prior_skills` para evitar este error.

---

## 2. Prerequisito: ubicar el archivo CSV

Los CSVs de planificación se encuentran en:

| Programa    | Ruta                                                                                                |
| ----------- | --------------------------------------------------------------------------------------------------- |
| AI Engineer | `course-outline-generator/ai-engineering/New Syllabus AI Engineer - Planificación del programa.csv` |

Rutas absolutas (workspace `/Users/marcogonzalo/Projects/4Geeks/AIE-Projects`):

```text
/Users/marcogonzalo/Projects/4Geeks/AIE-Projects/course-outline-generator/ai-engineering/New Syllabus AI Engineer - Planificación del programa.csv
```

Si el contexto no especifica el programa, usar el CSV de **AI Engineer** por
defecto. El nombre del archivo puede variar; buscar el que contenga
`Planificacion` o `Syllabus` en el nombre.

---

## 3. Script de extracción

Ruta: `scripts/parse_syllabus.py`

### Comandos disponibles

**Listar todas las lecciones** (para orientarse o mapear semana/día):

```bash
python3 scripts/parse_syllabus.py \
  --csv <ruta_al_csv> \
  --list
```

**Extraer contexto de un día específico:**

```bash
python3 scripts/parse_syllabus.py \
  --csv <ruta_al_csv> \
  --week <semana> \
  --day <día>
```

Ejemplos de valores válidos:

- `--week 1 --day 2`
- `--week 0 --day -1`
- `--week 0 --day "-4 y -3"`
- `--week "HITO 01" --day "En Syllabus"` ← usar con comillas si hay espacios

**Incluir skills previas** (modo _smart_ por defecto: hitos previos + últimas N lecciones regulares):

```bash
python3 scripts/parse_syllabus.py \
  --csv <ruta_al_csv> \
  --week <semana> \
  --day <día> \
  --include-prior
```

Opciones de `prior_skills`:

| Flag                      | Efecto                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------- |
| `--include-prior`         | Modo **smart** (default): todos los hitos previos + últimas 15 lecciones regulares |
| `--prior-window N`        | Cambia N en modo smart (default `15`)                                              |
| `--prior-full`            | Todas las lecciones anteriores (máximo detalle, más tokens)                        |
| `--prior-milestones-only` | Solo hitos previos                                                                 |

**Buscar por palabra clave** (índice ligero; luego extraer el día):

```bash
python3 scripts/parse_syllabus.py \
  --csv <ruta_al_csv> \
  --search "tailwind"
```

Devuelve `matches` con `week`, `day`, `skill` — **no** el contenido completo. Después:

```bash
python3 scripts/parse_syllabus.py --csv <ruta> --week <w> --day <d> --include-prior
```

**Salida compacta** (default): JSON en una línea. Para depurar: `--pretty`.

---

## 4. Estructura del output JSON

```jsonc
{
  "current": {
    "week": "1",
    "day": "2",
    "is_milestone": false,
    "skill": "Descripción de la skill a desarrollar",

    // Contenido del día (teoría + proyectos, separados por ---)
    "content": "...",

    // Forma de pensar / mentalidad que debe desarrollar el estudiante
    "how_to_think": "...",

    // Buenas prácticas concretas esperadas
    "best_practices": "...",

    // Patrones de diseño / código recomendados
    "patterns": "...",

    // Anti-patrones a evitar
    "anti_patterns": "...",

    // Limitaciones del día (qué NO usar o qué restringir)
    "limitaciones": "...",

    // Estado de aprobación del contenido
    "statuses": "En Syllabus | Pendiente evaluación | ..."
  },

  // Solo presente con --include-prior
  "prior_skills": [
    { "week": "0", "day": "-6", "skill": "...", "is_milestone": false },
    ...
  ],
  "prior_skills_meta": {
    "mode": "smart",
    "window": 15,
    "total_prior": 29,
    "returned": 18
  }
}
```

**Búsqueda** (`--search`):

```jsonc
{
  "query": "tailwind",
  "count": 2,
  "matches": [
    { "week": "3", "day": "12", "skill": "...", "is_milestone": false },
  ],
  "next": "Run --week and --day on a match for full lesson context.",
}
```

Cualquier campo puede ser `null` si el CSV no tiene información para esa celda.

---

## 5. Flujo de trabajo recomendado

```text
1. Si semana/día desconocidos: --search "tema" → elegir match → --week/--day
   (o --list si hace falta ver todo el índice)
2. Ejecutar --week X --day Y --include-prior
   (usar --prior-full solo si hace falta el historial completo)
3. Leer el JSON resultado (compacto; no pegarlo entero al usuario):
   a. `current.skill`        → objetivo pedagógico del día
   b. `current.content`      → temario y proyectos
   c. `current.how_to_think` → mentalidad/razonamiento a desarrollar
   d. `current.best_practices` + `patterns` → qué enseñar como correcto
   e. `current.anti_patterns` + `limitaciones` → qué evitar y restringir
   f. `prior_skills`         → qué ya sabe el estudiante (NO adelantar)
4. Usar ese contexto para generar el contenido solicitado
```

---

## 6. Convenciones del CSV

| Columna | Contenido                                                          |
| ------- | ------------------------------------------------------------------ |
| 0       | Semana (número) o `HITO XX` para hitos                             |
| 1       | Día (número, rango como `-4 y -3`, o estado como `En Syllabus`)    |
| 2       | Skill (en filas de día) o contenido/proyecto (en filas de detalle) |
| 3       | How to think                                                       |
| 4       | Best practices                                                     |
| 5       | Patterns                                                           |
| 6       | Anti-patterns                                                      |
| 7       | Limitaciones                                                       |

- Un día puede tener **varias filas de contenido** (teoría + proyecto por separado).
  El script las une con `---` como separador.
- Los estados comunes son: `En Syllabus`, `Pendiente evaluación`, `Proyecto pendiente evaluación`.
- El **Prework** corresponde a `week: "0"` con días negativos (`-6` a `-1`).
- Las filas `--- SECCIÓN ---` son separadores de módulo. El parser las usa para
  hacer flush de la lección actual antes de continuar (día `-1` del Prework del
  AI Engineer termina justo antes de `--- INICIO DEL CURSO ---`).

---

## 7. Casos especiales

**Hitos (HITO 01, HITO 02…)**
Los hitos representan proyectos evaluables de cierre de módulo.
Para consultarlos:

```bash
python3 scripts/parse_syllabus.py --csv <ruta> --week "HITO 01" --day "En Syllabus"
```

**Días con rango** (ej: `-4 y -3`)
El valor de `--day` debe coincidir exactamente con lo que aparece en el CSV.
Usar `--list` primero si hay dudas.

**Búsqueda por tecnología / tema**
Cuando el usuario menciona "Tailwind", "React", "API", etc. sin especificar
semana/día: `--search` (índice ligero) → `--week`/`--day` con `--include-prior`.
No usar `--search-full` salvo depuración.

---

## 8. Notas para la generación de contenido

Una vez obtenido el JSON, aplicar estas reglas al generar cualquier material:

1. **El nivel de abstracción** debe corresponder al `how_to_think`: no
   introducir conceptos que el estudiante aún no tiene vocabulario para entender.
2. **Las restricciones de herramientas** (`limitaciones`) son pedagógicas y
   deben respetarse en ejemplos, ejercicios y proyectos generados.
3. **Los anti-patrones** son errores comunes esperados; el material debe
   anticiparlos y ayudar a prevenirlos explícitamente.
4. **`prior_skills`** define el techo de conocimiento previo. No asumir que
   el estudiante sabe algo que aparece en una fila posterior a la consultada.
5. El estado `Pendiente evaluación` indica que el contenido **puede estar
   sujeto a cambios**; advertir al usuario si corresponde.
