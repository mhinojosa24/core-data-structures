#!python

def factorial(num):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(num, int) or num < 0:
        raise ValueError('factorial is undefined for n = {}'.format(num))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)
    return factorial_recursive(num)


def factorial_iterative(num):
    # TODO: implement the factorial function iteratively here
    product = 1
    while num > 0:
        product *= num
        num -= 1
    return product

def factorial_recursive(num):
    # check if n is one of the base cases
    if num == 0 or num == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif num > 1:
        # call function recursively
        return num * factorial_recursive(num - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
