import requests
from bs4 import BeautifulSoup

def fetch_article_content(url) -> str:
    try:
        res = requests.get(url, timeout=(5, 10))
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = "\n".join(p.get_text(strip=True) for p in paragraphs)
        return content
    except Exception as e:
        return ""
