# Function for string validation 
# 1.  isalnum()   -- all character in string is alphanumeric 
# 2.  isalpha()   -- all character in string is alphabets
# 3.  isdigit()   -- all character in string is digits
# 4.  islower()   
# 5.  isupper()
# 6.  istitle()   -- if string titled    ex - Python Is Easy
# 7.  isspace()   -- if all the characters have space
# 8.  isnumeric()
# 9.  isidentifier()   -- if string is valid identifier 
# 10. isprintable() -- all the characters are printable or string is empty
        # ex- "Python is \n easy"  -- \n is not printable hence false


#  Basic table program 

while True:
  num = int(input("Enter a number: "))
  for i in range(1,11):
    print(f"{num}*{i}={num*i}")
  ans=input("Do you want to continue(y/n): ")
  ans=ans.lower()
  if ans != 'y':
    break


# Menu driven program :

while True:
  num1 = int(input("Enter a number 1: "))
  num2 = int(input("Enter a number 2: "))
  print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
  choice = int(input("choose above choice: "))
  if choice == 1:
    print("Addition is: ",num1+num2)
  elif choice ==2:
    print("Subtraction is: ",num1-num2)
  elif choice ==3:
    print("Multiplication is: ",num1*num2)
  elif choice ==4:
    print("Division is: ",num1/num2)
  else:
    print("Invalid num ")
  ans = input("Do you want to continue? (y/n): ")
  ans = ans.lower()
  if ans != "y":
    break
