import requests
from bs4 import BeautifulSoup

url = "https://www.lefigaro.fr/"

def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith("http"):
            links.append(href)

def scrape_text_from_links(links):
    texts = []
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        content_body = soup.find(class_="fig-content-body")
        if content_body:
            text = content_body.get_text(strip=True)
            texts.append(text)
    return texts