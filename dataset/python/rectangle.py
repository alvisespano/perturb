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

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return f"Square(side_length={self.width})"

def test():
    rectangle1 = Rectangle(5, 10)
    rectangle2 = Rectangle(2, 25)

    print(rectangle1)
    print("Area:", rectangle1.area())
    print("Perimeter:", rectangle1.perimeter())

    print(rectangle2)
    print("Area:", rectangle2.area())
    print("Perimeter:", rectangle2.perimeter())

    if rectangle1 == rectangle2:
        print("The two rectangles have the same area.")
    else:
        print("The two rectangles have different areas.")
