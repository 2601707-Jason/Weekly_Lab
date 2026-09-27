INVENTORY_FILE = "inventory.txt"


def load_inventory():
    """Read saved orders from inventory.txt.
    If the file doesn't exist, start with an empty list and no error."""
    try:
        with open(INVENTORY_FILE, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return []

    orders = []
    for line in lines:
        if not line.strip():
            continue
        order_id, product, quantity = line.split(",")
        orders.append({
            "id": int(order_id),
            "product": product,
            "quantity": int(quantity)
        })
    return orders


def save_inventory(orders):
    """Write every order back to inventory.txt, one per line."""
    with open(INVENTORY_FILE, "w") as f:
        for order in orders:
            f.write(f"{order['id']},{order['product']},{order['quantity']}\n")
    print("Order successfully saved to inventory.txt")


def display_current_orders(orders):
    print("Current Orders:")
    if not orders:
        print("  (No previous orders found)")
    else:
        for order in orders:
            print(f"  {order['id']}, {order['product']}, {order['quantity']}")
    print("-" * 40)


def get_valid_quantity():
    failed_attempts = 0
    while True:
        user_input = input("Enter Quantity: ")
        if not user_input.isdigit():
            print("Please enter a valid non-negative integer")
            failed_attempts += 1
            continue
        return int(user_input), failed_attempts


def generate_report(total_units, failed_attempts, total_transactions):
    print("\n=== Audit Report ===")
    print(f"Total Transactions Recorded: {total_transactions}")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    orders = load_inventory()
    display_current_orders(orders)

    next_id = max((order["id"] for order in orders), default=1000) + 1
    total_units = sum(order["quantity"] for order in orders)
    failed_attempts = 0

    while True:
        product_name = input("Enter Product Name (or 'quit' to exit): ")
        if product_name.lower() == "quit":
            break

        quantity, failed = get_valid_quantity()
        failed_attempts += failed

        order = {"id": next_id, "product": product_name, "quantity": quantity}
        orders.append(order)
        total_units += quantity

        print("\nNew Order Added:")
        print(f"{order['id']}, {order['product']}, {order['quantity']}")
        next_id += 1

    save_inventory(orders)
    generate_report(total_units, failed_attempts, len(orders))


if __name__ == "__main__":
    main()