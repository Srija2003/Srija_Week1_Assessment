def fizz_buzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def main():
    fizz_buzz(1, 100)


main()
