# Ejercicios Prácticos - Unidad 4, Sesión 1
## Agentes de IA y Fundamentos de n8n

---

## Ejercicio 1: Análisis del Paradigma PDA

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Análisis
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de la sección 4.1 sobre agentes de IA y el paradigma Percepción-Decisión-Acción

### Contexto
El paradigma Percepción-Decisión-Acción (PDA) es el marco conceptual fundamental para diseñar agentes de IA efectivos. Antes de construir un agente, necesitamos ser capaces de identificar claramente qué información percibe, cómo toma decisiones y qué acciones ejecuta. Este ejercicio te entrenará para analizar escenarios reales descomponiéndolos en sus componentes PDA, una habilidad esencial para el diseño de automatizaciones inteligentes.

### Objetivo de Aprendizaje
- Aplicar el paradigma PDA a escenarios empresariales reales
- Identificar los tres componentes fundamentales de un agente en diferentes contextos
- Distinguir entre percepción pasiva (espera inputs) y activa (monitoriza fuentes)
- Desarrollar el pensamiento estructurado necesario para diseñar agentes efectivos

### Enunciado

Para cada uno de los siguientes escenarios, identifica y describe los componentes del paradigma PDA. Completa la tabla indicando qué percibe el agente, cómo decide qué hacer y qué acciones concretas ejecuta.

### Escenario A: Agente de Soporte Técnico (eCommerce)

Una tienda online quiere un agente que atienda consultas de clientes sobre el estado de sus pedidos, gestione devoluciones sencillas y escale a un humano los casos complejos.

| Componente | Descripcion |
|------------|-------------|
| **Percepcion** (Que informacion recibe?) | Mensaje del cliente via chat, email o WhatsApp |
| Fuentes de datos | Chat en vivo, base de datos de pedidos, historial de interacciones, politica de devoluciones |
| Formato de entrada | Texto libre (lenguaje natural del cliente) |
| **Decision** (Como procesa?) | Un LLM analiza el mensaje, identifica la intencion (consulta de pedido, devolucion, queja) y determina la accion apropiada |
| Modelo de IA utilizado | GPT-4o-mini (buen balance coste/rendimiento para soporte) |
| Instrucciones clave del prompt | "Eres un agente de soporte de [tienda]. Responde de forma amable y profesional. Consulta el estado del pedido antes de responder. Si el cliente menciona problemas legales, defectos de seguridad o pide hablar con un humano, escala inmediatamente." |
| Criterios para escalar a humano | Solicitud explicita del cliente, temas legales, queja repetida (>2 interacciones sin resolucion), devoluciones de alto valor (>200 EUR) |
| **Accion** (Que ejecuta?) | Responder al cliente con informacion del pedido, iniciar devolucion en el ERP, escalar ticket a agente humano, enviar email de confirmacion |
| Acciones posibles | Consultar API de tracking, crear ticket en Zendesk, enviar email, actualizar CRM |
| Sistemas externos que necesita | Base de datos de pedidos, sistema de tracking, Zendesk/Freshdesk, email (SMTP/Gmail) |

### Escenario B: Agente de Recursos Humanos

Una empresa quiere automatizar la primera fase de seleccion de candidatos: recibir CVs, analizarlos segun los requisitos del puesto y enviar respuestas personalizadas a los candidatos.

| Componente | Descripcion |
|------------|-------------|
| **Percepcion** | CVs recibidos por email o formulario web, descripcion del puesto con requisitos, historial de candidatos previos |
| **Decision** | El LLM analiza cada CV extrayendo informacion clave (experiencia, formacion, habilidades), la compara con los requisitos del puesto y genera una puntuacion de idoneidad. Decide si el candidato pasa a la siguiente fase, se descarta o requiere revision humana |
| **Accion** | Enviar email personalizado al candidato (aceptacion para entrevista, rechazo cortes o solicitud de informacion adicional), actualizar el ATS (Applicant Tracking System), notificar al reclutador sobre candidatos destacados |

### Escenario C: Agente de Marketing de Contenidos

Un equipo de marketing necesita un agente que monitorice menciones de su marca en redes sociales, analice el sentimiento y genere borradores de respuesta para el community manager.

| Componente | Descripcion |
|------------|-------------|
| **Percepcion** | Menciones de marca en Twitter/X, Instagram, LinkedIn (via APIs de redes sociales o herramientas de social listening), notificaciones en tiempo real o monitorizacion periodica |
| **Decision** | El LLM analiza el sentimiento de cada mencion (positivo, negativo, neutro), clasifica la urgencia (mencion casual vs. crisis potencial), determina si requiere respuesta y genera un borrador adaptado al tono de la marca |
| **Accion** | Guardar la mencion y su analisis en una base de datos, enviar borrador de respuesta al community manager via Slack, alertar al equipo de crisis si el sentimiento es muy negativo, generar informe semanal de menciones |

### Escenario D: Agente Educativo (Tutor IA)

Una universidad quiere un agente que ayude a estudiantes con dudas sobre una asignatura, proporcionando explicaciones personalizadas y recomendando recursos de estudio.

| Componente | Descripcion |
|------------|-------------|
| **Percepcion** | Pregunta del estudiante via chat, historial de preguntas anteriores del mismo estudiante, materiales del curso (apuntes, presentaciones, ejercicios) |
| **Decision** | El LLM interpreta la duda, identifica el tema y el nivel de comprension, busca en los materiales del curso la informacion relevante y genera una explicacion adaptada al nivel del estudiante. Decide si recomendar recursos adicionales o sugerir tutoria presencial |
| **Accion** | Responder con una explicacion personalizada, compartir enlaces a recursos especificos (videos, capitulos del libro, ejercicios), registrar la interaccion para seguimiento del profesor, enviar alerta al profesor si detecta dificultades recurrentes |

### Preguntas de Reflexion

**1. Cual de los cuatro escenarios tiene la percepcion mas compleja? Por que?**

El Escenario C (Marketing) tiene la percepcion mas compleja porque necesita monitorizar multiples fuentes de datos en tiempo real (varias redes sociales), procesar diferentes formatos (texto, imagenes, videos) y gestionar un flujo continuo de informacion. Esto requiere multiples integraciones y un sistema de filtrado para evitar sobrecarga del agente.

**2. En el Escenario A, que criterios usarias para escalar a humano? Es mejor ser cauteloso o autonomo?**

Es mejor pecar de cauteloso al principio e ir calibrando con el tiempo. Un agente que resuelve incorrectamente un caso dana la confianza del cliente y la marca. Criterios progresivos: empezar escalando todo lo que no sea consulta directa de pedido, y gradualmente ampliar la autonomia del agente conforme se valida su rendimiento con metricas de satisfaccion.

**3. Compara los Escenarios B y C: como cambia el componente de decision entre documentos estructurados y texto libre?**

Los CVs (Escenario B) tienen estructura semi-predecible (secciones de experiencia, formacion, habilidades), lo que facilita la extraccion de informacion. Las redes sociales (Escenario C) son texto completamente libre, con jerga, ironia, emojis y contexto cultural que dificultan el analisis de sentimiento. El componente de decision en C necesita mayor sofisticacion linguistica y mayor tolerancia a la ambiguedad.

**4. Que escenario elegirias para implementar primero en n8n?**

El Escenario A (Soporte Tecnico) es la mejor opcion para empezar: la percepcion es clara (mensajes de chat), las acciones son acotadas (consultar pedido, responder), el valor de negocio es inmediato (reduce carga del equipo de soporte) y el riesgo es moderado si se implementa escalado a humano como red de seguridad.

---

## Ejercicio 2: Comparativa de Plataformas de Automatización

### Metadata
- **Duración estimada**: 15 minutos
- **Tipo**: Investigación/Análisis
- **Modalidad**: Parejas
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de la sección 4.2 sobre introducción a n8n y su comparativa con Make y Zapier

### Contexto
En el mercado existen múltiples plataformas de automatización, cada una con sus fortalezas y limitaciones. Elegir la plataforma correcta para un proyecto específico es una decisión estratégica que impacta en costes, escalabilidad, seguridad y capacidades de IA. Este ejercicio te ayudará a desarrollar criterios de evaluación para tomar esta decisión de forma informada.

### Objetivo de Aprendizaje
- Comparar las tres plataformas principales de automatización no-code (n8n, Make, Zapier)
- Aplicar criterios de decisión a un caso de uso concreto
- Comprender las ventajas competitivas de n8n para agentes de IA
- Desarrollar argumentación técnica para la selección de herramientas

### Enunciado

### Parte A: Tabla de Decisión (7 min)

Tu equipo debe evaluar qué plataforma es más adecuada para el siguiente caso de uso:

> **Caso**: Una clínica dental con 3 sedes quiere automatizar la gestión de citas. El sistema debe: (1) recibir solicitudes de cita por WhatsApp, (2) consultar la disponibilidad en Google Calendar, (3) confirmar la cita al paciente, y (4) enviar recordatorios 24h antes. Además, quieren que un agente de IA responda preguntas frecuentes sobre tratamientos. Los datos de pacientes son sensibles (normativa sanitaria) y el presupuesto es limitado.

Completa la siguiente tabla de evaluación (puntúa de 1 a 5 cada criterio):

| Criterio | n8n | Make | Zapier | Peso (importancia) |
|----------|-----|------|--------|---------------------|
| Coste (menor es mejor) | 5 | 3 | 2 | Alta |
| Facilidad de uso | 3 | 4 | 5 | Media |
| Integracion con WhatsApp | 4 | 4 | 4 | Alta |
| Capacidades de IA nativas | 5 | 3 | 3 | Alta |
| Despliegue on-premise (datos sensibles) | 5 | 1 | 1 | Muy Alta |
| Numero de integraciones disponibles | 3 | 4 | 5 | Media |
| Soporte de la comunidad | 4 | 3 | 4 | Baja |
| Escalabilidad | 4 | 4 | 3 | Media |
| **Total ponderado** | **86** | **61** | **61** | |

**Instrucciones para el total ponderado:**
- Muy Alta = x4, Alta = x3, Media = x2, Baja = x1

### Parte B: Justificacion de la Decision (5 min)

**Calculos del total ponderado:**
- n8n: 5x3 + 3x2 + 4x3 + 5x3 + 5x4 + 3x2 + 4x1 + 4x2 = 15+6+12+15+20+6+4+8 = **86**
- Make: 3x3 + 4x2 + 4x3 + 3x3 + 1x4 + 4x2 + 3x1 + 4x2 = 9+8+12+9+4+8+3+8 = **61**
- Zapier: 2x3 + 5x2 + 4x3 + 3x3 + 1x4 + 5x2 + 4x1 + 3x2 = 6+10+12+9+4+10+4+6 = **61**

**1. Plataforma recomendada:** n8n. Gana con diferencia en los criterios mas ponderados: despliegue on-premise (imprescindible para datos sanitarios bajo normativa), coste (clinica con presupuesto limitado, n8n es open source) y capacidades de IA nativas (agente para FAQ de tratamientos).

**2. Factor determinante:** El despliegue on-premise. Los datos de pacientes son sensibles y la normativa sanitaria exige control sobre donde se almacenan. Sin este criterio, el resultado seria mucho mas equilibrado y Zapier podria ganar por facilidad de uso.

**3. Trade-offs de n8n:** Menor numero de integraciones predefinidas (se suple con HTTP Request), curva de aprendizaje mayor que Zapier (mitigable con templates y documentacion), y necesidad de mantener la infraestructura propia (mitigable con Docker y backups automatizados).

### Parte C: Escenario Alternativo (3 min)

Ahora imaginad que el caso de uso cambia: en lugar de una clinica dental con datos sensibles, se trata de una **tienda de ropa online** que solo necesita automatizar publicaciones en Instagram y responder mensajes directos.

**Respuesta:** Si, cambiaria la recomendacion a **Zapier**. Sin requisitos de privacidad de datos sensibles, el despliegue on-premise deja de ser critico. Zapier tiene integracion nativa y robusta con Instagram, su facilidad de uso reduce el tiempo de implementacion y el equipo de marketing probablemente no tiene perfil tecnico para mantener una instancia de n8n. El mayor coste de Zapier se compensa con el ahorro en administracion de sistemas.

### Preguntas de Reflexion

**1. En que situaciones elegirias Zapier a pesar de su mayor coste?**

Cuando el equipo no tiene perfil tecnico, cuando se necesita una solucion rapida (dias, no semanas), cuando las integraciones requeridas son populares (Gmail, Slack, Notion) y cuando no hay datos sensibles que exijan on-premise. La simplicidad es mas valiosa que la flexibilidad cuando el coste de oportunidad de aprender una herramienta compleja supera el beneficio de esa flexibilidad.

**2. n8n open source es siempre una ventaja? Que desafios implica mantener una instancia propia?**

No siempre. Mantener una instancia propia implica: administrar el servidor (actualizaciones, backups, seguridad), gestionar la disponibilidad (si se cae n8n, se paran las automatizaciones), configurar SSL/TLS para acceso seguro, y escalar la infraestructura si crece el uso. Para equipos sin DevOps, un servicio gestionado como n8n Cloud o incluso Zapier puede ser mas rentable a pesar del coste extra.

---

## Ejercicio 3: Primer Workflow en n8n

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Hands-on / Práctico
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: n8n instalado y funcionando (local con Docker o n8n Cloud), lectura de secciones 4.3 y 4.4 sobre instalación y arquitectura de n8n

### Contexto
La mejor manera de aprender n8n es construyendo. En este ejercicio crearás tu primer workflow funcional que incluye los tres tipos de nodos fundamentales: un trigger que inicia la ejecución, un nodo de procesamiento que transforma datos y un nodo condicional que bifurca el flujo según una condición. Este patrón básico (trigger → procesamiento → condicional) es la base de la mayoría de las automatizaciones.

### Objetivo de Aprendizaje
- Crear un workflow desde cero en n8n
- Comprender el flujo de datos entre nodos (concepto de items y JSON)
- Utilizar el Manual Trigger para ejecutar y depurar workflows
- Configurar un nodo Set para definir y transformar datos
- Implementar lógica condicional con el nodo IF

### Enunciado

### Paso 1: Crear un Nuevo Workflow (2 min)

1. Abre n8n en tu navegador (por defecto: `http://localhost:5678`)
2. Haz clic en **"Add workflow"** (o el botón **+** en la esquina superior)
3. Dale un nombre descriptivo al workflow: `Ejercicio 3 - Mi Primer Workflow`

### Paso 2: Añadir el Manual Trigger (3 min)

1. Haz clic en el botón **"+"** en el canvas para añadir un nodo
2. Busca **"Manual Trigger"** y selecciónalo (también llamado "When clicking 'Test workflow'")
3. Este nodo se ejecutará cada vez que hagas clic en **"Test workflow"**

> **Nota**: El Manual Trigger es ideal para desarrollo y pruebas. En producción, lo sustituirías por un Webhook Trigger, Schedule Trigger u otro tipo de trigger automático.

### Paso 3: Añadir un Nodo Set (10 min)

1. Haz clic en el **"+"** que aparece a la derecha del Manual Trigger
2. Busca **"Edit Fields (Set)"** y selecciónalo
3. Configura los siguientes campos haciendo clic en **"Add Field"**:

| Campo | Tipo | Valor |
|-------|------|-------|
| `nombre` | String | `María García` |
| `edad` | Number | `28` |
| `curso` | String | `Aprendizaje Automático II` |
| `nota_final` | Number | `7.5` |
| `asistencia_porcentaje` | Number | `85` |

4. Haz clic en **"Test step"** para verificar que el nodo produce datos
5. Observa la pestaña **Output** a la derecha: deberías ver un JSON con los 5 campos

**Resultado esperado en la salida (Output):**
```json
[
  {
    "nombre": "María García",
    "edad": 28,
    "curso": "Aprendizaje Automático II",
    "nota_final": 7.5,
    "asistencia_porcentaje": 85
  }
]
```

> **Concepto clave**: En n8n, los datos fluyen entre nodos como **items**. Cada item es un objeto JSON. Un nodo puede producir uno o varios items que pasan al siguiente nodo.

### Paso 4: Añadir un Nodo IF (10 min)

1. Haz clic en el **"+"** a la derecha del nodo Set
2. Busca **"IF"** y selecciónalo
3. Configura la condición:
   - **Value 1**: Selecciona `{{ $json.nota_final }}` (haz clic en el campo y usa el selector de expresiones, o escribe directamente arrastrando el campo desde el panel izquierdo)
   - **Operation**: `is greater than or equal` (mayor o igual que)
   - **Value 2**: `5`

4. El nodo IF tiene dos salidas:
   - **true**: Se ejecuta cuando la condición se cumple (nota >= 5, aprobado)
   - **false**: Se ejecuta cuando la condición NO se cumple (nota < 5, suspenso)

### Paso 5: Añadir Nodos de Resultado (5 min)

1. En la salida **true** del IF, añade un nodo **Edit Fields (Set)** con:
   - Campo `resultado`: String, valor `Aprobado`
   - Campo `mensaje`: String, valor `Enhorabuena, {{ $json.nombre }}. Has aprobado con un {{ $json.nota_final }}.`

2. En la salida **false** del IF, añade otro nodo **Edit Fields (Set)** con:
   - Campo `resultado`: String, valor `Suspenso`
   - Campo `mensaje`: String, valor `Lo sentimos, {{ $json.nombre }}. No has alcanzado la nota mínima.`

> **Nota sobre expresiones**: Las dobles llaves `{{ }}` permiten usar expresiones en n8n. `$json` hace referencia a los datos que llegan del nodo anterior.

### Paso 6: Ejecutar y Verificar (5 min)

1. Haz clic en **"Test workflow"** (botón en la parte superior)
2. Observa cómo los datos fluyen por los nodos: cada nodo mostrará un indicador verde con el número de items procesados
3. Haz clic en cada nodo para inspeccionar su salida (Output)

**Verificaciones:**
- [ ] El Manual Trigger se ejecuta sin errores
- [ ] El nodo Set produce un item con los 5 campos
- [ ] El nodo IF evalúa correctamente la condición (nota 7.5 >= 5 → true)
- [ ] El flujo sigue por la rama **true** (aprobado)
- [ ] El mensaje final incluye el nombre y la nota del estudiante

### Paso 7: Experimentar (tiempo extra)

Modifica el valor de `nota_final` a `3.5` y vuelve a ejecutar el workflow. Verifica que ahora el flujo sigue por la rama **false** (suspenso).

**Diagrama del workflow completo:**
```
[Manual Trigger] → [Set: Datos Estudiante] → [IF: nota >= 5?]
                                                  ├── true → [Set: Aprobado]
                                                  └── false → [Set: Suspenso]
```

### Preguntas de Reflexión

1. ¿Qué ocurre si añades una segunda condición al nodo IF (por ejemplo, `asistencia_porcentaje >= 80`)? ¿Cómo combinarías ambas condiciones (AND/OR)?
2. El nodo Set define datos estáticos. En un workflow real, ¿de dónde vendrían estos datos? Nombra al menos 3 fuentes posibles (ej: formulario web, base de datos, API...).
3. ¿Cómo modificarías este workflow para procesar una lista de 10 estudiantes en lugar de uno solo? (Pista: el nodo Set puede producir múltiples items)

---

## Ejercicio 4: Diseño de Automatización con Schedule Trigger

### Metadata
- **Duración estimada**: 25 minutos
- **Tipo**: Diseño
- **Modalidad**: Individual
- **Dificultad**: Intermedia
- **Prerequisitos**: Comprensión de los tipos de nodos en n8n (sección 4.4), conocimiento básico de APIs REST

### Contexto
Muchas automatizaciones empresariales necesitan ejecutarse de forma periódica: resúmenes diarios, informes semanales, monitorizaciones cada hora... El Schedule Trigger de n8n permite programar estas ejecuciones automáticas. En este ejercicio diseñarás un workflow completo para un caso de uso real, combinando múltiples tipos de nodos en un flujo coherente.

### Objetivo de Aprendizaje
- Comprender el funcionamiento del Schedule Trigger y sus opciones de configuración
- Diseñar workflows multi-paso con bifurcaciones condicionales
- Planificar la integración de servicios externos (APIs, email)
- Documentar un diseño de workflow antes de implementarlo

### Enunciado

### Escenario

Tu jefe te pide diseñar un workflow en n8n que genere y envíe un **resumen diario de noticias sobre IA** cada mañana a las 8:00. El workflow debe:

1. Ejecutarse automáticamente todos los días laborables (lunes a viernes)
2. Obtener las últimas noticias sobre IA de una API de noticias
3. Filtrar solo las noticias en español o inglés
4. Generar un resumen con un modelo de IA
5. Enviar el resumen por email al equipo

### Parte A: Diagrama de Nodos (10 min)

Dibuja (en papel o en una herramienta de diagramas) el workflow completo identificando cada nodo necesario. Para cada nodo, indica:
- **Tipo de nodo** en n8n (nombre exacto)
- **Propósito** (qué hace en el flujo)
- **Datos de entrada** (qué recibe del nodo anterior)
- **Datos de salida** (qué produce para el siguiente nodo)

**Plantilla de nodos a considerar:**

```
Nodo 1: [Schedule Trigger]
   ├── Tipo: Schedule Trigger
   ├── Configuracion: Cron expression: lunes a viernes a las 8:00 (Europe/Madrid)
   ├── Entrada: Ninguna (es el trigger)
   └── Salida: Timestamp de ejecucion ({ "timestamp": "2026-03-10T08:00:00.000Z" })

Nodo 2: [HTTP Request - NewsAPI]
   ├── Tipo: HTTP Request
   ├── Configuracion: GET https://newsapi.org/v2/everything?q=artificial+intelligence+OR+inteligencia+artificial&language=es,en&sortBy=publishedAt&pageSize=10, Header Auth con X-Api-Key
   ├── Entrada: Timestamp del trigger (no se usa directamente, solo activa la ejecucion)
   └── Salida: JSON con array de articulos ({ "status": "ok", "totalResults": N, "articles": [...] })

Nodo 3: [IF - Hay noticias?]
   ├── Tipo: IF
   ├── Configuracion: Condicion: {{ $json.totalResults }} is greater than 0
   ├── Entrada: Respuesta de NewsAPI
   └── Salida: true (pasa articulos al siguiente nodo) / false (no hay noticias, se detiene)

Nodo 4: [OpenAI - Generar Resumen]
   ├── Tipo: HTTP Request (POST a OpenAI API) o nodo OpenAI nativo
   ├── Configuracion: POST https://api.openai.com/v1/chat/completions, modelo gpt-4o-mini, system prompt con instrucciones de resumen, user message con los titulares y descripciones
   ├── Entrada: Array de articulos filtrados (true branch del IF)
   └── Salida: Texto del resumen generado por el modelo

Nodo 5: [Gmail - Enviar Resumen]
   ├── Tipo: Gmail (o Send Email)
   ├── Configuracion: To: equipo@empresa.com, Subject: "Resumen diario de noticias IA - {{ $now.format('dd/MM/yyyy') }}", Body: contenido del resumen generado
   ├── Entrada: Texto del resumen del nodo OpenAI
   └── Salida: Confirmacion de envio del email
```

**Diagrama visual sugerido:**
```
[Schedule Trigger] → [HTTP Request] → [IF: ¿Hay noticias?]
    (L-V 8:00)       (API noticias)        ├── true → [OpenAI] → [Gmail]
                                           └── false → [Stop]
```

### Parte B: Configuración Detallada del Schedule Trigger (5 min)

Especifica la configuración exacta del Schedule Trigger:

| Parametro | Valor | Justificacion |
|-----------|-------|---------------|
| Trigger Times → Rule | Cron | Permite control granular sobre dias y horas exactas |
| Hora | 8 | El equipo empieza a trabajar a las 8:00-8:30, asi tienen el resumen al abrir el correo |
| Minuto | 0 | Ejecucion al inicio de la hora, momento predecible |
| Dias de la semana | Lunes, Martes, Miercoles, Jueves, Viernes | Solo dias laborables, no tiene sentido enviar el fin de semana si nadie lo va a leer |
| Zona horaria | Europe/Madrid (CET/CEST) | La hora debe coincidir con el horario laboral del equipo en Espana |

**Pregunta**: Que ocurre si el servidor de n8n esta apagado a las 8:00? Se ejecutara el workflow cuando el servidor vuelva a estar online?

**Respuesta:** No, n8n NO recupera ejecuciones perdidas por defecto. Si el servidor esta apagado a las 8:00, esa ejecucion se pierde. Cuando n8n vuelve a estar online, simplemente espera al siguiente horario programado. Para mitigar esto se puede: (1) usar un servicio de monitorizacion que alerte si n8n se cae, (2) desplegar n8n con Docker + restart policy "always" para que se reinicie automaticamente, o (3) anadir un workflow de "health check" que detecte si se ha saltado alguna ejecucion.

### Parte C: Diseño del Nodo HTTP Request (5 min)

Para obtener las noticias, usarás la API gratuita de NewsAPI (https://newsapi.org). Diseña la configuración del nodo HTTP Request:

| Parámetro | Valor |
|-----------|-------|
| Method | `GET` |
| URL | `https://newsapi.org/v2/everything` |
| Query Parameters | |
| → `q` | `artificial intelligence OR inteligencia artificial` |
| → `language` | `es` (se puede hacer dos peticiones, una con `es` y otra con `en`, o filtrar despues) |
| → `sortBy` | `publishedAt` (las mas recientes primero) |
| → `pageSize` | `10` (suficientes para un resumen diario sin saturar) |
| Authentication | Predefined Credential Type → Header Auth |
| → Header Name | `X-Api-Key` |
| → Header Value | `{{ $credentials.newsApiKey }}` |

**Pregunta**: Por que es importante usar `$credentials` en lugar de poner la API key directamente en el nodo? Como se configuran las credenciales en n8n?

**Respuesta:** Usar `$credentials` es importante por tres razones: (1) **Seguridad**: las credenciales se almacenan cifradas en la base de datos de n8n, no en texto plano dentro del workflow. (2) **Portabilidad**: si exportas el workflow como JSON, las credenciales NO se incluyen, evitando fugas accidentales de API keys. (3) **Mantenimiento**: si la key cambia, solo la actualizas en un sitio (Settings > Credentials) y todos los workflows que la usan se actualizan automaticamente. Se configuran en Settings > Credentials > Add Credential, eligiendo el tipo (Header Auth, OAuth2, etc.) y rellenando los campos requeridos.

### Parte D: Diseño del Prompt para el Resumen (5 min)

Escribe el System Prompt que usarías en el nodo de OpenAI (o el modelo de IA que prefieras) para generar el resumen:

```
System Prompt:
Eres un analista de noticias sobre inteligencia artificial. Tu tarea es generar un resumen diario conciso y profesional a partir de una lista de articulos.

Formato de salida:
- Titulo: "Resumen diario de IA - [fecha]"
- Un parrafo introductorio (2-3 frases) con la tendencia general del dia
- Lista de 3-5 noticias destacadas, cada una con:
  * Titulo de la noticia (en negrita)
  * Fuente y fecha
  * Resumen en 1-2 frases
  * Enlace al articulo original
- Un parrafo de cierre con una reflexion breve sobre la tendencia del dia

Reglas:
- Escribe siempre en espanol
- Tono profesional e informativo, sin sensacionalismo
- Prioriza noticias con impacto practico o empresarial
- Si hay noticias repetidas (mismo tema, distintas fuentes), agrupa y menciona la fuente mas fiable
- Longitud total: 300-500 palabras
```

**Consideraciones aplicadas en el prompt:**
- Longitud: 300-500 palabras (legible en 2-3 minutos, ideal para un email matutino)
- Formato: Titulo + intro + bullets con estructura fija + cierre (facil de escanear)
- Tono: Profesional e informativo (contexto empresarial)
- Idioma: Espanol (equipo hispanohablante)
- Informacion por noticia: Titulo, fuente, resumen, enlace (lo esencial sin saturar)

### Preguntas de Reflexion

**1. Como manejarias el caso en que la API de noticias devuelve un error (ej: limite de peticiones excedido)? Que nodo anadirias y donde?**

Anadiria un nodo IF justo despues del HTTP Request que compruebe el codigo de respuesta: si `{{ $json.statusCode }}` no es 200, el flujo va por la rama false hacia un nodo de notificacion (email o Slack) que avise al administrador del error. Ademas, en la configuracion del HTTP Request activaria "Continue On Fail" para que el workflow no se detenga abruptamente. Tambien se podria anadir un nodo "Wait" + reintentar la peticion (patron retry) antes de notificar.

**2. Si quisieras enviar el resumen tambien por Slack ademas de por email, como modificarias el diagrama? Los nodos de Gmail y Slack irian en paralelo o en serie?**

Irian en **paralelo**. Despues del nodo OpenAI (que genera el resumen), conectaria tanto el nodo Gmail como el nodo Slack directamente. En n8n esto se hace simplemente conectando la salida del nodo OpenAI a ambos nodos. No hay dependencia entre ellos: el envio por email no necesita esperar al de Slack ni viceversa. El diagrama quedaria:
```
[OpenAI] → [Gmail]
[OpenAI] → [Slack]
```

**3. Que ventaja tiene programar el workflow a las 8:00 en vez de ejecutarlo manualmente cada manana? Mas alla del ahorro de tiempo, que otros beneficios aporta la automatizacion?**

Beneficios adicionales: (1) **Consistencia**: se ejecuta todos los dias sin excepciones, no depende de que alguien se acuerde. (2) **Fiabilidad**: a las 8:00 exactas, no a las 8:15 o 9:30 segun el dia. (3) **Escalabilidad**: si manana quieres anadir otro resumen (ej: noticias de ciberseguridad a las 9:00), solo duplicas el workflow. (4) **Auditabilidad**: n8n registra cada ejecucion con su resultado, util para depurar o demostrar que se envio. (5) **Independencia**: funciona aunque la persona responsable este de vacaciones o de baja.

---

## Ejercicio 5: Configuración de Credenciales y Primer Nodo de IA

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Hands-on / Práctico
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: n8n instalado y funcionando, cuenta en OpenAI o en OpenRouter (alternativa gratuita) con API key disponible, lectura de secciones 4.3 y 4.5

### Contexto
Antes de construir agentes de IA en n8n, necesitamos configurar las credenciales que permiten a n8n comunicarse con los proveedores de modelos de lenguaje. La gestión segura de credenciales es un aspecto crítico de cualquier plataforma de automatización: las API keys deben almacenarse de forma cifrada y nunca exponerse en los workflows. En este ejercicio configurarás tus primeras credenciales y verificarás que la conexión funciona correctamente.

### Objetivo de Aprendizaje
- Configurar credenciales de un proveedor de IA (OpenAI u OpenRouter) en n8n de forma segura
- Comprender el sistema de gestión de credenciales de n8n
- Realizar una primera llamada a un modelo de IA desde n8n
- Verificar la conexión y diagnosticar errores comunes

### Enunciado

### Paso 1: Obtener tu API Key (3 min)

Puedes usar **OpenAI** o **OpenRouter** (alternativa gratuita recomendada). Elige una de las dos opciones:

**Opción A: OpenAI (de pago)**
1. Accede a [platform.openai.com](https://platform.openai.com)
2. Ve a **API Keys** en el menú lateral
3. Crea una nueva API key: haz clic en **"Create new secret key"**
4. **Copia la key inmediatamente** (solo se muestra una vez)
5. Verifica que tienes créditos disponibles en **Usage** > **Billing**

**Opción B: OpenRouter (gratuita)**
1. Accede a [openrouter.ai](https://openrouter.ai) y crea una cuenta (puedes usar Google o GitHub)
2. Ve a **Keys** en el menú lateral ([openrouter.ai/keys](https://openrouter.ai/keys))
3. Crea una nueva API key haciendo clic en **"Create Key"**
4. **Copia la key inmediatamente** (comienza por `sk-or-...`)
5. OpenRouter ofrece modelos gratuitos, no necesitas añadir saldo para este ejercicio

> **Importante**: Tu API key es como una contraseña. Nunca la compartas, no la pongas en código fuente y no la pegues en chats o documentos compartidos. n8n la almacenará cifrada.

### Paso 2: Configurar Credenciales en n8n (5 min)

1. En n8n, ve a **Settings** (icono de engranaje) > **Credentials**
2. Haz clic en **"Add Credential"**
3. Busca **"Header Auth"** en la lista de tipos de credencial
4. Rellena los campos:

**Si usas OpenAI:**

| Campo | Valor |
|-------|-------|
| Credential Name | `OpenAI - Mi cuenta` |
| Name | `Authorization` |
| Value | `Bearer sk-...` (pega tu API key con el prefijo Bearer) |

**Si usas OpenRouter:**

| Campo | Valor |
|-------|-------|
| Credential Name | `OpenRouter - Mi cuenta` |
| Name | `Authorization` |
| Value | `Bearer sk-or-...` (pega tu API key con el prefijo Bearer) |

5. Haz clic en **"Save"**
6. n8n mostrará un mensaje de confirmación indicando que las credenciales se han guardado

> **Nota sobre seguridad**: n8n almacena las credenciales cifradas en su base de datos. Cuando usas Docker, la clave de cifrado se define mediante la variable de entorno `N8N_ENCRYPTION_KEY`. Asegúrate de que esta variable está configurada y respaldada.

### Paso 3: Crear un Workflow de Prueba con IA (7 min)

1. Crea un nuevo workflow llamado `Ejercicio 5 - Test IA`
2. Añade los siguientes nodos en orden:

**Nodo 1: Manual Trigger**
- Tipo: `Manual Trigger`

**Nodo 2: HTTP Request (llamada al modelo de IA)**
- Tipo: Busca **"HTTP Request"** en los nodos

Configura el nodo HTTP Request según el proveedor que elegiste:

**Si usas OpenAI:**

| Parámetro | Valor |
|-----------|-------|
| Method | `POST` |
| URL | `https://api.openai.com/v1/chat/completions` |
| Authentication | Predefined Credential Type → Header Auth |
| Credential | Selecciona `OpenAI - Mi cuenta` |
| Body Content Type | JSON |
| Body | Ver abajo |

**Si usas OpenRouter:**

| Parámetro | Valor |
|-----------|-------|
| Method | `POST` |
| URL | `https://openrouter.ai/api/v1/chat/completions` |
| Authentication | Predefined Credential Type → Header Auth |
| Credential | Selecciona `OpenRouter - Mi cuenta` |
| Body Content Type | JSON |
| Body | Ver abajo |

**Body del request (igual para ambos proveedores):**
```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Eres un asistente útil que responde en español de forma concisa."
    },
    {
      "role": "user",
      "content": "Explica en 2 frases qué es un agente de IA."
    }
  ],
  "max_tokens": 150,
  "temperature": 0.7
}
```

> **Nota OpenRouter**: Si usas OpenRouter, puedes cambiar el modelo a uno gratuito como `google/gemma-3-4b-it:free` o `meta-llama/llama-4-scout:free`. Consulta los modelos gratuitos disponibles en [openrouter.ai/models?q=free](https://openrouter.ai/models?q=free).

3. Conecta los nodos: `Manual Trigger → HTTP Request`

### Paso 4: Ejecutar y Verificar (5 min)

1. Haz clic en **"Test workflow"**
2. Inspecciona la salida del nodo HTTP Request
3. Verifica que la respuesta contiene texto generado por el modelo

**Verificaciones:**
- [ ] Las credenciales se configuraron sin errores
- [ ] El nodo se conecta exitosamente a la API (OpenAI u OpenRouter)
- [ ] La respuesta contiene un campo `choices` con el texto generado
- [ ] El texto está en español como se solicitó en el system prompt
- [ ] No hay errores de autenticación (código 401) ni de cuota (código 429)

### Diagnóstico de Errores Comunes

Si la ejecución falla, consulta esta tabla:

| Error | Código HTTP | Causa Probable | Solución |
|-------|-------------|----------------|----------|
| Invalid API key | 401 | API key incorrecta o expirada | Verifica la key en platform.openai.com u openrouter.ai/keys |
| Rate limit exceeded | 429 | Demasiadas peticiones | Espera unos segundos y reintenta |
| Insufficient quota | 429 | Sin créditos (OpenAI) | Añade saldo en Billing. Con OpenRouter usa un modelo gratuito |
| Model not found | 404 | Nombre de modelo incorrecto | Verifica que el modelo existe. En OpenRouter consulta openrouter.ai/models |
| Connection refused | - | n8n no puede acceder a internet | Verifica la configuración de red/Docker |

### Preguntas de Reflexión

1. ¿Qué diferencia hay entre usar el nodo nativo de OpenAI en n8n y hacer una llamada HTTP Request manual? ¿Cuándo preferirías uno sobre el otro?
2. ¿Qué pasaría si compartes el workflow exportado (JSON) con un compañero? ¿Se incluyen las credenciales en la exportación? ¿Por qué es importante que no se incluyan?
3. Si quisieras usar Claude (Anthropic) en lugar de OpenAI, ¿qué cambiarías en la configuración? ¿n8n soporta múltiples proveedores de IA?
4. ¿Qué ventajas e inconvenientes tiene usar un servicio como OpenRouter frente a usar directamente la API del proveedor (OpenAI, Anthropic, etc.)? Considera aspectos como coste, latencia, disponibilidad y variedad de modelos.

---

## Ejercicio 6: Exploración de Templates de n8n

### Metadata
- **Duración estimada**: 15 minutos
- **Tipo**: Exploración/Investigación
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Familiaridad básica con la interfaz de n8n, comprensión del concepto de workflow y nodos

### Contexto
n8n cuenta con una biblioteca pública de templates (plantillas) con cientos de workflows pre-construidos por la comunidad y el equipo de n8n. Explorar estos templates es una excelente forma de aprender patrones de diseño, descubrir nodos que no conocías y acelerar el desarrollo de tus propios workflows. En particular, los templates de agentes de IA muestran las mejores prácticas para combinar modelos de lenguaje con herramientas y memoria.

### Objetivo de Aprendizaje
- Navegar y filtrar la biblioteca de templates de n8n
- Identificar templates relevantes para agentes de IA
- Analizar la estructura de workflows existentes para aprender patrones de diseño
- Evaluar qué templates pueden servir como punto de partida para proyectos propios

### Enunciado

### Parte A: Exploración de la Biblioteca (5 min)

1. Accede a la biblioteca de templates de n8n: [https://n8n.io/workflows/](https://n8n.io/workflows/)
2. Familiarízate con los filtros disponibles:
   - **Categoría** (ej: AI, Marketing, Sales, IT...)
   - **Nodos utilizados** (ej: OpenAI, Slack, Gmail...)
   - **Popularidad** y **fecha de publicación**

3. Realiza las siguientes búsquedas y anota cuántos resultados obtienes:

| Búsqueda | Número de resultados |
|----------|---------------------|
| "AI Agent" | ___ |
| "OpenAI" | ___ |
| "chatbot" | ___ |
| "email automation" | ___ |

### Parte B: Selección y Análisis de Templates (7 min)

Busca y selecciona **3 templates** que sean relevantes para construir agentes de IA. Para cada template, documenta la siguiente información:

**Template 1:**

| Aspecto | Descripción |
|---------|-------------|
| Nombre del template | __________________ |
| URL | __________________ |
| Descripción breve | __________________ |
| Nodos que utiliza (listado) | __________________ |
| ¿Usa nodo AI Agent? | Sí / No |
| ¿Incluye memoria? | Sí / No |
| ¿Qué herramientas (tools) usa el agente? | __________________ |
| ¿Qué trigger lo inicia? | __________________ |
| Complejidad estimada (Baja/Media/Alta) | __________________ |
| ¿Podrías usarlo como base para un proyecto propio? | __________________ |

**Template 2:**

| Aspecto | Descripción |
|---------|-------------|
| Nombre del template | __________________ |
| URL | __________________ |
| Descripción breve | __________________ |
| Nodos que utiliza (listado) | __________________ |
| ¿Usa nodo AI Agent? | Sí / No |
| ¿Incluye memoria? | Sí / No |
| ¿Qué herramientas (tools) usa el agente? | __________________ |
| ¿Qué trigger lo inicia? | __________________ |
| Complejidad estimada (Baja/Media/Alta) | __________________ |
| ¿Podrías usarlo como base para un proyecto propio? | __________________ |

**Template 3:**

| Aspecto | Descripción |
|---------|-------------|
| Nombre del template | __________________ |
| URL | __________________ |
| Descripción breve | __________________ |
| Nodos que utiliza (listado) | __________________ |
| ¿Usa nodo AI Agent? | Sí / No |
| ¿Incluye memoria? | Sí / No |
| ¿Qué herramientas (tools) usa el agente? | __________________ |
| ¿Qué trigger lo inicia? | __________________ |
| Complejidad estimada (Baja/Media/Alta) | __________________ |
| ¿Podrías usarlo como base para un proyecto propio? | __________________ |

### Parte C: Comparación y Patrones (3 min)

Responde las siguientes preguntas basándote en los 3 templates seleccionados:

1. **Patrón común**: ¿Qué nodos aparecen en los 3 templates? ¿Hay un patrón de diseño recurrente?
2. **Trigger más frecuente**: ¿Qué tipo de trigger es el más utilizado en templates de agentes de IA? ¿Por qué crees que es así?
3. **Memoria**: De los templates que incluyen memoria, ¿qué tipo de memoria usan (Window Buffer, PostgreSQL, etc.)? ¿Cómo afecta el tipo de memoria al comportamiento del agente?

### Preguntas de Reflexión

1. ¿Es mejor crear un workflow desde cero o partir de un template existente? ¿En qué situaciones preferirías cada enfoque?
2. Los templates de la comunidad pueden estar desactualizados o usar versiones antiguas de nodos. ¿Cómo verificarías que un template sigue siendo funcional antes de usarlo en un proyecto real?
3. Si tuvieras que crear un template para compartir con la comunidad, ¿qué workflow diseñarías? ¿Qué problema resolvería?

---

## Soluciones de Referencia

<details>
<summary>Ver solución Ejercicio 1 - Análisis del Paradigma PDA</summary>

### Escenario A: Agente de Soporte Técnico (eCommerce)

| Componente | Descripción |
|------------|-------------|
| **Percepción** | Mensaje del cliente vía chat, email o WhatsApp |
| Fuentes de datos | Chat en vivo, base de datos de pedidos, historial de interacciones, política de devoluciones |
| Formato de entrada | Texto libre (lenguaje natural del cliente) |
| **Decisión** | Un LLM (ej: GPT-4o o Claude) analiza el mensaje, identifica la intención (consulta de pedido, devolución, queja) y determina la acción apropiada |
| Modelo de IA utilizado | GPT-4o-mini (suficiente para soporte, buen balance coste/rendimiento) |
| Instrucciones clave del prompt | "Eres un agente de soporte de [tienda]. Responde de forma amable y profesional. Consulta el estado del pedido antes de responder. Si el cliente menciona problemas legales, defectos de seguridad o solicita hablar con un humano, escala inmediatamente." |
| Criterios para escalar a humano | Solicitud explícita del cliente, temas legales, queja repetida (>2 interacciones sin resolución), devoluciones de alto valor (>200 EUR) |
| **Acción** | Responder al cliente con información del pedido, iniciar proceso de devolución en el ERP, escalar ticket a agente humano, enviar email de confirmación |
| Acciones posibles | Consultar API de tracking, crear ticket en Zendesk, enviar email, actualizar CRM |
| Sistemas externos que necesita | Base de datos de pedidos, sistema de tracking, Zendesk/Freshdesk, email (SMTP/Gmail) |

### Escenario B: Agente de Recursos Humanos

| Componente | Descripción |
|------------|-------------|
| **Percepción** | CVs recibidos por email o formulario web, descripción del puesto con requisitos, historial de candidatos previos |
| **Decisión** | El LLM analiza cada CV extrayendo información clave (experiencia, formación, habilidades), la compara con los requisitos del puesto y genera una puntuación de idoneidad. Decide si el candidato pasa a la siguiente fase, se descarta o requiere revisión humana |
| **Acción** | Enviar email personalizado al candidato (aceptación para entrevista, rechazo cortés o solicitud de información adicional), actualizar el ATS (Applicant Tracking System), notificar al reclutador sobre candidatos destacados |

### Escenario C: Agente de Marketing de Contenidos

| Componente | Descripción |
|------------|-------------|
| **Percepción** | Menciones de marca en Twitter/X, Instagram, LinkedIn (vía APIs de redes sociales o herramientas de social listening), notificaciones en tiempo real o monitorización periódica |
| **Decisión** | El LLM analiza el sentimiento de cada mención (positivo, negativo, neutro), clasifica la urgencia (mención casual vs. crisis potencial), determina si requiere respuesta y genera un borrador de respuesta adaptado al tono de la marca |
| **Acción** | Guardar la mención y su análisis en una base de datos, enviar borrador de respuesta al community manager vía Slack, alertar al equipo de crisis si el sentimiento es muy negativo, generar informe semanal de menciones |

### Escenario D: Agente Educativo (Tutor IA)

| Componente | Descripción |
|------------|-------------|
| **Percepción** | Pregunta del estudiante vía chat, historial de preguntas anteriores del mismo estudiante, materiales del curso (apuntes, presentaciones, ejercicios) |
| **Decisión** | El LLM interpreta la duda del estudiante, identifica el tema y el nivel de comprensión, busca en los materiales del curso la información relevante y genera una explicación adaptada al nivel del estudiante. Decide si recomendar recursos adicionales o sugerir tutoría presencial |
| **Acción** | Responder con una explicación personalizada, compartir enlaces a recursos específicos (vídeos, capítulos del libro, ejercicios), registrar la interacción para seguimiento del profesor, enviar alerta al profesor si detecta dificultades recurrentes |

### Respuestas a las preguntas de reflexión

1. El Escenario C (Marketing) tiene la percepción más compleja porque necesita monitorizar múltiples fuentes de datos en tiempo real (varias redes sociales), procesar diferentes formatos (texto, imágenes, vídeos) y gestionar un flujo continuo de información. Esto requiere múltiples integraciones y un sistema de filtrado para evitar sobrecarga.

2. Para el escalado a humano, es mejor pecar de cauteloso al principio e ir calibrando con el tiempo. Un agente que resuelve incorrectamente un caso daña la confianza del cliente y la marca. Criterios progresivos: empezar escalando todo lo que no sea consulta directa de pedido, y gradualmente ampliar la autonomía del agente conforme se valida su rendimiento.

3. Los CVs (Escenario B) tienen estructura semi-predecible (secciones de experiencia, formación, etc.), lo que facilita la extracción de información. Las redes sociales (Escenario C) son texto completamente libre, con jerga, ironía, emojis y contexto cultural que dificultan el análisis de sentimiento. El componente de decisión en C necesita mayor sofisticación lingüística.

4. Respuesta abierta. El Escenario A suele ser la mejor opción para empezar: la percepción es clara (mensajes de chat), las acciones son acotadas (consultar pedido, responder) y el valor de negocio es inmediato (reducción de carga del equipo de soporte). El riesgo es moderado si se implementa escalado a humano.

</details>

<details>
<summary>Ver solución Ejercicio 2 - Comparativa de Plataformas</summary>

### Parte A: Tabla de Evaluación

| Criterio | n8n | Make | Zapier | Peso |
|----------|-----|------|--------|------|
| Coste (menor es mejor) | 5 | 3 | 2 | Alta (x3) |
| Facilidad de uso | 3 | 4 | 5 | Media (x2) |
| Integración con WhatsApp | 4 | 4 | 4 | Alta (x3) |
| Capacidades de IA nativas | 5 | 3 | 3 | Alta (x3) |
| Despliegue on-premise | 5 | 1 | 1 | Muy Alta (x4) |
| Número de integraciones | 3 | 4 | 5 | Media (x2) |
| Soporte de la comunidad | 4 | 3 | 4 | Baja (x1) |
| Escalabilidad | 4 | 4 | 3 | Media (x2) |

**Total ponderado:**
- **n8n**: 5x3 + 3x2 + 4x3 + 5x3 + 5x4 + 3x2 + 4x1 + 4x2 = 15+6+12+15+20+6+4+8 = **86**
- **Make**: 3x3 + 4x2 + 4x3 + 3x3 + 1x4 + 4x2 + 3x1 + 4x2 = 9+8+12+9+4+8+3+8 = **61**
- **Zapier**: 2x3 + 5x2 + 4x3 + 3x3 + 1x4 + 5x2 + 4x1 + 3x2 = 6+10+12+9+4+10+4+6 = **61**

### Parte B: Justificación

1. **Plataforma recomendada**: n8n. Gana en los criterios más ponderados: despliegue on-premise (imprescindible para datos sanitarios), coste (clínica con presupuesto limitado) y capacidades de IA nativas (agente para FAQ).

2. **Factor determinante**: El despliegue on-premise. Si la normativa sanitaria no exigiera control de datos, Make o Zapier podrían ser opciones viables. Sin este criterio, el resultado sería más equilibrado.

3. **Trade-offs de n8n**: Menor número de integraciones predefinidas (pero se puede suplir con HTTP Request), curva de aprendizaje mayor que Zapier (mitigable con templates y documentación), y necesidad de mantener la infraestructura propia (mitigable con Docker y backups automatizados).

### Parte C: Escenario Alternativo

Para la tienda de ropa online, **Zapier** sería la mejor opción: no hay requisitos de privacidad de datos sensibles, la integración con Instagram es nativa y robusta, la facilidad de uso reduce el tiempo de implementación, y el equipo de marketing probablemente no tiene perfil técnico para mantener una instancia de n8n.

</details>

<details>
<summary>Ver solución Ejercicio 4 - Diseño de Automatización con Schedule Trigger</summary>

### Parte A: Diagrama de Nodos

```
Nodo 1: [Schedule Trigger]
   ├── Tipo: Schedule Trigger
   ├── Configuración: Lunes a Viernes, 8:00 AM, Europe/Madrid
   ├── Entrada: Ninguna
   └── Salida: { timestamp: "2026-02-21T08:00:00.000Z" }

Nodo 2: [HTTP Request - NewsAPI]
   ├── Tipo: HTTP Request
   ├── Configuración: GET https://newsapi.org/v2/everything?q=artificial+intelligence&language=es&sortBy=publishedAt&pageSize=10
   ├── Entrada: Timestamp del trigger
   └── Salida: Array de artículos con título, descripción, URL, fuente

Nodo 3: [IF - ¿Hay noticias?]
   ├── Tipo: IF
   ├── Configuración: {{ $json.totalResults }} is greater than 0
   ├── Entrada: Respuesta de NewsAPI
   └── Salida: true (hay noticias) / false (no hay noticias)

Nodo 4: [OpenAI - Generar Resumen]
   ├── Tipo: HTTP Request (POST a OpenAI API)
   ├── Configuración: Model gpt-4o-mini, System prompt con instrucciones de resumen
   ├── Entrada: Array de artículos filtrados
   └── Salida: Texto del resumen en formato HTML/Markdown

Nodo 5: [Gmail - Enviar Resumen]
   ├── Tipo: Gmail
   ├── Configuración: To: equipo@empresa.com, Subject: "Resumen IA - {{ $now.format('dd/MM/yyyy') }}"
   ├── Entrada: Texto del resumen generado
   └── Salida: Confirmación de envío
```

### Parte B: Configuración del Schedule Trigger

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| Trigger Times → Rule | Cron Expression | Permite especificar días y hora exacta |
| Expresión Cron | `0 8 * * 1-5` | Minuto 0, hora 8, cualquier día del mes, cualquier mes, lunes(1) a viernes(5) |
| Zona horaria | Europe/Madrid | Para que las 8:00 sean hora local española |

Si el servidor está apagado a las 8:00, n8n NO ejecutará el workflow retroactivamente cuando vuelva a estar online (por defecto). Las ejecuciones perdidas se pierden. Para mitigar esto, es recomendable monitorizar la disponibilidad del servidor y/o configurar alertas.

### Parte C: HTTP Request

| Parámetro | Valor |
|-----------|-------|
| `q` | `"artificial intelligence" OR "inteligencia artificial" OR "AI agents"` |
| `language` | `es` |
| `sortBy` | `publishedAt` |
| `pageSize` | `10` |

Usar `$credentials` es fundamental porque: (1) la API key se almacena cifrada en n8n, (2) no se expone al exportar el workflow, (3) se puede revocar y actualizar sin modificar el workflow, y (4) se puede compartir entre múltiples workflows.

### Parte D: System Prompt

```
Eres un asistente especializado en resumir noticias de inteligencia artificial para un equipo técnico.

Genera un resumen diario con las siguientes características:
- Título: "Resumen de IA - [fecha de hoy]"
- Incluye entre 3 y 5 noticias destacadas
- Para cada noticia incluye: título, fuente, resumen de 2-3 frases y enlace original
- Organiza las noticias por relevancia (de mayor a menor impacto)
- Al final, incluye una sección "Tendencia del día" con una reflexión breve sobre el tema dominante
- Escribe en español, con tono profesional e informativo
- Usa formato HTML para que el email se vea bien formateado
- Longitud total: máximo 500 palabras
```

</details>

<details>
<summary>Ver solución Ejercicio 5 - Configuración de Credenciales</summary>

### Respuestas a las preguntas de reflexión

1. **Nodo nativo vs HTTP Request**: El nodo nativo de OpenAI abstrae la complejidad de la API (no necesitas recordar la URL, los headers ni el formato del body). Es más rápido de configurar y menos propenso a errores. Sin embargo, el HTTP Request ofrece más control: puedes acceder a endpoints que el nodo nativo no soporta, personalizar headers, usar modelos de otros proveedores con API compatible (ej: modelos locales con API OpenAI-compatible), y depurar más fácilmente viendo la petición y respuesta completas.

2. **Exportación de workflows**: Al exportar un workflow como JSON, las credenciales NO se incluyen (por seguridad). Solo se incluye una referencia al nombre de la credencial. El destinatario deberá configurar sus propias credenciales con el mismo nombre o remapearlas al importar. Esto es un diseño intencional para evitar fugas de API keys.

3. **Claude en lugar de OpenAI**: Para usar Claude (Anthropic), necesitarías: (a) crear credenciales de tipo "Anthropic" o "HTTP Header Auth" en n8n, (b) cambiar la URL del endpoint a `https://api.anthropic.com/v1/messages`, (c) ajustar el formato del body (Anthropic usa un formato diferente al de OpenAI), y (d) cambiar el header de autenticación a `x-api-key`. n8n soporta múltiples proveedores de IA de forma nativa: OpenAI, Anthropic, Google (Gemini), Ollama (modelos locales), Hugging Face, entre otros.

</details>

<details>
<summary>Ver solución Ejercicio 6 - Exploración de Templates</summary>

### Nota sobre los Templates

Los templates de n8n se actualizan frecuentemente, por lo que los resultados exactos de búsqueda pueden variar. A continuación se muestra un ejemplo representativo de lo que podrías encontrar:

### Ejemplos de Templates Relevantes para Agentes de IA

**Template 1: AI Agent Chat**

| Aspecto | Descripción |
|---------|-------------|
| Nombre del template | AI Agent Chat |
| Descripción breve | Un agente conversacional con memoria que puede mantener conversaciones multi-turno |
| Nodos que utiliza | Chat Trigger, AI Agent, OpenAI Chat Model, Window Buffer Memory |
| ¿Usa nodo AI Agent? | Sí |
| ¿Incluye memoria? | Sí (Window Buffer Memory) |
| ¿Qué herramientas usa? | Ninguna adicional (solo conversación) |
| ¿Qué trigger lo inicia? | Chat Trigger (interfaz de chat embebida) |
| Complejidad estimada | Baja |

**Template 2: AI Agent with Tools**

| Aspecto | Descripción |
|---------|-------------|
| Nombre del template | AI Agent with Custom Tools |
| Descripción breve | Agente que puede buscar en internet, hacer cálculos y consultar APIs externas |
| Nodos que utiliza | Chat Trigger, AI Agent, OpenAI Chat Model, SerpAPI Tool, Calculator Tool, HTTP Request Tool |
| ¿Usa nodo AI Agent? | Sí |
| ¿Incluye memoria? | Sí |
| ¿Qué herramientas usa? | SerpAPI (búsqueda web), Calculator, HTTP Request |
| ¿Qué trigger lo inicia? | Chat Trigger |
| Complejidad estimada | Media |

**Template 3: Customer Support Agent**

| Aspecto | Descripción |
|---------|-------------|
| Nombre del template | Customer Support AI Agent |
| Descripción breve | Agente de soporte al cliente que consulta una base de conocimiento y puede escalar tickets |
| Nodos que utiliza | Webhook Trigger, AI Agent, OpenAI Chat Model, Postgres (memoria), Vector Store Tool |
| ¿Usa nodo AI Agent? | Sí |
| ¿Incluye memoria? | Sí (PostgreSQL para persistencia) |
| ¿Qué herramientas usa? | Vector Store (búsqueda semántica en documentos), Webhook (para integraciones) |
| ¿Qué trigger lo inicia? | Webhook Trigger |
| Complejidad estimada | Alta |

### Parte C: Patrones Observados

1. **Patrón común**: Todos usan el nodo AI Agent + un modelo de chat (OpenAI Chat Model es el más frecuente) + alguna forma de trigger. El patrón recurrente es: `Trigger → AI Agent (con modelo + memoria + herramientas)`.

2. **Trigger más frecuente**: El Chat Trigger es el más utilizado en templates de agentes de IA, porque la mayoría de los agentes están diseñados para interacción conversacional. Para integraciones en producción, se usan Webhook Triggers.

3. **Tipos de memoria**: Window Buffer Memory es la opción más simple (almacena los últimos N mensajes en memoria del proceso). PostgreSQL o Supabase proporcionan persistencia entre ejecuciones. La elección depende de si el agente necesita recordar conversaciones entre sesiones (persistente) o solo dentro de una conversación activa (buffer).

</details>
