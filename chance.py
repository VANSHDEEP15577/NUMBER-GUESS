import random
print("Guess the Number")
number = random.randint(1,20)
chance = 0
print("GUESS THE NUMBER BETWEEN 1 - 20")
while chance < 6:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("CONGRATS!!!! YOU GUESS IS RIGHT")
        break
    elif guess < number:
        print("YOUR GUESSED NUMBER IS TO LOW, THE NUMBER IS HIGHER THAN", guess)
    else:
        print("YOUR GUESSED NUMBER IS TO HIGH, THE NUMBER IS LOWER THAN", guess)
    chance += 1
if not chance < 6:
    print("YOU LOSE!!! The number is", number)
