def check_num(num):
    if num % 2 == 0:
        return "the number is even"
    elif num % 2 != 0:
        return "the number is odd"

num = int(input("Enter a number to check: "))

print(check_num(num))