# Encodings-XOR-and-the-One-Time-Pad

## ASCII Encoding and Decoding

`Practical-3/ASCII.py` combines ASCII encoding and decoding into one
program. It saves encoded values in `Practical-3/ASCII_Encrypted.txt` and
decoded plaintext in `Practical-3/ASCII_Decryted.txt`.

### Encode a message

Run this command from the `Practical-3` folder:

```bash
python3 ASCII.py -e
```

When the program displays `Write a message:`, type any ASCII sentence and
press Enter. The program saves the values to `ASCII_Encrypted.txt` and
prints a confirmation. The file contains values such as:

```python
encrypted_message_ascii = [72, 101, 108, 108, 111]
```

These values represent `Hello` in decimal ASCII.

### Decode the message

Run the decoder after encrypting a message:

```bash
python3 ASCII.py -d
```

The program reads the values from `ASCII_Encrypted.txt`, prints the original
message in the terminal, and saves it to `ASCII_Decryted.txt`. Run `-e` again
to replace the encrypted file with a new message.

The program supports ASCII characters only and reports an error for
non-ASCII characters. This is ASCII encoding, not encryption in the security
sense: anyone who sees the numbers can decode them.

### Important note

This example is ASCII decoding, not one-time-pad decryption. ASCII converts
numbers into characters. One-time-pad decryption uses XOR and requires both
the ciphertext and the matching key. The `one_time_pad.py` program handles
that XOR operation when a key and ciphertext are available.