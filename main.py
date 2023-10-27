
import text_collector
import text_handler

url = "https://www.lefigaro.fr/secteur/high-tech"

links = []

links = text_collector.get_urls(url)

for link in links:
    content = text_collector.scrape_text(link)
    sentence = text_handler.handle_infinitives(content)
    analyzed_data = {
        'link': link,
        'content': sentence
    }
    text_handler.save_results(analyzed_data)

print("All infinitives were found!")