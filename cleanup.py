import json
import sys

articles = json.load(open(sys.argv[1]))
cleanarticles = {'left' : {}, 'right' : {}}

for url in articles['left']:
	print(url)
	if not articles['left'][url] == "":
		cleanarticles['left'][url] = articles['left'][url]

for url in articles['right']:
	print(url)
	if not articles['right'][url] == "":
		cleanarticles['right'][url] = articles['right'][url]

open('cleanarticles.json', 'w').write(json.dumps(cleanarticles))
