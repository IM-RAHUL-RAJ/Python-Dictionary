import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def meaning(word):
    if word in data:
        for x in data[word]:
            print(x)
    elif word.title() in data: #for country name which start with a capital letter Eg-"Delhi,Paris"
        for x in data[word.title()]:
            print(x)
    elif word.upper() in data: #in case user enters words like USA or NATO
        for x in data[word.upper()] :
            print(x)            
    elif len(get_close_matches(word,data.keys(),cutoff=0.7))>0:
        predicted=get_close_matches(word,data.keys())[0]
        action=input("Did you mean %s ? (Y/N): " %predicted)
        if action=='y' or action=='Y':
            for x in data[predicted]:
                print(x)
        elif action=='n' or action=='N':
            return "The Entered word did not match"
        else:
            return "We didn't understand your input"    
            
            
    else:
        return "the word is doesn't exit please double check it."     

word=input("Enter the word: ")
word=word.lower()


meaning(word)