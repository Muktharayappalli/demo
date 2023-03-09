row = int(input("enter the number of rows:"))
k = 2*row-2
for i in range(0,row):
    for j in range(0,k):
        print(end=" ")
    k = k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()

for i in range (row, -1, -1):
    for j in range(k,0,-1):
        print(end=" ")
    k = k+1
    for j in  range(0, i+1):
        print("*",end=" ")
    print()