# Function definition
def changeme(mylist):
    print('In function, before change:', mylist)
    mylist[1] = 50
    print('In function, after change:', mylist)

# Call function
mylist = [10,20,30]
changeme(mylist)
print('Outside function:',mylist)