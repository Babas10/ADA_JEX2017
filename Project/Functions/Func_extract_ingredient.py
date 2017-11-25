import requests
from bs4 import BeautifulSoup
import string

def Func_extract_ingredient():
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