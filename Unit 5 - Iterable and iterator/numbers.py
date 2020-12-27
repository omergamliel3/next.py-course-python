def main():
    # first solution
    numbers = iter(list(range(1, 101)))
    for i in numbers:
        next(numbers)
        next(numbers)
        print(i)

    # sedonc solution
    numbers = iter(list(range(1, 101, 3)))
    for i in numbers:
        print(i)


if __name__ == "__main__":
    main()
