import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.moving_up, "Up")
screen.onkey(player.moving_down, "Down")

cars = []
game_is_on = True
carloop = 0
while game_is_on:
    if carloop % 6 == 1:
        print("yey")
        car = CarManager()
        if scoreboard.level != 1:
            car.stage_clear(scoreboard.level)
        cars.append(car)
    carloop += 1
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    for c in cars:
        c.move()
        if player.distance(c) < 15:
            game_is_on = False
    if player.xcor() == 280 or player.ycor() == 280:
        for c in cars:
            c.reset()
        cars = []
        carloop = 0
        player.stage_clear()
        scoreboard.level_up()







screen.exitonclick()
