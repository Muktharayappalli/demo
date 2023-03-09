def factors(n):
    i=1
    while (i<n+1):
        if n % i == 0:
            print(i)
        i = i+1
number = int(input("enter a num:"))
print("the factors",number,"are")
factors(number)
