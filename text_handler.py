import spacy
from termcolor import colored

# Load the French language model
nlp = spacy.load('fr_core_news_sm')

# Define the text to be analyzed
text = """Il essaie de te parler. """

def handle_infinitives(text):
    # Process the text using spaCy
    doc = nlp(text)

    # Find all infinitive forms in the text
    infinitives = [token for token in doc if token.morph.get('VerbForm') == ['Inf']]

    for sent in doc.sents:
        sentence = []
        for token in sent:
            if token in infinitives:
                sentence.append(colored(token.text, 'red', attrs=['bold']))
            else:
                sentence.append(token.text)
        print(' '.join(sentence))
    return(sentence)