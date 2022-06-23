import six
from .shape import Shape

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