from replit import clear
import random as r
import hangman_art as art
import hangman_words as words

stages = art.stages
word_list = words.word_list

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = r.choice(word_list)

# List of blank spaces with the length of the chosen_word
display = []
for i in range(len(chosen_word)):
    display.append("_")

# Print the chosen word
print(art.logo)

#Game Loop
lives = 6
end_of_game = False
while (not end_of_game):
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess_letter = input("Guess a letter: ").lower()
    clear()
    
    # Check if the guessed letter is in the chosen_word
    if guess_letter not in chosen_word:
        lives -= 1
        print(f"You guessed {guess_letter}, it's not in the word. You lose a life")
    elif guess_letter in display:
        print(f"You have already guessed {guess_letter}.")
    else:
        # Fill the display list with the guessed letter.
        for i in range(len(chosen_word)):
            if guess_letter == chosen_word[i]:
                display[i] = guess_letter

    # Print display to show results
    print(f"{' '.join(display)}")
    print(f"{stages[lives]}\n")
    # Check end_of_game
    if "_" not in display:
        end_of_game = True
        print("You Won.")
    elif lives == 0:
        end_of_game = True
        print(f"You Lost. The word was {chosen_word}")