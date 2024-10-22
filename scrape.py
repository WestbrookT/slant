import newspaper
from newspaper import Article
from os import listdir
import json

left = listdir('left')
right = listdir('right')
neutral = listdir('neutral')
articles = {'left' : {}, 'right' : {}, 'neutral' : {}}

for news in left:
	urls = open('left/'+news)
	
	for url in urls:
		article = Article(url)
		article.download()
		try:
			article.parse()
		except newspaper.article.ArticleException:
			continue
		articles['left'][url] = article.text
	urls.close()
	
for news in right:
	urls = open('right/'+news)
	
	for url in urls:
		article = Article(url)
		article.download()
		try:
			article.parse()
		except newspaper.article.ArticleException:
			continue
		articles['right'][url] = article.text
	urls.close()


for news in neutral:
	urls = open('neutral/'+news)
	
	for url in urls:
		article = Article(url)
		article.download()
		try:
			article.parse()
		except newspaper.article.ArticleException:
			continue
		articles['neutral'][url] = article.text
	urls.close()
dump = json.dumps(articles)

f = open('articles.json', 'w')
f.write(dump)
f.close()
