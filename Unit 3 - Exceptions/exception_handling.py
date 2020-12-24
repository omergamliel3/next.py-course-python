def sneaky_func(thing):
    try:
        print("Try!" + thing)
    except:
        print("Exception!")
    else:
        print("Else!")
    finally:
        print("Finally!")


def foo():
    try:
        return 1
    except Exception as err:
        print(err)
    finally:
        return 2


def read_file(file_name):
    print('__CONTENT_START__')
    try:
        input_file = open(file_name, 'r')
    except IOError as err:
        print('__NO_SUCH_FILE__')
    except Exception as err:
        print(err)
    else:
        print(input_file.read())
        input_file.close()
    finally:
        print('__CONTENT_END__')


def main():
    #read_file('Unit 3 - Exceptions/names.txt')
    read_file('Unit 3 - Exceptions/names1.txt')


if __name__ == "__main__":
    main()
