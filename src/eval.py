#!/bin/python3
from utils.reader import extract_text as et
from utils.tokenizer import hindi_tokenizer as ht

def preprocess_questions(path_to_questions):
    strings = et(path_to_questions)
    questions = ht(strings)
    return questions

def gensim_eval(w2v_model_path, ft_model_path, questions):
    from gensim.models import FastText
    from gensim.models import Word2Vec
    w2v = Word2Vec.load(w2v_model_path)
    ft = FastText.load(ft_model_path)

    w2v_score = 0
    ft_score = 0
    
    for question in questions:
        tmp = w2v.most_similar(positive=[question[0],question[2]], negative=[question[1]], topn=10)
        if question[3] in [i[0] for i in tmp]:
            w2v_score+=1
        tmp = ft.most_similar(positive=[question[0],question[2]], negative=[question[1]], topn=10)
        if question[3] in [i[0] for i in tmp]:
            ft_score+=1
    
    return w2v_score, ft_score

def main():
    questions = preprocess_questions('eval/smallquestions.txt')
    w2v, ft = gensim_eval('w2v.model', 'ft.model', questions)
    return w2v, ft

w2v, ft = main()
print(w2v, ft)








print(0, 0)
    