import os
import sys
import random
import re

def normalizeTextForAlgo(text):

    chars = ",.;/:!()[]-"
    text = text.replace("...", "3DOTS")
    
    for c in chars:
        text = text.replace(c, " " + c + " ")

    text = text.replace("\n", " \n")
    text = text.replace("   ","  ")
    text = text.replace("  ", " ")

    #text = text.replace("\n", " ")
    text = text.replace("\t"," ")
    text = text.replace("3DOTS", "...")

    return text

def normalizeTextForReading(text):
    chars = ",.;/:!()[]-"

    for c in chars:
        text = text.replace(" "+c, c)

    return text

def createChainFromText(text):
    chain = {}

    text = normalizeTextForAlgo(text)
    splited_data = text.split(" ")

    for i in range(2, len(splited_data)):
        groupWords = splited_data[i-2].lower() + " " + splited_data[i-1].lower()
        if groupWords not in chain.keys():
            chain[groupWords] = []

    for i in range(2, len(splited_data)):
        chain[splited_data[i-2].lower() + " " + splited_data[i-1].lower()].append(splited_data[i].lower())

    return chain

def createTextFromChaine(chaine, start, length):
    current = start
    generate = start.split(" ") 

    while len(current) >= 3 and len(chain[current]) > 0 and len(generate) < length:
        new = chain[current][random.randint(0, len(chain[current]) - 1)]
        current = generate[-1] + " " + new
        generate. append(new)

    return " ".join(generate)

path = sys.argv[1]
file = open(path,'r')
text = file.read()

chain = createChainFromText(text)

keys = list(chain.keys())
first = keys[0]


generatedText = createTextFromChaine(chain, first, 500)
generatedText = normalizeTextForReading(generatedText)
print(generatedText)
os.system("pause")
