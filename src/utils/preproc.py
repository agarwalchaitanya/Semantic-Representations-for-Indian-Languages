import re
import sys
from tqdm import tqdm

def preprocess(infile_path, outfile_path):
	'''
	cleans corpus
	'''
	infile = open(infile_path)
	outfile = open(outfile_path, 'w')
	
	for text in tqdm(infile.readlines()):
		text = text.strip('\n')
		if text:
			text = re.sub(r'(\d),(\d)', r'\1\2', text)
			text = text.replace(u',', ' ,')
			text = text.replace(u'।', ' ।')
			text = re.sub('.\n', ' .\n', text)
			text = text.replace(u')', ' )')
			text = text.replace(u'(', '( ')
			text = text.replace(u"''", '')
			text = text.replace(u"'", " ' ")
			text = text.replace(u'!', ' !')
			text = text.replace(u'?', ' ?')
			text = text.replace(u'""', '')
			text = text.replace(u'"', ' " ')
			text = text.replace(u'-', ' - ')
			text = text.replace(u':', ' : ')
			text = re.sub(r"(\d+(\.\d+)?)",r" \1 ", text)
			text = re.sub('^ ', '', text)
			text = re.sub(' +', ' ', text)
			print(text, file = outfile)

if __name__=="__main__":
	infile_path = sys.argv[1]
	outfile_path = sys.argv[2]
	preprocess(infile_path, outfile_path)