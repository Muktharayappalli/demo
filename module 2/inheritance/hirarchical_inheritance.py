class vehicle:
    def fun1(self):
        print(" VEHICLE class")
class car(vehicle):
    def fun2(self,name1):
        print("name=",name1)
class bus(vehicle):
    def fun3(self,name2):
        print("name=",name2)

obj1=car()
obj1.fun1()
obj1.fun2("BMW")

obj2=bus()
obj2.fun1()
obj2.fun3("KSRTC")
