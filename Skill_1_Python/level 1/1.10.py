phrase = "P@ssw0rd"

#T_phrase = "Password"

vowels = "aeiouAEIOU"

valid_phrase = ""

for char in phrase:
    if char in vowels:
        char = "*"
        valid_phrase += char
    else:
        valid_phrase += char
        
print(valid_phrase)