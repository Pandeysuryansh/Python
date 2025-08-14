# elif
num = int(input("Enter a number: "))
if num==10:
  print("Number is 10")
elif num==20:
  print("Number is 20")
elif num==30:
  print("Number is 30")
else:
  print("num is big")


#looping 
# in python we have only two loops while loop and for loop
#while loop->
num = int(input("Enter a number: "))
i=1
while i<=10:
  print(num,"*",i,"=",num*i)
  i+=1

# while loop with else 
cnt =1
while cnt<=3:
  print("inside loop: ")
  cnt+=1
else:
  print("outside else: ")


