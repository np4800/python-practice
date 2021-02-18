input_score = input("Enter the scores of student: ")

list_score = input_score.split()

max = int(list_score[0])
for s in list_score:
  if int(s) > max:
    max = int(s)

print(f"The highest score in the class is: {max}")
