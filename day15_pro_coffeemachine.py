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

status = {
    "current_status": {
        "water": 500,
        "milk": 500,
        "coffee": 1000
    },
    "money": 0.0
}

end_process = False

# Print the report
def report(status):
    print(f"Water: {status['current_status']['water']}ml")
    print(f"Milk: {status['current_status']['milk']}ml")
    print(f"Coffee: {status['current_status']['coffee']}g")
    print(f"Money: ${status['money']}")

# Check resources sufficient?
def is_resource_available(ans,item,status):
    if item['ingredients']['water'] > status['current_status']['water']:
        print("Sorry, there is not enough water.")
        return False
    elif item['ingredients']['milk'] > status['current_status']['milk'] and ans != 'espresso':
        print("Sorry, there is not enough milk.")
        return False
    elif item['ingredients']['coffee'] > status['current_status']['coffee']:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True

# Process coins
def process_coins():
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    
    return (quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01)

# Check if the transaction is successful
def check_transaction(amount,item):
    if amount < item['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        balance = amount - item['cost']
        print(f"Here is {round(balance,2)} dollars in chage")
        return True

# Make coffee
def make_coffee(amount,ans,item,status):
    if ans == 'espresso':
        status['current_status']['water'] = status['current_status']['water'] - item['ingredients']['water']
        status['current_status']['coffee'] = status['current_status']['coffee'] - item['ingredients']['coffee']
    else:
        status['current_status']['water'] = status['current_status']['water'] - item['ingredients']['water']
        status['current_status']['coffee'] = status['current_status']['coffee'] - item['ingredients']['coffee']
        status['current_status']['milk'] = status['current_status']['milk'] - item['ingredients']['milk']

    status['money'] = item['cost']
    return status

# Prompt the user for coffee untill it is has been turned off
while not end_process:
    answer = input("What would you like (espresso/latte/capaccino)?: ")
    
    # Print report
    if answer.lower() == "report":
        report(status)
    elif answer.lower() == "off":
        end_process = True
    else:    
        if not is_resource_available(answer.lower(),MENU[answer.lower()],status):
            end_process = True
        else:
            amount = process_coins()
            if not check_transaction(amount,MENU[answer.lower()]):
                end_process = True
            else:
                status = make_coffee(amount,answer.lower(),MENU[answer.lower()],status)
                print(f"Here is your {answer}. Enjoy!")