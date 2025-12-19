# Section 1 - Your code
from utils import *
set_background("spring")
import time
def my_function():
    count = 0
    count2=0
    while count >= -1000:
        count=count+1
        count2=count2+2
        s2 = create_sprite("freg", count2, count)
        time.sleep(.01)
my_function()
s1 = create_sprite("cardinal", 100, 100)
s2 = create_sprite("cardinal", -100, 100)
s2 = create_sprite("cardinal", -100, -100)
s2 = create_sprite("cardinal", 100, -100)
s2 = create_sprite("cardinal", 100, 150)


message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Xander",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()