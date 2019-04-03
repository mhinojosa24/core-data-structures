import string

number = '235'
alphabet = string.ascii_lowercase
digits = '235'
base =  8
# result = ''
#
#
# # alphabet = string.ascii_lowercase
# # digits = digits.lower()
# exponent = len(digits) - 1
# print('expo =>', exponent)
# num_result = 0
#
# for digit in digits:
#     if digit not in alphabet: # check if digit is not a letter
#         num_result += (base ** exponent) * int(digit)
#         print('num result => ', num_result)
#         exponent -= 1
#         print('expo =>', exponent)
#     else:
#         hex_to_digit = ord(digit) - 87 # get ordinal number of that character from ascii chart
#         digit = hex_to_digit
#         num_result += (base ** exponent) * int(digit)
#         exponent -= 1
#         print('expo =>', exponent)
# print(num_result)



reversed_digits = str(digits[::-1].lower())
conversion_values = string.printable
if base == 64:
    conversion_values = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
answer = 0
for index, given_value in enumerate(reversed_digits):
    print('index => {}, given value => {}'.format(index, given_value))
    print('index of conversion string =>', conversion_values.index(given_value))
    answer += conversion_values.index(given_value)*(base**index)
    print('answer => ', answer)
# if answer == 0:
#     return 0
# else:
#     return answer
