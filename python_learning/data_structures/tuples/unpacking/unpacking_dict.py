dict={1:"one", 2:"two", 3:"three"}
#unacking both keys and values
for key, value in dict.items():
    print(f"key: {key} and value :{value}")



print()
#unpack only keys
for key in dict.keys():
    print(key)




print()
#unpack only values
for values in dict.values():
    print(values)


print()
#unpack only keys
for keys in dict:
    print(keys)

#unpack only values