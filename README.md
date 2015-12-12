# robot-hat
NLP term project: The Execution of Code through Word-Sense  Disambiguation and Metaprogramming

_using python 3_
before hand please have the following libraries installed (via pip or their respective websites)

_nltk_

### Robot Hat generates code from natural language.

`python script.py "display each filename in folder"`

prints out possible lexico-syntax translations into code, as well as pairings from English words to python methods. Below is the example output for the command above.

```
[('display', 'NN'), ('each', 'DT'), ('filename', 'NN'), ('in', 'IN'), ('folder', 'NN')]
possible matching pattern [(None, None), (None, 'DT'), (None, 'NN'), (None, 'IN'), (None, 'NN')]

for filename in folder:
        display(filename)



[]
('display', Synset('display.n.06')) None
('each', None)
[]
('filename', Synset('filename.n.01')) None
('in', None)
[]
('folder', Synset('folder.n.02')) None
```

The output is split into 3 sections: the pattern matching and part of speech tagging, the code generation, and matching Synsets and English words with Python functions and modules.

`python script.py "please print example"`

outputs the following

```
[('please', 'NN'), ('print', 'VBP'), ('example', 'NN')]
possible matching pattern [(None, None), (None, 'VBP'), (None, 'NN')]

print(example)



('please', None)
('print', Synset('print.v.04')) print
[]
('example', Synset('model.n.07')) None
```
