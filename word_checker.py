from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import nltk
import builtins
import sys

sys.path.append('pywsd')
sys.path.append('pywsd/pywsd')
from pywsd import disambiguate

mem = {} # hashed values for type -> (library name)

# adds a library and it's functions to the mem
def add_library_to_mem(library):
    for named in dir(library):
        mem[type(named)] = (library, named)

def return_true():
    return True
# return possible functions / classes / etc... for a given part of speech,
# i.e. verbs (or 'v') should be mapped to functions
def components_for_pos(pos, library_filter=return_true):
    result = []
    if pos == 'v':
        if 'method' in mem:
            result += mem['method']
        if 'builtin_function_or_method' in mem:
            result += mem['builtin_function_or_method']
    return [item[1] for item in result if library_filter(item)]

def check_word(synset, library=builtins):
    # definition for the synset
    defin = synset.definition()

    # for each name in the synsets list of names
    #   check if name exists in library as a class, function, or attribute name
    for name in synset.lemma_names():
        if name in dir(library):
            return name

    # else lets check all the library's methods and functions, and see if their
    # definitions match the words definition
    component_rank_function = (None,0)
    add_library_to_mem(builtins)
    print(components_for_pos(synset.pos))
    for component in components_for_pos(synset.pos):
        component_definition = getattr(library, component).__doc__
        if (component_definition):
            result = compare_defin(component_definition, defin)
            print(component, result)
            if result > component_rank_function[1]:
                component_rank_function = (component, result)
    return component_rank_function[0]

def compare_defin(defin1, defin2):
    return len([item for item in set(disambiguate(defin1)).intersection(disambiguate(defin2)) if filter_stopwords(item)])

def filter_stopwords(token_pair):
    # this operation is taking extremely long, lets just return True for the time being
    return True
    # token_pair has (word, synset)
    token = token_pair[1]
    # if token isn't None
    if (token):
        # for each word in the synset
        for word in token.lemma_names():
            # if the word is in stopwords
            if word in stopwords.words():
                # don't include the word
                return False
    # if the token_pair is in the stopwords
    if token_pair[0] in stopwords.words():
        # don't include the word
        return False
    # else include the word
    return True

def check_sense(function):
    name = function.__name__
    doc_string = function.__doc__
