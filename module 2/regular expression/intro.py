import re
string1="hello my number is 99467453 my officail number is 055672345"
print("our string is:",string1)
#findall
regex='\d+'
match= re.findall(regex,string1)
print(match)

spaces= '\s'
match=re.findall(spaces,string1)
print(match)
#search
x=re.search('python',string1)
print(x)
#split
y=re.split('\s',string1)
print("after spliting:",y)

s= '\D+'     #'\D'  #'\S'  #'\w'   #'\W'
match=re.findall(s,string1)
print(match)

