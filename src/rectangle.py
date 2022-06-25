import six
from .shape import Shape
class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        # init default value
        Shape.__init__(self, x, y)
        self.IV_width = 0
        self.IV_height = 0
        # init values
        self.IV_name = 'Rectangle'
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
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x,'y:', self.IV_y)
        print('Height:', self.IV_height, 'Width:', self.IV_width)

    def set_width(self, width):
        if self.validate_width(width):
            self.IV_width = width

    def set_height(self, height):
        if self.validate_height(height):
            self.IV_height = height

    def get_area(self):
        return self.IV_width * self.IV_height

