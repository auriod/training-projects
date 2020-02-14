import sqlite3

conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row  # объекты sqlite3.Row - аналог dict
curs = conn.cursor()

'''
функция create_table() создает таблицу pays в файле БД database.db
поля таблицы:
sum REAL: сумма платежа
category TEXT: категория платежа
data TEXT: дата 
comment TEXT: комментарии к платежу
type TEXT: тип платежа доход/расход
'''
def create_table():
    curs.execute(''' CREATE TABLE IF NOT EXISTS pays
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  sum REAL,
                  category TEXT,
                  data TEXT,
                  comment TEXT,
                  type TEXT)''')

    pays = [
        (125.36, 'еда', '2019-06-29', 'молоко, хлеб, сыр', 'cost'),
        (10535.00, 'зарплата', '2019-06-30', 'зарплата за июль', 'gain'),
        (742.10, 'авто', '2019-07-02', 'новое колесо', 'cost'),
        (535.00, 'еда', '2019-07-06', 'мясо, хлеб, сок', 'cost'),
        (1000.00, 'подработка', '2019-07-10', 'верстка сайта', 'gain'),
        (841.00, 'здоровье', '2019-07-15', 'стоматолог', 'cost'),
        (200.00, 'отдых', '2019-07-20', 'кино', 'cost'),
        (135.00, 'еда', '2019-07-25', 'гречка, макароны', 'cost'),
        (2700.00, 'обучение', '2019-07-30', 'курсы в академии "Шаг"', 'cost'),
        (500.00, 'долг', '2019-08-01', 'Петров П.П.', 'gain'),
        (242.00, 'еда', '2019-08-01', 'торт на работу', 'cost'),
    ]
    curs.executemany('INSERT INTO pays(sum, category, data, comment, type) VALUES (?, ?, ?, ?, ?)', pays)

    conn.commit()


# отображение всех записей таблицы pays
def show_all_pays():
    curs.execute('SELECT * FROM pays')

    for pay in curs.fetchall():
        for k, v in dict(pay).items():
            print(f'{k}:{v}', end='| |')
        print()


# возвращает общую сумму расходов
def get_sum_cost():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    curs.execute('SELECT * FROM pays WHERE type=="cost"')
    return sum([s['sum'] for s in curs.fetchall()])


# возвращает общую сумму доходов
def get_sum_gain():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    curs.execute('SELECT * FROM pays WHERE type=="gain"')
    return sum([s['sum'] for s in curs.fetchall()])


# функция возвращает данные по расходам в виде списка объектов sqlite3.Row
# переменная field_sorted определяет поле по которому сортируются записи (по умолчанию сортировка по дате)
def get_cost_data(field_sorted='data'):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    curs.execute("SELECT * FROM pays WHERE type=='cost' ORDER BY " + field_sorted + " DESC")
    res = curs.fetchall()
    conn.close()
    return res


# функция возвращает данные по доходам в виде списка объектов sqlite3.Row
# переменная field_sorted определяет поле по которому сортируются записи (по умолчанию сортировка по дате)
def get_gain_data(field_sorted='data'):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()
    # print(field_sorted)
    curs.execute("SELECT * FROM pays WHERE type=='gain' ORDER BY " + field_sorted + " DESC")
    res = curs.fetchall()
    conn.close()

    return res


# функция добавляет данный платежа типа "cost" в БД
def save_cost_data(sum, category, data, comment):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    data = (sum, category, data, comment, 'cost')
    curs.execute('''INSERT INTO pays(sum, category, data, comment, type) 
                    VALUES (?, ?, ?, ?, ?)''', data)
    conn.commit()
    conn.close()


# функция добавляет данный платежа типа "gain" в БД
def save_gain_data(sum, category, data, comment):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    data = (sum, category, data, comment, 'gain')
    curs.execute('''INSERT INTO pays(sum, category, data, comment, type) 
                    VALUES (?, ?, ?, ?, ?)''', data)
    conn.commit()
    conn.close()

# возвращает общую сумму долгов (записей в БД у которых поле "category" равно "долг")
def get_credit():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    curs.execute('SELECT * FROM pays WHERE category=="долг"')
    return sum([s['sum'] for s in curs.fetchall()])


if __name__ == '__main__':
    # create_table()
    show_all_pays()


