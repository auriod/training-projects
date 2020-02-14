'''
Model (MVC):
'''
import random as rnd
import sqlite3
colors = ['green', 'orange', 'black', 'DeepPink', 'BlueViolet', 'Indigo', 'Teal', 'white']


class Segment:

    def __init__(self, a, x, y, canvas, color):
        self.a, self.x, self.y, self.c, self.color = a, x, y, canvas, color
        self.segment = self.c.create_oval(x*self.a, y*self.a, x*self.a+self.a, y*self.a+self.a, fill=self.color)

    def move_segment(self):
        self.c.coords(self.segment, self.x*self.a, self.y*self.a, self.x*self.a+self.a, self.y*self.a+self.a)

    def change_color(self, color):
        self.segment['fill'] = color


class Snake:
    def __init__(self, a, canvas, m, n):
        self.color = rnd.choice(colors)
        self.last_x, self.last_y = 0, 0
        self.a, self.canvas = a, canvas
        self.m, self.n = m, n
        self.segments = []
        self.segments.append(Segment(self.a, 7, 10, self.canvas, self.color))
        self.segments.append(Segment(self.a, 6, 10, self.canvas, self.color))
        self.segments.append(Segment(self.a, 5, 10, self.canvas, self.color))

    def move(self, direction):
        self.last_x = self.segments[-1].x
        self.last_y = self.segments[-1].y

        if direction == 'right':
            self.segments[-1].x = self.segments[0].x + 1
            if self.segments[-1].x == self.n:
                self.segments[-1].x = 0
            self.segments[-1].y = self.segments[0].y

        if direction == 'left':

            self.segments[-1].x = self.segments[0].x - 1

            self.segments[-1].y = self.segments[0].y
            if self.segments[-1].x == -1:
                self.segments[-1].x = self.n - 1

        if direction == 'up':
            self.segments[-1].x = self.segments[0].x
            self.segments[-1].y = self.segments[0].y - 1
            if self.segments[-1].y == -1:
                self.segments[-1].y = self.m - 1

        if direction == 'down':
            self.segments[-1].x = self.segments[0].x
            self.segments[-1].y = self.segments[0].y + 1
            if self.segments[-1].y == self.m:
                self.segments[-1].y = 0

        self.segments[-1].move_segment()
        self.segments = self.segments[-1:] + self.segments[0:-1]

    def __eq__(self, other):
        return self.segments[0].x == other.x and self.segments[0].y == other.y

    def __len__(self):
        return len(self.segments)

    def growth_snake(self):
        self.segments.append(Segment(self.a, self.last_x, self.last_y, self.canvas, self.color))

    def change_color(self):
        self.color = rnd.choice(colors)
        for segment in self.segments:
            self.canvas.itemconfig(segment.segment, fill=self.color)

    def delete(self):
        for segment in self.segments:
            self.canvas.delete(segment.segment)


class Food:
    def __init__(self,  a, x, y, canvas):

        self.a, self.x, self.y, self.c = a, x, y, canvas
        self.food = self.c.create_oval(x * self.a, y * self.a, x * self.a + self.a, y * self.a + self.a,
                                       fill='red')
        self.ccal = 1  # сколько сегментов добавляется змее
        self.point = 5  # количество очков за съедение

    def delete(self):
        self.c.delete(self.food)


class BigFood:
    def __init__(self,  a, x, y, canvas):

        self.a, self.x, self.y, self.c = a, x, y, canvas
        self.big_food = self.c.create_rectangle(x * self.a, y * self.a, x * self.a + self.a, y * self.a + self.a,
                                                fill='blue')
        self.ccal = 2  # сколько сегментов добавляется змее
        self.point = 10  # количество очков за съедение

    def delete(self):
        self.c.delete(self.big_food)


class Trap:
    def __init__(self, a, x, y, canvas):
        self.a, self.x, self.y, self.c = a, x, y, canvas
        self.points = 100  # количество вычитаемых очков
        self.trap = self.c.create_rectangle(x * self.a, y * self.a, x * self.a + self.a, y * self.a + self.a,
                                            fill='black')

    def active(self, points):
        return points - self.points

    def delete(self):
        self.c.delete(self.trap)


class DataBase:
    def __init__(self, filename, tablename='log_game'):
        """
        :param filename: имя файла БД
        :param tablename: наименование таблицы для хранения данных
        """
        self.table_name = tablename
        self.connect = sqlite3.connect(filename)
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS ''' + self.table_name + ''' 
        (
        data TEXT,
        points INTEGER,
        level INTEGER,
        length INTEGER
        )''')

    def save_date_db(self, data):
        self.cursor.execute('''
        INSERT INTO ''' + self.table_name + ''' VALUES (?, ?, ?, ?)
        ''', data)
        self.connect.commit()

    def get_data_db(self):
        self.cursor.execute('SELECT * FROM ' + self.table_name + ' ORDER BY data')
        # return self.cursor.fetchall()
        return [dict(data) for data in self.cursor.fetchall()]





