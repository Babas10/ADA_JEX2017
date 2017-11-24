import pandas as pd
import re
import nltk
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tag import UnigramTagger
from nltk.corpus import brown
import webcolors



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


    if (x[:][1] in('JJ') and x[:][0] in (webcolors.CSS3_NAMES_TO_HEX)):
        return True
    if (x[:][1] not in('DT','PRP$','IN','JJ','RB','ADV','PRT','PRON')):
        return True

    else: return False


def extract_ingredients_quantities(one_receipe,measure_quantity_list):

    if '|' in one_receipe:
        ingredients=one_receipe.split('|')
    else:
        ingredients=one_receipe.split(', ')

    dic_ingre={}
    dic_tec={}
    for elem in ingredients:

        sent = sum([pos_tag([w]) for w in elem.split(' ')],[])

        a = list(filter(lambda x: conditionsSelection(x), sent))
        elem_list=[]
        techniques=[]
        for w,t in a:
            if t=='VBN':
                techniques.append(w)
            else:
                elem_list.append(w)


        if (bool(re.search(r'\d', elem_list[0]))):
            add=1
            while (elem_list[add] in measure_quantity_list) or bool(re.search(r'\d',elem_list[add])):
                add=add+1

            s_ingredient=' '.join(elem_list[add:])

            parenthesis_del = re.compile('\(.+?\)')
            s_ingredient = parenthesis_del.sub('', s_ingredient)

            if 'or ' in s_ingredient:
                split=s_ingredient.split('or ')
                if 'taste' in split[1] or bool(re.search(r'\d', split[1])):
                    s_ingredient=split[0]
                else: s_ingredient=split[1]

            dic_ingre[s_ingredient.replace(',','')]=' '.join(elem_list[0:add])
            dic_tec[s_ingredient.replace(',','')]=techniques

    return dic_ingre,dic_tec
