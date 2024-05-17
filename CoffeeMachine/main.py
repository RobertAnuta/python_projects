MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "total": 0,
}


# Function to check if resources are sufficient
def check_resources(choice):
    for item, quantity in MENU[choice]["ingredients"].items():
        if resources.get(item, 0) < quantity:
            print(f"Sorry there is not enough {item}")
            return False
    return True


# Ask for coin and calculate the total
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# Prepare the coffee, subtract the resources and add the money
def prepare_coffee(choice):
    for item, quantity in MENU[choice]["ingredients"].items():
        resources[item] -= quantity
        money["total"] += MENU[choice]["cost"]
    print(f"Here is your {choice}. Enjoy!")


# Main function

def main():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input in MENU:
            if check_resources(user_input):
                payment = process_coins()
                if payment >= MENU[user_input]["cost"]:
                    change = payment - MENU[user_input]["cost"]
                    if change == 0:
                        print(f"Preparing your {user_input}!")
                    else:
                        print(f"Here is ${change: .2f} in change")
                        prepare_coffee(user_input)
                else:
                    print("Sorry that's not enough money. Money refunded!")
            else:
                print("Please refill machine!")
                break
        elif user_input == "report":
            print(f'Water: {resources["water"]}')
            print(f'Milk: {resources["milk"]}')
            print(f'Coffee: {resources["coffee"]}')
            print(f'Money: {money["total"]}')
        else:
            print("Invalid choice! Please choose again!")


# Run the function
if __name__ == "__main__":
    main()






