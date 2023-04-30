from datetime import datetime

import requests
import pandas as pd
from sqlalchemy import func, desc

from config import session, URL
from models import Item, History


def refresh():
    new_items_count = 0

    print("Requesting HTML.")
    page = requests.get(URL)
    tables = pd.read_html(page.text)

    print("Adding rows to database.")
    for row in tables[1].values:
        row_query = session.query(Item).filter_by(title=row[0], price=row[2])

        if row_query.count() == 0:
            item = Item(row[0], row[2])
            session.add(item)
            new_items_count += 1

        item_id = row_query.first().id
        item_history = History(row[1], row[2], item_id)
        session.add(item_history)

    print("Saving...")
    session.commit()
    print("Done")

    result = f"Added {new_items_count} new items"
    print(result)
    return result


def show_changes(user_date=datetime.today()):

    result = []

    if type(user_date) != datetime:
        user_date = datetime.strptime(user_date+" 23:59:59", "%d.%m.%Y  %H:%M:%S")

    user_day_history = session.query(History).filter(func.DATE(History.add_time) == user_date.date()).all()

    for udh in user_day_history:
        yesterday_item = session.query(History).filter(
            History.add_time < user_date,
            History.count > udh.count
        ).filter_by(
            item_id=udh.item_id,
            price=udh.price
        ).first()

        item = session.query(Item).filter_by(id=udh.item_id).first()

        try:
            result_item = f"\n{item.id} {item.title}:\n\t- Added in {item.add_date}\n\t- Old count {yesterday_item.count}\n\t- New count {udh.count}\n\t- Was sold {yesterday_item.count-udh.count}\n\t- Price {udh.price}\n"
            print(result_item)
            result.append(result_item)
        except:
            pass

    return result


def get_item_history(item_id):

    result = {}

    item_history = session.query(History).filter_by(item_id=item_id).order_by(desc(History.add_time)).limit(20)
    orig_item = session.query(Item).filter_by(id=item_id).first().title

    print(f"\n{orig_item}:")
    result.update({orig_item: []})

    for item in item_history:
        print(f"\t- Add time: {item.add_time}\n\t- Price: {item.price}\n\t- Count: {item.count}\n")
        data = {
            "item_date": item.add_time,
            "item_price": item.price,
            "item_count": item.count
        }

        result[orig_item].append(data)

    return result
