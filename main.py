from turtle import *
import time
import random

score = 0
best_score = 0

screen = Screen()
screen.bgcolor("green")
screen.title("Welcome to Snake by Cyberchain")
screen.setup(width=600, height=600)
screen.tracer(False)

head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

body_parts = []

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(50, 50)

score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.goto(0, 260)
score_sign.write("Score: 0 Best: 0", align="center", font=("arial, 20"))
score_sign.hideturtle()

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
     if head.direction != "right":
        head.direction = "left" 

def move_right():
    if head.direction != "left":
        head.direction = "right"    

screen.listen()
screen.onkeypress(move_up, "8")
screen.onkeypress(move_down, "5")
screen.onkeypress(move_right, "6")
screen.onkeypress(move_left, "4")    

while True:
    screen.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        for one_body_part in body_parts:
            one_body_part.goto(1200, 1200)
            
        body_parts.clear()

        score = 0

        score_sign.clear()
        score_sign.write(f"Score: {score} Best: {best_score}", align="center", font=("arial, 20"))
        
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x,y)

        new_body_parts = Turtle("square")
        new_body_parts.speed(0)
        new_body_parts.color("grey")
        new_body_parts.penup()
        body_parts.append(new_body_parts)

        score += 1

        if score > best_score:
            best_score = score

        score_sign.clear()
        score_sign.write(f"Score: {score} Best: {best_score}", align="center", font=("arial, 20"))

    for index in range(len(body_parts) - 1, 0, -1):
       x = body_parts[index - 1].xcor()
       y = body_parts[index - 1].ycor()
       body_parts[index].goto(x,y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
    
    move()

    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            for one_body_part in body_parts:
                one_body_part.goto(1200, 1200)

            body_parts.clear()

            score = 0

            score_sign.clear()
            score_sign.write(f"Score: {score} Best: {best_score}", align="center", font=("arial, 20"))

    time.sleep(0.1)

screen.exitonclick()
