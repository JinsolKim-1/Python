min_length = 8
key = str(input("Enter your password: "))
auth = False

if any(char.isupper() for char in key) and any(char.islower() for char in key) and any(char.isdigit() for char in key) and any(not char.isalnum() for char in key):
    print ("Nice one! You got it on first try!")
while not auth:
    if len(key) < min_length:
        print("Password must be 8 characters long!")
    elif not any(char.isupper() for char in key):
        print("Password should contain uppercase letters!")
    elif not any(char.islower() for char in key):
        print("Password should contain lowercase letters!")
    elif not any(char.isdigit() for char in key):
        print("Password should contain at least one digit!")
    elif not any(not char.isalnum() for char in key):
        print("Password should contain at least one special character!")
    else:
        auth = True
        break
    
    key = input("Enter your password: ")

print("Your password is strong and valid!")
k=input(("press ") + ("'ENTER'") + (" to exit"))