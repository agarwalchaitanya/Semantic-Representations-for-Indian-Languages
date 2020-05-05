#!/bin/python3
import spacy
from tqdm import tqdm

def hindi_tokenizer(list_of_strings):
    '''
    using the multilingual model by spacy;
    find the docs at https://spacy.io/models/xx
    '''
    nlp = spacy.load("xx_ent_wiki_sm")
    tokenized_strings = []
    
    for string in tqdm(list_of_strings):
        if type(string)==str:
            doc = nlp(string)
            tokenized_strings.append([token.text for token in doc])
    return tokenized_strings


if __name__=="__main__":
    from reader import extract_text
    dev_path = '../../dev_test/dev.hi'
    list_of_strings = extract_text(dev_path)
    strings = hindi_tokenizer(list_of_strings)
    print(strings)
    
