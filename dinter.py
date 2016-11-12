from models import Page
from db import session, init_db


def create_page(link):

	doc = Page(link)

	session.add(doc)
	session.commit()

init_db()

create_page('https://www.trasewestbrook.com/pages/Tamuhack%202016')