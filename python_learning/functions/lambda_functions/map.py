#double each number in element
num=[5,10,15,20,25]

res=map(lambda x : x*2,num)
#print(list(res))

#ADD ELEMENTS FROM TWO LISTS
a=[5,10,15,20,25]
b=[5,10,15,20,25]
print()
res1=list(map(lambda x,y: x+y, a,b))
#print(res1)

#list of strings to uppercase:
names=['sri', 'sha', 'nar', 'ram']

s=[]
for i in names:
    s.append(i.upper())
print(s)

print()
res_upper=list(map(lambda x : x.upper(), names))
print(res_upper)


