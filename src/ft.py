from utils.preproc import preprocess
from utils.tokenizer import hindi_tokenizer
from utils.reader import extract_text
from we.fasttext import fasttext as ft
import sys

def fasttext(preprocessed_corpus_path, model_path, raw_corpus_path=None):
    if raw_corpus_path!=None:
        print("preprocessing")
        preprocess(raw_corpus_path, preprocessed_corpus_path)
        
    preprocessed_corpus = extract_text(preprocessed_corpus_path)
    print("tokenizing")
    sentences = hindi_tokenizer(preprocessed_corpus)

    print("training fasttext")
    ft(model_path, sentences)
    return model_path

if __name__=="__main__":
    fasttext(sys.argv[1], sys.argv[2])
    
