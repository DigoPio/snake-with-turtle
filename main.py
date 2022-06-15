import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("DigoPio's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.turn_up, 'Up')
screen.onkey(snake.turn_down, 'Down')
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')




game_is_on = True
while game_is_on:
    score.write_score()
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.food_appear()
        snake.grow_itself()
        score.new_point()
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()
    with open('highscore.txt', mode='w') as file:
        file.write(f'{score.high_score}')

screen.exitonclick()

