import numpy as np
import pandas as pd
import re
import nltk
import itertools
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tag import UnigramTagger
from nltk.corpus import brown
import requests
from bs4 import BeautifulSoup
import string

def verbeSelection(x):

    if (x[:][1] == 'VBN'):
        return True

    else: return False
    
def technique_list(dataset):    
    techniqueList = []
    for j in range(len(dataset)):
        a=dataset.loc[j]['ingredients_list']
        if '|' in a:
            ingredients=a.split('|')
        else:  
            ingredients=a.split(', ')

        recepie = ""
        for i, elem in enumerate(ingredients):
            regex = re.compile('[,\.!?%#*-]')
            elem=regex.sub('', elem)

            sent=pos_tag(nltk.word_tokenize(elem))

            a = list(filter(lambda x: verbeSelection(x), sent))
            if len(a)>0 and a[0][0] not in techniqueList:
                if a[0][0][-2:] == 'ed':
                    techniqueList.append(a[0][0])
                    
def extract_ingredient():
    ingredient =[]
    alphabet = list(string.ascii_lowercase)
    alphabet.remove('x')
    for letter in (alphabet):
        url='http://www.bbc.co.uk/food/ingredients/by/letter/'+ letter
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('ol', class_='resources foods grid-view')
        for a in stat.find_all('li',class_='resource food'):
            ingredient.append(a.get('id'))
        
    ingredient_list = list(map(lambda x: x.replace('_',' '), ingredient))
    with open('Ingredient_list.txt', 'w') as f:
        for s in ingredient_list:
            f.write(s + '\n')
    print('Ingredient_list.txt has been created') 
