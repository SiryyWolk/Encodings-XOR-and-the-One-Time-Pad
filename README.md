# Encodings-XOR-and-the-One-Time-Pad

## ASCII Decryption

The file `Practical-3/ASCII_Encrypted.txt` contains a list of decimal
numbers. Each number represents one character in ASCII (American Standard
Code for Information Interchange).

For example:

```text
65, 83, 67, 73, 73
```

represents:

```text
ASCII
```

### What the program does

`Practical-3/ASCII-Decryption.py` performs these steps:

1. Finds `ASCII_Encrypted.txt` in the same folder as the Python script.
2. Reads the list of decimal ASCII values from the file.
3. Uses `ast.literal_eval()` to safely convert the text list into Python data.
4. Converts the values into bytes.
5. Decodes the bytes as ASCII characters.
6. Writes the decoded message to `Practical-3/ASCII_Decrypted.txt`.
7. Prints the decoded message in the terminal.

### How to use it

Open a terminal in the project folder and run:

```bash
python3 Practical-3/ASCII-Decryption.py
```

The program prints the decrypted message and creates or replaces:

```text
Practical-3/ASCII_Decrypted.txt
```

For the current input, the output is:

```text
ASCII stands for American Standard Code for Information Interchange.
```

### Important note

This example is ASCII decoding, not one-time-pad decryption. ASCII converts
numbers into characters. One-time-pad decryption uses XOR and requires both
the ciphertext and the matching key. The `one_time_pad.py` program handles
that XOR operation when a key and ciphertext are available.