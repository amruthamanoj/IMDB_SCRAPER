from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

import os

#CREATE A DIRECTORY TO SAVE THE FILES AND SPECIFY ITS PATH

path = '/Users/apple/Desktop/py/series'
os.chdir(path)


#make a list for page numbers, each element of this list goes in for 'k' in url and we iterate over this
#or alternatively u can make a list of urls here

for z in range(0,200):
    indlist.append(z*50+1)
    
    
for k  in range(1,len(indlist)+1):

    #give the URL
    #identify the page listing patten, which goes in for 'k'; iterating over indlist of page numbers
    
    url = 'https://www.imdb.com/search/title/?title_type=tv_series&start=' + str(k) +'&ref_=adv_nxt'
    
    response = requests.get(url)
    soup=BeautifulSoup(response.text, 'lxml')
    print('processing page ', k )
    indlist = []
    names=[]
    years=[]
    genre=[]
    ratings=[]
    votes=[]
    links = []
    
    
    movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')
    for i in range(len(series_containers)):
        
        name = series_containers[i].h3.a.text
        names.append(name)
        
        year = series_containers[i].h3.find('span', class_ = 'lister-item-year').text
        years.append(year)
        try:
            l = series_containers[i].find('h3',class_ ='lister-item-header').a.get('href')
        except AttributeError:

            l = 'NA'
        links.append(l)
        
        try:
            r = series_containers[i].find('div', class_ = 'inline-block ratings-imdb-rating').strong.text
        except AttributeError:

            r = 'NA'
        ratings.append(r)
        try:
            v = (series_containers[i].find('p', class_="sort-num_votes-visible").text.replace('\n', '')).split(':')[1]
        except AttributeError:

            v = 'NA'
        votes.append(v)
        try:
            g = series_containers[i].p.find('span',class_ = 'genre').text.replace('\n', '')
        except AttributeError:

            g = 'NA'
        genre.append(g)
       
    # Store in a dictionary
    
    df = pd.DataFrame({'movie': names,
        'year': years,
        'rating': ratings,
        'genre': genre,
        'votes': votes,
        'link' : links
         })

    df.to_csv('series'+str(k)+'.csv', encoding='utf-8', index=False, header= True)
    
