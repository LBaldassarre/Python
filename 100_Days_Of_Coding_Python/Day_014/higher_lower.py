from replit import clear
import art
from game_data import data
import random as r

# Global variables
answer_is_correct = True
score = 0

while answer_is_correct: 
    # Getting random options
    optionA = r.choice(data)
    optionB = r.choice(data)
    
    while (optionA == optionB):
        optionB = r.choice(data)
    
    # Saving what option has more followers    
    has_more_followers = ""
    if optionA["follower_count"] > optionB["follower_count"]:
        has_more_followers = "A"
    elif optionA["follower_count"] == optionB["follower_count"]:
        has_more_followers = "-1"
    else:
        has_more_followers = "B"
    
    # Printing user prompt
    print(art.logo)
    
    if score > 0:
        print(f"You are right! Current score: {score}.")
        
    print(f'Compare A: {optionA["name"]}, a {optionA["description"]}, from {optionA["country"]}')
    print(art.vs)
    print(f'Compare B: {optionB["name"]}, a {optionB["description"]}, from {optionB["country"]}')
    
    user_guess = input('Who has more followers? Type "A" or "B": ').upper()
    
    # Taking action based on the user_guess
    if has_more_followers == "-1" or user_guess == has_more_followers:
        score += 1
    else:
        answer_is_correct = False
    
    # clearing console
    clear()

# Print game over prompt
if not answer_is_correct:
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}.")