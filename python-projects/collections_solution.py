a = [10,20,30,40,50]

# In Python we can use methods directly on the list
# Methods similar to methods used on ArrayLists in Java can be
# used directly on a list in Python
# add and remove items to list
# append, remove(item), pop() and pop(index)
# sort, reverse

# Add 5, 6, 7
a.append(5)
a.append(6)
a.append(7)
print(a)

# Remove 50
a.remove(50)
a.pop(2)
print(a)
a.pop()
print(a)

a.reverse()
print(a)
a.sort()
print(a)

# slice lists just like strings
# remove the first element
# [start_index:end_index]
a=a[1:]
print(a)

# use .index and .count  and .copy methods
# add 20 to the list two times
a.append(20)
a.append(20)
# returns the nubmer of times 20 occurs in list a
num20 = a.count(20)
print(a)
print(num20)

# returns the index place of 20
index7 = a.index(20)
print(index7)

# this copies a reference to a
copy_lst = a
copy_lst[0] = 99
# if we modify the coipied list, we modify the original too
print(a)

# copy makes a copy
copy_lst = a.copy()
# modifying the copied list does not modify the orignal
copy_lst[-1] = 99
print(copy_lst)
print(a)

# Declare an empty list. Use a for loop to add values to it. 
# Only add values between 20 and 40

empty=[]
# for i in range(len(a)):
for val in a:
    if val >= 20 and val <= 40:
        empty.append(val)
print(empty)

# Can't access element in list without initializing it first
empty=[]
# can't do this, it will raise an error
# empty[5] = 10
# initialize empty with 10 zeros
empty = [0] * 10
empty[5] = 10
print(empty)

# This can be used with strings too
dog = 'dog'
dogs = dog * 3
print(dogs)

# Operator is most often used to initialize lists
zeros = [0] * 1000
print(zeros)

# Comprehensions
squares=[]
for i in range(1, 10):
    squares.append(i * i)
print(squares)

squares_comp=[i * i for i in range(1,10)]
print(squares_comp)

# comprehension can iterate through an existing list
# comprehensions can also use a conditional like if animale=='dog'
animals = ['dog','cat','dog','turtle']
dogs=[animal for animal in animals if animal == 'dog']
print(dogs)

squares = [val*val for val in range(1,10) if val%2 == 0] # in each iteration store up to not including 10
print(squares)

# Sets - unorder list of items
aset = {1,2,3}
print(aset)
# Sets are unordered so we can't access them with an index place
# notallowed = aset[2]

# Sets don't allow duplicates
dups = [1,2,3,1,2,3]
no_dups = set(dups)
print(no_dups)

# Dictionaries
fav_foods={'Kathleen': 'pizza', 'Steve': 'burger', 'John': 'steak', 
           'Michelle': 'pasta', 'Patrick': 'pizza'}
print(fav_foods)

# Get access to value using key
kff=fav_foods['Kathleen']
print(kff)

# Iterate through a dictionary
for key in fav_foods:
    print(key,'favorite food is',fav_foods[key])

for key,value in fav_foods.items():
    print(key,'favorite food is',value)

# check if key Bob is in dictionary
if 'Bob' in fav_foods:
    print("Bob's favorite food is",fav_foods['Bob'])
else:
    fav_foods["Bob"] = 'donuts'
