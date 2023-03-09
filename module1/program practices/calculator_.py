def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def mul(p,q):
    return p*q
def div(p,q):
    return p/q

print("please enter choise:")
print("A.add")
print("B.sub")
print("c.mul")
print("d.div")
choice = input("enter your choice:")

num1= int(input("enter first num:"))
num2= int(input("enter second num:"))

if choice=="A":
    print(add(num1,num2))
elif choice=="B":
    print(sub(num1,num2))
elif choice=="C":
    print(mul(num1,num2))
else :
    print(div(num1,num2))