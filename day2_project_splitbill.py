#!/usr/local/bin

print("Welcome to the split bill app")
print("----------------------------")
total_bill = input("What is your total bill? $")
split_per = input("What percentage tip would you like to give? 10 12 15? ")
people = input("How many people to split the bill? ")
total_bill_after_tip = float(total_bill) * (1+(float(split_per)/100))
share=total_bill_after_tip/int(people)
print(f"Total Bill: {total_bill}, Tip: {split_per}, split-people {people}")
print(f"Each person should pay: ${round(share,2)}")
