# Using global variable
total = 0   # This is global variable

# Function definition
def sum_data(arg1, arg2):
    total  = arg1 + arg2; # total is local variable
    print('In function local total :', total )

# MAIN    
# Call function
sum_data(10, 20)


print('Outside function global total :', total)
