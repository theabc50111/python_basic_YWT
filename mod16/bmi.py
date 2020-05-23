# bmi module
def BMI(w,h):
    return w/(h/100)**2


# MAIN
print(__name__) # 直接執行bmi.py時，為'__main__'，當bmi.py是被匯入時，為'bmi'
print(__file__)

if __name__=='__main__':
    height=float(input('Height(cm): '))
    weight=float(input('Weight(kg): '))
    print('BMI is ',BMI(weight,height))

