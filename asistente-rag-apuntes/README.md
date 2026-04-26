# Asistente RAG de Apuntes

Asistente académico que responde preguntas sobre documentos usando recuperación semántica, ChromaDB y la API de Google Gemini.

## Estructura

- `app.py`: interfaz en Streamlit.
- `data/documentos/`: documentos fuente.
- `chroma_db/`: persistencia local de Chroma.
- `src/`: lógica de ingesta, prompts y pipeline RAG.
- `docs/capturas/`: capturas para la demo.

## Ejecución prevista

1. Crear entorno virtual.
2. Instalar dependencias con `pip install -r requirements.txt`.
3. Añadir la API key en `.env`.
4. Colocar documentos en `data/documentos/`.
5. Ejecutar la ingesta.
6. Lanzar la app con `streamlit run app.py`.
