try:
    a=int(input("enter the number :"))
    b=int(input("enter the number :"))
    result = a/b
    print("result=", result)
#expect clause with no exception
except:
#expect zerodivisionerror:
    print("error occured")
else:
    print("successful division")
finally:
    print("blocked")

#key error,intentation,value,multivalue,zero division = bulid in