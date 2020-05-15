# bmi module
def BMI(w,h):
    return w/(h/100)**2


# MAIN
print(__name__)
print(__file__)

if __name__=='__main__':
    height=float(input('Height(cm): '))
    weight=float(input('Weight(kg): '))
    print('BMI is ',BMI(weight,height))

