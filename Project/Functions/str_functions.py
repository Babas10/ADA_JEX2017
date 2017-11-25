import pandas as pd
import re
import nltk
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tag import UnigramTagger
from nltk.corpus import brown
import webcolors
from nltk.stem import WordNetLemmatizer


def composedWords(x):
    if set('-').intersection(x[:][0]):
        return True

    else: return False

def quantityComposeWord(x,measure_quantity_list):

    decomposed = x.split('-')
    if (decomposed[0] in measure_quantity_list or decomposed[1] in measure_quantity_list):
        return decomposed
    else: return ' '

def usefullcomposedWords(x,measure_quantity_list):

    #We check if the word of interest is in between parenthesis
    if (set('(').intersection(x[:][0]) or set(')').intersection(x[:][0])):
        #if it's the case, we take them out
        inWord = re.sub('[(){}<>]', '', x[:][0])
        # We check if the word is a compose word, if it's the case we split it again and we check if it's a word
        # belonging to the measure quantity list
        if composedWords(x):
            decomposed = inWord.split('-')
            if (decomposed[0] in measure_quantity_list) or (decomposed[1] in measure_quantity_list[1]):
                return True
            else: return False
        # If it's not a composed word we check if it belong to the measure quantity list to keep it
        elif inWord in measure_quantity_list:
            return True
        else: return False

    else: return False


def conditionsSelection(x):

    #if set('-').intersection(x[:][0]):
    #    composedWord = x[:][0].split('-')
    #    y = pos_tag([composedWord])
    #    if composedWord[0]


    #if (x[:][1] in('JJ') and x[:][0] in (webcolors.CSS3_NAMES_TO_HEX)):
    #    return True
    if (x[:][1] not in('DT','PRP$','IN','JJ','RB','ADV','PRT','PRON','CC')):
        return True

    else: return False


def extract_ingredients(one_receipe,ingredients_list,techniques_list,units_list):
    ''' Function extractiing all ingredients, quantities and possiblity technics of cooking

    '''
    lemmatizer = WordNetLemmatizer()
    if '|' in one_receipe:
        ingredients=one_receipe.split('|')
    else:
        ingredients=one_receipe.split(', ')

    dic_ingre={}
    dic_tec={}
    for elem in ingredients:
        #split in words
        elem_list=elem.split(' ')
        #keep only alphanumerics in each words
        elem_list=[re.sub('[^0-9a-zA-Z/ ]+', '', x) for x in elem_list]
        #keep only the root of the word
        check = [lemmatizer.lemmatize(token) for token in elem_list]


        techniques=[]
        units=[]
        one_ingr=None
        for word in check:
            if word in techniques_list:  #check if it belongs to our technics list
                techniques.append(word)
            elif word in ingredients_list: #check if it belongs to our ingredient list
                one_ingr=word
            elif (word in units_list) or bool(re.search(r'\d',word)): #check if it belongs to our unit list or is alphanumeric
                units.append(word)
        for biword in nltk.bigrams(check): # check if we have a biword ingredient
            if ' '.join(biword) in ingredients_list:
                one_ingr=' '.join(biword)
        if one_ingr==None :        # check if we have no ingredient : avoid this element of recipe
            continue
        if len(units)==0:
            units.append('1 unit') # fill with a special unit if we are dealing with no quantity
        dic_ingre[one_ingr]=' '.join(units)
        dic_tec[one_ingr]=' '.join(techniques)

    return dic_ingre,dic_tec
