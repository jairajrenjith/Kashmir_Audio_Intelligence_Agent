import spacy

nlp = spacy.load("xx_ent_wiki_sm")

def extract_entities(text):
    doc = nlp(text)

    persons = list({ent.text for ent in doc.ents if ent.label_ == "PER"})
    locations = list({ent.text for ent in doc.ents if ent.label_ in ["LOC", "GPE"]})
    times = list({ent.text for ent in doc.ents if ent.label_ in ["DATE", "TIME"]})

    return persons, locations, times
