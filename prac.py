import string

number = 56
alphabet = string.printable
base =  19
result = ''


while number is not 0:
    remainder = number % base
    quotient = number // base

    if remainder > 9:
        remainder = alphabet[remainder]
        # print(remainder)
        result += str(remainder)
        number = quotient
    else:
        result += str(remainder)
        number = quotient
    print(result)
print(result[::-1])
