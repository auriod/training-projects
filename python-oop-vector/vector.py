from math import sqrt, acos, degrees


class Vector:
    """
    class Vector - класс для работы с векторами.
    Vector(x, y, z)
        x, y, z - координаты вектора;
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __float__(self):
        """
        Определение длины отрезка (модуля) вектора.
        |a(x,y,z)| = sqrt(x**2 + y**2 + z**2)
        """
        return round(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 5)

    def __str__(self):
        # if self.x >= 0:
        #     x = f'{self.x}'
        # else:
        #     x = f'-{abs(self.x)}'
        # if self.y >= 0:
        #     y = f'+ {self.y}'
        # else:
        #     y = f'- {abs(self.y)}'
        # if self.z >= 0:
        #     z = f'+ {self.z}'
        # else:
        #     z = f'- {abs(self.z)}'
        # return f'{x}i {y}j {z}k'
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        """
        Сложение векторов.
        a(x1,y1,z1) + b(x2,y2,z2) = c(x1+x2, y1+y2, z1+z2)
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        """
        Унарный минус. Знаки значений координат вектора меняются на противоположные
        """
        return Vector(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        """
        Разность векторов
        a(x1,y1,z1) - b(x2,y2,z2) = c(x1-x2, y1-y2, z1-z2)
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """
        Произведение вектора на число и скалярное произведение векторов.
        Если other - число - возвращается вектор с измененными координатами;
        a(x,y,z) * n = a(x*n, y*n, z*n)
        Если other - объект класса Vector - возращается значение типа float;
        a(x1,y1,z1) * b(x2,y2,z2) = x1*x2 + y1*y2 + z1*z2
        """
        if type(other) == float or type(other) == int:
            return Vector(round(self.x * other, 3), round(self.y * other, 3), round(self.z * other, 3))
        else:
            return round(self.x * other.x + self.y * other.y + self.z * other.z, 3)

    def __bool__(self):
        """
        Если вектор ненулевой - True
        Если вектор нулевой - False
        """
        return not (self.x == 0 and self.y == 0 and self.z == 0)

    def __eq__(self, other):
        """
        Проверка равенства двух векторов (==).
        Векторы равны если они сонаправлены и их модули равны.
        """
        return (float(self) == float(other)) and is_aligned(self, other)

    def __lt__(self, other):
        """
        Операция 'строго меньше': <
        """
        return float(self) < float(other)

    def __le__(self, other):
        """
        Операция 'меньше или равно': <=
        """
        return (float(self) < float(other)) or (float(self) == float(other))

    def __qt__(self, other):
        """
        Операция 'строго больше': >
        """
        return float(self) > float(other)

    def __qe__(self, other):
        """
        Операция 'больше или равно': >=
        """
        return (float(self) > float(other)) or (float(self) == float(other))


def get_angle(vector_a, vector_b, unit='r'):
    """
    функция возвращает значение угла между векторами vector_a и vector_b.
    если вектор vector_a или vector_b является нулевым, функция возвращает -1
    если вектор vector_a или vector_b равны и сонаправленны, угол 0
    если вектор vector_a или vector_b равны и разнонаправленны, угол 180 градусов / 3,14159 радиан(pi)
    переменная unit определяет единицы измерения угла:
      'r' - радианы (по умолчанию); 'd' - градусы
    угол между ab = arccos((a * b) / (|a| * |b|))
    """
    if (not vector_a) or (not vector_b): return -1
    if vector_a == vector_b: return 0
    if unit == 'r':
        if vector_a == -vector_b or vector_b == -vector_a: return 3.14159
        return round(acos((vector_a * vector_b) / (float(vector_a) * float(vector_b))), 2)
    elif unit == 'd':
        if vector_a == -vector_b or vector_b == -vector_a: return 180
        return round(degrees(acos((vector_a * vector_b) / (float(vector_a) * float(vector_b)))), 2)


def get_vector_mul(vector_a, vector_b):
    """
    Векторное произведение векторов vector_a и vector_b.
    [a(x1,y1,z1) * b(x2,y2,z2)] = c(y1*z2 - z1*y2, -(x1*z2 - x2*z1), x1*y2 - x2*y1)
    """
    return Vector(vector_a.y * vector_b.z - vector_a.z * vector_b.y,
                  -(vector_a.x * vector_b.z - vector_a.z * vector_b.x),
                  vector_a.x * vector_b.y - vector_a.y * vector_b.x)


def get_projection(vector_a, vector_b):
    """
    метод возвращает значение проекции вектора vector_a на вектор vector_b.
    если вектор vector_a или vector_b является нулевым, функция возвращает -1
    ПрbA - проекция вектора a на вектро b = a*b/|b|
    """
    if (not vector_a) or (not vector_b): return -1
    return round((vector_a * vector_b) / float(vector_b), 5)


def is_collinear(vector_a, vector_b):
    """
    метод проверяет являются ли вектора коллинеарными.
    Векторы коллинеарны если их векторное произведение - нулевой вектор.
    True - коллинеарны; False - неколлинеарны
    """
    return not (get_vector_mul(vector_a, vector_b))


def is_aligned(vector_a, vector_b):
    """
    метод проверяет сонаправленность векторов
    True - сонаправленны; False - разнонаправленны
    """
    return is_collinear(vector_a, vector_b) and (vector_a * vector_b > 0)


def get_vector(point_a, point_b):
    """
    функция возвращает объект класса Vector.
    координаты вектора высчитываются из координат точек начала и конца вектора
    :param point_a: координаты начальной точки вектора
    :param point_b: координаты конечной точки вектора
    :return: объект класса Vector [x, y, z]
    """
    x1, y1, z1 = point_a[0], point_a[1], point_a[2]
    x2, y2, z2 = point_b[0], point_b[1], point_b[2]
    return Vector(x2 - x1, y2 - y1, z2 - z1)


if __name__ == '__main__':
    """
    a = Vector(2,3,4)
    b = Vector(2,3,4)
    print(float(a), float(b), sep='\n')
    print(get_angle(a,b), get_angle(a,b, 'd'))
    """

    print('Создание вектора a:')
    x1, y1, z1 = [int(e) for e in input('Введите координаты начальной точки: ').split(',')]
    x2, y2, z2 = [int(e) for e in input('Введите координаты конечной точки: ').split(',')]
    a = get_vector((x1, y1, z1), (x2, y2, z2))
    print(f'Создан вектор a({a})')

    print('Создание вектора b:')
    x1, y1, z1 = [int(e) for e in input('Введите координаты начальной точки: ').split(',')]
    x2, y2, z2 = [int(e) for e in input('Введите координаты конечной точки: ').split(',')]
    b = get_vector((x1, y1, z1), (x2, y2, z2))
    print(f'Создан вектор b({b})')

    print(f'Модуль вектора a = {float(a)}\nМодуль вектора b = {float(b)}')
    print(f'Сумма векторов a+b = {a+b}\nРазность векторов a-b = {a-b}')
    print(f'Скалярное произведение a*b: {a*b}\nВекторное произведение a*b: {get_vector_mul(a, b)}')
    print(f"Угол между векторами a b: {get_angle(a, b)} радиан, " +
          f"{get_angle(a, b, 'd')} градусов")
    print(f'Проекция вектора a на вектор b: {get_projection(a, b)}')
    print(f'Проекция вектора b на вектор a: {get_projection(b, a)}')

    if is_collinear(a, b):
        print('Вектор a и b: коллинеарны')
    else:
        print('Вектор a и b: неколлинеарны')
    if is_aligned(a, b):
        print('Вектор a и b: сонаправленные')
    else:
        print('Вектор a и b: разнонаправленные')


