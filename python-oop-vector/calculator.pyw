from vector import *
from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title('Калькулятор векторов')
root.geometry("700x510+100+100")
root.config(bg='#55aaff')

a = None  # вектор a
b = None  # вектор b


def create_vector():
    """функция создает два вектора с введенными координатами"""
    global a, b
    x1, y1, z1 = int(x_1.get()), int(y_1.get()), int(z_1.get())
    x2, y2, z2 = int(x_2.get()), int(y_2.get()), int(z_2.get())

    a = Vector(x1, y1, z1)
    b = Vector(x2, y2, z2)


def show_module():
    """Модуль векторов"""
    text_result.delete(1.0, 7.0)
    try:
        create_vector()
        text_result.insert(1.0, f'Модуль вектора а{a}: {float(a)}\nМодуль вектора b{b}: {float(b)}')
    except ValueError:
        mb.showinfo('Ошибка', f'Некорректные данные')


def show_add_sub():
    """Сумма и разность векторов"""
    text_result.delete(1.0, 7.0)
    try:
        create_vector()
        text_result.insert(1.0, f'Сумма векторов а{a} + b{b} = {a + b}\nРазность векторов а{a} - b{b} = {a - b}' +
                           f'\nРазность векторов b{b} - a{a} = {b - a}')
    except ValueError:
        mb.showinfo('Ошибка', f'Некорректные данные')


def show_projection():
    """Проекция векторов"""
    text_result.delete(1.0, 7.0)
    try:
        create_vector()
        text_result.insert(1.0, f'Проекция вектора а{a} на вектор b{b} = {get_projection(a, b)}' +
                           f'\nПроекция вектора b{b} на вектор a{a} = {get_projection(b, a)}')
    except ValueError:
        mb.showinfo('Ошибка', f'Некорректные данные')


def show_angle():
    """угол между векторами"""
    text_result.delete(1.0, 7.0)
    try:
        create_vector()
        text_result.insert(1.0, f'Угол \u2220 аb: {get_angle(a, b)} радиан; {get_angle(a, b, "d")} градусов')
    except ValueError:
        mb.showinfo('Ошибка', f'Некорректные данные')


def show_mul():
    """Скалярное произведение векторов"""
    text_result.delete(1.0, 7.0)
    try:
        create_vector()
        text_result.insert(1.0, f'Скалярное произведение а{a} * b{b} = {a * b}')
    except ValueError:
        mb.showinfo('Ошибка', f'Некорректные данные')


def show_mul_v():
    """Векторное произведение векторов"""
    text_result.delete(1.0, 7.0)
    try:
        create_vector()
        text_result.insert(1.0, f'Векторное произведение [а{a} * b{b}] = {get_vector_mul(a, b)}')
    except ValueError:
        mb.showinfo('Ошибка', f'Некорректные данные')


def show_is_collinear():
    """Коллинеарность векторов"""
    text_result.delete(1.0, 7.0)
    try:
        create_vector()
        if is_collinear(a, b):
            text_result.insert(1.0, f'Векторы а{a} и b{b} коллинеарны')
        else:
            text_result.insert(1.0, f'Векторы а{a} и b{b} неколлинеарны')
    except ValueError:
        mb.showinfo('Ошибка', f'Некорректные данные')


def show_is_aligned():
    """Сонаправленность векторов"""
    text_result.delete(1.0, 7.0)
    try:
        create_vector()
        if is_aligned(a, b):
            text_result.insert(1.0, f'Векторы а{a} и b{b} сонаправленны')
        else:
            text_result.insert(1.0, f'Векторы а{a} и b{b} разнонаправленны')
    except ValueError:
        mb.showinfo('Ошибка', f'Некорректные данные')


lf_create = LabelFrame(root, width=680, bg='#55aaff', text='Введите координаты векторов',
                       font='Garamond 14 bold', height=100, fg='white')
lf_create.grid(row=0, column=0, columnspan=2, padx=5)

lb1 = Label(lf_create, text=' a (', font='Garamond 20 bold', bg='#55aaff', fg='white')
lb1.grid(row=0, column=0, padx=5, pady=5)

x_1 = Entry(lf_create, font='Garamond 20 bold', width=4, justify=CENTER)
x_1.grid(row=0, column=1, padx=5)

lb2 = Label(lf_create, text=',', font='Garamond 20 bold', bg='#55aaff', fg='white')
lb2.grid(row=0, column=2)

y_1 = Entry(lf_create, font='Garamond 20 bold', width=4, justify=CENTER)
y_1.grid(row=0, column=3, padx=5)

lb3 = Label(lf_create, text=',', font='Garamond 20 bold', bg='#55aaff', fg='white')
lb3.grid(row=0, column=4)

z_1 = Entry(lf_create, font='Garamond 20 bold', width=4, justify=CENTER)
z_1.grid(row=0, column=5, padx=5)

lb4 = Label(lf_create, text=')', font='Garamond 20 bold', bg='#55aaff', fg='white')
lb4.grid(row=0, column=6)

#######################################################################################
#######################################################################################

lb5 = Label(lf_create, text=';  b (', font='Garamond 20 bold', bg='#55aaff', fg='white')
lb5.grid(row=0, column=7, padx=5, pady=5)

x_2 = Entry(lf_create, font='Garamond 20 bold', width=4, justify=CENTER)
x_2.grid(row=0, column=8, padx=5)

lb2 = Label(lf_create, text=',', font='Garamond 20 bold', bg='#55aaff', fg='white')
lb2.grid(row=0, column=9)

y_2 = Entry(lf_create, font='Garamond 20 bold', width=4, justify=CENTER)
y_2.grid(row=0, column=10, padx=5)

lb3 = Label(lf_create, text=',', font='Garamond 20 bold', bg='#55aaff', fg='white')
lb3.grid(row=0, column=11)

z_2 = Entry(lf_create, font='Garamond 20 bold', width=4, justify=CENTER)
z_2.grid(row=0, column=12, padx=5)

lb3 = Label(lf_create, text=')', font='Garamond 20 bold', bg='#55aaff', fg='white')
lb3.grid(row=0, column=13)

#######################################################################################
#######################################################################################

lf_btn = LabelFrame(root, width=680, bg='#55aaff', text='Операции',
                    font='Garamond 14 bold', height=100, fg='white')
lf_btn.grid(row=1, column=0, columnspan=2, padx=5)
###################################
b_float = Button(lf_btn, width=10, bg='#5555ff', text='Модуль', fg='white', height=2,
                 font='Garamond 14 bold', command=show_module)
b_float.grid(row=0, column=0, padx=10, pady=3)

b_add = Button(lf_btn, width=10, bg='#5555ff', text='Сумма\nРазность', fg='white', height=2,
                 font='Garamond 14 bold', command=show_add_sub)
b_add.grid(row=0, column=1, padx=10, pady=3)

b_proj = Button(lf_btn, width=10, bg='#5555ff', text='Проекция', fg='white', height=2,
                 font='Garamond 14 bold', command=show_projection)
b_proj.grid(row=0, column=2, padx=10, pady=3)

b_angle = Button(lf_btn, width=10, bg='#5555ff', text='Угол', fg='white', height=2,
                 font='Garamond 14 bold', command=show_angle)
b_angle.grid(row=0, column=3, padx=10, pady=3)
#########################################
b_mul = Button(lf_btn, width=10, bg='#5555ff', text='Скалярное\nпроизведение', fg='white',
                 font='Garamond 12 bold', height=2, padx=10, command=show_mul)
b_mul.grid(row=1, column=0, padx=10, pady=3)

b_mul_v = Button(lf_btn, width=10, bg='#5555ff', text='Векторное\nпроизведение', fg='white',
                 font='Garamond 12 bold', height=2, padx=10, command=show_mul_v)
b_mul_v.grid(row=1, column=1, padx=10, pady=3)

b_col = Button(lf_btn, width=10, bg='#5555ff', text='Коллинеарность', fg='white',
                 font='Garamond 12 bold', height=2, padx=10, command=show_is_collinear)
b_col.grid(row=1, column=2, padx=10, pady=3)

b_aligned = Button(lf_btn, width=10, bg='#5555ff', text='Сонаправлен\nность', fg='white',
                 font='Garamond 12 bold', height=2, padx=10, command=show_is_aligned)
b_aligned.grid(row=1, column=3, padx=10, pady=3)

#######################################################################################
#######################################################################################

lf_result = LabelFrame(root, width=680, bg='#55aaff', text='Результаты',
                       font='Garamond 14 bold', height=250, fg='white')
lf_result.grid(row=2, column=0, columnspan=2, padx=5)

text_result = Text(lf_result, width=62, height=8, font='Garamond 14 bold')
text_result.pack()

root.mainloop()

