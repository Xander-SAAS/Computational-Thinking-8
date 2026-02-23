import turtle, math, time, random
from utils import *
#the goal of the game is to get bellow the white line, you move left with A down with S and right with D
# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
sprite_list = []
s1 = create_sprite("blue copy", 0,275)
s2 = create_sprite("big_red", 0, -300)
s4 = create_sprite("line", 0, -240)
set_background("void")

x=s1.xcor()
y=s1.ycor()
# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control
def move_down():
    x=s1.xcor()
    y=s1.ycor()-25
    s1.goto(x,y)
def move_left():
    x=s1.xcor()-25
    y=s1.ycor()
    s1.goto(x,y)
    s2.goto(x,-275)
def move_right():
    x=s1.xcor()+25
    y=s1.ycor()
    s1.goto(x,y)
    s2.goto(x,-275)

# Section 3: Game Loop
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(move_down, "s")

window.listen()
for i in range(10000000000):

    gameover=0
    # TODO - add code for automatic actions
    for s3 in sprite_list:
        if i % 10 == 0:
            y3=s3.ycor()+25
            x3=s3.xcor()
            s3.goto(x3,y3)
    if i % 50 == 0:
        x2=s2.xcor()
        y2=s2.ycor()
        s3=create_sprite("little_red", x2,y2)
        sprite_list.append(s3)
    for s3 in sprite_list:
        if get_distance (s1, s3) < 24:
            gameover=1
    if y<=-240:
        gameover=1
    if gameover==1:
        break
    # TODO - make an if statement for ending the game
    y=s1.ycor()
    
    time.sleep(0.01)
    window.update()
    
if y<=-240: 
    print("You Win")
else:
    print("Game over")