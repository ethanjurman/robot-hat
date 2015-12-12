import sys
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import builtins
import types
import inspect

sys.path.append('pywsd')
sys.path.append('pywsd/pywsd')
from pywsd import disambiguate

import sentence_cleaner as sc
import word_checker as wc
import pattern_checker as pc

if (len(sys.argv) < 2):
    # no sentence provided
    print("NO SENTENCE PROVIDED, EXITING PROGRAM")
    sys.exit(0)

# patterns follows: [token matching list, output string]
# token matching list: [('possible enlish word', 'possible part of speech')]
#   if None, accepts anything.
patterns = [
        [[(None, None),(None,'NN')], "0(1)"],
        [[(None, None),(None,'VBP'),(None,'NN')], "1(2)"],
        [[(None, None),(None,'DT'),(None,'NN'),(None,'IN'),(None,'NN')], "for 2 in 4:\n\t0(2)"]
    ]

sentence = sys.argv[1]
pc.lexico_syntax_translator(sentence,patterns)

print("\n\n")
for token in disambiguate(sentence):
    if (token[1]):
        print(token, wc.check_word(token[1], builtins))
    else:
        print(token)
