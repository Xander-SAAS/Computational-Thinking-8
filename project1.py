print("Hello, this code is designed to be a tool you use")
print("it can be used as a stopwatch to track how long you take to do things")
print("or set a timer to remind you when to do something")
print("however you use it,I hope you find it useful")
name = input("What is your name :")
import time
def my_function():
    print("Please don't make this timer go for like 1 million, there is more code after the first timer")
    count = int(input(f"Ok {name} how long do you want the timer to go? 1 = 1 millisecond: "))
    while count >= 0:
        print(count)
        count=count-1
        time.sleep(.001)
my_function()
print("If you want the time to run again, type again")
print("if you want a stopwatch type stopwatch")
print("if you type anything else, the code breaks")
print("if you want the code to reset, hover your cursor over the highlighted rectangle in the bottom left corner of the screen and click the trash bin")
def my_function2() :
    variable1=input("type input here:")
    if variable1 == "again": 
        count2=int(input("how long do you want the timer to go this time: "))
        while count2>=0:
            print(count2)
            count2=count2-1
            time.sleep(.001)
    if variable1 == "stopwatch":
        count3=0
        while count3>-1:
            print(count3)
            count3=count3+.001
            time.sleep(.001)
my_function2()

