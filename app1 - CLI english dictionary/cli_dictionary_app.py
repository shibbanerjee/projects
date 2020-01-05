import json

import difflib

data = json.load(open("data.json"))

#function to return the value of the key entered
def translate(w):
    w = w.lower()
    if w in data.keys():
        #here we check if the lower case word is present in the dict keys and return value
        if len(data[w])>0:
            return '\n'.join(phrase for phrase in data[w])
        #w is local variable
    else:
        #else we state that the word was not found
        return close_match(w)
        #return "Word not found in dictionary, please double-check it."

#function to recommend the best match using get_close_matches
def close_match(word1):
    if len(difflib.get_close_matches(word1,data.keys()))>0:
        recomm_word = difflib.get_close_matches(word1,data.keys(),n=3,cutoff=0.8)[0]
        #the get_close_matches method takes 4 args, the word, a list of words to match it with, the no.of best matches,
        #and the minimum ratio of similarity
        #Note the output of this method will be an ordered list, meaning the best matched word is the first item of the dict
        #and so on
        usr_inp = input('Did you mean {}, enter yes or no: '.format(recomm_word))
        #check with user if the recommended word if similar to what they had in mind
        if usr_inp =='yes':
            if len (data[recomm_word])>1:
                return '\n'.join(phrase for phrase in data[recomm_word])
            #return the value of the dict key i
        elif usr_inp =='no':
            return "No problem, please check the spelling and enter again"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesnt exist please double check"


#Global variable
word = input("Enter a word: ")

print(translate(word))
