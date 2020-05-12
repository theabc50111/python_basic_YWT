# Function definition
def printme(pstr):
    """This function print a string"""
    print(pstr)

def sum_nums(n1, n2):
    """This function return sum of two numbers"""
    return n1+n2
    
# Call function
printme('Hello Python')
printme('Python Programming')

total = sum_nums(35,20)
print('Total :',total)

print('Total :',sum_nums(40,50))
