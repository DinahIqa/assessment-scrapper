import requests
import json
import time
from bs4 import BeautifulSoup

#def getsoup(url):
#    response = requests.get(url, headers)
#    return response.text

url = "https://www.reddit.com/r/uofm/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)

domains = soup.find_all("span", class_="domain")
for domain in domains:
    if domain != "(self.uofm)":
        continue

    print(domain.text)