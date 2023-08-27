import turtle
import time
import random

delay = 0.1
score = 0
highest_score = 0
bodies = []

main_screen = turtle.Screen()
main_screen.title("SNAKE BY SHANDILYA")
main_screen.bgcolor("#585858")
main_screen.setup(width=600, height=600)

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("white")
snake_head.up()
snake_head.goto(0, 0)
snake_head.direction = "stop"

snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape("square")
snake_food.color("orange")
snake_food.up()
snake_food.goto(0, 200)

score_board = turtle.Turtle()
score_board.shape("circle")
score_board.fillcolor("yellow")
score_board.ht()
score_board.up()
score_board.goto(-280, 250)
score_board.write('Score: 0 | Highest Score: 0', font=('arial', 15, 'bold'))

def moveup():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'

def movedown():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'

def moveleft():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'

def moveright():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'

def movestop():
    snake_head.direction = 'stop'

def move():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x + 20)

main_screen.listen()
main_screen.onkey(moveup, 'Up')
main_screen.onkey(movedown, 'Down')
main_screen.onkey(moveleft, 'Left')
main_screen.onkey(moveright, 'Right')
main_screen.onkey(movestop, 'space')

while True:
    main_screen.update()

    if snake_head.xcor() > 280:
        snake_head.setx(-280)
    if snake_head.xcor() < -280:
        snake_head.setx(280)
    if snake_head.ycor() > 280:
        snake_head.sety(-280)
    if snake_head.ycor() < -280:
        snake_head.sety(280)

    if snake_head.distance(snake_food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snake_food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.shape("circle")
        body.color('white')
        body.fillcolor("white")
        body.up()
        bodies.append(body)

        score += 10
        if score > highest_score:
            highest_score = score
        score_board.clear()
        score_board.write('Score: {} | Highest Score: {}'.format(score, highest_score), font=('arial', 15, 'bold'))

    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        bodies[0].goto(x, y)

    move()

    for body in bodies:
        if body.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = 'stop'

            for body in bodies:
                body.ht()
            bodies.clear()
            score = 0
            delay = 0.1
            score_board.clear()
            score_board.write('Score: {} | Highest Score: {}'.format(score, highest_score), font=('arial', 15, 'bold'))

    time.sleep(delay)
