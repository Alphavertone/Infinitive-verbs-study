import spacy
import pandas as pd
from termcolor import colored

def handle_infinitives(text):
    # Load the French language model
    nlp = spacy.load('fr_core_news_sm')
    # Process the text using spaCy
    doc = nlp(text)
    # Find all infinitive forms in the text
    infinitives = [token for token in doc if token.morph.get('VerbForm') == ['Inf']]
    sentences_with_infinitives = []
    for sent in doc.sents:
        has_infinitive = any(token in infinitives for token in sent)
        if has_infinitive:
            sentence = []
            for token in sent:
                if token in infinitives:
                    sentence.append(f"**{token.text}**")
                else:
                    sentence.append(token.text)
            sentences_with_infinitives.append(' '.join(sentence))
    return sentences_with_infinitives

import pandas as pd

def save_results(analyzed_data):
    # Load existing data from the Excel file, if it exists
    try:
        existing_data = pd.read_excel('output.xlsx')
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    # Create a DataFrame from the analyzed_data
    new_data = pd.DataFrame(analyzed_data, columns=['link', 'content'])

    # Append the new data to the existing data
    combined_data = existing_data._append(new_data, ignore_index=True)

    # Save the combined data to the Excel file
    combined_data.to_excel('output.xlsx', index=False)