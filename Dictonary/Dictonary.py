# -*- coding: utf-8 -*-

import json
from difflib import get_close_matches

dataset = json.load(open("data.json"))

word = input("Enter the word: ")

def translate(word):
    word = word.lower()             # .lower() convert string to lowercase.
    if word in dataset:
        print("Meaning - ")
        meanings = dataset[word]
        for meaning in meanings:
            print("-> ",meaning)
    else:
        replacement = get_close_matches(word,dataset.keys(),n=1,cutoff=0.75)
#        "get_close_matches" is a function of difflib library that provides a close match available to a string with a defined ]
#    cutoff value(match-propability)
    
        if not replacement:
            print("Sorry! The word doesn't exist in dictonary.")
        else:
            response = input("Did you mean %s? If yes enter Y else N\n"% replacement[0]) 
            response.lower()
            if response is "y":
                translate(replacement[0])
            else:
                print("Sorry! The word doesn't exist in dictonary.")
                    
translate(word)
