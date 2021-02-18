logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

print(logo)

operation_symbol = {
 "+": add,
 "-": sub,
 "*": multiply,
 "/": divide
}

def calculate():
  should_continue = True

  num1 = float(input("What's the first number? "))
  for symbol in operation_symbol:
    print(symbol)

  while should_continue:
    operation = input(" \nPick an operation: ")
    num2 = float(input("What's the next number? " ))
    calculation_function = operation_symbol[operation]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation} {num2} = {answer}")
  
    flag = input((f"Type 'y' to continue the operation with {answer}, else 'n' to exit: "))
    if flag == 'y':
      num1 = answer
    else:
      should_continue = False
      calculate()

calculate()
