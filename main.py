from src.shape import Shape    
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
    
# How do you handle errors?
# what happens if someone missplaces values in the methods?
# are there any exception ahndling?
sh = Shape('qq', 4)
sh.draw()
rec = Rectangle(1, 2, 5, 10)
rec.draw()
cir = Circle(3, 3, 10)
cir.draw()
sqr = Square(3,3, 10)
sqr.draw()


# What will happen if this is used inside teh code? how do people know it failed because of this and how would they be able to avoid this error? they need to catch it before the product it's published. 
sh0 = Shape(4, 'qq', 4)
sh.draw()