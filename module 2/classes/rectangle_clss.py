class rectangle:
    def __init__(self,l,b):
        self.L=l
        self.B=b
    def area(self):
        area=self.L*self.B
        print(area)
L=int(input("enter length"))
B=int(input("enter bredth"))
obj=rectangle(L,B)
obj.area()
