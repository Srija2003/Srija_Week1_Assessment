def display_menu():
    print("\nShopping Cart Menu:")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Calculate Total")
    print("4. Exit")

def add_item(cart):
    item_name = input("Enter the name of the item: ")
    
    item_price = float(input("Enter the price of the item: "))
    cart.append({"name": item_name, "price": item_price})
    print(f"{item_name} added to the cart.")
    
    print("Invalid price. Please enter a number.")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} - {item['price']:.2f}")

def calculate_total(cart):
    total = sum(item['price'] for item in cart)
    print(f"\nTotal price of items in the cart: ${total:.2f}")

def shopping_cart():
    cart = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            calculate_total(cart)
        elif choice == "4":
            print("Thank you for shopping. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the shopping cart program
shopping_cart()
