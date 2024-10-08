# coffee machine code dictionary below
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

profit = 0 #initial money is zero
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000
}

# now we will define a function that shows there are not enough ingredients
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not have enough {item}.")
            return False
    return True

# function created to process the coins inserted to calculate the total amount    
def process_coins():
    print("Welcome to the Coffee Hub, Please insert coins.")
    total = int(input("Insert quarters?: "))*0.25
    total += int(input("Insert dimes?: "))*0.1
    total += int(input("Insert nickels?: "))*0.05
    total += int(input("Insert pennies?: "))*0.01
    return total

# this function makes sure that the transaction is successful then only the drink is processed else the money is returned back.
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change. Enjoy your Drink :))")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's is not enough money. Money refunded back!")
        return False

#deducts the ingredients after each order
def make_coffee(drink_name, order_ingredients): 
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Have a great one!!!")

machine_is_on = True

while machine_is_on:
    choice = input("What would you like to drink today? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Water: {resources['water']}ml")
        print(f"Money: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid Choice. Please select again.")

