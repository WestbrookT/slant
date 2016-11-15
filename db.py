from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
#from newspaper import Article, nlp


db = create_engine('sqlite:///data.db', echo=False)

Base = declarative_base()

def init_db():
	Base.metadata.create_all(bind=db)


session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db))

Base = declarative_base()
Base.query = session.query_property()


init_db()
