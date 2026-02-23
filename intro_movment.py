import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("cool_dog",0,-200)
s2 = create_sprite("dog",0,200)

# Section 2: define controls
def move_up2():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x,y)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x,y)
    
def move_left2():
    x = s2.xcor() - 10
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right2(): 
    x = s2.xcor() + 10
    y = s2.ycor() 
    s2.goto(x,y)

def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)

def draw():
    s1.pendown()

def stop_drawing():
    s1.penup()

def erase():
    s1.clear()

def purple_pen():
    s1.color("purple")

def blue_pen():
    s1.color("blue")

def reset(x,y):
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")
window.onkeypress(erase, "e")
window.onkeypress(purple_pen, "p")
window.onkeypress(blue_pen, "b")
window.onscreenclick(reset)

window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_right2, "Right")
window.onkeypress(move_left2, "Left")
# Section 3: define other controls
def hide_draw():
    s1.hideturtle()
    s1.pendown()

def show_stopdraw():
    s1.showturtle()
    s1.penup()
window.onkeypress(hide_draw, "h")
window.onkeyrelease(show_stopdraw, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()