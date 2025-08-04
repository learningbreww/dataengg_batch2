# list comprehensions
#square of numbers using list
lis=[1,2,3,4,5,6,7,8,9,10]
res=[x**2 for x in lis]
print(res) #o/p===> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#square of numbers using range
res1=[x**2 for x in range(10)]
print(res1) #o/p===>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print()

#generator expression
#square of numbers using list
g_exp=(y**2 for y in lis)
print(g_exp)
for i in g_exp:
    print(i)

'''
<generator object <genexpr> at 0x000001FD974A0110>
1
4
9
16
25
36
49
64
81
100
'''
print()


#square of numbers using range
g_exp_1=(i**2 for i in range(5))
for j in g_exp_1:
    print(j)
'''   
0
1
4
9
16
'''





















