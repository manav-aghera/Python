print(" ---------- Sign Up into instagram ------------")
username = input("Enter your username: ")
gmail = input("Enter your gmail account (for 2 factor verification): ")
mobile_no = input("Enter your mobile number: ")
c_password = input("Create a password: ")

upper = False
symbol = False
numbers = False

for i in c_password:
    if i.isupper():
        upper = True
    if i in "!@#$%^&*()?/":
        symbol = True
    if i in "1234567890":
        numbers = True

if upper and symbol and numbers and len(c_password) >= 8:
    print("Your password seems strong!")
    attempt = 3
    for i in range(attempt):
        r_password = input("Re-Enter the password: ")
        if r_password == c_password:
            print("Account successfully created!")
            break
        else:
            print("Not matching! Try again.")
else:
    print("Your password is not strong enough! \n Password must contain At least 8 characters, one uppercase letter, one number ,one symbol")