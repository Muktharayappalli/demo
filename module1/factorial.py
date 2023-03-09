num = int(input("enter the num:"))
factorial = 1
if num<0:
    print("enter a positive number")
elif num==0:
    print("please enter a positive num")
else:
    for i in range (1, num+1):
        factorial = factorial*i
    print("factorial of",num,"is", factorial)
