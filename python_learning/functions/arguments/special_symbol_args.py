def add_numbers(*numbers):
    result=sum(numbers)
    #print(result)
add_numbers(10,20,30,40,50,60)

print()

def add_numbers(*numbers):
    res=0
    for num in numbers:
        res+=num
    #print(res)

add_numbers(10,20,30,40,50,50)
print()

def add_numbers(*numbers):
    print(f"numbers : {numbers}")

add_numbers(10,20,30,40,50,50)
