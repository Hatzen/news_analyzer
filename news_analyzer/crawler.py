import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from news_analyzer.config import NEWS_SOURCES

def get_yesterday_date_str():
    return (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

def extract_articles():
    articles = []
    for source in NEWS_SOURCES:
        for url in source["overview_urls"]:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            for link in soup.find_all("a", href=True):
                href = link["href"]
                if href.startswith("http") and "2025" in href and get_yesterday_date_str() in href:
                    articles.append({
                        "source": source["name"],
                        "url": href,
                        "title": link.get_text(strip=True)
                    })
    return articles
