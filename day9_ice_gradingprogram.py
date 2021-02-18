student_score = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_score:
  if student_score[key] >= 91 and student_score[key] <= 100:
    student_grades[key] = "Outstanding"
  elif student_score[key] >= 81 and student_score[key] <= 90:
    student_grades[key] = "Exceeds Expectation"
  elif student_score[key] >= 71 and student_score[key] <= 80:
    student_grades[key] = "Acceptable"
  elif student_score[key] <= 70:
    student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)






