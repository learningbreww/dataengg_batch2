# creation of tuples

#empty tuple

tup1=()
print(type(tup1))

#tuples with string

tup2=('sridhar','savitha')
print(tup2)

# creating tuple with list
lis=[1,3,5,7,9]

tup3=(lis)
print(tup3)

#with tuple func
lis1=[2,4,6,8,0]
tup4=tuple(lis1)
print(tup4)

#tuples with diff datypes
tup5=(1,1.1,'sridhar','1.223',lis1)
print(tup5)

tup6=(1)
print(tup6)