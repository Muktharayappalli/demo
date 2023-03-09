employee = {"name":"mukth","salary":"25000","company":"luminar","place":"cochin"}
print("******employee details*****")
print("employee nmae:",employee["name"])
print("employee salary:",employee["salary"])
print("employee company:",employee["company"])
print("employee place:",employee["place"])
#new keyvalue add
employee["position"]="software engineer"
print("after updation",employee)
#keyvalue update
employee["place"] = "kakkanad"
print("after updatn:",employee["place"])

#using forloop
#printing keys from dictionary
for i in employee:
    print(i)
#printing values from dictionary
for j in employee:
    print(employee[j])
#printing both key and value from dictionary
for k in employee.items():
    print(k)



