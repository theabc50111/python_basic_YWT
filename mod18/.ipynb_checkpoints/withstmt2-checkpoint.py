# file read
fname='note.txt'

with open(fname, 'r') as fp:
    print('Content(no new line):')

    for line in fp:
        print(line, end='') 
