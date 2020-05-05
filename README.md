# Semantic Representations for Hindi

## Introduction

The aim of this project was to build word embeddings along with an evaluation criteria for Hindi. The following Algorithms were explored and implemented on the [IIT-B Parallel Corpus](http://www.cfilt.iitb.ac.in/iitb_parallel/).

- Word2Vec
- FastText
- BERT
- ELMO

The embeddings were analysed by using a custom list of Semantic, and Syantactic Analogies. [Here](https://github.com/agarwalchaitanya/Semantic-Representations-for-Indian-Languages), you'll find the implementation. [Here](https://docs.google.com/document/d/1wMU2sxNhnWa9rnUaseiPHYY2bzHP-mnojsn-wQNTa_k/edit?usp=sharing), you'll find the report.

## Running the scripts
```bash
$ pip3 install -r requirements.txt
$ cd src
$ python3 ft.py ../corpus/preprocess.hi ft.model
$ python3 w2v.py ../corpus/preprocess.hi w2v.model
$ python3 eval.py
$ ./bert.sh
```