class employee:
    def __init__(self,name,salary,company,mobilenum):
        self.Name= name
        self.Salary= salary
        self.Company= company
        self.Mobilenum= mobilenum
    def displaydata(self):
        print(self.Name)
        print(self.Salary)
        print(self.Company)
        print(self.Mobilenum)
obj = employee("mukthar",24000,"TCS",9946743453)
obj.displaydata()
obj1=employee("ayapp",23000,"yre",334443003)
obj1.displaydata()