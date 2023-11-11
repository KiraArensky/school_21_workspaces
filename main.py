from flask import Flask

app = Flask(__name__)


@app.route('/user/<username>')
def user_profile(username):
    return f"Школа 21 для {username}"


if __name__ == '__main__':
    app.run()
