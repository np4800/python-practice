import random

banker_names = input("Enter the names of bankers in comma separated way e.g Angela, Ben, Carrie? ")
banker_list = banker_names.split(",")
total_count = len(banker_list)

rand_gen = random.randint(0,total_count-1)
print(f"The bill will be paid by : {banker_list[rand_gen]}")

