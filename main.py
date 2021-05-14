from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# creating the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# creating the snake object
snake = Snake()

# initializing food object
food = Food()

# creating the scoreboard
score = Score()

# moving the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_status = True
while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # snake eats food
    if snake.head.distance(food) < 15:
        food.new_position()
        snake.grow()
        score.increase_score()

    # detecting collision with the wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.game_over()
        game_status = False

    # detect collision with body
    for body in snake.body:
        if body == snake.head:
            pass
        elif snake.head.distance(body) < 10:
            game_status = False
            score.game_over()

screen.exitonclick()
