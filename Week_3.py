# Constants
DAYS_IN_WEEK = 7
MINIMUM_YIELD_THRESHOLD = 12
MINIMUM_DAYS_FOR_LOW_YIELD = 4


# Function to record yield for each cow
def record_yield(herd):
    for cow_id, yield_record in herd.items():
        print(f"Recording yield for cow {cow_id}:")
        for day in range(1, DAYS_IN_WEEK + 1):
            yield_amount = float(input(f"Enter yield for Day {day} (litres): "))
            yield_record.append(yield_amount)


# Function to calculate total weekly volume and average yield per cow
def calculate_statistics(herd):
    total_volume = 0
    total_cows = len(herd)

    for cow_id, yield_record in herd.items():
        total_volume += sum(yield_record)
        average_yield = sum(yield_record) / DAYS_IN_WEEK
        print(f"Cow {cow_id}: Total Yield - {sum(yield_record)} litres, Average Yield - {average_yield:.1f} litres")

    print(f"\nTotal Weekly Volume of Milk for the Herd: {total_volume} litres")
    print(f"Average Yield Per Cow in a Week: {total_volume / total_cows:.1f} litres")


# Function to identify the most productive cow and cows with low volume of milk
def identify_cows(herd):
    max_yield_cow = None
    max_yield = 0
    low_yield_cows = []

    for cow_id, yield_record in herd.items():
        total_yield = sum(yield_record)
        if total_yield > max_yield:
            max_yield = total_yield
            max_yield_cow = cow_id

        if yield_record.count(0) >= MINIMUM_DAYS_FOR_LOW_YIELD:
            low_yield_cows.append(cow_id)

    print(f"\nMost Productive Cow of the Week: Cow {max_yield_cow} with {max_yield} litres")

    if low_yield_cows:
        print(f"Cows with a Yield of Less than {MINIMUM_YIELD_THRESHOLD} litres for Four or More Days:")
        for cow_id in low_yield_cows:
            print(f"Cow {cow_id}")


# Task 1
def task_1():
    herd = {}
    herd_size = int(input("Enter the number of cows in the herd: "))

    for i in range(1, herd_size + 1):
        cow_id = input(f"Enter the 3-digit identity code for cow {i}: ")
        herd[cow_id] = []

    record_yield(herd)
    return herd


# Task 2
def task_2(herd):
    calculate_statistics(herd)


# Task 3
def task_3(herd):
    identify_cows(herd)


# Main function
def main():
    print("TASK 1:")
    herd = task_1()

    print("\nTASK 2:")
    task_2(herd)

    print("\nTASK 3:")
    task_3(herd)


if __name__ == "__main__":
    main()
