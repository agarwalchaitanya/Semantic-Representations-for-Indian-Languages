# Semantic Representations for Hindi

## Introduction

The aim of this project was to build word embeddings along with an evaluation criteria for Hindi. The following Algorithms were explored and implemented on the [IIT-B Parallel Corpus](http://www.cfilt.iitb.ac.in/iitb_parallel/).

- Word2Vec
- FastText
- BERT
- ELMo

The embeddings were analysed by using a custom list of Semantic, and Syantactic Analogies. [Here](https://github.com/agarwalchaitanya/Semantic-Representations-for-Indian-Languages), you'll find the implementation. [Here](https://docs.google.com/document/d/1wMU2sxNhnWa9rnUaseiPHYY2bzHP-mnojsn-wQNTa_k/edit?usp=sharing), you'll find the report.

## Running the scripts
Install the dependencies
```bash
$ pip3 install -r requirements.txt
```
You can generate `word2vec` and `fasttext` embeddings on the preprocessed corpus using
```bash
$ cd src
$ python3 ft.py ../corpus/preprocess.hi ft.model
$ python3 w2v.py ../corpus/preprocess.hi w2v.model
```
To evaluate the above models, use:
```bash
$ cd src
$ python3 eval.py
```
The `config` for `bert` hasn't been provided due to size constraints. However, you can train a 81M parameter `DistilBERT` like  `byte-level BPE tokenizer` on the preprocessed dataset using:
```bash
$ cd src/we
$ python3 bert.py
```
for generating embeddings, use
```bash
$ cd src
$ ./bert.sh
```

for generating a `biLm` model like `ELMo` use
```bash
$ cd src
$ ./elmos.sh
```