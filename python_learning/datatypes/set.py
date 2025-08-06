a=set()
print(type(a))

b=set([10,100,3,5,65,7,4,8,2,900]) # unordered collection
print(b) #{65, 2, 3, 100, 5, 4, 7, 8, 900, 10}

c=set([1,1,20,20,50,50,25,25,35]) #no duplicates
print(c)#{1, 35, 50, 20, 25}

c.add(100) # add single element
c.update([200,'learning',"brew"]) # update multiple values
print(c) # output: {1, 35, 100, 200, 50, 20, 500, 25}

e={1,2,3,4,3}
print(e) #{1, 2, 3, 4}
print(type(e))# <class 'set'>
e.add(10)
print(e) #{1, 2, 3, 4, 10}
e.update({23,34})
print(e) #{1, 2, 3, 4, 34, 10, 23}









