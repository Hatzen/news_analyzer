import requests
from news_analyzer.config import OLLAMA_API_URL

ANALYSIS_PROMPT = """Analysiere folgenden Nachrichtenartikel. Gib die Bewertung als JSON zurück.

Überschrift: "{title}"
Kategorie: "{category}"
Datum: {date}
Artikeltext:
{content}

Beantworte:
- Wie faktentreu ist der Artikel? (0 = nur Meinung, 100 = rein faktisch)
- Ist die Überschrift emotional/manipulativ? (0 = sachlich, 100 = sehr manipulativ)
- Politische Tendenz? ("neutral", "links", "rechts", "liberal", "konservativ", "populistisch", "grün", "progressiv", etc.)
- Wird Meinung als Tatsache dargestellt? (true/false)
- Enthält der Artikel emotionale Sprache? (true/false)
- Gibt es wichtige Auslassungen? (true/false)

Rückgabeformat:
{
  "fakten_score": 92,
  "manipulationsgrad": 20,
  "tendenz": "neutral",
  "meinung_als_tatsache": false,
  "emotional_sprache": false,
  "auslassung": false
}
"""

def analyze_article(title, content, category, date):
    prompt = ANALYSIS_PROMPT.format(title=title, content=content, category=category, date=date)
    response = requests.post(OLLAMA_API_URL, json={"model": "llama3", "prompt": prompt})
    return response.json()
