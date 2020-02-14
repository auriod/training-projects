import tkinter as tk
from tkinter import messagebox as mb
import sqlite3
#######################################
#            SETTING                  #
#######################################
main_color = '#2E9AFE'
btn_color = 'white'
font_select = 'Vernada 10'
font_main = 'Arial 14'

con = sqlite3.connect('travel_agency.db')
con.row_factory = sqlite3.Row
cur = con.cursor()


class GuestsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=main_color)

        logo_update = tk.PhotoImage(file="img/update.gif")

        btn_update = tk.Button(self, image=logo_update, width=50, height=50,
                               command=self.select_data)
        btn_update.image = logo_update
        btn_update.grid(row=0, column=1, sticky='e')

        tk.Label(self, text='ГОСТИ', font='Arial 25 bold', fg='white', bg=main_color).grid(row=0, column=0, sticky='w')

        self.select_data()

        btn = tk.Button(self, text='На главную', font=font_main, bg='#85929E',
                        command=lambda: controller.show_frame('main'))
        btn.grid(row=2, column=0)

        btn = tk.Button(self, text='Добавить гостя', font=font_main, bg='lightgreen',
                        command=lambda: AddGuestsWindow())
        btn.grid(row=2, column=1)

    def select_data(self):
        labels = []
        cur.execute('''
                SELECT (guests.name || " " || guests.surname) as ФИО, 
                guests.country as страна, 
                guests.dob as дата_рождения, 
                COUNT(orders.id_guest) as визиты,
                SUM(orders.number_day) as дни,
                SUM(orders.number_day * hotels.price) as потрачено
                FROM orders INNER JOIN guests
                ON orders.id_guest = guests.id
                INNER JOIN hotels
                ON orders.id_hotel = hotels.id
                GROUP BY guests.surname, guests.name;
                ''')
        data = [dict(d) for d in cur.fetchall()]

        result_form = tk.LabelFrame(self, text='Данные', padx=10, pady=10, bg=main_color, fg='white', font='Arial 11')
        result_form.grid(row=1, column=0, pady=5, columnspan=2)

        for k in enumerate(data[0].keys()):
            labels.append(tk.Label(result_form, width=20, font=font_select, text=f'{k[1]}',
                                   borderwidth=1, relief='solid'))
            labels[-1].grid(row=0, column=k[0])

        for r in range(len(data)):
            for v in enumerate(data[r].values()):
                labels.append(tk.Label(result_form, width=20, font=font_select, text=f'{v[1]}',
                                       borderwidth=1, relief='solid'))
                labels[-1].grid(row=r + 1, column=v[0])


class AddGuestsWindow(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title('Добавить гостя')
        self.geometry('400x400+100+200')
        self.config(bg=main_color)
        self.entryes = []
        label_text = ['Имя', 'Фамилия', 'Дата рождения\n(ГГГГ-ММ-ДД)', 'Страна']
        for i in range(len(label_text)):
            label = tk.Label(self, text=label_text[i], font=font_main, width=15, bg=main_color, fg='white')
            label.grid(row=i, column=0, ipady=20)
            self.entryes.append(tk.Entry(self, width=20))
            self.entryes[-1].grid(row=i, column=1)

        btn_add = tk.Button(self, text="Добавить", bg=btn_color, font=font_main,
                            command=self.add_guest)
        btn_add.grid(row=4, column=0)

        btn_close = tk.Button(self, text="Закрыть", bg=btn_color, font=font_main,
                              command=lambda: self.destroy())
        btn_close.grid(row=4, column=1)

    def add_guest(self):
        data = []
        try:
            for entry in self.entryes:
                data.append(entry.get())
                entry.delete(0, 'end')

            #  проверка на незаполненные поля
            for d in data:
                if not d:
                    mb.showinfo("Error", "Все поля должны быть заполнены.")
                    return

            cur.execute('''
            INSERT INTO guests (name, surname, dob, country) 
            VALUES (?, ?, ?, ?);
            ''', data)

            con.commit()
        except ValueError:
            mb.showinfo("Error", "Некорректный ввод данных")


if __name__ == '__main__':
    pass
