from flask import Flask, url_for, render_template, redirect, request
from database import *

app = Flask(__name__)


'''
Основная страница приложения.
Отображается общее состояние счета пользователя: переменная score
Сумма долгов: переменная credit
Таблица с данными последних десяти платежей(сумма, категория, дата).
'''
@app.route('/')
def index():
    data = sorted(get_cost_data() + get_gain_data(), key=lambda x: x['data'], reverse=True)
    score = get_sum_gain() - get_sum_cost()
    credit = get_credit()
    return render_template('index.html', data=data[:10], score=score, credit=credit)


'''
Страница с данными расходов.
Отображается общая сумма расходов: переменная score
Таблица с данными расходов(сумма, категория, комментарии, дата).
Функции:
1. При нажатии на заголовок калонки "Сумма" или "Дата" информация сортируется по соответствующим данным
в порядке убывания
2. При нажатии на "зеленый крестик" происходит переход на форму добавления данных нового платежа
'''
@app.route('/info/cost/<field_sorted>')
def show_info_cost(field_sorted):
    return render_template('info.html',
                           pays=get_cost_data(field_sorted),
                           score=get_sum_cost(),
                           title='Расходы')


'''
Страница с данными доходов.
Отображается общая сумма доходов: переменная score
Таблица с данными доходов(сумма, категория, комментарии, дата).
Функции:
1. При нажатии на заголовок калонки "Сумма" или "Дата" информация сортируется по соответствующим данным
в порядке убывания
2. При нажатии на "зеленый крестик" происходит переход на форму добавления данных нового платежа
'''
@app.route('/info/gain/<field_sorted>')
def show_info_gain(field_sorted):
    return render_template('info.html',
                           pays=get_gain_data(field_sorted),
                           score=get_sum_gain(),
                           title='Доходы')


# вызов формы для добавления расходов
@app.route('/form/cost')
def form_cost():
    return render_template('form.html',
                           handler='/add_cost',  # url обработчика формы
                           title='Добавить расходы')


# вызов формы для добавления доходов
@app.route('/form/gain')
def form_gain():
    return render_template('form.html',
                           handler='/add_gain',  # url обработчика формы
                           title='Добавить доходы')


# добавление данных расхода в БД
@app.route('/add_cost', methods=['POST'])
def add_cost():
    sum = float(request.form['sum'])
    category = request.form['category']
    data = request.form['data']
    comment = request.form['comment']
    save_cost_data(sum, category, data, comment)
    return redirect(url_for('form_cost'))


# добавление данных дохода в БД
@app.route('/add_gain', methods=['POST'])
def add_gain():
    sum = float(request.form['sum'])
    category = request.form['category']
    data = request.form['data']
    comment = request.form['comment']
    save_gain_data(sum, category, data, comment)
    return redirect(url_for('form_gain'))


