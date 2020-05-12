# function: return sum of two values
def sum_data(a, b):
    return a+b
    
# function: using function as parameter    
def operate_on(x, y, func):
    return func(x, y)

# MAIN
r = operate_on(16,20,sum_data)   # call function
print('operate_on(16,20,sum_data) =',r)
          
r = operate_on(10,40,lambda a,b:a-b)   # with anonymous function
print('operate_on(10,40,Lambda_function) =', r)


