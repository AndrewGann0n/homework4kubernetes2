# RESTful API
from flask import Flask, render_template, redirect, g, request, url_for, jsonify, Response
import sqlite3
import urllib
import json
import http.client

DATABASE = 'todolist.db'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/api/items")  # default method is GET
def get_items(): # this is the counterpart of show_list() from homework 3
    db = get_db()
    cur = db.execute('SELECT what_to_do, due_date, status FROM entries')
    entries = cur.fetchall()
    tdlist = [dict(what_to_do=row[0], due_date=row[1], status=row[2])
              for row in entries]
    response = Response(json.dumps(tdlist),  mimetype='application/json')
    return response


@app.route("/api/items", methods=['POST'])
def add_item(): # this is the counterpart of add_entry() from homework 3
    db = get_db()
    db.execute('insert into entries (what_to_do, due_date) values (?, ?)',
               [request.json['what_to_do'], request.json['due_date']])
    db.commit()
    return jsonify({"result": True})


@app.route("/api/items/<item>", methods=['DELETE'])
def delete_item(item): # this is the counterpart of delete_entry() from homework 3
    # TODO
    db = get_db()


@app.route("/api/items/<item>", methods=['PUT'])
def update_item(item): # this is the counterpart of mark_as_done() from homework 3
    # TODO
    db = get_db()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



    conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
    
    headers = {
        'x-rapidapi-key': "039fc7d0admshc3318ca98b043c8p15dcc8jsn4d10416c3e91",
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }
    
    conn.request("GET", "/words/.22-caliber/pertainsTo", headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    
    print(data.decode("utf-8"))


conn = http.client.HTTPSConnection("sms77io.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "039fc7d0admshc3318ca98b043c8p15dcc8jsn4d10416c3e91",
    'x-rapidapi-host': "sms77io.p.rapidapi.com"
    }

conn.request("GET", "/balance?p=%3CREQUIRED%3E", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001)
