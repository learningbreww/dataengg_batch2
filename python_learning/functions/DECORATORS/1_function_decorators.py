def dec_func(func):
    def wrapper():
        print("before calling the function")
        func()
        print("after calling the function")
    #return func
    return wrapper

@dec_func
def greet():
    print("inside greet")

if __name__ == '__main__':
    print("start main method")
    greet()
    print("end  main method")


