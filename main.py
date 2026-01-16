from parser.rss_reader import fetch_new_articles
from parser.article_fetcher import fetch_html
from parser.article_extractor import extract_text
from translator.translator import translate_text
from storage.store import save_article

def main():
    articles = fetch_new_articles("feeds.txt")

    for entry in articles:
        url = ["link"]
        print(f"Parsing -> {url}")

        html = fetch_html(url)
        if not html:
            continue

        text = extract_text(html)
        if not text:
            continue

        translated = translate_text(text, target="ru")

        save_article(url, entry["title"], text, translated)
        print(f"Done: {entry['title']}")

if __name__=="__main__":
    main()

