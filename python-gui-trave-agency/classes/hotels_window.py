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


class HotelsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=main_color)

        logo_update = tk.PhotoImage(file="img/update.gif")

        btn_update = tk.Button(self, image=logo_update, width=50, height=50,
                               command=self.select_data)
        btn_update.image = logo_update
        btn_update.grid(row=0, column=1, sticky='e')

        tk.Label(self, text='ОТЕЛИ', font='Arial 25 bold', fg='white', bg=main_color).grid(row=0, column=0, sticky='w')

        self.select_data()

        btn = tk.Button(self, text='На главную', font=font_main,  bg='#85929E',
                        command=lambda: controller.show_frame('main'))
        btn.grid(row=2, column=0)

        btn_add = tk.Button(self, text='Добавить отель', font=font_main, bg='lightgreen',
                            command=lambda: AddHotelWindow())
        btn_add.grid(row=2, column=1)

    def select_data(self):
        labels = []
        cur.execute("""
                    SELECT * FROM hotels
                    ORDER BY stars DESC;
                    """)
        data = [dict(d) for d in cur.fetchall()]

        result_form = tk.LabelFrame(self, text='Данные', padx=5, pady=5, bg=main_color, fg='white', font='Arial 10')
        result_form.grid(row=1, column=0, pady=5, columnspan=2)

        for k in enumerate(data[0].keys()):
            labels.append(tk.Label(result_form, width=15, font=font_select, text=f'{k[1]}',
                                   borderwidth=1, relief='solid'))
            labels[-1].grid(row=0, column=k[0])

        for r in range(len(data)):
            for v in enumerate(data[r].values()):
                labels.append(tk.Label(result_form, width=15, font=font_select, text=f'{v[1]}',
                                       borderwidth=1, relief='solid'))
                labels[-1].grid(row=r + 1, column=v[0])


class AddHotelWindow(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title('Добавить отель')
        self.geometry('400x400+100+200')
        self.config(bg=main_color)
        self.entryes = []
        label_text = ['Название', 'Количество\nзвезд', 'Количество\nномеров', 'Цена']
        for i in range(len(label_text)):
            label = tk.Label(self, text=label_text[i], font=font_main, width=15, bg=main_color, fg='white')
            label.grid(row=i, column=0, ipady=20)
            self.entryes.append(tk.Entry(self, width=20))
            self.entryes[-1].grid(row=i, column=1)

        btn_add = tk.Button(self, text="Добавить", bg=btn_color, font=font_main,
                            command=self.add_hotel)
        btn_add.grid(row=4, column=0)

        btn_close = tk.Button(self, text="Закрыть", bg=btn_color, font=font_main,
                              command=lambda: self.destroy())
        btn_close.grid(row=4, column=1)

    def add_hotel(self):
        data = []
        try:
            data.append(self.entryes[0].get())  # name
            data.append(int(self.entryes[1].get()))  # stars
            data.append(int(self.entryes[2].get()))  # rooms
            data.append(float(self.entryes[3].get()))  # price

            for e in self.entryes:
                e.delete(0, 'end')

            cur.execute('''
            INSERT INTO hotels (name, stars, rooms, price)
            VALUES (?, ?, ?, ?);
            ''', data)

            con.commit()

        except ValueError:
            mb.showinfo("Error", "Некорректный ввод данных")


if __name__ == '__main__':
    pass



