def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }

    inventory.append(item)
    print(f"{name} has been added to the inventory.")

def update_item():
    name = input("Enter the name of the item to update: ")
    for item in inventory:
        if item['name'] == name:
            print("Item found. Enter new details:")
            item['price'] = float(input("Enter new price: "))
            item['quantity'] = int(input("Enter new quantity: "))
            item['category'] = input("Enter new category: ")
            print(f"{name} has been updated.")
            return
    print("Item not found.")

def view_inventory():
    if not inventory:
        print("The inventory is empty.")
    else:
        print("\nInventory:")
        for item in inventory:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")
        print()

def remove_item():
    name = input("Enter the name of the item to remove: ")
    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            print(f"{name} has been removed from the inventory.")
            return
    print("Item not found.")


def search_by_category():
    category = input("Enter the category to search: ")
    found_items = [item for item in inventory if item['category'] == category]

    if found_items:
        print(f"Items in category '{category}':")
        for item in found_items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
    else:
        print(f"No items found in category '{category}'.")


def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            search_by_category()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the main loop
if __name__ == "__main__":
    main()
