#remove operation
#clear() method
department=['IT', 'admin','L&D','Housekeeping', 'fullfillment','admin','staffing']
print(department)
department.clear()

print(department)





print()
#del keyword
department=['IT', 'admin','L&D','Housekeeping', 'fullfillment','admin','staffing']
print(department)

#remove a slice of elements
del department[2:5]
print(department)

print()
# del keyword
del department[1]
print(department)



print()


#1. remove() operation


if  'admin' in department:
    department.remove("admin")
    print(department)
else:
    print("admin is not available")

print()



#2. pop() operation
department=['IT', 'admin','L&D','Housekeeping', 'fullfillment','admin','staffing']
print(department)

print()
pop_value=department.pop(3)
print(pop_value) # pop value will returns only the poped value
print()
print(department)
print()

if len(department) !=0:
    pop_value1 = department.pop() # since no index is specified, it will pop last element
    print("printing popped value")
    print(pop_value1)
else:
    print("department doesnot contain any values")


















#3.del operation

#3.clear() operation

