import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def extract_action_items(text):
    doc = nlp(text)
    actions = []

    for sent in doc.sents:
        persons = [ent.text for ent in sent.ents if ent.label_ == "PERSON"]
        dates = [ent.text for ent in sent.ents if ent.label_ == "DATE"]
        orgs = [ent.text for ent in sent.ents if ent.label_ == "ORG"]
        
        verbs = [token.lemma_ for token in sent if token.pos_ == "VERB"]  # Extract verbs (lemmatized)

        if persons and verbs:
            action_item = f"{persons[0]} should {verbs[0]}"  # Forming an action statement
            if dates:
                action_item += f" by {dates[0]}"
            actions.append(action_item)

    return actions

if __name__ == "__main__":
    transcript = "John will submit the budget report by next Friday."
    print(extract_action_items(transcript))