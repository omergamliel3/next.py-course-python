class A:
    def __init__(self) -> None:
        self._secret = 12

    def print_secret(self):
        print(self._secret)


class B(A):
    pass


def main():
    # auto call __init__ for B subclass and A superclass
    b = B()
    b.print_secret()


if __name__ == "__main__":
    main()
