def get_valid_input():
    failed_attempts = 0

    while True:            
        user_input = input("Enter a stock quantity or Enter quit to stop: ")
        if user_input.lower() == "quit":
            return "quit", failed_attempts
        
        if not user_input.isdigit():
            print("Please enter a valid non-negative integer")
            failed_attempts += 1
            continue

        return int(user_input), failed_attempts

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed Entries: {failed_attempts}")

def main():
    total_units = 0
    failed_attempts = 0

    while True:
        delivery, failed = get_valid_input()
        failed_attempts += failed

        if delivery == "quit":
            break

        total_units = process_delivery(total_units, delivery)
        tax = calculate_tax(delivery)
        print(f"Tax for this delivery: {tax}")
    generate_report(total_units, failed_attempts)

if __name__ == "__main__":
    main()


