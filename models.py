from sqlalchemy import create_engine, Column, String, Integer, Float
from db import Base
from newspaper import Article, nlp


class Page(Base):

	__tablename__ = 'pages'

	id = Column(Integer, primary_key=True)
	content = Column(String)
	keywords = Column(String)
	link = Column(String, unique=True)
	lean = Column(Float)



	def link_init(self, link):
		pass

	def __init__(self, link, text=None):
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
			return


		self.content = text.lower()

		keywords = ''

		for i in nlp.keywords(text):
			keywords += i.lower() + ' '
		self.link = link
		self.keywords = keywords