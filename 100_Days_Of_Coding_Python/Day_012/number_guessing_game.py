import random as r

print("welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 a 100.")

number_to_guess = r.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()

while(difficulty not in ["easy", "hard"]):
    difficulty = input("Upss. That is not an available option, try again: ").lower()
    
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

number_guessed = 0

while (attempts > 0):
    print(f"You have {attempts} remaining to guess the number.")
    
    number_guessed = int(input("Make a guess: "))
    
    attempts -= 1
    
    if attempts == 0 and (number_guessed < number_to_guess or number_guessed > number_to_guess):
        print("You got no attempts remaining. You lost")
        print(f"The number I was thinking was: {number_to_guess}")
    elif number_guessed > number_to_guess:
        print("Too high.")
        print("Guess again.")
    elif number_guessed < number_to_guess:
        print("Too low.")
        print("Guess again.")
    else:
        print("Congratulations. You Won!")
        attempts = 0
        