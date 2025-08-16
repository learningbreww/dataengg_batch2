#Integer caching effect
x=257
y=257
z=x
a=100
print(x is not y)
print(z is not x)
print(x is not a)



print()
value =10

if value is not None:
    print("value is not null")
else:
    print("value is null")



print()
lis=[1,2,3]
lis1=[1,2,3]

lis2=lis

print(lis is not lis2)
print(lis is not lis1)