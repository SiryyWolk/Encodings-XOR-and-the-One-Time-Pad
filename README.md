# Encodings XOR and the One Time Pad

## ASCII Encoding and Decoding

`Practical-3/ASCII.py` combines ASCII encoding and decoding into one
program. It saves encoded values in `Practical-3/ASCII_Encrypted.txt` and
decoded plaintext in `Practical-3/ASCII_Decrypted.txt`.

### Encode a message

Run this command from the `Practical-3` folder:

```bash
python3 ASCII.py -e
```

When the program displays `Write a message:`, type any ASCII sentence and
press Enter. The program saves the values to `ASCII_Encrypted.txt` and
prints a confirmation. The file contains values such as:

```python
[72, 101, 108, 108, 111]
```

These values represent `Hello` in decimal ASCII.

### Decode the message

Run the decoder after encrypting a message:

```bash
python3 ASCII.py -d
```

The program reads the values from `ASCII_Encrypted.txt`, prints the original
message in the terminal, and saves it to `ASCII_Decrypted.txt`. Run `-e` again
to replace the encrypted file with a new message.

The program supports ASCII characters only and reports an error for
non-ASCII characters. This is ASCII encoding, not encryption in the security
sense: anyone who sees the numbers can decode them.

### Important note

This example is ASCII decoding, not one-time-pad decryption. ASCII converts
numbers into characters. One-time-pad decryption uses XOR and requires both
the ciphertext and the matching key. The `one_time_pad.py` program handles
that XOR operation when a key and ciphertext are available.

## How the One-Time Pad Works

A one-time pad is a stream cipher that uses a key as long as the message. In
this project, the key is generated with `os.urandom(length)` so it is random
and unpredictable.

The encryption and decryption step uses XOR, a bitwise operation:

```python
ciphertext_byte = plaintext_byte ^ key_byte
```

XOR works like this:

- 0 ^ 0 = 0
- 0 ^ 1 = 1
- 1 ^ 0 = 1
- 1 ^ 1 = 0

Because XOR is its own inverse, the same operation can be used to decrypt:

```python
plaintext_byte = ciphertext_byte ^ key_byte
```

This means:

- Encrypt: `C = P XOR K`
- Decrypt: `P = C XOR K`

The key must be:

- truly random
- at least as long as the message
- used only once
- shared securely between sender and receiver

If the wrong key is used, the output is garbage; if the same key is reused,
attackers can detect patterns and break the cipher.

In `Practical-3/one_time_pad.py`, the program checks that the plaintext and key
have the same length before XORing each byte. The key is output as hexadecimal,
and the ciphertext is also printed in hexadecimal so it can be safely shared.

This is why one-time pad encryption is considered information-theoretically
secure, as long as the key remains secret and is never reused.
