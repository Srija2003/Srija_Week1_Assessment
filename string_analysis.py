def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if ('a' <= char <= 'z' or 'A' <= char <= 'Z') and char not in vowels:
            count += 1
    return count

def count_digits(s):
    count = 0
    for char in s:
        if '0' <= char <= '9':  # Check if char is between '0' and '9'
            count += 1
    return count

def count_special_characters(s):
    count = 0
    for char in s:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):  # Not a letter or digit
            count += 1
    return count

def reverse_string(s):
    return s[::-1]

def analyze_string(s):
    vowels = count_vowels(s)
    consonants = count_consonants(s)
    digits = count_digits(s)
    special_chars = count_special_characters(s)
    reversed_str = reverse_string(s)

    print("\nString Analysis:")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")
    print(f"Special Characters: {special_chars}")
    print(f"Reversed String: {reversed_str}")

def main():
    user_input = input("Enter a string to analyze: ")
    analyze_string(user_input)
    
main()
