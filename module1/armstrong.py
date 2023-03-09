#armstrong number
num = int(input("enter the num"))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum += digit**3
    temp//=10
if num==sum:
    print("number is armstrong")
else:
    print("number is not armstrong")
