# Function definition 
def printinfo(name, age=35):
    print('Name:', name)
    print('Age', age)

# MAIN
# Call function
printinfo(age=50, name='Calvin')   # age is 50
printinfo(name='Calvin')   # age is 35
