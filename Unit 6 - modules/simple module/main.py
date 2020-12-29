import file1 as f1
import file2 as f2


def main():
    b = f2.BirthdayCard(sender_age=10)
    b.greeting_msg()

    g = f1.GreetingCard()
    g.greeting_msg()


if __name__ == "__main__":
    main()
