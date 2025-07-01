import random
x=random.randint(1,10)
inp=int(input("enter a random number from 1 to 10 "))
while inp!=x:
    inp=int(input("enter a random number from 1 to 10 "))
    print("try again")
print("you won")