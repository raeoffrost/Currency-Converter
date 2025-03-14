#Names: Zainab Aamir, Abby, Mark


def greeting_message():
    userName = input("Please Enter your Name: ")
    print(f"Welcome to Currency Converter {userName}!")
    return userName


def exit_message(name):
    print(f"Thank you for Using Currency Converter")
    print(f"Have a Wonderful Day {name}")


def main():
    userName = greeting_message()

    #insert other code


    exit_message(userName)