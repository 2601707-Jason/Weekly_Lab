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
