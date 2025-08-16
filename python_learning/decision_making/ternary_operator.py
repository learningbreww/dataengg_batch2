grade=70

graderes="A grade" if grade >90 else  "B grade" if grade > 60 else  "C grade" if grade >50 else "just pass"
print(graderes)

print()


#even and odd numbers
a=10

if a%2==0:
    print("a is even")
else:
    print("a is odd")

print()

#equivalent:
a=15
res="a is even" if a%2==0 else "a is odd"
print(res)