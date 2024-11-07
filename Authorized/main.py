#Yenesis Rabelo Authorized Users

authorized_users = [
        "admin1", "user1", "user2", "admin2", "user3" "user4", "admin3", "user5", "user6", "user7", "user8", "user9"
]

#List of authorized admin users
admins = ["admin1", "admin2", "admin3"]

#Checking the users status
def check_user_status(username):
    if username in authorized_users:
        if username in admins:
            print(f"{username} is an admin.")
        else:
            print(f"{username} is a regular user.")
    else:
        print(f"{username} is not authorized.")

        #Example usage
        user_input = input("Enter your username")
        check_user_status(user_input)
