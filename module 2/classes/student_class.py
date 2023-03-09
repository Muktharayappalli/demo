class student:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
    def myfunction(self):
        print("hello,my name is ",self.Name)
mm = student("mukthar",22)
print("NAME=",mm.Name)
print("AGE=",mm.Age)
mm.myfunction()