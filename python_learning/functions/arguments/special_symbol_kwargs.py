def both_special_symbol(*args, **kwargs):
    print(args)
    print()
    print(kwargs)

both_special_symbol(1,2,3,4, a='sri', b='sha', c='nar')

print()







def emp_info(**data):
    print(f"type of data : {type(data)}")
    for key, value in data.items():
        print("{} is {}".format(key, value))

    print()

emp_info(first_name='sridhar', last_name='R', age=36)
print()
emp_info(first_name='sridhar', last_name='R', age=36, place='bangalore')
print()

