# Ejercicios Prácticos - Unidad 5, Sesión 1
## Fundamentos de RAG: Embeddings, Vectores y Chunking

---

## Ejercicio 1: Análisis Conceptual de una Arquitectura RAG

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Análisis
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de la sección 5.1 sobre introducción a RAG y sus componentes principales

### Contexto
Retrieval-Augmented Generation (RAG) combina la capacidad generativa de los LLMs con la recuperación de información de fuentes externas para producir respuestas fundamentadas en datos reales. Antes de implementar un sistema RAG, es fundamental saber diseñar su arquitectura: elegir las fuentes de datos, la estrategia de chunking, el modelo de embeddings y la base de datos vectorial adecuada para cada caso de uso. Este ejercicio entrena la capacidad de tomar decisiones de diseño informadas.

### Objetivo de Aprendizaje
- Comprender los componentes fundamentales de un pipeline RAG
- Identificar las decisiones de diseño clave en cada etapa del pipeline
- Evaluar qué tecnologías y configuraciones son más adecuadas según el contexto
- Desarrollar pensamiento crítico sobre las limitaciones de RAG frente a fine-tuning

### Enunciado

Para cada uno de los siguientes escenarios empresariales, diseña la arquitectura RAG completando la tabla con las decisiones técnicas que tomarías. Justifica brevemente cada elección.

### Escenario A: Asistente Legal para un Despacho de Abogados

Un despacho de abogados con 15 años de actividad quiere un asistente que responda preguntas sobre jurisprudencia, legislación vigente y documentos internos (contratos, dictámenes). Los documentos incluyen PDFs escaneados, documentos Word y bases de datos de sentencias.

| Componente | Tu decisión | Justificación |
|------------|-------------|---------------|
| **Fuentes de datos** | PDFs escaneados, documentos Word, bases de datos de sentencias, legislación vigente | Cubrir todas las fuentes mencionadas para tener información completa del despacho |
| **Preprocesamiento necesario** | OCR para PDFs escaneados (Tesseract/Azure Document Intelligence), conversión Word a texto, limpieza y normalización de texto legal | Los PDFs escaneados requieren OCR para extraer texto; los documentos Word necesitan conversión; el texto legal suele tener formatos específicos que requieren normalización |
| **Estrategia de chunking** | Chunking semántico por secciones legales (artículos, cláusulas, párrafos) con RecursiveCharacterTextSplitter | Los documentos legales tienen estructura jerárquica clara; es importante no cortar artículos o cláusulas a mitad |
| **Tamaño de chunk recomendado** | 500-800 caracteres con overlap de 100-150 | Los textos legales son densos y requieren contexto suficiente para ser interpretados correctamente |
| **Modelo de embeddings** | Modelo local como multilingual-e5-large o modelo on-premise | Por confidencialidad de documentos legales, evitar enviar datos a APIs externas |
| **Base de datos vectorial** | Weaviate o pgvector (on-premise) | Necesidad de mantener datos confidenciales en infraestructura propia; pgvector si ya usan PostgreSQL |
| **Número de chunks a recuperar (top-k)** | 5-7 chunks | Balance entre contexto suficiente y evitar ruido; documentos legales requieren precisión |
| **LLM para generación** | Modelo local (Llama 3, Mistral) o API con acuerdo de confidencialidad (Claude/GPT con Enterprise) | Protección de datos confidenciales; si usan cloud, necesitan acuerdos DPA |

### Escenario B: FAQ Inteligente para una Universidad

La universidad U-TAD quiere que los estudiantes puedan hacer preguntas sobre normativas académicas, planes de estudio, horarios, convocatorias de exámenes y servicios del campus. La información está en la web institucional, PDFs de normativa y documentos de Moodle.

| Componente | Tu decisión | Justificación |
|------------|-------------|---------------|
| **Fuentes de datos** | Web institucional (scraping), PDFs de normativa, documentos de Moodle exportados | Cubrir todas las fuentes de información estudiantil |
| **Estrategia de chunking** | RecursiveCharacterTextSplitter con separadores por secciones y preguntas-respuestas | Los FAQ y normativas tienen estructura clara de pregunta-respuesta o artículos |
| **Modelo de embeddings** | text-embedding-3-small de OpenAI o all-MiniLM-L6-v2 (sentence-transformers) | Coste-efectivo para volumen moderado; información no es confidencial |
| **Base de datos vectorial** | ChromaDB o Pinecone (tier gratuito) | Fácil de implementar, bajo coste, escalabilidad suficiente para el volumen de una universidad |
| **LLM para generación** | GPT-4o-mini o Claude Haiku | Buena relación calidad-precio para respuestas directas; no requiere razonamiento complejo |

### Escenario C: Soporte Técnico para Documentación de Software

Una empresa SaaS con documentación técnica extensa (API reference, tutoriales, guías de migración, changelogs) quiere un chatbot que responda consultas técnicas de desarrolladores. La documentación se actualiza semanalmente.

| Componente | Tu decisión | Justificación |
|------------|-------------|---------------|
| **Fuentes de datos** | Documentación API (OpenAPI specs), tutoriales Markdown, guías de migración, changelogs en Git | Documentación técnica típica de SaaS; mantener actualizada desde el repositorio |
| **Estrategia de chunking** | MarkdownHeaderTextSplitter combinado con chunking por código | Preservar estructura de documentación técnica; separar bloques de código de explicaciones |
| **Frecuencia de reindexación** | Semanal (sincronizado con actualizaciones de documentación) + webhook en merge a main | La documentación se actualiza semanalmente; triggers automáticos aseguran sincronización |
| **Modelo de embeddings** | text-embedding-3-small o CodeBERT para secciones de código | Balance entre coste y calidad; CodeBERT mejora embeddings de código |
| **Base de datos vectorial** | Pinecone o Weaviate Cloud | Escalabilidad cloud, bajo mantenimiento DevOps, buena integración con pipelines CI/CD |
| **Estrategia de búsqueda** | Híbrida (vectorial + keyword BM25) | La búsqueda de documentación técnica se beneficia de términos exactos (nombres de funciones, errores) combinados con similitud semántica |

### Preguntas de Reflexión

1. **RAG vs. Fine-tuning**: En el Escenario A, el despacho se plantea si sería mejor hacer fine-tuning de un modelo con todos sus documentos en lugar de usar RAG. ¿Qué le recomendarías y por qué? Considera aspectos como actualización de datos, alucinaciones, coste y trazabilidad de las respuestas.

**Respuesta:** Recomendaría **RAG** sobre fine-tuning por las siguientes razones:
- **Actualización de datos**: RAG permite actualizar la base de conocimiento sin reentrenar el modelo. Los documentos legales (nueva jurisprudencia, cambios legislativos) se pueden añadir de forma incremental.
- **Alucinaciones**: RAG ancla las respuestas en documentos reales, permitiendo citar fuentes específicas. El fine-tuning no garantiza fidelidad a documentos específicos.
- **Coste**: El fine-tuning de un modelo grande es costoso y debe repetirse con cada actualización significativa. RAG solo requiere reindexar documentos nuevos.
- **Trazabilidad**: RAG puede mostrar qué documentos se usaron para cada respuesta, crítico en contexto legal para verificación y auditoría.

2. **Privacidad**: El Escenario A maneja documentos legales confidenciales. ¿Cómo afecta esto a la elección de modelo de embeddings y LLM? ¿Usarías APIs en la nube o modelos locales?

**Respuesta:** La confidencialidad afecta significativamente la arquitectura:
- **Modelo de embeddings**: Usar modelos locales (sentence-transformers, multilingual-e5) que se ejecuten on-premise, evitando enviar texto a APIs externas.
- **LLM**: Optar por modelos locales (Llama 3, Mistral 7B) o, si se necesita mayor capacidad, APIs enterprise con acuerdos de confidencialidad (DPA) como Claude Enterprise o Azure OpenAI.
- **Recomendación**: Modelos locales para máxima privacidad, aceptando trade-off en calidad/velocidad.

3. **Escalabilidad**: Si el Escenario C pasa de 1.000 a 100.000 documentos, ¿qué componentes de tu arquitectura necesitarían cambiar?

**Respuesta:** Los cambios necesarios serían:
- **Base de datos vectorial**: Migrar de solución en memoria a cluster distribuido (Pinecone tier superior, Weaviate cluster, Milvus distribuido).
- **Índices**: Usar algoritmos ANN más eficientes (HNSW con parámetros optimizados, IVF con más centroides).
- **Reindexación**: Implementar indexación incremental en lugar de reindexar todo; pipeline de procesamiento paralelo.
- **Caché**: Añadir capa de caché para queries frecuentes.
- **Infraestructura**: Posiblemente sharding de datos y réplicas para disponibilidad.

---

## Ejercicio 2: Experimentación con Embeddings y Similitud Semántica

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Programación
- **Modalidad**: Individual
- **Dificultad**: Intermedia
- **Prerequisitos**: Lectura de la sección 5.2 sobre embeddings y espacios vectoriales, conocimientos básicos de Python y numpy

### Contexto
Los embeddings son representaciones numéricas densas de texto que capturan su significado semántico. La calidad de un sistema RAG depende directamente de la calidad de sus embeddings: si frases con significado similar no producen vectores cercanos, la recuperación fallará. Este ejercicio permite experimentar de primera mano con embeddings, entender la similitud coseno y descubrir tanto las capacidades como las limitaciones de estos modelos.

### Objetivo de Aprendizaje
- Generar embeddings usando la API de OpenAI o sentence-transformers
- Calcular e interpretar la similitud coseno entre vectores
- Identificar patrones: sinonimia, paráfrasis, negación, cambio de idioma
- Comprender las limitaciones de los embeddings para ciertos tipos de relaciones semánticas

### Enunciado

Escribe un programa en Python que genere embeddings para un conjunto de frases y analice las relaciones semánticas entre ellas mediante similitud coseno.

### Paso 1: Configuración del entorno

Elige **una** de las dos opciones:

**Opción A: OpenAI API** (requiere API key)
```python
from openai import OpenAI
import numpy as np

client = OpenAI()  # Usa OPENAI_API_KEY del entorno

def get_embedding(text, model="text-embedding-3-small"):
    """Genera el embedding de un texto usando OpenAI."""
    response = client.embeddings.create(
        input=text,
        model=model
    )
    return np.array(response.data[0].embedding)
```

**Opción B: Sentence-Transformers** (local, gratuito)
```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text, model=model):
    """Genera el embedding de un texto usando sentence-transformers."""
    return model.encode(text)
```

### Paso 2: Definir las frases de prueba

Usa el siguiente conjunto de frases diseñado para explorar diferentes relaciones semánticas:

```python
frases = {
    # Grupo 1: Frases semánticamente similares (paráfrasis)
    "A1": "El gato se sentó en la alfombra",
    "A2": "Un felino descansaba sobre el tapete",
    "A3": "The cat sat on the mat",  # Misma idea, otro idioma

    # Grupo 2: Frases sobre tecnología
    "B1": "Python es un lenguaje de programación muy popular",
    "B2": "JavaScript se usa mucho para desarrollo web",
    "B3": "Los lenguajes de programación son herramientas esenciales",

    # Grupo 3: Negación y contraste
    "C1": "El restaurante tiene buena comida",
    "C2": "El restaurante no tiene buena comida",
    "C3": "La comida del restaurante es terrible",

    # Grupo 4: Frases sin relación
    "D1": "La fotosíntesis convierte luz solar en energía",
    "D2": "El precio del petróleo subió un 5% ayer",
}
```

### Paso 3: Generar embeddings y calcular similitudes

```python
from numpy import dot
from numpy.linalg import norm

def cosine_similarity(a, b):
    """Calcula la similitud coseno entre dos vectores."""
    return dot(a, b) / (norm(a) * norm(b))

# Generar embeddings para todas las frases
embeddings = {}
for key, frase in frases.items():
    embeddings[key] = get_embedding(frase)
    print(f"[{key}] Embedding generado - dimensiones: {len(embeddings[key])}")

# Calcular matriz de similitudes
print("\n--- MATRIZ DE SIMILITUD COSENO ---\n")
keys = list(frases.keys())
print(f"{'':>4}", end="")
for k in keys:
    print(f"{k:>8}", end="")
print()

for i, ki in enumerate(keys):
    print(f"{ki:>4}", end="")
    for j, kj in enumerate(keys):
        sim = cosine_similarity(embeddings[ki], embeddings[kj])
        print(f"{sim:>8.3f}", end="")
    print()
```

### Paso 4: Análisis de resultados

Responde a las siguientes preguntas basándote en los resultados obtenidos:

| Pregunta | Tu respuesta |
|----------|-------------|
| 1. ¿Cuál es la similitud entre A1 y A2 (paráfrasis en español)? ¿Es alta? | **0.4864** - Es moderada-alta. El modelo captura que ambas frases expresan ideas similares (gato/felino, alfombra/tapete), aunque no perfectamente. |
| 2. ¿Cuál es la similitud entre A1 y A3 (misma idea, diferente idioma)? ¿Es comparable a A1-A2? | **0.0107** - Sorprendentemente BAJA. El modelo all-MiniLM-L6-v2 no captura bien la equivalencia cross-lingual entre español e inglés, a diferencia de modelos multilingües específicos. |
| 3. ¿Los embeddings de B1, B2 y B3 forman un grupo coherente? ¿Son más similares entre sí que con otros grupos? | Sí, forman un grupo coherente: B1-B2=0.24, B1-B3=0.52, B2-B3=0.21. Son más similares entre sí que con grupos A, C y D, indicando que comparten el dominio de programación/tecnología. |
| 4. ¿Cuál es la similitud entre C1 ("buena comida") y C2 ("no tiene buena comida")? ¿Es sorprendentemente alta o baja? | **0.9696** - Es SORPRENDENTEMENTE ALTA. Aunque semánticamente son opuestas, el modelo las considera casi idénticas porque comparten las mismas palabras. |
| 5. ¿Los embeddings capturan bien la negación? Compara C1-C2 vs C1-C3. ¿Cuál debería ser más diferente semánticamente? | NO capturan bien la negación. C1-C2=0.97, C1-C3=0.75, C2-C3=0.76. Semánticamente C2 y C3 expresan lo mismo (comida mala) pero tienen similitud moderada. La negación añade "no" pero el embedding apenas cambia. Esta es una limitación conocida de los embeddings. |
| 6. ¿Las frases D1 y D2 tienen baja similitud con el resto de grupos, como esperarías? | D1-D2=0.18, que es baja como esperado. Ambas tienen similitudes bajas con otros grupos (D1-A1=0.29, D1-B1=0.07), confirmando que pertenecen a dominios semánticos distintos. |
| 7. ¿Cuál es la dimensionalidad de los embeddings generados? ¿Qué modelo usaste? | **384 dimensiones** con el modelo **all-MiniLM-L6-v2** de sentence-transformers (opción local y gratuita). |

### Paso 5 (Bonus): Visualización

Si tienes tiempo, añade una visualización 2D usando PCA o t-SNE:

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Reducir a 2D
vectors = np.array(list(embeddings.values()))
pca = PCA(n_components=2)
coords = pca.fit_transform(vectors)

# Graficar
plt.figure(figsize=(10, 8))
colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'orange'}
for i, key in enumerate(keys):
    grupo = key[0]
    plt.scatter(coords[i, 0], coords[i, 1], c=colors[grupo], s=100, zorder=5)
    plt.annotate(f"{key}: {frases[key][:30]}...",
                 (coords[i, 0], coords[i, 1]),
                 fontsize=8, ha='left', va='bottom')

plt.title("Embeddings proyectados en 2D (PCA)")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("embeddings_2d.png", dpi=150)
plt.show()
```

### Extensión (Opcional)

- Compara los resultados usando `text-embedding-3-small` vs `text-embedding-3-large` de OpenAI. ¿El modelo más grande captura mejor la negación?
- Añade frases en un tercer idioma (francés, alemán) y observa si se agrupan con sus equivalentes semánticos
- Experimenta con el parámetro `dimensions` de OpenAI para reducir la dimensionalidad del embedding y observa cómo afecta a las similitudes

---

## Ejercicio 3: Comparativa de Bases de Datos Vectoriales

### Metadata
- **Duración estimada**: 25 minutos
- **Tipo**: Exploración/Análisis
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de la sección 5.3 sobre bases de datos vectoriales

### Contexto
La elección de la base de datos vectorial es una de las decisiones arquitectónicas más importantes en un sistema RAG. No existe una opción universalmente mejor: la elección depende de factores como el volumen de datos, la necesidad de persistencia, el presupuesto, si se requiere búsqueda híbrida (vectorial + texto) y el nivel de experiencia del equipo. Este ejercicio te prepara para tomar esta decisión de forma informada en proyectos reales.

### Objetivo de Aprendizaje
- Conocer las principales bases de datos vectoriales del mercado
- Comparar sus características técnicas, modelos de pricing y casos de uso
- Evaluar qué solución es más adecuada según diferentes escenarios
- Distinguir entre soluciones locales, cloud-native y bases de datos tradicionales con extensiones vectoriales

### Enunciado

Investiga las siguientes bases de datos vectoriales y completa la tabla comparativa. Puedes usar la documentación oficial de cada una, artículos técnicos y los materiales de la asignatura.

### Parte 1: Tabla Comparativa

Completa la siguiente tabla para cada base de datos vectorial:

| Criterio | **FAISS** | **ChromaDB** | **Pinecone** | **Weaviate** | **pgvector** |
|----------|-----------|-------------|-------------|-------------|-------------|
| **Tipo** (librería / BD embebida / servicio cloud / extensión) | Librería | BD embebida | Servicio cloud | BD vectorial (self-hosted/cloud) | Extensión PostgreSQL |
| **Desarrollador** | Meta (Facebook) | Chroma Inc. | Pinecone Systems | Weaviate BV | Supabase / comunidad |
| **Lenguaje principal** | C++ (bindings Python) | Python | Managed (API REST/SDKs) | Go | C (PostgreSQL) |
| **Persistencia** (en memoria / disco / cloud) | En memoria / disco | Disco (SQLite) / memoria | Cloud (managed) | Disco / cloud | Disco (PostgreSQL) |
| **Coste** (gratuito / freemium / pago) | Gratuito (open source) | Gratuito (open source) | Freemium (tier gratuito limitado) | Gratuito self-hosted / pago cloud | Gratuito (open source) |
| **Escalabilidad** (prototipo / producción pequeña / enterprise) | Prototipo a producción (requiere gestión) | Prototipo / producción pequeña | Enterprise (auto-scaling) | Prototipo a enterprise | Producción (escala con PostgreSQL) |
| **Búsqueda híbrida** (vectorial + keyword) | No nativo | Sí (desde v0.4) | Sí | Sí (BM25 + vectorial) | No nativo (requiere extensión FTS) |
| **Filtrado por metadatos** | Manual (pre/post filtrado) | Sí | Sí | Sí | Sí (SQL WHERE) |
| **Integración con LangChain** | Sí | Sí (muy buena) | Sí | Sí | Sí |
| **Requiere infraestructura propia** | Sí | No (embebido) / Sí para servidor | No (managed) | Sí para self-hosted / No para cloud | Sí (necesita PostgreSQL) |
| **Curva de aprendizaje** (baja / media / alta) | Media-Alta | Baja | Baja | Media | Baja (si conoces SQL) |
| **Caso de uso ideal** | Prototipado rápido, investigación, alta performance local | Prototipos, proyectos pequeños-medianos, desarrollo local | Producción enterprise sin DevOps, startups que escalan | Producción con búsqueda híbrida, GraphQL | Empresas que ya usan PostgreSQL |

### Parte 2: Decisiones de Diseño

Para cada escenario, elige la base de datos vectorial más adecuada y justifica tu decisión:

**Escenario 1**: Un estudiante quiere hacer un prototipo rápido de RAG para un proyecto de clase, con ~100 documentos PDF.
- Base de datos elegida: **ChromaDB**
- Justificación: Es la opción más sencilla para prototipos. Se instala con `pip install chromadb`, no requiere infraestructura externa, persiste datos localmente, y tiene excelente integración con LangChain. Para ~100 documentos el rendimiento es más que suficiente.

**Escenario 2**: Una startup necesita un sistema RAG en producción que maneje 500.000 documentos y escale automáticamente, sin dedicar DevOps al mantenimiento.
- Base de datos elegida: **Pinecone**
- Justificación: Es un servicio 100% managed que escala automáticamente sin necesidad de DevOps. Soporta búsqueda híbrida, filtrado por metadatos, y tiene SLAs de producción. El coste se justifica por el ahorro en personal de infraestructura.

**Escenario 3**: Un banco necesita un sistema RAG para documentos financieros confidenciales. Todo debe ejecutarse on-premise por regulación. Tienen equipo de infraestructura.
- Base de datos elegida: **Weaviate (self-hosted) o pgvector**
- Justificación: Weaviate self-hosted permite deployment on-premise con todas las funcionalidades enterprise (búsqueda híbrida, filtrado). Si ya usan PostgreSQL, pgvector es una opción más simple que no introduce nueva tecnología. Ambas opciones mantienen los datos 100% on-premise cumpliendo regulaciones bancarias.

**Escenario 4**: Una empresa ya usa PostgreSQL para toda su infraestructura y quiere añadir capacidad de búsqueda semántica sin introducir una nueva tecnología.
- Base de datos elegida: **pgvector**
- Justificación: Se integra directamente en PostgreSQL existente como extensión. El equipo ya conoce SQL, no necesitan aprender nueva tecnología, y pueden combinar búsquedas vectoriales con queries SQL existentes. Aprovecha infraestructura, backups y monitoring ya configurados.

### Parte 3: Pregunta de Reflexión

¿Es posible empezar con ChromaDB para un prototipo y migrar después a Pinecone para producción? ¿Qué abstracción de LangChain facilita esta migración? ¿Qué cambios serían necesarios en el código?

**Respuesta:** Sí, es completamente posible y es un patrón común de desarrollo. La abstracción de LangChain que facilita esto es la clase **VectorStore** y la interfaz unificada. Tanto `Chroma` como `Pinecone` implementan la misma interfaz (`add_documents()`, `similarity_search()`, `as_retriever()`), permitiendo cambiar entre ellas con cambios mínimos.

**Cambios necesarios en el código:**
1. Cambiar la importación: de `from langchain_chroma import Chroma` a `from langchain_pinecone import PineconeVectorStore`
2. Cambiar la inicialización: configurar API key de Pinecone y nombre del índice en lugar de path local
3. Migrar los datos: re-indexar los documentos en Pinecone (no hay migración directa de datos)
4. El resto del código (retriever, chains) permanece igual gracias a la abstracción

### Extensión (Opcional)

- Instala ChromaDB localmente (`pip install chromadb`) e indexa 5-10 documentos de prueba. Experimenta con diferentes consultas y observa los resultados de similitud.
- Investiga Qdrant y Milvus como alternativas adicionales y añádelos a la tabla comparativa.

---

## Ejercicio 4: Laboratorio de Estrategias de Chunking

### Metadata
- **Duración estimada**: 35 minutos
- **Tipo**: Programación
- **Modalidad**: Individual
- **Dificultad**: Intermedia
- **Prerequisitos**: Lectura de la sección 5.4 sobre chunking, conocimientos de Python, familiaridad básica con LangChain

### Contexto
El chunking (fragmentación del texto) es una etapa crítica y a menudo subestimada en un pipeline RAG. Un chunking demasiado grande puede incluir información irrelevante que confunda al LLM; uno demasiado pequeño puede perder el contexto necesario para una respuesta coherente. El solapamiento (overlap) entre chunks permite que la información no se "corte" en medio de una idea. Este ejercicio te permite experimentar de primera mano con diferentes configuraciones y desarrollar intuición sobre sus efectos.

### Objetivo de Aprendizaje
- Usar `RecursiveCharacterTextSplitter` de LangChain con diferentes configuraciones
- Comprender el impacto del `chunk_size` y `chunk_overlap` en la fragmentación
- Analizar cuándo se pierde contexto y cuándo se preserva
- Desarrollar criterios para elegir la configuración óptima según el tipo de documento

### Enunciado

Experimenta con diferentes configuraciones de chunking sobre un documento de ejemplo y analiza los resultados.

### Paso 1: Preparar el documento de ejemplo

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Documento de ejemplo: artículo sobre inteligencia artificial
documento = """
# Introducción a la Inteligencia Artificial

La inteligencia artificial (IA) es una rama de la informática que busca crear sistemas
capaces de realizar tareas que normalmente requieren inteligencia humana. Estas tareas
incluyen el aprendizaje, el razonamiento, la percepción y la comprensión del lenguaje natural.

## Historia de la IA

El término "inteligencia artificial" fue acuñado por John McCarthy en 1956 durante la
conferencia de Dartmouth. Sin embargo, las ideas sobre máquinas pensantes se remontan a
mucho antes. Alan Turing, en 1950, propuso el famoso Test de Turing como criterio para
determinar si una máquina puede exhibir comportamiento inteligente indistinguible del humano.

Durante las décadas de 1960 y 1970, la IA experimentó un período de optimismo conocido
como la "edad de oro". Los investigadores creían que la IA general estaba a pocas décadas
de distancia. Sin embargo, las limitaciones computacionales y teóricas llevaron a los
"inviernos de la IA", períodos de reducción de financiación e interés.

## Aprendizaje Automático

El aprendizaje automático (machine learning) es un subcampo de la IA que se centra en
desarrollar algoritmos que permiten a las computadoras aprender de los datos sin ser
programadas explícitamente. Los tres paradigmas principales son:

1. Aprendizaje supervisado: el modelo aprende de ejemplos etiquetados.
2. Aprendizaje no supervisado: el modelo descubre patrones en datos sin etiquetar.
3. Aprendizaje por refuerzo: el modelo aprende mediante prueba y error con recompensas.

## Deep Learning

El deep learning o aprendizaje profundo utiliza redes neuronales con múltiples capas
(de ahí "profundo") para aprender representaciones jerárquicas de los datos. Las
arquitecturas más importantes incluyen:

- Redes Neuronales Convolucionales (CNN): especializadas en procesamiento de imágenes.
- Redes Neuronales Recurrentes (RNN): diseñadas para secuencias temporales.
- Transformers: la arquitectura dominante actual para procesamiento de lenguaje natural,
  introducida en el paper "Attention is All You Need" (2017).

## Modelos de Lenguaje

Los modelos de lenguaje grandes (LLMs) como GPT-4, Claude y Llama representan el estado
del arte en procesamiento de lenguaje natural. Estos modelos se entrenan con cantidades
masivas de texto y pueden generar texto coherente, traducir idiomas, resumir documentos
y responder preguntas.

La técnica de RAG (Retrieval-Augmented Generation) complementa estos modelos permitiéndoles
acceder a información externa actualizada, reduciendo las alucinaciones y proporcionando
respuestas más precisas y verificables.
"""

print(f"Longitud total del documento: {len(documento)} caracteres")
print(f"Número de líneas: {len(documento.splitlines())}")
```

### Paso 2: Experimentar con diferentes configuraciones

```python
configuraciones = [
    {"chunk_size": 100, "chunk_overlap": 0,  "nombre": "Muy pequeño, sin overlap"},
    {"chunk_size": 100, "chunk_overlap": 20, "nombre": "Muy pequeño, con overlap"},
    {"chunk_size": 300, "chunk_overlap": 0,  "nombre": "Mediano, sin overlap"},
    {"chunk_size": 300, "chunk_overlap": 50, "nombre": "Mediano, con overlap"},
    {"chunk_size": 500, "chunk_overlap": 50, "nombre": "Grande, con overlap pequeño"},
    {"chunk_size": 500, "chunk_overlap": 100,"nombre": "Grande, con overlap grande"},
    {"chunk_size": 1000,"chunk_overlap": 200,"nombre": "Muy grande, con overlap"},
]

for config in configuraciones:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config["chunk_size"],
        chunk_overlap=config["chunk_overlap"],
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = splitter.split_text(documento)

    print(f"\n{'='*70}")
    print(f"Configuración: {config['nombre']}")
    print(f"  chunk_size={config['chunk_size']}, chunk_overlap={config['chunk_overlap']}")
    print(f"  Número de chunks: {len(chunks)}")
    print(f"  Tamaño promedio: {sum(len(c) for c in chunks) / len(chunks):.0f} caracteres")
    print(f"  Tamaño mínimo: {min(len(c) for c in chunks)} caracteres")
    print(f"  Tamaño máximo: {max(len(c) for c in chunks)} caracteres")
    print(f"  Caracteres totales (con overlap): {sum(len(c) for c in chunks)}")

    # Mostrar los primeros 3 chunks
    for i, chunk in enumerate(chunks[:3]):
        print(f"\n  --- Chunk {i+1} ({len(chunk)} chars) ---")
        # Mostrar solo las primeras y últimas líneas
        lines = chunk.strip().split('\n')
        if len(lines) <= 4:
            print(f"  {chunk.strip()}")
        else:
            print(f"  {lines[0]}")
            print(f"  {lines[1]}")
            print(f"  ...")
            print(f"  {lines[-1]}")
```

### Paso 3: Análisis detallado del overlap

```python
# Analizar qué información se comparte entre chunks consecutivos
print("\n\n" + "="*70)
print("ANÁLISIS DE OVERLAP")
print("="*70)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""]
)
chunks = splitter.split_text(documento)

for i in range(len(chunks) - 1):
    chunk_actual = chunks[i]
    chunk_siguiente = chunks[i + 1]

    # Encontrar el texto solapado
    overlap_text = ""
    for length in range(min(len(chunk_actual), len(chunk_siguiente)), 0, -1):
        if chunk_actual.endswith(chunk_siguiente[:length]):
            overlap_text = chunk_siguiente[:length]
            break

    print(f"\nEntre Chunk {i+1} y Chunk {i+2}:")
    print(f"  Overlap encontrado ({len(overlap_text)} chars): \"{overlap_text[:80]}...\"" if len(overlap_text) > 80 else f"  Overlap encontrado ({len(overlap_text)} chars): \"{overlap_text}\"")
    print(f"  Final chunk {i+1}: \"...{chunk_actual[-50:]}\"")
    print(f"  Inicio chunk {i+2}: \"{chunk_siguiente[:50]}...\"")
```

### Paso 4: Tabla de análisis comparativo

Completa la siguiente tabla con los resultados de tus experimentos:

| Configuración | N. Chunks | Tam. Promedio | ¿Se cortan ideas a mitad? | ¿Hay redundancia excesiva? |
|--------------|-----------|---------------|---------------------------|---------------------------|
| 100, overlap 0 | 36 | 71 chars | Sí, 63.9% de chunks terminan abruptamente | No, sin redundancia |
| 100, overlap 20 | 36 | 71 chars | Sí, frecuentemente. El overlap ayuda poco con chunks tan pequeños | Poca (~20%) |
| 300, overlap 0 | 14 | 184 chars | Ocasionalmente, en transiciones de párrafo | No |
| 300, overlap 50 | 14 | 186 chars | Menos frecuente, overlap ayuda en transiciones | Moderada (~17%) |
| 500, overlap 50 | 8 | 333 chars | Raramente, chunks capturan secciones completas | Poca (~10%) |
| 500, overlap 100 | 8 | 333 chars | 37.5% de cortes abruptos - mejor que chunks pequeños | Moderada (~20%) |
| 1000, overlap 200 | 4 | 655 chars | No, cada chunk contiene secciones completas | Moderada (~20%) |

### Preguntas de Reflexión

1. ¿Con qué configuración se cortan más frases a mitad de una idea? ¿Por qué?

**Respuesta:** Con **chunk_size=100 y overlap=0**. El 63.9% de los chunks terminan abruptamente. Un tamaño tan pequeño (71 chars promedio) no permite que quepan párrafos o ideas completas. Las frases del documento tienen ~60-150 caracteres, por lo que frecuentemente se cortan a mitad. Sin overlap, no hay forma de recuperar el contexto perdido.

2. ¿Cuál es el trade-off entre chunk_size pequeño y grande para la calidad de la búsqueda?

**Respuesta:**
- **Chunk pequeño**: Mayor precisión en la recuperación (se recupera exactamente la información relevante), pero pérdida de contexto, frases cortadas, y el LLM puede no entender el chunk aislado.
- **Chunk grande**: Preserva contexto completo e ideas coherentes, pero puede incluir información irrelevante, menos precisión semántica, y consume más tokens del contexto del LLM.

3. ¿Por qué `RecursiveCharacterTextSplitter` usa una jerarquía de separadores (`\n\n`, `\n`, `. `, ` `)? ¿Qué pasaría si solo usara un separador?

**Respuesta:** Usa jerarquía para cortar en los puntos más naturales primero: `\n\n` (párrafos) > `\n` (líneas) > `. ` (oraciones) > ` ` (palabras) > `""` (caracteres). Si solo usara un separador (ej. espacio), los cortes serían más arbitrarios y se perderían las divisiones naturales del texto como párrafos y secciones.

4. Si tu documento fuera código fuente Python en lugar de texto, ¿cambiarías los separadores? ¿Cuáles usarías?

**Respuesta:** Sí, para código Python usaría separadores específicos:
```python
separators=["\nclass ", "\ndef ", "\n\n", "\n", " ", ""]
```
O mejor aún, usar un splitter específico para código como `PythonCodeTextSplitter` de LangChain que entiende la estructura del código.

5. ¿Qué configuración elegirías para un documento legal con párrafos largos y densos? ¿Y para un FAQ con preguntas y respuestas cortas?

**Respuesta:**
- **Documento legal**: chunk_size=800-1000, overlap=150-200. Los artículos legales suelen ser largos y autónomos; necesitan contexto para interpretarse correctamente.
- **FAQ**: chunk_size=200-300, overlap=0-50. Cada par pregunta-respuesta es una unidad semántica independiente; chunks pequeños son suficientes y mejoran la precisión de búsqueda.

### Extensión (Opcional)

- Prueba `MarkdownHeaderTextSplitter` de LangChain, que divide por encabezados Markdown preservando la jerarquía. Compara los resultados con `RecursiveCharacterTextSplitter` sobre el mismo documento.
- Implementa un splitter personalizado que divida por secciones (`##`) y mantenga el título de sección como metadato de cada chunk.

---

## Ejercicio 5: Diseño de un Pipeline RAG Completo

### Metadata
- **Duración estimada**: 25 minutos
- **Tipo**: Diseño
- **Modalidad**: Grupal (2-3 personas)
- **Dificultad**: Intermedia
- **Prerequisitos**: Lectura completa de las secciones 5.1 a 5.4, comprensión de los ejercicios anteriores

### Contexto
Diseñar un sistema RAG completo requiere tomar decisiones coordinadas en cada etapa del pipeline: desde la ingesta y preprocesamiento de documentos, pasando por el chunking y la generación de embeddings, hasta la recuperación y la generación de respuestas. Cada decisión afecta a las demás y al rendimiento global del sistema. Este ejercicio integra todos los conceptos de la sesión en un diseño coherente de principio a fin.

### Objetivo de Aprendizaje
- Integrar todos los conceptos de la sesión en un diseño de sistema completo
- Tomar decisiones de diseño coordinadas y justificadas
- Identificar los puntos de fallo potenciales en un pipeline RAG
- Desarrollar la capacidad de comunicar decisiones técnicas a través de diagramas

### Enunciado

En grupos de 2-3 personas, elegid **uno** de los siguientes casos de uso y diseñad un pipeline RAG completo. Debéis producir: un diagrama del sistema, una tabla de decisiones técnicas y un análisis de riesgos.

### Casos de Uso (elegir uno)

**Caso A: Asistente de Documentación Técnica**
Una empresa de software con 2.000 páginas de documentación técnica (API docs, tutoriales, guías de troubleshooting) quiere un chatbot que ayude a los desarrolladores. La documentación está en Markdown en un repositorio Git y se actualiza 3-4 veces por semana.

**Caso B: Buscador Inteligente de Normativa Universitaria**
Una universidad quiere que estudiantes y profesores puedan hacer preguntas sobre normativa académica (reglamentos de evaluación, normativa TFG/TFM, convocatorias, protocolos). Los documentos son PDFs oficiales (~50 documentos, ~500 páginas totales) que se actualizan una vez al año.

**Caso C: Asistente de Recursos Humanos**
Una empresa con 500 empleados quiere un asistente que responda preguntas sobre políticas internas (vacaciones, teletrabajo, beneficios, código de conducta). Los documentos son una mezcla de PDFs, páginas de la intranet y presentaciones PowerPoint.

### Parte 1: Diagrama del Pipeline

Dibujad (en papel, pizarra o herramienta digital) un diagrama que incluya todas las etapas del pipeline, desde la fuente de datos hasta la respuesta al usuario. Debe incluir como mínimo:

```
┌─────────────┐    ┌──────────────┐    ┌───────────┐    ┌──────────────┐
│  Fuentes de │───>│ Preprocesado │───>│ Chunking  │───>│  Generación  │
│    Datos    │    │  y Limpieza  │    │           │    │  Embeddings  │
└─────────────┘    └──────────────┘    └───────────┘    └──────┬───────┘
                                                               │
                                                               v
┌─────────────┐    ┌──────────────┐    ┌───────────┐    ┌──────────────┐
│  Respuesta  │<───│  Generación  │<───│ Ranking y │<───│    Base de   │
│  al Usuario │    │   con LLM    │    │ Selección  │    │    Datos     │
└─────────────┘    └──────────────┘    └───────────┘    │  Vectorial   │
                                                        └──────────────┘
         ▲                                                     ▲
         │              ┌───────────┐                          │
         └──────────────│  Consulta │──────────────────────────┘
                        │  Usuario  │
                        └───────────┘
```

Para cada bloque del diagrama, anotad la tecnología o herramienta concreta que usaríais.

### Parte 2: Tabla de Decisiones Técnicas

| Decisión | Vuestra elección | Alternativas consideradas | Justificación |
|----------|-----------------|--------------------------|---------------|
| **Formato de entrada** | PDF + HTML | Solo PDF, bases de datos | La normativa está principalmente en PDFs oficiales; la web complementa con información actualizada |
| **Herramienta de extracción de texto** | PyMuPDF (fitz) + BeautifulSoup | pdfplumber, PyPDF2, Unstructured | PyMuPDF es rápido y maneja bien PDFs con estructura; BeautifulSoup para HTML es estándar |
| **Estrategia de chunking** | RecursiveCharacterTextSplitter con separadores de sección | MarkdownHeaderTextSplitter, chunking semántico | Los PDFs de normativa tienen estructura de artículos; el splitter recursivo respeta párrafos |
| **chunk_size** | 400 caracteres | 200, 500, 800 | Balance entre contexto suficiente para normativa y precisión de búsqueda |
| **chunk_overlap** | 80 caracteres (~20%) | 50, 100, 150 | Suficiente para no perder contexto en transiciones entre artículos |
| **Modelo de embeddings** | text-embedding-3-small (OpenAI) | all-MiniLM-L6-v2, multilingual-e5 | Buena calidad para español, coste razonable, información no es confidencial |
| **Base de datos vectorial** | ChromaDB con persistencia | Pinecone, pgvector | Volumen pequeño (~500 páginas), fácil de mantener, sin coste adicional |
| **Número de chunks recuperados (top-k)** | 5 | 3, 7, 10 | Suficiente contexto sin sobrecargar el prompt; normativa es específica |
| **Estrategia de búsqueda** (solo vectorial / híbrida) | Vectorial pura | Híbrida (vectorial + BM25) | Para este volumen, búsqueda vectorial es suficiente; híbrida añade complejidad innecesaria |
| **LLM para generación** | GPT-4o-mini | Claude Haiku, GPT-4o, Llama 3 | Coste-efectivo, suficiente para respuestas sobre normativa, buen español |
| **Prompt template** (describir estructura) | Estructurado con instrucciones de cita y admisión de desconocimiento | Prompt simple, few-shot | La normativa requiere precisión y citas a fuentes |
| **Frecuencia de actualización del índice** | Anual (con trigger manual para cambios extraordinarios) | Mensual, semanal | La normativa universitaria cambia típicamente una vez al año |

### Parte 3: Prompt Template

Diseñad el prompt que recibirá el LLM para generar la respuesta. Debe incluir instrucciones claras sobre cómo usar el contexto recuperado:

```
Eres un asistente virtual de la universidad U-TAD especializado en normativa académica.
Tu función es responder preguntas de estudiantes y profesores basándote EXCLUSIVAMENTE
en la normativa oficial proporcionada en el contexto.

CONTEXTO (extractos de normativa oficial):
{contexto_recuperado}

INSTRUCCIONES:
- Responde SOLO con información presente en el contexto proporcionado
- Si la información no está en el contexto, indica claramente: "No he encontrado esta información en la normativa disponible. Te recomiendo consultar con Secretaría Académica."
- Cita siempre el documento fuente entre corchetes, por ejemplo: [Reglamento de Evaluación, Art. 15]
- Usa un tono formal pero cercano, apropiado para comunicación universitaria
- Si hay múltiples normativas aplicables, menciona todas las relevantes
- Para plazos y fechas, indica que deben verificarse en la convocatoria vigente

PREGUNTA DEL USUARIO:
{pregunta}

RESPUESTA:
```

### Parte 4: Análisis de Riesgos y Mitigaciones

Identificad al menos 4 riesgos potenciales del sistema y proponed mitigaciones:

| Riesgo | Probabilidad | Impacto | Mitigación propuesta |
|--------|-------------|---------|---------------------|
| El LLM alucina e inventa información no presente en el contexto | Alta | Alto | Prompt estricto que indica responder SOLO con el contexto; instrucción para admitir cuando no tiene información; revisión humana periódica de respuestas |
| La consulta del usuario no tiene respuesta en los documentos | Media | Medio | Mensaje claro de "información no encontrada" con redirección a Secretaría Académica; FAQ de preguntas más comunes como fallback |
| La normativa se actualiza y el índice está desactualizado | Baja | Alto | Pipeline de actualización anual con checklist; fecha de última actualización visible al usuario; alerta de re-indexación cuando hay cambios |
| El usuario hace preguntas fuera del ámbito (no académicas) | Media | Bajo | Prompt con scope definido; clasificador de intención previo; respuesta educada redirigiendo a recursos apropiados |
| Chunks recuperados no contienen la información más relevante | Media | Alto | Experimentar con diferentes chunk_size y overlap; considerar reranking; añadir metadatos de sección/documento para filtrado |
| Sobrecarga del sistema en épocas de matrícula/exámenes | Baja | Medio | Caché de respuestas frecuentes; rate limiting por usuario; escalado horizontal si es necesario |

### Parte 5: Presentación (5 minutos por grupo)

Cada grupo presenta brevemente su diseño al resto de la clase, explicando:
1. El caso de uso elegido y por qué
2. Las 2-3 decisiones técnicas más importantes y su justificación
3. El riesgo que consideran más crítico y cómo lo mitigan

### Extensión (Opcional)

- Añadid al diseño un sistema de evaluación: ¿cómo mediríais la calidad de las respuestas del sistema? Investigad métricas como Faithfulness, Answer Relevancy y Context Precision del framework RAGAS.
- Diseñad un flujo de feedback del usuario: ¿cómo incorporaríais las valoraciones de los usuarios (pulgar arriba/abajo) para mejorar el sistema?
