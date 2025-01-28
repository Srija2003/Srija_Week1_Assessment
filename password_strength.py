def check_password_strength(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    for char in password:
        if 'A' <= char <= 'Z':
            has_uppercase = True
        elif 'a' <= char <= 'z':
            has_lowercase = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_characters:
            has_special = True

    if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak Password"

def main():
    user_password = input("Enter a password to check its strength: ")
    strength = check_password_strength(user_password)
    print(f"Password Strength: {strength}")
main()