def load_keywords(path="data/threat_keywords.txt"):
    with open(path) as f:
        return [w.strip().lower() for w in f if w.strip()]

def find_threat_words(text, keywords):
    text_lower = text.lower()
    return sorted({w for w in keywords if w in text_lower})
