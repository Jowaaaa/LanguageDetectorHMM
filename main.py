import pandas as pd
import re
import string


trigrams = list()
data = pd.read_csv('D:/Coding/Projects/HMM/Language_Detection.csv')
df = pd.DataFrame(data)
eng = df.loc[df['Language'] == 'English', 'Text'] #only print english text
#print(eng)
text = (df['Text'].to_string(index=False))


#Take the text and remove symbols and numbers specified in the function
def removeSymbolsAndNumbers(text):        
        text = re.sub(r'[{}]'.format(string.punctuation), '', text)
        text = re.sub(r'[\([{})\]!@#$,"%^*?:;~`]', ' ', text)
        text = re.sub(r"\\|[0-9]|/|-|_|'|\.", '', text)
        text = re.sub('\s+', ' ', text)  
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[@]', '', text)
        text = re.sub(r'[\([{})\]!@#$,"%^*?:;~`0-9]', ' ', text)
        text = text.lower()

        return text

removeSymbolsAndNumbers(text)

n = 3 # 1 = Unigram, 2 = bigram, 3 = trigram
text_len = len(text)
num_ngrams = text_len - n + 1 # How many ngrams of length n will fit in this text

def n_grams(text):
    
    
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

    sortedbyfreq = {k: v for k, v in sorted(dictionary.items(), key= lambda v: v[1], reverse=True)}
    #print (sortedbyfreq, end=" ") 
    for k, v in sortedbyfreq.items():
        print(k, ':', v / num_ngrams) #sorted by frequency on new line | divide by num_ngrams to get probability
    #print ("Frequency of ", allKeys, end = " ")
    #print (":", end = " ")
    #print (dictionary[allKeys], end = " ")
    #print()


def detectLanguage():
    x = input('Van welke tekst wil je de taal weten?')
    n = 3 # n in n-grams
    lenInput = len(x)
    num_ngrams = lenInput - n + 1 # How many ngrams of length n will fit in this text
    print(f"The text is {lenInput} characters long and will fit {num_ngrams} n-grams of length {n}.")

    for p in range(num_ngrams):
        print(f"{p}: {x[p:p+n]}")
    

#detectLanguage()

def ustandDataset (df):
    df.info() #basic information about data
    print(df['Language'].value_counts(normalize=True)*100)

#ustandDataset(df)
