import requests
import json
import sqlite3


# url = 'http://muslimsalat.com/daily.json'
# response = requests.get(url)


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
    cur.execute(f'''INSERT INTO workspace (login) VALUES("{login}") ''')
    con.commit()

    return login, place

#
# # Подключение к БД
# con = sqlite3.connect("workspace.db")
# # Создание курсора
# cur = con.cursor()
# for s in ['hy', 'ca']:
#     for i in range(1, 9):
#         for j in ["a", "b", "c"]:
#             # добавление записи в базу данных
#             cur.execute(f''' INSERT INTO workspace (place, login) VALUES("{s}-{j}{i}", "empty") ''')
#             con.commit()
