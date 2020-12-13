# conditional expression
h = int(input('Enter hour(0-23): '))

h = h%24 if h>=24 else h

print(f'Current time = {h}')

