import time
def my_function():time
count = input("how long do you want timer to go 1 = 1 millisecond: ")
while count>0:
    print(count)
    count=count-1
    time.sleep(.001)