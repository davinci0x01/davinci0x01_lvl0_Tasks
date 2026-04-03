def check_password(password):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if any(char in special_characters for char in password) and any(char.isdigit() for char in password) and len(password) >= 8:
        print("Password is valid.")
        return True
    else:
        print("Password must contain at least 1 special characters and 1 digit.")
        return False


user_password = input("Enter your password: ")
check_password(user_password)
