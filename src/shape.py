import six
# Missing typing documentation. read more about it in python:typing :: https://docs.python.org/3/library/typing.html
class Shape:
    # Missing IV_x definition at class level.
    # Missing IV_y definition at class level.
    # Missing IV_name definition at class level.
    # Missing IV_color definition at class level.

    def __init__(self, x, y, color = 'black'):
        # Missing descriptors at method definitions: 
        #
        # example:
        #     def __init__(self, arg_1: int, arg_2: str, arg_3: dict = {}) -> None:
        #         # Do something
        #         pass
        #
        # Missing IV_color definition at class level.
        # init default values
        self.IV_x = 0
        self.IV_y = 0
        # validate check
        if not isinstance(x, six.integer_types): # Advice: remember to simplify the sintaxis for human reading.
            print('Invalid data:: X')
            x = 0
        if not isinstance(y, six.integer_types): # Advice: remember to simplify the sintaxis for human reading.
            print('Invalid data:: Y')
            y = 0
        # init values
        self.IV_name = 'Shape'
        self.set_x(x)# How do you know it was successfull?, what if i pass a string directly to this coordenate?
        self.set_y(y)# How do you know it was successfull?, what if i pass a string directly to this coordenate?
        self.set_color(color) # How do you know the type of color is valid? what are the types that are supported?
        # How do developers know when it failed?
        # If any of these failed, what are we expecting? an exception, a message? a logger? how do you handle error that might happen in the future?

    def draw(self):
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x, 'y:', self.IV_y)

    def set_x(self, x):
        if not isinstance(x, six.integer_types): # Advice: remember to simplify the sintaxis for human reading.
            print('Invalid data:: X')
        else:
            self.IV_x = x

    def set_y(self, y):
        if not isinstance(y, six.integer_types): # Advice: remember to simplify the sintaxis for human reading.
            print('Invalid data:: Y')
        else:
            self.IV_y = y

    def set_color(self, color): # how do developers know what kind of type is color? is it a string? an hex, a binary number?
        # Why is it called color? should't it be IV_color, CV_color CVC_color, G_color?
        self.color = color

    def getPythonVersion():
        if six.PY2:
            # something in PY2
            print('Python version: 2.x')
        else:
            #something in PY3
            print('Python version: 3.x')
