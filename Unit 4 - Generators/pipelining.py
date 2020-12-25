

def main():
    integers = (n for n in range(1, 11))
    squared = (n * n for n in integers)
    negated = (-n for n in squared)

    for num in negated:
        print(num)


if __name__ == "__main__":
    main()
