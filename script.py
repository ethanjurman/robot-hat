import sys
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import builtins
import types
import inspect

sys.path.append('pywsd')
sys.path.append('pywsd/pywsd')
from lesk import simple_lesk
from pywsd import disambiguate
from pywsd.similarity import max_similarity as maxsim

import sentence_cleaner as sc
import word_checker as wc

if (len(sys.argv) < 2):
    # no sentence provided
    print("NO SENTENCE PROVIDED, EXITING PROGRAM")
    sys.exit(0)

sentence = sys.argv[1]
for token in disambiguate(sentence):
    print(token)
    if (token[1] != None):
        print(token, wc.check_word(wn.synset(token[1]), builtins))
