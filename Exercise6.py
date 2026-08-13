# Validate user input exercise.
# 1. username must not be more than 12 characters.
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")
if len(username) > 12:
    print("Username must not be more than 12 characters.")
elif username.find(" ") != -1:
    print("Username must not contain spaces.")
elif username.isdigit() == True:
    print("Username must not contain digits.")
else:
    print("Username is valid.")