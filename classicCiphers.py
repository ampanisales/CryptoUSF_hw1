#!/usr/bin/env python

""" classicCiphers.py

- Description: Able to encrypt or decrypt a text file with a 
               variety of ciphers

- TODO: Descriptions of algorithms used

__author__ = "Anthony Panisales"

- Resources:
	http://www.practicalcryptography.com/ciphers/caesar-cipher/
	www.practicalcryptography.com/ciphers/affine-cipher/
	https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm

"""

# from __future__ import print_function
# from future.utils import python_2_unicode_compatible
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

class CaesarCipher:

	letters = []
	for i in range(0, 26):
 		letters.append(chr(ord('A') + i))

	def getKey(self):
		""" TODO: Function Description """
		while True:
			try:
				key = int(input("Key (0-25): "))	
				if key < 0 or key > 25:
					print("Invalid key")
					continue
				else:
					return key      
			except ValueError:
				print("Invalid key")
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

class VigenereCipher:

	letters = []
	for i in range(0, 26):
 		letters.append(chr(ord('A') + i))
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

class AffineCipher:

	letters = []
	for i in range(0, 26):
 		letters.append(chr(ord('A') + i))

	def getKey(self):
		""" TODO: Function Description """
		key = []
		while True:
			try:
				a = int(input("a: "))	
				if a < 0 or a % 2 == 0 or a == 13:
					print("Invalid key: Must be a positive number less than and has no common factors with 26")
					continue
				else:
					key.append(a)
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
					key.append(b)
					return key      
			except ValueError:
				print("Invalid key")
				continue

	def encipher(self, oldFileText, file):
		""" TODO: Function Description """
		key = self.getKey()
		a = key[0]
		b = key[1]
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[((self.letters.index(c) * a + b) % 26) % 26]
			file.write(newChar)

	def decipher(self, oldFileText, file):
		""" TODO: Function Description """
		key = self.getKey()
		a = key[0]
		b = key[1]
		inverse = 0
		for x in range(0, 27):
			if (x * a) % 26 == 1:
				inverse = x
		for c in oldFileText:
			newChar = c
			if c in self.letters:
				newChar = self.letters[(inverse * (self.letters.index(c) - b) % 26) % 26]
			file.write(newChar)

class AtbashCipher:

	letters = []
	for i in range(0, 26):
 		letters.append(chr(ord('A') + i))

	def getKey(self):
		""" TODO: Function Description """

	def encipher(self, oldFileText, file):
		""" TODO: Function Description """

	def decipher(self, oldFileText, file):
		""" TODO: Function Description """


@click.group(context_settings=CONTEXT_SETTINGS)
def classicCiphers():
    pass

@classicCiphers.command()
@click.option('-c', is_flag=True, help='use the Caesar Cipher')
@click.option('-v', is_flag=True, help='use the Vigenere Cipher')
@click.option('-af', is_flag=True, help='use the Affine Cipher')
@click.option('-at', is_flag=True, help='use the Atbash Cipher')
@click.argument('file', type=click.Path(exists=True))
def encrypt(c, v, a, **f):
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
@click.argument('file', type=click.Path(exists=True))
def decrypt(c, v, af, **f):
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

		if cipher is not None:
			cipher.decipher(oldFileText, file)
		else:
			file.write(oldFileText)
	except KeyboardInterrupt:
		file.write(oldFileText)

	file.close()

if __name__ == '__main__':
    classicCiphers()
