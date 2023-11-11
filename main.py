import sqlite3
import json
import psycopg2
from data.back_json import json_open

from flask import Flask, render_template

app = Flask(__name__)


def db():
    # подключение к базам данных
    con = sqlite3.connect("data/workspace.db")
    # Создание курсора
    cur = con.cursor()

    # запрос всех данных из базы данных
    result_db = cur.execute("""SELECT * FROM workspace""").fetchall()

    # создание словаря с ключами места и значением логина
    json_output = {}
    for i in result_db:
        json_output[i[0]] = i[1]

    return json_output


@app.route('/')
def feed():
    json_output = db()
    if open("db/login.json"):
        file_json = 'db/login.json'
        login, place = json_open(file_json)
    return render_template("index.html", workspace=json_output)


if __name__ == '__main__':
    app.run()
