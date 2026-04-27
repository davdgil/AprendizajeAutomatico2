# Asistente RAG de Apuntes

Asistente academico desarrollado en Python que responde preguntas sobre documentos usando un pipeline RAG. El sistema indexa apuntes en una base vectorial ChromaDB, recupera los fragmentos mas relevantes para cada consulta y genera una respuesta final con Google Gemini.

## Unidades del curso aplicadas

- **Unidad 2: Prompt Engineering** El proyecto utiliza un prompt estructurado para obligar al modelo a responder unicamente con el contexto recuperado, indicando cuando no hay informacion suficiente y priorizando respuestas claras y breves.
- **Unidad 3: Transformers y APIs** La aplicacion accede programaticamente a la API de Google Gemini tanto para generar embeddings como para generar la respuesta final del asistente.
- **Unidad 5: RAG y Bases Vectoriales** El sistema implementa un pipeline RAG completo con carga de documentos, chunking, generacion de embeddings, almacenamiento en ChromaDB y recuperacion semantica de contexto.

## Arquitectura

El flujo del sistema se divide en dos fases:

### 1. Indexacion

1. Se cargan los documentos desde `data/documentos/`.
2. Se extrae el texto de archivos `.pdf`, `.txt` y `.md`.
3. El texto se divide en chunks con solapamiento.
4. Gemini genera los embeddings de cada chunk.
5. Los chunks y sus metadatos se almacenan en ChromaDB.

### 2. Consulta

1. El usuario introduce una pregunta en la app de Streamlit.
2. Gemini genera el embedding de la consulta.
3. ChromaDB recupera los fragmentos mas similares.
4. Se construye un prompt con la pregunta y el contexto recuperado.
5. Gemini genera una respuesta final basada en ese contexto.

## Tecnologias utilizadas

- Python
- Streamlit
- ChromaDB
- Google Gemini API
- `google-genai`
- `pypdf`
- `python-dotenv`

## Instalacion y configuracion

1. Clonar el repositorio.
2. Entrar en la carpeta del proyecto:

```powershell
cd asistente-rag-apuntes
```

3. Crear y activar un entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

4. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

5. Crear un archivo `.env` a partir de `.env.example` e introducir la clave de Google Gemini:

```env
GOOGLE_API_KEY=tu_clave_aqui
```

6. Colocar los documentos que se quieran indexar dentro de `data/documentos/`.

## Uso

### 1. Ingesta de documentos

Ejecutar el script de ingesta para indexar los documentos en ChromaDB:

```powershell
python .\src\ingest.py
```

Si todo va bien, el script mostrara el numero de chunks almacenados.

### 2. Prueba por terminal

Se puede probar el pipeline RAG desde consola:

```powershell
python .\src\rag_pipeline.py
```

El sistema pedira una pregunta, generara una respuesta y mostrara las fuentes recuperadas.

### 3. Interfaz web

Para lanzar la aplicacion con Streamlit:

```powershell
streamlit run .\app.py
```

Una vez abierta la app:

1. Escribir una pregunta sobre los documentos indexados.
2. Pulsar el boton de consulta.
3. Revisar la respuesta generada y las fuentes recuperadas.

## Capturas / Demo

Pendiente de anadir capturas reales del proyecto en funcionamiento.

Capturas recomendadas:

- Pantalla principal de Streamlit con una consulta escrita.
- Respuesta generada por el sistema junto con las fuentes recuperadas.
- Ejecucion correcta del script de ingesta mostrando los chunks almacenados.

Las imagenes se guardaran en `docs/capturas/`.

## Decisiones tecnicas

- **Uso de Gemini**: se eligio Google Gemini porque permite trabajar con la misma API tanto para embeddings como para generacion de respuestas.
- **Uso de ChromaDB**: se eligio ChromaDB por su simplicidad de uso en local y por encajar muy bien en un proyecto academico de RAG.
- **Separacion de fases**: la indexacion se separa de la consulta para no recalcular embeddings en cada pregunta.
- **Prompt externo**: el prompt se movio a `src/prompts.py` para separar la logica del pipeline de la parte de prompt engineering.
- **Chunking con overlap**: se usa solapamiento entre chunks para reducir perdida de contexto en los bordes de cada fragmento.

Parametros relevantes actuales:

- `chunk_size = 800`
- `overlap = 100`
- `top_k = 4`
- modelo de embeddings: `gemini-embedding-001`
- modelo de generacion: `gemini-2.5-flash`

Dificultades encontradas:

- Se tuvo que adaptar el proyecto de OpenAI a Gemini debido a la disponibilidad real de la API.
- Fue necesario habilitar la Gemini API en Google Cloud para poder usar embeddings y generacion.
- Se ajustaron imports y configuracion para que el pipeline funcionara tanto por terminal como desde Streamlit.

## Posibles mejoras

- Permitir subir documentos directamente desde la interfaz en Streamlit y ejecutar la ingesta desde la propia app.
- Mejorar la visualizacion de fuentes mostrando extractos mas cortos y mejor formateados.
- Implementar reindexacion incremental para detectar cambios en documentos sin rehacer toda la base vectorial.
- Anadir memoria conversacional para mantener el contexto entre varias preguntas consecutivas.

## Autor(es)

- [Anadir nombre y apellidos]
