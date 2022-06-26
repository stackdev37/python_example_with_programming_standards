from xmlrpc.client import Boolean
import six
# Missing typing documentation. read more about it in python:typing :: https://docs.python.org/3/library/typing.html
class Shape:
    IV_x: int
    IV_y: int
    IV_name: str
    IV_color: str
    
    def __init__(self, x: int, y: int, color: str = 'black') -> None:
        # init default values
        self.IV_x = 0
        self.IV_y = 0
        # init values
        self.IV_name = 'Shape'
        assert self.set_x(x), 'invalid type error: x' 
        assert self.set_y(y), 'invalid type error: y' 
        assert self.set_color(color), 'invalide type error: color' 

    def draw(self) -> None:
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x, 'y:', self.IV_y)

    def set_x(self, x) -> Boolean:
        if isinstance(x, six.integer_types): 
            self.IV_x = x
            return True
        return False

    def set_y(self, y: int) -> Boolean:
        if isinstance(y, six.integer_types): 
            self.IV_y = y
            return True
        return False

    def set_color(self, color: str) -> Boolean: 
        if isinstance(color, six.string_types):
            self.IV_color = color
            return True
        return False

    def getPythonVersion() -> None:
        if six.PY2:
            # something in PY2
            print('Python version: 2.x')
        else:
            #something in PY3
            print('Python version: 3.x')
