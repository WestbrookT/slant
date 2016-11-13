from models import Page
from db import session, init_db
# from nltk.metrics import edit_distance
from math import sqrt
from sqlalchemy import and_
from json import dump, load
from os import system

init_db()


def _edit_dist_init(len1, len2):
	lev = []
	for i in range(len1):
		lev.append([0] * len2)  # initialize 2D array to zero
	for i in range(len1):
		lev[i][0] = i  # column 0: 0,1,2,3,4,...
	for j in range(len2):
		lev[0][j] = j  # row 0: 0,1,2,3,4,...
	return lev


def _edit_dist_step(lev, i, j, s1, s2, transpositions=False):
	c1 = s1[i - 1]
	c2 = s2[j - 1]

	# skipping a character in s1
	a = lev[i - 1][j] + 1
	# skipping a character in s2
	b = lev[i][j - 1] + 1
	# substitution
	c = lev[i - 1][j - 1] + (c1 != c2)

	# transposition
	d = c + 1  # never picked by default
	if transpositions and i > 1 and j > 1:
		if s1[i - 2] == c2 and s2[j - 2] == c1:
			d = lev[i - 2][j - 2] + 1

	# pick the cheapest
	lev[i][j] = min(a, b, c, d)


def edit_distance(s1, s2, transpositions=False):
	"""
	Calculate the Levenshtein edit-distance between two strings.
	The edit distance is the number of characters that need to be
	substituted, inserted, or deleted, to transform s1 into s2.  For
	example, transforming "rain" to "shine" requires three steps,
	consisting of two substitutions and one insertion:
	"rain" -> "sain" -> "shin" -> "shine".  These operations could have
	been done in other orders, but at least three steps are needed.

	This also optionally allows transposition edits (e.g., "ab" -> "ba"),
	though this is disabled by default.

	:param s1, s2: The strings to be analysed
	:param transpositions: Whether to allow transposition edits
	:type s1: str
	:type s2: str
	:type transpositions: bool
	:rtype int
	"""
	# set up a 2-D array
	len1 = len(s1)
	len2 = len(s2)
	lev = _edit_dist_init(len1 + 1, len2 + 1)

	# iterate over the array
	for i in range(len1):
		for j in range(len2):
			_edit_dist_step(lev, i + 1, j + 1, s1, s2, transpositions=transpositions)
	return lev[len1][len2]


def create_page(link, text=None, img=None):
	doc = Page(link, text=text, img=img)

	session.add(doc)


def commit():
	session.commit()


def create_pages(links):
	for link in links:
		create_page(link)
	session.commit()


def get_link(link):
	return Page.query.filter(Page.link == link).first()


def get_all():
	num = 1
	rows = 0
	if num == 1:
		rows += Page.query.count()

	while num <= rows:
		while Page.query.get(num) == None:
			rows += 1
			num += 1
		yield Page.query.get(num)
		num += 1


def match(word, cmp):
	return edit_distance(word, cmp) <= int(sqrt(len(word)))


def freq(word, text):
	count = 0

	for token in text:
		if match(word, token):
			count += 1
	return count


def search(query):
	out = {}
	words = query.lower().split(' ')
	wl = len(words)
	for page in get_all():
		out[page.link] = 0
		space = page.content.lower().split(' ')
		count = 0
		for word in words:
			print(word)
			out[page.link] += freq(word, space)

			for token in page.keywords.split(' '):
				if match(word, token):
					count += 1

		temp = count / wl
		# print(count, page.keywords)

		out[page.link] = {'rel':(out[page.link] / len(space)) + count, 'lean':page.lean}

	return out


def count():
	return Page.query.count()


def query(start, stop, string):
	pages = list(Page.query.filter(and_(Page.id >= start, Page.id < stop)))
	# print(list(pages))

	out = {}
	words = string.lower().split(' ')
	wl = len(words)



	for page in pages:
		out[page.link] = 0
		space = page.content.lower().split(' ')
		count = 0
		for word in words:
			out[page.link] += freq(word, space)

			for token in page.keywords.split(' '):
				if match(word, token):
					count += 1

		temp = count / wl
		# print(count, page.keywords)

		out[page.link] = {'rel': (out[page.link] / len(space)) + count, 'lean': page.lean, 'text':page.content, 'keywords':page.keywords}

	return out


def lambda_search(q):

	fin = []
	count = 0
	for page in get_all():
		if count == 20:
			break
		count += 1

		inp = open('pl.json', 'w')
		pl = {'text':page.content, 'keywords':page.keywords, 'query':q}
		dump(pl, inp)
		inp.close()



		system('aws lambda invoke --invocation-type RequestResponse --function-name scoreus --region us-east-1 --payload file://pl.json --profile adminuser --output text out.txt')

		out = open('out.txt', 'r')
		data = load(out)
		out.close()



		print(data)

		fin.append({'text':page.content, 'img':page.img, 'rel':float(data['body']), 'lean':page.lean, 'link':page.link})
	return fin

