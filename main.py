from asyncio.windows_events import NULL
import math
import six

class Shape:
    def __init__(self, x, y, color = 'black'):
        if not isinstance(x, six.integer_types):
            print('Type error: X')
            x = 0
        if not isinstance(y, six.integer_types):
            print('Type error: Y')
            y = 0
        self.name = 'Shape'
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        print('Drawing', self.name, 'at origin x:', self.x, 'y:', self.y)

    def setColor(self, color):
        self.color = color

    def getPythonVersion():
        if six.PY2:
            # something in PY2
            print('Python version: 2.x')
        else:
            #something in PY3
            print('Python version: 3.x')
    
class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        Shape.__init__(self, x, y)
        if not isinstance(width, six.integer_types):
            print('Type error: width')
            width = 0
        if not isinstance(height, six.integer_types):
            print('Type error: height')
            height = 0
        self.name = 'Rectangle'
        self.height = height
        self.width = width
    
    #overriding base class definition
    def draw(self):
        print('Drawing', self.name, 'at origin x:', self.x,'y:', self.y)
        print('Height:', self.height, 'Width:', self.width)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, x, y, width):
        Shape.__init__(self, x, y)
        if not isinstance(width, six.integer_types):
            print('Type error: width')
            width = 0
        self.name = 'Square'
        self.width = width
    
    #overriding base class definition
    def draw(self):
        print('Drawing', self.name, 'at origin x:', self.x, 'y:', self.y)
        print('Width:', self.width)

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return 2 * self.width

class Circle(Shape):
    def __init__(self, x, y,  radius):
        Shape.__init__(self, x, y)
        if not isinstance(radius, six.integer_types):
            print('Type error: radius')
            width = 0
        self.name = 'Circle'
        self.radius = radius
    #overriding base class definition
    def draw(self):
        print('Drawing', self.name, 'at origin x:', self.x, 'y:', self.y)
        print('Radius:', self.radius)

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
sh = Shape('qq', 4)
sh.draw()
rec = Rectangle(1, 2, 5, 10)
rec.draw()
cir = Circle(3, 3, 10)
cir.draw()
sqr = Square(3,3, 10)
sqr.draw()



