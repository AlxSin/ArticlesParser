import trafilatura

def extract_text(html: str) -> str | None:
    result = trafilatura.extract(html, include_comments=False, include_tables=False)
    return result.strip() if result else None
