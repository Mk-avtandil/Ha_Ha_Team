import requests
import json
from bs4 import BeautifulSoup

JSON = 'kloop.json'
URL = 'https://kloop.kg/news/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
}

def get_content():
    r = requests.get(url=URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('article', class_='elementor-post')
    new_posts = []

    for item in items:
        new_posts.append({
            "title" : item.find('h3', class_ = 'elementor-post__title').get_text(strip="True"),
            "data" : item.find('span', class_ = 'elementor-post-date').get_text(strip="True"),
            'photo' : item.find('img').get('src'),
            'link' : item.find('a').get('href'),
        })

    with open('news.json', 'w') as file:
        json.dump(new_posts, file, indent=4, ensure_ascii=False)


def main():
    get_content()

if __name__ == "__main__":
    main()