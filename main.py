from datetime import datetime

import argparse

from utils import refresh, show_changes, get_item_history
from webui import app as webapp


app = argparse.ArgumentParser(description="App for keeping FB acc sales statistics",
                              epilog="©Amir Hasanov all rights reserved")

app.add_argument("-r", "--refresh", action="store_true", help="refresh sales count")
app.add_argument("-s", "--show_changes", action="store_true", help="list changes")
app.add_argument("--start", default=datetime.today(), help="show_changes start point")
app.add_argument("-H", "--item_history", type=int, help="show item history by item id")
app.add_argument("-w", "--webui", action="store_true", help="start web user interface")

args = app.parse_args()

if __name__ == "__main__":
    if args.refresh:
        refresh()
    if args.show_changes:
        show_changes(args.start)
    if args.item_history:
        get_item_history(args.item_history)
    if args.webui:
        webapp.run(host="0.0.0.0", port=8080, debug=False)
