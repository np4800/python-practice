import random
print("Welcome to Py Password Generator")
letters = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*','(',')']
numbers = ['0','1','2','3','4','5','6','7','8','9']

nr_letters = int(input("Enter the number of characters you want: "))
nr_symbols = int(input("Enter the number of special character you want: "))
nr_numbers = int(input("Enter the number of numbers you want: "))


passwd_list = []
for l in range(0,nr_letters):
   passwd_list.append(random.choice(letters))

for s in range(0,nr_symbols):
  passwd_list += random.choice(symbols)

for n in range(0,nr_numbers):
  passwd_list += random.choice(numbers) 

print(passwd_list)
random.shuffle(passwd_list)
print(passwd_list)

passwd_str=''
for char in passwd_list:
  passwd_str += char

print(passwd_str)
