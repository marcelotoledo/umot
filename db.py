from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine  = create_engine('postgresql://umot:RabrXfC9ggBhyFWBsWAWoH3@localhost/umot', echo=True)
Base    = declarative_base()
Session = sessionmaker(bind=engine)

Session.configure(bind=engine)

session = Session()

def create_all():
    Base.metadata.create_all(engine)

def drop_all():
    Base.metadata.drop_all(engine)
