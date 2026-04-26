from pathlib import Path

from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}


def get_document_paths(documents_dir: str | Path) -> list[Path]:
    base_path = Path(documents_dir)

    if not base_path.exists():
        raise FileNotFoundError(f"No existe la carpeta de documentos: {base_path}")

    paths = [
        path
        for path in base_path.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    return sorted(paths)


def load_text_file(file_path: str | Path) -> str:
    path = Path(file_path)
    return path.read_text(encoding="utf-8")


def load_pdf_file(file_path: str | Path) -> str:
    path = Path(file_path)
    reader = PdfReader(str(path))
    pages: list[str] = []

    for page in reader.pages:
        pages.append(page.extract_text() or "")

    return "\n".join(pages).strip()


def load_document(file_path: str | Path) -> dict[str, str]:
    path = Path(file_path)
    extension = path.suffix.lower()

    if extension == ".pdf":
        content = load_pdf_file(path)
    elif extension in {".txt", ".md"}:
        content = load_text_file(path)
    else:
        raise ValueError(f"Formato no soportado: {extension}")

    return {
        "source": path.name,
        "path": str(path),
        "content": content.strip(),
    }


def load_documents(documents_dir: str | Path) -> list[dict[str, str]]:
    document_paths = get_document_paths(documents_dir)
    return [load_document(path) for path in document_paths]
