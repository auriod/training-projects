import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3
import datetime
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


class OrdersWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=main_color)
        self.labels = []

        tk.Label(self, text='ЗАКАЗЫ  ', font='Arial 25 bold', fg='white', bg=main_color)\
            .grid(row=0, column=0, sticky='w')

        select_form = tk.LabelFrame(self, text='Сортировка данных',
                                    bg=main_color, fg='white', font='Arial 11')
        select_form.grid(row=0, column=1)

        tk.Label(select_form, text='Выбирите гостя', font=font_main, fg='white', bg=main_color)\
            .grid(row=0, column=0, sticky='w', padx=10)

        box_guest = ttk.Combobox(select_form, values=['']+AddOrdersWindow.get_guests_name(), width=20)
        box_guest.grid(row=0, column=1, padx=10)

        tk.Label(select_form, text='Выбирите отель', font=font_main, fg='white', bg=main_color)\
            .grid(row=0, column=2, sticky='w', padx=10)
        box_hotel = ttk.Combobox(select_form, values=['']+AddOrdersWindow.get_hotels_name(), width=20)
        box_hotel.grid(row=0, column=3, padx=10)

        logo_update = tk.PhotoImage(file="img/update.gif")

        btn_update = tk.Button(self, image=logo_update, width=50, height=50,
                               command=lambda: self.select_data(box_guest.get(), box_hotel.get()))
        btn_update.image = logo_update
        btn_update.grid(row=0, column=2, sticky='e')

        self.result_form = tk.LabelFrame(self, text='Данные', padx=20, pady=20,
                                         bg=main_color, fg='white', font='Arial 11')
        self.result_form.grid(row=1, column=0, columnspan=3)

        self.select_data()

        btn = tk.Button(self, text='На главную', font=font_main, bg='#85929E',
                        command=lambda: controller.show_frame('main'))
        btn.grid(row=2, column=0, pady=10, sticky='w')

        btn_add = tk.Button(self, text='Добавить заказ', font=font_main, bg='lightgreen',
                            command=lambda: AddOrdersWindow())
        btn_add.grid(row=2, column=1, pady=10, sticky='w')

        btn_add = tk.Button(self, text='Удалить заказ', font=font_main, bg='#FF5733',
                            command=lambda: DeleteOrdersWindow())
        btn_add.grid(row=2, column=1)

    def select_data(self, guest='', hotel=''):
        # удаление текущей таблицы, если она существует
        if self.labels:
            for l in self.labels:
                l.destroy()

        guery = '''
                SELECT orders.id, guests.surname, guests.name, orders.data as data_order, hotels.name as hotel, 
                orders.data_settlement as data_set, orders.number_day,
                orders.number_day * hotels.price as gain
                FROM orders INNER JOIN guests
                ON orders.id_guest = guests.id
                INNER JOIN hotels
                ON orders.id_hotel = hotels.id '''
        try:
            if guest == '' and hotel == '':     # последние заказы
                cur.execute(guery + ' ORDER BY 1 DESC LIMIT 10;')
            elif guest != '' and hotel == '':   # отображение заказов выбранного гостя
                cur.execute(guery + 'WHERE guests.name = ? AND guests.surname = ? ORDER BY 1 DESC;', guest.split(' '))
            elif guest == '' and hotel != '':   # отображение заказов выбранного отеля
                cur.execute(guery + 'WHERE hotels.name = ? ORDER BY 1 DESC;', (hotel,))
            else:                               # отображение заказов выбранного отеля и гостя
                cur.execute(guery + '''WHERE guests.name = ? AND guests.surname = ? AND hotels.name = ? 
                                       ORDER BY 1 DESC;''', guest.split(' ') + [hotel])

            data = [dict(d) for d in cur.fetchall()]

            for k in enumerate(data[0].keys()):
                self.labels.append(tk.Label(self.result_form, width=15, font=font_select, text=f'{k[1]}',
                                   borderwidth=1, relief='solid'))
                self.labels[-1].grid(row=0, column=k[0])

            for r in range(len(data)):
                for v in enumerate(data[r].values()):
                    self.labels.append(tk.Label(self.result_form, width=15, font=font_select, text=f'{v[1]}',
                                       borderwidth=1, relief='solid'))
                    self.labels[-1].grid(row=r + 1, column=v[0])

        except IndexError:
            mb.showinfo("Error", "Данные не найдены")


class AddOrdersWindow(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title('Добавить заказ')
        self.geometry('400x400+100+200')
        self.config(bg=main_color)

        label_text = ['Выберите гостя', 'Выберите отель', 'Дата заселения\n(ГГГГ-ММ-ДД)', 'Количество дней']
        for i in range(len(label_text)):
            label = tk.Label(self, text=label_text[i], font=font_main, width=15, bg=main_color, fg='white')
            label.grid(row=i, column=0, ipady=20)

        guests_name = self.get_guests_name()

        self.box_name = ttk.Combobox(self, width=20, values=guests_name)
        self.box_name.grid(row=0, column=1)

        hotels_name = self.get_hotels_name()

        self.box_hotel = ttk.Combobox(self, width=20, values=hotels_name)
        self.box_hotel.grid(row=1, column=1)

        self.box_data = tk.Entry(self, width=20)
        self.box_data.grid(row=2, column=1)

        self.box_day = tk.Entry(self, width=20)
        self.box_day.grid(row=3, column=1)

        btn_add = tk.Button(self, text="Добавить", bg=btn_color, font=font_main,
                            command=self.add_order)
        btn_add.grid(row=4, column=0)

        btn_close = tk.Button(self, text="Закрыть", bg=btn_color, font=font_main,
                              command=lambda: self.destroy())
        btn_close.grid(row=4, column=1)

    @staticmethod
    def get_guests_name():
        cur.execute('''
                    SELECT (name || " " || surname) as name FROM guests
                    ''')
        return [dict(d)['name'] for d in cur.fetchall()]

    @staticmethod
    def get_hotels_name():
        cur.execute('''
                    SELECT name FROM hotels
                    ''')
        return [dict(d)['name'] for d in cur.fetchall()]

    def add_order(self):
        try:
            name, surname = self.box_name.get().split(' ')
            self.box_name.set('')
            hotel = self.box_hotel.get()
            self.box_hotel.set('')
            data = self.box_data.get()
            self.box_data.delete(0, 'end')
            day = int(self.box_day.get())
            self.box_day.delete(0, 'end')

            #  проверка на незаполненные поля
            for d in (name, surname, hotel, data, day):
                if not d:
                    mb.showinfo("Error", "Все поля должны быть заполнены.")
                    return

            data_now = datetime.date.today()
            # print(name, surname, hotel, data, day, data_now, sep='\n')

            cur.execute('''
            INSERT INTO orders (data, id_guest, id_hotel, data_settlement, number_day) 
            VALUES
            (
                ?,
                (SELECT id FROM guests WHERE name=? and surname=?),
                (SELECT id FROM hotels WHERE name=?),
                ?,
                ?    
            );
            ''', (data_now, name, surname, hotel, data, day))

            con.commit()

        except ValueError:
            mb.showinfo("Error", "Некорректный ввод данных")


class DeleteOrdersWindow(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title('Удалить заказ')
        self.geometry('400x200+100+200')
        self.config(bg=main_color)

        label = tk.Label(self, text='Введите id\nзаказа', font=font_main, width=15, bg=main_color, fg='white')
        label.grid(row=0, column=0, ipady=20)

        self.box_id = tk.Entry(self, width=20)
        self.box_id.grid(row=0, column=1)

        btn_add = tk.Button(self, text="Удалить", bg=btn_color, font=font_main,
                            command=lambda:self.delete_order(int(self.box_id.get())))
        btn_add.grid(row=4, column=0)

        btn_close = tk.Button(self, text="Закрыть", bg=btn_color, font=font_main,
                              command=lambda: self.destroy())
        btn_close.grid(row=4, column=1)

    def delete_order(self, id):
        cur.execute('DELETE FROM orders WHERE id = ?', (id,))
        con.commit()
        self.box_id.delete(0, 'end')


if __name__ == '__main__':
    root = tk.Tk()
    frame = OrdersWindow(root, root)
    frame.grid(row=0, column=0)

    root.mainloop()

