# guess the output
x= ['a','b','c','d']
for x[-1] in x:
  print(x[-1],end="")


#  Set in Python ->>
 # It is unordered collection of items of different types enclosed in curely braces 
 # order maintain nhi rahta hai 


 # two ways of creating set -
 # 1 . bY using curly braces 
 # 2. by using set function -
 # syntax ----   setname = set(iterable)
s = {1,2,2+4j}
print(type(s))


sa = set(['hello',101,10.4])
print(sa)
print(type(sa))


# Rules 1. No duplicates are allowed 
#       2. Elements are not in particular order 
#       3. indexing and slicing are not applied in set
#       4. Set is mutable 
#       5. Elements in set must be  immutable 

# add()  method  -----   add one element in the set     syntax -- set_name.add(item)
# update() method  -----   add multiple method in the set    syntax -- set_name.update([items1,items2])
# remove() method  -----   remove one element                syntax  -- set_name.remove(item)
# discard() method  ----   remove one element                syntax  -- set_name.discard(item)
# # pop()  method     -----   remove any element randomly    syntax  -- set_name.pop()
# clear()  method  -----   remove all elements from set      syntax  -- set_name.clear()


# union of sets 

# 1. by using union operator --   syntax --- set1|set2
# 2. by using union function --   syntax --- set1.union(set2)


# intersection in sets

# 1.by using intersection operator (&)   ----  syntax --- set1 & set2
# 2.by using intersection function       ----  syntax --- set1.intersection(set2)



# Difference of two sets 
# A={2,4,5,6}
# B={4,6,7,8}
# A-B : {2,5}
# B-A : {7,8}


# symmetric difference 

# A={2,4,5,6}
# B={4,6,7,8}
#  A^B
#  {2,5,7,8}
#  way - 2  ->> A.symmetric_difference(B)

# super set 
# sub set 


#  Frozen set --- immutable version of python set 
# while elements of set can be modified at any time elements of frozen set remain same after creation 
#  Syntax --- frozenset(iterable)

# frozenset --- unchangeable
vowels = {'a','e','i','o','u'}
fset = frozenset(vowels)
print(type(fset))

# frozenset ka use tab karna hai jab set ki saari property chahiye but elements ko change nhi karna 
#   union intersection perform kar skte hai frozen set mein


# concatanation allowed nhi hota set mein







