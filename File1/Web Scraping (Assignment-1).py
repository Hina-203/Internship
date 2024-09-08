#!/usr/bin/env python
# coding: utf-8

#                            ASSIGNMENT-1

# Q: 1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame.

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://www.imdb.com/list/ls056092300/")

soup = BeautifulSoup(url.content, 'html.parser')

movies = soup.find_all('div', class_='lister-item mode-detail')

names = []
ratings = []
yearsofrelease = []

for movie in movies:
    name = movie.h3.a.text.strip()
    rating = movie.strong.text.strip()
    year = movie.h3.find('span', class_='lister-item-year').text.strip()
    names.append(title)
    ratings.append(rating)
    yearsofrelease.append(year)

movies_df = pd.DataFrame({
    'Name': names,
    'Rating': ratings,
    'Year of Release': yearsofrelease})

print(movies_df)


# 
# 

# Q:2) Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the
# heading, date, content and the likes for the video from the link for the youtube video from the post.

# In[6]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='Card-titleContainer')  

for article in articles:
    heading_element = article.find('a', class_='Card-title')
    if heading_element:
        heading = heading_element.text.strip()
    else:
        heading = "No heading found"

    date_element = article.find('time', class_='Card-time')  
    if date_element:
        date = date_element.text.strip()
    else:
        date = "No date found"

    link_element = article.find('a', href=True)
    if link_element:
        news_link = link_element['href']
    else:
        news_link = "No link found"

    print(f"Heading: {heading}")
    print(f"Date: {date}")
    print(f"News Link: {news_link}\n")


# 
# 
# 

# Q:3 Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,
# Rajaji

# In[7]:


import requests
from bs4 import BeautifulSoup

# Define the localities
localities = ["Indira Nagar", "Jayanagar", "Rajaji Nagar"]

# Iterate over each locality
for locality in localities:
    url = f"https://www.nobroker.in/property/sale/bangalore/{locality.lower().replace(' ', '-')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print(f"Scraping houses in {locality}...\n")
    
    # Find all house containers
    houses = soup.find_all('div', class_='card')
    
    for house in houses:
        # Extract house title
        title_element = house.find('h2', class_='heading-6')
        title = title_element.text.strip() if title_element else "No title found"

        # Extract location
        location_element = house.find('h1', class_='text-16')
        location = location_element.text.strip() if location_element else "No location found"

        # Extract area
        area_element = house.find('p', class_='text-left pl-1.5p ab:p-0 tab:text-12 tab:mt-0.5p tab:mb-0 tab:pl-0') 
        area = area_element.text.strip() if area_element else "No area found"

        # Extract EMI
        emi_element = house.find('div', class_='font-semi-bold')
        emi = emi_element.text.strip() if emi_element else "No EMI found"

        # Extract price
        price_element = house.find('span', class_='text-18 font-bold')
        price = price_element.text.strip() if price_element else "No price found"

        # Print the details
        print("Title:", title)
        print("Location:", location)
        print("Area:", area)
        print("EMI:", emi)
        print("Price:", price)
        print()
    
    print("="*50)


#     

# 4) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/bestseller?sort=popular .

# In[ ]:


import requests
from bs4 import BeautifulSoup

url = "https://www.bewakoof.com/bestseller?sort=popular%20"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_='categoryWrapper')[:10]

for product in products:
    # Product Name
    name_element = product.find('h1', class_='ProductName')
    name = name_element.text.strip() if name_element else "No name found"
    
    # Product Price
    price_element = product.find('div', class_='discountedPriceText clr-p-black   false')
    price = price_element.text.strip() if price_element else "No price found"
    
    # Image URL
    image_element = product.find('div',class_='productImg')
    if image_element and 'data-src' in image_element.attrs:
        image_url = image_element['data-src']
    else:
        image_url = "No image URL found"

    print(f"Product Name: {name}")
    print(f"Price: {price}")
    print(f"Image URL: {image_url}\n")



#    

# Q: 5) Please visit https://www.cnbc.com/world/?region=world and scrap
# a)headings
# b) date
# c) News link

# In[46]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='Card-titleContainer')  

for article in articles:
    heading_element = article.find('a', class_='Card-title')
    if heading_element:
        heading = heading_element.text.strip()
    else:
        heading = "No heading found"

    date_element = article.find('time', class_='Card-time')  
    if date_element:
        date = date_element.text.strip()
    else:
        date = "No date found"

    link_element = article.find('a', href=True)
    if link_element:
        news_link = link_element['href']
    else:
        news_link = "No link found"

    print(f"Heading: {heading}")
    print(f"Date: {date}")
    print(f"News Link: {news_link}\n")


#    

# Q: 6) Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/
# and scrap
# 
# a)Paper title
# b) date
# c) Author

# In[45]:


import requests
from bs4 import BeautifulSoup

url = "https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='article-listing')

for article in articles:
    # Paper Title
    title_element = article.find('h2', class_='h5 article-title')
    title = title_element.text.strip() if title_element else "No title found"
    
    # Date
    date_element = article.find('p', class_= 'article-date')
    date = date_element.text.strip() if date_element else "No date found"
    
    # Author
    author_element = article.find('p', class_='article-authors')
    author = author_element.text.strip() if author_element else "No author found"

    print(f"Paper Title: {title}")
    print(f"Date: {date}")
    print(f"Author: {author}\n")

