# conditional expression
h = int(input('Enter hour(0-23): '))

h = h%24 if h>=24 else h

print('Current time = {}:00'.format(h))

