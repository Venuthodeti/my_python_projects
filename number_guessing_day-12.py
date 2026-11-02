import random
guessed_number= random.randint(1, 100)

def hard(guessed_number):
    n=5
    for p in range(n):
        user_guessed = int(input("Guess a number between 1 and 100: "))
        if n-p-1 ==0:
            print("You lose")
            break
        if user_guessed<guessed_number:
            print("Too low")
        elif user_guessed>guessed_number:
            print("Too high")
        elif guessed_number==user_guessed:
            print("Congrats, you won!")
            break

        print(f"you have only {n-p-1} chances left")

def easy(guessed_number):
    n = 10
    for i in range(n):
        user_guessed = int(input("Guess a number between 1 and 100: "))
        if n - i - 1 == 0:
            print("You lose")
            break
        if user_guessed < guessed_number:
            print("Too low")
        elif user_guessed > guessed_number:
            print("Too high")
        elif guessed_number == user_guessed:
            print("Congrats, you won!")
            break
        print(f"you have only {n - i - 1} chances left")



level=input("Which level do you want?(easy, hard): ")
if level == "easy":
    easy(guessed_number)
elif level == "hard":
    hard(guessed_number)
