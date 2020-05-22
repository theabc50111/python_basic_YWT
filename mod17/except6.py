try:
    n1,n2 = eval(input('Input two integers(n1,n2): '))
    r = n1/n2
    print('r =', r)    
except (SyntaxError,ZeroDivisionError):
    print('Error: Please separate input data by comma! Or Devided by zero!')
except:
    print('Error: Input error!')
else:
    print('no error')
finally:
    print('finally')