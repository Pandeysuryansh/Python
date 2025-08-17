#  WAP to Find the complement of given number

# 1.step Find the binary of given number
# 2.step visit every bit and flip it
# 3.step convert result of flipping into decimal integer

def findthecompliment(num):
  binary = bin(num)[2:]
  complement = ''
  for bit in binary:
    if bit=='1':
      complement+='0'
    else:
      complement+='1'

  return int(complement,2)


n = int(input("enter the number : "))

print(findthecompliment(n))

print(0O15)   # octal to decimal int 
print(0x124A) #hexadicmal to decimal int


# slicing 
name = "code yug"
print(name[::])
print(name[0::3])
print(name[0:5:2])
print(name[-1:-4:-1])

l=[1,2,3,4,5,6,7,8,9]
print(l[:-4:-1])

#   STRING IS IMMUTABLE 

str1 = "Sohan"
str2 = "Babu"
str3 = str1 + " " + str2
print("FULL name is ", str3)

str4 = "Ishu"
str5 = str4 * 2
print(str5)


#iterating on a string 
naam = "Mohan"
for char in naam:
  print(char,end =" ")


print(len(str4))

# string membership batata hai ki particular string usme present hai ki nhii
na = "shantanu" 
if 'tanu' in na:
  print("present")



# calculate number of vowels in string 

str6 = input("Enter the string : ")
vowels = ['a','e','i','o','u']
cnt =0
for char in str6:
  if char in vowels:
    cnt += 1
print("no. of vowels :", cnt)


# count number of occurence of specified substring in string 
str7 = "CODECODECODE"
counter  =str7.count('CO',3,12)
print(counter)


# enumerate method()
s="honey"
print(list(enumerate(s)))


