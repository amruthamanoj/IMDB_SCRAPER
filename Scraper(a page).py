from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
path = '/Users/apple/Desktop/py/series'
os.chdir(path)
url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
response = requests.get(url)
soup=BeautifulSoup(response.text, 'lxml')


names=[]
years=[]
genre=[]
ratings=[]
votes=[]
links = []
    
    
movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')
for i in range(len(movie_containers)):
        
    name = movie_containers[i].h3.a.text
    names.append(name)
        # The year
    year = movie_containers[i].h3.find('span', class_ = 'lister-item-year').text
    years.append(year)
    try:
        l = movie_containers[1].find('h3',class_ ='lister-item-header').a.get('href')
    except AttributeError:

        l = 'NA'
    links.append(l)
        
    try:
        r = movie_containers[i].find('div', class_ = 'inline-block ratings-imdb-rating').strong.text
    except AttributeError:

        r = 'NA'
    ratings.append(r)
    try:
        v = (movie_containers[i].find('p', class_="sort-num_votes-visible").text.replace('\n', '')).split(':')[1]
    except AttributeError:

        v = 'NA'
    votes.append(v)
    try:
        g = movie_containers[i].p.find('span',class_ = 'genre').text.replace('\n', '')
    except AttributeError:

        g = 'NA'
    genre.append(g)
       
    # Store each item into dictionary (data), then put those into a list (imdb)
df = pd.DataFrame({'movie': names,
        'year': years,
        'rating': ratings,
        'genre': genre,
        'votes': votes,
        'link' : links
         })


    
def fun(s):

    p = 'imdb.com' + s
    return p

df['link'] = df['link'].apply(fun)
df
