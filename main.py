import pandas as pd
import re
import string
import collections


trigrams = list()
data = pd.read_csv('D:/Coding/Projects/HMM/Language_Detection.csv')
df = pd.DataFrame(data)

text = (df['Text'].to_string(index=False))


#Take the text and remove symbols and numbers specified in the function
def removeSymbolsAndNumbers(text):        
        text = re.sub(r'[{}]'.format(string.punctuation), '', text)
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[@]', '', text)

        return text.lower()

removeSymbolsAndNumbers(text)


def n_grams(text):
    n = 3 # 1 = Unigram, 2 = bigram, 3 = trigram
    text_len = len(text)
    num_ngrams = text_len - n + 1 # How many ngrams of length n will fit in this text
    print(f"The text is {text_len} characters long and will fit {num_ngrams} n-grams of length {n}.")

    for p in range(num_ngrams):
        #print(f"{p}: {text[p:p+n]}")
        trigrams.append(text[p:p+n])
    return trigrams
                

n_grams(text)


def count(elements):
    # if there exists a key as "elements" then simply
    # increase its value.
    if elements in dictionary:
        dictionary[elements] += 1
 
    # if the dictionary does not have the key as "elements"
    # then create a key "elements" and assign its value to 1.
    else:
        dictionary.update({elements: 1})

dictionary = {}

for elements in trigrams:
    count(elements)


for allKeys in dictionary:
    print ("Frequency of ", allKeys, end = " ")
    print (":", end = " ")
    print (dictionary[allKeys], end = " ")
    print()