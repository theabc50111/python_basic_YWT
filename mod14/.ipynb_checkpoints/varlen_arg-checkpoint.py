# Function definition
def printinfo(arg1, *vartuple):
    print('Output is: ')
    print('first:',arg1)
    for var in vartuple:
        print(var)
    print()
    
# MAIN
# Call function
printinfo(10)
printinfo(70, 60, 50)
