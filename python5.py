#membership operator

str = "mitali"
print("tali" in str)


number = [32,2,1,2,56]
print(50 in number)



group = ["honey", "sunny", "bunny"]
name = input("Enter the name: ")

if name in group:
  print(f"{name} is present")
else:
  print("not present")

# interview 
# How membership operator works in dictionary ?
data = {1:"Shantanu", 2:"Honey"}
print("shantanu" in data)


#
lst = [1,2,3]
print(lst in lst)   # list ek dusre ke part nhi hai


# Identity operators 

a=100
b=100
c="money"

print(a is b)
print(a is c)
print(a is not c)


#interview ->
#difference between is and == operator
#identity operator hai 
#== is comparasion operator

data = [1,2,3,4]
data1 = [1,2,3,4]
print(id(data))
print(id(data1))
#memory allocation values ke liye hote hai   yeh ek mutable list tabhi id number alg alg hai
