import sys
import newspaper
from newspaper import Article, nlp

paper = newspaper.build(str(sys.argv[1]))

for article in paper.articles:
	print(article.url)
