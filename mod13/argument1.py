# Function definition
def changeme(myvar):
    print('In function, before change:', myvar)
    myvar = 50
    print('In function, after change:', myvar)
    
# main function
myvar = 20
changeme(myvar) # Call function
print('Outside function:', myvar)