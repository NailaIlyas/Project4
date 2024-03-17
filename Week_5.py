# Constants
PRICE_TABLE = {
    "Sunday": {"max_hours": 8, "price_day": 2.00, "price_night": 2.00},
    "Monday": {"max_hours": 2, "price_day": 10.00, "price_night": 2.00},
    "Tuesday": {"max_hours": 2, "price_day": 10.00, "price_night": 2.00},
    "Wednesday": {"max_hours": 2, "price_day": 10.00, "price_night": 2.00},
    "Thursday": {"max_hours": 2, "price_day": 10.00, "price_night": 2.00},
    "Friday": {"max_hours": 2, "price_day": 10.00, "price_night": 2.00},
    "Saturday": {"max_hours": 4, "price_day": 3.00, "price_night": 2.00}
}


# Function to calculate parking fee
def calculate_parking_fee(day, arrival_time, hours_parked, frequent_parking_number):
    if arrival_time < 8 or arrival_time >= 24:
        print("Parking is not allowed between Midnight and 08:00.")
        return None

    price_table = PRICE_TABLE[day]
    max_hours = price_table["max_hours"]
    price_per_hour = price_table["price_day"] if 8 <= arrival_time < 16 else price_table["price_night"]

    if hours_parked > max_hours:
        print(f"Maximum parking duration exceeded. Max hours allowed: {max_hours}")
        return None

    if frequent_parking_number == "12345":  # Example frequent parking number
        price_per_hour *= 0.9  # Apply 10% discount

    total_price = price_per_hour * hours_parked
    return total_price


# Main function
def main():
    day = input("Enter the day of the week: ").capitalize()
    arrival_time = int(input("Enter the arrival time (24-hour format, e.g., 13 for 1 PM): "))
    hours_parked = int(input("Enter the number of hours parked: "))
    frequent_parking_number = input("Enter your frequent parking number (leave blank if none): ")

    parking_fee = calculate_parking_fee(day, arrival_time, hours_parked, frequent_parking_number)
    if parking_fee is not None:
        print(f"Total parking fee: ${parking_fee:.2f}")


if __name__ == "__main__":
    main()
