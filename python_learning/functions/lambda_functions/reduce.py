from functools import reduce
#maximum element in a list.
nums=[5,24,25,10,11,15,18]
res=reduce(lambda x, y: x if x>y else y, nums)
#print(res)
print()
#Product of elements
product=reduce(lambda x,y: x*y, nums)
#print(product)

print()
#SUM OF ELEMENTS
tot_sum=reduce(lambda x, y : x+y, nums)
print(tot_sum)