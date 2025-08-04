lis =[1,2,3,4,5,6,7,8,9]

try:
    lis_iterator=iter(lis)
    print(next(lis_iterator))
    print(next(lis_iterator))
    print(next(lis_iterator))
    print(next(lis_iterator))
    print(next(lis_iterator))
    print(next(lis_iterator))
    print(next(lis_iterator))
    print(next(lis_iterator))
    print(next(lis_iterator))
    print(next(lis_iterator))
except StopIteration:
    print(f"Exception caught: {StopIteration}")



