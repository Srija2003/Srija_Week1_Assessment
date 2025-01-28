def generate_pattern(n):
    """Generate a pattern of stars based on user input."""
    pattern = []
    for i in range(1, n + 1):
        pattern.append("*" * i)
    return pattern

def generate_reverse_pattern(n):
    """Generate a reverse pattern of stars based on user input."""
    pattern = []
    for i in range(n, 0, -1):
        pattern.append("*" * i)
    return pattern

def main():
    while True:
        print("\nPattern Generator")
        print("1. Generate Pattern")
        print("2. Generate Reverse Pattern")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("Enter the number of rows: "))
            pattern = generate_pattern(n)
            print("\nGenerated Pattern:")
            for line in pattern:
                print(line)
        elif choice == 2:
            n = int(input("Enter the number of rows: "))
            reverse_pattern = generate_reverse_pattern(n)
            print("\nGenerated Reverse Pattern:")
            for line in reverse_pattern:
                print(line)
        elif choice == 3:
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
main()
