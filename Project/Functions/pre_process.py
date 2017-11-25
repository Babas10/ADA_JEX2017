import numpy as np
import pandas as pd
import re
import nltk
import itertools

from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tag import UnigramTagger
from nltk.corpus import brown

    
def partitionPar(string):
    ''' 
    ingridientSplited is splitted according to the parenthesis if there are any. 
    Example '3 (15 ounce) cans black beans, drained and rinsed' is splitted
    ('3 ', '(15 ounce)', ' cans black beans, drained and rinsed')  
    '''
    if parenthesisBool(string):
        partition = re.findall(r'\([^)]*\)|[^()]+', string)
        return partition
    else: return string.split(' ')


def parenthesisBool(ingridientSplited):
    '''
    True if there is a parenthesis in the string
    '''   
    if any(')' and '(' in x for x in ingridientSplited):
          return True
        
    else: return False
    
#def multipleparenthesis

def getParLoc(ingridientSplited):
    ''' Get the location of the parenthesis word '''
    loc = []
    for i, elem in enumerate(ingridientSplited):
        if ( ')' and '(' in elem):
            loc.append(i)
    return loc
        
        
def numerCheck(elem_list):
    if elem_list:
        if elem_list[0][1] == 'CD':
            return True
    
    else: return False
    
    
def inListElem(elem_list,checkList):
    if elem_list[:][0] == "":
        return False
    if elem_list[:][0] in checkList: 
        return True
    
    else: return False
        
        
        
def stringCorpusAnalysis(string):
    
    x = []
    newS = string.lstrip() #takes out space in the first element of string if one  
    if len(newS) == 2 and newS[1] == ' ': # We check for the special partern '3 '      
        x.append(pos_tag([newS[0]])[0]) # string[0] = '3' and pos_tag([string[0]])[0] = ('3', 'CD') it's usefull to avoint double list
        return x   
    if len(newS) == 1:
        x.append(pos_tag([newS[0]])[0])
        return x
    
    for w in newS.split(' '): #If the string has multiple words, we split in words and analyse one by one
        
        if len(w)>1:
            x.append(pos_tag([w])[0])
    return x

#Main function, that uses the all the others to make the checl        
def bef_af_parrenthesisCheck(ingridientSplited, loc, measure_quantity_list):
    
    # Ingridient is a list of strings ex: ('3 ', '(15 ounce)', ' cans black beans, drained and rinsed') 
    if loc == 0 or loc == len(ingridientSplited) - 1:
        return False
    
    # First Check if the word before the parenthesis is a number
    if (ingridientSplited[loc-1] != ' '):
        posParenthesis = stringCorpusAnalysis(ingridientSplited[loc-1]) # The word before the parenthesis posParenthesis = [('3','CD')]
        numberBol = numerCheck(posParenthesis) # We check if the string before the parenthesis is a number
        
    else : return False
    
    # Second Check, if the word after the parenthesis is in the measure list
    if (ingridientSplited[loc+1] != ' '):
        postParenthesis = ingridientSplited[loc+1]#.split(' ')
        y = stringCorpusAnalysis(postParenthesis)
    else : return False
    bolinList = inListElem(y[0],measure_quantity_list)
 
    
    if (numberBol and bolinList):
        return True
    else: return False
    
def removeFirstWordString(string):

    if string[0] == " ":
        newS = string[1:]
    else: newS = string

    splitS = newS.split(' ', 1)
    splitS = splitS[1:]
    sentence = ""
    for i , words in enumerate(splitS):
        sentence += str(words)        
    return sentence

def composedWords(x):
    if set('-').intersection(x):
        return True
    
    else: return False
    
def quantityComposeWord(x):
    
    decomposed = x.split('-')
    if (decomposed[0] in measure_quantity_list or decomposed[1] in measure_quantity_list):
        return decomposed
    else: return ' '
    
    
def Usefull_parenthesis(string,loc, list_to_check):

    decomposed = string[loc[0]].strip("()").split(' ') # We get rid of the parenthesis

    if any(decomposed) in list_to_check:
        return True
    else: return False
    
def delParenthesis(ingridient,loc):
    
    sentence = ""
    count = 0
    for i in loc:
        
        if count == 0:          
            del ingridient[i]
        else: 
            del ingridient[i-count]
        count += 1
    
    for j,words in enumerate(ingridient):
        
        sentence += str(words)        
    return sentence 