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



my_list = ['max', 'sara', 'jenny', 'isaiah']
my_list.sort()
minus_first = my_list[:-1]
print(minus_first)
