# Function = Block of reusable code
#            place () after the function to invoke it

'''def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print() '''

# happy_birthday("Enjin", 20)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

display_invoice("Genshin", 234.4567, "01/09")