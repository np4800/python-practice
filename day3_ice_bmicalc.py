#!/usr/local/bin

print("PEMDASLR - the order in which the mathematical operation will take place")
h=input("Enter your height in meters: ")
w=input("Enter your weight in kgs: ")
print("Your BMI is:" )
bmi=round(float(w)/float(h)**2,2)
print(str(bmi))
if bmi <= 18.5:
  print("You are underweight")
elif bmi > 18.5 and bmi < 25:
  print ("You have normal weight")
elif bmi > 25 and bmi < 30:
  print ("Youu are overweight")
elif bmi > 30 and bmi < 35:
  print ("You are obese")
else:
  print ("You are clincally obese")

