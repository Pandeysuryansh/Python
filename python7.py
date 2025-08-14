#input 

name = input("My name is ")    
print(name)    


num1 = int(input("Number 1 "))
num2 = int(input("Number 2 "))
res = num1+num2
print("Addition is",res)


# important 
print(9//2)
print(9.0//2)
print(-9//2)

# even number program

num = int(input("Number: "))
if num%2==0:
  print("Even number")
else:
  print("Not a even")


# nested if else
age = int(input("Enter the age: "))
if age<30:
  if age<18:
    print("Go to school")
  else:
    print("Go to cllg")
else:
  print("To old to go to cllg or school")