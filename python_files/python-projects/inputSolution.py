# Use input() to read a line of input from the command line
num = input()
print("you entered",num)
num = input("Enter a number ")
print("you entered ",num)

# input() reads in a string and a new line
# in the example above, num will hold a string and new line.
# convert it to an integer or float if you want a number
num = int(input("Enter a number"))
num = num + 1
print("num is ",num)

# Read in a file
# use the keyword with to handle connecting to the file system
# The example reads in the file movies.txt and stores it in the variable file
# Use a for loop to iterate through the file line by line
# use strip() to strip off the new line that's read
with open('movies.txt') as file:
    for line in file:
        print(line.strip())

# This example reads in heights.txt 
# It strips the new line off of each line
# The split() function separates each space separated word into an item in an array
# values will hold ['firstname','lastname',height]
# It then concatenates the first and last name and uses the full name as the key 
# into the dictionary height and stores the height as the value.
heights={}
with open('heights.txt') as file:
    for line in file:
        line=line.strip()
        print(line)
        values=line.split()
        print(values)
        heights[values[0]+" "+values[1]]=values[2]
print(heights)






