from xmlrpc.client import Boolean
import six
from .shape import Shape
# Missing typing on method definitions.

class Rectangle(Shape):
    # Missing IV_width at class definition level.
    IV_width: int
    # Missing IV_height at class definition level.
    IV_height: int
    # Missing IV_name at class definition level.
    IV_name: int

    def __init__(self, x: int, y: int, height: int , width: int) -> None:
        # init default value
        Shape.__init__(self, x, y)
        self.IV_width = 0
        self.IV_height = 0
        # init values
        self.IV_name = 'Rectangle'
        # How do we know that the width and height are correct? what if we parse a string? a list or a dictionary?
        self.set_width(width)
        self.set_height(height)
        # How do developers know when it failed?
        # If any of these failed, what are we expecting? an exception, a message? a logger? how do you handle error that might happen in the future?
    
    def validate_width(self, width: int) -> Boolean:
        if isinstance(width, six.integer_types):
            return True
        else: 
            print('Invalid data:: width')
            return False
    
    def validate_height(self, height: int) -> Boolean:
        if isinstance(height, six.integer_types):            
            return True
        else:
            print('Invalid data:: height')
            return False
    #overriding base class definition
    def draw(self) -> None:
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x,'y:', self.IV_y)
        print('Height:', self.IV_height, 'Width:', self.IV_width)

    def set_width(self, width: int) -> None:
        assert self.validate_width(width), 'invalid type error: rectangle -> width'
        self.IV_width = width

    def set_height(self, height: int) -> None:
        assert self.validate_height(height), 'invalid type error: rectangle -> height'
        self.IV_height = height

    def get_area(self) -> int:
        return self.IV_width * self.IV_height

