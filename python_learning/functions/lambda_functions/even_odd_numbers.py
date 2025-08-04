num=[1,2,3,4,5,6,7,8,9,10]

res=list(filter(lambda x: x%2 == 0 , num))

print(f"even numbers : {res}")


res_odd=list(filter(lambda x: x%2 !=0, num))
print(f"odd numbers : {res_odd}")

res_labels=list(map(lambda x :(x,'even') if x%2==0 else (x,'odd'),num))
print(f"numbers label : {res_labels}")



