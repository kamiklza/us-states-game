from turtle import Turtle

class StateName(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()

    def draw_name(self, location, state):
        self.goto(location)
        self.write(f"{state}", font=("Arial", 8, "bold"))



