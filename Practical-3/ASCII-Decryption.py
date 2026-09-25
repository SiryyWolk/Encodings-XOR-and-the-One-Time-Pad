import ast
from pathlib import Path


input_file = Path(__file__).with_name("ASCII_Encrypted.txt")
output_file = Path(__file__).with_name("ASCII_Decrypted.txt")

# Read the collected decimal ASCII values from the input file.
ascii_values = ast.literal_eval(input_file.read_text(encoding="utf-8"))
plaintext = bytes(ascii_values).decode("ascii")

output_file.write_text(plaintext + "\n", encoding="utf-8")
print(f"Decrypted message written to {output_file.name}:")
print(plaintext)
