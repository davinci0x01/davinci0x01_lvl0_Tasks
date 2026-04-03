user_input = input("Enter a year: ")

if int(user_input) % 4 == 0 and (int(user_input) % 100 != 0 or int(user_input) % 400 == 0):
    print(f"{user_input} is a leap year.")
    
else:
    print(f"{user_input} is not a leap year.")