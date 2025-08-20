# what is dictionary ?
#   dictinary is unordered collection of key value pairs 

# creating using two ways 
 # 1.  using curely braces
   #    dict_name = {key1:val1,key2:val2,key3:val3}
#  2. using dict functions
 # dict_name = dict([(key1,val1),(key2,val2),(key3,val3)])


# characterstics :
#  1. keys must be immutable items(string , tuple etc..)
#  2. values can be any datatype
#  3. duplicate of keys are not allowed 
#  4. Dictionary is mutable
#  5. keys can't be duplicated but values can be 
#  6. keys are case -sensitive 



# empty dictionary 
    # 1.
students = {}
print(type(students))

student = dict()
print(type(student))

# Accessing the item of dictionary 
#  we can not use indexing and slicing in dictionary 
    # syntax how to access - dict_name(key)

employee = {'suraj':1000,'manoj':3000,'shyaam':4500}
print(employee['shyaam'])


# how to modify dictionary 
# we can modify value by using this syntax - dict_name[key] = new_value
employee['manoj'] = 3662
print(employee)


# get() method -- returns the value of specified key 
#  syntax -- dict_name.get(key,default_value)     # default_value is none
# IF key not found then default value is printed 
print(employee.get('surya','Not found'))

# ways of removing key value 
#  1. using del keyword    --- del dict_name[key]

#  2. using clear() method  --- dict_name.clear()

#  3. using pop() method    ---  it is used to delete a key and value associated with it 
      # syntax --- dict_name.pop(key,value if not found)   default value key not found 

#  4. popitem() method --  koi bhi randomly delete kar deta hai 

 
#  update() method -->    syntax ----- dict_name.update({key1:value1})
employee.update({'jaya':5500})
print(employee)


student = {}
n=int(input("How many students to add: "))
while len(student)<n:
  roll = int(input("enter the roll number: "))
  marks = float(input(f"enter the marks of {roll}: "))
  if roll not in student:
    student[roll] = marks
  else:
    print("invalid code")

print(student)


# copying in dictionary 
# creates new copy of dictionary and returns it 
    #  syntax --- dict_name.copy()    no argument inside this

old_students = {"karan":200,"shyaam":900,"honey":190}
new_student = old_students
print(id(new_student))
print(id(old_students))




old1_student = {"lalit":200,"soni":900,"money":190}
new1_student = old1_student.copy()      # iss tarah copy karne mein memory address alg alg hote hai 
print(id(new1_student))
print(id(old1_student))


#  for loop (iterating in dictionary)

stu = {"son":200,"lod":900,"mon":190}
for item in stu:
  print(item,'---->',stu[item])


# zip function in python 
    # zip function aggregate elements from two or more iterables 
    # you can map elements from two or more containers using index 
    #  syntaxx   ------- zip(iterable1,iterable2,iterable3)
#  uses -
# 1. data aggregation and mapping 
# 2. parallel iteration
# 3. creating dictionaries 


std = ["rohan","mohan","shivam","adarsh"]
roll = {122,123,124}
marks = [98,67,78,88]

zipped_obj = zip(std,roll,marks)
for ele in zipped_obj:
  print(ele)


  # unzip 
std1 = ["rohan","mohan","shivam"]
roll1 = {110,111,112}
zi_object = zip(std1,roll1)
result = list(zi_object)


abc,xyz = zip(*result)
print(abc,xyz)

#  View objects in dictionary 
        # three  View objects we can create 
# 1. view of key-value pairs --- using items() methods 
# 2. view of keys --- using keys() method 
# 3. view of values --- using values()  method 


# 2. keys method used to fetch all the keys from the dictionary
     # syntax - dict.keys()   # there are no parameter 

fees = {"rohan":100,"aalo":200,"heena":500}
key_view = fees.keys()
print(key_view)

  # 3.  vlues method used to fetch all the values from the dictinary 
fees = {"rohan":100,"aalo":200,"heena":500}
values_list = fees.values()
print(values_list)

  # 1. key-value pairs --- using items() method
    #  dict1.items()


# setdefault() method --- returns value of specified key if key exist  if key not exist insert key with specified value 
#      syntax ---- dict1.setdefault(key,dict_default)  

studen = {"amol":202,"smol":303,"dhyaan":305}
var = studen.setdefault('smol')
print(var)



# 1. we can not use dictinary as key  
# 2. we can use dictionary as value

#m_dict = {{'one':1}:'first'} # we can not use this 
mydict1 = {'first':{'one':1}}  #  we can use dictionary as value 

# how to take dictinary as input 
studentt= {}
n = int(input("How many nubers req"))
for i in range(n):
  name = input("enter the name:")
  fee = float(input("enter the fees"))
  studentt[name]= fee
print(studentt)
