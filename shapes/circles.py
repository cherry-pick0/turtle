import turtle
# Source: https://www.geeksforgeeks.org/draw-circle-in-python-using-turtle/


class SpiralCircle:
    @staticmethod
    def execute():
        t = turtle.Turtle()

        # taking radius of initial radius
        r = 10

        # Loop for printing spiral circle
        for i in range(100):
            t.circle(r + i, 45)
