import base64

FILE_NAME = 'Unit 6 - modules/b64/message.txt'


def main():
    # read the text from the file
    with open(FILE_NAME) as input_file:
        base64_message = input_file.read()

    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)

if __name__ == "__main__":
    main()
