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
    - math: used for its ceil function which is used in the simple columnar transposition cipher to get the column sizes
- Sources:
    - Caesar Cipher:
        - "Manual of Cryptography", 1911, page 28
	    - https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm
	    - http://www.practicalcryptography.com/ciphers/caesar-cipher/
	    - https://pycipher.readthedocs.io/en/master/#caesar-cipher
    - Vigenere cipher
        - "Friedman Lectures on Cryptography", 1965, page 29
	    - https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm
    - Affine cipher
        - https://pycipher.readthedocs.io/en/master/#affine-cipher
	    - http://www.practicalcryptography.com/ciphers/affine-cipher/
    - Atbash cipher
        - "Cryptography", 1926, page 28
	    - http://www.practicalcryptography.com/ciphers/classical-era/atbash-cipher/
    - Simple Substitution cipher
        - "The Mathamatical Theory of Cryptography", 1945, pages 31-32
	    - https://pycipher.readthedocs.io/en/master/#simple-substitution-cipher
	    - http://www.practicalcryptography.com/ciphers/simple-substitution-cipher/
    - Simple Columnar Transposition cipher
        - "Basic Cryptanalysis", 1970, pages 4-2, 4-3
	    - www.practicalcryptography.com/ciphers/classical-era/columnar-transposition/
    
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
  -c              use the Caesar cipher
  -v              use the Vigenere cipher
  -af             use the Affine cipher
  -at             use the Atbash cipher
  -s              use the Simple Substitution cipher
  -t              use the Columnar Transposition cipher
  -k, --key TEXT  The key needed for the cipher
  --a TEXT        The 'a' variable need for the Affine cipher
  --b TEXT        The 'b' variable need for the Affine cipher
  -h, --help      Show this message and exit.
```

Decrypt Command Help:
```
Usage: classicCiphers.py decrypt [OPTIONS] FILE

  Decrypts a file using one of the available ciphers.

Options:
  -c              use the Caesar cipher
  -v              use the Vigenere cipher
  -af             use the Affine cipher
  -at             use the Atbash cipher
  -s              use the Simple Substitution cipher
  -t              use the Columnar Transposition cipher
  -k, --key TEXT  The key needed for the cipher
  --a TEXT        The 'a' variable need for the Affine cipher
  --b TEXT        The 'b' variable need for the Affine cipher
  -h, --help      Show this message and exit.
```

Example Usage:
```
# To encrypt a file using the Caesar cipher
py classicCiphers.py encrypt -c --key=3 test.txt

# To decrypt a file using the Caesar cipher
py classicCiphers.py decrypt -c --key=3 test.txt

# To encrypt a file using the Affine cipher
py classicCiphers.py encrypt -af --a=3 --b=11 test.txt

# To decrypt a file using the Affine cipher
py classicCiphers.py decrypt -af --a=3 --b=11 test.txt

# To encrypt a file using the Vigenere cipher
py classicCiphers.py encrypt -v --key=point test.txt

# To decrypt a file using the Vigenere cipher
py classicCiphers.py decrypt -v --key=point test.txt
```
