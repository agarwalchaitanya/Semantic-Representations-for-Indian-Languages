import numpy as np
import embeddingsfile

questions = open('questions.txt', 'r') #This contains the tests

score = 0
numclose = 3 #Higher the value higher the chance of passing the test. Increase the value if scores are too low. Decrease if scores are too high

for sent in questions:
	count = 0
	arr = sent.split(' ')
	final = np.subtract(embeddingsfile[arr[0]], embeddingsfile[arr[1]])
	final = np.add(final, embeddingsfile[arr[2]])
	
	sortedDict = sorted(embeddingsfilem key=lambda x:np.dot(embeddingsfile[x], final)/(np.linalg.norm(embeddingsfile[x])*np.linalg.norm(final)))
	
	for key in sortedDict and count < numclose:
		closest.append(key)
		count = count + 1

	if final in closest:
		score = score + 1
print(f"Score : {score}")
		
