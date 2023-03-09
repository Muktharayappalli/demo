#multiple inheritance in python
class person:
    def funtion1(self,name,age):
        print("person details:")
        print("name=",name)
        print("age=",age)

class company:
    def funtion2(self,cname,loc):
        print("company details:")
        print("company name=",cname)
        print("loction=",loc)

class employee(person,company):
    def funtion3(self,job,salary):
        print("employee details:")
        print("job=",job)
        print("salary=",salary)
obj=employee()
obj.funtion3("engineer",24000)
obj.funtion1("mukthar",22)
obj.funtion2("tcc","kochi")