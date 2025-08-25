#skip empty strings
words=["shree", "", "", "aru", "kal"]

for i in words:
    if i=="":
        continue
    print(i)

print()
#print only odd numbers
for i in range(1,20):
    if i%2==0:
        continue
    print(f"odd number is :{i}")