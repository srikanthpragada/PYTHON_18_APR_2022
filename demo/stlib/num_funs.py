# Numeric functions

def iseven(n):
    """
    Checks whether given number is even
    :param n: Number to check
    :return: True on even, False otherwise
    """
    return n % 2 == 0


def ispositive(n):
    return n > 0


# Testing
if __name__ == '__main__':
    print(iseven(10), iseven(15))
    print(ispositive(10), ispositive(-15))