users = {
    "admin": "admin123",
    "user1": "pass123",
    "user2": "qwerty",
    "guest": "guest123"
}

username = input("Enter username: ")

if username in users:
    print("Password:", users[username])
else:
    print("Username not found.")
