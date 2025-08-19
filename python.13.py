# list  - store data of different types 
# how to implement array in python by using array module and by using numpy module

# list and array are not same
# concetation of list ->

l1=[1,2,"hello",[1,2,3]]
l2=[4,3,"suryansh"]
print(l1+l2)

# multiplication of list
l3=[1,2,"hello",[1,2,3]]
print(l3*3)

# iteration through list
l4=[1,2,"hello",[1,2,3]]
for item in l4:
  print(item)

#membership of list
l3=[1,2,"hello",[1,2,3]]
print("hello" in l3)

#length of list
l3=[1,2,"hello",[1,2,3]]
print(len(l3))

# maximum in list
# max(iterable,key,default)
numbers = [1,34,21,899,10,9,899.1]
print(max(numbers))
name = ["Shantanu","Aditya","Kartik","Manoj"]   
print(max(name,key=len))    #  ascii value check karke max batata hai 

# minimum in list 
# same max ki tarah use karte hai 


# maximum minimum by manual program
nums = [12,11,13,16,10,98,76,54]
max1 = nums[0]
for ele in nums:
  if ele > max1:
    max1 = ele

print("maximum value is : ",max1)
# same as minimum


# append()   -- yeh none return kar raha hai

bowlers = ["shami","jasprit","ishant"]
bowlers.append("jadeja")
print(bowlers)


# adding multiple items
bowler = []
for ele in range(3):
  naam = input("enter bowler name : ")
  bowler.append(naam)
print(bowler)

# multiple list ko append karne ke liye extend() function kaa use bhi kar skte hai
# list.extend(iterable)
lan1 = ["hindi","urdu","marathi"]
lan2 = ["sapanish","english","punjabi"]
lan1.extend(lan2)
print(lan1)

# insert in the list
# specified index pe insert kar deta hai
# list.insert(index,elment)
batsman = ["rohit","sachin","dhoni","rahul","jaddu"]
batsman.insert(0,"Virat")
print(batsman)

# remove in list 
# remove(element)
items = ["laptop","laptop","pendrive","mouse"]
items.remove("laptop")
print(items)

# pop in list
# pop method returns deleted item for future use 

cart = ["laptop","laptop","pendrive","mouse"]
removed_ele= cart.pop(1)    # default value is -1

print(cart)
print(removed_ele)

# clear in list 
# this method remove all items in the list 
# syntax - list.clear()


# delete in list 
# Delete list   ----  del listname
# delete any item ----- del listname[index]


# removing duplicate from list --
#  way 1 -- using set function

data = [2,3,2,4,2,4,5,6,7,8,6]
print("original list: ",data)
print(list(set(data)))    # set use karne se order is not preserved 

# way 2 -- using normal way (for loop)
visited_ele = []
for ele in data:
  if ele not in visited_ele:
    visited_ele.append(ele)

print(visited_ele)
print(data)

# advantage - order is preserved 
# disadvantage  - new list is created 


# way 3 -- using normal way + list comprehension (for loop)
data = [2,3,4,2,3,4,1,2,3,4,98]
print("original list: ",data)
visit_ele =[]
[visit_ele.append(ele) for ele in data if ele not in visit_ele]
print(visit_ele)


# way 4 -- using enumerate() function
data1 = [2,3,4,2,3,4,1,2,3,4,22,22,22,22,22,23,24,26,26]
print("original data: ",data1)
new_list = []
for idx,ele in enumerate(data1):
  if ele not in data1[:idx]:
    new_list.append(ele)
print(new_list)


# way 5 -- using dictionary concepts 
data2 = [2,3,4,2,3,4,1,2,3,4,22,22,22,22,22,23,24,26,26]
print("original data: ",data2)
print(list(dict.fromkeys(data2)))  #{'2':none,'3':none,'4':none,'1':none..................}