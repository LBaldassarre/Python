from replit import clear
from art import logo
import random as r

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
    print(logo)
        
    #Setting game_result variable
    game_result = ""
    
    # Dealing cards to player
    player_cards = [cards[r.randint(0, 12)], cards[r.randint(0, 12)]]
    
    # Dealing cards to pc
    pc_cards = [cards[r.randint(0, 12)], cards[r.randint(0, 12)]]
    
    # Declaring continue dealing variable
    get_another_card = "y"
    
    # Checking for BlackJack
    player_score = sum(player_cards)
    pc_score = sum(pc_cards)
    if (player_score == 21):
        get_another_card = "n"
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("You got BlackJack. Congratulations You Won!")
    elif (pc_score == 21):
        get_another_card = "n"
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("Your opponent got BlackJack. You Lost")
    
        
    while(get_another_card == "y"):
        # Updating Scores
        player_score = sum(player_cards)
        pc_score = sum(pc_cards)
        
        if (11 in player_cards and player_score > 21):
            player_cards.remove(11)
            player_cards.append(1)
            player_score = sum(player_cards)
            
        if (11 in pc_cards and player_score > 21):
            pc_cards.remove(11)
            pc_cards.append(1)
            pc_score = sum(pc_cards)
        
        # Printing values in console
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {pc_cards[0]}")
        
        # Dealing option
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        # Making sure that this answer is either "y" or "n"
        while (get_another_card not in ["y", "n"]):
            print("Ups, that is not an available option, try again...")
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        # Appending Player card in case of a positive answer on the previous input
        if get_another_card == "y":
            player_cards.append(cards[r.randint(0, 12)])
        
        # Updating Scores
        if (11 in player_cards and sum(player_cards) > 21):
            player_cards.remove(11)
            player_cards.append(1)
            
            
        if (11 in pc_cards and sum(pc_cards) > 21):
            pc_cards.remove(11)
            pc_cards.append(1)
            
        player_score = sum(player_cards)
        pc_score = sum(pc_cards)
        
        # Cases were the game would be stop
        if (player_score == 21):
            get_another_card = "n"
        elif (player_score > 21):
            get_another_card = "n"
    
    # Updating game result and validating if another draw from the dealer is needed
    while (pc_score < 17):
        pc_cards.append(r.randint(0,12))
        pc_score = sum(pc_cards)
        
    player_score = sum(player_cards)
    
    # Possible game results depending on the scores
    if ((player_score == pc_score)):
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("It's a Draw")
    elif (player_score == 21):
        get_another_card = "n"
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("You got BlackJack. Congratulations You Won!")
    elif (player_score > 21):
        get_another_card = "n"
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("Sorry, You Lost")
    elif (pc_score > 21):
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("The House Busted. Congratulations You Won!")
    elif (player_score > pc_score and player_score < 21):
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("Congratulations You Won!")
    elif (pc_score == 21):
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("Your opponent got BlackJack. You Lost")
    elif (pc_score > player_score and pc_score < 21):
        print(f"Your cards: {player_cards}, your score: {player_score}")
        print(f"Your opponent cards: {pc_cards}, opponent score: {pc_score}")
        print("Sorry, You Lost")

continue_playing = "y"
while(continue_playing == "y"):
    
    continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    clear()
    
    if continue_playing == "y":
        play_game()
    
    while (continue_playing not in ["y", "n"]):
        print("Ups, that is not an available option, try again...")
        continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()