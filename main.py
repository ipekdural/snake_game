import time
from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import Score
from highest_score import HighestScore

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)
def game():
    snake=Snake()
    food=Food()
    scoreboard = Score()
    pen=Turtle()

    highest_s = HighestScore()
    highest_s.hideturtle()


    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    game_is_on=True

    pen.hideturtle()
    pen.penup()
    pen.color("RED")
    while game_is_on:
        highest_s.append(scoreboard.score)
        highest_s.write_()
        screen.update()
        sleep(0.1)
        snake.move()
        #food and snake collision detection
        if snake.head.distance(food)<17:
            food.relocate()
            snake.extend()
            scoreboard.increase_score()
        #snake and wall collision detection
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.game_is_over()
            new=max(int(highest_s.highest),int(scoreboard.score))
            with open("data.txt", mode="w") as file:
                file.write(f"{new}")
            game_is_on=False
            time.sleep(0.5)



        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<12:
                scoreboard.game_is_over()
                new = max(int(highest_s.highest), int(scoreboard.score))
                with open("data.txt", mode="w") as file:
                    file.write(f"{new}")
                time.sleep(0.5)
                game_is_on = False



    screen.onkey(restart_game, "r")

def restart_game():
    sleep(1)

    screen.reset()
    game()

game()
screen.exitonclick()


