# startswith()  method  prefix mein string yaa tuple hoga 
mssg = "hello,welcome"
# print(mssg.startswith((',we',5,11)))

print(mssg.startswith(('hello','bye')))


# WAP to find the country mobile number
mobile=input("enter a mobile number ")
if mobile.startswith('+91'):
  print("India")
elif mobile.startswith("+1"):
  print("America")
elif mobile.startswith("+86"):
  print("China")
else:
  print("none")


# endswith() method suffix mein string yaa phir tuple hoga
mess = "hello, janhvi"
print(mess.endswith('hvi',5))


#Removing leading and trailing character from given string 
# there are 3 inbuilt methods 
#    1. lstrip()
#    2. strip()
#    3. rstrip()


# lstrip()
name = input("Enter the name : ")
print(name.lstrip())

urls = ["https://www.facebook","https://www.cricket","https://www.baseball"]
for var in urls:
  var = var.lstrip('https://www.')
  print(var)


# strip()
ur = ["https://www.facebook.com","https://www.hockey.com","https://www.baseball.com"]
for var in ur:
  var = var.strip('https://www.com')
  print(var)

# r.strip()

#  right se remove kr deta hai


#reverse string 

name = input("enter the string: ")
print("original string: ",name)

print(name[::-1])


# replace 
# replace(old_value,new_value,count)


#find()
# string.find(substring,start,end)    start default value is 0

#rfind()
# returns index of last ocuurence of substring
# Syntax  ---  string.rfind(substring,start,end)    last occurence ka index return kar dega 


# f-string is known as Literal string interpolation    ,,,,  f string ke andar function ko bhi call kar sakte hai

name = input("Enter name: ")
age = int(input("Enter the age: "))

print(f"Entered the name {name} and age {age}")


string = "Be a programmer"
str9 = string.center(25,'*')
print(str9)


# z-fill 0 de deta hai starting mein

# split()   use kaeke string ko list mein covert kar dete hai 

mg = "i,want,to,become,a,developer"
words=mg.split(",")
print(len(words))
print(words)


# join() 
# takes all items iterable and joins them in one string 
# seperator.join(iterable)
l = ['p','y','t','h','o','n']
str8 = ''.join(l)
print(str8)

# string some basic methods 
# upper()
# lower()
# swapcase()   upper case ko lower case mein covert kar deta hai aur lower case ko upper case mein covert kar deta hai
# title() pahla letter capital kar deta hai 
# capitalize()  pahla letter capital kar deta hai 

