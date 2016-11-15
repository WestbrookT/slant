from nltk.corpus import movie_reviews, stopwords
from nltk.classify import NaiveBayesClassifier, util
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import itertools
import json, pickle, nltk

score_fn = BigramAssocMeasures.chi_sq

sw = set(stopwords.words('english'))
sw.add('NPR')


def word_feats(words):
	out = {}

	bigram_finder = BigramCollocationFinder.from_words(words.lower().split(' '))
	bigrams = bigram_finder.nbest(score_fn, n=10)

	for word in itertools.chain(words.lower().split(' '), bigrams):

		if word not in sw:
			out[word] = True
	return out


def word_feats1(words):
	return dict([(word, True) for word in words])





def corpus(side, corpus):
	out = []
	for i in corpus[side]:

		out.append((word_feats(corpus[side][i]), side))

	return out

#0.6573511543134872


stuff = json.load(open('cleanarticles.json'))
right = corpus('right', stuff)
left = corpus('left', stuff)
neutral = corpus('neutral', stuff)

print(len(stuff['right'].keys()), len(stuff['left'].keys()), len(stuff['neutral'].keys()))

pos = 400

#
data = right[:300] + left[:300]
#  data = right[:pos] + left[:1843-pos] + neutral[:150]
test = right[300:600] + left[300:]



cls = NaiveBayesClassifier.train(data)
print('accuracy: ', nltk.classify.util.accuracy(cls, test))
#print(util.accuracy(cls, test))
f = open('classifier.py', 'wb')
pickle.dump(cls, f)
f.close()