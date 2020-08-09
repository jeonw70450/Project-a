#Check the age of user and if under or equal to 18 print "Underage"
loop = True
while loop:
  try:
    age = float(input("What is your age? "))
    if age <= 18 and age > 0:
      print("under age")
      break
    elif age <= 0:
      print("Please enter a valid number")
      continue
    else:
      print("Over age")
      break
  except ValueError:
    print("please enter a valid number")