def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(47))  # Output: True
print(is_prime(8))   # Output: False
print(is_prime(92))   # Output: False
print(is_prime(13))   # Output: True