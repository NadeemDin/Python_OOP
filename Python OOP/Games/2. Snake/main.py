from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


# snakebody =[]
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up") # when detects up arrow key, calls method snake.up
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# #snakebody 3 squares.
# for b in range(0, 3):
#     x = int(b * -20)
#     b = Turtle("square")
#     b.penup()
#     b.color("white")
#     b.goto(x, 0)
#     snakebody.append(b)
#
#
# #moving snake, tracing previous movement.
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collsion with food?
    if snake.head.distance(food)< 15:
        print("MUNCH")
        food.munched()
        snake.grow()
        scoreboard.increase_score()



    #collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() <-300 or snake.head.ycor() > 300 or snake.head.ycor()< -300:
        scoreboard.reset()
        snake.reset()

    #collision with self.
    for segment in snake.snakebody[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()






#     #overwritingpositional data for each segment (segments follow segment infront)
#     for segment in range(len(snakebody) -1 , 0,  -1):
#         new_xpos = snakebody[segment -1].xcor()
#         new_ypos = snakebody[segment -1].ycor()
#         snakebody[segment].goto(new_xpos, new_ypos) # last segment of snake body traces position of previous seg
#
#     snakebody[0].forward(20)

#change direction.










screen.exitonclick()