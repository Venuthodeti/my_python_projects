import random
import game_guessing_game

guessed_number= random.randint(1, 100)
print("welcome to the number guessing game!")
print("guess a number between 1 and 100")

def hard_easy(guessed_number,attemps):
    for attemp in range(attemps):

        print(f"you have {attemps-attemp} chances left")
        guess=int(input("make a guess: "))
        if attemps - attemp - 1 == 0:
            print("You lose!")
            break

        if guess == guessed_number:
            print("you win")
            break
        elif guess < guessed_number:
            print("Too low")
        elif guess > guessed_number:
            print("Too high")

        print("guess again")








level=input("Which level do you want?(easy, hard): ")
if level == "easy":
    attemps=10
    hard_easy(guessed_number,attemps)
elif level == "hard":
    attemps=5
    hard_easy(guessed_number,attemps)