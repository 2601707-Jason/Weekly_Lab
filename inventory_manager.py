import json
from validators import (
    ask,
    parse_non_empty,
    parse_price,
    parse_stock,
    parse_option,
    parse_product_id,
)

INVENTORY_FILE = "inventory.json"


def display_main_menu():
    print(f"{'-' * 10} MENU {'-' * 10}")
    menu = [
        "Display All Products",
        "Add Product",
        "Update Stock",
        "Search Product",
        "Save Inventory",
        "Exit",
    ]
    for i, m in enumerate(menu, start=1):
        print(f"{i}. {m}")
    print("-" * 26)
    print()


def load_inventory(file=INVENTORY_FILE):
    try:
        with open(file, mode="r", encoding="utf-8") as f:
            inventory = json.load(f)
        print("inventory.json found.")
        print("inventory loaded successfully.")
        print()

        return inventory

    except FileNotFoundError:
        print("inventory.json not found. Starting with an empty inventory.")
        return []


def save_inventory(inventory, file=INVENTORY_FILE):
    with open(file, mode="w") as f:
        json.dump(inventory, f, indent=4)
    print("Inventory saved successfully to inventory.json")


def display_all_products(inventory):
    print()
    print("Current Inventory")
    print("-" * 50)
    for product in inventory:
        print(
            f"ID: {product['ID']} | Name: {product['Name']} | Price: ${product['Price']:.2f} | Stock: {product['Stock']}"
        )
    print("-" * 50)
    print()


def add_product(inventory):
    print()
    product_id = ask("Product ID: ", lambda t: parse_product_id(t, inventory))
    product_name = ask("Produt Name: ", parse_non_empty)
    product_price = ask("Price: ", parse_price)
    product_stock = ask("Stock Quantity: ", parse_stock)

    new_product = {
        "ID": product_id,
        "Name": product_name,
        "Price": product_price,
        "Stock": product_stock,
    }
    inventory.append(new_product)
    print()
    print("Product added successfully!")


def update_stock(inventory):
    print()
    print("Update Stock")
    product_id = ask("Enter Product ID: ", parse_non_empty)
    print()

    found = None

    for product in inventory:
        if product["ID"] == product_id:
            found = product
            break

    if found is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {found['Name']}")
    print(f"Current Stock: {found['Stock']}")
    print()

    updated_stock = ask("New Stock Quantity: ", parse_stock)
    found["Stock"] = updated_stock
    print()
    print("Stock updated successfully")


def search_product(inventory):
    print()
    print("Search Product")
    product_id = ask("Enter Product ID: ", parse_non_empty)
    print()

    found = None

    for product in inventory:
        if product["ID"] == product_id:
            found = product

    if found is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 50)

    print(f"ID: {found['ID']}")
    print(f"Name: {found['Name']}")
    print(f"Price: {found['Price']}")
    print(f"Stock: {found['Stock']}")

    print("-" * 50)
    print()


def exit_program(inventory):
    print("Saving inventory before exit...")
    save_inventory(inventory)

    print()
    print("Thank you for using Inventory Management System.")
    print("Program Terminated")


def main():
    print("=" * 45)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 45)

    print()

    inventory = load_inventory()

    actions = {
        1: display_all_products,
        2: add_product,
        3: update_stock,
        4: search_product,
        5: save_inventory,
        6: exit_program,
    }

    display_main_menu()

    while True:

        option = ask(f"Enter option: ({1} - {len(actions)}): ", parse_option)
        actions[option](inventory)

        if option == 6:
            break


if __name__ == "__main__":
    main()
