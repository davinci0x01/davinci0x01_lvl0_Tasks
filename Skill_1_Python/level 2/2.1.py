password = "s3cr3t"

print("Welcome! Please enter the password to continue.")
user_input = input("Enter the password: ")

if user_input == password:
    print("Access granted.")
    print("#"*30)
    print("Welcome to the secret area!")
    print("#"*30)
else:
    print("Access denied. Incorrect password.")
    
