#insert operation
print()
mixed_data=[1,2,3,"sri","45"]
#insert element at 4th position
mixed_data.insert(3,"111")
print(mixed_data)
print(mixed_data[4]) #3rd index

print()

lis3=[]

#syntax insert(index_position, object or element)
lis3.insert(0,"sridhar")
print(lis3)



print()




#+ operator , concatenate list
num1=[1,2,3]
num2=[10,20,30]

print(num1)
print(num2)
res_num=num1 + num2
print(res_num)

print()






print()
#extend()
numbers=[1,2,5,7]

num=[10,20,20]
numbers.extend(num) #adding list
print(numbers)

tup=(100,200,300)
numbers.extend(tup) #adding tuple values to the list
print(numbers)



print()
#append()
numbers=[1,2,5,7]
print(numbers)

numbers.append(10)
print(numbers)
print()
numbers.append('breww')
print(numbers)
