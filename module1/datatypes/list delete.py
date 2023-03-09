list1 = ["python","java",1,2,3,4,5,6]
print("list1",list1)

#delete list element
#using del element
del list1[3]
print("after del:",list1)

del list1[2]
print(list1)

#using remove() method
list1.remove(4)
print("removing:",list1)

#using clear() method
list1.clear()
print("our list:",list1)


del list1