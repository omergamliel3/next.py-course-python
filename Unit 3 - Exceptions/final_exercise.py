from string import punctuation
import sys

# Username contains illegal character exception


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg, index):
        super().__init__(arg)
        self._arg = arg
        self._index = index

    def __str__(self) -> str:
        return f"Provided char '{self._arg}' at index {self._index + 1} is illegal."


# Username's length is shorter then 3 exception
class UsernameTooShort(Exception):
    def __init__(self, arg):
        super().__init__(arg)
        self._arg = arg

    def __str__(self) -> str:
        return f"Username ({self._arg}) contains less then 3 characters."


# Username's length is greater then 16 exception
class UsernameTooLong(Exception):
    def __init__(self, arg):
        super().__init__(arg)
        self._arg = arg

    def __str__(self) -> str:
        return f"Username ({self._arg}) contains more then 16 characters."


# Password missing required characters exception
class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        super().__init__(arg, 'Miss')
        self._arg = arg

    def __str__(self) -> str:
        return f"Provided password is missing required character ({self._arg})."


# Password's length is shorter then 8 exception
class PasswordTooShort(Exception):
    def __init__(self, arg):
        super().__init__(arg)
        self._arg = arg

    def __str__(self) -> str:
        return f"Provided password ({self._arg}) contains less then 8 characters."


# Password's length is greater then 40 exception
class PasswordTooLong(Exception):
    def __init__(self, arg):
        super().__init__(arg)
        self._arg = arg

    def __str__(self) -> str:
        return f"Provided password ({self._arg}) contains more then 40 characters."


# validate username
def check_username(username: str):
    length = len(username)
    if length < 3:
        raise UsernameTooShort(username)
    if length > 16:
        raise UsernameTooLong(username)
    for char in username:
        if not (char.isalpha() or char.isdigit() or char == '_'):
            raise UsernameContainsIllegalCharacter(char, username.index(char))


# validate password
def check_password(password: str):
    # length validation
    length = len(password)
    if length < 8:
        raise PasswordTooShort(password)
    if length > 40:
        raise PasswordTooLong(password)

    # required characters validation
    uppercase_char = False
    lowrcase_char = False
    digit_char = False
    punctuation_char = False

    for char in password:
        if char.isupper():
            uppercase_char = True
        elif char.islower():
            lowrcase_char = True
        elif char.isdigit():
            digit_char = True
        elif char in punctuation:
            punctuation_char = True

    if not all([uppercase_char, lowrcase_char, digit_char, punctuation_char]):
        missing_chars = []
        if not uppercase_char:
            missing_chars.append('uppercase char')
        if not lowrcase_char:
            missing_chars.append('lowercase char')
        if not digit_char:
            missing_chars.append('digit char')
        if not punctuation_char:
            missing_chars.append('special char')

        raise PasswordMissingCharacter(', '.join(missing_chars))


# validate input (username & password)
def check_input(username, password):
    try:
        check_username(username)
        check_password(password)
    except Exception as err:
        print(err)
    else:
        print('\nVALID INPUT\n')
        return True


# test check_input
def test():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

# main
def main():
    while True:
        username = input('\nEnter username: ')
        password = input('\nEnter password: ')
        if username in ["0", ""] or password in ["0", ""]:
            sys.exit(0)
        valid = check_input(username, password)
        if valid:
            break


if __name__ == "__main__":
    main()
