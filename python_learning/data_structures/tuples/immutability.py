#mutable objects in list
tup=(1,2,3,[10,20,30,"sri"],4,5,6,'end')
print(tup)

tup[3].append("100")

print(tup)





print()
print()
numbers=(1,2,3,54)
#delete entire tuple
del numbers
#print(numbers)



#delete element in tuple
#del numbers[1]
#print(numbers)
#tuples do not have append func


#modify tuples
numbers[4]=4
#print(numbers)