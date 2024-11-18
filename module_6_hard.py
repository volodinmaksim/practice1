
class Figure:
    sides_count = 0
    def __init__(self, color = None, sides = None, filled = False):
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [1]*self.sides_count
        self.__color = color
        self.filled = filled

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def __is_valid_sides(self, *args):
        if len(args) != len(self.__sides):
            return False

        return all(isinstance(side, int) and side > 0 for side in args)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=None, sides=None, filled=False):
        super().__init__(color, sides, filled)
        self.__radius = sides[0] / 2 * 3.14

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=None, sides=None, filled=False):
        super().__init__(color, sides, filled)

    def get_square(self):
        p = self.__len__()/2
        return __import__('math').sqrt(p * (p - self.get_sides()[0]) * \
                (p - self.get_sides()[1]) * (p - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=None, side=None, filled=False):
        super().__init__(color, side*12, filled)

    def get_volume(self):
        return self.get_sides()[0]**3


circle1 = Circle((200, 200, 100), [10]) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), [6])

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())