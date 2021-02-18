stu_height = input("Enter the height of students in comma seprated format: ")
list_stu_height = stu_height.split()
sum = 0
count = 0
for h in list_stu_height:
  sum = sum + int(h)
  count += 1

avg_height = sum / count

print(f"Average Height: {avg_height}")

