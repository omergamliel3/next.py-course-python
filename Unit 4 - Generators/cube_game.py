import random

# Generator that generates 4 random numbers representing dice rolls
cube_game = (random.randint(1, 6) for i in range(4))


def main():
    total = 0
    for num in cube_game:
        total += num
    print(total)


if __name__ == "__main__":
    main()
