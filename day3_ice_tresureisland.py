#!/usr/local/bin

print('''
    uuu       uuu
   uuu|=====uuu |
   | |======| |'|
   | | .==. | | |
   |___|##|___|/  (PS)
''')


print("Welcome to Tresure Island")
print("Your mission is to find the tresure")
answer1=input("You are on a cross road, which way do you want to go right or left? ").lower()

if answer1 == "right":
  print ("Game Over your: Your are end of the road")
elif answer1 == "left":
  answer2 = input('You come to a lake, Do you want to wait for boat or swim? Type "wait" or "swim" ' ).lower()
  if answer2 == "swim":
    print("Oh no! Game Over!  You have become the delicious meal for Shark or Aligatoer :-\( ")
  elif answer2 == "wait":
    answer3 = input("You have arrived to the island unharmed. There are three doors, One red One yellow One green. Which color do you choose? ").lower()
    if answer3 == "yellow" or answer3 == "red":
      print("Oh no! Game Over! Better luck next time!!")
    elif answer3 == "green":
      print("Voila! You got the Uncle Screwdge! Tresure !!!")
