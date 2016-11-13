from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier


def word_feats(words):
	return dict([(word, True) for word in words])

fid = movie_reviews.fileids('neg')
print(fid)

for f in fid:
	print()