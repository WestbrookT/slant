import json
import newspaper
from newspaper import Article

articles = json.load(open('cleanarticles.json'))
fulldata = {}

for lean in articles:
	for url in articles[lean]:
		print(str(url))
		article = Article(url)
		article.download()
		try:
			article.parse()
		except newspaper.article.ArticleException:
			continue
		image = article.top_image
		fulldata[url] = {}
		fulldata[url]["image"] = image
		fulldata[url]["text"] = article.text

open('fulldata.json', 'w').write(json.dumps(fulldata))
