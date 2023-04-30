from datetime import datetime

from sqlalchemy import Column, String, Integer, DATETIME

from config import Base, engine


class Item(Base):
    __tablename__ = "item"

    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(300))
    price = Column("price", String(20))
    add_date = Column("add_date", DATETIME, default=datetime.now())
    total_sales_count = Column("sales", Integer, default=0)

    def __init__(self, title, price, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.price = price

    def __repr__(self):
        return f"{self.id=}, {self.title=}, {self.price=}"


class History(Base):
    __tablename__ = "history"

    id = Column("id", Integer, primary_key=True)
    count = Column("count", Integer)
    price = Column("price", String(20))
    add_time = Column("add_time", DATETIME, default=datetime.now())
    item_id = Column("item_id", Integer())

    def __init__(self, count, price, item_id):
        self.count = count
        self.price = price
        self.item_id = item_id

    def __repr__(self):
        return f"{self.item_id=}, {self.count=}, {self.price=}, {self.add_time=}"


# Base.metadata.create_all(bind=engine)
