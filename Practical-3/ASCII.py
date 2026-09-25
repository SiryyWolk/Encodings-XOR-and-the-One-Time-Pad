import ast
import sys
from pathlib import Path


ENCRYPTED_FILE = Path(__file__).with_name("ASCII_Encrypted.txt")
DECRYPTED_FILE = Path(__file__).with_name("ASCII_Decrypted.txt")


def encrypt_message():
    message = input("Write a message: ")

    try:
        ascii_values = list(message.encode("ascii"))
    except UnicodeEncodeError as error:
        raise ValueError("Only ASCII characters are supported.") from error

    ENCRYPTED_FILE.write_text(repr(ascii_values) + "\n", encoding="utf-8")
    print(f"Encrypted ASCII values saved to {ENCRYPTED_FILE.name}")


def decrypt_message():
    if not ENCRYPTED_FILE.exists():
        raise FileNotFoundError(
            f"{ENCRYPTED_FILE.name} was not found. Run ASCII.py -e first."
        )

    values = ast.literal_eval(ENCRYPTED_FILE.read_text(encoding="utf-8"))
    if not isinstance(values, list) or not all(
        isinstance(value, int) and 0 <= value <= 127 for value in values
    ):
        raise ValueError(
            f"{ENCRYPTED_FILE.name} must contain ASCII values from 0 to 127."
        )

    plaintext = bytes(values).decode("ascii")
    DECRYPTED_FILE.write_text(plaintext + "\n", encoding="utf-8")
    print("Decrypted message:")
    print(plaintext)
    print(f"Plaintext saved to {DECRYPTED_FILE.name}")


if len(sys.argv) != 2 or sys.argv[1] not in {"-e", "-d"}:
    print("Usage: python ASCII.py [-e|-d]")
    sys.exit(1)

try:
    if sys.argv[1] == "-e":
        encrypt_message()
    else:
        decrypt_message()
except (FileNotFoundError, OSError, ValueError) as error:
    print(f"Error: {error}")
    sys.exit(1)