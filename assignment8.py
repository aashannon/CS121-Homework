#Aaron Shannon
#CS 121 T/Th


import string

class Cipher(object):
    """This is the Cipher Class"""
    def __init__(self, inputString):
        self.inputString = inputString
        self.encodedString = ''
        self.decodedString = ''

    def __repr__(self):
        s = 'Original String: %s\nEncoded String: %s\nDecoded String: %s' \
                % (self.inputString, self.encodedString, self.decodedString)
        return s


    def upperLower(self, n):
        #Checks to see if element passed in is uppercase, lowercase, or other

        if n in string.ascii_uppercase:
            return 'u'
        elif n in string.ascii_lowercase:
            return 'l'
        else:
            return 'o'

    def countUp(self, char, count, letter):
        #Checks edge cases for ASCII range, and continues to shift the letters in the positive direciton


        #Checks uppercase range
        if letter == 'u':
            while count > 0:
                if char < 90:
                    char += 1
                else:
                    char = 65
                count -= 1
            return char

        #Checks lowercase range
        elif letter == 'l':
            while count > 0:
                if char < 122:
                    char += 1
                else:
                    char = 97
                count -= 1
            return char

        else:
            return None

    def countDown(self, char, count, letter):
        #Checks edge cases for ASCII range, and contiues counting to shift the letters in the negative direction


        #Checks uppercase range
        if letter == 'u':
            while count > 0:
                if char <= 65:
                    char = 90
                else:
                    char -= 1
                count -= 1
            return char

        #Checks lowercase range
        elif letter == 'l':
            while count > 0:
                if char <= 97:
                    char = 122
                else:
                    char -= 1
                count -= 1
            return char

        else:
            return None


    def encipher(self, n):
        #Takes input string and then shifts letters by the number 'n'

        list = []
        for i in self.inputString:
            if self.upperLower(i) == 'u':
                newChar = self.countUp(ord(i), n, 'u')
                list.append(chr(newChar))

            elif self.upperLower(i) == 'l':
                newChar = self.countUp(ord(i), n, 'l')
                list.append(chr(newChar))

            else:
                list.append(i)

        self.encodedString = ''.join(list)


    def decipherEasy(self, n):
        #Takes in the encoded string and deciphers it. Result should be the same as input.

        list = []
        for i in self.encodedString:
            if self.upperLower(i) == 'u':
                newChar = self.countDown(ord(i), n, 'u')
                list.append(chr(newChar))

            elif self.upperLower(i) == 'l':
                newChar = self.countDown(ord(i), n, 'l')
                list.append(chr(newChar))

            else:
                list.append(i)

        self.decodedString = ''.join(list)



def main():
    s = Cipher('Hello how are Zou?')
    print(repr(s))

    print(s.encipher(3))
    print(s.decipherEasy(3))

    print(s)

if __name__ == '__main__':
    main()
