import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 =200
x2 =-200
y2 =50
x3 =-200
y3 =-100
x4 =-200
y4 =-225


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("castle")
t1 = create_sprite("cool_dog",x1,y1)
t2 = create_sprite("gecko (2)",x2,y2)
t3 = create_sprite("dog",x3,y3)
t4 = create_sprite("alien",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
# for i in range(3):
for i in range (50):
     x1 += 1
     x2 +=1
     x3 +=1
     x4 +=10
#alien will always win becuse it goes 10x further every step.

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("cool dog wins!")
elif x2>=x1 and x2>=x3 and x2>=x4:
     print("geko wins!")
elif x3 >= x1 and x3 >=x2 and x3 >= x4:
     print ("dog wins!")
elif x4 >= x1 and x4 >= x2 and x4 >=x3:
     print ("alien wins!")
else:
     print ("a tie can't happen")


turtle.exitonclick()