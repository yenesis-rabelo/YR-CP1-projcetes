#Yenesis Rabelo Password Validator SkillPractice

import re

def check_password_strength():
    while True:
        # prompt the user to input a password
        password = input("Enter your password: ")

        # check if the password meets the length requirement which must be at least 8 characters
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        
        # check if the password contains at least one number
        if not any(char.isdigit() for char in password):
            print("Password must include at least one number.")
            continue
        
        # check if the password contains at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("Password must include at least one special character (e.g., @, #, $, %, *, &).")
            continue
        
        # if all the requirements are met, break out of the loop and accept the password
        print("Password accepted!")
        break

# call the function to check the password
check_password_strength()
