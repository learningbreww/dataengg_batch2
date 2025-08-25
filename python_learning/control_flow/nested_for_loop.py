#Creating Combinations or Pairs
bottles=["glass",'plastic',"steel"]
litres=["500ml", "750ml","1000ml"]
combination=[]

for bottle in bottles:
    for size in litres:
        combination.append((bottle, size))

print(combination)

print()
print()
#Generating a Multiplication Table
for i in range(1,6):
    for j in range(1,6):
        res=i*j
        print(f"{res:5}",end="")
    print()

print()
