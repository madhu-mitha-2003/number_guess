import random

guesses = 1

print("Hello!! What's your name?")
name = input()

num = random.randint(0,50)

print(name + " I am thinking of a number between 0 to 50, can you guess it!!! ")
guess = int(input())
if num == guess:
    print("You have guessed it correct!!!")

while guesses < 10:
    guesses += 1
    if guess < num:
        print("You need to guess a higher number!!!!! Try again")
        guess = int(input("Guess a number between 0 to 50: "))
    else:
        print("You need to guess a lower number!!!!! Try again")
        guess = int(input("Guess a number between 0 to 50: "))

    if guess == num:
        break


if guess == num:
    guesses = str(guesses)
    print("You have guessed the number in " + guesses + " guesses")

if guess != num:
    num = str(num)
    print("You have lost your chance the number I have guessed is ", num )
    
            

