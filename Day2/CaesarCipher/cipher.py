# Takes a piece of plain text and outputs the Caesar-ciphered text (encode). 
# Can also accept Caesar Ciphered text,and output plain text (decode)
# Caesar code essentially consists of shifting every letter by 13 alphabets (and continuing back from a after z)

def shift(char):
    if char.isalpha():
        num = ord(char) + 13  # shift by 13
        if (char.isupper() and num > 90) or (char.islower() and num > 122):
            num -= 26  # rotate from the end
        return chr(num)
    else:
        return char


def unshift(char):
    return shift(char) # IN caesar's code, shifting the code, will actually decode the encoded code as well.


more = "A"
print("Welcome to the Caesar Cipherer!")
while more.upper() != 'Q':
    more = input('Please enter "E" to Encode, "D" to Decode, "Q" to Quit: ')
    if more.upper() == "E":
        text = input ('Please enter the text to be encoded: ')
        encoded = ''.join([shift(c) for c in text])
        print("Equivalent Caesar Encoded text is: ", encoded)
    elif more.upper() == "D":
        text = input('Please enter the text to be decoded: ')
        decoded = ''.join([shift(c) for c in text])
        print("Equivalent Caesar Decoded text is: ", decoded)
    elif more.upper() == "Q":
        print ("Thanks for using the Caesar Cipherer. Come back soon!")
    else:
        print("I didn't quite get that. Please try again. ")

