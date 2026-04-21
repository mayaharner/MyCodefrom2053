# MAYA HARNER
# Cite any sources you used to help with the homework including TAs and classmates: PythonBasics.pdf given

def last_4_doubled(string):
    """
    Given a string, return a new string made of 2 copies of the last 4 characters of the original string.
    The string length will be at least 4.
    """
    # Your code here
    # use print to debug
    # make sure to return solution
    last_4_letters = string[len(string)-4:] # set last 4 characters to a variable
    new_string = last_4_letters + last_4_letters # add the two copies into one string
    print(new_string) # print string to debug
    return new_string # return solution

def has_789(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    7, 8, 9 appears in the list somewhere. 7, 8, 9 must occur in order.
    """
    # Your code here
    for i in range(len(nums)-2): # go through length of list
        if (nums[i] == 7) and (nums[i+1] == 8) and (nums[i+2] == 9): # check if 789 in order
            return True
    return False # return false if 789 does not appear in the list in order

def count_x_o(string):
    """
    Return the number of times that the string "x-o" appears anywhere in the given string,
    except we'll accept any character for the '-', so "xao", "xbo", etc. count.
    """
    # Your code here
    count = 0 # create a count variable
    for i in range(len(string)-2):
        if (string[i] == 'x') and (string[i+2] == 'o'): # check if "x-o" appears
            count += 1 # increment to keep track of times the string appears
    print(count) # print out the count
    return count # return the count

def samesunmoon(string):
    """
    Return True if the string "sun" and "moon" appear the same number of times in the given string.
    *** This can be simplified using a Python string method ***
    """
    # Your code here
    count_sun = string.count("sun") # use string method to count # of times sun appears
    count_moon = string.count("moon") # count # of times moon appears
    if count_sun == count_moon: # check that numbers they appear are the same
        return True
    return False # return false if they do not appear same # of times
        

def trimmed_average(nums):
    """
    Return the "trimmed" average of a list of ints, which is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """
    # Your code here
    sum = 0 # create sum variable
    for i in nums:
        sum += i # find sum of the list
    new_sum = sum - min(nums) # create new val to ignore smallest value in list
    new_sum -= max(nums) # ignore largest value in list
    new_len = len(nums) - 2 # subtract 2 to ignore the two values now removed
    trim_average = new_sum // new_len # use floor division to find trimmed average
    return trim_average # return trimmed average

# Test functions - Do not modify these.
assert last_4_doubled("HelloThere") == 'herehere', 'last_4_doubled("HelloThere") expected ereere'
print("Test 1 for last_4_doubled passed")
assert last_4_doubled("abcdefgh") == 'efghefgh', 'last_4_doubled("abcdefgh") expected efghefgh'
print("Test 2 for last_4_doubled passed")
assert last_4_doubled("ComputerScience") == 'enceence', 'last_4_doubled("ComputerScience") expected enceence'
print("Test 3 for last_4_doubled passed")
print("-" * 20)

assert has_789([7, 7, 8, 9, 7]) is True, '[7, 7, 8, 9, 7] has 789'
print("Test 1 for has_789 passed")
assert has_789([7, 7, 8, 1, 9]) is False, '[7, 7, 8, 1, 9] does not have 789'
print("Test 2 for has_789 passed")
assert has_789([7, 7, 8, 7, 8, 9]) is True, '[7, 7, 8, 7, 8, 9] has 789'
print("Test 3 for has_789 passed")
print("-" * 20)

assert count_x_o("x-ox_ox.o") == 3, 'x-ox_ox.o has 3'
print("Test 1 for count_x_o passed")
assert count_x_o("xxox.o") == 2, 'xxox.o has 2'
print("Test 2 for count_x_o passed")
assert count_x_o("xrooo") == 1, 'xrooo has 1'
print("Test 3 for count_x_o passed")
print("-" * 20)

assert samesunmoon("sunmoon") is True, 'sunmoon has same sun/moon count'
print("Test 1 for samesunmoon passed")
assert samesunmoon("sunlightmoon") is True, 'sunlightmoon has same sun/moon count'
print("Test 2 for samesunmoon passed")
assert samesunmoon("sunmoonmoon") is False, 'sunmoonmoon does not have same sun/moon count'
print("Test 3 for samesunmoon passed")
print("-" * 20)

assert trimmed_average([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("Test 1 for trimmed_average passed")
assert trimmed_average([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("Test 2 for trimmed_average passed")
assert trimmed_average([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("Test 3 for trimmed_average passed")
print("-" * 20)
print("All tests passed! Great job!")