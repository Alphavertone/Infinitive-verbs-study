import requests
from bs4 import BeautifulSoup
import time

def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    count = 0  # Counter to keep track of scraped links
    for div in soup.find_all("div", class_="fig-main"):
        for link in div.find_all("a"):
            href = link.get("href")
            if href and href.startswith("http"):
                links.append(href)
                count += 1
                if count == 40:  # Stop scraping after 20 links
                    break
        if count == 40:  # Stop scraping after 20 links
            break
    return links

def scrape_text(link):
    results = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(link, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad requests
        soup = BeautifulSoup(response.text, "html.parser")
        article_elements = soup.find_all('article')
        article_texts = []
        for article in article_elements:
            # Extract the text from the article
            article_text = article.get_text(separator=' ', strip=True)  # Join the text into a single piece
            article_texts.append(article_text)
        if article_texts:
            # Join all the articles into a single text block for the link
            link_text = ' '.join(article_texts)
            result = link, link_text
            results.append(result)
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {link}: {e}")
    except Exception as e:
        print(f"An error occurred for {link}: {e}")
    time.sleep(1)  # Add a 1-second delay between requests
    return link_text
