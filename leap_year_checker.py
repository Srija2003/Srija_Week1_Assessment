def get_year_from_user():
    return input("Enter a year to check if it's a leap year (or 'exit' to quit): ")

def is_valid_year(year):
    return year.isdigit()

def is_leap_year(year):
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_leap_year():
    while True:
        user_input = get_year_from_user()
        
        if user_input.lower() == 'exit':
            break
        
        if is_valid_year(user_input):
            if is_leap_year(user_input):
                print(f"{user_input} is a leap year.")
            else:
                print(f"{user_input} is not a leap year.")
        else:
            print("Please enter a valid year.")

check_leap_year()
