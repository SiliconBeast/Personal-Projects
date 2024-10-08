# the program is a simple game which has 2 levels
# it gives us chances to guess the number and tells whether the guess is too high or too low
# i used the fact of using the def function and the simple if-else statements for this personal projects :)
import random


def number_guessed():
    print("Hi There The Player!")
    level = input("Choose a difficulty level, Select by typing either 'easy' or 'hard': ").lower()

    if level == "easy":
        attempts = 10
    elif level == "hard":
        attempts = 5
    else:
        print("Invalid choice. Defaulting to 'easy' mode.")
        attempts = 0

    number_to_guess = random.randint(1, 100)
    print(f"You have {attempts} attempts to guess the number between 1 and 100.")

    while attempts > 0:
        guess = int(input("Make A Guess: "))

        if guess < number_to_guess:
            print("You are going too low")
        elif guess > number_to_guess:
            print("You are going too high")
        elif guess == number_to_guess:
            print("You guessed the right number!!!")
            return

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining")
        else:
            print("You have run out of the attempts player :( ")
            print(f"The number was {number_guessed}")


number_guessed()        
