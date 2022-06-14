prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

prime_factors = []


def get_prime_factors(value):
    """Calculate the prime factors for a given value.
    The prime factors for a value are the lowers prime numbers that when multiplied together
    equal the given value.

    Args:
        value (int): The number to calculate prime factors of.

    Returns:
        int: The number 1 if the calculation has succeeded.
    """
    for prime in prime_numbers:
        if value == prime:
            prime_factors.append(prime)
            value = value / prime
            break
        elif value % prime == 0:
            prime_factors.append(prime)
            value = get_prime_factors(value / prime)
    return value


get_prime_factors(630)
print(prime_factors)
