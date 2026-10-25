from inventory import Inventory

def validate_product_id(product_id: str, inventory: Inventory) -> int:
    product_id = product_id.strip()
    if not product_id:
        raise ValueError("Product ID can't be empty")

    try:
        product_id = int(product_id)
    except ValueError:
        raise ValueError("Product ID must be a whole number")

    if product_id <= 0:
        raise ValueError("Product ID must be a positive number")

    if inventory.has_product(product_id):
        raise ValueError(f"{product_id} already exists!")

    return product_id

def validate_product_name(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("Product name can't be empty")
    return name

def validate_product_price(price: str) -> float:
    try:
        value = float(price)
    except ValueError:
        raise ValueError("Price must be a number, e.g. 9.99")
    if value <= 0:
        raise ValueError("Price must be greater than 0")
    return value

def validate_product_stock(stock: str) -> int:
    if not stock.isdecimal():
        raise ValueError("Stock must be a whole number")
    return int(stock)

def validate_stock_change(stock: str) -> int:
    try:
        value = int(stock)
        
    except ValueError:
        raise ValueError("Enter a whole number, e.g. 10 or -3")
    
    if value == 0:
        raise ValueError("Value can't be 0")
    return value

def validate_options(option: str, max_option: int) -> int:
    if not option.isdecimal():
        raise ValueError("Not a correct format!")
    
    value = int(option)
    if not 1 <= value <= max_option:
        raise ValueError(f"Choose a number between 1 and {max_option}")
    return value

def ask(prompt, validator, *args):
    while True:
        try:
            return validator(input(prompt), *args)
        except ValueError as e:
            print(e)