

def split_text(text: str, chunk_size: int = 800, overlap: int = 100) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size debe ser mayor que 0")

    if overlap < 0:
        raise ValueError("overlap no puede ser negativo")

    if overlap >= chunk_size:
        raise ValueError("overlap debe ser menor que chunk_size")

    cleaned_text = text.strip()

    if not cleaned_text:
        return []

    chunks: list[str] = []
    start = 0

    while start < len(cleaned_text):
        end = min(start + chunk_size, len(cleaned_text))
        chunk = cleaned_text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(cleaned_text):
            break

        start = end - overlap

    return chunks
