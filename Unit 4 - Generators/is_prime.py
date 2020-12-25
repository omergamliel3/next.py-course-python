def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def calculate_primes():
    prime_generator = (n for n in range(100) if is_prime(n))
    print(next(prime_generator))
    print(next(prime_generator))
    print(next(prime_generator))


def main():
    calculate_primes()


if __name__ == "__main__":
    main()
