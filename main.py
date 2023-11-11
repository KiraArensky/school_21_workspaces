from flask import request
from data.back_json import json_open, db, check_login

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        json_output = db()
        if open("db/login.json"):
            file_json = 'db/login.json'
            if json_open(file_json) is False:
                pass
        search_login = "empty"
        return render_template("index.html", workspace=json_output, query=search_login)
    else:
        search_login = request.form['query']
        json_output = db()
        if open("db/login.json"):
            file_json = 'db/login.json'
            json_open(file_json)
            if check_login(search_login):
                return render_template("index.html", workspace=json_output, query=search_login)
        search_login = "empty"
        return render_template("index.html", workspace=json_output, query=search_login)



if __name__ == '__main__':
    app.run()
