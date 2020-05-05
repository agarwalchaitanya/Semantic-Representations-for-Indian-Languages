#!/bin/python3
from gensim.models import Word2Vec, KeyedVectors
from gensim.test.utils import get_tmpfile

def word2vec(model_path, sentences):
    '''
    https://radimrehurek.com/gensim/models/word2vec.html
    model_path should have a .model extension
    sentences: list of list of strings(tokens)
    '''

    model = Word2Vec(sentences, min_count=1)
    word_vectors = model.wv
    model.save(model_path)
    return model_path

def get_embeddings(model_path, words):
    '''
    model_path should have a .kv extension
    words: list of strings(tokens)
    '''
    model = Word2Vec.load(model_path)
    word_vectors = model.wv
    return [word_vectors[word] for word in words]

def most_similar(model_path, pairs_of_positives, negatives):
    '''
    pairs_of_positives: list of 2d lists
    negatives: list of strings
    '''
    model = Word2Vec.load(model_path)
    word_vectors = model.wv
    return [word_vectors.most_similar(positive=postive, negative=[negative])[0] for positive, negative in zip(pairs_of_positives, negatives)]
    
if __name__=="__main__":
    pass