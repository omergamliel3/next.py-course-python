class GreetingCard:
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch'):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f'Recipient: {self._recipient} , Sender: {self._sender}')
