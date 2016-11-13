import json
from os import listdir
import sys

articles = json.load(open(sys.argv[1]))
cleanarticles = {'left' : {}, 'right' : {}, 'neutral' : {}}

for url in articles['left']:
	print(url)
	if not articles['left'][url] == "":
		cleanarticles['left'][url] = articles['left'][url]

for url in articles['right']:
	print(url)
	if not articles['right'][url] == "":
		cleanarticles['right'][url] = articles['right'][url]

for url in articles['neutral']:
	print(url)
	if not articles['neutral'][url] == "":
		cleanarticles['neutral'][url] = articles['neutral'][url]

open('cleanarticles.json', 'w').write(json.dumps(cleanarticles))
