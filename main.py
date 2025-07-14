from news_analyzer.crawler import extract_articles
from news_analyzer.parser import fetch_article_content
from news_analyzer.ollama_api import analyze_article
from news_analyzer.repository import saveAll
from datetime import datetime
import json
from news_analyzer.logger import logger
from concurrent.futures import ThreadPoolExecutor

def handleArticle(article):
    content = fetch_article_content(article["url"])
    if not content:
        return
    title = article["title"]
    analysis = analyze_article(title, content, "Politik", datetime.now().strftime("%Y-%m-%d"))
    result = {
        "title": title,
        "url": article["url"],
        "source": article["source"],
        "content": content, #content[:500],
        "analysis": analysis
    }
    logger.info(f"add another result {title}")
    try:
        saveAll(result)
    except:
        logger.warning("Cannot persist data")
    return result


def main():
    logger.info("Application started")
    articles = extract_articles()
    logger.info(f"Found {len(articles)} articles")
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(handleArticle, articles))

    logger.info(f"Finished {len(results)} overall results")
    with open("analysis_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        

if __name__ == "__main__":
    main()
