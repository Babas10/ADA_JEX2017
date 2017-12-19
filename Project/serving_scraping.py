import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def fun_sparkpeople_scrap(url):
    # recipes.sparkpeople.com
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('div', class_='prep_box_w')
        for a in stat.find('span',itemprop='recipeYield'):
            return a
        
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass


def fun_foodnetwork_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('section', class_='o-RecipeInfo o-Yield')
        for a in stat.find('dd',class_='o-RecipeInfo__a-Description'):
            temp = re.findall(r'\d+', a)
            servings = int(temp[0])
            return servings
        
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass

    
def fun_cdkitchen_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('div', class_='col-md-4 col-sm-4 mb-20')
        for a in stat.find('form', class_='change-servs-form'):
            servings = a.get('value')
            return servings
        
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass
    
def fun_Allrecipes_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('span', class_='recipe-ingredients__header__toggles')
        for a in stat.find_all('meta'):
            servings = a.get('content')
            return servings
        
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass 
    

    
def fun_food_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('div', class_='recipe-body-wrapper')
        for a in stat.find('span', class_='count'):
            servings = a
            return servings
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass

def fun_Myrecipes_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('div', class_='recipe-meta-container clearfix')
        for a in stat.find_all('div', class_='recipe-meta-item-body'):
            temp = a.get_text()
            if 'serving' in temp:
                serv = re.findall(r'\d+', temp)
                servings = int(serv[0]) 
                return servings        
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass
    

def fun_bettycrocker_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('div', class_='recipePartAttributes recipePartPrimaryAttributes')
        for a in stat.find('span', class_='attributeValue'):
            return int(a)
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass
    
def fun_cookeatshare_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('div', class_='recipe-summary')
        for a in stat.find('span', itemprop='recipeYield'):
            serv = re.findall(r'\d+', a)
            servings = int(serv[0])
            return servings
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass
    
def fun_eatingwell_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('h2', class_='headingH2GuttersIngredients')
        for a in stat.find_all('meta'):
            servings = a.get('content')
            return servings       
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass
    
def fun_delish_scrap(url):
    
    try: # We try if the website exist and have the information concerning the servings
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('div', class_='recipe-info-item recipe-info-serves')
        serv = re.findall(r'\d+', stat.get_text())
        servings = int(serv[0])
        return servings
    except Exception: # if the website doesn't contain the necessary information we return 0 servings
        return 0
    pass

    
def fun_serving_scrapI(domain,url):
    
    if domain == 'recipes.sparkpeople.com':
        servings = fun_sparkpeople_scrap(url)
        return servings
        

    ## foodnetwork.com
    elif domain == 'foodnetwork.com':
        servings = fun_foodnetwork_scrap(url)
        return servings

    ## cdkitchen.com        
    elif domain == 'cdkitchen.com':
        servings = fun_cdkitchen_scrap(url)
        return servings
        
        
    ## Allrecipes.com        
    elif domain == 'allrecipes.com':
        servings = fun_Allrecipes_scrap(url)
        return servings
        
        
    ## Food.com    
    elif domain == 'food.com':
        servings = fun_food_scrap(url)
        return servings

    ## Myrecipes.com
    elif domain == 'myrecipes.com':
        servings = fun_Myrecipes_scrap(url)
        return servings

    ## Bettycrocker.com    
    elif domain == 'bettycrocker.com':
        servings = fun_bettycrocker_scrap(url)
        return servings

    ## Cookeatshare.com    
    elif domain == 'cookeatshare.com':
        servings = fun_cookeatshare_scrap(url)
        return servings

    ## eatingwell.com    
    elif domain == 'eatingwell.com':
        servings = fun_eatingwell_scrap(url)
        return servings

    ## delish.com    
    elif domain == 'delish.com':
        servings = fun_delish_scrap(url)
        return servings
    else:
        return  0