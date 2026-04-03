string = "Hello, World!"

letter = 'o'
count = 0

for char in string:
    if char == letter:
        count += 1

print(f"The letter '{letter}' appears {count} times in the string.")