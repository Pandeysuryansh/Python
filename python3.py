def square(num):
  print(num*num)

square(5)

print(type(10))   # it is built in function


#id()->  Every Python value/object has its own unique identity number . It is called  as id

x=100

print(id(x))

# bin()-> returns binary string equivalent  to integer passed  syntax - bin(integer)
print(bin(17))

# pow() function->  syntax - pow(x,y,z)
# x: base number
# y: exponent
# z: modulus(optional)
print(pow(2,3,4))

# round() in python
# returns rounded number of specified number
# Syntax - round(number, digits)
# where number - number specified for rounding
#  digits - number of decimals to use 
# (optional argument and default is 0)

num = 3.499
print(round(num,1))

# abs()-
#used to find absolute number
#syntax - abs(value)
print(abs(-19))
print(abs(2+3j))


# buuiltin   function kon kon se hai
import builtins
# print(dir(builtins))


#isinstance()->

age = "pinky"

print(isinstance(age,str))