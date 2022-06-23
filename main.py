from asyncio.windows_events import NULL
import math
import six

class Shape:
    def __init__(self, x, y, color = 'black'):
        # init default values
        self.x = 0
        self.y = 0
        # validate check
        if not isinstance(x, six.integer_types):
            print('Invalid data:: X')
            x = 0
        if not isinstance(y, six.integer_types):
            print('Invalid data:: Y')
            y = 0
        # init values
        self.name = 'Shape'
        self.set_x(x)
        self.set_y(y)
        self.set_color(color)

    def draw(self):
        print('Drawing', self.name, 'at origin x:', self.x, 'y:', self.y)

    def set_x(self, x):
        if not isinstance(x, six.integer_types):
            print('Invalid data:: X')
        else:
            self.x = x

    def set_y(self, y):
        if not isinstance(y, six.integer_types):
            print('Invalid data:: Y')
        else:
            self.y = y

    def set_color(self, color):
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
        # init default value
        Shape.__init__(self, x, y)
        self.width = 0
        self.height = 0
        # init values
        self.name = 'Rectangle'
        self.set_width(width)
        self.set_height(height)
    
    def validate_width(self, width):
        if not isinstance(width, six.integer_types):
            print('Invalid data:: width')
            return False
        return True
    
    def validate_height(self, height):
        if not isinstance(height, six.integer_types):
            print('Invalid data:: height')
            return False
        return True
    #overriding base class definition
    def draw(self):
        print('Drawing', self.name, 'at origin x:', self.x,'y:', self.y)
        print('Height:', self.height, 'Width:', self.width)

    def set_width(self, width):
        if self.validate_width(width):
            self.width = width

    def set_height(self, height):
        if self.validate_height(height):
            self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, x, y, width):
        # init values
        Shape.__init__(self, x, y)
        self.width = 0
        # init values
        self.name = 'Square'
        self.set_width(width)

    def validate_width(self, width):
        if not isinstance(width, six.integer_types):
            print('Invalid data:: width')
            return False
        return True

    #overriding base class definition
    def draw(self):
        print('Drawing', self.name, 'at origin x:', self.x, 'y:', self.y)
        print('Width:', self.width)

    def set_width(self, width):
        if self.validate_width(width):
            self.width = width

    def get_area(self):
        return 2 * self.width

class Circle(Shape):
    def __init__(self, x, y,  radius):
        # init values
        Shape.__init__(self, x, y)
        self.radius = 0
            
        self.name = 'Circle'
        self.set_radius(radius)
    
    def validate_radius(self, radius):
        if not isinstance(radius, six.integer_types):
            print('Invalid data:: radius')
            return False
        return True

    #overriding base class definition
    def draw(self):
        print('Drawing', self.name, 'at origin x:', self.x, 'y:', self.y)
        print('Radius:', self.radius)

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if self.validate_radius(radius):
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



