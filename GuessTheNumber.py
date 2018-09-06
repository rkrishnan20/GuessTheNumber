import random

answer = random.randint(1, 100)

guess = int(input("Welcome to Guess the Number! Guess any number between 1 and 100. See how many tries it takes to win!"))
tries = 0;

while guess != answer:
    if guess > answer:
        guess = int(input("Too high. Try again."))
    else:
        guess = int(input("Too low. Try again."))
    tries += 1

print("Congratulations! You win!")
print("Score: " + str(tries))

