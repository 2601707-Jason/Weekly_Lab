import json
from product import Product
from inventory import Inventory
from file import File
from validators import (
    ask,
    validate_product_id,
    validate_product_name,
    validate_product_price,
    validate_product_stock,
    validate_stock_change,
    validate_options,
)

MENU = [
    "Display All Products",
    "Add Product",
    "Update Stock",
    "Search Product",
    "Save Inventory",
    "Exit",
]


def display_main_menu():
    print()
    print(f"{'-' * 10} MENU {'-' * 10}")
    for i, m in enumerate(MENU, start=1):
        print(f"{i}. {m}")
    print("-" * 26)
    print()


def display_inventory(inventory: Inventory):
    print("Current Inventory")
    print("-" * 50)
    inventory.display_all_products()
    print("-" * 50)


def add_product(inventory: Inventory):
    print("Add New Product")
    product_id = ask("Enter Product ID: ", validate_product_id, inventory)
    name = ask("Enter Product Name: ", validate_product_name)
    price = ask("Enter Product Price: ", validate_product_price)
    stock = ask("Enter Product Stock: ", validate_product_stock)
    inventory.add_product(Product(product_id, name, price, stock))
    print("Product added successfully!")


def update_product(inventory: Inventory):
    print("Update Stock")
    product_id = int(input("Enter Product ID: ").strip())
    product = inventory.search_product(product_id)
    if product is None:
        print(f"No product found with ID {product_id}")
        return

    print("Product Found:")
    product.display_information()
    change = ask("Stock change (e.g. 10 or -3): ", validate_stock_change)
    try:
        product.update_stock(change)
    except ValueError as e:
        print(e)
        return
    print("Stock updated successfully")


def search_product(inventory: Inventory):
    print("Search Product")
    product_id = int(input("Enter Product ID: ").strip())
    product = inventory.search_product(product_id)
    if product is None:
        print(f"No product found with ID {product_id}")
        return

    print("Product Found")
    print("-" * 50)
    product.display_information()
    print("-" * 50)


def save_inventory(file, inventory: Inventory):
    file.save_inventory(inventory.to_dict())
    print("Inventory saved successfully")


def exit_program(file, inventory):
    print("Saving inventory before exit...")
    save_inventory(file, inventory)
    print("Thank you for using Inventory Management System")

def load_products(file: File) -> list[Product]:
    if not file.exists():
        print("inventory.json not found. Starting with an empty inventory.")
        return []
    try:
        products = [Product.from_dict(p) for p in file.load_inventory()]
    except json.JSONDecodeError:
        print("inventory.json is empty or corrupted. Starting with an empty inventory.")
        return []
    print("inventory.json loaded successfully")
    return products

def main():
    print("=" * 45)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 45)

    print()

    file = File(file="inventory.json")
    inventory = Inventory(products=load_products(file))

    actions = {
        1: lambda: display_inventory(inventory),
        2: lambda: add_product(inventory),
        3: lambda: update_product(inventory),
        4: lambda: search_product(inventory),
        5: lambda: save_inventory(file, inventory),
    }
    
    while True:
        display_main_menu()
        option = ask(f"Enter option (1-{len(MENU)}): ", validate_options, len(MENU))

        if option == 6:
            exit_program(file, inventory)
            break
        actions[option]()


if __name__ == "__main__":
    main()
