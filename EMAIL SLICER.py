#First take input as enter the email address.
#Define what is your username.
#Define what is your domain name.
#Than print the output using "f" function.
#At the output we got username and domain name separated. 

print("Welcome to Email slicer!!!")
email = input("Enter your Email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
print(f"Your username is {username} & domain is {domain}")