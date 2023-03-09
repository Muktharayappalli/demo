set1 = {"mukt","yass","sham"}
set2 = {"azu","ivan","mukt"}
print("set1=",set1)
print("set2=",set2)
#union
print(set1|set2) #pipe operator=|
print(set1.union(set2))

#intersection
print(set1&set2) #ambrasent operator=&
print(set1.intersection(set2))

#difference
print(set1-set2)
print(set1.difference(set2))

#symmetric difference
print(set1^set2)#rise to operator= ^
print(set1.symmetric_difference(set2))

