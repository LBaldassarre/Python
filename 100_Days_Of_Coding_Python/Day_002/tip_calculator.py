print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to pay? ")) / 100
num_people = int(input("How many people to split the bill? "))

total_per_person = "{:.2f}".format((total_bill * (1 + tip_percentage) ) / num_people, 2)

print(f"Each person should pay: ${total_per_person}")