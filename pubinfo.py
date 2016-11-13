import json
import newspaper
from newspaper import Article

articles = json.load(open('fulldata.json'))
fulldata = {}

for url in articles:
	print(str(url))
	fulldata[url] = articles[url]
	if "huffingtonpost" in url:
		fulldata[url]["publication"] = "Huffington Post"
	elif "jacobinmag" in url:
		fulldata[url]["publication"] = "The Jacobin"
	elif "jezebel" in url:
		fulldata[url]["publication"] = "Jezebel"
	elif "motherjones" in url:
		fulldata[url]["publication"] = "Mother Jones"
	elif "salon" in url:
		fulldata[url]["publication"] = "Salon"
	elif "vox" in url:
		fulldata[url]["publication"] = "Vox"
	elif "theblaze" in url:
		fulldata[url]["publication"] = "The Blaze"
	elif "breitbart" in url:
		fulldata[url]["publication"] = "Breitbart"
	elif "dailystormer" in url:
		fulldata[url]["publication"] = "The Daily Stormer"
	elif "foxnews" in url:
		fulldata[url]["publication"] = "Fox News"
	elif "washingtontimes" in url:
		fulldata[url]["publication"] = "The Washington Times"
	elif "npr" in url:
		fulldata[url]["publication"] = "National Public Radio"
	else:
		fulldata[url]["publication"] = "Across the web"

open('pubinfo.json', 'w').write(json.dumps(fulldata))
