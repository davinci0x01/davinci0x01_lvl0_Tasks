import base64

input_file = "file2.txt"
output_file = "encoded_file.txt"

with open(input_file, "rb") as f:
    data = f.read()

encoded_data = base64.b64encode(data)

with open(output_file, "wb") as f:
    f.write(encoded_data)

print("File encoded successfully.")
print("Output saved to:", output_file)
