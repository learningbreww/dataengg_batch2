items=['mobile', 'tablet', 'laptop']
quantity=[20, 10,30]
#print each items wotj quantity
print(list(zip(items, quantity)))

print()
for product, quantity in zip(items, quantity):
    print(f"the product {product} is having quantity of")