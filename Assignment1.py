#Names: Zainab Aamir, Abby Friesen, Mark Vu Nguyen

#note(delete once completed): Zainab please add inline comments to your sections of code. Thanks!

def greeting_message():
    userName = input("Please Enter your Name: ")
    print(f"Welcome to Currency Converter {userName}!")
    return userName


def exit_message(name):
    print(f"Thank you for Using Currency Converter")
    print(f"Have a Wonderful Day {name}")

# Exchange Rates
# Australian Dollar, Brazilian Real, European Euro, Indian Rupee, Japanese Yen, Mexican Peso
AUD, BRL, EUR, INR, JPY, MXN = 1.58872, 5.78991, 0.922317, 86.9736, 148.586, 20.1058

# Rate Names list
rateNames = ["Australian Dollar", "Brazilian Real", "European Euro", "Indian Rupee", "Japanese Yen", "Mexican Peso"]

# 100 USD, to exchange
USD = 100

# currency conversion method
# takes exchange rate as the parameter
def convert_currency(rate):
    # $100 USD in X is...
    return USD * rate

def list_choices():
    # Print currency options by looping over rateNames list
    num = 0
    for x in rateNames:
        num += 1
        print(f"{num}. {x}")

def request_input():
    # keeps asking for input until no errors are triggered
    while True:
        try:
            # request input and cast to an int
            # if input cannot be converted to an int (ex. it contains letters) a ValueError will occur
            request = int(input("Please enter your choice of currency (1-6): ")) 
           
            # if request is not within 1-6 raise the IndexError
            if request not in range (1, 6): 
                raise IndexError
            # if no errors were triggered break out of loop
            break
        except IndexError:
            print("Invalid option. Enter a number within list. (1-6)")
        except ValueError:
            print("Enter only the numeric value without additional characters.")
    # returns the request as an int
    return request

def process_input(input):
    # echoes user input and displays it
    print("Your choice:", input)
    # code to process input here
    convert_currency(input)
    # code to print result

def main():
    userName = greeting_message()

    # show options
    list_choices()

    # request currency to convert to
    input = request_input()

    # process request 
    process_input(input)

    exit_message(userName)

#run the program
main()
