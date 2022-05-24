import datetime

email = "hammy@gmail.com"
password = "1234"

email_prompt = True
while email_prompt:
    entered_email = input("Please enter email: ")
    if entered_email == email:
        email_prompt = False
        password_prompt = True
        while password_prompt:
            entered_password = input("Please enter password: ")
            if entered_password == password:
                password_prompt = False
            else:
                print("Please enter the correct password")
    else:
        print("Please enter a valid email")

login_time = datetime.datetime.now()
print(f"Login success! You logged in on {login_time}")    
