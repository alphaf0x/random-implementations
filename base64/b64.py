#! /usr/bin/env python3

import sys
import binascii

PADDING = '='
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def b64encode(data):
    encoded=''
    binary = to_binary(data)
    # add 0 until an integral number of 6-bit groups forms ??
    while (len(binary)%6)!=0:
        binary = binary + '0'

    # encode 6 bit words of data
    words = int(len(binary)/2)
    slice = 6
    for word in range(0, len(binary), slice):
        letter = ALPHABET[int(binary[word:word+slice], 2)]
        encoded = encoded+letter
    
    # add padding
    if len(data)%3 != 0:
        while len(encoded)%4 != 0:
            encoded = encoded+PADDING
    return encoded    

def b64decode(data):
    print('Decoding!')
    decoded = ''
    for word in range(0, len(data), 4):
        chunk = data[word:word+4]
        chunk = chunk.replace('=','')
        to_decode=''
        for index in range(len(chunk)):
            letter = chunk[index]
            letter_index = ALPHABET.index(letter)
            bin_letter = bin(letter_index)[2:].zfill(6)
            to_decode = to_decode + bin_letter
        for bytes in range(0, len(to_decode), 8):
            decoded = decoded + chr(int(to_decode[bytes:bytes+8],2))
    return decoded
    

def to_binary(data):
    '''Takes data and returns a list of 6 bit slices.'''
    binary_data = ''.join(format(ord(char), 'b').zfill(8) for char in data)
    return binary_data

# Test cases
def test_encoding():
    assert b64encode('pleasure.') == 'cGxlYXN1cmUu'
    assert b64encode('leasure.') == 'bGVhc3VyZS4='
    assert b64encode('easure.') == 'ZWFzdXJlLg=='
    assert b64encode('asure.') == 'YXN1cmUu'
    assert b64encode('sure.') == 'c3VyZS4='


def main():
    data = 'easure.'
    encoded_data = b64encode(data)
    print('Encoded: ' + encoded_data)
    decoded_data = b64decode(encoded_data)
    print('Decoded: ' + decoded_data)

if __name__ == '__main__':
    test_encoding()
    main()