import streamlit as st

from src.rag_pipeline import generate_answer


st.set_page_config(page_title="Asistente RAG de Apuntes")

st.title("Asistente RAG de Apuntes")
st.write(
    "Haz una pregunta sobre los documentos indexados y el sistema respondera "
    "usando el contexto recuperado desde ChromaDB."
)

question = st.text_input("Escribe tu pregunta")

if st.button("Preguntar"):
    if not question.strip():
        st.warning("Introduce una pregunta antes de continuar.")
    else:
        with st.spinner("Buscando contexto y generando respuesta..."):
            result = generate_answer(question.strip())

        st.subheader("Respuesta")
        st.write(result["answer"])

        st.subheader("Fuentes recuperadas")

        for index, chunk in enumerate(result["chunks"], start=1):
            with st.expander(f"Fuente {index}: {chunk['source']}"):
                st.write(f"Distancia: {chunk['distance']}")
                st.write(chunk["content"])
