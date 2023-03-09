#highest common factor
def cal_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf
num1= int(input("enter num1:"))
num2= int(input("enter num2:"))
print("the number is:",cal_hcf(num1,num2))
