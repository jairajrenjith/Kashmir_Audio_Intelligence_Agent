def load_sensitive_locations(path="data/sensitive_locations.txt"):
    with open(path) as f:
        return [l.strip().lower() for l in f if l.strip()]

def compute_risk(threat_words, locations, sensitive_list):
    score = 0

    if threat_words:
        score += 2

    if any(loc.lower() in sensitive_list for loc in locations):
        score += 3

    if score >= 4:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    return "LOW"


def detect_suspects(persons, transcript, threat_words):
    suspects = []
    text_lower = transcript.lower()

    for person in persons:
        score = sum(1 for word in threat_words if word in text_lower)
        if score > 0:
            suspects.append({
                "name": person,
                "suspicion_score": score
            })

    return suspects
