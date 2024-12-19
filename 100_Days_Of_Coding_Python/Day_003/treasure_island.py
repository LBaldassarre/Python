print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.\n")

option1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')

if (option1.lower() == 'right'):
    print('You fell into a trap. Game Over.')
else:
    option2 = input('You found your self in front of a river, do you "swim" or "wait" for the boat\n')
    if (option2.lower() == 'swim'):
        print('You drowned. Game Over')
    else:
        option3 = input('As you reach the coast you see a chest and three different colored keys, "red", "blue" and "yellow". Which one do you chose\n')
        if (option3.lower() != 'blue'):
            print('The chest explodes. Game Over')
        else:
            print('As you you open the chest glimmering gold light covers your face. You Won!')