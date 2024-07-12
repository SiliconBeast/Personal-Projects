# coffee machine code

profit = 0 #initial money is zero
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# now we will define a function that shows there are not enough ingredients
def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry, there is not have enough {item}.")
            is_enough = False
    return True


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
    else:

