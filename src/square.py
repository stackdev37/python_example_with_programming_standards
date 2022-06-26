from xmlrpc.client import Boolean
import six
from .shape import Shape

class Square(Shape):

    IV_width: int
    IV_name: str

    def __init__(self, x: int, y: int, width: int) -> None:
        # init values
        super().__init__(x, y)
        self.IV_width = 0
        # init values
        self.IV_name = 'Square'
        self.set_width(width)

    def validate_width(self, width: int) -> Boolean:
        if isinstance(width, six.integer_types): 
            return True
        else: 
            print('Invalid data:: width')
            return False

    # overriding base class definition
    def draw(self) -> None:
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x, 'y:', self.IV_y) 
        print('Width:', self.IV_width)

    def set_width(self, width: int) -> None: 
        assert self.validate_width(width), 'invalid type error: square -> width'
        self.IV_width = width

    def get_area(self) -> int:
        return 2 * self.IV_width