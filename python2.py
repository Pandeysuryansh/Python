a = 100
print(id(a))

b = 100
print(id(b))    # id prints the memmory address

c=a
print(id(c))   


d =20
print(id(d))

d=30
print(id(d))

# reassigning the value->
age=20

age="two"
print(age)

#create multiple variables in one line
name,salary,age = "Suryansh",220000,22
print(age),print(salary),print(name)

#assign single value to mutiple variables->
num = age = value = 23

#How to delete variable name->
a = 12
print(a)

# del a
# print(a)

# How to get list keywords->
import keyword
print("Keywords are:",keyword.kwlist)
