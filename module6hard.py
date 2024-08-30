from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, __color: tuple, *__sides, filled=False):
        self.__sides = list(__sides)
        self.__color = list(__color)
        self.filled = filled
        if len(self.__color) != 3:
            print('Неправильный ввод цвета! Должно быть 3 числа (формат RGB)')
            exit()

        if len(self.__sides) != self.sides_count:
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        return self.__color

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if not isinstance(side, int) or side <= 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(self, *new_sides) and len(new_sides) == self.sides_count:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=filled)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius * self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=filled)
        if not self.__are_valid_triangle_sides():
            print('Не может быть треугольника с такими сторонами!')


    def __are_valid_triangle_sides(self): # проверим, может ли быть треугольник с такими сторонами
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        return a + b > c and a + c > b and b + c > a

    def get_square(self):
        if self.__are_valid_triangle_sides():
            a = self.get_sides()[0]
            b = self.get_sides()[1]
            c = self.get_sides()[2]
            return 0.25 * sqrt((a ** 2 + b ** 2 + c ** 2) ** 2 - 2 * (a ** 4 + b ** 4 + c ** 4))
        else:
            print('Неверные стороны треугольника!')

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled=False):
        if len(__sides) == 1:
            __sides = [__sides[0]] * 12
        super().__init__(__color, *__sides, filled=filled)


    def get_square(self):
        return (self.get_sides()[0] ** 2) * 6

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Выполним проверки из задания:

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# А теперь выполним проверки каждой фигуры
print('Мои собственные проверки:')
fig1 = Circle((255, 255, 0), 3, 4, 6, 1)
print('Круг:')
print('Стороны: ', fig1.get_sides())
print('Цвет: ', fig1.get_color())
print('Зададим новый цвет:', fig1.set_color(200, 300, 500))
print('Цвет неверный, поэтому не меняется')
print('Зададим еще раз новый цвет:', fig1.set_color(200, 30, 50))
print('Заданный формат цвета верный, поэтому поменялся: ', fig1.get_color())

fig2 = Circle((200, 100, 50), 7)
print('Другой круг:')
print('Стороны: ', fig2.get_sides())
print('Поменяем стороны:')
fig2.set_sides(16)
print(fig2.get_sides())
print(f'Площадь круга с длиной окружности {fig2.get_sides()[0]}: {fig2.get_square()} ')

triangle1 = Triangle((0, 255, 0), 3, 4, 6, 1)
print('Треугольник:')
print('Стороны: ', triangle1.get_sides())
print('Цвет: ', triangle1.get_color())
print('Зададим новый цвет:', triangle1.set_color(200, 300, 500))
print('Цвет неверный, поэтому не меняется')
print('Зададим еще раз новый цвет:', triangle1.set_color(200, 30, 50))
print('Заданный формат цвета верный, поэтому поменялся: ', triangle1.get_color())

print('Другой треугольник:')
triangle2 = Triangle((200, 100, 50), 1, 3, 5)

print('Стороны: ', triangle2.get_sides())
print('Поменяем стороны:')
triangle2.set_sides(6, 7, 9)
print(triangle2.get_sides())

print(f'Площадь треугольника со сторонами {triangle2.get_sides()}: {triangle2.get_square()} ')

print('Куб:')
my_cube = Cube((200, 100, 50), 7, 6, 5)
print('Стороны куба:', my_cube.get_sides())
print(f'Площадь поверхности куба со стороной {my_cube.get_sides()[0]}: {my_cube.get_square()}')
print('Возьмем другой куб:')
my_cube = Cube((200, 100, 50), 5)
print('Стороны куба:', my_cube.get_sides())
print(f'Объем куба со стороной {my_cube.get_sides()[0]}: {my_cube.get_volume()}')

