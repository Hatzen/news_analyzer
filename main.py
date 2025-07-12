from news_analyzer.crawler import extract_articles
from news_analyzer.parser import fetch_article_content
from news_analyzer.ollama_api import analyze_article
from datetime import datetime
import json

def main():
    articles = extract_articles()
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

    with open("analysis_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
