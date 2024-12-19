from menu import menu
from functions import print_resources, sufficient_resources, ask_money, sufficient_money


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


machine_is_on = True
while(machine_is_on):
    
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if (order == "off"):
        machine_is_on = False
    elif (order == "resources"):
        print_resources(resources, profit)
    elif (order not in ["espresso", "latte", "cappuccino"]):
        print("That's not a valid option, please try again.")
    else:
        
        if (sufficient_resources(resources, order)):
            amount_paid = ask_money()
            
            if (sufficient_money(order, amount_paid)):
                
                if (amount_paid > menu[order]["cost"]):
                    
                    change = amount_paid - menu[order]["cost"]
                    print(f"Here is ${change} dollars in change.")
                
                profit += menu[order]["cost"]
                
                for ingredient in menu[order]["ingredients"]:
                    resources[ingredient] -= menu[order]["ingredients"][ingredient]
                
                print(f"Here is your {order}. Enjoy!")