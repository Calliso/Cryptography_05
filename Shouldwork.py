import string
import random


ASCII_ALPH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ALPHABET = []
ALPHABET2 = []


class Cipher:

    def prepare_key(self, text):
        """
        Deletes duplicate chars from key and makes it uppercase

        Args:
            text (str): key 

        Returns:
            (str): transformed key
        """
        text = text.upper()
        return ''.join(sorted(set(text), key=text.index))

    def __init__(self, key="CAT"):
        self.key = self.prepare_key(key)

    def __repr__(self):
        return "cipher"

    def calc_ascii(self, text):
        """
        Calculates ascii value of given word

        Args:
            text (str): word to calculate ascii value

        Returns:
            (int): calculated ascii value
        """
        return sum(map(ord, text))

    def create_alphabet(self, key):
        """
        Creates two alphabets using given key.
        First alphabet is made by inserting key into first indexes
        of regular english alphabet (26 letters); rest letters are shiftted
        to the right.
        Second one is self-made alphabet which starts at the ascii value of the key
        and next 'letters' are increased by length of given key

        """
        ascii_summ = self.calc_ascii(key)

        for letter in key:
            ALPHABET.append(letter)
        for letter in list(string.ascii_uppercase):
            if letter not in key:
                ALPHABET.append(letter)

        for _ in range(len(ALPHABET)):
            ALPHABET2.append(ascii_summ)
            ascii_summ += len(key)
            if(ascii_summ >= 1000):
                ascii_summ = 100

    def crypt(self, text):
        """
        Encrypts given text

        Args:
            text (str): file name

        Returns:
            (str): encrypted text
        """
        if len(ALPHABET) == 0:
            self.create_alphabet(self.key)
        with open(text) as text:
            lines = [line.split() for line in text]

        
        encrypted = ''
        for line in lines:
            for word in line:
                word = word.upper()
                for letter in word:
                    rand_alph = random.randint(0, 1)
                    if letter in string.ascii_uppercase:
                        if rand_alph == 0:
                            encrypted += ALPHABET[ord(letter)-65]
                        else:
                            encrypted += str(ALPHABET2[ord(letter)-65])
                    else:
                        encrypted += letter
                encrypted += ' '
            encrypted += '\n'
        f = open('encrypted.txt', 'w')
        f.write(encrypted)
        f.close()

        return encrypted

    def decrypt(self, text):
        """
        Decrypts given text

        Args:
            text (str): Encrypted text
        """
        with open(text) as text:
            lines = [line.split() for line in text]
        decrypted = ''
        if len(ALPHABET) == 0:
            self.create_alphabet(self.key)
        number = ''
        for line in lines:
            for word in line:
                for letter in word:

                    if letter in string.ascii_uppercase:
                        decrypted += ASCII_ALPH[ALPHABET.index(letter)]
                    elif letter.isnumeric():
                        number += letter
                    else:
                        decrypted += letter
                    if len(number) == 3:
                        decrypted += ASCII_ALPH[ALPHABET2.index(int(number))]
                        number = ''
                decrypted += ' '
            decrypted += '\n'
        
        f = open('decrypted.txt', 'w')
        f.write(decrypted)
        f.close()

        return decrypted
