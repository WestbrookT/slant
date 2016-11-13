from pickle import load

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords
import itertools

sw = set(stopwords.words('english'))
score_fn = BigramAssocMeasures.chi_sq

f = open('classifier.py', 'rb')
cls = load(f)
f.close()

def word_feats(words):
	out = {}

	bigram_finder = BigramCollocationFinder.from_words(words)
	bigrams = bigram_finder.nbest(score_fn, n=10)

	for word in itertools.chain(words, bigrams):
		if word not in sw:
			out[word] = True
	return out