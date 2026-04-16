print("Hello World!")

# COMMENTS -----------------
'''
also a comment like /* comment */
'''
# highlight a group of code than do ctrl forward slash and will automatically 
# comment it out

# DECLARATIONS -----------
# don't have to declare a variable datatype
x=100
y=5.5
x="hello"
print(x)

# OPERATORS --------
x=100+1 # operators are mainly normal

# floor division!
x=100/10
# print(x) - you get a float
# print(int(x)) changes type OR can do floor division
x=100//10
print(x) # cuts off dec points

x=100%10

min_val=min([1,2,3,4,5])
print(min_val)

x=2**4 # raise 2 to the 4th power
x=pow(2,5) # also does the same for power

# IF/CONDITIONAL STATEMENTS ---------------
# need to indent code in order for it to work!!!
if x>10:
    x=5
    y=10

# when done with statement, just bring cursur back

if x>10 and y<5: # just use word "and" instead of & and "or" instead of ||
    print("x is greater than 10")
    y=10

if x>10 or y==10:
    print("10")

# elif instead of elseif
if x<0:
    x=0
elif x>10:
    x=0
else:
    x=100

# LOOPS!!!! -------------
# for loop
for i in range(5): # loop starts at 0 and will increment until 5
    print(i) # will print 0 through 4

# lists
lst=[1,2,3,4,5]
for i in range(len(lst)): # 0 up through not including length of list
    print(i, lst[i])

for i in range (1,5,2): # starts at 1 and goes up through not including 5
    print(i) # then increments by 2

for i in range(len(lst)-1,-1,-1): # start at last index and decrement by 1 down to 0
    print(i,lst[i])

# loop below is preferred compared to above (can only start iterations at 1 w enumerate though)
for i, num in enumerate(lst):
    print(i,num)

for val in lst:
    print(val)

# while loop
while num < 10:
    print(num)
    num+=1 # can't do num++ :(

# FUNCTIONS ---------
def hello(): # def then function name
    print("Hello World!")
hello() # call function

def greeting(name = "Alice"): # with parameter (& default)
    print("Hello", name)
greeting("Bob")
greeting() # greeting() will give error if no default

# STRINGS ---------
demo = "Maya's email address is"
email = "mharne01@villanova.edu"

for c in demo:
    print(c) # print out each character
last_char = email[-1] # negative indexing
print()
print(last_char)

# slicing strings
# str[start:end], end is up to but not including, could also just do [0:4] or [:4] or [8:]
domain = email[10:24]

# comparing strings
stra = "hello"
strb = "hello"
# if stra == strb -> true