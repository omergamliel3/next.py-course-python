import itertools


def main():
    # use permutations func from itertools to calculate all permutations
    lst = [0, 5, 6, 9]
    for permutation in itertools.permutations(lst):
        print(permutation)


if __name__ == "__main__":
    main()
