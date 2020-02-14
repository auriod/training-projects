'''
Controller (MVC)
'''
from tkinter import *
from view import View
from model import *
import random as rnd
import time


class Game:
    def __init__(self):
        self.width, self.height, self.a = 30, 30, 25
        self.direction = 'right'  # направление движения змеи на старте
        self.counter = 0  # счетчик
        self.speed_game = 300  # скорость игры
        self.level_game = 0  # уровень игры
        self.points = 0  # количество очков
        self.points_for_level = 20  # необходимое количество очков для следующего уровня
        self.foods = []  # список объектов классов Food, BigFood- "яблоки"
        self.traps = []  # список объектов класс Trap - "ловушки"
        self.flag_pause = 0
        self.flag_end_game = 0
        self.database = DataBase('log.db')  # объект класса DataBase для работы с БД
        self.root = Tk()
        self.root.title('SnakeGame')
        self.root.geometry('+100+100')
        self.view = View(self.width, self.height, self.a, self.root, self.database)
        self.snake = Snake(self.a, self.view.canvas, self.width, self.height)
        self.root.bind('<Key>', self.keypress)
        self.root.bind('<Button-1>', self.restart_game)
        self.root.bind('<Button-3>', self.pause_game)
        self.root.after(100, self.start)

        self.root.mainloop()

    # обработчик нажатия "стрелок"
    def keypress(self, e):
        keys = {'left': 37, 'right': 39, 'up': 38, 'down': 40}

        # нельзя двигаться в противоположную сторону
        if e.keycode == keys['left'] and self.direction != 'right':
            self.direction = 'left'
        if e.keycode == keys['right'] and self.direction != 'left':
            self.direction = 'right'
        if e.keycode == keys['up'] and self.direction != 'down':
            self.direction = 'up'
        if e.keycode == keys['down'] and self.direction != 'up':
            self.direction = 'down'

    def start(self):
        self.counter += 1
        # создание "еды" и "ловушек"
        if len(self.foods) < 5 and self.counter % 20 == 0:  # не более 4 яблок на экране
            self.create_food()
        if len(self.foods) < 5 and self.counter % 70 == 0:  # не более 4 "слив" на экране
            self.create_big_food()
        if len(self.traps) < 4 and self.counter % 111 == 0:  # не более 3 "ловушек" на экране
            self.create_trap()
        self.snake.move(self.direction)

        # проверка попадания в ловушку
        for trap in self.traps:
            if self.snake == trap and type(trap) is Trap:
                self.points = trap.active(self.points)
                self.view.show_points(self.points, self.points_for_level)
                self.traps.remove(trap)
                trap.delete()

        # проверка поглощения "еды"
        for food in self.foods:
            if self.snake == food:
                for i in range(food.ccal):
                    self.snake.growth_snake()
                self.points += food.point
                self.view.show_points(self.points, self.points_for_level)
                self.foods.remove(food)
                food.delete()
        # переход на новый уровень
        if self.points >= self.points_for_level:
            self.next_level()

        # проверка самопоглощения
        if not self.crossing():
            # проверка не нажата ли пауза
            if self.flag_pause == 0:  # флаг поднимается функцией pause_game
                self.root.after(self.speed_game, self.start)
        else:
            self.loos_game()

    def create_food(self):
        x = rnd.randint(0, self.width - 1)
        y = rnd.randint(0, self.height - 1)
        self.foods.append(Food(self.a, x, y, self.view.canvas))

    def create_big_food(self):
        x = rnd.randint(0, self.width - 1)
        y = rnd.randint(0, self.height - 1)
        self.foods.append(BigFood(self.a, x, y, self.view.canvas))

    def next_level(self):
        self.level_game += 1
        self.speed_game -= 10
        self.points_for_level *= 2
        self.snake.change_color()
        self.view.show_points(self.points, self.points_for_level)
        self.view.show_level(self.level_game)

    # проверка самопоглощения: возвращает True если координата первого сегмента совпадает с коорд. других сегментов
    def crossing(self):
        return any([self.snake.segments[0].x == s.x and self.snake.segments[0].y == s.y for s in self.snake.segments[1:]])

    def create_trap(self):
        x = rnd.randint(0, self.width - 1)
        y = rnd.randint(0, self.height - 1)
        self.traps.append(Trap(self.a, x, y, self.view.canvas))

    def loos_game(self):
        self.view.show_loss_text()
        self.save_data()
        self.flag_end_game = 1  # поднят флаг окончания игры, допускается рестарт

    def restart_game(self, event):
        if self.flag_end_game == 1:  # флаг поднимается функцией loos_game
            # возращение стандартных настроек
            self.view.clear_loss_text()
            self.flag_end_game = 0
            self.snake.delete()  # delete old snake
            self.snake = Snake(self.a, self.view.canvas, self.width, self.height)
            self.direction = 'right'
            self.counter = 0
            self.speed_game = 300
            self.level_game = 0
            self.points = 0
            self.points_for_level = 20
            # очистка canvas
            for food in self.foods:
                food.delete()
            for trap in self.traps:
                trap.delete()
            # очистка списков
            self.foods.clear()
            self.traps.clear()
            self.view.show_points(self.points, self.points_for_level)
            self.view.show_level(self.level_game)
            # запуск
            self.start()

    def pause_game(self, event):
        if self.flag_pause == 0:
            self.flag_pause = 1
        else:
            self.flag_pause = 0
            self.start()

    def save_data(self):
        time_ = time.strftime('%d.%m.%Y %H:%M', time.localtime())
        # список параметров игры: дата/время, очки, уровень, длина змеи
        data = [time_, self.points, self.level_game, len(self.snake)]
        self.database.save_date_db(data)


