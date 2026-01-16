import feedparser

def fetch_new_articles(feed_file: str):
    with open(feed_file, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    entries = []
    for feed in urls:
        data = feedparser.parse(feed)
        entries.extend([{"title": e.get("title"), "link": e.get("link")} for e in data.entries])

    return entries
