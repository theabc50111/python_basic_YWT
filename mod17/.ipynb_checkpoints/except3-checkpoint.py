# exception
try:
    num = eval(input('Enter a number: '))
    print('value is', num)    
except NameError as e:
    print('Error: ',e)


num = eval(input('Enter a number: '))
print('value is', num)