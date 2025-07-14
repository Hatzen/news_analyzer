import os

NEWS_SOURCES = [
  {
    "name": "Spiegel",
    "base_url": "https://www.spiegel.de/",
    "overview_urls": [
        #"https://www.spiegel.de/schlagzeilen/index.rss",
        "https://www.spiegel.de/politik/index.rss"
    ]
  },
  {
    "name": "Süddeutsche Zeitung",
    "base_url": "https://rss.sueddeutsche.de/",
    "overview_urls": [
        #"https://rss.sueddeutsche.de/alles",
        "https://rss.sueddeutsche.de/rss/Politik"
    ]
  },
  {
    "name": "Die Zeit",
    "base_url": "https://www.zeit.de/",
    "overview_urls": [
      "https://newsfeed.zeit.de/politik/index"
    ]
  },
  {
    "name": "Tagesschau",
    "base_url": "https://www.tagesschau.de/",
    "overview_urls": [
      "https://www.tagesschau.de/xml/rss2"
    ]
  },
  {
    "name": "n-tv",
    "base_url": "https://www.n-tv.de/",
    "overview_urls": [
      "https://www.n-tv.de/rss"
    ]
  },
  {
    "name": "Deutschlandfunk Politik",
    "base_url": "https://www.deutschlandfunk.de/",
    "overview_urls": [
      "https://www.deutschlandfunk.de/podcast-politik.1041.de.podcast.xml"
    ]
  },
  {
    "name": "Welt",
    "base_url": "https://www.welt.de/",
    "overview_urls": [
      "https://www.welt.de/feeds/section/politik.rss"
    ]
  },
  {
    "name": "Focus Online",
    "base_url": "https://www.focus.de/",
    "overview_urls": [
      "https://www.focus.de/politik/rssfeed/politik.rss"
    ]
  },
  {
    "name": "RT (Russia Today)",
    "base_url": "https://www.rt.com/",
    "overview_urls": [
      "https://www.rt.com/rss/news/"
    ]
  },
  {
    "name": "Xinhua (China)",
    "base_url": "http://www.xinhuanet.com/",
    "overview_urls": [
      "http://www.xinhuanet.com/english/rss/worldrss.xml"
    ]
  },
  {
    "name": "Washington Post",
    "base_url": "https://www.washingtonpost.com/",
    "overview_urls": [
      "http://feeds.washingtonpost.com/rss/politics"
    ]
  },
  {
    "name": "BBC Politics",
    "base_url": "https://www.bbc.com/",
    "overview_urls": [
      "http://feeds.bbci.co.uk/news/politics/rss.xml"
    ]
  },
  {
    "name": "The Guardian Politics",
    "base_url": "https://www.theguardian.com/",
    "overview_urls": [
      "https://www.theguardian.com/politics/rss"
    ]
  },
  {
    "name": "Reuters Politics",
    "base_url": "https://www.reuters.com/",
    "overview_urls": [
      "https://www.reutersagency.com/feed/?best-topics=politics"
    ]
  },
  {
    "name": "Politico Europe",
    "base_url": "https://www.politico.eu/",
    "overview_urls": [
      "https://www.politico.eu/rss/politics/"
    ]
  },
  {
    "name": "Al Jazeera Politics",
    "base_url": "https://www.aljazeera.com/",
    "overview_urls": [
      "https://www.aljazeera.com/xml/rss/all.xml"
    ]
  }
]


weaviate_url = os.getenv("WEAVIATE_HOST", "http://localhost:8080")
ollama_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_API_URL = ollama_url + "/api/generate"
