class birds:
    def intro1(self):
        print("there are multiple birds in world")
    def flight1(self):
        print("many of these birds can fly ")
class sparrow(birds):
    def flight1(self):
        print("sparow are the fly")
class ostrich(birds):
    def flight1(self):
        print("ostriches are the birds")
obj1=birds()
obj2=sparrow()
obj3=ostrich()
obj1.intro1()
obj1.flight1()
obj2.intro1()
obj2.flight1()
obj3.intro1()
obj3.flight1()