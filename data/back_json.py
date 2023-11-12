import json
import sqlite3


def db():
    # подключение к базам данных
    con = sqlite3.connect("data/workspace.db")
    # Создание курсора
    cur = con.cursor()

    # запрос всех данных из базы данных
    result_db = cur.execute("""SELECT place, login FROM workspace""").fetchall()

    result_db_1 = cur.execute("""SELECT place, book_login FROM workspace""").fetchall()

    # создание словаря с ключами места и значением логина
    json_output = {}
    for i in result_db:
        json_output[i[0]] = i[1]

    # создание словаря с ключами места и значением забронированного логина
    book_login = {}
    for i in result_db_1:
        book_login[i[0]] = i[1]

    return json_output, book_login


def json_open(file_json):
    # Подключение к БД
    con = sqlite3.connect("data/workspace.db")
    # Создание курсора
    cur = con.cursor()

    # открытие .json
    with open(file_json, encoding="UTF-8") as json_file:
        records = json.load(json_file)

    # присваивание переменным данные из json
    login = records["login"]
    place = records["place"]

    places_db = cur.execute("""SELECT place FROM workspace""").fetchall()

    if place in places_db or len(login) == 8:
        # добавление записи в базу данных
        cur.execute(f'''UPDATE workspace SET login = '{login}' WHERE place = '{place}' ''')
        con.commit()


def check_login(search_login):
    con = sqlite3.connect("data/workspace.db")
    # Создание курсора
    cur = con.cursor()

    # добавление записи в базу данных
    result_db = cur.execute("""SELECT login FROM workspace""").fetchall()
    if (search_login,) in result_db:
        return True
    return False

# # Подключение к БД
# con = sqlite3.connect("workspace.db")
# # Создание курсора
# cur = con.cursor()
# for s in ['su']:
#     for i in range(1, 4):
#         for j in ["e", "f"]:
#             # добавление записи в базу данных
#             cur.execute(f''' INSERT INTO workspace (place, login) VALUES("{s}-{j}{i}", "empty") ''')
#             con.commit()
