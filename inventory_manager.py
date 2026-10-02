# b. After load_inventory() is working.
# c. After the final save_inventory() is verified.

import json


def display_main_menu():
    print(f"{'-' * 6} MENU {'-' * 6}")
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
    print(f"{'-' * 6} MENU {'-' * 6}")


def display_all_products(inventory):
    print("Current Inventory")
    print("-" * 50)
    for product in inventory:
        print(
            f"ID: {product["ID"]} | Name: {product["Name"]} | Price: ${product["Price"]:.2f} | Stock: {product["Stock"]}"
        )
    print("-" * 50)


def load_inventory(file):
    try:
        with open(file, mode="r", encoding="utf-8") as file:
            inventory = json.load(file)
        print("inventory.json found.")
        print("inventory loaded successfully")
        return inventory
    
    except FileNotFoundError:
        print("inventory.json not found. Starting with an empty inventory.")
        return []


def ask(prompt, parse):
    while True:
        text = input(prompt).strip()
        try:
            return parse(text)
        except ValueError as e:
            print(e)


def parse_non_empty(text):
    if not text:
        raise ValueError("This cannot be empty")
    return text


def parse_price(text):
    try:
        price = float(text)
    except ValueError:
        raise ValueError("Please enter a number e.g. 299.99")
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    return price


def parse_stock(text):
    if not text.isdigit():
        raise ValueError("Please enter a whole number (0 or more).")
    return int(text)


def parse_option(text):
    if not text.isdigit() or not 1 <= int(text) <= 6:
        raise ValueError("Please enter a valid option")
    return int(text)


def parse_product_id(text, inventory):
    if not text:
        raise ValueError("This cannot be empty")
    if any(item["ID"] == text for item in inventory):
        raise ValueError(f"{text} already exists")
    return text


def add_product(inventory: list):
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

    print("Product added successfully!")
    return


def main():
    print("=" * 20)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 20)
    
    inventory = load_inventory("inventory.json")
    
    # inventory = [
    #     {"ID": "P001", "Name": "Laptop", "Price": 1200, "Stock": 15},
    #     {"ID": "P002", "Name": "Mouse", "Price": 25.20, "Stock": 40},
    #     {"ID": "P003", "Name": "Keyboard", "Price": 45.00, "Stock": 25},
    # ]

    actions = {1: display_all_products, 2: add_product}

    display_main_menu()

    while True:

        option = ask("Enter option: ", parse_option)
        actions[option](inventory)


main()
