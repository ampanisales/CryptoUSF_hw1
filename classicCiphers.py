#!/usr/bin/env python

""" classicCiphers.py

- Description: Able to encrypt or decrypt a text file with a 
               variety of ciphers

__author__ = "Anthony Panisales"

- Resources:
	https://pycipher.readthedocs.io/en/master/

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


@click.group(context_settings=CONTEXT_SETTINGS)
def classicCiphers():
    pass

@classicCiphers.command()
@click.option('-c', is_flag=True, help='use the Caesar Cipher')
@click.argument('file', type=click.Path(exists=True))
def encrypt(c, **f):
	"""Encrypts a file"""
	file = open(f.get('file'), 'r')
	oldFileText = file.read().upper()
	file.close()

	file = open(f.get('file'), 'w')

	# Use Caesar Cipher
	if c == True:
		cipher = CaesarCipher()
		cipher.encipher(oldFileText, file)

	
	file.close()

@classicCiphers.command()
@click.option('-c', is_flag=True, help='use the Caesar Cipher')
@click.argument('file', type=click.Path(exists=True))
def decrypt(c, **f):
	"""Decrypts a file"""
	file = open(f.get('file'), 'r')
	oldFileText = file.read().upper()
	file.close()

	file = open(f.get('file'), 'w')

	# Use Caesar Cipher
	if c == True:
		cipher = CaesarCipher()
		cipher.decipher(oldFileText, file)
	else:
		file.write(oldFileText)

	file.close()

if __name__ == '__main__':
    classicCiphers()