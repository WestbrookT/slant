from nltk.corpus import movie_reviews, stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import itertools

score_fn = BigramAssocMeasures.chi_sq

sw = set(stopwords.words('english'))

def word_feats(words):
	out = {}

	bigram_finder = BigramCollocationFinder.from_words(words)
	bigrams = bigram_finder.nbest(score_fn, n=10)

	for word in itertools.chain(words, bigrams):
		if word not in sw:
			out[word] = True
	return out







def corpus(side, corpus):
	out = []
	for i in corpus[side]:

		out.append((word_feats(corpus[side][i]), side))

	return out




stuff = {'right': {'url':'donald trump'}, 'left': {'url': 'hillary'}}
right = corpus('right', stuff)
left = corpus('left', stuff)

cls = NaiveBayesClassifier.train(right+left)

print(cls.classify(word_feats("red")))