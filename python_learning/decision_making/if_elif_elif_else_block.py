#access control
is_user_logged_in=True
user_role='user'

if is_user_logged_in:
    print("user is logged in")

    if user_role=="admin":
        print("access granted")
    else:
        print("access rejected")
else:
    print("kindly login")




print()








#grade calculation
marks = 80

if marks>90:
    print("A grade")
elif marks >80:
    print("B grade")
elif marks >70:
    print("C grade")
else:
    print("No grade")