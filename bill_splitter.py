def calculate_tip(total_bill, tip_percentage):
    return (tip_percentage / 100) * total_bill

def calculate_total_amount(total_bill, tip_amount):
    return total_bill + tip_amount

def calculate_amount_per_person(total_amount, num_people):
    return total_amount / num_people

def split_bill():
    total_bill = float(input("Enter the total bill amount:"))
    num_people = int(input("Enter the number of people: "))
    tip_percentage = float(input("Enter the tip percentage (enter 0 for no tip): "))
    tip_amount = calculate_tip(total_bill, tip_percentage)
    total_amount = calculate_total_amount(total_bill, tip_amount)
    
    amount_per_person = calculate_amount_per_person(total_amount, num_people)
    print(f"\nTotal bill amount:{total_bill:.2f}")
    print(f"Tip amount:{tip_amount:.2f}")
    print(f"Total amount including tip:{total_amount:.2f}")
    print(f"Amount per person:{amount_per_person:.2f}")

split_bill()