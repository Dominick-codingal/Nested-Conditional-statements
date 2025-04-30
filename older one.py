print("Check your age is between 15 to 30 years or not")
x = int(input("enter your age: "))


if x > 15: 
  print("Your age is more than 15 years")
  if x > 30:
    print("And it is more than 30 as well")
  else:
    print("But it is less than 30")