def cal_lcm(x,y):
    if x<y:
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0)and(greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
num1= int(input("enter the num1:"))
num2= int(input("enter the num2:"))
print("LCM OF NUMBERS ARE",cal_lcm(num1,num2))
