import random

RandomInteger = random.randint(0, 100)
GuessingPrompt = None

Strikes = 0

while (GuessingPrompt != RandomInteger):
    GuessingPrompt = int(input("Guess a number between 0-100: "))
    Strikes += 1
    print("You guessed wrong! " + str(Strikes) + " strike(s).")

    if Strikes == 10:
        print("You lose!" + " The number was " + str(RandomInteger))
        break

if Strikes < 10:
    print("Congrats! You guessed correctly!")
