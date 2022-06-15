from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
snake_parts = []
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_parts()
        self.head = self.snake_parts[0]

    def create_parts(self):
        for coordinate in STARTING_POSITIONS:
            part = Turtle(shape='square')
            part.color('white')
            part.penup()
            part.goto(coordinate)
            self.snake_parts.append(part)

    def grow_itself(self):
        part = Turtle(shape='square')
        part.color('white')
        part.penup()
        part.goto(self.snake_parts[-1].position())
        self.snake_parts.append(part)

    def move_snake(self):
        for part_num in range(len(self.snake_parts)-1, 0, -1):
            new_x_cor = self.snake_parts[part_num - 1].xcor()
            new_y_cor = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x_cor, new_y_cor)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake_parts:
            seg.goto(1000, 1000)
        self.snake_parts.clear()
        self.__init__()

