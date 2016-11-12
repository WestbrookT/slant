from sqlalchemy import create_engine, Column, String, Integer
from db import Base
from newspaper import Article, nlp


class Page(Base):

	__tablename__ = 'pages'

	id = Column(Integer, primary_key=True)
	content = Column(String)
	keywords = Column(String)
	link = Column(String, unique=True)


	def __init__(self, link):
		article = Article(link)
		article.download()
		article.parse()

		content = article.text

		keywords = ''

		for i in nlp.keywords(content):
			keywords += i

		self.content = content
		self.keywords = keywords
		self.link = link