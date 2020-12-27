def get_fibo():
    yield 0
    yield 1
    fibo_numbers = [0, 1]
    while True:
        length = len(fibo_numbers)
        fibo_numbers.append(
            fibo_numbers[length - 1] + fibo_numbers[length - 2])
        yield fibo_numbers[len(fibo_numbers) - 1]


def get_fibo_better():
    yield 0
    yield 1
    x = 0
    y = 1
    while True:
        num = x + y
        x = y
        y = num
        yield num


def main():
    fibo_gen = get_fibo_better()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))


if __name__ == "__main__":
    main()
