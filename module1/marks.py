phy = int(input("mark phy"))
eng = int(input("mark eng"))
maths = int(input("mark maths"))
chem = int(input("mark chem"))
ss = int(input("mark ss"))

total = phy+chem+maths+chem+ss
print("total mark",total)
prect = (total/500)*100
print("pernt = ",prect)

if prect>=90:
    print("a grade")
elif prect>=80:
    print("b grade")
elif prect>=70:
    print("c grade")
else:
    print("failed")
