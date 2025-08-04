def countUpto(num1):
    count=1
    # for i in range(num1):
    #     yield i
    #     count +=1
    while count <=num1:
        yield count
        count +=1

for num in countUpto(10):
    print(num)