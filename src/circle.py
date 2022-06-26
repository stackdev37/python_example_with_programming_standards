from xmlrpc.client import Boolean
import six
import math
from .shape import Shape

class Circle(Shape):
    # definition
    IV_radius: int

    def __init__(self, x: int, y: int,  radius: int) -> None:
        # init values
        super().__init__(x, y)
        self.IV_radius = 0
            
        self.IV_name = 'Circle'
        self.set_radius(radius)
    
    def validate_radius(self, radius: int) -> Boolean:
        if isinstance(radius, six.integer_types):
            return True
        else: 
            print('Invalid data:: radius')
            return False

    #overriding base class definition
    def draw(self) -> None:
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x, 'y:', self.IV_y)
        print('Radius:', self.IV_radius)

    def get_radius(self) -> int:
        return self.IV_radius

    def set_radius(self, radius) -> None:
        assert self.validate_radius(radius), 'invalid type error: circle radius'
        self.IV_radius = radius

    def get_area(self) -> int:
        return math.pi * self.IV_radius * 2
