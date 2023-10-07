import requests
from bs4 import BeautifulSoup


def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith("http"):
            links.append(href)
    return links

def scrape_text(links):
    results = []
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        content_body = soup.find(class_="fig-content-body")
        if content_body:
            text = content_body.get_text(strip=True)
            result = {
                "link": link,
                "text": text
            }
            results.append(result)
    return results