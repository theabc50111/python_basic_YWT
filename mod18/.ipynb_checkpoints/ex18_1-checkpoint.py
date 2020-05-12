# file write
fp = open('note.txt', 'w')
fp.write('資策會\n')
fp.write('iiiedu\n')
print('Write two data to note.txt!')
fp.close()

fp = open('note.txt', 'a')
fp.write('iii.org.tw\n')
print('Append one data to note.txt!')
fp.close()
