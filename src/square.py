from xmlrpc.client import Boolean
import six
from .shape import Shape

class Square(Shape):

    # missing IV_width at class level.
    IV_width: int
    # missing IV_name definition at class level.
    IV_name: str

    def __init__(self, x: int, y: int, width: int) -> None:
        # init values
        Shape.__init__(self, x, y) # you can use `super().__init__(x,y)`
        self.IV_width = 0 # you need to declare the IV_width attr. inside the class description
        # init values
        self.IV_name = 'Square' # you need to declare the IV_width attr. inside the class description
        self.set_width(width)
        # How do developers know when it failed?

    def validate_width(self, width: int) -> Boolean:
        if isinstance(width, six.integer_types): # i would advice you to use a more simple to read expression like `if isinstance(...) is False`, since most people might get confused with the `if not` logic block.
            return True
        else: 
            print('Invalid data:: width')
            return False

    # overriding base class definition
    def draw(self) -> None:
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x, 'y:', self.IV_y) # i would advice you to use a F-string, it makes easier to see what will be the endr result. and also is less blocking.
        print('Width:', self.IV_width)

    def set_width(self, width: int) -> None: # what if it fails?, what happens if width is not the type of self.IV_width?.
        assert self.validate_width(width), 'invalid type error: square -> width'
        self.IV_width = width

    def get_area(self) -> int:
        return 2 * self.IV_width