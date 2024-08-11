import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")


def play_game():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move()

        # detect collision with car
        for car in car_manager.cars:
            if car.distance(player) < 20:
                scoreboard.game_over()
                game_is_on = False
        if player.ycor() > 280:
            scoreboard.add_level()
            time.sleep(0.5)
            player.go_to_starting_position()
            car_manager.increase_speed()


def main():
    while True:
        print("Starting a new game...")
        play_game()
        retry = screen.textinput(title="Retry?", prompt="Yes or No?")
        if retry is None or retry.lower() != "yes":
            break
        scoreboard.reset()
        player.reset()
        car_manager.reset()
        screen.listen()
        screen.onkey(player.move, "Up")

    screen.exitonclick()


if __name__ == '__main__':
    main()
