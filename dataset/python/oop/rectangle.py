
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return False


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class ParaSquare(Square):
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        return self.width * 2


class Rectangle__cp:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tmp = width

    def area(self):
        return self.tmp * self.height

    def perimeter(self):
        return 2 * (self.tmp + self.height)


class Rectangle__cf:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.k = 2

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.k * (self.width + self.height)




def test():
    a = Rectangle(5, 10)
    b = ParaSquare(25)    
    return a == b
