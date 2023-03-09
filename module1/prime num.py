number = int (input("enter the num"))
if number<0:
    print("enter a pos number")
else:
    for i in range(2, number):
        if number%i == 0:
            print("nunber is not prime")
            break
    else:
        print("number is prime")