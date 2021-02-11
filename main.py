import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Configure Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)  # Turn of animation


# Instance's
player = Player()
cars = CarManager()
scoreboard = Scoreboard()


# Screen Listeners
screen.listen()
screen.onkeypress(player.move, "Up")

# Main Loop

game_is_on = True
while game_is_on:
    screen.update()  # Refresh animation
    time.sleep(0.1)

    cars.create_car()
    cars.move()

    # Player Cross the road.
    if player.ycor() > 280:
        player.starting_position()
        scoreboard.rise_level()
        cars.new_level()

    # Collision with car
    for car in cars.cars_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
