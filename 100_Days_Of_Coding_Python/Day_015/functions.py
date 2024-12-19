from menu import menu

def print_resources(resources, profit):
    
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${profit}')
    
    
def sufficient_resources(resources, order):
    
    for ingredient in menu[order]["ingredients"]:
        if (resources[ingredient] < menu[order]["ingredients"][ingredient]):
            print(f"Sorry there is not enough {ingredient}.")
            return False
    
    return True


def ask_money():
    
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    
    total = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    
    return total


def sufficient_money(order, amount_paid):
    
    order_price = menu[order]["cost"]
    
    if (amount_paid < order_price):
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    return True    