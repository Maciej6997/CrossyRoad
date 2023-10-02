import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

player_turtle = Player()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player_turtle.go_up, 'w')
score = Scoreboard()

game_is_on = True
i = 0

while game_is_on:
    i += 1
    time.sleep(0.1)
    screen.update()

    if i % 6 == 0:
        car_manager.add_car()
        car_manager.move_car()

    for car in car_manager.all_cars:
        if player_turtle.distance(car) < 30:
            score.game_over()
            game_is_on = False

    if player_turtle.ycor() >= player.FINISH_LINE_Y:
        player_turtle.reset_position()
        car_manager.increment += MOVE_INCREMENT
        score.take_point()

screen.exitonclick()

#tralala