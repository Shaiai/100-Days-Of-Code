from turtle import Turtle

#Constants to simplify code
STARTING_POSITIONS = [(0,0),(-20,0), (-40,0)]
MOVE_DISTANCE = 20
#Directions represented as degrees for later use
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
    
    #Function that creates new instances of a square turtle to add to the legnth of the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #Function that moves the head of the snake and tells each subsequent segment to follow its footsteps.
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    #Adds a new segment to the snake.
    def extend(self):
        self.add_segment(self.tail.position())
    
    #Functions to handle turning the head of the snake
    def up(self):
        #If the head is already going down, we can not go up. 
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

