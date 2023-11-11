import json
import sqlite3


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


def json_open(file_json):
    # открытие .json
    with open(file_json, encoding="UTF-8") as json_file:
        records = json.load(json_file)

    # присваивание переменным данные из json
    login = records["login"]
    place = records["place"]

    # Подключение к БД
    con = sqlite3.connect("data/workspace.db")
    # Создание курсора
    cur = con.cursor()

    # добавление записи в базу данных
    cur.execute(f'''UPDATE workspace SET login = '{login}' WHERE place = '{place}' ''')
    con.commit()

    return login, place


# # Подключение к БД
# con = sqlite3.connect("workspace.db")
# # Создание курсора
# cur = con.cursor()
# for s in ['hy', 'ca']:
#     for i in range(1, 10):
#         for j in ["a", "b", "c", "d", "f", "g", "h"]:
#             # добавление записи в базу данных
#             cur.execute(f''' INSERT INTO workspace (place, login) VALUES("{s}-{j}{i}", "empty") ''')
#             con.commit()
