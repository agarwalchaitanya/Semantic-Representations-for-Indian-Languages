#!/bin/python3

def extract_text(path_to_text):
    f = open(path_to_text)
    f = f.readlines()
    return [sent.rstrip('\n') for sent in f]
    
if __name__=="__main__":
    dev_path = '../../dev_test/dev.hi'
    list_of_strings = extract_text(dev_path)
    for string in list_of_strings:
        assert type(string)==str
