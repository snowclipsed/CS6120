from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
import string

documents = [
    "Zipf's law is directly tied to our sparseness problem - since it can be used to gauge the importance of a word in the corpus, based on its frequency.",
    "Words that are in the highest ranks in the Zipf's law plot are generally conjunctive words, like  and the which do not add specific meaning to the sentence themselves."
]


def remove_stopwords(doc):
    stop_words = stopwords.words('english')
    return " ".join([word for word in doc.split() if word not in stop_words])

def remove_punctuation(doc):
    return doc.translate(str.maketrans('', '', string.punctuation))

def DTM(documents):
    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    return bow_matrix.toarray(), feature_names

stopwords_removed_documents = [remove_stopwords(doc) for doc in documents]

punctuation_removed_documents = [remove_punctuation(doc) for doc in stopwords_removed_documents]

bow_matrix, feature_names = DTM(punctuation_removed_documents)

print(bow_matrix)
print(feature_names)