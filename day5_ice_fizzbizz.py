for num in range(1,101):
  if len(str(num)) == 1:
    if num%3 == 0:
      print("Fizz")
    elif num%5 == 0:
      print("Buzz")
    else:
      print(num)
  total = 0  
  if len(str(num)) > 1:
    if num%15 == 0:
      print("FizzBuzz")
    else:
      num_string = str(num)
      len_string = len(num_string)
      for digit in range(0,len_string):
        total += int(num_string[digit])
      if total%3 == 0:
        print("Fizz")
      elif num%5 == 0:
        print("Buzz")
      else:
        print(num)

        
