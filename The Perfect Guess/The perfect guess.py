import random
a = random.randint(1, 100)
b = 0

while(b != a):
    b = int(input("Enter a number: "))

    if(b > a):
        print("Too high! Try again and guess lower.")

    else:
        print("Too low! Try again and guess higher.")

print("Congratulations! You've guessed the correct number:", a)