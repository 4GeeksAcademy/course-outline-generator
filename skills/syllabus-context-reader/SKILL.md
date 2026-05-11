---
name: syllabus-context-reader
description: >
  Reads the AI Engineer (or AI Native Full Stack) syllabus CSV and extracts the
  full pedagogical context for a specific course day: skill being developed,
  content outline, how-to-think guidance, best practices, design patterns,
  anti-patterns, and known limitations. Also provides the list of prior skills
  so content is always coherent with what students already know.

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

## 1. Cuándo usar esta skill

- Crear o revisar **contenido de clase** (teoría, ejercicios, proyectos).
- Generar **READMEs** de proyectos o hitos.
- Diseñar **rúbricas** o **criterios de evaluación**.
- Producir **quizzes**, **checklists** o **material de apoyo**.
- Verificar que el contenido sea coherente con **lo que el estudiante ya sabe**.

> Regla de oro: nunca referenciar contenido de días futuros. El parser
> entrega `prior_skills` para evitar este error.

---

## 2. Prerequisito: ubicar el archivo CSV

Los CSVs de planificación se encuentran en:

| Programa             | Ruta                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------ |
| AI Engineer          | `course-outline-generator/ai-engineering/New Syllabus AI Engineer - Planificación del programa.csv`          |
| AI Native Full Stack | `course-outline-generator/ai-engineering/New Syllabus AI Native Full Stack - Planificación del programa.csv` |

Rutas absolutas (workspace `/Users/marcogonzalo/Projects/4Geeks/AIE-Projects`):

```
/Users/marcogonzalo/Projects/4Geeks/AIE-Projects/course-outline-generator/ai-engineering/New Syllabus AI Engineer - Planificación del programa.csv
/Users/marcogonzalo/Projects/4Geeks/AIE-Projects/course-outline-generator/ai-engineering/New Syllabus AI Native Full Stack - Planificación del programa.csv
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

**Incluir skills previas** (contexto acumulado hasta ese día):

```bash
python3 scripts/parse_syllabus.py \
  --csv <ruta_al_csv> \
  --week <semana> \
  --day <día> \
  --include-prior
```

**Buscar por palabra clave** (cuando no se conoce el día exacto):

```bash
python3 scripts/parse_syllabus.py \
  --csv <ruta_al_csv> \
  --search "tailwind"
```

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
    { "week": "0", "day": "-6", "skill": "..." },
    ...
  ]
}
```

Cualquier campo puede ser `null` si el CSV no tiene información para esa celda.

---

## 5. Flujo de trabajo recomendado

```
1. Ejecutar --list para confirmar semana y día exactos
2. Ejecutar --week X --day Y --include-prior
3. Leer el JSON resultado:
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
semana/día, usar `--search` para localizar la lección relevante, luego
extraer con `--week`/`--day`.

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
