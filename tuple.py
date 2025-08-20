# What is tuple-->
#  Immutable hote hai tuple
data = (2,1,3,4,"shantanu",[1,2,3])


# another way to create tuple

tuple_data = 2,1,3,4,"shantanu",[1,2,3]
print(tuple_data)


# creating tuple of length one ->>
tup = ("hemani",)
print(type(tup))


# characterstics 

# tuple is heterogenous consits items of different types 
# we can have nested tuple
# we can pack and unpack tuples 

data1 = (21,"Shantanu",80,5.9)  # pack
age,name,weight,height = data1   # unpack
print(name)     

# operations on tuple 

# concetation of tuple same as list 
# Repetation of tuple same as list 
# Deletion of tuple --- entire tuple ko delete kar sakte hai bs
# membership in tuple  same as list 
# iterating in tuple 
# length of tuple


# Accessing items of tuple ---->
# ---------------------------

#  1.Indexing 
#  2. Slicing 


# Important methods of tuple 
#  1. index(item,[start],[end])
#     -- search for certain item in a tuple 
#     -- returns index of first match 

#  2.  count()
#  to count number of occurences 


#  min()
# max()
# sum()  -- string values ka sum nhi kar skte 


data3 = [2,12,10,3,234,231,22,222,342,23,21,22]
print(min(data3))
print(max(data3))
print(sum(data3))

# all() - if all the values are true than it returns true 
# any() -- if there is any atleast one true value than it will give true 
# sorted() -- returns new sorted list conataing all elements from the tuple  ,, sorted hamesa list return karta hai chahe isse kissi mein bhi apply karo


tuple2 = (1,0,True)
print(all(tuple2))
print(any(tuple2))


tuple3 = (0,3,2,1,11,0,-9,-4,-12)
print(sorted(tuple3))

# Note --- agr tuple ke andar koi list hai toh hum usko change kar skte hai [][] isse access kar lenge phir change kar denge
