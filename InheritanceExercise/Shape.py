
# Import tools
import math


class Shape():
    """
    Description: Base class from which we will derive any shape that requires a computation for area and perimeter
    """

    def __init__(self):
        """
        Description: Constructor for Shape Class
        Params: 
            shape: the name of the shape
        Returns: None
        """
        self.shape = "Shape"

    def compute_perimeter(self):
        pass

    def compute_area(self):
        pass

    def print_shape(self):
        """
        Description: Function that prints the type of shape
        Params: None
        Returns: None
        """
        print("I am a ", self.shape)


class Rectangle(Shape):
    """
    Description: Child class Rectangle that inherits from parent class Shape
    Required Values: length and width of the Rectangle
    """

    def __init__(self, length, width):
        """
        Description: Constructor for Rectangle Class
        Params: 
            length: the length of the rectangle
            width: the width of the rectangle
        Returns: None
        """
        self.length = length
        self.width = width
        self.shape = "Rectangle"

    def compute_perimeter(self):
        """
        Description: Function that computes the perimeter of the rectangle
        Params: None
        Returns: 
            The permimeter of the rectangle
        """
        return 2 * (self.length + self.width)

    def compute_area(self):
        """
        Description: Function that computes the area of the rectangle
        Params: None
        Returns: 
            The area of the rectangle
        """
        return (self.length * self.width)


class Square(Rectangle):
    """
    Description: Child class Square that inherits from parent class Rectangle
    Required Values: the length of a side (All sides will be the same, so no need for length and width)
    """

    def __init__(self, side):
        """
        Description: Constructor for Square Class
        Params: 
            side: the length of the square's sides
        Returns: None
        """
        self.side = side
        self.shape = "Square"

    def compute_perimeter(self):
        """
        Description: Function that computes the perimeter of the square
        Params: None
        Returns: 
            The perimeter of the square
        """
        return 4 * self.side

    def compute_area(self):
        """
        Description: Function that computes the area of the square
        Params: None
        Returns: 
            The area of the square
        """
        return (pow(self.side, 2))


# Base class object
s = Shape()

# Sinlge inheritance
rect = Rectangle(2, 4)
print("Area of the Rectangle: ", rect.compute_area())
print("Area of the Rectangle: ", rect.compute_perimeter())
# Print shape name using inheritted method from Shape
rect.print_shape()

# Multiple Inheritance
sqr = Square(4)
print("Area of the Square: ", sqr.compute_area())
print("Area of the Square: ", sqr.compute_perimeter())
# Print shape name using inheritted method from Shape
sqr.print_shape()
