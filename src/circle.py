import six
import math
from .shape import Shape

class Circle(Shape):
    def __init__(self, x, y,  radius):
        # init values
        Shape.__init__(self, x, y)
        self.IV_radius = 0
            
        self.IV_name = 'Circle'
        self.set_radius(radius)
    
    def validate_radius(self, radius):
        if not isinstance(radius, six.integer_types):
            print('Invalid data:: radius')
            return False
        return True

    #overriding base class definition
    def draw(self):
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x, 'y:', self.IV_y)
        print('Radius:', self.IV_radius)

    def get_radius(self):
        return self.IV_radius

    def set_radius(self, radius):
        if self.validate_radius(radius):
            self.IV_radius = radius

    def get_area(self):
        return math.pi * self.IV_radius * 2
