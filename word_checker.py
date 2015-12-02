from nltk.corpus import wordnet as wn
import builtins

def check_word(synset, library=builtins):
    defi = synset.definition()
    # for each name in the synsets list of names
    #   check if name exists in library as a class, function, or attribute name
    for name in synset.lemma_names():
        if name in dir(library):
            print(name, True)
            return name
    return None

def check_sense(function):
    name = function.__name__
    doc_string = function.__doc__
