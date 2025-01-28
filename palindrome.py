def is_palindrome(value):
    value = str(value)
    start = 0
    end = len(value) - 1
    
    while start < end:
        if value[start] != value[end]:
            return False
        start += 1
        end -= 1
    
    return True

while True:
    user_input = input("Enter a string or number (or 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break
    
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")
    else:
        print(f"{user_input} is not a palindrome.")
