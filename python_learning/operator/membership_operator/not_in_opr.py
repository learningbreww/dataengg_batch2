dict={1:"sri", 2: "sha", 3: "ram"}

if 3 not in dict:
    print("3 is not available")
else:
    print("3 is present")

print()


print()
message="my python program"

if 'my' not in message:
    print("substring not available")
else:
    print("substring presemt")


print()

number=[1,2,3,4,5,6,7,8,9]

if 3.5 not in number:
    print("number doesnot exists")
else:
    print("number exists")


print()






#Validating a User's Input
reserved_usernames = ['admin', 'root', 'support']
#new_user_name='learning_brew'
new_user_name='support'

if new_user_name not in reserved_usernames:
    print("user name is available")
else:
    print("username already taken")

