#multilevel inheritance
class vehicle:
    def fun1(self):
        print("vehicle class")
class car(vehicle):
    def fun2(self):
        print("car class")
class sportcar(car):
    def fun3(self):
        print("sportcar")

obj=sportcar()
obj.fun1()
obj.fun2()
obj.fun3()