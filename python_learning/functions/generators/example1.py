def generator(num:int):
    for i in range(num):
        yield i

for num in generator(5):
    print(num)