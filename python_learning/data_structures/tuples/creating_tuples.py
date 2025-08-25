#without parenthesis
tups=1, 2.2, 3.0, "sri"," "
print(tups)
print(type(tups))
print()


#repitition
tup_rep=("one",) * 3
print(tup_rep)
print(type(tup_rep))

print()


#mixed datatypes
mixd_tup_dict=(1, "one", 2, "three",[1,2,3], {1:"one", 2:"two"})
print(mixd_tup_dict)
print(type(mixd_tup_dict))
print()

mixd_tup1=(1, "one", 2, "three",[1,2,3], ['sri','abh','shre','aru'])
print(mixd_tup1)
print(type(mixd_tup1))

print()
mixd_tup=(1, "one", 2, "three")
print(mixd_tup)





print()
#using built in class
str_lis=["one", "true", "three"]
tup_str=tuple(str_lis)
print(tup_str)
print(type(tup_str))


print()
lis=[1,2,3,4]
tup_lis1=tuple(lis)
print(tup_lis1)
print(type(tup_lis1))


print()
# tup_lis=tuple(1,2,3,4,5)
# print(tup_lis)
# print(type(tup_lis))


print()
tup=tuple()
print(type(tup))



print()
#using strings
str_tup=("one","two","three")
lis_tup=(1,2,3,4)

print(str_tup)
print(lis_tup)
print()
print(type(str_tup))
print(type(lis_tup))


print()
#empty tuple
tup_empty=()
print(type(tup_empty))
print(tup_empty)