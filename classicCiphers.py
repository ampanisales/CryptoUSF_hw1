#!/usr/bin/env python
""" classicCiphers.py
    Able to encrypt or decrypt a text file with a variety of ciphers

__author__ = "Anthony Panisales"

"""

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

class Cipher(object):
	""" Base class for the ciphers """
	letters = []
	for i in range(0, 26):
		letters.append(chr(ord('A') + i))
	pass

class CaesarCipher(Cipher):
	""" In the Caesar Cipher, "each letter of the text is replaced
        by the letter which stands a certain number of places
        before or after it in the alphabet"

        Sources:
            "Manual of Cryptography", 1911, page 28
            https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm
            http://www.practicalcryptography.com/ciphers/caesar-cipher/
            https://pycipher.readthedocs.io/en/master/#caesar-cipher
	"""

	def getKey(self):
		""" TODO: Function Description """
		while True:
			try:
				key = int(input("Shift value (0-25): "))	
				if key < 0 or key > 25:
					print("Invalid value")
					continue
				else:
					return key      
			except ValueError:
				print("Invalid value")
				continue

	def encipher(self, oldFileText, file):
		""" TODO: Function Description """
		key = self.getKey()
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[(self.letters.index(c) + key) % 26]
			file.write(newChar)

	def decipher(self, oldFileText, file):
		""" TODO: Function Description """
		key = self.getKey()
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[(self.letters.index(c) - key) % 26]
			file.write(newChar)


class VigenereCipher(Cipher):
	""" The Vigenere table "consists of a set of twenty-six alphabets 
        successively displaced one letter per row, with the plaintext 
        letters at the top of the square, the key letters at the side, 
        and the cipher letters inside. The method of using the table is 
        to agree upon a key word, which causes the equivalents of the 
        plaintext letters to change as the key changes."

        Sources:
            "Friedman Lectures on Cryptography", 1965, page 29
            https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm
	"""
	key = []

	def getKey(self):
		""" TODO: Function Description """
		keyString = ""
		while not keyString.isalpha():
			keyString = input("Key: ").upper()	
			if not keyString.isalpha():
				print("Invalid key: The key should only contain letters")

		for c in keyString:
			self.key.append(self.letters.index(c))

	def encipher(self, oldFileText, file):
		""" TODO: Function Description """
		keyIndex = 0
		self.getKey()
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[(self.letters.index(c) + self.key[keyIndex % len(self.key)]) % 26]
			keyIndex += 1
			file.write(newChar)

	def decipher(self, oldFileText, file):
		""" TODO: Function Description """
		keyIndex = 0
		self.getKey()
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[(self.letters.index(c) - self.key[keyIndex % len(self.key)]) % 26]
			keyIndex += 1
			file.write(newChar)


class AffineCipher(Cipher):
	""" The 'key' for the Affine cipher consists of 2 numbers, we'll call 
        them a and b. The following discussion assumes the use of a 26 character 
        alphabet (m = 26). a should be chosen to be relatively prime to m (i.e. 
        a should have no factors in common with m). b is an integer 0-25.

        The ciphertext letter c, for any given letter p is:
        c = ap + b (mod m)

        The decryption function is: 
        p = a^-1 (c - b) (mod m)
        where a^-1 is the multiplicative inverse of a in the group of integers modulo m.

        To find a multiplicative inverse, we need to find a number x such that:
        ax = 1 (mod m)

        Sources:
            https://pycipher.readthedocs.io/en/master/#affine-cipher
            http://www.practicalcryptography.com/ciphers/affine-cipher/
	"""

	key = []

	def getKey(self):
		""" TODO: Function Description """
		while True:
			try:
				a = int(input("a: "))	
				if a < 0 or a % 2 == 0 or a == 13:
					print("Invalid key: Must be a positive number less than and has no common factors with 26")
					continue
				else:
					self.key.append(a)
					break     
			except ValueError:
				print("Invalid key: Must be a positive number less than and has no common factors with 26")
				continue

		while True:
			try:
				b = int(input("b (0-25): "))	
				if b < 0 or b > 25:
					print("Invalid key")
					continue
				else:
					self.key.append(b)
					return      
			except ValueError:
				print("Invalid key")
				continue

	def encipher(self, oldFileText, file):
		""" TODO: Function Description """
		self.getKey()
		a = self.key[0]
		b = self.key[1]
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[((self.letters.index(c) * a + b) % 26) % 26]
			file.write(newChar)

	def decipher(self, oldFileText, file):
		""" TODO: Function Description """
		self.getKey()
		a = self.key[0]
		b = self.key[1]
		inverse = 0
		for x in range(0, 27):
			if (x * a) % 26 == 1:
				inverse = x
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[(inverse * (self.letters.index(c) - b) % 26) % 26]
			file.write(newChar)


class AtbashCipher(Cipher):
	""" The Atbash Cipher "consisted in writing the last
        letter of the alphabet instead of the first letter,
        and the last but one instead of the second, and so on."

        Sources:
            "Cryptography", 1926, page 28
            http://www.practicalcryptography.com/ciphers/classical-era/atbash-cipher/
	"""

	def encipher(self, oldFileText, file):
		""" TODO: Function Description """
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[25 - self.letters.index(c)]
			file.write(newChar)

	def decipher(self, oldFileText, file):
		""" TODO: Function Description """
		self.encipher(oldFileText, file)


class SimpleSubstitutionCipher(Cipher):
	""" In the Simple Substitution Cipher, "each letter of the message
        is replaced by a ﬁxed substitute, usually also a letter...
        The key is a permutation of the alphabet."

        Sources:
            "The Mathamatical Theory of Cryptography", 1945, pages 31-32
            https://pycipher.readthedocs.io/en/master/#simple-substitution-cipher
            http://www.practicalcryptography.com/ciphers/simple-substitution-cipher/
	"""

	key = []

	def getKey(self):
		""" TODO: Function Description """
		keyString = ""
		while True:
			keyString = input("Key: ").upper()	
			if not keyString.isalpha():
				print("Invalid key: The key should only contain letters")
				continue
			if len(keyString) != 26:
				print("Invalid key: The key must be 26 characters in length")
				continue
			for c in keyString:
				self.key.append(c)
			if len(self.key) != len(set(self.key)):
				print("Invalid key: There should be no repeated characters in the key")
				continue
			break

	def encipher(self, oldFileText, file):
		""" TODO: Function Description """
		self.getKey()
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.key[self.letters.index(c)]
			file.write(newChar)

	def decipher(self, oldFileText, file):
		""" TODO: Function Description """
		self.getKey()
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[self.key.index(c)]
			file.write(newChar)

@click.group(context_settings=CONTEXT_SETTINGS)
def classicCiphers():
    pass

@classicCiphers.command()
@click.option('-c', is_flag=True, help='use the Caesar Cipher')
@click.option('-v', is_flag=True, help='use the Vigenere Cipher')
@click.option('-af', is_flag=True, help='use the Affine Cipher')
@click.option('-at', is_flag=True, help='use the Atbash Cipher')
@click.option('-s', is_flag=True, help='use the Simple Substitution Cipher')
@click.argument('file', type=click.Path(exists=True))
def encrypt(c, v, af, at, s, **f):
	"""Encrypts a file"""
	file = open(f.get('file'), 'r')
	oldFileText = file.read().upper()
	file.close()

	file = open(f.get('file'), 'w')

	cipher = None
	
	try:
		if c == True:
			cipher = CaesarCipher()
		elif v == True:
			cipher = VigenereCipher()
		elif af == True:
			cipher = AffineCipher()
		elif at == True:
			cipher = AtbashCipher()
		elif s == True:
			cipher = SimpleSubstitutionCipher()

		if cipher is not None:
			cipher.encipher(oldFileText, file)
		else:
			file.write(oldFileText)
	except KeyboardInterrupt:
		file.write(oldFileText)

	file.close()

@classicCiphers.command()
@click.option('-c', is_flag=True, help='use the Caesar Cipher')
@click.option('-v', is_flag=True, help='use the Vigenere Cipher')
@click.option('-af', is_flag=True, help='use the Affine Cipher')
@click.option('-at', is_flag=True, help='use the Atbash Cipher')
@click.option('-s', is_flag=True, help='use the Simple Substitution Cipher')
@click.argument('file', type=click.Path(exists=True))
def decrypt(c, v, af, at, s, **f):
	"""Decrypts a file"""
	file = open(f.get('file'), 'r')
	oldFileText = file.read().upper()
	file.close()

	file = open(f.get('file'), 'w')

	cipher = None

	try:
		if c == True:
			cipher = CaesarCipher()
		elif v == True:
			cipher = VigenereCipher()
		elif af == True:
			cipher = AffineCipher()
		elif at == True:
			cipher = AtbashCipher()
		elif s == True:
			cipher = SimpleSubstitutionCipher()

		if cipher is not None:
			cipher.decipher(oldFileText, file)
		else:
			file.write(oldFileText)
	except KeyboardInterrupt:
		file.write(oldFileText)

	file.close()

if __name__ == '__main__':
    classicCiphers()
