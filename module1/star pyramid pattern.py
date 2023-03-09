row = int(input("enter the number of rows:"))
k = 2*row
for i in range(0,row):
    for j in range(0,k):
        print(end=" ")
    k = k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()