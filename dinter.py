from models import Page
from db import session, init_db
from nltk.metrics import edit_distance
from math import sqrt
from sqlalchemy import and_

init_db()

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
			out[page.link] += freq(word, space)


			for token in page.keywords.split(' '):
				if match(word, token):
					count += 1



		temp = count/wl
		#print(count, page.keywords)

		out[page.link] = (out[page.link]/len(space)) + count




	return out

def count():
	return Page.query.count()

def query(start, stop, string):


	pages = list(Page.query.filter(and_(Page.id >= start, Page.id < stop)))
	#print(list(pages))

	out = {}
	words = string.lower().split(' ')
	wl = len(words)

	for i in pages:
		print(i.link)

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

		out[page.link] = (out[page.link] / len(space)) + count

	return out