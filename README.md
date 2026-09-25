# Encodings XOR and the One Time Pad

This project shows three related ideas:

- ASCII encoding and decoding
- XOR as a bitwise operation
- The one-time pad cipher

## ASCII Encoding and Decoding

`Practical-3/ASCII.py` combines ASCII encoding and decoding into one program.
It saves encoded values in `Practical-3/ASCII_Encrypted.txt` and decoded text in
`Practical-3/ASCII_Decrypted.txt`.

### Encode a message

From the `Practical-3` folder, run:

```bash
python3 ASCII.py -e
```

When prompted, type a message. The program stores the ASCII values in the
encrypted file, for example:

```python
[72, 101, 108, 108, 111]
```

This represents `Hello` in decimal ASCII.

### Decode the message

```bash
python3 ASCII.py -d
```

The program reads the saved values, converts them back to characters, and saves
the plaintext output. This is simple data conversion, not secure encryption.

### Important note

ASCII is just a way of representing text as numbers. Anyone who sees those
numbers can decode them, so this is not real cryptography.

## XOR Basics

The file `Practical-3/xor.py` demonstrates XOR on byte sequences. XOR is a
bitwise operation, not a base-conversion or big-number calculation.

```python
def xor_bytes(bytes_seq_1, bytes_seq_2):
    return bytes([a ^ b for a, b in zip(bytes_seq_1, bytes_seq_2)])
```

XOR rules:

- 0 ^ 0 = 0
- 0 ^ 1 = 1
- 1 ^ 0 = 1
- 1 ^ 1 = 0

Because XOR is reversible, the same operation can be used to undo it:

```python
ciphertext_byte = plaintext_byte ^ key_byte
plaintext_byte = ciphertext_byte ^ key_byte
```

This is the same idea used in a one-time pad.

## How the One-Time Pad Works

A one-time pad is a stream cipher that uses a key as long as the message. In
this project, the key is generated using `os.urandom(length)`, which produces a
random byte sequence.

Encryption is:

```python
ciphertext_byte = plaintext_byte ^ key_byte
```

Decryption is:

```python
plaintext_byte = ciphertext_byte ^ key_byte
```

The key must be:

- truly random
- the same length as the message
- used only once
- kept secret by both sender and receiver

If the key is reused or guessed, the encryption is no longer secure.

The script `Practical-3/one_time_pad.py` checks that the message and key have
matching lengths before XORing each byte. It prints the key and ciphertext in
hexadecimal so they can be shared safely.

This is why the one-time pad is considered theoretically secure: as long as the
key is secret and never reused, the ciphertext reveals no useful information
about the plaintext.
