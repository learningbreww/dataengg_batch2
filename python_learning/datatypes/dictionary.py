a={}
print(a)
print(type(a))

b={'one':1,'two':2, 'three':3 }
print(b)

val=b['one'] #accessing element using key
print(val)

c=b.get('three') #accessing element using get
print(c)

print()

d=dict(f_name="ramu", l_name="somu")
print(d)

e=dict()
print(e)

f=dict([(1,2),(3,2),(4,5)])
print(f)

print()

help(f.values)

print(dir())#  return varibales classes, functions defined within the scope,
print(dir(f)) # returns valid functions, object
print(dir(list)) # returns methods available in the list
