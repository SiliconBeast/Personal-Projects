# coffee machine code
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

def process_coins():
    print("Welcome to the Coffee Hub, Please insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.1
    total += int(input("how many nickels?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total

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

def make_coffee(drink_name, order_ingredients): #deducts the ingredients after each order
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Have a great one!!!")

machine_is_on = True
while machine_is_on:
    choice = input("What would you like to drink today? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Water: {resources['water']}ml")
        print(f"Money: ${profit}")
    elif choice != "espresso" or choice != "latte" or choice != "cappuccino":
        print("Invalid Choice. Please select again.")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])


