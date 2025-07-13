import os

NEWS_SOURCES = [
    {
        "name": "Spiegel",
        "base_url": "https://www.spiegel.de/",
        "overview_urls": [
            "https://www.spiegel.de/schlagzeilen/index.rss",
            "https://www.spiegel.de/politik/index.rss"
        ]
    },
    {
        "name": "FAZ",
        "base_url": "https://www.faz.net/",
        "overview_urls": [
            "https://www.faz.net/rss/aktuell/"
        ]
    },
    {
        "name": "SZ",
        "base_url": "https://rss.sueddeutsche.de/",
        "overview_urls": [
            "https://rss.sueddeutsche.de/alles",
            "https://rss.sueddeutsche.de/rss/Politik"
        ]
    }
]

weaviate_url = os.getenv("WEAVIATE_HOST", "http://localhost:8080")
ollama_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_API_URL = ollama_url + "/api/generate"
