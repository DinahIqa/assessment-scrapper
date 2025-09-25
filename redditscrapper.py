import requests
import json
import time
from bs4 import BeautifulSoup

#def getsoup(url):
#    response = requests.get(url, headers)
#    return response.text

# url = "https://www.reddit.com/r/uofm/"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
# page = requests.get(url, headers=headers)
# soup = BeautifulSoup(page.text, 'html.parser')

# print(soup)

# domains = soup.find_all("span", class_="domain")
# for domain in domains:
#     if domain != "(self.uofm)":
#         continue

#     print(domain.text)

##try json
base_url = "https://www.reddit.com/r/uofm/.json"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}


image_post = []
after = None

for i in range(2):
    url = base_url if not after else f"{base_url}?after={after}"
    print("Fetching: ", url)
    page = requests.get(url, headers=headers)
    json_data = page.json()

    for post in json_data["data"]["children"]:
        post_data = post["data"]
        post_title = post_data["title"]
        image_url = post_data.get("url_overridden_by_dest")

        if image_url:
            image_post.append({
                "post_title": post_title,
                "image_url": image_url
            })
    
    after = json_data["data"].get("after") # to go to the next page
    if not after:
        break

    time.sleep(2)

with open("redditdata.json", "w", encoding="utf-8") as f:
    json.dump(image_post, f, indent=2)


