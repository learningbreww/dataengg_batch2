states=["karnataka", "kerala",'kolkota','bombay','andra','telangana']
search_for_state='bombay'

i=0
while i<len(states):
    if search_for_state==states[i]:
        print(f"{i} :match found")
        break
    i+=1

else:
    print("match not found")

print("end of the program")