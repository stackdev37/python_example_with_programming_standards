import six
from .shape import Shape

class Square(Shape):
    def __init__(self, x, y, width):
        # init values
        Shape.__init__(self, x, y)
        self.IV_width = 0
        # init values
        self.IV_name = 'Square'
        self.set_width(width)

    def validate_width(self, width):
        if not isinstance(width, six.integer_types):
            print('Invalid data:: width')
            return False
        return True

    #overriding base class definition
    def draw(self):
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x, 'y:', self.IV_y)
        print('Width:', self.IV_width)

    def set_width(self, width):
        if self.validate_width(width):
            self.IV_width = width

    def get_area(self):
        return 2 * self.IV_width