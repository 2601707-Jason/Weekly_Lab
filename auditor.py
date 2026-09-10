inventory = 0
failed_entries = 0
while inventory < 500:
    user_input = input("Enter a stock quantity or Enter quit to stop:")
    if user_input.lower() == "quit":
        break
    if not user_input.isdigit():
        print("Please enter a valid non-negative integer")
        failed_entries += 1
        continue
    inventory += int(user_input)
    if inventory > 500:
        print("Overstock Alert: Inventory exceeded 500 units!")
        break
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed Entries: {failed_entries}")