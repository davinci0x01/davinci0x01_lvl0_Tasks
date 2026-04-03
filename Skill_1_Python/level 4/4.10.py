def extract_vowels(phrase):
    vowels = "aeiouAEIOU"
    founded_vowels = ""
    valid_phrase = ""
    for char in phrase:
        if char in vowels:
            founded_vowels += char
        else:
            valid_phrase += char
    return founded_vowels , valid_phrase
phrase = input("Enter a phrase: ")

print("Vowels in the phrase:", extract_vowels(phrase)[0])
print("Phrase without vowels:", extract_vowels(phrase)[1])
