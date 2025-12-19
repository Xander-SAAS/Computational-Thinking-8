summer_points=0
winter_points=0
spring_points=0
fall_points=0

answer = input("what do you like most, A sunny weather, B rainy weather, or C snowy weather? :")
if answer == "A" or answer == "a":
    summer_points+=1
    spring_points+=1
    winter_points-=1
elif answer == "b" or answer == "B":
    fall_points+=1
elif answer == "B" or answer == "b":
    winter_points+=2
else:
    print("restart the quiz and give a real answer")
answer2=input("do you enjoy most A skiing/snowboarding, B swimming outdoors or C swimming i? :")
if answer2 == "A" or answer2 == "a":
    winter_points+=3
elif answer2=="B" or answer2=="b":
    summer_points+=2
elif answer2=="C" or answer2=="c":
    fall_points+=1
    spring_points+=1
    winter_points+=1
else:
    print("restart the quiz and give a real answer")
answer3=input("are you allergic to pollen A=yes B=no? :")
if answer3=="A" or answer3=="a":
    spring_points-=3
else:
    print("Ok")
answer4=input("are you afraid of insects/spiders A=yes B=no? :")
if answer4=="A" or answer4=="a":
    spring_points-=2
    summer_points-=2
    fall_points-=2
else:
    print("Ok")
answer5=input("what do you like the most A, ice cream or B, hot chocolate? :")
if answer5=="A" or answer5=="a":
    summer_points+=1
    spring_points+=1
    fall_points+=1
elif answer5=="B" or answer5=="b":
    winter_points+=2
if spring_points>summer_points and spring_points>winter_points and spring_points>fall_points:
    print("you are a spring person! yay")
elif winter_points>spring_points and winter_points>summer_points and winter_points> fall_points:
    print("you are a winter person, and I agree with you")
elif fall_points>winter_points and fall_points> summer_points and fall_points>spring_points:
    print("you are a fall person, I don't think you exist and I bet no one will see this ending")
elif summer_points>spring_points and summer_points>winter_points and summer_points>fall_points:
    print("you are a summer person, cool")
else:
    print("you are in the middle, which is basically just fall \__(OO)__/")