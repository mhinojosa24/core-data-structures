import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)


    alphabet = string.ascii_lowercase
    digits = digits.lower()
    exponent = len(digits) - 1
    num_result = 0
    hex_letter_offset = 87

    for digit in digits:
        if digit.isnumeric():
            digit_value = int(digit)

        elif digit in alphabet:
            digit_value = ord(digit) - hex_letter_offset  # get ordinal number of that character from ascii chart

        else:
            raise ValueError('Opps! you entered a weird character')
        num_result += (base ** exponent) * digit_value
        exponent -= 1
    return num_result



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    all_characters = string.printable
    str_result = ''

    if number == 0:
        return '0'

    while number is not 0:
        remainder = number % base
        quotient = number // base

        if remainder > 9:
            remainder = all_characters[remainder]
            str_result += str(remainder)
            number = quotient # update the current number
        else:
            str_result += str(remainder)
            number = quotient
    print('converted number to base{} => {} '.format(base, str_result[::-1]))
    return str_result[::-1]





def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    decoded_num = decode(digits, base1)
    return encode(decoded_num, base2)




def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # print(decode(digits, base1))
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    print(encode(200, 16))
