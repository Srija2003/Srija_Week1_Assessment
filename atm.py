
account_balance = 1000  

def check_balance(): 
    print(f"Your current balance is:{account_balance:.2f}")

def deposit_money():
    global account_balance
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        account_balance += amount
        print(f"{amount:.2f} has been deposited. New balance: {account_balance:.2f}")
    else:
        print("Invalid amount. Please enter a positive value.")
        
def withdraw_money():
    global account_balance
    amount = float(input("\nEnter the amount to withdraw: "))
    if amount > 0:
        if amount <= account_balance:
            account_balance -= amount
            print(f"{amount:.2f} has been withdrawn. Remaining balance: {account_balance:.2f}")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid amount. Please enter a positive value.")
        
def main():
    
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()