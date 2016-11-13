from sqlalchemy import create_engine, Column, String, Integer, Float
from db import Base
from newspaper import Article, nlp
from cls import cls

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords

sw = set(stopwords.words('english'))

import itertools

score_fn = BigramAssocMeasures.chi_sq



class Page(Base):

	__tablename__ = 'pages'

	id = Column(Integer, primary_key=True)
	content = Column(String)
	keywords = Column(String)
	link = Column(String, unique=True)
	lean = Column(Float)
	img = Column(String)



	def link_init(self, link):
		pass

	def __init__(self, link, text=None, img=None):
		if text == None:
			article = Article(link)
			article.download()
			article.parse()

			content = article.text

			keywords = ''

			for i in nlp.keywords(content):
				keywords += i.lower() + ' '

			self.content = content.lower()
			self.keywords = keywords
			self.link = link
			self.img = article.top_image

			vals = {'right': 0, 'left': 1, 'neutral': .5}

			self.lean = vals[cls.classify(self.word_feats(content))]
			return


		self.content = text.lower()

		keywords = ''

		for i in nlp.keywords(text):
			keywords += i.lower() + ' '
		self.link = link
		self.keywords = keywords
		self.img = img
		vals = {'right': 0, 'left': 1, 'neutral': .5}



		self.lean = self.classify(text.lower())


	def word_feats(self, words):
		out = []

		bigram_finder = BigramCollocationFinder.from_words(words)
		bigrams = bigram_finder.nbest(score_fn, n=10)



		for i, sentence in enumerate(words.split('.')):
			out.append({})
			for word in itertools.chain(sentence, bigrams):
				if word not in sw:
					out[i][word] = True
		return out

	def classify(self, words):

		bag = self.word_feats(words)
		out = 0
		count = 0
		vals = {'right': 0, 'left': 1, 'neutral': .5}
		for sentence in bag:
			count += 1
			out += vals[cls.classify(sentence)]

		if count == 0:
			count = 1
		return out/count


# data = {'url':{'img':'string', 'article':'string'}}