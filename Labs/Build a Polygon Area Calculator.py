from math import sqrt


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width, /):  # The '/' makes 'name' positional-only
        self.width = width

    def set_height(self, height, /):  # The '/' makes 'name' positional-only
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            represents_shape = ""
            for _ in range(self.height):
                represents_shape=represents_shape + "*" * self.width +"\n"
            return represents_shape

    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
    def __init__(self, side_length) -> None:
        self.width = side_length
        self.height = side_length

    def set_width(self, side_length, /):
        self.width = side_length
        self.height = side_length

    def set_height(self, side_length, /):
        self.width = side_length
        self.height = side_length

    def set_side(self, value):
        self.width = value
        self.height = value

    def __str__(self) -> str:
        return f"Square(side={self.height})"


def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

if __name__ == "__main__":
    main()
