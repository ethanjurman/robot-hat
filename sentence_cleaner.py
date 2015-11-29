def clean(sentence):
    return sentence.lower()

# parse the text, removing stop words and punctuation
def parse_text(sentence):
    punctuation = set("{}(),\\/-=+*&^%$#@!.<>?;\"'")
    sentence = ''.join(c for c in sentence if c not in punctuation).lower()
    return set(sentence.split()).difference(stopwords.words("english"))
