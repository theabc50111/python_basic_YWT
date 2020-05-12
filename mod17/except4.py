# exception
while True:
    try:
        lst1 = [1,2,3,4]
        idx = int(input('Enter an index: '))
        if not 0<=idx<4:
            raise IndexError('Index out of range')
        print('Value is',lst1[idx])
        break
    except IndexError as e:
        print('Index Error :', e)
