import hashlib

def calculate_sha256(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()


file1 = input("Enter first file path: ")
file2 = input("Enter second file path: ")

hash1 = calculate_sha256(file1)
hash2 = calculate_sha256(file2)

print("File 1 Hash:", hash1)
print("File 2 Hash:", hash2)

if hash1 == hash2:
    print("Files are identical (Integrity verified)")
else:
    print("Files are different")
