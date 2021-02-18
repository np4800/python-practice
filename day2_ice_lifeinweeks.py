#!/usr/local/bin

print("Count the number of days and weeks left till you turn 90")
age=input("Enter your current age: ")
balance_age=90-int(age)
months=balance_age * 12
weeks=balance_age * 52
days=balance_age * 365
print(f"You have {days} days, {weeks} weeks and {months} months left")

