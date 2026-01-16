import httpx

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible)"}

def fetch_html(url: str) -> str | None:
    try:
        resp = httpx.get(url, headers=HEADERS, timeout=10.0)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"Fetch error: {e}")
        return None
    