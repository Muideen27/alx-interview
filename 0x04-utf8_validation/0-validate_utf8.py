#!/usr/bin/python3
""" module for UTF8 validation """

def validUTF8(data):
    # Helper function to check if a byte is a valid continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        # Get the number of leading '1' bits to determine the character length
        num_leading_ones = bin(data[i])[2:].rfind('0')
        
        if num_leading_ones == -1:
            num_leading_ones = 0

        # Check if it's a valid start byte and calculate character length
        if num_leading_ones in {0, 1, 2, 3}:
            char_length = num_leading_ones + 1
        else:
            return False

        # Check if there are enough bytes for the character
        if i + char_length > len(data):
            return False

        # Check that the following bytes are valid continuation bytes
        for j in range(1, char_length):
            if not is_continuation(data[i + j]):
                return False

        i += char_length

    return True

# Test cases
data1 = [65]
print(validUTF8(data1))  # True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # False

