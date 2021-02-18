#!/usr/local/bin

name1 = input("Enter your Name: ")
name2 = input("Enter name of your love: ")

print(f"{name1.lower()} {name2.lower()}")
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = str(true) + str(love)

if int(love_score) > 90 or int(love_score) < 10:
  print(f'Your score is {love_score}, and you go like coke and methos')
elif int(love_score) > 40 and int(love_score) < 50:
  print(f'Your scroe is {love_score}, you go togather very well')
else:
  print(f'Your score is {love_score}')

