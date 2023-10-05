import spacy
from termcolor import colored

# Load the French language model
nlp = spacy.load('fr_core_news_sm')

# Define the text to be analyzed
text = """Il essaie de te parler. """

# Process the text using spaCy
doc = nlp(text)

# Find all infinitive forms in the text
infinitives = [token for token in doc if token.morph.get('VerbForm') == ['Inf']]

# Print the infinitive forms
for infinitive in infinitives:
    print(infinitive)

for sent in doc.sents:
    sentence = []
    for token in sent:
        if token in infinitives:
            sentence.append(colored(token.text, 'red', attrs=['bold']))
        else:
            sentence.append(token.text)
    print(' '.join(sentence))