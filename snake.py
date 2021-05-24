import turtle
import time
import random
score = 0 

#creating the screen
screen = turtle.Screen()
screen.title("Snake by CodePlateau")
screen.bgcolor("green")
screen.setup(width=600, height=600) 

#creating the snake's head
head = turtle.Turtle()
head.penup()
head.speed(0)
head.shape("square")
head.color("red")
head.goto(0,0)
head.direction = "stop"  #Default Direction to make head Static

# Creating the Food
food = turtle.Turtle()
food.penup()
food.speed(0)
food.shape("square")
food.color("black")
food.goto(100,100)
food.direction = "stop"

#game functions
def go_up():
    head.direction = "up"
def go_down ():
    head.direction = "down"
def go_right ():
         head.direction = "right"
def go_left ():
         head.direction = "left"
def pause():
         head.direction = "stop"
def reset ():
    head.direction = "dawo"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    elif head.direction == "stop":
        head.direction = "stop"
    elif head.direction == "dawo":
        head.goto (0,0)

#Keyboard Setup
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
screen.onkey(pause, "a")
screen.onkey(reset, "b")

#the main game loop

while True:
    screen.update()
    if head.distance(food) < 20:
       x = random.randint(-280, 280)
       y = random.randint(-280, 280)
       food.goto (x,y)

    # Snake New Body
    new_segment = turtle.Turtle ()
    new_segment = penup ()
    new_segment = shape ("square")
    new_segment = color ("yellow")
    new_segment = speed (0)

    snake.append (new_segment)

    #Moving the end segments first in reverse order
for x in range (len ()) [index]    

       score = score + 5
       print ("Oga I Don Wack")
    move ()
    time.sleep(0.1)


screen.mainloop()
