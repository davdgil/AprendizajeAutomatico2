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

from document_loader import load_documents
from text_splitter import split_text


BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = BASE_DIR / "data" / "documentos"
CHROMA_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "apuntes"
EMBEDDING_MODEL = "gemini-embedding-001"
EMBEDDING_DIMENSIONALITY = 768
EMBEDDING_BATCH_SIZE = 100


def build_chunks(documents: list[dict[str, str]]) -> list[dict[str, str]]:
    chunked_documents: list[dict[str, str]] = []

    for document in documents:
        chunks = split_text(document["content"])

        for index, chunk in enumerate(chunks):
            chunked_documents.append(
                {
                    "id": f'{document["source"]}-{index}',
                    "text": chunk,
                    "source": document["source"],
                    "path": document["path"],
                }
            )

    return chunked_documents


def get_google_api_key() -> str:
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("KEY")

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


def embed_texts(
    client: genai.Client, texts: list[str], task_type: str
) -> list[list[float]]:
    all_embeddings: list[list[float]] = []

    for start in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        batch = texts[start : start + EMBEDDING_BATCH_SIZE]
        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=batch,
            config=types.EmbedContentConfig(
                task_type=task_type,
                output_dimensionality=EMBEDDING_DIMENSIONALITY,
            ),
        )
        all_embeddings.extend(embedding.values for embedding in response.embeddings)

    return all_embeddings


def ingest_documents() -> int:
    load_dotenv()
    api_key = get_google_api_key()

    documents = load_documents(DOCUMENTS_DIR)
    chunked_documents = build_chunks(documents)

    if not chunked_documents:
        return 0

    google_client = genai.Client(api_key=api_key)
    collection = get_collection()

    ids = [chunk["id"] for chunk in chunked_documents]
    documents_text = [chunk["text"] for chunk in chunked_documents]
    embeddings = embed_texts(
        google_client,
        documents_text,
        task_type="RETRIEVAL_DOCUMENT",
    )
    metadatas = [
        {
            "source": chunk["source"],
            "path": chunk["path"],
        }
        for chunk in chunked_documents
    ]

    collection.upsert(
        ids=ids,
        documents=documents_text,
        metadatas=metadatas,
        embeddings=embeddings,
    )
    return len(chunked_documents)


def main() -> None:
    total_chunks = ingest_documents()
    print(f"Ingesta completada. Chunks almacenados: {total_chunks}")


if __name__ == "__main__":
    main()
