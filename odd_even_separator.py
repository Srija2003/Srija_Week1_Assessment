def separate_odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return odd_numbers, even_numbers

def get_numbers_from_user():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = user_input.split()
    return [int(num) for num in numbers]

def display_results(odd_numbers, even_numbers):
    print(f"Odd numbers: {odd_numbers}")
    print(f"Even numbers: {even_numbers}")

def main():
    numbers = get_numbers_from_user()
    odd_numbers, even_numbers = separate_odd_even(numbers)
    display_results(odd_numbers, even_numbers)

main()
