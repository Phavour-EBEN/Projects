number = int(input("Enter  number: "))


def Fizz_buzz(input):
    if number %5==0 and number%3==0:
        print("FizzBuzz")
    elif number %3==0:
        print("Fizz")
    elif number %5==0:
        print("Buzz")
    else:
        print(number)

Fizz_buzz(number)