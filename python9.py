print(list(range(2,11,2)))


#for loop

digits =[0,1,5]
for i in digits:
  print(i)
else:
  print(".....yes")

fruits=["orange","apple","mangoes"]
vegetables = ["potato","lady","tomato"]
for x in fruits:
  for y in vegetables:
    print(x,y)

#  match  case 

status_code = int(input("Enter the code: "))
match status_code:
  case 200:
    print("Success")
  case 501:
    print("internal server error")
  case 404:
    print("page not found")
  case _:
    print("Invaild status code")

# we can use ternary operator like this 
age = 20
mssg = "you can vote" if (age >=18) else "you can't vote"
# print(mssg)



#walrus operator 

print((a:=100)+1)    # this is walrus operator


data = [10,20,30,40,50]
i=0
while i<(n:=len(data)):
  print(data[i])
  i=i+1


data = [10,20,30,40,50]
while (n:=len(data)) > 0:
  print(data.pop())
  n-=1
print(data)