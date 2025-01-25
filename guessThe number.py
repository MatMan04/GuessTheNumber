import random as rd
print("I am thinking of a number between 1 and 20")
opponent=rd.randint(1,20)
for i in range (100):
    print("take a guess")
    guess=int(input())
    if guess>opponent:
        print("your guess is too high")
    elif guess<opponent:
        print("yoir guess is too low")
    else:
        break
if guess==opponent:
    print("good job! you guessed my number in " + str(i) + " times")
else:
    print("nope. the number i was thinking of was" + str(opponent))
