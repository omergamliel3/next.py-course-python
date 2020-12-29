import file1 as f


class BirthdayCard(f.GreetingCard):
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch', sender_age=0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print('Happy birthday!')
        print(f'Sender age: {self._sender_age}')
