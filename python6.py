
#swap two numbers

a=10
b=20
a,b=b,a
print("a is",a)
print("b is",b)


#Contuation character(\)
print("himani " \
"das")


#Python escape sequence

print("Suryansh\nPandey")
print("Suryansh\tPandey")
print("Suryans\tPandey")
print("Suryansh\bPandey")
print("Suryansh\rPandey")
print("Suryansh\\Pandey")

print(r"Hi \n and \t whassup")    # raw string


#unicode

print("\U00000041")
print("\U00000062")
print("\U0001F167")


# ord and chr functions ->

print(ord('#'))

print(chr(35))


#importing all
#  from addition import *
#  subtract(3,5)


#how to import multiple attributes 
 # from addition import add,subtract
 # subtract(3,5)

import math as m
print(m.factorial(5)) 

# dir() function->
my_name = "himansh"
print(dir(my_name))

print("Jolly")
x=100
# print(dir(x))


import math
print(dir(math))


#Reloading the module 

# import importlib
# importlib.reload(math)

# print(help("modules"))

#impilcit coversion
x=123
y=12.3
z=x+y
print(z)

# ranking int,float,str

#explicit conversion

value = 12.5
print(value)
value1 = int(value)
print(value1)


value = '23'
print(type(value))
value1 = int(value)
print(type(value1))



#print(objects,sep="")
print("hello",21,sep="#")