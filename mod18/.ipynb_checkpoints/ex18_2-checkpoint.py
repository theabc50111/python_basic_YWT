# file read
fp = open('note.txt', 'r')
print('Content(with new line):')

for line in fp:
    print(line)
fp.close() 


fp = open('note.txt', 'r')   
print('Content(no new line):')

for line in fp:
    print(line, end='')    
fp.close()
print()


fp = open('note.txt', 'r')   
print('Content(readline):')

while True: 
    line=fp.readline() 
    if not line:
        break
    print(line, end='')    
fp.close()