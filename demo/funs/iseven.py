def iseven(n):
    return n % 2 == 0

def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False

    return True


print(iseven(10), iseven(13))
print(isprime(11))
