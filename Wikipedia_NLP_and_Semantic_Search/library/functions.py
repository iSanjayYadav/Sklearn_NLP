import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import string
import pickle

def jsonify_wiki_category (category_name): 
    '''
    Insert category name as a string, note that this is case sensitive
    Make sure to import requests 
    Make sure to import pandas 
    '''
    base_url = 'https://en.wikipedia.org/w/api.php'
    action = '?action=query'
    parameters = '&list=categorymembers' + '&cmtitle='
    params = '&cmlimit=max'
    form = '&format=json'
    
    category_name_url = base_url + action + parameters + category_name + params + form
    category_name_response = requests.get(category_name_url)
    category_name_json = category_name_response.json()
    return category_name_json


def dfize_category_names (category_name):
    '''
    takes a category name formatted as 'Category:_____'
    '''
    category_name_json = jsonify_wiki_category(category_name)
    category_name_df = pd.DataFrame(category_name_json['query']['categorymembers'])
    category_name_df['category'] = [category_name for pageid in category_name_df['pageid'] if pageid!=0]
    
    return category_name_df


def dfize_cat_articles_only (category_name):
    category_name_df = dfize_category_names(category_name)
    articles_list = []
    
    category_mask = category_name_df['title'].str.contains('Category:')
    articles_df = category_name_df[~category_mask]
    articles_list.append(articles_df)
    article_titles_list = articles_df['title'].tolist()
    
    return articles_df



def list_subcategories (category_name):
    category_name_df = dfize_category_names(category_name)
    subcat_list = []
    
    category_mask = category_name_df['title'].str.contains('Category:')
    subcat_df = category_name_df[category_mask]
    subcat_list.append(subcat_df)
    #category_name_df = pd.concat(subcat_list)
    subcat_list = subcat_df['title'].tolist()
    
    return subcat_list



def dfize_subcategory_article (category_name):
    subcat_list = list_subcategories(category_name)
    subcat_temp = []
    
    for subcat in subcat_list:
        df = dfize_category_names(subcat)
        category_mask = df['title'].str.contains('Category:')
        
        df_articles_only = df[~category_mask]
        
        subcat_temp.append(df_articles_only)
        df = pd.concat(subcat_temp)    

    return df



def jsonify_wiki_article (article_name): 
    '''
    Insert category name as a string, note that this is case sensitive
    Make sure to import requests first before using this functiona
    '''
    base_url = 'https://en.wikipedia.org/w/api.php'
    action = '?action=parse'
    prop = '&page='
    form = '&format=json'
    
    article_name_url = base_url + action + prop + article_name + form
    article_name_response = requests.get(article_name_url)
    article_name_json = article_name_response.json()
    return article_name_json



def htmlify_wiki_article (article_name):
    article_name_json = jsonify_wiki_article(article_name)
    article_name_html = article_name_json['parse']['text']['*'] if not article_name_json.get('error') else ''
    return article_name_html


def beautify_html_article (article_name):
    article_name_html = htmlify_wiki_article(article_name)
    soup = BeautifulSoup(article_name_html, 'html.parser')
    article_text = soup.get_text().replace('\n', '')
    return article_text



def text_cleaner(text):
    text = re.sub('[\.]',' ',text)
    text = re.sub('([^A-Za-z0-9_])\W+',' ', text)
    text = re.sub('\W',' ',text.lower())
    text = re.sub('\d','', text)
    text = re.sub('[\_]', ' ', text)
    return text



def tokenize (text):
    clean_text = text_cleaner(text)
    return clean_text.lower().split() 


