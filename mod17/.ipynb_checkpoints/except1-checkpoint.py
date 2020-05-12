# exception
try:
    n1,n2 = eval(input('Input two integers(n1,n2): '))
    r = n1/n2
    print('r =', r)    
except SyntaxError:
    print('Error: Please separate input data by comma!')
except ZeroDivisionError:
    print('Error: Devided by zero!')
except:
    print('Error: Input error!')
else:
    print('kk')
finally:
    print('finally')