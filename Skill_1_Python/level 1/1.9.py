phrase = "H4ck3r"
valid_phrase = ""
status = 1

for char in phrase:
    if char.isdigit():
        valid_phrase += char
    elif status == 0:
        char = char.lower()
        valid_phrase += char
        status = 1
    elif status == 1:
        char = char.upper()
        valid_phrase += char
        status = 0


print(valid_phrase)