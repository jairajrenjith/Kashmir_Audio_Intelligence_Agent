def highlight_text(text, words):
    for w in words:
        text = text.replace(w, f"**{w.upper()}**")
        text = text.replace(w.capitalize(), f"**{w.upper()}**")
    return text
