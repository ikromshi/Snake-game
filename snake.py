from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.speed("slow")
        snake.goto(position)
        self.snakes.append(snake)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for snek in range(len(self.snakes) - 1, 0, -1):
            newX = self.snakes[snek - 1].xcor()
            newY = self.snakes[snek - 1].ycor()
            self.snakes[snek].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
