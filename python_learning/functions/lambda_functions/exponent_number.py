#syntax
#lambda arguments : expression
def expo(num:int):
    print(num**3)
print("without lambda")
expo(3)

print()

print("with lambda")
res=lambda x: x**3
print(res(3))