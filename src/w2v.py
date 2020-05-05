from utils.preproc import preprocess
from utils.tokenizer import hindi_tokenizer
from utils.reader import extract_text
from we.word2vec import word2vec
import sys

def w2v(preprocessed_corpus_path, model_path, raw_corpus_path=None):
    if raw_corpus_path!=None:
        print("preprocessing")
        preprocess(raw_corpus_path, preprocessed_corpus_path)
        
    preprocessed_corpus = extract_text(preprocessed_corpus_path)
    print("tokenizing")
    sentences = hindi_tokenizer(preprocessed_corpus)

    print("training word2vec")
    word2vec(model_path, sentences)
    return model_path

if __name__=="__main__":
    w2v(sys.argv[1], sys.argv[2])
    
