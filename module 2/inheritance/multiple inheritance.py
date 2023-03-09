class parent1:
    def funtion1(self):
        print("parent1 clss")
class parent2:
    def funtion2(self):
        print("parent2 clss")
class child(parent1,parent2):
    def funtion3(self):
        print("child class")

obj=child()
obj.funtion3()
obj.funtion2()
obj.funtion1()