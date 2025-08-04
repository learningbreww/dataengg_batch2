class Maths_operation:
    @staticmethod
    def add(x,y):
        res=x+y
        return res

if __name__ == '__main__':
    #WITHOUT DECORATOR
    '''mathsop=Maths_operation()
    res1=mathsop.add(10,10)
    print(res1)'''

    #WITH DECORATOR
    res2=Maths_operation.add(x=10,y=20)
    print(res2)
