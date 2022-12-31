from turtle import Turtle

START_POS = [ (0, 0), (-20, 0), (-40, 0)] # for three body segmetns at start
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakebody =[]
        self.create_snake()
        self.head =self.snakebody[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self,position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.snakebody.append(new_seg)

    def grow(self):
        self.add_segment(self.snakebody[-1].position())

    def reset(self):
        for seg in self.snakebody:
            seg.goto(1800,1800)
        self.snakebody.clear()
        self.create_snake()
        self.head = self.snakebody[0]






        # for position in START_POS:
        #

    # moving snake, tracing previous movement.
    def move(self):
        # overwritingpositional data for each segment (segments follow segment infront)
        for segment in range((len(self.snakebody)-1), 0, -1):
            new_xpos = self.snakebody[segment - 1].xcor()
            new_ypos = self.snakebody[segment - 1].ycor()
            self.snakebody[segment].goto(new_xpos, new_ypos)  # last segment of snake body traces position of previous seg
        self.head.forward(MOVE_DISTANCE)

    # change direction.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



