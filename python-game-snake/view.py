'''
View (MVC):
'''
from tkinter import *


class View:
    def __init__(self, m, n, a, master, database):
        """
        :param m: width
        :param n: height
        :param a: размер ячейки
        :param master: root
        :param database: объек DataBase в котором хранятся логи игры
        """
        self.m, self.n, self.a, self.master = m, n, a, master
        self.database = database

        self.menu = Menu()
        self.master.config(menu=self.menu)
        self.menu.add_command(label='Журнал', command=self.show_log_game)
        self.menu.add_command(label='Выход', command=lambda: self.master.destroy())

        self.lebel_frame = LabelFrame(self.master,
                                      width=self.n*self.a, height=80,
                                      bg='FloralWhite')
        self.lebel_frame.pack()

        self.lebel_point = Label(self.lebel_frame,
                                 font='Garamond 40 bold',
                                 text='0/0',
                                 width=10, bg='FloralWhite')
        self.lebel_point.grid(row=0, column=0)

        self.lebel_level = Label(self.lebel_frame,
                                 font='Garamond 20 bold',
                                 text='Level 0', width=18, bg='FloralWhite')
        self.lebel_level.grid(row=0, column=1)

        self.canvas = Canvas(self.master, height=m * a, width=n * a, bg='yellow')
        self.canvas.pack()

        self.text_loss = self.canvas.create_text(int((self.n*self.a) / 2),
                                                 int((self.m*self.a) / 2),
                                                 font='Courier 30 bold')

    def show_points(self, points, point_to_next):
        self.lebel_point['text'] = f'{points} / {point_to_next}'

    def show_level(self, level):
        self.lebel_level['text'] = f'Level {level}'

    def show_loss_text(self):
        self.canvas.itemconfig(self.text_loss, text='GAME OVER', fill='black')

    def clear_loss_text(self):
        self.canvas.itemconfig(self.text_loss, text='', fill='black')

    def show_log_game(self):
        root_log = Toplevel(self.master)
        root_log.title('Журнал')
        text_log = Text(root_log,
                        width=52,
                        height=20,
                        bg='#FFFFE0')
        text_log.pack()
        s = '{:^16}||{:^8}||{:^8}||{:^8}\n' \
            .format('Дата', 'Уровень', 'Очки', 'Длина змеи')
        text_log.insert(1.0, s)
        for data in self.database.get_data_db():
            text_log.insert(2.0, '{:^16}||{:^8}||{:^8}||{:^8}\n'
                            .format(data['data'], data['level'], data['points'], data['length']))
        root_log.mainloop()









