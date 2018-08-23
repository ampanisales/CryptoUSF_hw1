#!/usr/bin/env python

""" classicCiphers.py

- Description: Able to encrypt or decrypt a text file with a 
               variety of ciphers

- TODO: Descriptions of algorithms used

__author__ = "Anthony Panisales"

- Resources:
	http://www.practicalcryptography.com/ciphers/caesar-cipher/
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
					print("Not a valid key")
					continue
				else:
					return key      
			except ValueError:
				print("Not a valid key")
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
		while True:
			keyString = input("Key: ").upper()	
			if not keyString.isalpha():
				print("Not a valid key")
				continue
			else:
				print("valid key")
				break
		
		for c in keyString:
			self.key.append(self.letters.index(c))


	def encipher(self, oldFileText, file):
		""" TODO: Function Description """
		keyIndex = 0
		for c in oldFileText:
			self.getKey()
			newChar = self.letters[self.letters.index(c) + self.key[keyIndex % len(self.key)]]
			keyIndex += 1
			file.write(newChar)

	def decipher(self, oldFileText, file):
		""" TODO: Function Description """
		keyIndex = 0
		for c in oldFileText:
			self.getKey()
			newChar = self.letters[self.letters.index(c) - self.key[keyIndex % len(self.key)]]
			keyIndex += 1
			file.write(newChar)


@click.group(context_settings=CONTEXT_SETTINGS)
def classicCiphers():
    pass

@classicCiphers.command()
@click.option('-c', is_flag=True, help='use the Caesar Cipher')
@click.option('-v', is_flag=True, help='use the Vigenere Cipher')
@click.argument('file', type=click.Path(exists=True))
def encrypt(c, v, **f):
	"""Encrypts a file"""
	file = open(f.get('file'), 'r')
	oldFileText = file.read().upper()
	file.close()

	file = open(f.get('file'), 'w')

	cipher = None
	
	if c == True:
		cipher = CaesarCipher()
	elif v == True:
		cipher = VigenereCipher()

	if cipher is not None:
		cipher.decipher(oldFileText, file)
	else:
		file.write(oldFileText)

	file.close()

@classicCiphers.command()
@click.option('-c', is_flag=True, help='use the Caesar Cipher')
@click.option('-v', is_flag=True, help='use the Vigenere Cipher')
@click.argument('file', type=click.Path(exists=True))
def decrypt(c, v, **f):
	"""Decrypts a file"""
	file = open(f.get('file'), 'r')
	oldFileText = file.read().upper()
	file.close()

	file = open(f.get('file'), 'w')

	cipher = None

	if c == True:
		cipher = CaesarCipher()
	elif v == True:
		cipher = VigenereCipher()

	if cipher is not None:
		cipher.decipher(oldFileText, file)
	else:
		file.write(oldFileText)

	file.close()

if __name__ == '__main__':
    classicCiphers()
