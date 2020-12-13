# Function definition
def changeme(myvar):
    print('In function, before change:', myvar)
    myvar = 50
    print('In function, after change:', myvar)
    
# Call function
myvar = 20
changeme(myvar)
print('Outside function:', myvar)
