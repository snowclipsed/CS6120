from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

def porter_stemmer(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

words = ["argument", "running", "jumped"]
stemmed_words = porter_stemmer(words)

print(f"Original words: {words}")
print(f"Porter Stemmed words: {stemmed_words}")

def snowball_stemmer(words):
    stemmer = SnowballStemmer("english")
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

words = ["argument", "running", "jumped"]
stemmed_words = snowball_stemmer(words)

print(f"Original words: {words}")
print(f"Snowball Stemmed words: {stemmed_words}")