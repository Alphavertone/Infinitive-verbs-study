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


def save_results(analyzed_data):
    # Create a DataFrame from the analyzed_data
    df = pd.DataFrame(analyzed_data, columns=['link', 'sentence'])

    # Save DataFrame to Excel file
    df.to_excel('output.xlsx', index=False)


