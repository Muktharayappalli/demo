a = {1,2,3,4,5}
print(type(a))
print("a=",a)

b = {"mm","hh","8","ii"}
print("b=",b)
for i in b:
    print(i)

#using set method
c = set([1,2,3,4,5,"mmm","***"])
print(c)
#using add method
d = {1,2,3,"set"}
print(d)
d.add("java")
print("set:",d)

#using update mthod
e = {1,2,3,"mm","tt"}
print(e)
e.update(["frd"])
print(e)

#using del method
#remove method
aa = {1,2,3,4,5,6}
print(aa)
aa.remove(10)
print(aa)
#discard method
aa.discard(5)
print(aa)
#in discard method error not shown but in remove shown the error if try to remove a element that not in set


