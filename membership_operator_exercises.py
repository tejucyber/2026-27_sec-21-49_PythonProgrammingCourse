a=[1,2,3,4]
b='student'
c={2,4,6,6,3}
d={'name':"harshi",'age':24,'place':"tuni"}
e=(1,2,3,'cat')
result='a'in b
answer='3'in a
output='5'in c
solution='place'in d
teju='t'in e
#in operator
print("a in",b,":",result)#in operator on string
print("3 in",a,":",answer)#in operator on list
print("5 in",c,":",output)#in operator on set 
print("palce in",d,":",solution)#in operator on dictionary
print("r in",e,":",solution )#in operator in on tuple
#not in operator
result='a' not in b
answer='3'not in a
output='5'not in c
solution='place'not in d
teju='t'in e
# not in operator
print("a not in",b,":",result)#not in operator on string
print("3 not in",a,":",answer)#not in operator on list
print("5 not in",c,":",output)#not in operator on set
print("palce not in",d,":",solution)#not in operator on dictionary
print("r not in",e,":",solution )#not in operator om tuple
