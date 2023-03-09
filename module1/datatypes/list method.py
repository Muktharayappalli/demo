#python datatypes - LIST
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

#using + operator
list3 = list1+list2
print("our new list:",list3)

#using append() method
list1.append(list2)
print("after appending list:",list1)

#using extend () method
list4 = ["python","java","MERNStack"]
list5 = [1,2,3]
list4.extend(list5)
print(list4)

#using insert() mathod
stud = ["sham","iavn","azu"]
print("stud:",stud)
stud.insert(0,"mukt")
print(stud)
stud.insert(2,"yas")
print(stud)