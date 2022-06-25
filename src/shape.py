import six

class Shape:
    def __init__(self, x, y, color = 'black'):
        # init default values
        self.IV_x = 0
        self.IV_y = 0
        # validate check
        if not isinstance(x, six.integer_types):
            print('Invalid data:: X')
            x = 0
        if not isinstance(y, six.integer_types):
            print('Invalid data:: Y')
            y = 0
        # init values
        self.IV_name = 'Shape'
        self.set_x(x)
        self.set_y(y)
        self.set_color(color)

    def draw(self):
        print('Drawing', self.IV_name, 'at origin x:', self.IV_x, 'y:', self.IV_y)

    def set_x(self, x):
        if not isinstance(x, six.integer_types):
            print('Invalid data:: X')
        else:
            self.IV_x = x

    def set_y(self, y):
        if not isinstance(y, six.integer_types):
            print('Invalid data:: Y')
        else:
            self.IV_y = y

    def set_color(self, color):
        self.color = color

    def getPythonVersion():
        if six.PY2:
            # something in PY2
            print('Python version: 2.x')
        else:
            #something in PY3
            print('Python version: 3.x')
