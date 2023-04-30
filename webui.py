from flask import Flask, render_template, request

from utils import refresh, show_changes, get_item_history


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/refresh")
def do_refresh():
    response = {
        "response": refresh()
    }

    return response


@app.route("/show_changes")
def do_show_changes():
    response = {
        "response": show_changes()
    }

    return response


@app.route("/show_history")
def do_show_history():
    item_id = request.args.get('item_id', type=int)

    if item_id:
        response = {
            "response": get_item_history(item_id)
        }

        return response

    return "You need to provide item_id in url"
