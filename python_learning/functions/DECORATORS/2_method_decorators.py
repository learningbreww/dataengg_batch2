def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("before func call")
        res=func(self, *args, **kwargs)
        print("after func call")
        return res
    return wrapper


class MyClass:
    @method_decorator
    def age(self):
        print("my name is :")


if __name__ == "__main__":
    cls=MyClass()
    cls.age()


