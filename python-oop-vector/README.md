# python-oop-vector

Класс Python для работы с векторами

1. # vector.py

class Vector(x, y, z) - класс для работы с векторами
	x, y, z - координаты векторами

Реализованные операции с векторами:
	- модуль вектора 
	- сложение/разность векторов
	- унарный минус
	- произведение векторов 
	- проверка нулевого вектора 
	- сравнение векторов
	- 

Доп. функции:
	- get_angel(vector_a, vector_b, unit='r') - возвращает угол
			между векторами vector_a и vector_b. unit - единицы измерения:
			'r' - радианы, 'd' - градусы
	- get_vector_mul(vector_a, vector_b) - возвращает векторное произведение vector_a и vector_b
	- get_projection(vector_a, vector_b) - проекция vector_a на vector_b. нулевой вектор - возвращается -1
	- is_collinear(vector_a, vector_b) - проверка коллинеарности векторов
	- is_aligned(vector_a, vector_b) - проверка сонаправленности векторов
	- get_vector(point_a, point_b) - возвращает объект класса Vector, координаты вектора высчитываются из координат точек начала и конца вектора 

2. # calculator.pyw

GUI-приложение (Tkinter) - калькулятор векторов

3. # test_vector.py

unit-тест класса Vector