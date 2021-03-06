# python-game-snake

Python 3, Tkinter, SQLite 

# Игра SnakeGame

Змея движеться по пшеничному полю. 
Красные кружочки - "яблоки" дают 5 очков, добавляют 1 сегмент,
Синие квадратики - "сливы" дают 10 очков, добавляют 2 сегмент,
Черный квадрат - "вьетнамская ловушка" забирает 100 очков.

При повышении уровня: змея сбрасывает кожу и становиться быстрее, увеличивается количество необходимых очков для следующего уровня

Управление:
стрелки - направление движения змеи,
л. кнопка мыши - при проигрыше рестартит игру
п. кнопка мыши - пауза

Логи игры сохранены в базе данных и доступны во вкладке "Журнал" меню окна игры

Использована схема MVC 
########################################################################################
Model: 
	файл model.py
классы:

	Segment - модель сегмента, из которых состоит змея  
		move_segment() - движение сегмента
		change_color(color) - изменение цвета сегмента

	Snake - модель змеи
		move(direction) - движение змеи в направлении, задаваемом переменной direction
		growth_snake() - добавление сегмента в конец змеи
		change_color() - изменение цвета змеи. Цвет выбирается рандомно из списка colors
		delete() - удаление змеи с экрана
		оператор == (_eq_) - проверка совпадения координат первого сегмента с координатами сравниваемого объекта 
		_len_ - возвращает количество сегментов змеи

	Food - модель "яблока"
		Food.ccal - поле, определяющее сколько сегментов добавиться при съедании
		Food.point - количество очков за съедение


	BigFood - модель "большого яблока"
		BigFood.ccal - поле, определяющее сколько сегментов добавиться при съедании
		BigFood.point - количество очков за съедение

	Trap - модель ловушки. При попадании в нее - отнимаются очки
		Trap.points - количество отнимаемых очков
		active() - возвращает количество очков игры, из которых вычтено поле Trap.points
	
	DataBase - модель базы данных. Данные сохраняются в таблицу log_game. Поля таблицы: data, points, level, length
		:param filename: имя файла БД
        :param tablename: наименование таблицы для хранения данных
		
		save_date_db(data) - сохраняет данные (список data) в базу данных
		create_table() - создание таблицы для хранения 
		

########################################################################################

View:
	файл view.py
класс:
	View - описывает все элементы окна игры: canvas, label, menu ...
		:param m: width
        :param n: height
        :param a: размер ячейки
        :param master: root
        :param database: объек DataBase в котором хранятся логи игры
		
		show_points(points, point_to_next) - отображение текущего количества 
				очков (points) и количство очков необходимого для перехода на следующий уровень(point_to_next)
		
		show_level(level) - отображение уровня игры (level)

		show_loss_text() - отображение надписи "GAME OVER"

		clear_loss_text() - удаление надписи "GAME OVER"

		show_log_game() - отображение окна с логами игры. Данные передаются 
						из базы данных database.db в виде dict 

########################################################################################

Controller:
	файл game.py
класс:
	Game - описывает процесс игры
		start() - процесс игры. Инкрементирование счетчика каждый вызов функции. 
				Если счетчик кратен 20 - создается объект класса Food, 70 - BigFood, 111 - Trap.

		create_food() - создает объект класса Food со случайными координатами

		create_big_food() - создает объект класса BigFood со случайными координатами
		
		create_trap() - создает объект класса Trap со случайными координатами
		
		next_level() - переход на новый уровень. Увеличение скорости игры, увеличение 
						в два раза количества необходимых для слеждеющего уровня очков, изменение цвета змеи
		
		crossing() - проверка "аварии" змеи (коорд. первого сегмента == коорд. любого другого сегмента)

		loos_game() - конец игры - сохранение данных, появляется возможность перезапуска игры (флаг self.flag_end_game)
		
		save_data() - сохранение данных игры (кол-во очков, длина змеи, уровень, дата/время). 
					Данные передаются в виде списка методу save_date_db() объекта DataBase.

		keypress(event) - обработчик нажатий на клавиши управления. Изменение направление движения змеи (переменная direction) 

		pause_game(event) - обработчик нажатия правой кнопки мыши. Пауза в игре (изменение значения флага self.flag_pause)

		restart_game(event) - обработчик нажатия левой кнопки мыши. Рестарт игры (при значении "1" флага self.flag_end_game)
							Возвращает переменным начальное значение, очищает списки foods и traps, очистка canvas
