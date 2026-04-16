# LOOPS
# exercise 1
for i in range(1,20):
    if (i % 3) == 0:
        print(i)

# exercise 2
sum = 0
count = 1
while (count <= 50):
    if count%2 == 0:
        sum += count
    count += 1
print(sum)

# exercise 3
numbers = [5,8,2,15,10,3,7]
for num in numbers:
    if num > 5:
        print(num, end=" ")
print()


# FUNCTIONS
# exercise 1
def swap(list): # take the list
    tmp = list[len(list)-1] # save val of last index
    list[len(list)-1] = list[0] # replace the last index with the first index
    list[0] = tmp # replace the first index with the last index
    print(list)

lst = [0,3,8,4,5]
swap(lst,5)