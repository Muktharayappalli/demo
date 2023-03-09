a = {1:"mukt",2:"hued",3:"esdrt"}
print(a)
#del
del a[1]
print("after delete",a)
del a[2]
print(a)
#clear
a.clear()
print(a)

#update
a.update({"name":"mukk"})
print(a)
a.update({"name":"numm"})
print(a)

del a
print(a)
