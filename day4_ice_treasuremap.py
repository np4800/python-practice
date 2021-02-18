row1,row2,row3 = ["O","O","O"],["O","O","O"],["O","O","O"]
matrix=[row1,row2,row3]

tresure_place=input("Where do you want to put the treasure? ")
print(tresure_place[0])
print(tresure_place[1])

column=int(tresure_place[0])
row=int(tresure_place[1])

matrix[column-1][row-1]="X"
print(f"{row1}\n{row2}\n{row3}")
