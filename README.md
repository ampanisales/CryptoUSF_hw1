# Classic Ciphers

A Python command-line program to encrypt or decrypt a text file. 

- This tool is able to use a variety of ciphers to accomplish encryption or decryption.
- Available ciphers:
    - the Caesar cipher
    - the Vigenere cipher
    - the Affine cipher
    - the Atbash cipher
    - the Simple Substitution cipher
- Built using Python 3.6.4
- Libraries used:
    - click: used to provide functionality for command line commands and option flags.
    
Help:
```
Usage: classicCiphers.py [OPTIONS] COMMAND [ARGS]...

  A tool that can encrypt or decrypt a text file with a variety of ciphers.

Options:
  -h, --help  Show this message and exit.

Commands:
  decrypt  Decrypts a file using one of the available...
  encrypt  Encrypts a file using one of the available...
```

Encrypt Command Help:
```
Usage: classicCiphers.py encrypt [OPTIONS] FILE

  Encrypts a file using one of the available ciphers.

Options:
  -c          use the Caesar cipher
  -v          use the Vigenere cipher
  -af         use the Affine cipher
  -at         use the Atbash cipher
  -s          use the Simple Substitution cipher
  -h, --help  Show this message and exit.
```

Decrypt Command Help:
```
Usage: classicCiphers.py decrypt [OPTIONS] FILE

  Decrypts a file using one of the available ciphers.

Options:
  -c          use the Caesar cipher
  -v          use the Vigenere cipher
  -af         use the Affine cipher
  -at         use the Atbash cipher
  -s          use the Simple Substitution cipher
  -h, --help  Show this message and exit.
```

Example Usage:
```
# To encrypt a file using the Caesar Cipher
py classicCiphers.py encrypt -c test.txt

# To decrypt a file using the Caesar Cipher
py classicCiphers.py decrypt -c test.txt
```
