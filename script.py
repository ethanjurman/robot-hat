import sys
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.parse.bllip import BllipParser
import builtins
import types
import inspect

import sentence_cleaner as sc

if (len(sys.argv) < 2):
    # no sentence provided
    print("NO SENTENCE PROVIDED, EXITING PROGRAM")
    sys.exit(0)

sentence = sys.argv[1]
sentence = sc.clean(sentence)
# words = [w for w in pos_tag(sentence.split())]
words = sentence.split(" ")
print(words)
for w in words:
    print(w, w in dir(builtins))
