import nltk

def lexico_syntax_translator(text, patterns):
    tokenized = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokenized)
    print(tags)
    # check each pattern
    for p in patterns:
        # check that the length of the tokens match the pattern
        if len(p[0]) == len(tags):
            print("possible matching pattern", p[0])
            compatible = True
            # check each element pair tags for the pattern
            for index in range(len(tags)):
                if ((tags[index][1] != p[0][index][1]) and (p[0][index][1] != None)):
                    print("not compatible", tags[index][1], p[0][index][1])
                    compatible = False
            if compatible:
                result = ""
                # for char in pattern output
                for c in p[1]:
                    # if it's a number
                    if (c.isdecimal()):
                        c = tags[int(c)][0]
                    result = result + c
                print()
                print(result)
                return result
