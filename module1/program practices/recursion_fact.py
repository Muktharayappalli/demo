def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)

num = int(input("enter a number:"))

if num<0:
    print("factorail does not exist for the number")
elif num==0:
    print("factorail of o is 1")
else:
    print("the factorial",num,"is",recur_factorial(num))