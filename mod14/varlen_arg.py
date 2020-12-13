# Function definition
# 在參數前面加上一個*，就可以接收複數個引數，且數量可以不固定
def printinfo(arg1, *vartuple):
    print('Output is: ')
    print('first:',arg1)
    print('the rest of args :', vartuple)
    for var in vartuple:
        print(var)
    print()
    
# MAIN
# Call function
printinfo(10)
printinfo(70, 60, 50) # 70 is a position argumnet, 60、50 is arbitrary arguments 
