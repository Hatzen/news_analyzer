import requests
from bs4 import BeautifulSoup
from news_analyzer.config import NEWS_SOURCES
from urllib.parse import urljoin
from news_analyzer.logger import logger


def extract_article(articles, url, source):
    res = requests.get(url, timeout=(5, 10))
    soup = BeautifulSoup(res.content, "xml")  # Parse as XML for RSS
    for item in soup.find_all("item"):
        link_tag = item.find("link")
        if not link_tag or not link_tag.text:
            continue

        href = link_tag.text.strip()

        # Ensure full URL using base_url
        if not href.startswith("http"):
            href = urljoin(source["base_url"], href)

        # Apply slash-count rules
        slash_count = href.count('/')
        if (href.startswith("http") and slash_count == 4) or (not href.startswith("http") and slash_count == 2):
            title_tag = item.find("title")
            articles.append({
                "source": source["name"],
                "url": href,
                "title": title_tag.text.strip() if title_tag else ""
            })

    return articles

def extract_articles() -> list:
    articles = []
    for source in NEWS_SOURCES:
        for url in source["overview_urls"]:
            try:
                logger.info(f"Extract for {url}")
                extract_article(articles, url, source)
            except Exception as e:
                logger.warning(f"Failed to extract articles from {url}: {e}")

    return articles


