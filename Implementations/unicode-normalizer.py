import unicodedata as unc


def decompose(text):
    return unc.normalize('NFD', text)

text = "Héllo, hôw àre ýou?"

print(decompose(text))

def compose(text):
    return unc.normalize('NFC', text)

text = "e\u0301"

print(compose(text))