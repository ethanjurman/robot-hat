import nltk

def clean(sentence):
    return sentence.lower()

# parse the text, removing stop words and punctuation
def parse_text(sentence):
    sentence = clean(sentence)
    punctuation = set("{}(),\\/-=+*&^%$#@!.<>?;\"'")
    sentence = ''.join(c for c in sentence if c not in punctuation).lower()
    return nltk.pos_tag(nltk.word_tokenize(sentence))
