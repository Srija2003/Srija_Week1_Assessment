def find_second_largest(numbers):
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

def get_numbers_from_user():
    user_input = input("Enter a list of numbers separated by spaces: ")
    return [int(num) for num in user_input.split()]

def main():
    numbers = get_numbers_from_user()
    
    if len(numbers) < 2:
        print("Please enter at least two numbers.")
    else:
        second_largest = find_second_largest(numbers)
        if second_largest == float('-inf'):
            print("All numbers in the list are the same.")
        else:
            print(f"The second largest number is: {second_largest}")

main()
