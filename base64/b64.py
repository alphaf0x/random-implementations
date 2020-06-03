#! /usr/bin/env python3

"""
My base64 encoder and decoder written in python3.

NOTE: This tool was made as a coding practice. It is advised
to use an official Python base64.py instead of this code.

https://tools.ietf.org/html/rfc3548.html#section-2.1

"""

"""
Note on Base64:

Base 64 is a way to take any form of data and transform it
to long string of plaintext to protect the data from getting
corrupted.

"""

import sys

"""
ASCII
A-Z => 65-90
a-z => 97-122
0-9 => 48-57
+ => 43
/ => 47
"""

"""
Hexadecimal to octal transformation is useful to convert between binary
and Base64. Both for advanced calculators and programming languages such
conversion is available. For example the 24 bits above is 4D616E (hex)
and converted into octal 23260556, which is divided into four groups
23 26 05 56, which in decimal is 19 22 05 46, which is converted by the
table to Base64.

If there are only two significant input octets (e.g., 'Ma'), or when the
last input group contains only two octets, all 16 bits will be captured
in the first three Base64 digits (18 bits); the two least significant
bits of the last content-bearing 6-bit block will turn out to be zero, 
and discarded on decoding (along with the following = padding characters). 
"""

def b64encode(data):
    ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" 
    """DEFAULT"""
    PADDING='='
    encoded=''

    binary = to_binary(data)

    # add 0 until an integral number of 6-bit groups forms
    while (len(binary)%6)!=0:
        binary = binary + '0'

    # encode 6 bit words of data
    words = int(len(binary)/2)
    slice = 6
    for word in range(0,len(binary),6):
        letter=ALPHABET[int(binary[word:word+slice],2)]
        encoded=encoded+letter
    
    # add padding
    if len(binary) == 12:
        encoded=encoded+PADDING*2
    if len(binary) == 18:
        encoded=encoded+PADDING

    return encoded    

def b64decode(data):

    print("Decoding!")

    pass

"""
Takes some data as input and breaks it down
into 24 bits.
Returns a list where each item is a 6 bit slice
from the previous 24 bits.
"""
def to_binary(data):
    # convert data into 24 bit string
    # zfill() pads string on the left with zeros to fill width.
    binary_data=''.join(format(ord(char), 'b').zfill(8) for char in data)
    return binary_data

# Test cases
data="coded by alphaf0x! :)"
data2 = "Man is distinguished, not only by his reason, but by this singular"
def main():
    # if len(sys.argv) > 3:
    #     print("Too many arguments.")
    #     return
    print("Data: " + data)
    print("Encoded: " + b64encode(data2))
    # b64decode(argv[0])

if __name__ == "__main__":
    main()