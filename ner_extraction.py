import spacy

nlp = spacy.load("en_core_web_sm")

def extract_action_items(text):
    doc = nlp(text)
    actions = []
    
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "DATE", "ORG"]:
            actions.append(f"{ent.text} → {ent.label_}")
    
    return actions

if __name__ == "__main__":
    transcript = "John will submit the budget report by next Friday."
    print(extract_action_items(transcript))
