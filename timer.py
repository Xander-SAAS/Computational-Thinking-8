import time
def my_function():
    count = int(input("how long do you want the timer to go? 1 = 1 millisecond: "))
    while count >= 0:
        print(count)
        count=count-1
        time.sleep(.001)
my_function()