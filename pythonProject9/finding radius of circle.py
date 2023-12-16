# important concepts
# procedural (functional) vs OOP
# classes - holds attributes and methods
# objects - instance of that class, may be different (subclass)
# attributes -
# methods -
# self parameter - has to be in all methods in the class.
# instantiation - created a single object
# encapsulation -
# data hiding -
# abstraction - idea of not knowing what's going on internally, unless the language requires it
# state - where it's at currently, on or off.

# classes define the attributes and methods for a particular type of object

# objects - think of cookies and a cookie cutter. The cookie cutter is the class (blueprint)
# and each cookie is an object created when we use the cookie cutter.
import math


class Circle:
    # class attributes go here, as in the __init__ for initialization.
    # self is mandatory in every method. Self ensure python is operating on the
    # specific object that the method is supposed to operate on.
    # self is focusing on that specific object itself
    def __init__(self, radius):  # initializes the attributes
        self.radius = radius

    # accessors and mutators
    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    # methods go here
    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * self.radius * math.pi

    def diameter(self):
        return 2 * self.radius


def main():
    circle_radius = float(input("Enter the radius for the circle: "))
    my_circle = Circle(circle_radius)  # creating a new object called my_circle
    area = my_circle.area()
    circumference = my_circle.circumference()
    diameter = my_circle.diameter()
    print(
        f"The area of the circle is {area}, with a radius of {my_circle.get_radius()}, a circumference of {circumference} and a diameter of {diameter}.")


if __name__ == '__main__':
    main()
