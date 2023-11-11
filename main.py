import sqlite3
import json
from data.back_json import json_open, db

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def feed():
    json_output = db()
    if open("db/login.json"):
        file_json = 'db/login.json'
        login, place = json_open(file_json)
    return render_template("index.html", workspace=json_output)


if __name__ == '__main__':
    app.run()
