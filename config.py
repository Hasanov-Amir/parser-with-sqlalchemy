from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


URL = "https://npprteam.shop/?cat_id=8291"

engine = create_engine("sqlite:///app.db")
Base = declarative_base()
# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
