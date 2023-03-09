class vehicle:
    def funtion1(self):
        print("this is parent class")
class car(vehicle):
    def function2(self):
        print("inside child class")
obj=car()
obj.funtion1()
obj.function2()
