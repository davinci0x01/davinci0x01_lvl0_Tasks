password = 'davinci0x01'
attempts = 3

while True:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted.")
        print("#"*30)
        print("Welcome Sir")
        print("#"*30)
        break
    else:
        attempts -= 1
        print(f"Incorrect password,You have {attempts} attempts left.")
        if attempts == 0:
            print("Access denied. No attempts left.")
            break

    
