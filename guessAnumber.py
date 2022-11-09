import random

number = random.randint(1, 100)

guess_chances = 0
name = input('What\'s your name?:').title()
print("Hi "+ name+", I would like you to guess the number I'm thinking: (1 to 100) ")

while guess_chances < 3:
    guess = int(input())
    guess_chances += 1
    if guess != number:
        print(f"Sorry, you have guessed {guess_chances + 0 } time{'s' if guess_chances > 1 else ''} incorrectly.")
    if guess == number:
        break
if guess == number:
    print(f"Congrats {name}, You just read my mind!")
else:
    print(f"You are out of tries, my number was {number}!")
    