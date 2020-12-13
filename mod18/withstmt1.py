# With the "with" statement, you get better syntax and exceptions handling. 
# The with statement simplifies exception handling by encapsulating common
# preparation and cleanup tasks.

try:
    fp = open('note.txt', 'r')
    data = fp.read()
    print('Content:')
    print(data) 
except:
    print('Error: File I/O error!')
finally:
    fp.close()

with open('note.txt', 'r') as fp:
    data = fp.read()
    print('Content:')
    print(data)
