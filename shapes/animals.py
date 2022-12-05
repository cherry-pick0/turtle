from turtle import *


class StaticTurtle:
    @staticmethod
    def execute():
        turtle_1 = Turtle()
        turtle_1.color('black')
        turtle_1.shape('turtle')
        turtle_1.shapesize(stretch_wid=20)
        turtle_1.getscreen().mainloop()
