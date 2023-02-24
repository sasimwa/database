from main import User

try:
    user_name = input("Enter Your Name \n")
    user_email = input("Enter Your Email \n")
    user_password = input("Enter Your Password \n")


    User.create(name = user_name,email = user_email,password = user_password)
    print("User Created Successfully")

except:
    print("Failed To Create User Use a Different Email")