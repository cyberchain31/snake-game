# Z turtle importuj Vsetko
from turtle import *
# from turtle import Screen
import time
import random

# Score
score = 0
best_score = 0

# Pozadie/Obrazovka
screen = Screen()
screen.bgcolor("green")
screen.title("Welcome to Snake by Cyberchain")
screen.setup(width=600, height=600)
# tracer ,,ako keby sa okno prestane restartovat / Preblikavat po zvacseni hada
screen.tracer(False)

# Hlava hada
head = Turtle("square")
head.color("black")
head.speed(0)
# Pero sa z platna zodvyhne
head.penup()
head.goto(0, 0)
# "stop" - Hlavu hada na zaciatku hry stoji
head.direction = "stop"

# Casti tela
body_parts = []

# Potrava - ,,jablka,,
apple = Turtle("circle")
apple.color("red")
# Pero sa z platna zodvyhne
apple.penup()
# Deafultna hodnota jablka
apple.goto(50, 50)

# Score - Text
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.goto(0, 260)
score_sign.write("Score: 0 Best: 0", align="center", font=("arial, 20"))
# Skryt objekt
score_sign.hideturtle()

# Funkcia - pohyb hada
def move():
    if head.direction == "up":
        # Do y uloz suradnicu y jeho hlavy - ycor ulozenie suradnice/jadra
        y = head.ycor()
        # Nastav poziciu y a pridaj o 20px
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

# Funkcie na klavesy - Smer
def move_up():
    # Zmena smeru - Ak sa nerovna smer dole, pojde stale hore
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

# Stlacenie klavesy - Zavolanie funkcie
screen.listen()
screen.onkeypress(move_up, "8")
screen.onkeypress(move_down, "5")
screen.onkeypress(move_right, "6")
screen.onkeypress(move_left, "4")    

# Hlavny cyklus - Nastavenie casu a obrazovky - funkciu move() vola ju cyklus 
while True:
    # Okno sa bude stale updatovat aby vykreslovalo kocky
    screen.update()

    # Kontrola kolizia s hranov platna - logicke operatory or
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # print("bum")
        # Zastav na 2 sekundy
        time.sleep(2)
        # Vrat hlavu na zaciatok
        head.goto(0, 0)
        head.direction = "stop"

        # Skrytie casti tela
        for one_body_part in body_parts:
            one_body_part.goto(1200, 1200)

        #  Vyprazdnime list s castami tela (sede 4ceky)   
        body_parts.clear()

        # Reset score
        score = 0

        # Vymaze stare defaultne skore 0, 0
        score_sign.clear()
        score_sign.write(f"Score: {score} Best: {best_score}", align="center", font=("arial, 20"))
        
    # Kolidacia/Zjedenie jablka s hlavou - 20px a nahodne zobrazenie jablka na ploche ,,pouziva sa casto v hre,,
    if head.distance(apple) < 20:
        # print("Bum")
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x,y)

        # Pridanie casti tela za hlavu
        new_body_parts = Turtle("square")
        new_body_parts.speed(0)
        new_body_parts.color("grey")
        new_body_parts.penup()
        body_parts.append(new_body_parts)

        # Zvysenie score
        score += 1

        # Best Score
        if score > best_score:
            best_score = score

        # Vymaze stare defaultne skore 0, 0
        score_sign.clear()
        score_sign.write(f"Score: {score} Best: {best_score}", align="center", font=("arial, 20"))

    # Cyklus - Ulozenie tela za hlavu hada
    for index in range(len(body_parts) - 1, 0, -1):
       x = body_parts[index - 1].xcor()
       y = body_parts[index - 1].ycor()
       body_parts[index].goto(x,y)

    # Cyklus - Umiestenie casti tela za seba
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
    
    move()

    # Cyklus - Naraz hlavy do tela
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            # Skrytie casti tela
            for one_body_part in body_parts:
                one_body_part.goto(1200, 1200)

            #  Vyprazdnime list s castami tela (sede 4ceky)   
            body_parts.clear()

            # Reset score
            score = 0

            # Vymaze stare defaultne skore 0, 0
            score_sign.clear()
            score_sign.write(f"Score: {score} Best: {best_score}", align="center", font=("arial, 20"))

    # Pockaj 0.1s a potom sa obnov
    time.sleep(0.1)

screen.exitonclick()

# # Video 33-34-35-36-37 (pro pokrocile)