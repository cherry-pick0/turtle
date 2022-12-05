import turtle


class UkraineFlag:
    def execute(self):
        flag = turtle.Turtle()
        turtle.screensize(600, 600)

        flag.pensize(2)

        flag.goto(0, 300)
        self.rectangle(flag, "blue")
        flag.goto(0, 150)
        self.rectangle(flag, "yellow")

        flag.getscreen().mainloop()

    @staticmethod
    def rectangle(flag, color):
        flag.begin_fill()
        flag.fillcolor(color)
        for i in range(2):
            # Width
            flag.forward(400)
            # Angle
            flag.right(90)
            # Height
            flag.forward(150)
            # Angle
            flag.right(90)
        flag.end_fill()

