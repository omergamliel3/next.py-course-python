from itertools import combinations


WALLET = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
TARGET_AMOUNT = 100


def main():
    combs_list = []
    for index in range(0, len(WALLET)):
        comb = combinations(WALLET, len(WALLET) - index)
        comb = set(comb)
        combs_list.append(comb)

    options = 0
    for item in combs_list:
        for comb in item:
            if sum(comb) == TARGET_AMOUNT:
                options += 1
                print(f'FIND {TARGET_AMOUNT}!!!')

    print(f'Options: {options}')


if __name__ == "__main__":
    main()
