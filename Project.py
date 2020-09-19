from graphics import *
from random import *

#Create the window and the bar.
win = GraphWin('Game', 700, 700, autoflush = False)
bar = Rectangle(Point(20, 180), Point(150, 180))
win.setBackground('lightblue')
bar.draw(win)

#Create the circle.
x = randrange(1, 700)
y = 0
circle = Circle(Point(x, y), 25)
circle.setFill('red')
circle.setOutline('black')
circle.draw(win)

for dy in range(0, 10):
        
        circle.move(0, randrange(0, 200))
        update(5)

win.getMouse()
win.close()
