class college:
    def __init__(self):
        self.name=" "
        self.location=" "
    def fun1(self):
        self.name=input("enter the name of college:")
        self.location=input("enter the location:")
    def showcollege(self):
        print("name of college",self.name)
        print("college  location",self.location)
class student(college):
    def __init__(self):
        self.sname=" "
        self.roll=" "
    def fun2(self):
        self.sname=input(("enter the name student:"))
        self.roll=input("enter the roll number:")
    def showstudent(self):
        print("name of student:",self.sname)
        print("roll number:",self.roll)
class department(college):
    def fun3(self):
        self.yoj=input("enter the year of join:")
        self.branch=input("enter the branch:")
    def showdepartment(self):
        print("year of yoj:",self.yoj)
        print("branch:",self.branch)
class lab(college):
    def __init__(self):
        self.attendance=" "
    def fun4(self):
        self.attendance=input("class attended:")
    def showlab(self):
        print("class attended:",self.attendance)


obj=student()
obj.fun1()
obj.fun2()

obj1=department()
obj1.fun3()

obj2=lab()
obj2.fun4()

obj.showstudent()
obj.showcollege()
obj1.showdepartment()
obj2.showlab()

