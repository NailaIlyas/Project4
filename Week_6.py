# Constants
TICKET_PRICES = {
    "one_day": {
        "adult": 20.00,
        "child": 12.00,
        "senior": 16.00,
        "family": 60.00,
        "group": 15.00
    },
    "two_days": {
        "adult": 30.00,
        "child": 18.00,
        "senior": 24.00,
        "family": 90.00,
        "group": 22.50
    },
    "extra_attractions": {
        "lion_feeding": 2.50,
        "penguin_feeding": 2.00,
        "evening_barbecue": 5.00
    }
}


# Function to display ticket options and extra attractions
def display_options():
    print("Ticket Options:")
    print("One-Day Tickets:")
    for ticket_type, price in TICKET_PRICES["one_day"].items():
        print(f"{ticket_type.capitalize()}: ${price:.2f}")
    print("\nTwo-Day Tickets:")
    for ticket_type, price in TICKET_PRICES["two_days"].items():
        print(f"{ticket_type.capitalize()}: ${price:.2f}")

    print("\nExtra Attractions:")
    for attraction, price in TICKET_PRICES["extra_attractions"].items():
        print(f"{attraction.replace('_', ' ').title()}: ${price:.2f}")


# Function to process a booking
def process_booking():
    total_cost = 0
    booking_number = generate_booking_number()

    print("\nEnter the number of tickets required for each type:")
    for ticket_type in TICKET_PRICES["one_day"]:
        quantity = int(input(f"Number of {ticket_type.capitalize()} tickets: "))
        total_cost += TICKET_PRICES["one_day"][ticket_type] * quantity

    for ticket_type in TICKET_PRICES["two_days"]:
        quantity = int(input(f"Number of {ticket_type.capitalize()} tickets: "))
        total_cost += TICKET_PRICES["two_days"][ticket_type] * quantity * 2

    extra_attractions_cost = 0
    while True:
        attraction = input("\nEnter the extra attraction you want to add (leave blank to finish): ").strip().lower()
        if not attraction:
            break
        if attraction in TICKET_PRICES["extra_attractions"]:
            extra_attractions_cost += TICKET_PRICES["extra_attractions"][attraction]
        else:
            print("Invalid extra attraction.")

    total_cost += extra_attractions_cost

    print(f"\nTotal cost: ${total_cost:.2f}")
    print(f"Booking number: {booking_number}")


# Function to generate a unique booking number
def generate_booking_number():
    # This is a simple method for generating a unique booking number
    # In a real-world scenario, you would use a more robust method such as UUID
    global booking_counter
    booking_counter += 1
    return f"BK{booking_counter:04d}"


# Main function
def main():
    print("Welcome to Wildlife Park Ticket Booking System")
    while True:
        print("\nTASK 1: Display Ticket Options and Extra Attractions")
        display_options()

        print("\nTASK 2: Process a Booking")
        process_booking()

        another_booking = input("\nDo you want to make another booking? (yes/no): ").strip().lower()
        if another_booking != 'yes':
            break


# Global variable to keep track of booking numbers
booking_counter = 0

if __name__ == "__main__":
    main()
