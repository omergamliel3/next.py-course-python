def main():
    # create an iterator
    x = iter([1, 2, 3, 4, 5])
    next(x)
    next(x)
    for i in x:
        print(i)

    # reversed returns an iterator
    sentence = ['Iterators', 'are', 'very', 'useful']
    my_iterator = reversed(sentence)
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))

    # map returns an iterator
    square_iter = map(lambda x: x ** 2, [2, 3, 4])
    for num in square_iter:
        print(num)


if __name__ == "__main__":
    main()
