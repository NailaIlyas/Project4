# Constants
MINIMUM_ITEMS_IN_AUCTION = 10
AUCTION_FEE_PERCENTAGE = 0.1


# Function to set up the auction
def auction_setup():
    auction_items = {}
    num_items = int(input("Enter the number of items in the auction (at least 10): "))
    if num_items < MINIMUM_ITEMS_IN_AUCTION:
        print("Error: Minimum 10 items required for the auction.")
        return None

    for i in range(1, num_items + 1):
        item_number = input(f"Enter item number for item {i}: ")
        description = input(f"Enter description for item {i}: ")
        reserve_price = float(input(f"Enter reserve price for item {i}: $"))
        auction_items[item_number] = {"description": description, "reserve_price": reserve_price, "number_of_bids": 0}

    return auction_items


# Function for buyers to place bids
def place_bid(auction_items):
    item_number = input("Enter the item number you want to bid for: ")
    if item_number not in auction_items:
        print("Error: Item not found in the auction.")
        return

    print(f"Item Number: {item_number}")
    print(f"Description: {auction_items[item_number]['description']}")
    print(f"Current Highest Bid: ${auction_items[item_number]['reserve_price']:.2f}")

    buyer_number = input("Enter your buyer number: ")
    bid_amount = float(input("Enter your bid amount: $"))

    if bid_amount <= auction_items[item_number]['reserve_price']:
        print("Error: Bid amount must be higher than the current highest bid.")
        return

    auction_items[item_number]['reserve_price'] = bid_amount
    auction_items[item_number]['number_of_bids'] += 1
    print("Bid placed successfully.")


# Function to process the end of the auction
def end_auction(auction_items):
    total_fee = 0
    sold_items = 0
    items_below_reserve = 0
    items_with_no_bids = 0

    print("\nResults of the Auction:")
    for item_number, details in auction_items.items():
        if details['reserve_price'] > details['reserve_price']:
            total_fee += AUCTION_FEE_PERCENTAGE * details['reserve_price']
            sold_items += 1
            print(f"Item {item_number} - Final Bid: ${details['reserve_price']:.2f}")
        else:
            items_below_reserve += 1
            print(f"Item {item_number} - Final Bid: Did not meet reserve price")

        if details['number_of_bids'] == 0:
            items_with_no_bids += 1

    print(f"\nTotal Auction Fees: ${total_fee:.2f}")
    print(f"Number of Items Sold: {sold_items}")
    print(f"Number of Items Below Reserve: {items_below_reserve}")
    print(f"Number of Items with No Bids: {items_with_no_bids}")


# Main function
def main():
    print("TASK 1: Auction Set Up")
    auction_items = auction_setup()
    if auction_items is None:
        return

    print("\nTASK 2: Buyer Bids")
    while True:
        place_bid(auction_items)
        another_bid = input("Do you want to place another bid? (yes/no): ").lower()
        if another_bid != 'yes':
            break

    print("\nTASK 3: End of Auction")
    end_auction(auction_items)


if __name__ == "__main__":
    main()
