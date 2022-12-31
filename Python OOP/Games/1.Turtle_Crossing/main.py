import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player((0, -280))
screen.onkey(turtle.moveforward, "Up")

cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    if turtle.ycor() > 280:
        turtle.lvl2()
        cars.lvlspeed()
        scoreboard.point()

    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
