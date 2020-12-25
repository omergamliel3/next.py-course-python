def parse_ranges(ranges_string: str):
    split_generator = (n.split('-') for n in ranges_string.split(','))
    nums = []
    for start, stop in split_generator:
        for num in range(int(start), int(stop) + 1):
            nums.append(num)
    return nums


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == "__main__":
    main()
