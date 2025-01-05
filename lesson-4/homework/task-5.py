password = input("enter your password: ")

if len(password) < 8:
    print("password is too short")
elif not any(char.isupper() for char in password):
    print("password should at least one contain upper char")
else:
    print("password is strong")
