# MAYA HARNER

# function that finds a minimum value from list as an input parameter
def find_min(lst):
    min_value = min(lst) # find min
    print("Min Value:", min_value) # print out the value for debugging
    return min_value # return an integer

# function that creates an email address from a string as an input parameter
def create_email_addr(string):
    email_addr = string + '@villanova.edu' # add the email part to the string to creat email addr
    print("email address:", email_addr) # print email address created
    return email_addr

# test function 1!
find_min([5,3,6,2,7])
find_min([33,55,15,20,4,8,10])
find_min([5,3,6])

# test function 2!
create_email_addr('mharne01')
create_email_addr('mayaharner')
create_email_addr('pbc2026')