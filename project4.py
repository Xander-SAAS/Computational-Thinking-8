import turtle, time, random
from utils import *
#the goal is to get money so you can get stuff to get more money

money=0
copper=0
copper_wire=0
miners=0
factories=1
stores=1
# Section 1 - setup
# TODO - set a background using set_background()
set_background("cave")

# TODO - create at least two variables and set their starting value. ex: cookies = 0




# Section 2 - controls
# TODO - define an action. ex: def my_control()
def make_wire():
    global copper, copper_wire
#this makes a copper into a copper wire
    if copper>=1:
        copper=copper-1
        copper_wire=copper_wire+1

def sell_wire():
    global copper_wire, money
#this make copper wire into money
    if copper_wire>=1:
        copper_wire=copper_wire-1
        money=money+1

def mine_copper():
#this adds 1 copper
    global copper
    copper=copper+1

def buy_factory():
    global money, factories
#this lets you buy factories
    if money>=10:
        factories=factories+1
        money=money-10

def buy_miner():
    global money, miners
#this lets you buy miners
    if money>=10:
        miners=miners+1
        money=money-10

def buy_store():
    global money, stores
#this lets you buy stores
    if money>=10:
        stores=stores+1
        money=money-10

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
#this lets you add 1 copper
window.onkeypress(mine_copper, "space")
#this lets you add a factory for $10
window.onkeypress(buy_factory, "w")
#this lets you add a miner for $10
window.onkeypress(buy_miner, "q")
#this lets you add a store for $10
window.onkeypress(buy_store, "e")

message_sprite = create_sprite ("alien", -350,200)
message_sprite.color("white")
message_sprite.hideturtle()
message_sprite2 = create_sprite ("alien", -350,0)
message_sprite2.hideturtle()
message_sprite2.color("white")
play=1
# Section 3 - game loop
window.listen()
j = 0
while play>= 0:
    j += 1
    # TODO - put any repeating actions here
    if j % 1000 == 0:
        for i in range (factories):
            if copper>=1:
                copper=copper-1
                copper_wire=copper_wire+1
    

        for i in range (miners):
            copper=copper+2
    # time.sleep(1)

        for i in range (stores):
            if copper_wire>=1:
                copper_wire=copper_wire-1
                money=money+1
    # time.sleep(1)


    
    
    message_sprite.clear()
    message_sprite.write(f"money={money} copper={copper} copper wire={copper_wire}",font=("comic_sans", 20, "normal"))
    message_sprite2.clear()
    message_sprite2.write(f"miners={miners} factories={factories} stores={stores}",font=("comic_sans", 20, "normal"))
   



    time.sleep(0.001)
    window.update()