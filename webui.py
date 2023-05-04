from datetime import datetime

from flask import Flask, render_template, request, jsonify

from utils import refresh, show_changes, get_item_history, get_all_items


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/refresh")
def do_refresh():
    response = jsonify(response=refresh())
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/show_changes")
def do_show_changes():
    response = jsonify(response=show_changes(datetime.today()))
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/show_history")
def do_show_history():
    item_id = request.args.get('item_id', type=int)

    if item_id:
        response = jsonify(response=get_item_history(item_id))
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response

    response = jsonify(response="You need to provide item_id in url")
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/show_all")
def do_show_all():
    response = jsonify(response=get_all_items())
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response
