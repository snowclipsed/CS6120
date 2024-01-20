import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

document = "The quick brown fox jumps over the lazy dog."

words = document.split()

unique_words = set(words)

sorted_words = sorted(list(unique_words))

onehot_encoded = np.zeros((len(words), len(unique_words)), int)

for i in range(len(words)):
    onehot_encoded[i, sorted_words.index(words[i])] = 1

print(onehot_encoded)

onehot_representation = pd.DataFrame(onehot_encoded, columns=sorted_words)
print(onehot_representation)