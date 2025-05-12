# Inventory management system

# Initial inventory with 5 products
inventory = {
    "apple": {"price": 0.5, "quantity": 100},
    "banana": {"price": 0.3, "quantity": 150},
    "milk": {"price": 1.2, "quantity": 50},
    "bread": {"price": 1.0, "quantity": 60},
    "eggs": {"price": 0.1, "quantity": 200}
}

# Function to add a product
def add_product():
    name = input("Enter product name: ").lower()
    if name in inventory:
        print("Product already exists.")
        return
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        if price <= 0 or quantity < 0:
            print("Price must be positive and quantity non-negative.")
            return
        inventory[name] = {"price": price, "quantity": quantity}
        print(f"{name} added successfully.")
    except ValueError:
        print("Invalid input. Price must be a number, quantity must be an integer.")

# Function to consult a product
def consult_product():
    name = input("Enter product name to consult: ").lower()
    if name in inventory:
        product = inventory[name]
        print(f"{name} - Price: ${product['price']}, Quantity: {product['quantity']}")
    else:
        print(f"{name} does not exist in the inventory.")

# Function to update the price of a product
def update_price():
    name = input("Enter product name to update price: ").lower()
    if name in inventory:
        try:
            new_price = float(input("Enter new price: "))
            if new_price > 0:
                inventory[name]['price'] = new_price
                print(f"Price of {name} updated to ${new_price}")
            else:
                print("Price must be a positive number.")
        except ValueError:
            print("Invalid input. Price must be a number.")
    else:
        print(f"{name} not found in inventory.")

# Function to delete a product
def delete_product():
    name = input("Enter product name to delete: ").lower()
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print(f"{name} does not exist in inventory.")

# Function to calculate total inventory value using lambda
def calculate_total_value():
    total = sum(map(lambda item: item['price'] * item['quantity'], inventory.values()))
    print(f"Total inventory value: ${total:.2f}")

# Main menu loop
def main():
    while True:
        print("\n=== Inventory Management ===")
        print("1. Add product to inventory")
        print("2. Consult product")
        print("3. Update product price")
        print("4. Delete product")
        print("5. Calculate total inventory value")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            consult_product()
        elif choice == '3':
            update_price()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            calculate_total_value()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 6.")

# Start the program
main()
