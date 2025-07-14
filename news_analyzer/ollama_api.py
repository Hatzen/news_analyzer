import requests
import re
import json
from news_analyzer.config import OLLAMA_API_URL

ANALYSIS_PROMPT = """Analysiere folgenden Nachrichtenartikel. Gib die Bewertung als JSON zurück. Der Artikeltext enhält wahrscheinlich noch Noise in Form von Werbetexten, HTML-Tags etc. ignoriere diesen Noise. 

Überschrift: "{title}"
Kategorie: "{category}"
Datum: {date}
Artikeltext:
{content}

Beantworte:
- Wie faktentreu ist der Artikel? factRatio (0 = nur Meinung, 100 = rein faktisch)
- Ist die Überschrift emotional/manipulativ? manipulativeLanguage (0 = sachlich, 100 = sehr manipulativ)
- Politische Tendenz? spectrum ("neutral", "links", "rechts", "liberal", "konservativ", "populistisch", "grün", "progressiv", etc.)
- Wird Meinung als Tatsache dargestellt? politicalBiased (true/false)
- Enthält der Artikel emotionale Sprache? emotionalBiased (true/false)
- Gibt es wichtige Auslassungen? contentGaps (true/false)

3 Beispiele für das Rückgabeformat:
{{
  "factRatio": 92,
  "manipulativeLanguage": 27,
  "spectrum": "neutral",
  "politicalBiased": false,
  "emotionalBiased": false,
  "contentGaps": false
}}

{{
  "factRatio": 1,
  "manipulativeLanguage": 89,
  "spectrum": "konservativ",
  "politicalBiased": true,
  "emotionalBiased": true,
  "contentGaps": true
}}

{{
  "factRatio": 49,
  "manipulativeLanguage": 51,
  "spectrum": "populistisch",
  "politicalBiased": false,
  "emotionalBiased": true,
  "contentGaps": false
}}
"""

class ArticleScore:
    factRatio: int
    manipulativeLanguage: int
    spectrum: str
    politicalBiased: bool
    emotionalBiased: bool
    contentGaps: bool
    fullResponse: str

def extract_json_from_text(text) -> ArticleScore | None:
    match = re.search(r"\{.*?\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return None

# TODO: Or analyze directly https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# TODO: Proper return type of ArticleScore and not dict
def analyze_article(title, content, category, date) -> ArticleScore:
    prompt = ANALYSIS_PROMPT.format(title=title, content=content, category=category, date=date)
    response = requests.post(OLLAMA_API_URL, json={"model": "llama3.2:latest", "prompt": prompt, "stream": False})

    full_text = response.json()["response"]
    parsedJson = extract_json_from_text(full_text)
    if parsedJson is None:
        return {"fullResponse": full_text}

    parsedJson["fullResponse"] = full_text
    return parsedJson
