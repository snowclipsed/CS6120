import spacy

def lemmatize_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    lemmatized_text = " ".join([token.lemma_ for token in doc])
    return lemmatized_text

text = "The cats are running and jumping over the fences."
lemmatized_text = lemmatize_text(text)
print(lemmatized_text)
