import requests
from bs4 import BeautifulSoup

url = 'https://timesofindia.indiatimes.com/home/headlines'

def fetch_soup(url):
    """
    Return a BeautifulSoup object for the given url
    """
    response = requests.get(url)
    html = response.content
    return BeautifulSoup(html)

def parse_html(soup):
    """
    Returns a list of tuples (Headline, Article URL)
    """
    headlines = []
    for divtag in soup.find_all('div', {'class': 'headlines-list'}):
        for ultag in divtag.find_all('ul', {'class': 'clearfix'}):
            for litag in ultag.find_all('li'):
                # Assuming the headline text is the text content of the li tag
                headline_text = litag.text.strip()
                # Extracting the href attribute from the 'a' tag within the li
                article_url = "https://timesofindia.indiatimes.com" + litag.find('a')['href']
                headlines.append((headline_text, article_url))

    return headlines

soup = fetch_soup(url)
headlines = parse_html(soup)
print(len(headlines))
print(headlines)
import pandas as pd
df=pd.DataFrame(headlines,columns=['Headline','Article URL'])
df.to_csv('headlines.csv',index=False)
print(df.head(10))
