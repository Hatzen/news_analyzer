from news_analyzer.crawler import extract_articles
from news_analyzer.parser import fetch_article_content
from news_analyzer.ollama_api import analyze_article
from news_analyzer.repository import saveAll
from datetime import datetime
import json
import logging
import os

def initLogger():    
    # Basic configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )

initLogger()
logger = logging.getLogger(__name__)

def main():
    logger.info("Application started")
    articles = extract_articles()
    logger.info(f"Found {len(articles)} articles")
    results = []
    for a in articles:
        content = fetch_article_content(a["url"])
        if not content:
            continue
        analysis = analyze_article(a["title"], content, "Politik", datetime.now().strftime("%Y-%m-%d"))
        results.append({
            "title": a["title"],
            "url": a["url"],
            "source": a["source"],
            "content": content[:500],
            "analysis": analysis
        })

    logger.info(f"Found {len(results)}")
    with open("analysis_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

        

if __name__ == "__main__":
    main()
