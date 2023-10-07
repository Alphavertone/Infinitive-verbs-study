
import text_collector
import text_handler

url = "https://www.lefigaro.fr/"

links = text_collector.get_urls(url)

analyzed_data = []

for link in links:
    content = text_collector.scrape_text(link)
    sentence = text_handler.handle_infinitives(content)
    analyzed_sentence = {
        "link": link,
        "sentence": sentence
    }
    analyzed_data.append(analyzed_sentence)

text_handler.save_results(analyzed_data)