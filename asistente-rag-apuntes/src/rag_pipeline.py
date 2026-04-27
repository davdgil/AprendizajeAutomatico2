import os
import logging
from pathlib import Path

os.environ["ANONYMIZED_TELEMETRY"] = "FALSE"
logging.getLogger("chromadb.telemetry.product.posthog").setLevel(logging.CRITICAL)

import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
from google import genai
from google.genai import types


BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "apuntes"
EMBEDDING_MODEL = "gemini-embedding-001"
EMBEDDING_DIMENSIONALITY = 768


def get_google_api_key() -> str:
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "No se ha encontrado GOOGLE_API_KEY ni KEY en el archivo .env"
        )

    return api_key


def get_collection():
    client = chromadb.PersistentClient(
        path=str(CHROMA_DIR),
        settings=Settings(anonymized_telemetry=False),
    )
    return client.get_or_create_collection(name=COLLECTION_NAME)


def embed_query(client: genai.Client, question: str) -> list[float]:
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=question,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=EMBEDDING_DIMENSIONALITY,
        ),
    )
    return response.embeddings[0].values


def retrieve_context(question: str, top_k: int = 4) -> list[dict]:
    load_dotenv()
    api_key = get_google_api_key()

    google_client = genai.Client(api_key=api_key)
    query_embedding = embed_query(google_client, question)
    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    retrieved_chunks: list[dict] = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for document, metadata, distance in zip(documents, metadatas, distances):
        retrieved_chunks.append(
            {
                "content": document,
                "source": metadata.get("source", "desconocido"),
                "path": metadata.get("path", ""),
                "distance": distance,
            }
        )

    return retrieved_chunks


def main() -> None:
    question = input("Escribe una pregunta sobre tus documentos: ").strip()

    if not question:
        print("No se ha introducido ninguna pregunta.")
        return

    results = retrieve_context(question)

    if not results:
        print("No se han recuperado fragmentos relevantes.")
        return

    print("\nChunks recuperados:\n")

    for index, chunk in enumerate(results, start=1):
        print(f"[{index}] Fuente: {chunk['source']}")
        print(f"Distancia: {chunk['distance']}")
        print(chunk["content"])
        print("-" * 80)


if __name__ == "__main__":
    main()
